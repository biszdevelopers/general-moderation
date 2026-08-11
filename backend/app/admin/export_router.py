"""Complete data export endpoint.

``GET /admin/export`` builds a ZIP archive of every database, CSV dump, log,
configuration snapshot (secrets redacted), semantic index, and a metadata
manifest, then streams it back. The endpoint is rate-limited to one request
per ten minutes per client.
"""

from __future__ import annotations

import time
from pathlib import Path
from typing import Any

from fastapi import APIRouter, BackgroundTasks, HTTPException, Request, status
from fastapi.responses import FileResponse

from app.export.export_service import ExportService
from app.semantic.semantic_service import SemanticService
from app.settings_service import SettingsService

_EXPORT_INTERVAL_SECONDS: int = 600


class ExportRateLimiter:
    """In-memory one-per-interval limiter keyed by client address."""

    def __init__(self, interval_seconds: int) -> None:
        self._interval: float = float(interval_seconds)
        self._last_export: dict[str, float] = {}

    def allowed(self, client: str) -> bool:
        """Return whether the client may start a new export now.

        :param client: client identifier
        :return: True when within the window
        """
        now: float = time.monotonic()
        last: float | None = self._last_export.get(client)
        if last is not None and now - last < self._interval:
            return False
        self._last_export[client] = now
        return True


def create_export_router(
    export_service: ExportService,
    engine: Any,
    semantic_service: SemanticService,
    settings_service: SettingsService,
    auth_dependency: Any,
) -> APIRouter:
    """Build the data export admin router.

    :param export_service: the export service
    :param engine: the moderation engine (for metadata)
    :param semantic_service: the semantic similarity service (for metadata)
    :param settings_service: the runtime settings service (for the snapshot)
    :param auth_dependency: FastAPI dependency guarding the routes
    :return: the configured APIRouter
    """
    router: APIRouter = APIRouter(prefix="/admin", tags=["admin"], dependencies=[auth_dependency])
    limiter: ExportRateLimiter = ExportRateLimiter(_EXPORT_INTERVAL_SECONDS)

    @router.get("/export")
    def export_data(request: Request, background_tasks: BackgroundTasks) -> FileResponse:
        """Build and stream a full data export archive.

        :param request: the ASGI request (used for the client address)
        :param background_tasks: FastAPI background task runner
        :return: the ZIP file response
        :raises HTTPException: 429 when the rate limit is exceeded
        """
        client: str = request.client.host if request.client is not None else "unknown"
        if not limiter.allowed(client):
            raise HTTPException(
                status_code=status.HTTP_429_TOO_MANY_REQUESTS,
                detail="Export is rate-limited to once per 10 minutes",
            )
        semantic_stats: dict[str, Any] = semantic_service.stats()
        metadata: dict[str, Any] = {
            "detector_count": len(getattr(engine, "_detectors", [])),
            "ai_available": bool(
                getattr(getattr(engine, "_llama", None), "is_available", lambda: False)()
            ),
            "semantic_available": semantic_stats.get("available", False),
            "semantic_categories": semantic_stats.get("categories", {}),
            "settings_snapshot": settings_service.to_json(),
        }
        zip_path: Path = export_service.create_export(metadata)

        def _cleanup(path: Path) -> None:
            time.sleep(5)
            path.unlink(missing_ok=True)

        background_tasks.add_task(_cleanup, zip_path)
        return FileResponse(
            zip_path,
            media_type="application/zip",
            filename=zip_path.name,
        )

    return router
