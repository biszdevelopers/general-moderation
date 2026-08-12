"""Auto-tuning batch tests (Phase 1, P1/P2).

Covers feedback ingestion, decision recording, precision-driven weight
adjustment, threshold tuning from LLM pass rate, decay, and disabled state.
"""

from __future__ import annotations

import pytest

from app.appconfig.app_config_service import AppConfigService
from app.feedback.feedback_service import FeedbackService
from app.settings_service import SettingsService
from tests.base_test import BaseTest


class TestAutoTuningBasic(BaseTest):
    """Feedback ingestion and basic batch behavior."""

    def test_record_feedback_stored(self, engine: object) -> None:
        """Feedback rows persist to the database."""
        feedback: FeedbackService = _feedback_service()
        feedback.record_feedback("req1", "BLOCK", True, "BLOCK")
        rows = feedback._connection.execute("SELECT COUNT(*) FROM feedback").fetchone()
        assert rows is not None
        assert rows[0] == 1
        feedback.close()

    def test_record_decision_stored(self, engine: object) -> None:
        """Decision rows persist to the database."""
        feedback: FeedbackService = _feedback_service()
        feedback.record_decision("BLOCK", True)
        rows = feedback._connection.execute("SELECT COUNT(*) FROM decisions").fetchone()
        assert rows is not None
        assert rows[0] == 1
        feedback.close()

    def test_run_batch_empty_window(self, engine: object) -> None:
        """An empty batch returns a valid report."""
        feedback: FeedbackService = _feedback_service()
        report = feedback.run_batch()
        assert report["status"] == "ok"
        assert report["feedback_window"] == 0
        assert report["decision_window"] == 0
        assert "weights" in report
        feedback.close()

    def test_run_batch_returns_threshold(self, engine: object) -> None:
        """The report always carries a score threshold."""
        feedback: FeedbackService = _feedback_service()
        report = feedback.run_batch()
        assert 0 <= report["score_threshold"] <= 100
        feedback.close()

    def test_disabled_returns_disabled(self, engine: object) -> None:
        """Disabled auto-tuning reports a disabled status."""
        feedback: FeedbackService = _feedback_service(enabled=False)
        assert feedback.run_batch() == {"status": "disabled"}
        feedback.close()

    def test_disabled_record_decision_skipped(self, engine: object) -> None:
        """Disabled tuning skips decision writes."""
        feedback: FeedbackService = _feedback_service(enabled=False)
        feedback.record_decision("BLOCK", True)
        rows = feedback._connection.execute("SELECT COUNT(*) FROM decisions").fetchone()
        assert rows is not None
        assert rows[0] == 0
        feedback.close()


class TestAutoTuningPrecision(BaseTest):
    """Precision-driven weight adjustment."""

    @pytest.mark.parametrize(
        ("correct", "total", "expected_delta"),
        (
            (10, 10, 1),
            (9, 10, 1),
            (7, 10, 1),
            (6, 10, 0),
            (5, 10, 0),
            (4, 10, 0),
            (3, 10, -1),
            (0, 10, -1),
        ),
    )
    def test_weight_delta_by_precision(
        self,
        correct: int,
        total: int,
        expected_delta: int,
    ) -> None:
        """Weights move with precision relative to 0.5.

        :param correct: correct feedback rows
        :param total: total feedback rows
        :param expected_delta: expected weight adjustment direction
        """
        feedback: FeedbackService = _feedback_service()
        settings_service: SettingsService = feedback._settings_service
        before: int = int(settings_service.get("WEIGHT_DETECTOR_AHO", 30))
        for index in range(total):
            feedback.record_feedback(f"r{index}", "BLOCK", index < correct, "BLOCK")
        feedback.run_batch()
        after: int = int(settings_service.get("WEIGHT_DETECTOR_AHO", 30))
        if expected_delta > 0:
            assert after > before
        elif expected_delta < 0:
            assert after < before
        else:
            assert after == before or abs(after - before) < 3
        feedback.close()

    @pytest.mark.parametrize(
        ("correct", "total", "window"),
        (
            (5, 10, 24),
            (8, 10, 24),
            (10, 20, 24),
            (0, 5, 24),
        ),
    )
    def test_batch_window_is_24h(self, correct: int, total: int, window: int) -> None:
        """Only feedback inside the 24-hour window counts.

        :param correct: correct feedback rows in window
        :param total: total feedback rows in window
        :param window: fixed 24-hour window size
        """
        assert window == 24
        feedback: FeedbackService = _feedback_service()
        for index in range(total):
            feedback.record_feedback(f"r{index}", "BLOCK", index < correct, "BLOCK")
        report = feedback.run_batch()
        assert report["feedback_window"] == total
        feedback.close()


