"""User profiling tests, part 1 (Phase 1, P0/P1).

Covers ratio calculation, daily row aggregation, empty profiles, and
per-app/user isolation using the frozen clock.
"""

from __future__ import annotations

from app.profiling.user_profiler import UserProfiler
from tests.base_test import BaseTest


class TestProfilerRatios(BaseTest):
    """Bad-content ratio calculation."""

    def test_empty_profile_ratio_zero(self) -> None:
        """No rows produce a zero ratio."""
        profiler: UserProfiler = UserProfiler(":memory:", ":memory:", 91)
        assert profiler.get_ratio("app", "u") == 0.0
        profiler.close()

    def test_all_clean_ratio_zero(self) -> None:
        """Only clean messages give a zero ratio."""
        profiler: UserProfiler = UserProfiler(":memory:", ":memory:", 91)
        profiler.record("app", "u", total_msgs=5)
        assert profiler.get_ratio("app", "u") == 0.0
        profiler.close()

    def test_all_flagged_ratio_one(self) -> None:
        """Every message flagged gives a ratio of one."""
        profiler: UserProfiler = UserProfiler(":memory:", ":memory:", 91)
        profiler.record("app", "u", total_msgs=1, flagged_msgs=1)
        assert profiler.get_ratio("app", "u") == 1.0
        profiler.close()

    def test_half_flagged_ratio_half(self) -> None:
        """Half flagged messages give a ratio of 0.5."""
        profiler: UserProfiler = UserProfiler(":memory:", ":memory:", 91)
        profiler.record("app", "u", total_msgs=1, flagged_msgs=1)
        profiler.record("app", "u", total_msgs=1)
        assert profiler.get_ratio("app", "u") == 0.5
        profiler.close()

    def test_blocked_counts_as_bad(self) -> None:
        """Blocked messages count toward the bad ratio."""
        profiler: UserProfiler = UserProfiler(":memory:", ":memory:", 91)
        profiler.record("app", "u", total_msgs=1, blocked_msgs=1)
        assert profiler.get_ratio("app", "u") == 1.0
        profiler.close()

    def test_reviewed_not_bad(self) -> None:
        """Reviewed messages do not count as bad."""
        profiler: UserProfiler = UserProfiler(":memory:", ":memory:", 91)
        profiler.record("app", "u", total_msgs=1, reviewed_msgs=1)
        assert profiler.get_ratio("app", "u") == 0.0
        profiler.close()

    def test_no_user_id_ignored(self) -> None:
        """Empty user ids are not recorded."""
        profiler: UserProfiler = UserProfiler(":memory:", ":memory:", 91)
        profiler.record("app", "", total_msgs=1, flagged_msgs=1)
        assert profiler.get_ratio("app", "") == 0.0
        assert profiler.stats()["active_users"] == 0
        profiler.close()

    def test_separate_users_isolated(self) -> None:
        """One flagged user does not affect another."""
        profiler: UserProfiler = UserProfiler(":memory:", ":memory:", 91)
        profiler.record("app", "bad", total_msgs=1, flagged_msgs=1)
        profiler.record("app", "good", total_msgs=1)
        assert profiler.get_ratio("app", "bad") == 1.0
        assert profiler.get_ratio("app", "good") == 0.0
        profiler.close()

    def test_separate_apps_isolated(self) -> None:
        """The same user in different apps is isolated."""
        profiler: UserProfiler = UserProfiler(":memory:", ":memory:", 91)
        profiler.record("app1", "u", total_msgs=1, flagged_msgs=1)
        profiler.record("app2", "u", total_msgs=1)
        assert profiler.get_ratio("app1", "u") == 1.0
        assert profiler.get_ratio("app2", "u") == 0.0
        profiler.close()


