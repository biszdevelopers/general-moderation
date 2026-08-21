"""Editable system prompt admin endpoints.

The prompt is versioned: every save creates a new version, and any
version can be reactivated. Activation pushes the template into the
model router immediately.
"""

from __future__ import annotations

from typing import Any

from fastapi import APIRouter, HTTPException
from pydantic import BaseModel


class PromptUpdateRequest(BaseModel):
    """A new system prompt template.

    :param template: the prompt text
    """

    template: str


def create_prompt_router(
    store: Any,
    on_change: Any,
    auth_dependency: Any,
) -> APIRouter:
    """Build the system prompt admin router.

    :param store: the PromptStore
    :param on_change: zero-argument callback invoked after activation
    :param auth_dependency: FastAPI dependency guarding the routes
    :return: the configured APIRouter
    """
    api: APIRouter = APIRouter(
        prefix="/admin/prompt", tags=["admin"], dependencies=[auth_dependency]
    )

    @api.get("")
    def get_prompt() -> dict[str, str]:
        """Return the active system prompt text.

        :return: the current template
        """
        return {"template": store.get_active()}

    @api.put("")
    def update_prompt(payload: PromptUpdateRequest) -> dict[str, Any]:
        """Save a new prompt version and make it active.

        :param payload: the new template text
        :return: the created version id
        :raises HTTPException: 400 for an empty template
        """
        try:
            version_id: int = store.save(payload.template)
        except ValueError as exc:
            raise HTTPException(status_code=400, detail=str(exc)) from exc
        on_change()
        return {"status": "ok", "version_id": version_id}

    @api.get("/versions")
    def versions() -> dict[str, list[dict[str, Any]]]:
        """Return every stored prompt version.

        :return: versions newest first with previews and active flags
        """
        return {"versions": store.list_versions()}

    @api.post("/versions/{version_id}/activate")
    def activate(version_id: int) -> dict[str, Any]:
        """Reactivate a stored version.

        :param version_id: the version to activate
        :return: confirmation
        :raises HTTPException: 400 for unknown ids
        """
        try:
            store.activate(version_id)
        except ValueError as exc:
            raise HTTPException(status_code=400, detail=str(exc)) from exc
        on_change()
        return {"status": "ok"}

    return api