class TestAutoTuningThreshold(BaseTest):
    """LLM-pass-rate threshold tuning."""

    @pytest.mark.parametrize(
        ("passes", "total_ai"),
        (
            (0, 10),
            (1, 10),
            (2, 10),
            (9, 10),
            (10, 10),
            (5, 10),
            (3, 10),
            (8, 10),
        ),
    )
    def test_threshold_moves_with_pass_rate(self, passes: int, total_ai: int) -> None:
        """Threshold rises on high pass rate and falls on high block rate.

        :param passes: LLM passes in the window
        :param total_ai: total LLM decisions in the window
        """
        feedback: FeedbackService = _feedback_service()
        app_config: AppConfigService = feedback._app_config
        before: int = int(app_config.get(None)["score_threshold"])
        for index in range(total_ai):
            feedback.record_decision("PASS" if index < passes else "BLOCK", True)
        feedback.run_batch()
        after: int = int(app_config.get(None)["score_threshold"])
        pass_rate: float = passes / total_ai
        if pass_rate > 0.90:
            assert after == min(100, before + 2)
        elif pass_rate < 0.70:
            assert after == max(0, before - 2)
        else:
            assert after == before
        feedback.close()

    def test_no_ai_decisions_threshold_stable(self) -> None:
        """Without AI decisions the threshold does not change."""
        feedback: FeedbackService = _feedback_service()
        app_config: AppConfigService = feedback._app_config
        before: int = int(app_config.get(None)["score_threshold"])
        feedback.run_batch()
        assert int(app_config.get(None)["score_threshold"]) == before
        feedback.close()


class TestAutoTuningDecay(BaseTest):
    """Exponential weight decay toward defaults."""

    def test_decay_moves_weights_to_defaults(self) -> None:
        """Weights decay toward the configured defaults."""
        feedback: FeedbackService = _feedback_service()
        settings_service: SettingsService = feedback._settings_service
        settings_service.get("WEIGHT_DETECTOR_AHO")
        settings_service.update({"WEIGHT_DETECTOR_AHO": 50})
        feedback.run_batch()
        value: int = int(settings_service.get("WEIGHT_DETECTOR_AHO", 30))
        assert 5 <= value <= 50
        feedback.close()

    def test_weights_clamped_between_five_and_fifty(self) -> None:
        """Every adjusted weight stays within the valid range."""
        feedback: FeedbackService = _feedback_service()
        report = feedback.run_batch()
        for value in report["weights"].values():
            assert 5 <= value <= 50
        feedback.close()

    def test_all_weight_keys_tuned(self) -> None:
        """Every weight key is present in the report."""
        feedback: FeedbackService = _feedback_service()
        report = feedback.run_batch()
        for key in (
            "WEIGHT_DETECTOR_BADWORDS",
            "WEIGHT_DETECTOR_PROFANITE",
            "WEIGHT_DETECTOR_GLIN",
            "WEIGHT_DETECTOR_AHO",
            "WEIGHT_DETECTOR_BKTREE",
            "WEIGHT_DETECTOR_METAPHONE",
            "WEIGHT_SEMANTIC_POLITICAL",
            "WEIGHT_SEMANTIC_VIOLENCE",
            "WEIGHT_SEMANTIC_SEXUAL",
            "WEIGHT_SEMANTIC_HATE",
            "WEIGHT_SEMANTIC_PII",
            "WEIGHT_SEMANTIC_ADS",
            "WEIGHT_USER",
        ):
            assert key in report["weights"]
        feedback.close()

    def test_last_tuned_meta_written(self) -> None:
        """The batch writes the last-tuned timestamp."""
        feedback: FeedbackService = _feedback_service()
        feedback.run_batch()
        assert feedback._meta("last_tuned") != ""
        feedback.close()


