"""User profiling tests, part 2 (Phase 1, P1/P2).

Covers archive cycle boundaries, linked summaries, multi-cycle ratios, and
parameterized ratio scenarios using the frozen clock.
"""

from __future__ import annotations

import pytest

from app.profiling.user_profiler import UserProfiler
from tests.base_test import BaseTest


class TestProfilerCycle(BaseTest):
    """91-day (and short-window) archive cycles."""

    def test_exact_window_day_archives(self) -> None:
        """Reaching the window day closes the cycle."""
        profiler: UserProfiler = UserProfiler(":memory:", ":memory:", 3)
        for _ in range(3):
            profiler.record("app", "u", total_msgs=1)
            self.advance_days(1)
        assert profiler.stats()["summary_count"] == 1
        profiler.close()

    def test_before_window_day_keeps_live(self) -> None:
        """One day before the window stays live."""
        profiler: UserProfiler = UserProfiler(":memory:", ":memory:", 3)
        for _ in range(2):
            profiler.record("app", "u", total_msgs=1)
            self.advance_days(1)
        assert profiler.stats()["summary_count"] == 0
        assert profiler.stats()["daily_rows"] == 2
        profiler.close()

    def test_three_cycles_linked(self) -> None:
        """Three cycles produce a chain of summaries."""
        profiler: UserProfiler = UserProfiler(":memory:", ":memory:", 3)
        for _ in range(9):
            profiler.record("app", "u", total_msgs=1)
            self.advance_days(1)
        profile = profiler.get_profile("app", "u")
        assert len(profile["summaries"]) == 3
        chain: list[int | None] = [summary["next_cycle_id"] for summary in profile["summaries"]]
        assert chain == [2, 3, None]
        profiler.close()

    def test_cycle_total_msgs(self) -> None:
        """A cycle summary totals every message in the window."""
        profiler: UserProfiler = UserProfiler(":memory:", ":memory:", 3)
        for _ in range(3):
            profiler.record("app", "u", total_msgs=1)
            self.advance_days(1)
        summary = profiler.get_profile("app", "u")["summaries"][0]
        assert summary["total_msgs"] == 3
        profiler.close()

    def test_cycle_flagged_summary(self) -> None:
        """Flagged messages aggregate into the summary."""
        profiler: UserProfiler = UserProfiler(":memory:", ":memory:", 3)
        for _ in range(3):
            profiler.record("app", "u", total_msgs=1, flagged_msgs=1)
            self.advance_days(1)
        summary = profiler.get_profile("app", "u")["summaries"][0]
        assert summary["flagged_msgs"] == 3
        profiler.close()

    def test_ratio_includes_archived_cycles(self) -> None:
        """Ratio merges live rows with every archived summary."""
        profiler: UserProfiler = UserProfiler(":memory:", ":memory:", 3)
        for _ in range(3):
            profiler.record("app", "u", total_msgs=1, flagged_msgs=1)
            self.advance_days(1)
        profiler.record("app", "u", total_msgs=1)
        assert profiler.get_ratio("app", "u") == 0.75
        profiler.close()

    def test_archive_idempotent_schema(self) -> None:
        """Reopening an existing profiler does not duplicate rows."""
        live: str = ":memory:"
        archive: str = ":memory:"
        first: UserProfiler = UserProfiler(live, archive, 3)
        first.close()
        second: UserProfiler = UserProfiler(live, archive, 3)
        assert second.stats()["daily_rows"] == 0
        second.close()


class TestProfilerRatioMatrix(BaseTest):
    """Parameterized ratio calculations."""

    @pytest.mark.parametrize(
        ("flagged", "blocked", "total", "expected"),
        (
            (0, 0, 1, 0.0),
            (1, 0, 1, 1.0),
            (0, 1, 1, 1.0),
            (1, 1, 4, 0.5),
            (2, 0, 4, 0.5),
            (0, 2, 4, 0.5),
            (3, 1, 10, 0.4),
            (1, 0, 2, 0.5),
            (4, 4, 10, 0.8),
            (0, 0, 0, 0.0),
            (5, 5, 10, 1.0),
            (1, 0, 3, pytest.approx(1 / 3)),
            (1, 1, 3, pytest.approx(2 / 3)),
            (2, 2, 20, 0.2),
            (7, 0, 10, 0.7),
            (0, 9, 10, 0.9),
            (1, 0, 100, 0.01),
            (50, 0, 100, 0.5),
            (10, 10, 200, 0.1),
            (99, 0, 100, 0.99),
        ),
    )
    def test_ratio_matrix(
        self,
        flagged: int,
        blocked: int,
        total: int,
        expected: float,
    ) -> None:
        """Ratio equals (flagged + blocked) / total.

        :param flagged: flagged message count
        :param blocked: blocked message count
        :param total: total message count
        :param expected: expected ratio value
        """
        profiler: UserProfiler = UserProfiler(":memory:", ":memory:", 91)
        profiler.record("app", "u", total_msgs=total, flagged_msgs=flagged, blocked_msgs=blocked)
        assert profiler.get_ratio("app", "u") == expected
        profiler.close()

    @pytest.mark.parametrize("window", (7, 30, 60, 91, 180, 365))
    def test_window_lengths_accepted(self, window: int) -> None:
        """Every supported window length initializes cleanly.

        :param window: profiling window in days
        """
        profiler: UserProfiler = UserProfiler(":memory:", ":memory:", window)
        profiler.record("app", "u", total_msgs=1)
        assert profiler.get_ratio("app", "u") == 0.0
        profiler.close()


