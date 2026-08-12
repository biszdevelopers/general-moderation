"""91-day archive cycle tests, part 1 (Phase 1, P0/P1).

Covers the clean single-user archive cycle, data volume variation, flagged
and blocked percentages, and cycle summarization using the frozen clock.
"""

from __future__ import annotations

from pathlib import Path

import pytest

from app.profiling.user_profiler import UserProfiler
from tests.base_test import BaseTest


class TestArchiveSingleUser(BaseTest):
    """Single user, single app archive cycles."""

    @pytest.mark.parametrize(
        ("volume", "flagged_pct", "blocked_pct"),
        (
            (1, 0, 0),
            (10, 0, 0),
            (25, 0, 0),
            (50, 0, 0),
            (100, 0, 0),
            (10, 10, 0),
            (10, 50, 0),
            (10, 0, 10),
            (10, 0, 50),
            (10, 10, 10),
            (20, 25, 25),
            (5, 100, 0),
            (5, 0, 100),
            (7, 30, 20),
            (3, 33, 33),
        ),
    )
    def test_clean_cycle_archives(
        self,
        tmp_path: Path,
        volume: int,
        flagged_pct: int,
        blocked_pct: int,
    ) -> None:
        """A full 91-day cycle aggregates and archives correctly.

        :param tmp_path: per-test temporary directory
        :param volume: messages recorded per day
        :param flagged_pct: percentage of messages flagged
        :param blocked_pct: percentage of messages blocked
        """
        profiler: UserProfiler = UserProfiler(
            str(tmp_path / "users.db"), str(tmp_path / "archive.db"), 91
        )
        for _ in range(91):
            flagged: int = max(0, round(volume * flagged_pct / 100))
            blocked: int = max(0, round(volume * blocked_pct / 100))
            profiler.record(
                "app",
                "user1",
                total_msgs=volume,
                flagged_msgs=flagged,
                blocked_msgs=blocked,
            )
            self.advance_days(1)
        profile = profiler.get_profile("app", "user1")
        assert len(profile["summaries"]) == 1
        summary = profile["summaries"][0]
        assert summary["total_msgs"] == volume * 91
        assert summary["start_day"] == "2026-01-01"
        assert summary["end_day"] == "2026-04-01"
        assert summary["next_cycle_id"] is None
        profiler.close()

    def test_live_rows_cleared_after_archive(self, tmp_path: Path) -> None:
        """After archiving, the live table is empty."""
        profiler: UserProfiler = UserProfiler(
            str(tmp_path / "users.db"), str(tmp_path / "archive.db"), 91
        )
        for _ in range(91):
            profiler.record("app", "user1", total_msgs=1)
            self.advance_days(1)
        assert profiler.stats()["daily_rows"] == 0
        assert profiler.stats()["summary_count"] == 1
        profiler.close()

    def test_day_91_included(self, tmp_path: Path) -> None:
        """The final day of the cycle is archived."""
        profiler: UserProfiler = UserProfiler(
            str(tmp_path / "users.db"), str(tmp_path / "archive.db"), 91
        )
        for _ in range(91):
            profiler.record("app", "user1", total_msgs=1)
            self.advance_days(1)
        rows = profiler._archive.execute(
            "SELECT day_offset FROM user_daily_archive WHERE app_name = 'app' AND user_id = 'user1'"
        ).fetchall()
        assert {row[0] for row in rows} == set(range(1, 92))
        profiler.close()

    def test_cycle_summary_flagged_counts(self, tmp_path: Path) -> None:
        """Flagged totals propagate into the summary."""
        profiler: UserProfiler = UserProfiler(
            str(tmp_path / "users.db"), str(tmp_path / "archive.db"), 91
        )
        for _ in range(91):
            profiler.record("app", "user1", total_msgs=1, flagged_msgs=1)
            self.advance_days(1)
        summary = profiler.get_profile("app", "user1")["summaries"][0]
        assert summary["flagged_msgs"] == 91
        profiler.close()

    def test_cycle_summary_blocked_counts(self, tmp_path: Path) -> None:
        """Blocked totals propagate into the summary."""
        profiler: UserProfiler = UserProfiler(
            str(tmp_path / "users.db"), str(tmp_path / "archive.db"), 91
        )
        for _ in range(91):
            profiler.record("app", "user1", total_msgs=1, blocked_msgs=1)
            self.advance_days(1)
        summary = profiler.get_profile("app", "user1")["summaries"][0]
        assert summary["blocked_msgs"] == 91
        profiler.close()

    def test_second_cycle_linked(self, tmp_path: Path) -> None:
        """A second cycle links to the first through next_cycle_id."""
        profiler: UserProfiler = UserProfiler(
            str(tmp_path / "users.db"), str(tmp_path / "archive.db"), 91
        )
        for _ in range(91):
            profiler.record("app", "user1", total_msgs=1)
            self.advance_days(1)
        for _ in range(91):
            profiler.record("app", "user1", total_msgs=1)
            self.advance_days(1)
        profile = profiler.get_profile("app", "user1")
        assert len(profile["summaries"]) == 2
        assert profile["summaries"][0]["next_cycle_id"] == profile["summaries"][1]["cycle_id"]
        profiler.close()

    def test_third_cycle_chain(self, tmp_path: Path) -> None:
        """Three cycles form a complete linked chain."""
        profiler: UserProfiler = UserProfiler(
            str(tmp_path / "users.db"), str(tmp_path / "archive.db"), 91
        )
        for _ in range(273):
            profiler.record("app", "user1", total_msgs=1)
            self.advance_days(1)
        profile = profiler.get_profile("app", "user1")
        assert [summary["next_cycle_id"] for summary in profile["summaries"]] == [2, 3, None]
        profiler.close()

    def test_archive_ratio_after_cycle(self, tmp_path: Path) -> None:
        """The ratio survives archiving."""
        profiler: UserProfiler = UserProfiler(
            str(tmp_path / "users.db"), str(tmp_path / "archive.db"), 91
        )
        for _ in range(91):
            profiler.record("app", "user1", total_msgs=1, flagged_msgs=1)
            self.advance_days(1)
        assert profiler.get_ratio("app", "user1") == 1.0
        profiler.close()