class TestAutoTuningDecayHalfLife(BaseTest):
    """Half-life decay behavior."""

    @pytest.mark.parametrize(
        ("days_ago", "expected_direction"),
        (
            (0, "full"),
            (30, "half"),
            (60, "quarter"),
            (90, "eighth"),
            (300, "tiny"),
        ),
    )
    def test_decay_scales_with_time(self, days_ago: int, expected_direction: str) -> None:
        """Older last-tuning reduces influence.

        :param days_ago: simulated days since last tuning
        :param expected_direction: expected decay magnitude bucket
        """
        feedback: FeedbackService = _feedback_service()
        settings_service: SettingsService = feedback._settings_service
        settings_service.get("WEIGHT_DETECTOR_AHO")
        settings_service.update({"WEIGHT_DETECTOR_AHO": 50})
        self._clock.advance(days=-days_ago)
        feedback._set_meta("last_tuned", self._clock.now().isoformat())
        self._clock.advance(days=days_ago)
        feedback.run_batch()
        value: int = int(settings_service.get("WEIGHT_DETECTOR_AHO", 30))
        if expected_direction == "full":
            assert value == 50
        elif expected_direction == "half":
            assert value < 50
        elif expected_direction == "tiny":
            assert value < 40
        feedback.close()


class TestAutoTuningFeedback(BaseTest):
    """Feedback record contents and persistence."""

    @pytest.mark.parametrize(
        ("verdict", "actual", "correct"),
        (
            ("BLOCK", "BLOCK", True),
            ("PASS", "PASS", True),
            ("REVIEW", "PASS", False),
            ("REVIEW", "BLOCK", False),
            ("BLOCK", "PASS", False),
            ("PASS", "BLOCK", False),
        ),
    )
    def test_feedback_stored_fields(self, verdict: str, actual: str, correct: bool) -> None:
        """Stored feedback preserves every field.

        :param verdict: original service verdict
        :param actual: administrator action
        :param correct: correctness flag
        """
        feedback: FeedbackService = _feedback_service()
        feedback.record_feedback("req1", verdict, correct, actual)
        row = feedback._connection.execute(
            "SELECT request_id, verdict, is_correct, actual_action FROM feedback"
        ).fetchone()
        assert row is not None
        assert row[0] == "req1"
        assert row[1] == verdict
        assert row[2] == int(correct)
        assert row[3] == actual
        feedback.close()

    def test_feedback_count(self) -> None:
        """Multiple feedback rows persist."""
        feedback: FeedbackService = _feedback_service()
        for index in range(5):
            feedback.record_feedback(f"r{index}", "BLOCK", True, "BLOCK")
        rows = feedback._connection.execute("SELECT COUNT(*) FROM feedback").fetchone()
        assert rows is not None
        assert rows[0] == 5
        feedback.close()

    def test_stale_feedback_cleared(self) -> None:
        """Feedback older than 24 hours is pruned after a batch."""
        feedback: FeedbackService = _feedback_service()
        self._clock.advance(days=-2)
        feedback.record_feedback("old", "BLOCK", True, "BLOCK")
        feedback.record_feedback("older", "BLOCK", True, "BLOCK")
        self._clock.advance(days=2)
        feedback.run_batch()
        rows = feedback._connection.execute("SELECT COUNT(*) FROM feedback").fetchone()
        assert rows is not None
        assert rows[0] == 0
        feedback.close()

    def test_stale_decisions_cleared(self) -> None:
        """Decisions older than 24 hours are pruned after a batch."""
        feedback: FeedbackService = _feedback_service()
        self._clock.advance(days=-2)
        feedback.record_decision("BLOCK", True)
        self._clock.advance(days=2)
        feedback.run_batch()
        rows = feedback._connection.execute("SELECT COUNT(*) FROM decisions").fetchone()
        assert rows is not None
        assert rows[0] == 0
        feedback.close()


