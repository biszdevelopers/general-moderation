"""91-day archive cycle tests, part 2 (Phase 1, P1/P2).

Covers multiple users, multiple apps, review percentages, partial cycles,
and concurrent isolation across archive boundaries.
"""

from __future__ import annotations

from pathlib import Path

import pytest

from app.profiling.user_profiler import UserProfiler
from tests.base_test import BaseTest


class TestArchiveMultiUser(BaseTest):
    """Multiple users within one app."""

    @pytest.mark.parametrize("user_count", (1, 2, 5, 10, 25))
    def test_multiple_users_archive(self, tmp_path: Path, user_count: int) -> None:
        """Every user archives independently.

        :param tmp_path: per-test temporary directory
        :param user_count: number of concurrent users
        """
        profiler: UserProfiler = UserProfiler(
            str(tmp_path / "users.db"), str(tmp_path / "archive.db"), 91
        )
        for _ in range(91):
            for index in range(user_count):
                profiler.record("app", f"user{index}", total_msgs=1)
            self.advance_days(1)
        stats = profiler.stats()
        assert stats["summary_count"] == user_count
        assert stats["summary_users"] == user_count
        profiler.close()

    def test_users_isolated_ratios(self, tmp_path: Path) -> None:
        """Flagged ratios stay per-user across a cycle."""
        profiler: UserProfiler = UserProfiler(
            str(tmp_path / "users.db"), str(tmp_path / "archive.db"), 91
        )
        for _ in range(91):
            profiler.record("app", "bad", total_msgs=1, flagged_msgs=1)
            profiler.record("app", "good", total_msgs=1)
            self.advance_days(1)
        assert profiler.get_ratio("app", "bad") == 1.0
        assert profiler.get_ratio("app", "good") == 0.0
        profiler.close()

    def test_user_missing_archive_returns_zero(self, tmp_path: Path) -> None:
        """An unknown user after archiving returns a zero ratio."""
        profiler: UserProfiler = UserProfiler(
            str(tmp_path / "users.db"), str(tmp_path / "archive.db"), 91
        )
        for _ in range(91):
            profiler.record("app", "user1", total_msgs=1)
            self.advance_days(1)
        assert profiler.get_ratio("app", "ghost") == 0.0
        profiler.close()


class TestArchiveMultiApp(BaseTest):
    """Multiple applications in the archive."""

    @pytest.mark.parametrize("app_count", (1, 2, 3, 5, 10))
    def test_multiple_apps_archive(self, tmp_path: Path, app_count: int) -> None:
        """Each app archives independently.

        :param tmp_path: per-test temporary directory
        :param app_count: number of applications
        """
        profiler: UserProfiler = UserProfiler(
            str(tmp_path / "users.db"), str(tmp_path / "archive.db"), 91
        )
        for _ in range(91):
            for index in range(app_count):
                profiler.record(f"app{index}", "user1", total_msgs=1)
            self.advance_days(1)
        stats = profiler.stats()
        assert stats["summary_count"] == app_count
        profiler.close()

    def test_app_isolation(self, tmp_path: Path) -> None:
        """Same user in two apps keeps separate archives."""
        profiler: UserProfiler = UserProfiler(
            str(tmp_path / "users.db"), str(tmp_path / "archive.db"), 91
        )
        for _ in range(91):
            profiler.record("app1", "user1", total_msgs=1, flagged_msgs=1)
            profiler.record("app2", "user1", total_msgs=1)
            self.advance_days(1)
        assert profiler.get_ratio("app1", "user1") == 1.0
        assert profiler.get_ratio("app2", "user1") == 0.0
        profiler.close()

    def test_app_unknown_returns_zero(self, tmp_path: Path) -> None:
        """An unknown app returns a zero ratio."""
        profiler: UserProfiler = UserProfiler(
            str(tmp_path / "users.db"), str(tmp_path / "archive.db"), 91
        )
        for _ in range(91):
            profiler.record("app1", "user1", total_msgs=1)
            self.advance_days(1)
        assert profiler.get_ratio("nonexistent", "user1") == 0.0
        profiler.close()


