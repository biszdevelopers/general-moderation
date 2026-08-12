"""Three-stage detection pipeline orchestration.

- Stage 1 exits clearly safe content through the safe word fast path.
- Stage 2 runs the rule detectors, semantic similarity, and the user profile
  to compute a 0-100 suspicion score.
- Stage 3 invokes the llama.cpp model only when the suspicion score, a high
  semantic similarity, or the user ratio crosses the per-app trigger policy.
"""

from __future__ import annotations

import logging
import time
from typing import Any

import mmh3

from app.ai.llama_detector import LlamaCppDetector
from app.appconfig.app_config_service import AppConfigService
from app.detectors.aho_detector import AhoCorasickDetector
from app.detectors.bktree_detector import BkTreeDetector
from app.detectors.bloom_detector import BloomFilterDetector
from app.detectors.interface import DetectorInterface
from app.detectors.metaphone_detector import MetaphoneDetector
from app.detectors.multi_language_detector import MultiLanguageDetector
from app.detectors.rolling_hash_detector import RollingHashDetector
from app.export.export_service import ExportService
from app.fastpath.safe_word_filter import SafeWordFilter
from app.feedback.feedback_service import FeedbackService
from app.models.request import BatchModerationRequest, ModerationRequest
from app.models.response import BatchModerationResponse, ModerationResponse
from app.models.verdict import DetectionResult, Verdict
from app.profiling.user_profiler import UserProfiler
from app.scoring.suspicion_scorer import SuspicionScorer
from app.semantic.semantic_service import SemanticService
from app.settings_service import SettingsService
from app.wordbank.manager import WordBankManager


