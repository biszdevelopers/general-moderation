"""Administrator feedback ingestion and the daily auto-tuning batch.

Feedback rows record whether the service verdict was correct. The daily batch
(run on the ``AUTO_TUNING_BATCH_HOUR``) aggregates the last 24 hours,
adjusts every weight toward high-precision values, applies exponential decay
to older influence (half-life ``WEIGHT_DECAY_HALF_LIFE_DAYS``), and re-tunes
the default suspicion threshold so the LLM handles approximately
``AI_TARGET_PERCENTAGE`` of traffic.
"""

from __future__ import annotations

import logging
import sqlite3
import threading
from datetime import UTC, datetime, timedelta
from pathlib import Path
from typing import Any

_LOGGER: logging.Logger = logging.getLogger(__name__)

_FEEDBACK_SCHEMA = """
    CREATE TABLE IF NOT EXISTS feedback (
        id INTEGER PRIMARY KEY,
        request_id TEXT NOT NULL,
        verdict TEXT NOT NULL,
        is_correct INTEGER NOT NULL,
        actual_action TEXT NOT NULL,
        timestamp TEXT NOT NULL
    )
"""
_DECISION_SCHEMA = """
    CREATE TABLE IF NOT EXISTS decisions (
        id INTEGER PRIMARY KEY,
        verdict TEXT NOT NULL,
        ai_used INTEGER NOT NULL,
        timestamp TEXT NOT NULL
    )
"""
_META_SCHEMA = """
    CREATE TABLE IF NOT EXISTS meta (
        key TEXT PRIMARY KEY,
        value TEXT NOT NULL
    )
"""

_WEIGHT_KEYS: tuple[str, ...] = (
    "WEIGHT_DETECTOR_BADWORDS",
    "WEIGHT_DETECTOR_PROFANITE",
    "WEIGHT_DETECTOR_GLIN",
    "WEIGHT_DETECTOR_AHO",
    "WEIGHT_DETECTOR_BKTREE",
    "WEIGHT_DETECTOR_METAPHONE",
    "WEIGHT_SEMANTIC_POLITICAL",
    "WEIGHT_SEMANTIC_VIOLENCE",
    "WEIGHT_SEMANTIC_SEXUAL",
    "WEIGHT_SEMANTIC_HATE",
    "WEIGHT_SEMANTIC_PII",
    "WEIGHT_SEMANTIC_ADS",
    "WEIGHT_USER",
)

_DEFAULT_WEIGHTS: dict[str, int] = {
    "WEIGHT_DETECTOR_BADWORDS": 25,
    "WEIGHT_DETECTOR_PROFANITE": 20,
    "WEIGHT_DETECTOR_GLIN": 20,
    "WEIGHT_DETECTOR_AHO": 30,
    "WEIGHT_DETECTOR_BKTREE": 20,
    "WEIGHT_DETECTOR_METAPHONE": 15,
    "WEIGHT_SEMANTIC_POLITICAL": 35,
    "WEIGHT_SEMANTIC_VIOLENCE": 40,
    "WEIGHT_SEMANTIC_SEXUAL": 30,
    "WEIGHT_SEMANTIC_HATE": 35,
    "WEIGHT_SEMANTIC_PII": 25,
    "WEIGHT_SEMANTIC_ADS": 15,
    "WEIGHT_USER": 20,
}


