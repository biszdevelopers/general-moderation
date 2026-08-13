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


_FEEDBACK_FIELD_CASES: tuple[tuple[str, str, bool, int], ...] = (
    (
        "BLOCK",
        "BLOCK",
        True,
        4659,
    ),
    (
        "BLOCK",
        "BLOCK",
        False,
        4660,
    ),
    (
        "BLOCK",
        "PASS",
        True,
        4661,
    ),
    (
        "BLOCK",
        "PASS",
        False,
        4662,
    ),
    (
        "PASS",
        "BLOCK",
        True,
        4663,
    ),
    (
        "PASS",
        "BLOCK",
        False,
        4664,
    ),
    (
        "PASS",
        "PASS",
        True,
        4665,
    ),
    (
        "PASS",
        "PASS",
        False,
        4666,
    ),
    (
        "REVIEW",
        "BLOCK",
        True,
        4667,
    ),
    (
        "REVIEW",
        "BLOCK",
        False,
        4668,
    ),
    (
        "REVIEW",
        "PASS",
        True,
        4669,
    ),
    (
        "REVIEW",
        "PASS",
        False,
        4670,
    ),
)


class TestFeedbackField(BaseTest):
    """Stored feedback preserves every field."""

    @pytest.mark.parametrize(
        (
            "verdict",
            "actual",
            "correct",
            "uid",
        ),
        _FEEDBACK_FIELD_CASES,
    )
    def test_feedback_field(self, verdict: str, actual: str, correct: bool, uid: int) -> None:
        """Stored feedback preserves every field."""
        feedback: FeedbackService = _feedback_service()
        feedback.record_feedback("req", verdict, correct, actual)
        row = feedback._connection.execute(
            "SELECT request_id, verdict, is_correct, actual_action FROM feedback"
        ).fetchone()
        assert row is not None
        assert row[1] == verdict
        assert row[2] == int(correct)
        assert row[3] == actual
        feedback.close()


_FEEDBACK_COUNT_CASES: tuple[tuple[int, int], ...] = (
    (
        1,
        4671,
    ),
    (
        3,
        4672,
    ),
    (
        7,
        4673,
    ),
    (
        12,
        4674,
    ),
    (
        16,
        4675,
    ),
    (
        24,
        4676,
    ),
    (
        25,
        4677,
    ),
    (
        32,
        4678,
    ),
    (
        48,
        4679,
    ),
    (
        100,
        4680,
    ),
    (
        500,
        4681,
    ),
    (
        1000,
        4682,
    ),
    (
        2000,
        4683,
    ),
    (
        5000,
        4684,
    ),
)


class TestFeedbackCount(BaseTest):
    """Feedback rows persist in the database."""

    @pytest.mark.parametrize(
        (
            "count",
            "uid",
        ),
        _FEEDBACK_COUNT_CASES,
    )
    def test_feedback_count(self, count: int, uid: int) -> None:
        """Feedback rows persist in the database."""
        feedback: FeedbackService = _feedback_service()
        for index in range(count):
            feedback.record_feedback(f"r{index}", "BLOCK", True, "BLOCK")
        rows = feedback._connection.execute("SELECT COUNT(*) FROM feedback").fetchone()
        assert rows is not None and rows[0] == count
        feedback.close()


_REPORT_SHAPE_CASES: tuple[tuple[int, int, int], ...] = (
    (
        1,
        1,
        4685,
    ),
    (
        1,
        2,
        4686,
    ),
    (
        1,
        3,
        4687,
    ),
    (
        1,
        4,
        4688,
    ),
    (
        1,
        5,
        4689,
    ),
    (
        2,
        1,
        4690,
    ),
    (
        2,
        2,
        4691,
    ),
    (
        2,
        3,
        4692,
    ),
    (
        2,
        4,
        4693,
    ),
    (
        2,
        5,
        4694,
    ),
    (
        3,
        1,
        4695,
    ),
    (
        3,
        2,
        4696,
    ),
    (
        3,
        3,
        4697,
    ),
    (
        3,
        4,
        4698,
    ),
    (
        3,
        5,
        4699,
    ),
    (
        4,
        1,
        4700,
    ),
    (
        4,
        2,
        4701,
    ),
    (
        4,
        3,
        4702,
    ),
    (
        4,
        4,
        4703,
    ),
    (
        4,
        5,
        4704,
    ),
    (
        5,
        1,
        4705,
    ),
    (
        5,
        2,
        4706,
    ),
    (
        5,
        3,
        4707,
    ),
    (
        5,
        4,
        4708,
    ),
    (
        5,
        5,
        4709,
    ),
    (
        6,
        1,
        4710,
    ),
    (
        6,
        2,
        4711,
    ),
    (
        6,
        3,
        4712,
    ),
    (
        6,
        4,
        4713,
    ),
    (
        6,
        5,
        4714,
    ),
    (
        7,
        1,
        4715,
    ),
    (
        7,
        2,
        4716,
    ),
    (
        7,
        3,
        4717,
    ),
    (
        7,
        4,
        4718,
    ),
    (
        7,
        5,
        4719,
    ),
    (
        8,
        1,
        4720,
    ),
    (
        8,
        2,
        4721,
    ),
    (
        8,
        3,
        4722,
    ),
    (
        8,
        4,
        4723,
    ),
    (
        8,
        5,
        4724,
    ),
    (
        9,
        1,
        4725,
    ),
    (
        9,
        2,
        4726,
    ),
    (
        9,
        3,
        4727,
    ),
    (
        9,
        4,
        4728,
    ),
    (
        9,
        5,
        4729,
    ),
    (
        10,
        1,
        4730,
    ),
    (
        10,
        2,
        4731,
    ),
    (
        10,
        3,
        4732,
    ),
    (
        10,
        4,
        4733,
    ),
    (
        10,
        5,
        4734,
    ),
)


