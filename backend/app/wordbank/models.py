"""Data models for the custom word bank."""

from __future__ import annotations

from dataclasses import dataclass
from enum import Enum


class WordCategory(str, Enum):
    """Semantic bucket for a custom word."""

    PROFANITY = "profanity"
    VIOLENCE = "violence"
    POLITICAL = "political"
    HATE_SPEECH = "hate_speech"
    SEXUAL = "sexual"
    OTHER = "other"


@dataclass(frozen=True)
class CustomWord:
    """A single custom word stored in the word bank.

    :param id: storage-assigned identifier
    :param word: the term, already NFKC-normalized and lowercased
    :param language: ISO 639-1 language code, or "any"
    :param category: semantic bucket from WordCategory
    :param severity: integer severity, higher is more severe
    :param created_at: ISO 8601 UTC timestamp of creation
    """

    id: int
    word: str
    language: str
    category: str
    severity: int
    created_at: str
