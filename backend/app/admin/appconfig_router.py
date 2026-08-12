"""Per-application trigger policy endpoints."""

from __future__ import annotations

from typing import Any

from fastapi import APIRouter, HTTPException, status
from pydantic import BaseModel, Field

from app.appconfig.app_config_service import AppConfigService


class AppConfigRequest(BaseModel):
    """The trigger policy for one application.

    :param app_name: the application name
    :param score_threshold: suspicion score that alone forces the LLM
    :param semantic_boost: force the LLM on high semantic similarity
    :param user_ratio_boost: force the LLM on a high user bad-content ratio
    :param logic_type: "or" for any condition, "and" for all conditions
    """

    app_name: str = Field(min_length=1)
    score_threshold: int = Field(default=50, ge=0, le=100)
    semantic_boost: bool = True
    user_ratio_boost: bool = True
    logic_type: str = Field(default="or", pattern="^(and|or)$")


def create_appconfig_router(app_config: AppConfigService, auth_dependency: Any) -> APIRouter:
    """Build the app trigger policy admin router.

    :param app_config: the app configuration service
    :param auth_dependency: FastAPI dependency guarding the routes
    :return: the configured APIRouter
    """
    router: APIRouter = APIRouter(prefix="/admin", tags=["admin"], dependencies=[auth_dependency])

    @router.get("/app-config")
    def list_app_configs() -> dict[str, Any]:
        """Return every stored app policy.

        :return: the app policy list
        """
        return {"apps": app_config.list_all()}

    @router.post("/app-config")
    def set_app_config(payload: AppConfigRequest) -> dict[str, Any]:
        """Create or update one app policy.

        :param payload: the policy to store
        :return: the stored policy
        """
        return app_config.set(
            app_name=payload.app_name,
            score_threshold=payload.score_threshold,
            semantic_boost=payload.semantic_boost,
            user_ratio_boost=payload.user_ratio_boost,
            logic_type=payload.logic_type,
        )

    @router.get("/app-config/{app_name}")
    def get_app_config(app_name: str) -> dict[str, Any]:
        """Return the effective policy for one app.

        :param app_name: the application name
        :return: the effective policy
        :raises HTTPException: 400 when the app name is empty
        """
        if not app_name.strip():
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="app_name required")
        return app_config.get(app_name)

    return router
