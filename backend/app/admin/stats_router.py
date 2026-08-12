"""Dashboard statistics and spot-check sampling endpoints."""

from __future__ import annotations

import random
from pathlib import Path
from typing import Any

import orjson
from fastapi import APIRouter

from app.feedback.feedback_service import FeedbackService
from app.wordbank.manager import WordBankManager


def create_stats_router(
    engine: Any,
    word_bank: WordBankManager,
    feedback_service: FeedbackService,
    log_file_path: str,
    auth_dependency: Any,
) -> APIRouter:
    """Build the statistics admin router.

    :param engine: the moderation engine
    :param word_bank: the shared word bank manager
    :param feedback_service: the feedback service
    :param log_file_path: path to the audit log file
    :param auth_dependency: FastAPI dependency guarding the routes
    :return: the configured APIRouter
    """
    router: APIRouter = APIRouter(prefix="/admin", tags=["admin"], dependencies=[auth_dependency])

    @router.get("/stats")
    def stats() -> dict[str, Any]:
        """Return the dashboard statistics.

        :return: counters, profiling stats, and word bank totals
        """
        return {
            "metrics": engine.metrics(),
            "profiling": engine._profiler.stats(),
            "word_bank": word_bank.get_stats(),
            "semantic": engine._semantic.stats(),
            "ai_available": engine._llama.is_available(),
            "detector_count": len(engine._detectors),
        }

    @router.get("/spot-check")
    def spot_check(count: int = 50) -> dict[str, Any]:
        """Sample recent audit entries for administrative review.

        :param count: how many recent entries to sample from
        :return: a random sample of the sampled entries
        """
        path: Path = Path(log_file_path)
        if not path.is_file():
            return {"sample": []}
        lines: list[str] = path.read_text(encoding="utf-8").splitlines()
        recent: list[str] = lines[-max(count, 1) * 20 :]
        entries: list[dict[str, Any]] = []
        for line in recent:
            try:
                record: dict[str, Any] = orjson.loads(line)
            except orjson.JSONDecodeError:
                continue
            if record.get("message") != "moderation_decision":
                continue
            entries.append(
                {
                    "requestId": record.get("requestId"),
                    "userId": record.get("userId"),
                    "verdict": record.get("verdict"),
                    "suspicionScore": record.get("suspicionScore", 0),
                    "matchedWord": record.get("matchedWord"),
                    "levelUsed": record.get("levelUsed"),
                    "aiTriggered": record.get("aiTriggered", False),
                    "timestamp": record.get("timestamp"),
                }
            )
        sample: list[dict[str, Any]] = (
            entries if len(entries) <= count else random.sample(entries, count)
        )
        return {"sample": sample}

    return router