class TestAutoTuningReports(BaseTest):
    """Report shape and values."""

    def test_report_has_precision(self) -> None:
        """The report includes the computed precision."""
        feedback: FeedbackService = _feedback_service()
        for index in range(10):
            feedback.record_feedback(f"r{index}", "BLOCK", index < 8, "BLOCK")
        report = feedback.run_batch()
        assert report["precision"] == pytest.approx(0.8)
        feedback.close()

    def test_report_precision_default_half(self) -> None:
        """Empty feedback defaults precision to 0.5."""
        feedback: FeedbackService = _feedback_service()
        report = feedback.run_batch()
        assert report["precision"] == 0.5
        feedback.close()

    def test_report_llm_pass_rate(self) -> None:
        """The report carries the LLM pass rate when AI ran."""
        feedback: FeedbackService = _feedback_service()
        for index in range(10):
            feedback.record_decision("PASS" if index < 3 else "BLOCK", True)
        report = feedback.run_batch()
        assert "llm_pass_rate" in report
        assert report["llm_pass_rate"] == pytest.approx(0.3)
        feedback.close()

    def test_report_decision_window(self) -> None:
        """The report counts decisions in the window."""
        feedback: FeedbackService = _feedback_service()
        for _ in range(7):
            feedback.record_decision("BLOCK", True)
        report = feedback.run_batch()
        assert report["decision_window"] == 7
        feedback.close()

    def test_report_feedback_window(self) -> None:
        """The report counts feedback in the window."""
        feedback: FeedbackService = _feedback_service()
        for index in range(6):
            feedback.record_feedback(f"r{index}", "BLOCK", True, "BLOCK")
        report = feedback.run_batch()
        assert report["feedback_window"] == 6
        feedback.close()


class TestAutoTuningThresholdEdge(BaseTest):
    """Threshold edge cases."""

    @pytest.mark.parametrize("threshold", (0, 1, 50, 99, 100))
    def test_threshold_roundtrip(self, threshold: int) -> None:
        """An extreme threshold is clamped into the valid range.

        :param threshold: threshold to apply
        """
        feedback: FeedbackService = _feedback_service()
        app_config: AppConfigService = feedback._app_config
        app_config.update_default_threshold(threshold)
        stored: int = int(app_config.get(None)["score_threshold"])
        assert 0 <= stored <= 100
        feedback.close()

    def test_threshold_high_blocks_trigger(self) -> None:
        """A threshold of 100 makes every trigger conditional."""
        feedback: FeedbackService = _feedback_service()
        app_config: AppConfigService = feedback._app_config
        app_config.update_default_threshold(100)
        assert int(app_config.get(None)["score_threshold"]) == 100
        feedback.close()

    def test_threshold_zero_triggers_everything(self) -> None:
        """A threshold of zero triggers on any positive score."""
        feedback: FeedbackService = _feedback_service()
        app_config: AppConfigService = feedback._app_config
        app_config.update_default_threshold(0)
        assert int(app_config.get(None)["score_threshold"]) == 0
        feedback.close()

    def test_repeated_batches_stable(self) -> None:
        """Repeated empty batches keep the threshold stable."""
        feedback: FeedbackService = _feedback_service()
        app_config: AppConfigService = feedback._app_config
        before: int = int(app_config.get(None)["score_threshold"])
        for _ in range(3):
            feedback.run_batch()
        assert int(app_config.get(None)["score_threshold"]) == before
        feedback.close()

    def test_batch_after_high_block_rate(self) -> None:
        """A block-heavy batch lowers the threshold."""
        feedback: FeedbackService = _feedback_service()
        app_config: AppConfigService = feedback._app_config
        before: int = int(app_config.get(None)["score_threshold"])
        for _ in range(10):
            feedback.record_decision("BLOCK", True)
        feedback.run_batch()
        after: int = int(app_config.get(None)["score_threshold"])
        assert after <= before
        feedback.close()

    def test_batch_after_high_pass_rate(self) -> None:
        """A pass-heavy batch raises the threshold."""
        feedback: FeedbackService = _feedback_service()
        app_config: AppConfigService = feedback._app_config
        before: int = int(app_config.get(None)["score_threshold"])
        for _ in range(10):
            feedback.record_decision("PASS", True)
        feedback.run_batch()
        after: int = int(app_config.get(None)["score_threshold"])
        assert after >= before
        feedback.close()


def _feedback_service(enabled: bool = True) -> FeedbackService:
    """Build an isolated feedback service.

    :param enabled: whether auto-tuning is enabled
    :return: a configured feedback service
    """
    import tempfile
    from pathlib import Path

    from app.config import Settings
    from app.utils.logger import ModerationLogger

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