class TestProfilerArchiveDetail(BaseTest):
    """Archive table details and summary metadata."""

    def test_archive_daily_rows_copied(self) -> None:
        """Closed-cycle rows are copied into the daily archive table."""
        profiler: UserProfiler = UserProfiler(":memory:", ":memory:", 3)
        for _ in range(3):
            profiler.record("app", "u", total_msgs=1)
            self.advance_days(1)
        rows = profiler._archive.execute(
            "SELECT cycle_id, day_offset FROM user_daily_archive "
            "WHERE app_name = 'app' AND user_id = 'u' ORDER BY day_offset"
        ).fetchall()
        assert [(row[0], row[1]) for row in rows] == [(1, 1), (1, 2), (1, 3)]
        profiler.close()

    def test_summary_created_at_present(self) -> None:
        """Summaries carry a creation timestamp."""
        profiler: UserProfiler = UserProfiler(":memory:", ":memory:", 3)
        for _ in range(3):
            profiler.record("app", "u", total_msgs=1)
            self.advance_days(1)
        summary = profiler.get_profile("app", "u")["summaries"][0]
        assert summary["start_day"] == "2026-01-01"
        profiler.close()

    def test_two_users_separate_cycles(self) -> None:
        """Different users archive independently."""
        profiler: UserProfiler = UserProfiler(":memory:", ":memory:", 3)
        for _ in range(3):
            profiler.record("app", "u1", total_msgs=1)
            self.advance_days(1)
        profiler.record("app", "u2", total_msgs=1)
        assert profiler.get_profile("app", "u1")["summaries"]
        assert not profiler.get_profile("app", "u2")["summaries"]
        profiler.close()

    def test_blocked_only_archive(self) -> None:
        """Blocked messages archive into the summary."""
        profiler: UserProfiler = UserProfiler(":memory:", ":memory:", 3)
        for _ in range(3):
            profiler.record("app", "u", total_msgs=1, blocked_msgs=1)
            self.advance_days(1)
        summary = profiler.get_profile("app", "u")["summaries"][0]
        assert summary["blocked_msgs"] == 3
        profiler.close()

    def test_reviewed_archive(self) -> None:
        """Reviewed messages archive into the summary."""
        profiler: UserProfiler = UserProfiler(":memory:", ":memory:", 3)
        for _ in range(3):
            profiler.record("app", "u", total_msgs=1, reviewed_msgs=1)
            self.advance_days(1)
        summary = profiler.get_profile("app", "u")["summaries"][0]
        assert summary["reviewed_msgs"] == 3
        profiler.close()

    def test_ratio_after_two_cycles(self) -> None:
        """Ratio reflects both archived cycles."""
        profiler: UserProfiler = UserProfiler(":memory:", ":memory:", 3)
        for _ in range(3):
            profiler.record("app", "u", total_msgs=1, flagged_msgs=1)
            self.advance_days(1)
        for _ in range(3):
            profiler.record("app", "u", total_msgs=1)
            self.advance_days(1)
        assert profiler.get_ratio("app", "u") == 0.5
        profiler.close()

    def test_mixed_counts_archive(self) -> None:
        """A cycle with mixed verdicts aggregates each counter."""
        profiler: UserProfiler = UserProfiler(":memory:", ":memory:", 3)
        profiler.record("app", "u", total_msgs=1, flagged_msgs=1)
        self.advance_days(1)
        profiler.record("app", "u", total_msgs=1, blocked_msgs=1)
        self.advance_days(1)
        profiler.record("app", "u", total_msgs=1, reviewed_msgs=1)
        summary = profiler.get_profile("app", "u")["summaries"][0]
        assert summary["total_msgs"] == 3
        assert summary["flagged_msgs"] == 1
        assert summary["blocked_msgs"] == 1
        assert summary["reviewed_msgs"] == 1
        profiler.close()
