"""Detection pipeline orchestration.

The engine runs detectors in strict priority order, short-circuiting on a
decisive exact match. Non-decisive hits (fuzzy, phonetic, probabilistic)
produce a REVIEW verdict which is resolved by the Level 2 llama.cpp engine
when available. Verdicts and latencies are measured and audited here.
"""

from __future__ import annotations

import logging
import time
from typing import Any

from app.ai.llama_detector import LlamaCppDetector
from app.detectors.aho_detector import AhoCorasickDetector
from app.detectors.bktree_detector import BkTreeDetector
from app.detectors.bloom_detector import BloomFilterDetector
from app.detectors.interface import DetectorInterface
from app.detectors.metaphone_detector import MetaphoneDetector
from app.detectors.minhash_detector import MinHashDetector
from app.detectors.multi_language_detector import MultiLanguageDetector
from app.detectors.rolling_hash_detector import RollingHashDetector
from app.models.request import BatchModerationRequest, ModerationRequest
from app.models.response import BatchModerationResponse, ModerationResponse
from app.models.verdict import DetectionResult, Verdict
from app.wordbank.manager import WordBankManager


class ModerationEngine:
    """Owns the detectors and produces moderation verdicts.

    :param settings: application settings
    :param word_bank: shared word bank manager
    :param logger: audit logger
    """

    def __init__(self, settings: Any, word_bank: WordBankManager, logger: Any) -> None:
        self._settings: Any = settings
        self._word_bank: WordBankManager = word_bank
        self._logger: Any = logger
        self._rolling_hash: RollingHashDetector = RollingHashDetector(
            cache_size=settings.spam_cache_size,
            ttl_seconds=settings.spam_cache_ttl_seconds,
        )
        self._llama: LlamaCppDetector = LlamaCppDetector(settings, logger)
        self._detectors: list[DetectorInterface] = self._build_detectors()

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
            MinHashDetector(
                self._word_bank,
                num_perm=self._settings.minhash_num_perm,
                threshold=self._settings.minhash_jaccard_threshold,
            ),
        ]

    def refresh_detectors(self) -> None:
        """Rebuild detector caches after the word bank is reloaded."""
        for detector in self._detectors:
            if detector.is_available():
                detector.reload()

    def moderate(self, request: ModerationRequest) -> ModerationResponse:
        """Moderate a single message.

        :param request: the incoming moderation request
        :return: the moderation response
        """
        start_ns: int = time.perf_counter_ns()
        chain: list[str] = []
        reasons: list[str] = []
        matched_words: list[str] = []
        matched_language: str | None = None
        confidence: float | None = None
        verdict: Verdict = Verdict.PASS
        level_used: int = 1

        for detector in self._detectors:
            if not detector.is_available():
                continue
            chain.append(detector.name)
            result: DetectionResult = detector.detect(request.text)
            if not result.matched:
                continue
            reasons.append(result.reason or detector.name)
            matched_words.extend(result.matched_words)
            if result.matched_language and matched_language is None:
                matched_language = result.matched_language
            result_confidence: float | None = result.confidence_score
            if result_confidence is not None:
                confidence = result_confidence if confidence is None else max(confidence, result_confidence)
            if detector.blocking:
                verdict = Verdict.BLOCK
                break

        if verdict is Verdict.PASS and reasons:
            verdict = Verdict.REVIEW

        if verdict is Verdict.REVIEW and self._llama.is_available():
            level_used = 2
            chain.append(self._llama.name)
            llm_result: DetectionResult = self._llama.detect(request.text)
            if llm_result.matched:
                verdict = Verdict.BLOCK
                reasons.append(llm_result.reason or self._llama.name)
                confidence = llm_result.confidence_score
                matched_words = list(dict.fromkeys(matched_words))

        if verdict is Verdict.BLOCK:
            self._rolling_hash.record_hit(request.text)

        latency_ms: float = (time.perf_counter_ns() - start_ns) / 1_000_000.0

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
        )

        return ModerationResponse(
            id=request.id,
            verdict=verdict,
            level_used=level_used,
            reasons=reasons,
            matched_words=matched_words,
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
                ModerationRequest(id=item.id, user_id=item.user_id, text=item.text)
            )
            for item in batch.items
        ]
        total_latency_ms: float = (time.perf_counter_ns() - start_ns) / 1_000_000.0
        return BatchModerationResponse(
            results=results, total_latency_ms=total_latency_ms
        )

    def shutdown(self) -> None:
        """Release models, storage, and logger resources."""
        self._llama.shutdown()
        self._word_bank.close()
        self._logger.close()

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
        )

    def log(self, message: str, **fields: Any) -> None:
        """Emit a structured log record through the shared logger.

        :param message: log message
        :param fields: structured fields
        """
        self._logger.log(logging.INFO, message, **fields)
