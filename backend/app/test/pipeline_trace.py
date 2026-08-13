"""Detailed pipeline trace data classes.

Each trace records what actually happened at every stage of a moderation
request: which detectors ran, what they found, how the suspicion score was
assembled, and whether the LLM was consulted. The objects are consumed by the
``/test`` endpoints and rendered by the test workbench UI.

The classes carry no logic beyond plain data holders; the engine populates
them while executing the pipeline.
"""

from __future__ import annotations

from dataclasses import asdict, dataclass, field
from typing import Any


@dataclass(frozen=True, slots=True)
class DetectorRunTrace:
    """One detector execution inside Stage 2.

    :param name: detector identifier
    :param enabled: whether the runtime toggle allowed the detector to run
    :param available: whether the detector reported itself usable
    :param matched: whether the detector flagged the text
    :param blocking: whether a match alone yields a BLOCK verdict
    :param confidence: detector confidence in 0.0-1.0, when reported
    :param matched_words: words or phrases that triggered the detector
    :param matched_language: ISO code of the detected language, if known
    :param reason: human-readable explanation of the match
    :param latency_ms: wall time spent in the detector
    :param weight: suspicion points the detector contributes on a match
    """

    name: str
    enabled: bool
    available: bool
    matched: bool
    blocking: bool
    confidence: float | None = None
    matched_words: list[str] = field(default_factory=list)
    matched_language: str | None = None
    reason: str | None = None
    latency_ms: float = 0.0
    weight: int = 0


@dataclass(frozen=True, slots=True)
class WeightContribution:
    """One line of the suspicion score breakdown.

    :param kind: "detector", "semantic", or "user"
    :param name: contributing component name
    :param value: the measured signal (1 for a hit, similarity, or ratio)
    :param weight: the configured weight
    :param contributed: points added to the score by this component
    """

    kind: str
    name: str
    value: float
    weight: float
    contributed: float


@dataclass(frozen=True, slots=True)
class Stage1Trace:
    """Stage 1 fast path details.

    :param fast_path: whether the safe word list exited the pipeline
    :param verdict: the verdict produced by Stage 1
    :param latency_ms: wall time spent in Stage 1
    """

    fast_path: bool
    verdict: str
    latency_ms: float = 0.0


@dataclass(frozen=True, slots=True)
class Stage2Trace:
    """Stage 2 detector, semantic, and user profile details.

    :param detector_results: per-detector execution records
    :param semantic_similarities: category to similarity mapping
    :param semantic_enabled: whether the semantic stage was active
    :param user_profile: profiler snapshot, or None when disabled
    :param suspicion_score: the computed 0-100 score
    :param weight_contributions: score breakdown lines
    :param latency_ms: wall time spent in Stage 2
    """

    detector_results: list[DetectorRunTrace] = field(default_factory=list)
    semantic_similarities: dict[str, float] = field(default_factory=dict)
    semantic_enabled: bool = False
    user_profile: dict[str, Any] | None = None
    suspicion_score: float = 0.0
    weight_contributions: list[WeightContribution] = field(default_factory=list)
    latency_ms: float = 0.0


@dataclass(frozen=True, slots=True)
class Stage3Trace:
    """Stage 3 LLM details.

    :param invoked: whether the LLM was called
    :param trigger: human-readable reason the LLM was forced
    :param model_available: whether the local model was loaded
    :param prompt: the exact prompt sent to the model
    :param response: the raw model reply
    :param verdict: the model verdict (BLOCK or ALLOW)
    :param confidence: confidence attached to the model verdict
    :param latency_ms: wall time spent in the LLM call
    """

    invoked: bool = False
    trigger: str | None = None
    model_available: bool = False
    prompt: str | None = None
    response: str | None = None
    verdict: str | None = None
    confidence: float | None = None
    latency_ms: float = 0.0


@dataclass(frozen=True, slots=True)
class PipelineTrace:
    """Full trace of one moderation request.

    :param request_id: caller-supplied request identifier
    :param app_name: calling application name
    :param user_id: calling user identifier
    :param text: the moderated message
    :param verdict: final verdict
    :param suspicion_score: the computed 0-100 score
    :param level_used: detection level that produced the verdict
    :param ai_triggered: whether the LLM was invoked
    :param reasons: accumulated reasons
    :param matched_words: matched words
    :param matched_language: detected language, if any
    :param confidence_score: overall confidence, if any
    :param stage_1: Stage 1 details
    :param stage_2: Stage 2 details
    :param stage_3: Stage 3 details, when the LLM was consulted
    :param total_latency_ms: total processing time in milliseconds
    """

    request_id: str | None
    app_name: str
    user_id: str | None
    text: str
    verdict: str
    suspicion_score: float
    level_used: int
    ai_triggered: bool
    reasons: list[str] = field(default_factory=list)
    matched_words: list[str] = field(default_factory=list)
    matched_language: str | None = None
    confidence_score: float | None = None
    stage_1: Stage1Trace = field(default_factory=Stage1Trace)
    stage_2: Stage2Trace = field(default_factory=Stage2Trace)
    stage_3: Stage3Trace | None = None
    total_latency_ms: float = 0.0

    def to_dict(self) -> dict[str, Any]:
        """Serialize the trace to a plain JSON-ready mapping.

        :return: the trace as nested dictionaries
        """
        return asdict(self)