class TestArchiveReview(BaseTest):
    """Reviewed percentage tracking."""

    @pytest.mark.parametrize("review_pct", (0, 10, 20, 30, 50, 100))
    def test_reviewed_percentage(self, tmp_path: Path, review_pct: int) -> None:
        """Reviewed messages archive into the summary.

        :param tmp_path: per-test temporary directory
        :param review_pct: percentage of messages reviewed
        """
        volume: int = 10
        profiler: UserProfiler = UserProfiler(
            str(tmp_path / "users.db"), str(tmp_path / "archive.db"), 91
        )
        for _ in range(91):
            profiler.record(
                "app",
                "user1",
                total_msgs=volume,
                reviewed_msgs=round(volume * review_pct / 100),
            )
            self.advance_days(1)
        summary = profiler.get_profile("app", "user1")["summaries"][0]
        assert summary["reviewed_msgs"] / summary["total_msgs"] * 100 == pytest.approx(
            review_pct, abs=2
        )
        profiler.close()


class TestArchivePartial(BaseTest):
    """Partial cycles and inactivity."""

    @pytest.mark.parametrize("days", (1, 7, 30, 60, 90, 91))
    def test_partial_cycle_live(self, tmp_path: Path, days: int) -> None:
        """A partial cycle keeps live rows until day 91.

        :param tmp_path: per-test temporary directory
        :param days: number of recorded days
        """
        profiler: UserProfiler = UserProfiler(
            str(tmp_path / "users.db"), str(tmp_path / "archive.db"), 91
        )
        for _ in range(days):
            profiler.record("app", "user1", total_msgs=1)
            self.advance_days(1)
        profile = profiler.get_profile("app", "user1")
        if days < 91:
            assert not profile["summaries"]
            assert len(profile["daily"]) == days
        else:
            assert len(profile["summaries"]) == 1
        profiler.close()

    def test_inactivity_then_resume(self, tmp_path: Path) -> None:
        """A long gap archives the stale cycle and restarts cleanly."""
        profiler: UserProfiler = UserProfiler(
            str(tmp_path / "users.db"), str(tmp_path / "archive.db"), 91
        )
        profiler.record("app", "user1", total_msgs=1)
        self.advance_days(100)
        profiler.record("app", "user1", total_msgs=1)
        profile = profiler.get_profile("app", "user1")
        assert len(profile["summaries"]) == 1
        assert len(profile["daily"]) == 0
        profiler.close()


class TestArchiveConcurrency(BaseTest):
    """Isolated archives across dimensions."""

    def test_users_and_apps_grid(self, tmp_path: Path) -> None:
        """A grid of users and apps archives cleanly."""
        profiler: UserProfiler = UserProfiler(
            str(tmp_path / "users.db"), str(tmp_path / "archive.db"), 91
        )
        for _ in range(91):
            for app_index in range(2):
                for user_index in range(3):
                    profiler.record(f"app{app_index}", f"user{user_index}", total_msgs=1)
            self.advance_days(1)
        assert profiler.stats()["summary_count"] == 6
        profiler.close()

    def test_archive_db_persists(self, tmp_path: Path) -> None:
        """Archive rows survive closing and reopening."""
        db_path: Path = tmp_path / "users.db"
        archive_path: Path = tmp_path / "archive.db"
        profiler: UserProfiler = UserProfiler(str(db_path), str(archive_path), 91)
        for _ in range(91):
            profiler.record("app", "user1", total_msgs=1)
            self.advance_days(1)
        profiler.close()
        reopened: UserProfiler = UserProfiler(str(db_path), str(archive_path), 91)
        profile = reopened.get_profile("app", "user1")
        assert len(profile["summaries"]) == 1
        assert profile["summaries"][0]["total_msgs"] == 91
        reopened.close()


