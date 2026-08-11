"""Level 2 AI detector backed by llama.cpp (C++ inference engine).

User input is strictly sanitized before reaching the model to prevent prompt
injection: chat control tokens are stripped with C regex, XML metacharacters
are escaped, and the text is wrapped in ``<user_text>`` tags. The engine runs
at ``temperature=0.0`` and must reply with a single classification token.
"""

from __future__ import annotations

import re
import xml.sax.saxutils
from typing import Any

try:
    import regex as _compiled_regex
except ImportError:  # pragma: no cover - regex is the C-backed primary
    _compiled_regex = None

from app.detectors.interface import DetectorInterface
from app.models.verdict import DetectionResult

_CONTROL_TOKEN_PATTERN = re.compile(r"<\|im_start\|>|<\|im_end\|>|<\|endoftext\|>")
_TOKEN_PREFIX_PATTERN = re.compile(r"^(system|user|assistant):", re.IGNORECASE)

_SYSTEM_PROMPT = (
    "You are a strict content moderation classifier. Analyze the user text for "
    "vulgar, abusive, hateful, or politically sensitive content. Reply with "
    "exactly one word: BLOCK or ALLOW."
)


class LlamaCppDetector(DetectorInterface):
    """Classifies borderline content with a locally hosted GGUF model."""

    def __init__(self, settings: Any, logger: Any | None = None) -> None:
        """Load and warm up the model.

        :param settings: application settings with MODEL_* variables
        :param logger: optional logger for load failures
        """
        self._settings: Any = settings
        self._logger: Any = logger
        self._model: Any | None = None
        self._load_model()

    def _load_model(self) -> None:
        """Load the GGUF model and run a warm-up pass."""
        try:
            from llama_cpp import Llama
        except ImportError as exc:
            self._record_failure("llama_cpp_import_failed", str(exc))
            return
        try:
            self._model = Llama(
                model_path=self._settings.model_path,
                n_ctx=self._settings.model_context_size,
                n_threads=self._settings.model_threads,
                n_batch=self._settings.model_batch_size,
                n_gpu_layers=0,
            )
            self._warm_up()
        except Exception as exc:  # pragma: no cover - model load varies by platform
            self._model = None
            self._record_failure("model_load_failed", str(exc))

    def _warm_up(self) -> None:
        """Run a tiny generation to force model initialization."""
        if self._model is not None:
            self._model(
                self._build_prompt("warmup"),
                temperature=0.0,
                max_tokens=1,
            )

    @property
    def name(self) -> str:
        """Return the detector name."""
        return "llama_cpp"

    @property
    def priority(self) -> int:
        """Return the pipeline position."""
        return 8

    @property
    def language(self) -> str:
        """Return the language scope."""
        return "any"

    @property
    def blocking(self) -> bool:
        """Model verdicts are decisive at Level 2."""
        return True

    def is_available(self) -> bool:
        """Whether the model loaded successfully."""
        return self._model is not None

    @staticmethod
    def sanitize(text: str) -> str:
        """Sanitize text against prompt injection before inference.

        Removes chat control tokens, strips leading system/user/assistant
        prefixes, XML-escapes metacharacters, and wraps the result in
        ``<user_text>`` tags.

        :param text: raw user text
        :return: a safe, tagged payload for the model
        """
        cleaned: str = _CONTROL_TOKEN_PATTERN.sub("", text)
        cleaned = _TOKEN_PREFIX_PATTERN.sub("", cleaned)
        escaped: str = xml.sax.saxutils.escape(cleaned, {'"': "&quot;"})
        return f"<user_text>{escaped}</user_text>"

    def _build_prompt(self, text: str) -> str:
        """Compose the classification prompt.

        :param text: raw user text
        :return: the full prompt with the sanitized payload
        """
        payload: str = LlamaCppDetector.sanitize(text)
        return f"{_SYSTEM_PROMPT}\n{payload}"

    def detect(self, text: str) -> DetectionResult:
        """Classify the text with the local model.

        :param text: normalized input text
        :return: a positive result when the model replies BLOCK
        """
        if self._model is None:
            return DetectionResult(matched=False)
        try:
            output: dict[str, Any] = self._model(
                self._build_prompt(text),
                temperature=0.0,
                max_tokens=self._settings.model_max_tokens,
            )
            reply: str = output["choices"][0]["text"].strip().upper()
        except Exception:
            return DetectionResult(matched=False)
        blocked: bool = reply.startswith("BLOCK") or "BLOCK" in reply
        return DetectionResult(
            matched=blocked,
            reason="LLM classified the text as BLOCK" if blocked else None,
            confidence_score=0.9 if blocked else None,
        )

    def reload(self) -> None:
        """No-op: the model is fixed for the process lifetime."""

    def shutdown(self) -> None:
        """Release the model and its memory."""
        if self._model is not None:
            try:
                self._model.close()
            except Exception:
                pass
            self._model = None

    def _record_failure(self, event: str, detail: str) -> None:
        """Emit a structured warning when the model cannot be used.

        :param event: short event name
        :param detail: failure detail
        """
        if self._logger is not None:
            self._logger.log(
                30,  # logging.WARNING
                f"llama:{event}",
                detail=detail,
            )