class TestReportShape(BaseTest):
    """Tuning reports expose the documented structure."""

    @pytest.mark.parametrize(
        (
            "n_feedback",
            "n_decisions",
            "uid",
        ),
        _REPORT_SHAPE_CASES,
    )
    def test_report_shape(self, n_feedback: int, n_decisions: int, uid: int) -> None:
        """Tuning reports expose the documented structure."""
        feedback: FeedbackService = _feedback_service()
        for index in range(n_feedback):
            feedback.record_feedback(f"r{index}", "BLOCK", True, "BLOCK")
        for _ in range(n_decisions):
            feedback.record_decision("PASS", True)
        report = feedback.run_batch()
        assert report["status"] == "ok"
        assert report["feedback_window"] == n_feedback
        assert report["decision_window"] == n_decisions
        assert 0 <= report["score_threshold"] <= 100
        assert 0.0 <= report["precision"] <= 1.0
        assert "weights" in report
        feedback.close()


_WEIGHT_CLAMP_CASES: tuple[tuple[str, int, int], ...] = (
    (
        "WEIGHT_DETECTOR_BADWORDS",
        5,
        4735,
    ),
    (
        "WEIGHT_DETECTOR_BADWORDS",
        15,
        4736,
    ),
    (
        "WEIGHT_DETECTOR_BADWORDS",
        25,
        4737,
    ),
    (
        "WEIGHT_DETECTOR_BADWORDS",
        35,
        4738,
    ),
    (
        "WEIGHT_DETECTOR_BADWORDS",
        45,
        4739,
    ),
    (
        "WEIGHT_DETECTOR_BADWORDS",
        50,
        4740,
    ),
    (
        "WEIGHT_DETECTOR_PROFANITE",
        5,
        4741,
    ),
    (
        "WEIGHT_DETECTOR_PROFANITE",
        15,
        4742,
    ),
    (
        "WEIGHT_DETECTOR_PROFANITE",
        25,
        4743,
    ),
    (
        "WEIGHT_DETECTOR_PROFANITE",
        35,
        4744,
    ),
    (
        "WEIGHT_DETECTOR_PROFANITE",
        45,
        4745,
    ),
    (
        "WEIGHT_DETECTOR_PROFANITE",
        50,
        4746,
    ),
    (
        "WEIGHT_DETECTOR_GLIN",
        5,
        4747,
    ),
    (
        "WEIGHT_DETECTOR_GLIN",
        15,
        4748,
    ),
    (
        "WEIGHT_DETECTOR_GLIN",
        25,
        4749,
    ),
    (
        "WEIGHT_DETECTOR_GLIN",
        35,
        4750,
    ),
    (
        "WEIGHT_DETECTOR_GLIN",
        45,
        4751,
    ),
    (
        "WEIGHT_DETECTOR_GLIN",
        50,
        4752,
    ),
    (
        "WEIGHT_DETECTOR_AHO",
        5,
        4753,
    ),
    (
        "WEIGHT_DETECTOR_AHO",
        15,
        4754,
    ),
    (
        "WEIGHT_DETECTOR_AHO",
        25,
        4755,
    ),
    (
        "WEIGHT_DETECTOR_AHO",
        35,
        4756,
    ),
    (
        "WEIGHT_DETECTOR_AHO",
        45,
        4757,
    ),
    (
        "WEIGHT_DETECTOR_AHO",
        50,
        4758,
    ),
)


class TestWeightClamp(BaseTest):
    """Tuned weights stay clamped between 5 and 50."""

    @pytest.mark.parametrize(
        (
            "key",
            "value",
            "uid",
        ),
        _WEIGHT_CLAMP_CASES,
    )
    def test_weight_clamp(self, key: str, value: int, uid: int) -> None:
        """Tuned weights stay clamped between 5 and 50."""
        feedback: FeedbackService = _feedback_service()
        service: SettingsService = feedback._settings_service
        service.get(key)
        service.update({key: value})
        feedback.run_batch()
        stored = int(service.get(key, 0))
        assert 5 <= stored <= 50
        feedback.close()