class ModerationEngine:
    """Owns the detectors and produces moderation verdicts.

    :param settings: application settings
    :param word_bank: shared word bank manager
    :param logger: audit logger
    :param settings_service: optional runtime settings service
    :param app_config: optional per-application trigger policy service
    :param feedback_service: optional feedback and auto-tuning service
    """

    def __init__(
        self,
        settings: Any,
        word_bank: WordBankManager,
        logger: Any,
        settings_service: SettingsService | None = None,
        app_config: AppConfigService | None = None,
        feedback_service: FeedbackService | None = None,
    ) -> None:
        self._settings: Any = settings
        self._word_bank: WordBankManager = word_bank
        self._logger: Any = logger
        self._settings_service: SettingsService = settings_service or SettingsService(settings)
        self._app_config: AppConfigService = app_config or AppConfigService(
            settings.app_config_db_path
        )
        self._feedback: FeedbackService = feedback_service or FeedbackService(
            settings, self._settings_service, self._app_config, logger
        )
        self._profiler: UserProfiler = UserProfiler(
            settings.user_db_path,
            settings.user_archive_db_path,
            int(self._settings_service.get("USER_WINDOW_DAYS", settings.user_window_days)),
        )
        self._semantic: SemanticService = SemanticService(settings, logger)
        self._safe_word: SafeWordFilter = SafeWordFilter(settings, logger)
        self._scorer: SuspicionScorer = SuspicionScorer(self._settings_service)
        self._export: ExportService = ExportService(settings, logger)
        self._rolling_hash: RollingHashDetector = RollingHashDetector(
            cache_size=settings.spam_cache_size,
            ttl_seconds=settings.spam_cache_ttl_seconds,
        )
        self._llama: LlamaCppDetector = LlamaCppDetector(settings, logger)
        self._detectors: list[DetectorInterface] = self._build_detectors()
        self._metrics: dict[str, float] = {
            "requests_total": 0.0,
            "ai_requests_total": 0.0,
            "rate_limit_hits_total": 0.0,
            "stage1_fast_path_total": 0.0,
            "semantic_queries_total": 0.0,
        }
        self._detector_seconds: dict[str, float] = {}
        self._cache: dict[int, ModerationResponse] = {}
        self._cache_timestamps: dict[int, float] = {}
        self._cache_max_size: int = settings.cache_max_size
        self._cache_ttl: int = settings.cache_ttl_seconds

    def _build_detectors(self) -> list[DetectorInterface]:
        """Instantiate every detector in priority order.

        :return: the ordered detector list
        """
        return [
            BloomFilterDetector(self._word_bank),
            self._rolling_hash,
            AhoCorasickDetector(self._word_bank),
            BkTreeDetector(self._word_bank, self._settings.fuzzy_max_distance),
            MetaphoneDetector(self._word_bank),
            MultiLanguageDetector(self._settings, self._logger),
        ]

    def refresh_detectors(self) -> None:
        """Rebuild detector caches after the word bank is reloaded."""
        self.clear_cache()
        for detector in self._detectors:
            if detector.is_available():
                detector.reload()

    def warm_up_model(self) -> None:
        """Start the background model download-and-load."""
        self._llama.start_preload()

    def clear_cache(self) -> None:
        """Drop every cached moderation result."""
        self._cache.clear()
        self._cache_timestamps.clear()

    def _get_cache_key(self, text: str) -> int:
        """Compute the cache key for a message.

        :param text: message text
        :return: a 64-bit MurmurHash3 key
        """
        return mmh3.hash64(text)[0]

    def _get_cached(self, key: int) -> ModerationResponse | None:
        """Return a fresh cached response for the key, or None.

        Expired entries are evicted on access.

        :param key: message hash
        :return: the cached response or None
        """
        cached: ModerationResponse | None = self._cache.get(key)
        if cached is None:
            return None
        if time.monotonic() - self._cache_timestamps[key] > self._cache_ttl:
            del self._cache[key]
            del self._cache_timestamps[key]
            return None
        return cached

    def _set_cache(self, key: int, response: ModerationResponse) -> None:
        """Store a response, evicting the oldest entry when full.

        :param key: message hash
        :param response: the moderation response to cache
        """
        if len(self._cache) >= self._cache_max_size:
            oldest_key: int = min(self._cache_timestamps, key=self._cache_timestamps.get)
            del self._cache[oldest_key]
            del self._cache_timestamps[oldest_key]
        self._cache[key] = response
        self._cache_timestamps[key] = time.monotonic()

    def moderate(self, request: ModerationRequest) -> ModerationResponse:
        """Moderate a single message through the three-stage pipeline.

        :param request: the incoming moderation request
        :return: the moderation response
        """
        start_ns: int = time.perf_counter_ns()
        cache_key: int = self._get_cache_key(request.text)
        cached: ModerationResponse | None = self._get_cached(cache_key)
        if cached is not None:
            self._metrics["requests_total"] += 1.0
            self._metrics[f"requests_{cached.verdict.value.lower()}_total"] = (
                self._metrics.get(f"requests_{cached.verdict.value.lower()}_total", 0.0) + 1.0
            )
            latency_ms: float = (time.perf_counter_ns() - start_ns) / 1_000_000.0
            return self._restore_cached(request, cached, latency_ms)

        app_name: str = request.app_name or "default"
        verdict: Verdict = Verdict.PASS
        level_used: int = 1
        chain: list[str] = []
        reasons: list[str] = []
        matched_words: list[str] = []
        matched_language: str | None = None
        confidence: float | None = None
        suspicion_score: float = 0.0
        ai_triggered: bool = False

        if self._safe_word.is_available() and self._safe_word.is_safe(request.text):
            chain.append("safe_word_list")
            self._metrics["stage1_fast_path_total"] += 1.0
        else:
            (
                chain,
                reasons,
                matched_words,
                matched_language,
                confidence,
                verdict,
                matched_detectors,
            ) = self._run_level_one(request.text)

            semantic_similarities: dict[str, float] = {}
            if self._semantic.is_available():
                self._metrics["semantic_queries_total"] += 1.0
                semantic_similarities = self._semantic.query(request.text)

            user_ratio: float = 0.0
            if self._profiler is not None and request.user_id:
                user_ratio = self._profiler.get_ratio(app_name, request.user_id)

            suspicion_score = self._scorer.score(
                detector_names=matched_detectors,
                semantic_similarities=semantic_similarities,
                user_ratio=user_ratio,
            )

            ai_triggered, level_used, verdict, chain, reasons, confidence = (
                self._resolve_stage_three(
                    request.text,
                    app_name,
                    verdict,
                    chain,
                    reasons,
                    confidence,
                    suspicion_score,
                    semantic_similarities,
                    user_ratio,
                )
            )

        if verdict is Verdict.BLOCK:
            self._rolling_hash.record_hit(request.text)
        if self._profiler is not None and request.user_id:
            self._profiler.record(
                app_name=app_name,
                user_id=request.user_id,
                total_msgs=1,
                flagged_msgs=1 if (reasons or suspicion_score >= 50) else 0,
                blocked_msgs=1 if verdict is Verdict.BLOCK else 0,
            )
        self._feedback.record_decision(verdict.value, ai_triggered)

        matched_words = list(dict.fromkeys(matched_words))

        self._metrics["requests_total"] += 1.0
        self._metrics[f"requests_{verdict.value.lower()}_total"] = (
            self._metrics.get(f"requests_{verdict.value.lower()}_total", 0.0) + 1.0
        )

        latency_ms = (time.perf_counter_ns() - start_ns) / 1_000_000.0

        self._audit(
            request=request,
            verdict=verdict,
            level_used=level_used,
            reason=reasons[0] if reasons else None,
            matched_word=matched_words[0] if matched_words else None,
            matched_language=matched_language,
            confidence=confidence,
            latency_ms=latency_ms,
            chain=chain,
            suspicion_score=suspicion_score,
            ai_triggered=ai_triggered,
        )

        response: ModerationResponse = self._build_response(
            request.id,
            verdict,
            level_used,
            ai_triggered,
            suspicion_score,
            reasons,
            matched_words,
            matched_language,
            confidence,
            latency_ms,
            chain,
        )
        self._set_cache(cache_key, response)
        return response

    @staticmethod
    def _restore_cached(
        request: ModerationRequest, cached: ModerationResponse, latency_ms: float
    ) -> ModerationResponse:
        """Replay a cached response for a new request id.

        :param request: the incoming request
        :param cached: the stored response
        :param latency_ms: cache-hit latency
        :return: the response with the caller id applied
        """
        return ModerationResponse(
            id=request.id,
            verdict=cached.verdict,
            allowed=cached.allowed,
            level_used=cached.level_used,
            ai_triggered=cached.ai_triggered,
            suspicion_score=cached.suspicion_score,
            reasons=cached.reasons,
            reason=cached.reason,
            matched_words=cached.matched_words,
            matched_word=cached.matched_word,
            matched_language=cached.matched_language,
            confidence_score=cached.confidence_score,
            latency_ms=latency_ms,
            detector_chain=cached.detector_chain,
        )

    def _run_level_one(
        self, text: str
    ) -> tuple[list[str], list[str], list[str], str | None, float | None, Verdict, list[str]]:
        """Run the ordered Level 1 detectors over the text.

        :param text: normalized input text
        :return: chain, reasons, matched words, language, confidence, verdict,
            names of detectors that matched
        """
        chain: list[str] = []
        reasons: list[str] = []
        matched_words: list[str] = []
        matched_detectors: list[str] = []
        matched_language: str | None = None
        confidence: float | None = None
        verdict: Verdict = Verdict.PASS

        for detector in self._detectors:
            if not detector.is_available():
                continue
            chain.append(detector.name)
            detector_start: int = time.perf_counter_ns()
            result: DetectionResult = detector.detect(text)
            self._detector_seconds[detector.name] = (
                self._detector_seconds.get(detector.name, 0.0)
                + (time.perf_counter_ns() - detector_start) / 1_000_000_000.0
            )
            if not result.matched:
                continue
            matched_detectors.append(detector.name)
            reasons.append(result.reason or detector.name)
            matched_words.extend(result.matched_words)
            if result.matched_language and matched_language is None:
                matched_language = result.matched_language
            result_confidence: float | None = result.confidence_score
            if result_confidence is not None:
                confidence = (
                    result_confidence if confidence is None else max(confidence, result_confidence)
                )
            if detector.blocking:
                verdict = Verdict.BLOCK
                break

        if verdict is Verdict.PASS and reasons:
            verdict = Verdict.REVIEW
        return (
            chain,
            reasons,
            matched_words,
            matched_language,
            confidence,
            verdict,
            matched_detectors,
        )

    def _resolve_stage_three(
        self,
        text: str,
        app_name: str,
        verdict: Verdict,
        chain: list[str],
        reasons: list[str],
        confidence: float | None,
        suspicion_score: float,
        semantic_similarities: dict[str, float],
        user_ratio: float,
    ) -> tuple[bool, int, Verdict, list[str], list[str], float | None]:
        """Decide whether the LLM must settle the verdict.

        :param text: the original request text
        :param app_name: the calling application name
        :param verdict: the Stage 2 verdict
        :param chain: detector names that ran
        :param reasons: accumulated reasons
        :param confidence: accumulated confidence
        :param suspicion_score: the computed suspicion score
        :param semantic_similarities: per-category semantic similarities
        :param user_ratio: the user bad-content ratio
        :return: ai_triggered, level_used, final verdict, chain, reasons, confidence
        """
        policy: dict[str, Any] = self._app_config.get(app_name)
        score_trigger: bool = suspicion_score > int(policy["score_threshold"])
        force_semantic: bool = bool(policy["semantic_boost"]) and bool(
            semantic_similarities
            and max(semantic_similarities.values())
            >= float(self._settings_service.get("SEMANTIC_FORCE_LLM_THRESHOLD", 0.90))
        )
        force_user: bool = bool(policy["user_ratio_boost"]) and user_ratio >= float(
            self._settings_service.get("USER_RATIO_THRESHOLD", 0.3)
        )
        if policy["logic_type"] == "and":
            trigger: bool = score_trigger and force_semantic and force_user
        else:
            trigger = score_trigger or force_semantic or force_user

        if not trigger:
            final_verdict: Verdict = verdict if verdict is Verdict.BLOCK else Verdict.PASS
            return False, 1, final_verdict, chain, reasons, confidence

        if not self._llama.is_available():
            return False, 2, Verdict.REVIEW, chain, reasons, confidence

        chain.append(self._llama.name)
        self._metrics["ai_requests_total"] += 1.0
        llm_result: DetectionResult = self._llama.detect(text)
        if llm_result.matched:
            reasons.append(llm_result.reason or self._llama.name)
            confidence = llm_result.confidence_score or confidence
            return True, 2, Verdict.BLOCK, chain, reasons, confidence
        return True, 2, Verdict.PASS, chain, reasons, confidence

    def _build_response(
        self,
        request_id: str | None,
        verdict: Verdict,
        level_used: int,
        ai_triggered: bool,
        suspicion_score: float,
        reasons: list[str],
        matched_words: list[str],
        matched_language: str | None,
        confidence: float | None,
        latency_ms: float,
        chain: list[str],
    ) -> ModerationResponse:
        """Assemble the final response DTO.

        :param request_id: caller-supplied identifier
        :param verdict: the final verdict
        :param level_used: detection level that decided
        :param ai_triggered: whether the LLM ran
        :param suspicion_score: the 0-100 suspicion score
        :param reasons: accumulated reasons
        :param matched_words: matched words
        :param matched_language: matched language, if any
        :param confidence: overall confidence, if any
        :param latency_ms: total latency
        :param chain: detector chain
        :return: the response model
        """
        return ModerationResponse(
            id=request_id,
            verdict=verdict,
            allowed=verdict is not Verdict.BLOCK,
            level_used=level_used,
            ai_triggered=ai_triggered,
            suspicion_score=suspicion_score,
            reasons=reasons,
            reason=reasons[0] if reasons else None,
            matched_words=matched_words,
            matched_word=matched_words[0] if matched_words else None,
            matched_language=matched_language,
            confidence_score=confidence,
            latency_ms=latency_ms,
            detector_chain=chain,
        )

    def moderate_batch(self, batch: BatchModerationRequest) -> BatchModerationResponse:
        """Moderate a batch of messages.

        :param batch: the incoming batch request
        :return: per-item responses plus the total batch latency
        """
        start_ns: int = time.perf_counter_ns()
        results: list[ModerationResponse] = [
            self.moderate(
                ModerationRequest(
                    id=item.id,
                    app_name=item.app_name,
                    user_id=item.user_id,
                    text=item.text,
                )
            )
            for item in batch.items
        ]
        total_latency_ms: float = (time.perf_counter_ns() - start_ns) / 1_000_000.0
        return BatchModerationResponse(results=results, total_latency_ms=total_latency_ms)

    def shutdown(self) -> None:
        """Release models, storage, and logger resources."""
        self._llama.shutdown()
        self._word_bank.close()
        self._logger.close()
        self._profiler.close()
        self._settings_service.close()
        self._app_config.close()
        self._feedback.close()

    def _audit(
        self,
        *,
        request: ModerationRequest,
        verdict: Verdict,
        level_used: int,
        reason: str | None,
        matched_word: str | None,
        matched_language: str | None,
        confidence: float | None,
        latency_ms: float,
        chain: list[str],
        suspicion_score: float,
        ai_triggered: bool,
    ) -> None:
        """Emit the structured audit record for one decision.

        :param request: the moderated request
        :param verdict: the final verdict
        :param level_used: detection level that decided
        :param reason: primary reason, if any
        :param matched_word: primary matched word, if any
        :param matched_language: matched language, if any
        :param confidence: overall confidence, if any
        :param latency_ms: processing time in milliseconds
        :param chain: ordered detector names that ran
        :param suspicion_score: the computed suspicion score
        :param ai_triggered: whether the LLM ran
        """
        self._logger.log_moderation(
            request_id=request.id,
            user_id=request.user_id,
            text=request.text,
            verdict=verdict.value,
            level_used=level_used,
            reason=reason,
            matched_word=matched_word,
            matched_language=matched_language,
            confidence_score=confidence,
            latency_ms=latency_ms,
            detector_chain=chain,
            suspicion_score=suspicion_score,
            ai_triggered=ai_triggered,
        )

    def record_rate_limit_hit(self) -> None:
        """Increment the rate limit violation counter."""
        self._metrics["rate_limit_hits_total"] += 1.0

    def metrics(self) -> dict[str, float]:
        """Return a snapshot of the runtime counters.

        :return: counter values keyed by metric name
        """
        combined: dict[str, float] = dict(self._metrics)
        for detector_name, seconds in self._detector_seconds.items():
            combined[f"detector_{detector_name}_seconds_total"] = seconds
        return combined

    def log(self, message: str, **fields: Any) -> None:
        """Emit a structured log record through the shared logger.

        :param message: log message
        :param fields: structured fields
        """
        self._logger.log(logging.INFO, message, **fields)
