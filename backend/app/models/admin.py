"""Admin API response models.

Admin responses serialize with camelCase aliases to match the API contract
used by the React console, while Python handlers keep snake_case field names.
"""

from __future__ import annotations

from pydantic import BaseModel, ConfigDict
from pydantic.alias_generators import to_camel


class AdminModel(BaseModel):
    """Base model that serializes fields with camelCase aliases."""

    model_config = ConfigDict(alias_generator=to_camel, populate_by_name=True)


class DetectorStatus(AdminModel):
    """Availability of one detector.

    :param name: detector identifier
    :param available: whether the detector can run
    """

    name: str
    available: bool


class WordBankStats(AdminModel):
    """Word bank summary statistics.

    :param total_words: total words in the snapshot
    :param custom_words: administrator-added words
    :param base_words: built-in dictionary words
    :param languages: distinct language codes
    :param categories: distinct categories
    """

    total_words: int
    custom_words: int
    base_words: int
    languages: int
    categories: int


class HealthReport(AdminModel):
    """Detailed service health report.

    :param status: service status
    :param uptime_seconds: seconds since the worker started
    :param word_count: word bank statistics
    :param llama_available: whether the LLM model is loaded
    :param detectors: per-detector availability
    """

    status: str
    uptime_seconds: float
    word_count: WordBankStats
    llama_available: bool
    detectors: list[DetectorStatus]


class WordEntry(AdminModel):
    """A custom word returned by the word bank API.

    :param id: storage-assigned identifier
    :param word: the normalized term
    :param language: ISO 639-1 language code, or "any"
    :param category: semantic bucket
    :param severity: integer severity
    :param created_at: ISO 8601 UTC creation timestamp
    """

    id: int
    word: str
    language: str
    category: str
    severity: int
    created_at: str