class TestArchiveChainDeep(BaseTest):
    """Long linked chains of cycles."""

    @pytest.mark.parametrize("cycles", (2, 3, 4, 5, 10))
    def test_n_cycles_chain(self, tmp_path: Path, cycles: int) -> None:
        """N cycles link into one chain.

        :param tmp_path: per-test temporary directory
        :param cycles: number of completed cycles
        """
        profiler: UserProfiler = UserProfiler(
            str(tmp_path / "users.db"), str(tmp_path / "archive.db"), 91
        )
        for _ in range(cycles * 91):
            profiler.record("app", "user1", total_msgs=1)
            self.advance_days(1)
        profile = profiler.get_profile("app", "user1")
        assert len(profile["summaries"]) == cycles
        expected: list[int | None] = [index + 2 for index in range(cycles - 1)] + [None]
        assert [summary["next_cycle_id"] for summary in profile["summaries"]] == expected
        profiler.close()

    def test_chain_total_messages(self, tmp_path: Path) -> None:
        """Chain summaries sum to the total recorded messages."""
        profiler: UserProfiler = UserProfiler(
            str(tmp_path / "users.db"), str(tmp_path / "archive.db"), 91
        )
        for _ in range(182):
            profiler.record("app", "user1", total_msgs=2)
            self.advance_days(1)
        profile = profiler.get_profile("app", "user1")
        assert sum(summary["total_msgs"] for summary in profile["summaries"]) == 364
        profiler.close()


class TestArchiveBoundaries(BaseTest):
    """Boundary conditions around the window edge."""

    @pytest.mark.parametrize(
        ("window", "days"),
        (
            (7, 7),
            (7, 6),
            (7, 8),
            (30, 30),
            (30, 29),
            (60, 61),
            (91, 90),
            (91, 92),
            (365, 364),
            (365, 366),
        ),
    )
    def test_window_boundary(self, tmp_path: Path, window: int, days: int) -> None:
        """Archiving fires exactly at the window edge.

        :param tmp_path: per-test temporary directory
        :param window: profiling window length
        :param days: days recorded
        """
        profiler: UserProfiler = UserProfiler(
            str(tmp_path / "users.db"), str(tmp_path / "archive.db"), window
        )
        for _ in range(days):
            profiler.record("app", "user1", total_msgs=1)
            self.advance_days(1)
        profile = profiler.get_profile("app", "user1")
        if days >= window:
            assert len(profile["summaries"]) >= 1
        else:
            assert not profile["summaries"]
        profiler.close()

    @pytest.mark.parametrize("window", (7, 30, 91, 365))
    def test_exact_day_archives(self, tmp_path: Path, window: int) -> None:
        """Day N exactly triggers archiving for any window.

        :param tmp_path: per-test temporary directory
        :param window: profiling window length
        """
        profiler: UserProfiler = UserProfiler(
            str(tmp_path / "users.db"), str(tmp_path / "archive.db"), window
        )
        for _ in range(window):
            profiler.record("app", "user1", total_msgs=1)
            self.advance_days(1)
        assert profiler.stats()["summary_count"] == 1
        profiler.close()


class TestArchiveStats(BaseTest):
    """Archive statistics reporting."""

    def test_stats_after_multiple_cycles(self, tmp_path: Path) -> None:
        """Stats reflect every archived cycle."""
        profiler: UserProfiler = UserProfiler(
            str(tmp_path / "users.db"), str(tmp_path / "archive.db"), 91
        )
        for _ in range(273):
            profiler.record("app", "user1", total_msgs=1)
            self.advance_days(1)
        stats = profiler.stats()
        assert stats["summary_count"] == 3
        assert stats["summary_users"] == 1
        assert stats["daily_rows"] == 0
        profiler.close()

    def test_stats_mixed_state(self, tmp_path: Path) -> None:
        """Stats report live rows alongside archived summaries."""
        profiler: UserProfiler = UserProfiler(
            str(tmp_path / "users.db"), str(tmp_path / "archive.db"), 91
        )
        for _ in range(91):
            profiler.record("app", "user1", total_msgs=1)
            self.advance_days(1)
        profiler.record("app", "user2", total_msgs=1)
        stats = profiler.stats()
        assert stats["summary_count"] == 1
        assert stats["daily_rows"] == 1
        assert stats["active_users"] == 1
        profiler.close()