class TestProfilerRecords(BaseTest):
    """Daily row aggregation."""

    def test_multiple_records_same_day(self) -> None:
        """Records on the same day aggregate into one row."""
        profiler: UserProfiler = UserProfiler(":memory:", ":memory:", 91)
        profiler.record("app", "u", total_msgs=1, flagged_msgs=1)
        profiler.record("app", "u", total_msgs=1, flagged_msgs=1)
        profile = profiler.get_profile("app", "u")
        assert len(profile["daily"]) == 1
        assert profile["daily"][0]["total_msgs"] == 2
        profiler.close()

    def test_distinct_days_separate_rows(self) -> None:
        """Records on different days create separate rows."""
        profiler: UserProfiler = UserProfiler(":memory:", ":memory:", 91)
        profiler.record("app", "u", total_msgs=1)
        self.advance_days(1)
        profiler.record("app", "u", total_msgs=1)
        profile = profiler.get_profile("app", "u")
        assert len(profile["daily"]) == 2
        profiler.close()

    def test_day_offsets_increment(self) -> None:
        """Day offsets increment across days."""
        profiler: UserProfiler = UserProfiler(":memory:", ":memory:", 91)
        profiler.record("app", "u", total_msgs=1)
        self.advance_days(1)
        profiler.record("app", "u", total_msgs=1)
        profile = profiler.get_profile("app", "u")
        assert [row["day_offset"] for row in profile["daily"]] == [1, 2]
        profiler.close()

    def test_profile_has_summaries_key(self) -> None:
        """The profile always includes a summaries list."""
        profiler: UserProfiler = UserProfiler(":memory:", ":memory:", 91)
        profile = profiler.get_profile("app", "u")
        assert "summaries" in profile
        assert profile["summaries"] == []
        profiler.close()

    def test_profile_ratio_included(self) -> None:
        """The profile embeds the computed ratio."""
        profiler: UserProfiler = UserProfiler(":memory:", ":memory:", 91)
        profiler.record("app", "u", total_msgs=1, flagged_msgs=1)
        profile = profiler.get_profile("app", "u")
        assert profile["ratio"] == 1.0
        profiler.close()

    def test_multiple_flagged_records_sum(self) -> None:
        """Flagged counts sum across records on one day."""
        profiler: UserProfiler = UserProfiler(":memory:", ":memory:", 91)
        profiler.record("app", "u", total_msgs=1, flagged_msgs=1)
        profiler.record("app", "u", total_msgs=1, flagged_msgs=1)
        profile = profiler.get_profile("app", "u")
        assert profile["daily"][0]["flagged_msgs"] == 2
        profiler.close()

    def test_multiple_blocked_records_sum(self) -> None:
        """Blocked counts sum across records on one day."""
        profiler: UserProfiler = UserProfiler(":memory:", ":memory:", 91)
        profiler.record("app", "u", total_msgs=1, blocked_msgs=1)
        profiler.record("app", "u", total_msgs=1, blocked_msgs=1)
        profile = profiler.get_profile("app", "u")
        assert profile["daily"][0]["blocked_msgs"] == 2
        profiler.close()

    def test_mixed_flags_per_day(self) -> None:
        """A day can hold flagged, blocked, and reviewed counts."""
        profiler: UserProfiler = UserProfiler(":memory:", ":memory:", 91)
        profiler.record("app", "u", total_msgs=3, flagged_msgs=1, blocked_msgs=1, reviewed_msgs=1)
        row = profiler.get_profile("app", "u")["daily"][0]
        assert row["flagged_msgs"] == 1
        assert row["blocked_msgs"] == 1
        assert row["reviewed_msgs"] == 1
        profiler.close()

    def test_ratio_with_multiple_days(self) -> None:
        """Ratio accounts for every recorded day."""
        profiler: UserProfiler = UserProfiler(":memory:", ":memory:", 91)
        profiler.record("app", "u", total_msgs=1, flagged_msgs=1)
        self.advance_days(1)
        profiler.record("app", "u", total_msgs=1, flagged_msgs=1)
        self.advance_days(1)
        profiler.record("app", "u", total_msgs=2)
        assert profiler.get_ratio("app", "u") == 0.5
        profiler.close()

    def test_ratio_uses_flagged_plus_blocked(self) -> None:
        """Ratio numerator is flagged plus blocked."""
        profiler: UserProfiler = UserProfiler(":memory:", ":memory:", 91)
        profiler.record("app", "u", total_msgs=1, flagged_msgs=1)
        profiler.record("app", "u", total_msgs=1, blocked_msgs=1)
        profiler.record("app", "u", total_msgs=2)
        assert profiler.get_ratio("app", "u") == 0.5
        profiler.close()