class TestArchiveSummary(BaseTest):
    """Summary metadata correctness."""

    def test_summary_has_all_fields(self, tmp_path: Path) -> None:
        """A summary exposes every expected field."""
        profiler: UserProfiler = UserProfiler(
            str(tmp_path / "users.db"), str(tmp_path / "archive.db"), 91
        )
        for _ in range(91):
            profiler.record("app", "user1", total_msgs=1)
            self.advance_days(1)
        summary = profiler.get_profile("app", "user1")["summaries"][0]
        for field in (
            "cycle_id",
            "start_day",
            "end_day",
            "total_msgs",
            "flagged_msgs",
            "blocked_msgs",
            "reviewed_msgs",
            "next_cycle_id",
        ):
            assert field in summary
        profiler.close()

    def test_first_cycle_id_one(self, tmp_path: Path) -> None:
        """The first cycle id is one."""
        profiler: UserProfiler = UserProfiler(
            str(tmp_path / "users.db"), str(tmp_path / "archive.db"), 91
        )
        for _ in range(91):
            profiler.record("app", "user1", total_msgs=1)
            self.advance_days(1)
        assert profiler.get_profile("app", "user1")["summaries"][0]["cycle_id"] == 1
        profiler.close()

    def test_cycle_duration_ninety_one(self, tmp_path: Path) -> None:
        """A full cycle spans 91 days."""
        profiler: UserProfiler = UserProfiler(
            str(tmp_path / "users.db"), str(tmp_path / "archive.db"), 91
        )
        for _ in range(91):
            profiler.record("app", "user1", total_msgs=1)
            self.advance_days(1)
        summary = profiler.get_profile("app", "user1")["summaries"][0]
        start = __import__("datetime").date.fromisoformat(summary["start_day"])
        end = __import__("datetime").date.fromisoformat(summary["end_day"])
        assert (end - start).days + 1 == 91
        profiler.close()

    def test_summary_sorted_ascending(self, tmp_path: Path) -> None:
        """Summaries are ordered by cycle id ascending."""
        profiler: UserProfiler = UserProfiler(
            str(tmp_path / "users.db"), str(tmp_path / "archive.db"), 91
        )
        for _ in range(182):
            profiler.record("app", "user1", total_msgs=1)
            self.advance_days(1)
        profile = profiler.get_profile("app", "user1")
        ids: list[int] = [summary["cycle_id"] for summary in profile["summaries"]]
        assert ids == sorted(ids)
        profiler.close()

    def test_archive_table_indexed(self, tmp_path: Path) -> None:
        """The archive user index exists for lookups."""
        profiler: UserProfiler = UserProfiler(
            str(tmp_path / "users.db"), str(tmp_path / "archive.db"), 91
        )
        indexes = profiler._archive.execute(
            "SELECT name FROM sqlite_master WHERE type = 'index' AND tbl_name = 'user_summaries'"
        ).fetchall()
        assert any("idx_summaries_user" in str(row[0]) for row in indexes)
        profiler.close()


