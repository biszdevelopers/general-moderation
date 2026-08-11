"""Service-level admin endpoints.

Covers bulk word import/export, word bank statistics, audit access, hot
reload, graceful shutdown, health, and Prometheus metrics.
"""

from __future__ import annotations

import os
import time
from pathlib import Path
from typing import Annotated, Any

import orjson
from fastapi import APIRouter, BackgroundTasks, Depends, Request, status
from pydantic import BaseModel, Field

from app.admin.wordlist import AddWordRequest
from app.engine.moderation_engine import ModerationEngine
from app.wordbank.manager import WordBankManager
from app.wordbank.models import CustomWord

_AUDIT_LINES: int = 100


class ImportWordsRequest(BaseModel):
    """Bulk import payload.

    :param items: the words to import
    """

    items: Annotated[list[AddWordRequest], Field(min_length=1, max_length=1000)]


def _prometheus_lines(metrics: dict[str, float]) -> str:
    """Render the runtime counters in Prometheus text format.

    :param metrics: counter values keyed by metric name
    :return: the Prometheus exposition payload
    """
    lines: list[str] = []
    for name, value in metrics.items():
        lines.append(f"# TYPE {name} counter")
        lines.append(f"{name} {value}")
    return "\n".join(lines) + "\n"


def create_wordbank_router(
    engine: ModerationEngine,
    word_bank: WordBankManager,
    log_file_path: str,
    auth_dependency: Any,
) -> APIRouter:
    """Build the service-level admin router.

    :param engine: the moderation engine
    :param word_bank: the shared word bank manager
    :param log_file_path: path to the audit log file
    :param auth_dependency: FastAPI dependency guarding the routes
    :return: the configured APIRouter
    """
    router: APIRouter = APIRouter(
        prefix="/admin", tags=["admin"], dependencies=[auth_dependency]
    )
    start_time: float = time.monotonic()

    @router.post("/wordbank/import")
    def import_words(payload: ImportWordsRequest) -> dict[str, int]:
        """Bulk-import custom words.

        :param payload: the words to import
        :return: the number of successfully imported words
        """
        imported: int = word_bank.import_words(
            [item.model_dump() for item in payload.items]
        )
        return {"imported": imported}

    @router.get("/wordbank/export", response_model=list[CustomWord])
    def export_words() -> list[CustomWord]:
        """Export every custom word.

        :return: the custom words ordered by id ascending
        """
        return word_bank.export_words()

    @router.get("/wordbank/audit")
    def audit_log() -> list[dict[str, Any]]:
        """Return the most recent audit records from the JSONL log.

        :return: the last parsed audit entries
        """
        path: Path = Path(log_file_path)
        if not path.is_file():
            return []
        lines: list[str] = path.read_text(encoding="utf-8").splitlines()
        entries: list[dict[str, Any]] = []
        for line in lines[-_AUDIT_LINES:]:
            try:
                entries.append(orjson.loads(line))
            except orjson.JSONDecodeError:
                continue
        return entries

    @router.get("/wordbank/stats")
    def word_bank_stats() -> dict[str, Any]:
        """Return word bank summary statistics.

        :return: total, custom, and base word counts
        """
        return word_bank.get_stats()

    @router.get("/wordbank/languages")
    def word_bank_languages() -> list[str]:
        """Return the distinct languages in the word bank.

        :return: sorted language codes
        """
        return word_bank.get_languages()

    @router.get("/wordbank/categories")
    def word_bank_categories() -> list[str]:
        """Return the distinct categories in the word bank.

        :return: sorted category names
        """
        return word_bank.get_categories()

    @router.post("/reload")
    def reload_word_bank() -> dict[str, str]:
        """Hot-reload the word bank and rebuild detector caches.

        :return: a status acknowledgment
        """
        word_bank.reload()
        engine.refresh_detectors()
        return {"status": "reloaded"}

    @router.post("/shutdown", status_code=status.HTTP_202_ACCEPTED)
    def shutdown(background_tasks: BackgroundTasks) -> dict[str, str]:
        """Trigger a graceful shutdown in the background.

        :param background_tasks: FastAPI background task runner
        :return: an acknowledgment
        """

        def _graceful_shutdown() -> None:
            time.sleep(0.2)
            engine.shutdown()
            os._exit(0)

        background_tasks.add_task(_graceful_shutdown)
        return {"status": "shutting_down"}

    @router.get("/health")
    def health() -> dict[str, Any]:
        """Return a detailed health report.

        :return: service status, detector availability, and uptime
        """
        return {
            "status": "ok",
            "uptime_seconds": round(time.monotonic() - start_time, 3),
            "word_count": word_bank.get_stats(),
            "llama_available": engine._llama.is_available(),
            "detectors": [
                {
                    "name": detector.name,
                    "available": detector.is_available(),
                }
                for detector in engine._detectors
            ],
        }

    @router.get("/metrics", include_in_schema=False)
    def metrics() -> Any:
        """Return the Prometheus metrics payload.

        :return: the metrics exposition as text
        """
        from fastapi.responses import PlainTextResponse

        return PlainTextResponse(
            _prometheus_lines(engine.metrics()),
            media_type="text/plain; version=0.0.4",
        )

    return router
