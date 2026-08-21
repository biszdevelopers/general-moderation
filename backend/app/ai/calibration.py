"""Confidence calibration for Stage 3 verdicts.

Raw provider confidence values are coarse (a BLOCK token carries no
graded certainty). The calibrator maps each verdict onto the configured
block/allow confidence bounds and nudges the value with the Stage 2
suspicion score so borderline text lands closer to 0.5 and clear-cut
text lands near the bounds.
"""

from __future__ import annotations

from typing import Any

from app.ai.providers.interface import ProviderResult

_BLEND_FACTOR: float = 0.5


class ConfidenceCalibrator:
    """Blends raw verdicts with the rule-based suspicion score.

    :param settings_service: runtime settings holding the calibration keys
    """

    def __init__(self, settings_service: Any) -> None:
        self._settings_service: Any = settings_service

    def calibrate(self, result: ProviderResult, suspicion_score: float) -> float:
        """Return the calibrated confidence for one classification.

        :param result: the raw provider result
        :param suspicion_score: the Stage 2 score, 0 to 100
        :return: the calibrated confidence clamped to 0.0-1.0
        """
        if not bool(self._settings_service.get("CALIBRATION_ENABLED", True)):
            return round(min(1.0, max(0.0, result.confidence)), 4)
        ratio: float = min(1.0, max(0.0, suspicion_score / 100.0))
        # ponytail: linear blend, replace with isotonic regression fitted on
        # feedback data when calibration quality measurably matters.
        if result.blocked:
            base: float = float(self._settings_service.get("CALIBRATION_BLOCK_CONFIDENCE", 0.9))
            calibrated: float = base + (1.0 - base) * ratio * _BLEND_FACTOR
        else:
            base = float(self._settings_service.get("CALIBRATION_ALLOW_CONFIDENCE", 0.35))
            calibrated = base - base * ratio * _BLEND_FACTOR
        return round(min(1.0, max(0.0, calibrated)), 4)
