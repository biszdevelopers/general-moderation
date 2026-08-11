"""Runtime settings admin endpoints.

``GET /admin/settings`` returns the full setting catalog with descriptions and
editability flags; ``POST /admin/settings`` validates and persists changes so
they apply without a service restart.
"""

from __future__ import annotations

from typing import Any

from fastapi import APIRouter, HTTPException, status
from pydantic import BaseModel

from app.settings_service import SettingsService


class UpdateSettingsRequest(BaseModel):
    """A batch of settings to update.

    :param settings: settings key to value mapping
    """

    settings: dict[str, Any]


def create_settings_router(settings_service: SettingsService, auth_dependency: Any) -> APIRouter:
    """Build the runtime settings admin router.

    :param settings_service: the runtime settings service
    :param auth_dependency: FastAPI dependency guarding the routes
    :return: the configured APIRouter
    """
    router: APIRouter = APIRouter(prefix="/admin", tags=["admin"], dependencies=[auth_dependency])

    @router.get("/settings")
    def get_settings() -> dict[str, list[dict[str, Any]]]:
        """Return the full settings catalog.

        :return: the settings with type, description, and editability flags
        """
        return {"settings": settings_service.describe()}

    @router.post("/settings")
    def update_settings(payload: UpdateSettingsRequest) -> dict[str, Any]:
        """Validate and apply a batch of settings.

        :param payload: the settings to update
        :return: the keys that changed
        :raises HTTPException: 400 for an unknown, read-only, or invalid value
        """
        try:
            updated: dict[str, Any] = settings_service.update(payload.settings)
        except ValueError as exc:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(exc)) from exc
        return {"status": "ok", "updated": list(updated.keys())}

    return router
