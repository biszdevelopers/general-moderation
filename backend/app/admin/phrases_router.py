"""Critical phrase admin endpoints.

Operators manage the high-severity phrase list independently of the general
word bank. Each phrase carries a category and a severity (0-10) that drives
the hard-block and suspicion-score floor policies.
"""

from __future__ import annotations

from typing import Annotated, Any

from fastapi import APIRouter, HTTPException, Query, status
from pydantic import BaseModel, Field

from app.models.admin import CriticalPhraseEntry
from app.phrases.manager import CriticalPhraseManager
from app.phrases.models import CriticalPhrase
from app.utils.unicode_utils import UnicodeUtils


class AddPhraseRequest(BaseModel):
    """Payload for adding a critical phrase.

    :param phrase: the phrase to add
    :param language: ISO 639-1 language code
    :param category: semantic bucket
    :param severity: severity score from 0 to 10
    """

    phrase: Annotated[str, Field(min_length=1, max_length=200)]
    language: str = "any"
    category: str = "other"
    severity: int = Field(default=5, ge=0, le=10)


class UpdatePhraseRequest(BaseModel):
    """Payload for updating a critical phrase.

    :param phrase: optional replacement phrase
    :param language: optional replacement language code
    :param category: optional replacement category
    :param severity: optional replacement severity
    """

    phrase: Annotated[str | None, Field(min_length=1, max_length=200)] = None
    language: str | None = None
    category: str | None = None
    severity: int | None = Field(default=None, ge=0, le=10)


def create_phrases_router(  # noqa: C901 - router factory with many sub-routes
    manager: CriticalPhraseManager,
    auth_dependency: Any,
    engine: Any | None = None,
) -> APIRouter:
    """Build the critical phrase admin router.

    :param manager: the critical phrase manager
    :param auth_dependency: FastAPI dependency guarding the routes
    :param engine: optional engine whose result cache is cleared on changes
    :return: the configured APIRouter
    """
    router: APIRouter = APIRouter(
        prefix="/admin/phrases", tags=["phrases"], dependencies=[auth_dependency]
    )

    @router.post("", response_model=CriticalPhraseEntry, status_code=status.HTTP_201_CREATED)
    def add_phrase(payload: AddPhraseRequest) -> CriticalPhrase:
        """Add a critical phrase.

        :param payload: the phrase to add
        :return: the persisted phrase
        :raises HTTPException: 409 when the phrase already exists
        """
        normalized: str = UnicodeUtils.prepare(payload.phrase).lower()
        try:
            created: CriticalPhrase = manager.add(
                phrase=normalized,
                category=payload.category,
                severity=payload.severity,
                language=payload.language,
            )
        except ValueError as exc:
            raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail=str(exc)) from exc
        if engine is not None:
            engine.clear_cache()
        return created

    @router.delete("")
    def remove_phrase(phrase_id: int = Query(..., ge=1)) -> dict[str, bool]:
        """Remove a critical phrase by id.

        :param phrase_id: identifier of the phrase to remove
        :return: whether a phrase was removed
        """
        removed: bool = manager.remove(phrase_id)
        if removed and engine is not None:
            engine.clear_cache()
        return {"removed": removed}

    @router.get("", response_model=list[CriticalPhraseEntry])
    def list_phrases() -> list[CriticalPhrase]:
        """List every critical phrase.

        :return: the phrases ordered by id ascending
        """
        return manager.list_all()

    @router.put("/{phrase_id}", response_model=CriticalPhraseEntry)
    def update_phrase(phrase_id: int, payload: UpdatePhraseRequest) -> CriticalPhrase:
        """Update an existing critical phrase.

        :param phrase_id: identifier of the phrase to update
        :param payload: fields to change
        :return: the updated phrase
        :raises HTTPException: 404 when the phrase id does not exist
        """
        fields: dict[str, Any] = payload.model_dump(exclude_none=True)
        if "phrase" in fields:
            fields["phrase"] = UnicodeUtils.prepare(str(fields["phrase"])).lower()
        try:
            updated: CriticalPhrase = manager.update(phrase_id, **fields)
        except ValueError as exc:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=str(exc)) from exc
        if engine is not None:
            engine.clear_cache()
        return updated

    return router
