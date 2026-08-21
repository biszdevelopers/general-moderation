"""Local llama.cpp provider wrapping the existing GGUF detector.

The download, load, idle-unload, and inference machinery already lives in
:class:`~app.ai.llama_detector.LlamaCppDetector`; this adapter presents it
through the provider interface so the router treats every backend alike.
"""

from __future__ import annotations

import time
from typing import Any

from app.ai.llama_detector import LlamaCppDetector
from app.ai.providers.interface import LLMProvider, ProviderResult

_ALLOW_CONFIDENCE: float = 0.5


class LocalLlamaCppProvider(LLMProvider):
    """Serves Stage 3 classifications from an in-process GGUF model."""

    def __init__(self, settings: Any, logger: Any | None = None) -> None:
        """Wrap a lazily loading llama.cpp detector.

        :param settings: application settings with MODEL_* variables
        :param logger: optional structured logger
        """
        self._detector: LlamaCppDetector = LlamaCppDetector(settings, logger)

    @property
    def name(self) -> str:
        """Return the provider identifier."""
        return "local_llama_cpp"

    def classify(self, text: str) -> ProviderResult:
        """Classify the text with the local model.

        :param text: raw user text
        :return: the classification result
        """
        start: float = time.monotonic()
        result = self._detector.detect(text)
        latency_ms: float = round((time.monotonic() - start) * 1000, 2)
        return ProviderResult(
            blocked=result.matched,
            confidence=result.confidence_score if result.matched else _ALLOW_CONFIDENCE,
            raw_reply=self._detector.last_reply or "",
            latency_ms=latency_ms,
        )

    def health_check(self) -> bool:
        """Return whether the local model is loaded."""
        return self._detector.is_available()

    @property
    def last_prompt(self) -> str | None:
        """Return the most recent prompt sent to the model."""
        return self._detector.last_prompt

    @property
    def last_reply(self) -> str | None:
        """Return the most recent raw reply."""
        return self._detector.last_reply

    def start(self) -> None:
        """Kick off the background download-and-load."""
        self._detector.start_preload()

    def shutdown(self) -> None:
        """Release the model memory."""
        self._detector.shutdown()
