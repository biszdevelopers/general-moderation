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
from collections.abc import Callable
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
from app.detectors.phrase_detector import PhraseDetector
from app.detectors.rolling_hash_detector import RollingHashDetector
from app.detectors.sensitive_stop_words_detector import SensitiveStopWordsDetector
from app.export.export_service import ExportService
from app.fastpath.safe_word_filter import SafeWordFilter
from app.feedback.feedback_service import FeedbackService
from app.models.request import BatchModerationRequest, ModerationRequest
from app.models.response import BatchModerationResponse, ModerationResponse
from app.models.verdict import DetectionResult, Verdict
from app.phrases.manager import CriticalPhraseManager
from app.profiling.user_profiler import UserProfiler
from app.scoring.suspicion_scorer import SuspicionScorer
from app.semantic.semantic_service import SemanticService
from app.settings_service import SettingsService
from app.test.pipeline_trace import (
    DetectorRunTrace,
    PipelineTrace,
    Stage1Trace,
    Stage2Trace,
    Stage3Trace,
    WeightContribution,
)
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
        self._safe_word: SafeWordFilter = SafeWordFilter(
            settings,
            logger,
            blocked_terms=lambda: (
                set(self._word_bank.snapshot.custom_words)
                | {phrase.phrase for phrase in self._phrases.list_all()}
            ),
        )
        self._scorer: SuspicionScorer = SuspicionScorer(self._settings_service)
        self._phrases: CriticalPhraseManager = CriticalPhraseManager(
            settings.critical_phrases_db_path
        )
        self._export: ExportService = ExportService(settings, logger)
        self._rolling_hash: RollingHashDetector = RollingHashDetector(
            cache_size=settings.spam_cache_size,
            ttl_seconds=settings.spam_cache_ttl_seconds,
        )
        self._llama: LlamaCppDetector = LlamaCppDetector(settings, logger)
        self._sync_runtime_detectors()
        self._detectors: list[DetectorInterface] = self._build_detectors()
        self._metrics: dict[str, float] = {
            "requests_total": 0.0,
            "ai_requests_total": 0.0,
            "rate_limit_hits_total": 0.0,
            "stage1_fast_path_total": 0.0,
            "semantic_queries_total": 0.0,
            "model_unavailable_total": 0.0,
        }
        self._detector_seconds: dict[str, float] = {}
        self._cache: dict[int, ModerationResponse] = {}
        self._cache_timestamps: dict[int, float] = {}
        self._cache_fingerprints: dict[int, int] = {}
        self._cache_max_size: int = settings.cache_max_size
        self._cache_ttl: int = settings.cache_ttl_seconds

    def _sync_runtime_detectors(self) -> None:
        """Apply runtime settings that the detectors read at construction.

        Re-runs on every reload so admin edits take effect without a restart:
        - multi-language package hits downgrade to REVIEW in review mode.
        """
        for detector in getattr(self, "_detectors", []):
            if isinstance(detector, MultiLanguageDetector):
                detector.set_review_mode(bool(self._settings_service.get("ML_REVIEW_MODE", False)))

    def _build_detectors(self) -> list[DetectorInterface]:
        """Instantiate every detector in priority order.

        :return: the ordered detector list
        """
        detectors: list[DetectorInterface] = [
            SensitiveStopWordsDetector(self._settings, self._settings_service, self._logger),
            BloomFilterDetector(self._word_bank),
            self._rolling_hash,
            AhoCorasickDetector(self._word_bank),
            BkTreeDetector(self._word_bank, self._settings.fuzzy_max_distance),
            MetaphoneDetector(self._word_bank),
            MultiLanguageDetector(self._settings, self._logger),
        ]
        if bool(self._settings_service.get("ENABLE_PHRASE_DETECTOR", True)):
            detectors.append(PhraseDetector(self._phrases))
        return detectors

    def refresh_detectors(self) -> None:
        """Rebuild detector caches after the word bank is reloaded."""
        self.clear_cache()
        self._sync_runtime_detectors()
        self._phrases.reload()
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
        self._cache_fingerprints.clear()

    def _config_fingerprint(self) -> int:
        """Hash the runtime settings that influence verdicts.

        Cached responses are invalidated when this value changes, so tuning a
        weight or threshold applies immediately instead of after the TTL.

        :return: a 64-bit MurmurHash3 key
        """
        keys: tuple[str, ...] = (
            "SEVERITY_HARD_BLOCK_THRESHOLD",
            "REVIEW_ESCALATION_THRESHOLD",
            "SEMANTIC_ENABLED",
            "SEMANTIC_SIMILARITY_THRESHOLD",
            "SEMANTIC_FORCE_LLM_THRESHOLD",
            "USER_RATIO_THRESHOLD",
            "USER_PROFILING_ENABLED",
            "AI_TARGET_PERCENTAGE",
            "WEIGHT_USER",
            "ML_REVIEW_MODE",
            "ENABLE_PHRASE_DETECTOR",
            "WEIGHT_DETECTOR_AHO",
            "WEIGHT_DETECTOR_BADWORDS",
            "WEIGHT_DETECTOR_PROFANITE",
            "WEIGHT_DETECTOR_GLIN",
            "WEIGHT_DETECTOR_BKTREE",
            "WEIGHT_DETECTOR_METAPHONE",
        )
        values: tuple[object, ...] = tuple(self._settings_service.get(key, None) for key in keys)
        return mmh3.hash64(repr(values))[0]

    def _get_cache_key(self, text: str) -> int:
        """Compute the cache key for a message.

        :param text: message text
        :return: a 64-bit MurmurHash3 key
        """
        return mmh3.hash64(text)[0]

    def _get_cached(self, key: int) -> ModerationResponse | None:
        """Return a fresh cached response for the key, or None.

        Expired entries are evicted on access, as are entries whose config
        fingerprint no longer matches (i.e. a runtime setting changed).

        :param key: message hash
        :return: the cached response or None
        """
        cached: ModerationResponse | None = self._cache.get(key)
        if cached is None:
            return None
        if time.monotonic() - self._cache_timestamps[key] > self._cache_ttl:
            del self._cache[key]
            del self._cache_timestamps[key]
            del self._cache_fingerprints[key]
            return None
        if self._cache_fingerprints.get(key) != self._config_fingerprint():
            del self._cache[key]
            del self._cache_timestamps[key]
            del self._cache_fingerprints[key]
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
            del self._cache_fingerprints[oldest_key]
        self._cache[key] = response
        self._cache_timestamps[key] = time.monotonic()
        self._cache_fingerprints[key] = self._config_fingerprint()

    def moderate(self, request: ModerationRequest) -> ModerationResponse:
        """Moderate a single message through the three-stage pipeline.

        :param request: the incoming moderation request
        :return: the moderation response
        """
        response, _trace = self._moderate_core(request)
        return response

    def moderate_detailed(
        self,
        request: ModerationRequest,
        event_sink: Callable[[str, dict[str, Any]], None] | None = None,
        record_training: bool = True,
    ) -> tuple[ModerationResponse, PipelineTrace]:
        """Moderate a message and capture a full pipeline trace.

        The trace bypasses the response cache so every call re-runs the
        pipeline against the current runtime settings. When ``event_sink`` is
        provided it receives ``(event_name, payload)`` pairs as each stage
        completes, which the test workbench streams over SSE.

        :param request: the incoming moderation request
        :param event_sink: optional callback for stage completion events
        :param record_training: record profile/feedback rows (False for load tests)
        :return: the moderation response and its detailed trace
        """
        return self._moderate_core(
            request,
            trace_mode=True,
            event_sink=event_sink,
            record_training=record_training,
        )

    def _moderate_core(  # noqa: C901 - one long pipeline with trace bookkeeping
        self,
        request: ModerationRequest,
        *,
        trace_mode: bool = False,
        event_sink: Callable[[str, dict[str, Any]], None] | None = None,
        record_training: bool = True,
    ) -> tuple[ModerationResponse, PipelineTrace | None]:
        """Run the three-stage pipeline and return the response and a trace.

        :param request: the incoming moderation request
        :param trace_mode: when True, build a full trace and bypass the cache
        :param event_sink: optional callback for stage completion events
        :param record_training: record profile/feedback rows (False for load tests)
        :return: the moderation response and the trace (None in fast mode)
        """
        start_ns: int = time.perf_counter_ns()
        if not trace_mode:
            cache_key: int = self._get_cache_key(request.text)
            cached: ModerationResponse | None = self._get_cached(cache_key)
            if cached is not None:
                self._metrics["requests_total"] += 1.0
                self._metrics[f"requests_{cached.verdict.value.lower()}_total"] = (
                    self._metrics.get(f"requests_{cached.verdict.value.lower()}_total", 0.0) + 1.0
                )
                latency_ms: float = (time.perf_counter_ns() - start_ns) / 1_000_000.0
                return self._restore_cached(request, cached, latency_ms), None

        app_name: str = request.app_name or "default"
        verdict: Verdict = Verdict.PASS
        level_used: int = 1
        chain: list[str] = []
        reasons: list[str] = []
        matched_words: list[str] = []
        matched_detectors: list[str] = []
        matched_language: str | None = None
        confidence: float | None = None
        suspicion_score: float = 0.0
        ai_triggered: bool = False
        trigger_info: dict[str, Any] = {}
        runs: list[DetectorRunTrace] = []

        # Stage 1: safe word fast path.
        stage1_start: int = time.perf_counter_ns()
        fast_path: bool = False
        max_severity: int = 0
        severity_category: str | None = None
        if self._safe_word.is_available() and self._safe_word.is_safe(request.text):
            chain.append("safe_word_list")
            self._metrics["stage1_fast_path_total"] += 1.0
            fast_path = True
        else:
            (
                chain,
                reasons,
                matched_words,
                matched_language,
                confidence,
                verdict,
                matched_detectors,
                max_severity,
                severity_category,
            ) = self._run_level_one(request.text, runs=runs if trace_mode else None)
            if max_severity > 0 and verdict is not Verdict.BLOCK:
                policy: dict[str, Any] = self._app_config.get(app_name)
                severity_threshold: int = int(
                    policy.get(
                        "severity_hard_block_threshold",
                        self._settings.severity_hard_block_threshold,
                    )
                )
                if max_severity >= severity_threshold:
                    verdict = Verdict.BLOCK
                    reasons.append(
                        f"Matched severity {max_severity} reaches the hard-block threshold"
                    )
        stage1_ms: float = (time.perf_counter_ns() - stage1_start) / 1_000_000.0
        if event_sink is not None:
            event_sink(
                "stage1_complete",
                {
                    "stage": 1,
                    "fast_path": fast_path,
                    "verdict": "PASS" if fast_path else verdict.value,
                    "latency_ms": round(stage1_ms, 3),
                },
            )

        # Stage 2: semantic similarity and user profiling. The safe word fast
        # path skips the queries so clean traffic exits with minimal work, but
        # the message is still counted in the user profile below.
        stage2_start: int = time.perf_counter_ns()
        semantic_similarities: dict[str, float] = {}
        semantic_enabled: bool = False
        user_ratio: float = 0.0
        user_profile: dict[str, Any] | None = None
        profiling_enabled: bool = (
            bool(self._settings_service.get("USER_PROFILING_ENABLED", True))
            and self._profiler is not None
        )
        if not fast_path:
            semantic_enabled = (
                bool(self._settings_service.get("SEMANTIC_ENABLED", True))
                and self._semantic.is_available()
            )
            if semantic_enabled:
                self._metrics["semantic_queries_total"] += 1.0
                semantic_similarities = self._semantic.query(request.text)

            if profiling_enabled and request.user_id:
                user_ratio = self._profiler.get_ratio(app_name, request.user_id)
                if trace_mode:
                    user_profile = self._profiler.get_profile(app_name, request.user_id)

            suspicion_score = self._scorer.score(
                detector_names=matched_detectors,
                semantic_similarities=semantic_similarities,
                user_ratio=user_ratio,
                max_severity=max_severity,
            )

            ai_triggered, level_used, verdict, chain, reasons, confidence, trigger_info = (
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
                    max_severity,
                )
            )
        stage2_ms: float = (time.perf_counter_ns() - stage2_start) / 1_000_000.0
        if event_sink is not None:
            for run in runs:
                event_sink(
                    "detector_result",
                    {
                        "name": run.name,
                        "matched": run.matched,
                        "blocking": run.blocking,
                        "confidence": run.confidence,
                        "matched_words": run.matched_words,
                        "reason": run.reason,
                        "latency_ms": round(run.latency_ms, 3),
                    },
                )
            event_sink(
                "stage2_complete",
                {
                    "stage": 2,
                    "suspicion_score": suspicion_score,
                    "latency_ms": round(stage2_ms, 3),
                    "semantic_similarities": semantic_similarities,
                    "user_profile": user_profile,
                    "weight_contributions": (
                        self._score_contributions(
                            matched_detectors, semantic_similarities, user_ratio
                        )
                        if not fast_path
                        else []
                    ),
                },
            )

        if verdict is Verdict.BLOCK:
            self._rolling_hash.record_hit(request.text)
        if record_training and profiling_enabled and request.user_id:
            self._profiler.record(
                app_name=app_name,
                user_id=request.user_id,
                total_msgs=1,
                flagged_msgs=1 if (reasons or suspicion_score >= 50) else 0,
                blocked_msgs=1 if verdict is Verdict.BLOCK else 0,
            )
        if record_training:
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
            severity=max_severity or None,
            category=severity_category,
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
            max_severity or None,
            severity_category,
        )
        if not trace_mode:
            self._set_cache(cache_key, response)

        if not trace_mode:
            return response, None

        stage3_trace: Stage3Trace | None = None
        if ai_triggered:
            stage3_trace = Stage3Trace(
                invoked=True,
                trigger=self._describe_trigger(trigger_info),
                model_available=self._llama.is_available(),
                prompt=self._llama._last_prompt,
                response=self._llama._last_reply,
                verdict=("BLOCK" if verdict is Verdict.BLOCK else "ALLOW"),
                confidence=confidence,
                latency_ms=float(trigger_info.get("latency_ms", 0.0)),
            )
        trace: PipelineTrace = self._build_trace(
            request=request,
            verdict=verdict,
            suspicion_score=suspicion_score,
            level_used=level_used,
            ai_triggered=ai_triggered,
            reasons=reasons,
            matched_words=matched_words,
            matched_language=matched_language,
            confidence=confidence,
            total_latency_ms=latency_ms,
            stage1_ms=stage1_ms,
            stage2_ms=stage2_ms,
            fast_path=fast_path,
            runs=runs,
            semantic_similarities=semantic_similarities,
            semantic_enabled=semantic_enabled,
            user_profile=user_profile,
            user_ratio=user_ratio,
            matched_detectors=matched_detectors,
            stage3=stage3_trace,
            severity=max_severity or None,
            category=severity_category,
        )
        if event_sink is not None:
            event_sink(
                "stage3_complete",
                {
                    "stage": 3,
                    "invoked": ai_triggered,
                    "trigger": trace.stage_3.trigger if trace.stage_3 else None,
                    "model_available": (
                        trace.stage_3.model_available
                        if trace.stage_3
                        else self._llama.is_available()
                    ),
                    "prompt": trace.stage_3.prompt if trace.stage_3 else None,
                    "response": trace.stage_3.response if trace.stage_3 else None,
                    "verdict": trace.stage_3.verdict if trace.stage_3 else None,
                    "confidence": trace.stage_3.confidence if trace.stage_3 else None,
                    "latency_ms": trace.stage_3.latency_ms if trace.stage_3 else 0.0,
                },
            )
            event_sink(
                "complete",
                {
                    "response": response.model_dump(by_alias=True),
                    "trace": trace.to_dict(),
                },
            )
        return response, trace

    def _score_contributions(
        self,
        matched_detectors: list[str],
        semantic_similarities: dict[str, float],
        user_ratio: float,
    ) -> list[dict[str, Any]]:
        """Break the suspicion score into its component contributions.

        :param matched_detectors: detectors that matched
        :param semantic_similarities: per-category similarities
        :param user_ratio: the user bad-content ratio
        :return: score breakdown lines
        """
        contributions: list[dict[str, Any]] = []
        for name in matched_detectors:
            weight: int = self._scorer.detector_weight(name)
            if weight > 0:
                contributions.append(
                    {
                        "kind": "detector",
                        "name": name,
                        "value": 1.0,
                        "weight": weight,
                        "contributed": weight,
                    }
                )
        threshold: float = float(self._settings_service.get("SEMANTIC_SIMILARITY_THRESHOLD", 0.85))
        for category, similarity in semantic_similarities.items():
            if similarity > threshold:
                category_weight: int = self._scorer._category_weight(category)
                if category_weight > 0:
                    contributions.append(
                        {
                            "kind": "semantic",
                            "name": category,
                            "value": round(similarity, 4),
                            "weight": category_weight,
                            "contributed": category_weight,
                        }
                    )
        user_weight: int = int(self._settings_service.get("WEIGHT_USER", 0) or 0)
        if user_weight > 0 and user_ratio > 0:
            contributions.append(
                {
                    "kind": "user",
                    "name": "user_ratio",
                    "value": round(user_ratio, 4),
                    "weight": user_weight,
                    "contributed": round(user_ratio * user_weight, 4),
                }
            )
        return contributions

    @staticmethod
    def _describe_trigger(trigger_info: dict[str, Any]) -> str:
        """Render the LLM trigger policy into a short human-readable string.

        :param trigger_info: trigger flags captured by ``_resolve_stage_three``
        :return: a description such as "score 55 > 50"
        """
        parts: list[str] = []
        score: bool = trigger_info.get("score_trigger", False)
        semantic: bool = trigger_info.get("semantic_force", False)
        user: bool = trigger_info.get("user_ratio_force", False)
        if score:
            parts.append(
                f"score {trigger_info.get('score', 0.0):g} > {trigger_info.get('score_threshold', 0)}"
            )
        if semantic:
            parts.append(
                f"semantic {trigger_info.get('max_semantic', 0.0):g} >= "
                f"{trigger_info.get('semantic_threshold', 0.0):g}"
            )
        if user:
            parts.append(
                f"user ratio {trigger_info.get('user_ratio', 0.0):g} >= "
                f"{trigger_info.get('user_threshold', 0.0):g}"
            )
        logic: str = str(trigger_info.get("logic_type", "or"))
        return (f"[{logic}] " + " | ".join(parts)) if parts else "no trigger"

    def _build_trace(
        self,
        *,
        request: ModerationRequest,
        verdict: Verdict,
        suspicion_score: float,
        level_used: int,
        ai_triggered: bool,
        reasons: list[str],
        matched_words: list[str],
        matched_language: str | None,
        confidence: float | None,
        total_latency_ms: float,
        stage1_ms: float,
        stage2_ms: float,
        fast_path: bool,
        runs: list[DetectorRunTrace],
        semantic_similarities: dict[str, float],
        semantic_enabled: bool,
        user_profile: dict[str, Any] | None,
        user_ratio: float,
        matched_detectors: list[str],
        stage3: Stage3Trace | None,
        severity: int | None = None,
        category: str | None = None,
    ) -> PipelineTrace:
        """Assemble the full pipeline trace.

        :return: the populated pipeline trace
        """
        return PipelineTrace(
            request_id=request.id,
            app_name=request.app_name or "default",
            user_id=request.user_id,
            text=request.text,
            verdict=verdict.value,
            suspicion_score=suspicion_score,
            level_used=level_used,
            ai_triggered=ai_triggered,
            reasons=reasons,
            matched_words=matched_words,
            matched_language=matched_language,
            confidence_score=confidence,
            stage_1=Stage1Trace(
                fast_path=fast_path,
                verdict="PASS" if fast_path else verdict.value,
                latency_ms=round(stage1_ms, 3),
            ),
            stage_2=Stage2Trace(
                detector_results=runs,
                semantic_similarities=semantic_similarities,
                semantic_enabled=semantic_enabled,
                user_profile=user_profile,
                suspicion_score=suspicion_score,
                weight_contributions=[
                    WeightContribution(**line)
                    for line in self._score_contributions(
                        matched_detectors, semantic_similarities, user_ratio
                    )
                ],
                latency_ms=round(stage2_ms, 3),
            ),
            stage_3=stage3,
            total_latency_ms=round(total_latency_ms, 3),
            severity=severity,
            category=category,
        )

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
            severity=cached.severity,
            category=cached.category,
        )

    def _run_level_one(  # noqa: C901 - many short detector bookkeeping branches
        self,
        text: str,
        runs: list[DetectorRunTrace] | None = None,
    ) -> tuple[
        list[str],
        list[str],
        list[str],
        str | None,
        float | None,
        Verdict,
        list[str],
        int,
        str | None,
    ]:
        """Run the ordered Level 1 detectors over the text.

        :param text: normalized input text
        :param runs: optional list that receives one execution record per detector
        :return: chain, reasons, matched words, language, confidence, verdict,
            names of detectors that matched, the maximum matched severity, and
            the category of the strongest match
        """
        chain: list[str] = []
        reasons: list[str] = []
        matched_words: list[str] = []
        matched_detectors: list[str] = []
        matched_language: str | None = None
        confidence: float | None = None
        verdict: Verdict = Verdict.PASS
        max_severity: int = 0
        severity_category: str | None = None

        for detector in self._detectors:
            if not detector.is_available():
                if runs is not None:
                    runs.append(
                        DetectorRunTrace(
                            name=detector.name,
                            enabled=self._detector_enabled(detector.name),
                            available=False,
                            matched=False,
                            blocking=detector.blocking,
                            latency_ms=0.0,
                            weight=self._scorer.detector_weight(detector.name),
                        )
                    )
                continue
            if not self._detector_enabled(detector.name):
                if runs is not None:
                    runs.append(
                        DetectorRunTrace(
                            name=detector.name,
                            enabled=False,
                            available=True,
                            matched=False,
                            blocking=detector.blocking,
                            latency_ms=0.0,
                            weight=self._scorer.detector_weight(detector.name),
                        )
                    )
                continue
            chain.append(detector.name)
            detector_start: int = time.perf_counter_ns()
            result: DetectionResult = detector.detect(text)
            detector_ms: float = (time.perf_counter_ns() - detector_start) / 1_000_000.0
            self._detector_seconds[detector.name] = (
                self._detector_seconds.get(detector.name, 0.0) + detector_ms / 1_000.0
            )
            effective_blocking: bool = (
                result.blocking if result.blocking is not None else detector.blocking
            )
            if runs is not None:
                runs.append(
                    DetectorRunTrace(
                        name=detector.name,
                        enabled=True,
                        available=True,
                        matched=result.matched,
                        blocking=effective_blocking,
                        confidence=result.confidence_score,
                        matched_words=list(result.matched_words),
                        matched_language=result.matched_language,
                        reason=result.reason,
                        latency_ms=round(detector_ms, 3),
                        weight=self._scorer.detector_weight(detector.name),
                        severity=result.severity,
                        category=result.category,
                    )
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
            if result.severity is not None and result.severity > max_severity:
                max_severity = result.severity
                severity_category = result.category
            if effective_blocking:
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
            max_severity,
            severity_category,
        )

    def _detector_enabled(self, name: str) -> bool:
        """Resolve the runtime enable toggle for one detector.

        :param name: detector identifier
        :return: True unless the toggle is explicitly disabled
        """
        key: str = "ENABLE_DETECTOR_" + name.upper()
        return bool(self._settings_service.get(key, True))

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
        max_severity: int = 0,
    ) -> tuple[bool, int, Verdict, list[str], list[str], float | None, dict[str, Any]]:
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
        :param max_severity: severity of the strongest match, 0-10
        :return: ai_triggered, level_used, final verdict, chain, reasons,
            confidence, and a trigger info mapping
        """
        policy: dict[str, Any] = self._app_config.get(app_name)
        score_threshold: int = int(policy["score_threshold"])
        semantic_threshold: float = float(
            self._settings_service.get("SEMANTIC_FORCE_LLM_THRESHOLD", 0.90)
        )
        user_threshold: float = float(self._settings_service.get("USER_RATIO_THRESHOLD", 0.3))
        llm_mode: str = str(policy.get("llm_mode", "auto"))
        review_escalation: int = int(
            policy.get("review_escalation_threshold", self._settings.review_escalation_threshold)
        )

        score_trigger: bool = suspicion_score > score_threshold
        if llm_mode == "passthrough":
            score_trigger = True
        elif llm_mode == "aggressive":
            score_trigger = score_trigger or suspicion_score >= review_escalation
        else:
            # auto: REVIEW content still escalates once it clears the lower
            # review threshold so weak signals are never a silent PASS.
            score_trigger = score_trigger or (
                verdict is Verdict.REVIEW and suspicion_score >= review_escalation
            )
        force_semantic: bool = bool(policy["semantic_boost"]) and bool(
            semantic_similarities and max(semantic_similarities.values()) >= semantic_threshold
        )
        force_user: bool = bool(policy["user_ratio_boost"]) and user_ratio >= user_threshold
        logic_type: str = str(policy["logic_type"])
        if logic_type == "and":
            trigger: bool = score_trigger and force_semantic and force_user
        else:
            trigger = score_trigger or force_semantic or force_user

        trigger_info: dict[str, Any] = {
            "score_trigger": score_trigger,
            "semantic_force": force_semantic,
            "user_ratio_force": force_user,
            "logic_type": logic_type,
            "llm_mode": llm_mode,
            "score": suspicion_score,
            "score_threshold": score_threshold,
            "review_escalation_threshold": review_escalation,
            "max_semantic": max(semantic_similarities.values(), default=0.0),
            "semantic_threshold": semantic_threshold,
            "user_ratio": user_ratio,
            "user_threshold": user_threshold,
            "latency_ms": 0.0,
        }

        if not trigger:
            final_verdict: Verdict = verdict if verdict is Verdict.BLOCK else Verdict.PASS
            return False, 1, final_verdict, chain, reasons, confidence, trigger_info

        if not self._llama.is_available():
            trigger_info["latency_ms"] = 0.0
            self._metrics["model_unavailable_total"] += 1.0
            # Preserve a hard BLOCK from Stage 2; only ambiguous content is
            # left as REVIEW when the model cannot settle it.
            final_verdict = verdict if verdict is Verdict.BLOCK else Verdict.REVIEW
            return False, 2, final_verdict, chain, reasons, confidence, trigger_info

        chain.append(self._llama.name)
        self._metrics["ai_requests_total"] += 1.0
        llm_start: int = time.perf_counter_ns()
        llm_result: DetectionResult = self._llama.detect(text)
        trigger_info["latency_ms"] = (time.perf_counter_ns() - llm_start) / 1_000_000.0
        if llm_result.matched:
            reasons.append(llm_result.reason or self._llama.name)
            confidence = llm_result.confidence_score or confidence
            return True, 2, Verdict.BLOCK, chain, reasons, confidence, trigger_info
        return True, 2, Verdict.PASS, chain, reasons, confidence, trigger_info

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
        severity: int | None = None,
        category: str | None = None,
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
        :param severity: severity of the strongest match, if any
        :param category: category of the strongest match, if any
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
            severity=severity,
            category=category,
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
        self._phrases.close()
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
        severity: int | None = None,
        category: str | None = None,
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
        :param severity: severity of the strongest match, if any
        :param category: category of the strongest match, if any
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
            severity=severity,
            category=category,
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
