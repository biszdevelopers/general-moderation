"""Custom word list admin endpoints.

All inputs are validated by Pydantic (Rust core) before reaching the word
bank; words are normalized with the C-backed Unicode pipeline.
"""

from __future__ import annotations

from typing import Annotated, Any

from fastapi import APIRouter, HTTPException, Query, status
from pydantic import BaseModel, Field

from app.models.admin import WordEntry
from app.utils.unicode_utils import UnicodeUtils
from app.wordbank.manager import WordBankManager
from app.wordbank.models import CustomWord, WordCategory


class AddWordRequest(BaseModel):
    """Payload for adding a custom word.

    :param word: the term to add
    :param language: ISO 639-1 language code
    :param category: semantic bucket
    :param severity: severity score
    """

    word: Annotated[str, Field(min_length=1, max_length=200)]
    language: str = "any"
    category: str = WordCategory.OTHER.value
    severity: int = Field(default=1, ge=0, le=10)


class UpdateWordRequest(BaseModel):
    """Payload for updating a custom word.

    :param word: optional replacement term
    :param language: optional replacement language code
    :param category: optional replacement category
    :param severity: optional replacement severity
    """

    word: Annotated[str | None, Field(min_length=1, max_length=200)] = None
    language: str | None = None
    category: str | None = None
    severity: int | None = Field(default=None, ge=0, le=10)


def create_wordlist_router(word_bank: WordBankManager, auth_dependency: Any) -> APIRouter:
    """Build the custom word list router with dependency injection.

    :param word_bank: the shared word bank manager
    :param auth_dependency: FastAPI dependency guarding the routes
    :return: the configured APIRouter
    """
    router: APIRouter = APIRouter(
        prefix="/admin/wordbank", tags=["wordlist"], dependencies=[auth_dependency]
    )

    @router.post("/words", response_model=WordEntry, status_code=status.HTTP_201_CREATED)
    def add_word(payload: AddWordRequest) -> CustomWord:
        """Add a custom word to the word bank.

        :param payload: the word to add
        :return: the persisted word
        :raises HTTPException: 409 when the word already exists
        """
        normalized: str = UnicodeUtils.prepare(payload.word).lower()
        try:
            return word_bank.add_word(
                word=normalized,
                language=payload.language,
                category=payload.category,
                severity=payload.severity,
            )
        except ValueError as exc:
            raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail=str(exc)) from exc

    @router.delete("/words")
    def remove_word(word_id: int = Query(..., ge=1)) -> dict[str, bool]:
        """Remove a custom word by its identifier.

        :param word_id: identifier of the word to remove
        :return: whether a word was removed
        """
        return {"removed": word_bank.remove_word(word_id)}

    @router.get("/words", response_model=list[WordEntry])
    def list_words(search: str | None = None) -> list[CustomWord]:
        """List custom words, optionally filtered by a search term.

        :param search: optional substring filter
        :return: the matching custom words
        """
        words: list[CustomWord] = word_bank.get_all_words()
        if search:
            needle: str = UnicodeUtils.prepare(search).lower()
            words = [word for word in words if needle in word.word]
        return words

    @router.put("/words/{word_id}", response_model=WordEntry)
    def update_word(word_id: int, payload: UpdateWordRequest) -> CustomWord:
        """Update an existing custom word.

        :param word_id: identifier of the word to update
        :param payload: fields to change
        :return: the updated word
        :raises HTTPException: 404 when the word id does not exist
        """
        fields: dict[str, Any] = payload.model_dump(exclude_none=True)
        if "word" in fields:
            fields["word"] = UnicodeUtils.prepare(str(fields["word"])).lower()
        try:
            return word_bank.update_word(word_id, **fields)
        except ValueError as exc:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=str(exc)) from exc

    return router