class TestArchiveVolume(BaseTest):
    """Data volume variation within a cycle."""

    @pytest.mark.parametrize(
        ("volume", "days"),
        (
            (100, 91),
            (250, 91),
            (500, 91),
            (1000, 91),
            (50, 45),
            (200, 91),
            (10, 91),
            (5, 91),
            (1, 91),
            (3, 91),
            (7, 91),
            (30, 91),
            (60, 91),
            (90, 91),
            (120, 91),
        ),
    )
    def test_volume_archive_total(self, tmp_path: Path, volume: int, days: int) -> None:
        """Total messages equal volume times days.

        :param tmp_path: per-test temporary directory
        :param volume: messages per day
        :param days: number of days recorded
        """
        profiler: UserProfiler = UserProfiler(
            str(tmp_path / "users.db"), str(tmp_path / "archive.db"), 91
        )
        for _ in range(days):
            profiler.record("app", "user1", total_msgs=volume)
            self.advance_days(1)
        profile = profiler.get_profile("app", "user1")
        if days >= 91:
            assert profile["summaries"][0]["total_msgs"] == volume * days
        else:
            assert not profile["summaries"]
            assert sum(row["total_msgs"] for row in profile["daily"]) == volume * days
        profiler.close()


class TestArchivePercentages(BaseTest):
    """Flagged/blocked percentage accuracy."""

    @pytest.mark.parametrize(
        ("flagged_pct", "blocked_pct", "days"),
        (
            (0, 0, 91),
            (5, 0, 91),
            (10, 0, 91),
            (20, 0, 91),
            (30, 0, 91),
            (50, 0, 91),
            (0, 10, 91),
            (0, 20, 91),
            (0, 50, 91),
            (10, 10, 91),
            (20, 20, 91),
            (30, 30, 91),
            (50, 50, 91),
            (100, 0, 91),
            (0, 100, 91),
        ),
    )
    def test_percentage_accuracy(
        self,
        tmp_path: Path,
        flagged_pct: int,
        blocked_pct: int,
        days: int,
    ) -> None:
        """Summary percentages match the configured rates.

        :param tmp_path: per-test temporary directory
        :param flagged_pct: flagged percentage
        :param blocked_pct: blocked percentage
        :param days: cycle length in days
        """
        volume: int = 20
        profiler: UserProfiler = UserProfiler(
            str(tmp_path / "users.db"), str(tmp_path / "archive.db"), 91
        )
        for _ in range(days):
            profiler.record(
                "app",
                "user1",
                total_msgs=volume,
                flagged_msgs=round(volume * flagged_pct / 100),
                blocked_msgs=round(volume * blocked_pct / 100),
            )
            self.advance_days(1)
        summary = profiler.get_profile("app", "user1")["summaries"][0]
        total: int = summary["total_msgs"]
        assert summary["flagged_msgs"] / total * 100 == pytest.approx(flagged_pct, abs=2)
        assert summary["blocked_msgs"] / total * 100 == pytest.approx(blocked_pct, abs=2)
        profiler.close()
