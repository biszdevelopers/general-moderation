"""Suspicion score calculation.

The score is a weighted sum of detector hits, semantic category hits, and the
user bad-content ratio, clamped to the 0-100 range:

.. math::

    score = \\sum_{d \\in D} hit_d \\cdot w_d
          + \\sum_{c \\in C} [s_c > \\theta_c] \\cdot w_c
          + ratio_{user} \\cdot w_{user}
"""

from __future__ import annotations

from typing import Any

_WEIGHT_KEYS: dict[str, str] = {
    "badwords": "WEIGHT_DETECTOR_BADWORDS",
    "profanite": "WEIGHT_DETECTOR_PROFANITE",
    "glin-profanity": "WEIGHT_DETECTOR_GLIN",
    "aho_corasick": "WEIGHT_DETECTOR_AHO",
    "bk_tree": "WEIGHT_DETECTOR_BKTREE",
    "double_metaphone": "WEIGHT_DETECTOR_METAPHONE",
    "multi_language": "WEIGHT_DETECTOR_BADWORDS",
    "sensitive_stop_words": "WEIGHT_DETECTOR_AHO",
    "rolling_hash": "WEIGHT_DETECTOR_AHO",
    "bloom_filter": "WEIGHT_DETECTOR_AHO",
}

_CATEGORY_KEYS: dict[str, str] = {
    "political": "WEIGHT_SEMANTIC_POLITICAL",
    "violence": "WEIGHT_SEMANTIC_VIOLENCE",
    "sexual": "WEIGHT_SEMANTIC_SEXUAL",
    "hate": "WEIGHT_SEMANTIC_HATE",
    "pii": "WEIGHT_SEMANTIC_PII",
    "ads": "WEIGHT_SEMANTIC_ADS",
    "other": "WEIGHT_SEMANTIC_POLITICAL",
}


class SuspicionScorer:
    """Computes the 0-100 suspicion score from weighted signals.

    :param settings_service: runtime settings used to resolve live weights
    """

    def __init__(self, settings_service: Any) -> None:
        self._settings: Any = settings_service

    def detector_weight(self, detector_name: str) -> int:
        """Resolve the configured weight for one detector.

        :param detector_name: detector identifier
        :return: the configured weight, or 0 when unknown
        """
        key: str | None = _WEIGHT_KEYS.get(detector_name)
        if key is None:
            return 0
        return int(self._settings.get(key, 0) or 0)

    def _category_weight(self, category: str) -> int:
        """Resolve the configured weight for one semantic category.

        :param category: semantic category name
        :return: the configured weight, or 0 when unknown
        """
        key: str = _CATEGORY_KEYS.get(category, "WEIGHT_SEMANTIC_POLITICAL")
        return int(self._settings.get(key, 0) or 0)

    def score(
        self,
        *,
        detector_names: list[str] | None = None,
        semantic_similarities: dict[str, float] | None = None,
        user_ratio: float = 0.0,
        max_severity: int = 0,
    ) -> float:
        """Compute the suspicion score for one request.

        Severity acts as a floor: a match whose severity is at least three
        lifts the score so ambiguous high-severity content clears the review
        escalation threshold. Low-severity matches (the default for ordinary
        custom words) leave the score unchanged, preserving existing behavior.

        :param detector_names: detectors that matched this request
        :param semantic_similarities: per-category similarities, in 0-1
        :param user_ratio: the user bad-content ratio, in 0-1
        :param max_severity: severity of the strongest match, 0-10
        :return: a score clamped to the 0-100 range
        """
        raw: float = 0.0
        for name in detector_names or []:
            raw += self.detector_weight(name)
        threshold: float = float(self._settings.get("SEMANTIC_SIMILARITY_THRESHOLD", 0.85))
        for category, similarity in (semantic_similarities or {}).items():
            if similarity > threshold:
                raw += self._category_weight(category)
        user_weight: int = int(self._settings.get("WEIGHT_USER", 0) or 0)
        raw += user_ratio * user_weight
        severity_floor: float = self._severity_floor(max_severity)
        if severity_floor > raw:
            raw = severity_floor
        return max(0.0, min(100.0, raw))

    @staticmethod
    def _severity_floor(max_severity: int) -> float:
        """Return the suspicion floor for a severity value.

        Severity below three contributes nothing so ordinary custom words
        (severity 1) keep the historical score exactly.

        :param max_severity: the strongest matched severity, 0-10
        :return: the floor, e.g. 30 points for severity 5
        """
        if max_severity < 3:
            return 0.0
        return float((max_severity - 2) * 10)
