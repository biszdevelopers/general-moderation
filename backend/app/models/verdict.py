"""Verdict enumeration and the shared detection result DTO."""

from __future__ import annotations

from dataclasses import dataclass, field
from enum import StrEnum


class Verdict(StrEnum):
    """Final decision returned for a moderated message."""

    PASS = "PASS"
    BLOCK = "BLOCK"
    REVIEW = "REVIEW"


@dataclass(frozen=True)
class DetectionResult:
    """Output produced by a single detector in the pipeline.

    :param matched: whether the detector flagged the text
    :param matched_words: words or phrases that triggered the detector
    :param matched_language: ISO code of the detected language, if known
    :param reason: human-readable explanation of the match
    :param confidence_score: optional confidence in the 0.0-1.0 range
    """

    matched: bool
    matched_words: tuple[str, ...] = field(default_factory=tuple)
    matched_language: str | None = None
    reason: str | None = None
    confidence_score: float | None = None