class TestProfilerGaps(BaseTest):
    """Behavior across long inactive gaps."""

    def test_gap_beyond_window_archives(self) -> None:
        """A gap past the window closes the cycle immediately."""
        profiler: UserProfiler = UserProfiler(":memory:", ":memory:", 91)
        profiler.record("app", "u", total_msgs=1)
        self.advance_days(120)
        profiler.record("app", "u", total_msgs=1)
        assert profiler.stats()["summary_count"] >= 1
        profiler.close()

    def test_gap_within_window_keeps_rows(self) -> None:
        """A gap inside the window leaves live rows untouched."""
        profiler: UserProfiler = UserProfiler(":memory:", ":memory:", 91)
        profiler.record("app", "u", total_msgs=1)
        self.advance_days(10)
        profiler.record("app", "u", total_msgs=1)
        assert profiler.stats()["daily_rows"] == 2
        profiler.close()

    def test_fresh_cycle_after_archive(self) -> None:
        """After archiving, the next record starts a fresh cycle."""
        profiler: UserProfiler = UserProfiler(":memory:", ":memory:", 5)
        for _ in range(5):
            profiler.record("app", "u", total_msgs=1)
            self.advance_days(1)
        assert profiler.stats()["summary_count"] == 1
        profiler.record("app", "u", total_msgs=1)
        assert profiler.get_profile("app", "u")["daily"]
        profiler.close()

    def test_archive_preserves_history_ratio(self) -> None:
        """Archived cycles still count toward the ratio."""
        profiler: UserProfiler = UserProfiler(":memory:", ":memory:", 5)
        for _ in range(5):
            profiler.record("app", "u", total_msgs=1, flagged_msgs=1)
            self.advance_days(1)
        assert profiler.get_ratio("app", "u") == 1.0
        profiler.close()

    def test_summary_linked_cycles(self) -> None:
        """Consecutive cycles link through next_cycle_id."""
        profiler: UserProfiler = UserProfiler(":memory:", ":memory:", 5)
        for _ in range(5):
            profiler.record("app", "u", total_msgs=1)
            self.advance_days(1)
        for _ in range(5):
            profiler.record("app", "u", total_msgs=1)
            self.advance_days(1)
        profile = profiler.get_profile("app", "u")
        assert len(profile["summaries"]) == 2
        assert profile["summaries"][0]["next_cycle_id"] == profile["summaries"][1]["cycle_id"]
        profiler.close()


