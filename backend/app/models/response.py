"""Outgoing moderation response models.

Responses serialize with camelCase aliases to match the API contract used by
clients, while Python callers construct them with snake_case field names.
"""

from __future__ import annotations

from pydantic import BaseModel, ConfigDict
from pydantic.alias_generators import to_camel

from app.models.verdict import Verdict


class ModerationResponse(BaseModel):
    """Result of moderating a single message.

    :param id: caller-supplied identifier echoed back from the request
    :param verdict: final decision: PASS, BLOCK, or REVIEW
    :param allowed: whether the message may be published
    :param level_used: detection level that produced the verdict (1 or 2)
    :param ai_triggered: whether the LLM was invoked
    :param suspicion_score: the 0-100 suspicion score
    :param reasons: human-readable reasons for the verdict
    :param reason: the primary reason, for simple clients
    :param matched_words: the offending words that were matched
    :param matched_word: the primary matched word, for simple clients
    :param matched_language: ISO code of the detected language, if known
    :param confidence_score: overall confidence in the verdict
    :param latency_ms: total processing time in milliseconds
    :param detector_chain: ordered names of detectors that ran
    """

    model_config = ConfigDict(alias_generator=to_camel, populate_by_name=True)

    id: str | None = None
    verdict: Verdict
    allowed: bool = True
    level_used: int
    ai_triggered: bool = False
    suspicion_score: float = 0.0
    reasons: list[str] = []
    reason: str | None = None
    matched_words: list[str] = []
    matched_word: str | None = None
    matched_language: str | None = None
    confidence_score: float | None = None
    latency_ms: float
    detector_chain: list[str] = []


class BatchModerationResponse(BaseModel):
    """Result of moderating a batch of messages.

    :param results: one response per input item, in request order
    :param total_latency_ms: wall-clock time for the whole batch
    """

    model_config = ConfigDict(alias_generator=to_camel, populate_by_name=True)

    results: list[ModerationResponse]
    total_latency_ms: float
