"""Phase 2 auto-tuning tests (generated).

Precision deltas, threshold pass-rate sweeps, decay half-lives and
report structure under the frozen clock."""

# multilingual fixtures use non-ASCII on purpose
from __future__ import annotations

import pytest

from app.appconfig.app_config_service import AppConfigService
from app.config import Settings
from app.feedback.feedback_service import FeedbackService
from app.settings_service import SettingsService
from app.utils.logger import ModerationLogger
from tests.base_test import BaseTest


def _feedback_service(enabled: bool = True) -> FeedbackService:
    import tempfile
    from pathlib import Path

    root: Path = Path(tempfile.mkdtemp())
    (root / "logs").mkdir(parents=True, exist_ok=True)
    settings = Settings(
        app_port=0,
        log_file_path=str(root / "logs" / "l.log"),
        feedback_db_path=str(root / "f.db"),
        settings_db_path=str(root / "s.db"),
        app_config_db_path=str(root / "c.db"),
        auto_tuning_enabled=enabled,
    )
    logger: ModerationLogger = ModerationLogger(settings.log_file_path, max_bytes=100_000)
    settings_service: SettingsService = SettingsService(settings)
    app_config: AppConfigService = AppConfigService(settings.app_config_db_path)
    return FeedbackService(settings, settings_service, app_config, logger)


_PRECISION_DELTA_CASES: tuple[tuple[int, int, int, int], ...] = (
    (
        2,
        30,
        -1,
        4359,
    ),
    (
        3,
        30,
        -1,
        4360,
    ),
    (
        4,
        30,
        -1,
        4361,
    ),
    (
        5,
        30,
        -1,
        4362,
    ),
    (
        6,
        30,
        -1,
        4363,
    ),
    (
        7,
        30,
        -1,
        4364,
    ),
    (
        8,
        30,
        -1,
        4365,
    ),
    (
        9,
        30,
        -1,
        4366,
    ),
    (
        10,
        30,
        -1,
        4367,
    ),
    (
        11,
        30,
        -1,
        4368,
    ),
    (
        12,
        30,
        0,
        4369,
    ),
    (
        13,
        30,
        0,
        4370,
    ),
    (
        14,
        30,
        0,
        4371,
    ),
    (
        15,
        30,
        0,
        4372,
    ),
    (
        16,
        30,
        0,
        4373,
    ),
    (
        17,
        30,
        0,
        4374,
    ),
    (
        18,
        30,
        0,
        4375,
    ),
    (
        19,
        30,
        1,
        4376,
    ),
    (
        20,
        30,
        1,
        4377,
    ),
    (
        21,
        30,
        1,
        4378,
    ),
    (
        22,
        30,
        1,
        4379,
    ),
    (
        23,
        30,
        1,
        4380,
    ),
    (
        24,
        30,
        1,
        4381,
    ),
    (
        25,
        30,
        1,
        4382,
    ),
    (
        26,
        30,
        1,
        4383,
    ),
    (
        27,
        30,
        1,
        4384,
    ),
    (
        28,
        30,
        1,
        4385,
    ),
    (
        29,
        30,
        1,
        4386,
    ),
    (
        30,
        30,
        1,
        4387,
    ),
    (
        0,
        40,
        -1,
        4388,
    ),
    (
        1,
        40,
        -1,
        4389,
    ),
    (
        2,
        40,
        -1,
        4390,
    ),
    (
        3,
        40,
        -1,
        4391,
    ),
    (
        4,
        40,
        -1,
        4392,
    ),
    (
        5,
        40,
        -1,
        4393,
    ),
    (
        6,
        40,
        -1,
        4394,
    ),
    (
        7,
        40,
        -1,
        4395,
    ),
    (
        8,
        40,
        -1,
        4396,
    ),
    (
        9,
        40,
        -1,
        4397,
    ),
    (
        10,
        40,
        -1,
        4398,
    ),
    (
        11,
        40,
        -1,
        4399,
    ),
    (
        12,
        40,
        -1,
        4400,
    ),
    (
        13,
        40,
        -1,
        4401,
    ),
    (
        14,
        40,
        -1,
        4402,
    ),
    (
        15,
        40,
        -1,
        4403,
    ),
    (
        16,
        40,
        0,
        4404,
    ),
    (
        17,
        40,
        0,
        4405,
    ),
    (
        18,
        40,
        0,
        4406,
    ),
    (
        19,
        40,
        0,
        4407,
    ),
    (
        20,
        40,
        0,
        4408,
    ),
)


