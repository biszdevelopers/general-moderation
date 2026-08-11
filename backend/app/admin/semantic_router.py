"""Semantic similarity index management endpoints."""

from __future__ import annotations

from typing import Any

from fastapi import APIRouter, HTTPException, status
from pydantic import BaseModel, Field

from app.semantic.semantic_service import CATEGORIES, SemanticService


class SemanticRequest(BaseModel):
    """One semantic index mutation.

    :param action: "add" or "delete"
    :param category: one of the semantic categories
    :param text: the sensitive example text
    """

    action: str = Field(pattern="^(add|delete)$")
    category: str
    text: str = Field(min_length=1)


def create_semantic_router(semantic_service: SemanticService, auth_dependency: Any) -> APIRouter:
    """Build the semantic index admin router.

    :param semantic_service: the semantic similarity service
    :param auth_dependency: FastAPI dependency guarding the routes
    :return: the configured APIRouter
    """
    router: APIRouter = APIRouter(prefix="/admin", tags=["admin"], dependencies=[auth_dependency])

    @router.get("/semantic")
    def semantic_status() -> dict[str, Any]:
        """Return the semantic stage status and categories.

        :return: availability, model, and per-category entry counts
        """
        return semantic_service.stats()

    @router.post("/semantic")
    def semantic_mutation(payload: SemanticRequest) -> dict[str, str]:
        """Add or delete one sensitive example from a category index.

        :param payload: the mutation to apply
        :return: an acknowledgment
        :raises HTTPException: 400 for an unknown category or empty text
        :raises HTTPException: 404 when deleting a missing example
        """
        try:
            if payload.action == "add":
                semantic_service.add(payload.category, payload.text)
            else:
                removed: bool = semantic_service.delete(payload.category, payload.text)
                if not removed:
                    raise HTTPException(
                        status_code=status.HTTP_404_NOT_FOUND,
                        detail="Example not found in the category index",
                    )
        except ValueError as exc:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(exc)) from exc
        return {"status": "ok"}

    @router.get("/semantic/categories")
    def semantic_categories() -> dict[str, list[str]]:
        """Return the supported semantic categories.

        :return: the category names
        """
        return {"categories": list(CATEGORIES)}

    return router
