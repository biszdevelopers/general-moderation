"""Outgoing moderation response models."""

from __future__ import annotations

from pydantic import BaseModel

from app.models.verdict import Verdict


class ModerationResponse(BaseModel):
    """Result of moderating a single message.

    :param id: caller-supplied identifier echoed back from the request
    :param verdict: final decision: PASS, BLOCK, or REVIEW
    :param level_used: detection level that produced the verdict (1 or 2)
    :param reasons: human-readable reasons for the verdict
    :param matched_words: the offending words that were matched
    :param matched_language: ISO code of the detected language, if known
    :param confidence_score: overall confidence in the verdict
    :param latency_ms: total processing time in milliseconds
    :param detector_chain: ordered names of detectors that ran
    """

    id: str | None = None
    verdict: Verdict
    level_used: int
    reasons: list[str] = []
    matched_words: list[str] = []
    matched_language: str | None = None
    confidence_score: float | None = None
    latency_ms: float
    detector_chain: list[str] = []


class BatchModerationResponse(BaseModel):
    """Result of moderating a batch of messages.

    :param results: one response per input item, in request order
    :param total_latency_ms: wall-clock time for the whole batch
    """

    results: list[ModerationResponse]
    total_latency_ms: float