class TestArchiveEdge(BaseTest):
    """Rare and boundary archive scenarios."""

    def test_two_apps_share_user(self, tmp_path: Path) -> None:
        """A shared user across apps archives into two summaries."""
        profiler: UserProfiler = UserProfiler(
            str(tmp_path / "users.db"), str(tmp_path / "archive.db"), 91
        )
        for _ in range(91):
            profiler.record("app1", "user1", total_msgs=1)
            profiler.record("app2", "user1", total_msgs=1)
            self.advance_days(1)
        assert profiler.get_profile("app1", "user1")["summaries"]
        assert profiler.get_profile("app2", "user1")["summaries"]
        assert profiler.stats()["summary_count"] == 2
        profiler.close()

    def test_zero_day_cycle(self, tmp_path: Path) -> None:
        """Recording zero messages archives zero totals."""
        profiler: UserProfiler = UserProfiler(
            str(tmp_path / "users.db"), str(tmp_path / "archive.db"), 91
        )
        for _ in range(91):
            profiler.record("app", "user1", total_msgs=0)
            self.advance_days(1)
        summary = profiler.get_profile("app", "user1")["summaries"][0]
        assert summary["total_msgs"] == 0
        profiler.close()

    def test_flag_only_archive(self, tmp_path: Path) -> None:
        """A cycle of pure flags archives total equal to flags."""
        profiler: UserProfiler = UserProfiler(
            str(tmp_path / "users.db"), str(tmp_path / "archive.db"), 91
        )
        for _ in range(91):
            profiler.record("app", "user1", total_msgs=1, flagged_msgs=1)
            self.advance_days(1)
        summary = profiler.get_profile("app", "user1")["summaries"][0]
        assert summary["total_msgs"] == summary["flagged_msgs"] == 91
        profiler.close()

    def test_cycle_ratio_persists(self, tmp_path: Path) -> None:
        """The ratio computed after a full cycle is correct."""
        profiler: UserProfiler = UserProfiler(
            str(tmp_path / "users.db"), str(tmp_path / "archive.db"), 91
        )
        for _ in range(91):
            profiler.record("app", "user1", total_msgs=2, flagged_msgs=1)
            self.advance_days(1)
        assert profiler.get_ratio("app", "user1") == 0.5
        profiler.close()

    def test_many_users_one_app_archive(self, tmp_path: Path) -> None:
        """Many users in one app archive independently."""
        profiler: UserProfiler = UserProfiler(
            str(tmp_path / "users.db"), str(tmp_path / "archive.db"), 91
        )
        for _ in range(91):
            for index in range(20):
                profiler.record("app", f"u{index}", total_msgs=1)
            self.advance_days(1)
        assert profiler.stats()["summary_count"] == 20
        profiler.close()

    def test_one_user_many_apps_archive(self, tmp_path: Path) -> None:
        """One user across many apps archives independently."""
        profiler: UserProfiler = UserProfiler(
            str(tmp_path / "users.db"), str(tmp_path / "archive.db"), 91
        )
        for _ in range(91):
            for index in range(20):
                profiler.record(f"app{index}", "u", total_msgs=1)
            self.advance_days(1)
        assert profiler.stats()["summary_count"] == 20
        profiler.close()

    def test_archive_summary_order(self, tmp_path: Path) -> None:
        """Archived summaries keep ascending cycle order per user."""
        profiler: UserProfiler = UserProfiler(
            str(tmp_path / "users.db"), str(tmp_path / "archive.db"), 91
        )
        for _ in range(273):
            profiler.record("app", "user1", total_msgs=1)
            self.advance_days(1)
        summaries = profiler.get_profile("app", "user1")["summaries"]
        assert [summary["cycle_id"] for summary in summaries] == [1, 2, 3]
        profiler.close()