class TestProfilerIsolation(BaseTest):
    """Isolation across apps and users."""

    def test_stats_counts_unique_users(self) -> None:
        """Stats count distinct app-user pairs."""
        profiler: UserProfiler = UserProfiler(":memory:", ":memory:", 91)
        profiler.record("app1", "u1", total_msgs=1)
        profiler.record("app1", "u2", total_msgs=1)
        profiler.record("app2", "u1", total_msgs=1)
        assert profiler.stats()["active_users"] == 3
        profiler.close()

    def test_same_user_two_apps(self) -> None:
        """A user in two apps yields separate ratios."""
        profiler: UserProfiler = UserProfiler(":memory:", ":memory:", 91)
        profiler.record("app1", "u", total_msgs=1, flagged_msgs=1)
        profiler.record("app2", "u", total_msgs=1)
        assert profiler.get_ratio("app1", "u") == 1.0
        assert profiler.get_ratio("app2", "u") == 0.0
        profiler.close()

    def test_same_app_two_users(self) -> None:
        """Two users in one app yield separate ratios."""
        profiler: UserProfiler = UserProfiler(":memory:", ":memory:", 91)
        profiler.record("app", "u1", total_msgs=1, flagged_msgs=1)
        profiler.record("app", "u2", total_msgs=1)
        assert profiler.get_ratio("app", "u1") == 1.0
        assert profiler.get_ratio("app", "u2") == 0.0
        profiler.close()

    def test_profile_fields(self) -> None:
        """The profile exposes app, user, and summary keys."""
        profiler: UserProfiler = UserProfiler(":memory:", ":memory:", 91)
        profiler.record("app", "u", total_msgs=1)
        profile = profiler.get_profile("app", "u")
        assert profile["app_name"] == "app"
        assert profile["user_id"] == "u"
        profiler.close()

    def test_day_offset_in_date(self) -> None:
        """Daily rows carry an ISO date string."""
        profiler: UserProfiler = UserProfiler(":memory:", ":memory:", 91)
        profiler.record("app", "u", total_msgs=1)
        row = profiler.get_profile("app", "u")["daily"][0]
        assert row["date"] == "2026-01-01"
        profiler.close()

    def test_zero_counts_in_profile(self) -> None:
        """Zero-count messages still record a row."""
        profiler: UserProfiler = UserProfiler(":memory:", ":memory:", 91)
        profiler.record("app", "u", total_msgs=0)
        profile = profiler.get_profile("app", "u")
        assert len(profile["daily"]) == 1
        assert profile["daily"][0]["total_msgs"] == 0
        profiler.close()

    def test_negative_day_offset_clamped(self) -> None:
        """A clock anomaly is clamped to day one."""
        profiler: UserProfiler = UserProfiler(":memory:", ":memory:", 91)
        self.advance_days(-5)
        profiler.record("app", "u", total_msgs=1)
        row = profiler.get_profile("app", "u")["daily"][0]
        assert row["day_offset"] == 1
        profiler.close()

    def test_archive_after_window_records_last_day(self) -> None:
        """The day beyond the window is archived as the final day."""
        profiler: UserProfiler = UserProfiler(":memory:", ":memory:", 3)
        profiler.record("app", "u", total_msgs=1)
        self.advance_days(1)
        profiler.record("app", "u", total_msgs=1)
        self.advance_days(1)
        profiler.record("app", "u", total_msgs=1)
        assert profiler.stats()["summary_count"] == 1
        profiler.close()

    def test_archive_contains_all_rows(self) -> None:
        """The archive stores every daily row of the closed cycle."""
        profiler: UserProfiler = UserProfiler(":memory:", ":memory:", 3)
        for _ in range(3):
            profiler.record("app", "u", total_msgs=1)
            self.advance_days(1)
        daily_archive = profiler._archive.execute(
            "SELECT COUNT(*) FROM user_daily_archive WHERE app_name = 'app' AND user_id = 'u'"
        ).fetchone()
        assert daily_archive is not None
        assert daily_archive[0] == 3
        profiler.close()

    def test_archive_clears_live_rows(self) -> None:
        """Closing a cycle empties the live daily table."""
        profiler: UserProfiler = UserProfiler(":memory:", ":memory:", 3)
        for _ in range(3):
            profiler.record("app", "u", total_msgs=1)
            self.advance_days(1)
        assert profiler.stats()["daily_rows"] == 0
        profiler.close()

    def test_archive_summary_counts(self) -> None:
        """The summary aggregates totals for the cycle."""
        profiler: UserProfiler = UserProfiler(":memory:", ":memory:", 3)
        for _ in range(3):
            profiler.record("app", "u", total_msgs=1, flagged_msgs=1)
            self.advance_days(1)
        summary = profiler.get_profile("app", "u")["summaries"][0]
        assert summary["total_msgs"] == 3
        assert summary["flagged_msgs"] == 3
        profiler.close()

    def test_cycle_ids_increment(self) -> None:
        """Cycle ids increment across cycles."""
        profiler: UserProfiler = UserProfiler(":memory:", ":memory:", 3)
        for _ in range(6):
            profiler.record("app", "u", total_msgs=1)
            self.advance_days(1)
        profile = profiler.get_profile("app", "u")
        assert [summary["cycle_id"] for summary in profile["summaries"]] == [1, 2]
        profiler.close()

    def test_summary_dates_set(self) -> None:
        """Summary start and end days match the cycle bounds."""
        profiler: UserProfiler = UserProfiler(":memory:", ":memory:", 3)
        for _ in range(3):
            profiler.record("app", "u", total_msgs=1)
            self.advance_days(1)
        summary = profiler.get_profile("app", "u")["summaries"][0]
        assert summary["start_day"] <= summary["end_day"]
        assert summary["start_day"] == "2026-01-01"
        profiler.close()


class TestProfilerStats(BaseTest):
    """Aggregate statistics."""

    def test_stats_empty(self) -> None:
        """A fresh profiler reports zero users and rows."""
        profiler: UserProfiler = UserProfiler(":memory:", ":memory:", 91)
        assert profiler.stats() == {
            "active_users": 0,
            "daily_rows": 0,
            "summary_count": 0,
            "summary_users": 0,
        }
        profiler.close()

    def test_stats_active_users(self) -> None:
        """Tracked users appear in the stats."""
        profiler: UserProfiler = UserProfiler(":memory:", ":memory:", 91)
        profiler.record("app", "u1", total_msgs=1)
        profiler.record("app", "u2", total_msgs=1)
        assert profiler.stats()["active_users"] == 2
        profiler.close()

    def test_stats_daily_rows(self) -> None:
        """Daily rows are counted."""
        profiler: UserProfiler = UserProfiler(":memory:", ":memory:", 91)
        profiler.record("app", "u1", total_msgs=1)
        self.advance_days(1)
        profiler.record("app", "u1", total_msgs=1)
        profiler.record("app", "u2", total_msgs=1)
        assert profiler.stats()["daily_rows"] == 3
        profiler.close()
