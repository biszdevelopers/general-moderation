"""Runtime settings admin endpoints.

``GET /admin/settings`` returns the full setting catalog with descriptions,
validation metadata, and editability flags; ``POST /admin/settings``
validates and persists changes so they apply without a service restart.
History and preset endpoints expose the audit trail and named bundles.
"""

from __future__ import annotations

from typing import Any

from fastapi import APIRouter, HTTPException, status
from pydantic import BaseModel

from app.settings_service import SettingsService

# Settings whose changes require the model router to rebuild its providers.
_MODEL_WATCHLIST: frozenset[str] = frozenset(
    {
        "LLM_PROVIDER",
        "BACKUP_LLM_PROVIDER",
        "ACTIVE_GGUF_PATH",
    }
)


class UpdateSettingsRequest(BaseModel):
    """A batch of settings to update.

    :param settings: settings key to value mapping
    """

    settings: dict[str, Any]


class CreatePresetRequest(BaseModel):
    """A new configuration preset.

    :param name: unique preset name
    :param description: human-readable purpose
    :param payload: settings key to value mapping applied together
    """

    name: str
    description: str = ""
    payload: dict[str, Any]


def create_settings_router(  # noqa: C901 - one handler per endpoint, many typed branches
    settings_service: SettingsService,
    auth_dependency: Any,
    engine: Any | None = None,
) -> APIRouter:
    """Build the runtime settings admin router.

    :param settings_service: the runtime settings service
    :param auth_dependency: FastAPI dependency guarding the routes
    :param engine: optional engine whose detector caches are refreshed after
        a settings change and whose model router is rebuilt when provider
        selection changes
    :return: the configured APIRouter
    """
    router: APIRouter = APIRouter(prefix="/admin", tags=["admin"], dependencies=[auth_dependency])

    @router.get("/settings")
    def get_settings() -> dict[str, list[dict[str, Any]]]:
        """Return the full settings catalog.

        :return: the settings with type, bounds, category, and flags
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
        if engine is not None:
            engine.refresh_detectors()
            if _MODEL_WATCHLIST.intersection(updated):
                engine.refresh_model_router()
        return {"status": "ok", "updated": list(updated.keys())}

    @router.get("/settings/history")
    def history(key: str | None = None, limit: int = 100) -> dict[str, list[dict[str, Any]]]:
        """Return recent configuration changes from the audit trail.

        :param key: optional settings key filter
        :param limit: maximum rows to return (1-1000)
        :return: audit rows newest first with secrets redacted
        """
        return {"history": settings_service.history(key=key, limit=limit)}

    @router.get("/presets")
    def presets() -> dict[str, list[dict[str, Any]]]:
        """Return every configuration preset.

        :return: preset name, description, and payload per entry
        """
        return {"presets": settings_service.presets()}

    @router.post("/presets", status_code=status.HTTP_201_CREATED)
    def create_preset(payload: CreatePresetRequest) -> dict[str, str]:
        """Store a new preset after validating every payload value.

        :param payload: name, description, and settings payload
        :return: creation confirmation
        :raises HTTPException: 400 for duplicate names or invalid values
        """
        try:
            settings_service.create_preset(payload.name, payload.description, payload.payload)
        except ValueError as exc:
            raise HTTPException(status_code=400, detail=str(exc)) from exc
        return {"status": "ok"}

    @router.post("/presets/{name}/apply")
    def apply_preset(name: str) -> dict[str, Any]:
        """Apply a preset as one validated batch update.

        :param name: the preset to apply
        :return: the keys that changed
        :raises HTTPException: 400 for unknown presets or invalid values
        """
        try:
            updated: dict[str, Any] = settings_service.apply_preset(name)
        except ValueError as exc:
            raise HTTPException(status_code=400, detail=str(exc)) from exc
        if engine is not None:
            engine.refresh_detectors()
            if _MODEL_WATCHLIST.intersection(updated):
                engine.refresh_model_router()
        return {"status": "ok", "updated": list(updated.keys())}

    @router.delete("/presets/{name}")
    def delete_preset(name: str) -> dict[str, str]:
        """Remove a preset by name.

        :param name: the preset to delete
        :return: deletion confirmation
        :raises HTTPException: 400 for unknown presets
        """
        try:
            settings_service.delete_preset(name)
        except ValueError as exc:
            raise HTTPException(status_code=400, detail=str(exc)) from exc
        return {"status": "ok"}

    return router