class TestPrecisionDelta(BaseTest):
    """Weights move with precision relative to 0.5."""

    @pytest.mark.parametrize(
        (
            "correct",
            "total",
            "expected",
            "uid",
        ),
        _PRECISION_DELTA_CASES,
    )
    def test_precision_delta(self, correct: int, total: int, expected: int, uid: int) -> None:
        """Weights move with precision relative to 0.5."""
        feedback: FeedbackService = _feedback_service()
        service: SettingsService = feedback._settings_service
        before = int(service.get("WEIGHT_DETECTOR_AHO", 30))
        for index in range(total):
            feedback.record_feedback(f"r{index}", "BLOCK", index < correct, "BLOCK")
        feedback.run_batch()
        after = int(service.get("WEIGHT_DETECTOR_AHO", 30))
        delta = (after > before) - (after < before)
        assert delta == expected
        feedback.close()


_THRESHOLD_PASS_RATE_CASES: tuple[tuple[int, int, int, int], ...] = (
    (
        0,
        2,
        -1,
        4409,
    ),
    (
        1,
        2,
        -1,
        4410,
    ),
    (
        2,
        2,
        1,
        4411,
    ),
    (
        0,
        4,
        -1,
        4412,
    ),
    (
        1,
        4,
        -1,
        4413,
    ),
    (
        2,
        4,
        -1,
        4414,
    ),
    (
        3,
        4,
        0,
        4415,
    ),
    (
        4,
        4,
        1,
        4416,
    ),
    (
        0,
        6,
        -1,
        4417,
    ),
    (
        1,
        6,
        -1,
        4418,
    ),
    (
        2,
        6,
        -1,
        4419,
    ),
    (
        3,
        6,
        -1,
        4420,
    ),
    (
        4,
        6,
        -1,
        4421,
    ),
    (
        5,
        6,
        0,
        4422,
    ),
    (
        6,
        6,
        1,
        4423,
    ),
    (
        0,
        8,
        -1,
        4424,
    ),
    (
        1,
        8,
        -1,
        4425,
    ),
    (
        2,
        8,
        -1,
        4426,
    ),
    (
        3,
        8,
        -1,
        4427,
    ),
    (
        4,
        8,
        -1,
        4428,
    ),
    (
        5,
        8,
        -1,
        4429,
    ),
    (
        6,
        8,
        0,
        4430,
    ),
    (
        7,
        8,
        0,
        4431,
    ),
    (
        8,
        8,
        1,
        4432,
    ),
    (
        0,
        10,
        -1,
        4433,
    ),
    (
        1,
        10,
        -1,
        4434,
    ),
    (
        2,
        10,
        -1,
        4435,
    ),
    (
        3,
        10,
        -1,
        4436,
    ),
    (
        4,
        10,
        -1,
        4437,
    ),
    (
        5,
        10,
        -1,
        4438,
    ),
    (
        6,
        10,
        -1,
        4439,
    ),
    (
        7,
        10,
        -1,
        4440,
    ),
    (
        8,
        10,
        0,
        4441,
    ),
    (
        9,
        10,
        0,
        4442,
    ),
    (
        10,
        10,
        1,
        4443,
    ),
    (
        0,
        15,
        -1,
        4444,
    ),
    (
        1,
        15,
        -1,
        4445,
    ),
    (
        2,
        15,
        -1,
        4446,
    ),
    (
        3,
        15,
        -1,
        4447,
    ),
    (
        4,
        15,
        -1,
        4448,
    ),
    (
        5,
        15,
        -1,
        4449,
    ),
    (
        6,
        15,
        -1,
        4450,
    ),
    (
        7,
        15,
        -1,
        4451,
    ),
    (
        8,
        15,
        -1,
        4452,
    ),
    (
        9,
        15,
        -1,
        4453,
    ),
    (
        10,
        15,
        -1,
        4454,
    ),
    (
        11,
        15,
        0,
        4455,
    ),
    (
        12,
        15,
        0,
        4456,
    ),
    (
        13,
        15,
        0,
        4457,
    ),
    (
        14,
        15,
        1,
        4458,
    ),
)


class TestThresholdPassRate(BaseTest):
    """The threshold rises on high pass rate and falls on high block rate."""

    @pytest.mark.parametrize(
        (
            "passes",
            "total",
            "expected",
            "uid",
        ),
        _THRESHOLD_PASS_RATE_CASES,
    )
    def test_threshold_pass_rate(self, passes: int, total: int, expected: int, uid: int) -> None:
        """The threshold rises on high pass rate and falls on high block rate."""
        feedback: FeedbackService = _feedback_service()
        app_config: AppConfigService = feedback._app_config
        before = int(app_config.get(None)["score_threshold"])
        for index in range(total):
            feedback.record_decision("PASS" if index < passes else "BLOCK", True)
        feedback.run_batch()
        after = int(app_config.get(None)["score_threshold"])
        delta = (after > before) - (after < before)
        assert delta == expected
        feedback.close()