class FeedbackService:
    """Stores corrections and runs the auto-tuning batch.

    :param settings: application settings
    :param settings_service: runtime settings service that receives the tuning
    :param app_config: app policy service whose default threshold is tuned
    :param logger: audit logger
    """

    def __init__(
        self,
        settings: Any,
        settings_service: Any,
        app_config: Any,
        logger: Any,
    ) -> None:
        self._settings: Any = settings
        self._settings_service: Any = settings_service
        self._app_config: Any = app_config
        self._logger: Any = logger
        self._lock: threading.Lock = threading.Lock()
        self._db_path: str = settings.feedback_db_path
        Path(self._db_path).parent.mkdir(parents=True, exist_ok=True)
        self._connection: sqlite3.Connection = sqlite3.connect(
            self._db_path, check_same_thread=False
        )
        self._connection.execute("PRAGMA journal_mode=WAL")
        self._connection.execute("PRAGMA synchronous=NORMAL")
        self._connection.executescript(_FEEDBACK_SCHEMA)
        self._connection.executescript(_DECISION_SCHEMA)
        self._connection.executescript(_META_SCHEMA)
        self._connection.commit()

    @staticmethod
    def _now() -> str:
        """Return the current UTC time as an ISO 8601 string."""
        return datetime.now(UTC).isoformat()

    def record_feedback(
        self, request_id: str, verdict: str, is_correct: bool, actual_action: str
    ) -> None:
        """Store one administrator correction.

        :param request_id: the request being corrected
        :param verdict: the original service verdict
        :param is_correct: whether the verdict was correct
        :param actual_action: the action the administrator took
        """
        with self._lock:
            self._connection.execute(
                "INSERT INTO feedback (request_id, verdict, is_correct, actual_action, timestamp) "
                "VALUES (?, ?, ?, ?, ?)",
                (request_id, verdict, int(is_correct), actual_action, self._now()),
            )
            self._connection.commit()

    def record_decision(self, verdict: str, ai_used: bool) -> None:
        """Record one moderation decision for threshold tuning.

        :param verdict: the final verdict (PASS, BLOCK, or REVIEW)
        :param ai_used: whether the LLM participated
        """
        if not self._settings.auto_tuning_enabled:
            return
        with self._lock:
            self._connection.execute(
                "INSERT INTO decisions (verdict, ai_used, timestamp) VALUES (?, ?, ?)",
                (verdict, int(ai_used), self._now()),
            )
            self._connection.commit()

    def _meta(self, key: str, default: str = "") -> str:
        """Read one metadata value."""
        row = self._connection.execute("SELECT value FROM meta WHERE key = ?", (key,)).fetchone()
        return row[0] if row else default

    def _set_meta(self, key: str, value: str) -> None:
        """Write one metadata value."""
        self._connection.execute(
            "INSERT INTO meta (key, value) VALUES (?, ?) "
            "ON CONFLICT(key) DO UPDATE SET value = excluded.value",
            (key, value),
        )
        self._connection.commit()

    def run_batch(self) -> dict[str, Any]:
        """Execute the daily weight and threshold tuning.

        :return: a tuning report with the adjusted weights and threshold
        """
        if not self._settings.auto_tuning_enabled:
            return {"status": "disabled"}
        now: datetime = datetime.now(UTC)
        since: str = (now - timedelta(hours=24)).isoformat()
        with self._lock:
            feedback_rows = self._connection.execute(
                "SELECT is_correct FROM feedback WHERE timestamp >= ?", (since,)
            ).fetchall()
            decision_rows = self._connection.execute(
                "SELECT verdict, ai_used FROM decisions WHERE timestamp >= ?", (since,)
            ).fetchall()
            self._connection.execute("DELETE FROM feedback WHERE timestamp < ?", (since,))
            self._connection.execute("DELETE FROM decisions WHERE timestamp < ?", (since,))
            self._connection.commit()

        report: dict[str, Any] = {
            "status": "ok",
            "feedback_window": len(feedback_rows),
            "decision_window": len(decision_rows),
        }

        last_tuned_raw: str = self._meta("last_tuned")
        if last_tuned_raw:
            last_tuned: datetime = datetime.fromisoformat(last_tuned_raw)
            days_since: float = max(0.0, (now - last_tuned).total_seconds() / 86400.0)
        else:
            days_since = 0.0
        half_life: float = max(1.0, float(self._settings.weight_decay_half_life_days))
        decay: float = 2 ** (-days_since / half_life)

        correct: int = sum(1 for row in feedback_rows if row[0])
        total: int = len(feedback_rows)
        precision: float = correct / total if total else 0.5
        report["precision"] = round(precision, 4)

        weights: dict[str, int] = {}
        for key in _WEIGHT_KEYS:
            current: int = int(
                self._settings_service.get(key, _DEFAULT_WEIGHTS[key]) or _DEFAULT_WEIGHTS[key]
            )
            delta: int = 0
            if total >= 10:
                delta = 1 if precision > 0.6 else (-1 if precision < 0.4 else 0)
            default: int = _DEFAULT_WEIGHTS[key]
            next_weight: int = round(default + (current - default) * decay)
            tuned: int = max(5, min(50, next_weight + delta))
            weights[key] = tuned
        report["weights"] = weights
        self._settings_service.update(weights)

        ai_used: int = sum(1 for row in decision_rows if row[1])
        ai_passes: int = sum(1 for row in decision_rows if row[1] and row[0] == "PASS")
        if ai_used > 0:
            pass_rate: float = ai_passes / ai_used
            block_rate: float = 1.0 - pass_rate
            current_threshold: int = int(self._app_config.get(None)["score_threshold"])
            if pass_rate > 0.90:
                current_threshold = min(100, current_threshold + 2)
            elif block_rate > 0.30:
                current_threshold = max(0, current_threshold - 2)
            self._app_config.update_default_threshold(current_threshold)
            report["score_threshold"] = current_threshold
            report["llm_pass_rate"] = round(pass_rate, 4)
        else:
            report["score_threshold"] = int(self._app_config.get(None)["score_threshold"])

        self._set_meta("last_tuned", now.isoformat())
        _LOGGER.info(
            "Auto-tuning batch complete: precision=%s, threshold=%s, %d weights adjusted",
            report.get("precision"),
            report.get("score_threshold"),
            len(weights),
        )
        return report

    def close(self) -> None:
        """Close the underlying database connection."""
        self._connection.close()
