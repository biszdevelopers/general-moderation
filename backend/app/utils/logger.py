"""JSONL audit logging.

Log records are serialized with ``orjson`` (Rust) and written through the
C-backed standard logging framework with size-based rotation. No passwords,
API keys, or raw message bodies are ever logged.
"""

from __future__ import annotations

import hashlib
import logging
import time
from logging.handlers import RotatingFileHandler
from typing import Any

import orjson


class OrjsonFormatter(logging.Formatter):
    """Serialize log records to single-line JSON using Rust orjson."""

    def format(self, record: logging.LogRecord) -> str:
        """Return the record serialized as a JSON object string."""
        payload: dict[str, Any] = {
            "timestamp": time.strftime("%Y-%m-%dT%H:%M:%S", time.gmtime(record.created)),
            "level": record.levelname,
            "message": record.getMessage(),
        }
        extra: dict[str, Any] = getattr(record, "extra_fields", None) or {}
        payload.update(extra)
        return orjson.dumps(payload, option=orjson.OPT_APPEND_NEWLINE).decode("utf-8")


class ModerationLogger:
    """Thin facade over a size-rotating JSONL logger.

    :param file_path: path to the log file
    :param level: minimum severity to record
    :param max_bytes: rotation threshold for a single log file
    :param backup_count: number of rotated files to retain
    """

    def __init__(
        self,
        file_path: str,
        level: str = "INFO",
        max_bytes: int = 104_857_600,
        backup_count: int = 10,
    ) -> None:
        self._logger: logging.Logger = logging.getLogger("moderation")
        self._logger.setLevel(level.upper())
        self._logger.propagate = False
        if not self._logger.handlers:
            handler: RotatingFileHandler = RotatingFileHandler(
                file_path,
                maxBytes=max_bytes,
                backupCount=backup_count,
                encoding="utf-8",
            )
            handler.setFormatter(OrjsonFormatter())
            self._logger.addHandler(handler)

    def log(self, level: int, message: str, **fields: Any) -> None:
        """Emit a structured record at the given logging level.

        :param level: one of the logging severity constants
        :param message: short human-readable message
        :param fields: structured fields merged into the JSON record
        """
        self._logger.log(level, message, extra={"extra_fields": fields})

    def log_moderation(
        self,
        *,
        request_id: str | None,
        user_id: str | None,
        text: str,
        verdict: str,
        level_used: int,
        reason: str | None,
        matched_word: str | None,
        matched_language: str | None,
        confidence_score: float | None,
        latency_ms: float,
        detector_chain: list[str],
        suspicion_score: float = 0.0,
        ai_triggered: bool = False,
    ) -> None:
        """Record a complete moderation decision.

        :param request_id: caller-supplied request identifier
        :param user_id: caller-supplied author identifier
        :param text: raw message text, used only to derive a hash and preview
        :param verdict: final verdict string
        :param level_used: detection level that produced the verdict
        :param reason: human-readable reason, if any
        :param matched_word: offending word, if any
        :param matched_language: ISO code of the detected language, if known
        :param confidence_score: overall confidence, if any
        :param latency_ms: total processing time in milliseconds
        :param detector_chain: ordered detector names that ran
        :param suspicion_score: the computed 0-100 suspicion score
        :param ai_triggered: whether the LLM was invoked
        """
        text_hash: str = hashlib.sha256(text.encode("utf-8")).hexdigest()
        text_preview: str = text[:50]
        self.log(
            logging.INFO,
            "moderation_decision",
            requestId=request_id,
            userId=user_id,
            textHash=text_hash,
            textPreview=text_preview,
            verdict=verdict,
            levelUsed=level_used,
            reason=reason,
            matchedWord=matched_word,
            matchedLanguage=matched_language,
            confidenceScore=confidence_score,
            latencyMs=latency_ms,
            detectorChain=detector_chain,
            suspicionScore=suspicion_score,
            aiTriggered=ai_triggered,
        )

    def close(self) -> None:
        """Flush and shut down the underlying logger."""
        for handler in self._logger.handlers:
            handler.flush()
            handler.close()
