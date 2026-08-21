"""Local llama.cpp provider wrapping the existing GGUF detector.

The download, load, idle-unload, and inference machinery already lives in
:class:`~app.ai.llama_detector.LlamaCppDetector`; this adapter presents it
through the provider interface so the router treats every backend alike.
A runtime settings view overlays the registry-selected GGUF path onto the
static model configuration so admin switches apply on the next load.
"""

from __future__ import annotations

import time
from typing import Any

from app.ai.llama_detector import LlamaCppDetector
from app.ai.providers.interface import LLMProvider, ProviderResult

_ALLOW_CONFIDENCE: float = 0.5


class RuntimeModelSettings:
    """Read-only view merging runtime keys over static model settings.

    :param static_settings: the environment-backed Settings object
    :param settings_service: runtime settings holding ACTIVE_GGUF_PATH
    """

    def __init__(self, static_settings: Any, settings_service: Any) -> None:
        self._static: Any = static_settings
        self._runtime: Any = settings_service

    def __getattr__(self, name: str) -> Any:
        """Resolve an attribute from runtime overrides, then static settings.

        :param name: the attribute name
        :return: the resolved value
        """
        if name == "model_path":
            active: Any = self._runtime.get("ACTIVE_GGUF_PATH", "")
            if active:
                return str(active)
        return getattr(self._static, name)


class LocalLlamaCppProvider(LLMProvider):
    """Serves Stage 3 classifications from an in-process GGUF model."""

    def __init__(
        self, settings: Any, settings_service: Any | None = None, logger: Any | None = None
    ) -> None:
        """Wrap a lazily loading llama.cpp detector.

        :param settings: application settings with MODEL_* variables
        :param settings_service: optional runtime settings for the active path
        :param logger: optional structured logger
        """
        view: Any = (
            RuntimeModelSettings(settings, settings_service)
            if settings_service is not None
            else settings
        )
        self._detector: LlamaCppDetector = LlamaCppDetector(view, logger)

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

    def set_system_prompt(self, template: str) -> None:
        """Replace the system prompt used for classification.

        :param template: the new system prompt text
        """
        self._detector.set_system_prompt(template)

    def start(self) -> None:
        """Kick off the background download-and-load."""
        self._detector.start_preload()

    def shutdown(self) -> None:
        """Release the model memory."""
        self._detector.shutdown()
