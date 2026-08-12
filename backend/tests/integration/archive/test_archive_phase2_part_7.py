"""Phase 2 archive cycle tests (generated).

Volume and percentage matrices, multi-cycle chains, multi-user/app
archives and boundary edges under the frozen clock."""

# multilingual fixtures use non-ASCII on purpose
from __future__ import annotations

from app.profiling.user_profiler import UserProfiler
from tests.base_test import BaseTest


class TestMultiAppArchive(BaseTest):
    """MultiAppArchive scenarios."""

    def test_multi_app_50_0_3909(self) -> None:
        """Each app archives independently for the shared user."""
        profiler: UserProfiler = UserProfiler(":memory:", ":memory:", 3)
        for _ in range(3):
            for index in range(50):
                flagged = 1 if (index + 0) % 4 == 0 else 0
                profiler.record(f"app{index}", "u", total_msgs=1, flagged_msgs=flagged)
            self.advance_days(1)
        stats = profiler.stats()
        assert stats["summary_count"] == 50
        profiler.close()

    def test_multi_app_50_1_3910(self) -> None:
        """Each app archives independently for the shared user."""
        profiler: UserProfiler = UserProfiler(":memory:", ":memory:", 3)
        for _ in range(3):
            for index in range(50):
                flagged = 1 if (index + 1) % 4 == 0 else 0
                profiler.record(f"app{index}", "u", total_msgs=1, flagged_msgs=flagged)
            self.advance_days(1)
        stats = profiler.stats()
        assert stats["summary_count"] == 50
        profiler.close()

    def test_multi_app_50_2_3911(self) -> None:
        """Each app archives independently for the shared user."""
        profiler: UserProfiler = UserProfiler(":memory:", ":memory:", 3)
        for _ in range(3):
            for index in range(50):
                flagged = 1 if (index + 2) % 4 == 0 else 0
                profiler.record(f"app{index}", "u", total_msgs=1, flagged_msgs=flagged)
            self.advance_days(1)
        stats = profiler.stats()
        assert stats["summary_count"] == 50
        profiler.close()

    def test_multi_app_50_3_3912(self) -> None:
        """Each app archives independently for the shared user."""
        profiler: UserProfiler = UserProfiler(":memory:", ":memory:", 3)
        for _ in range(3):
            for index in range(50):
                flagged = 1 if (index + 3) % 4 == 0 else 0
                profiler.record(f"app{index}", "u", total_msgs=1, flagged_msgs=flagged)
            self.advance_days(1)
        stats = profiler.stats()
        assert stats["summary_count"] == 50
        profiler.close()

    def test_multi_app_50_4_3913(self) -> None:
        """Each app archives independently for the shared user."""
        profiler: UserProfiler = UserProfiler(":memory:", ":memory:", 3)
        for _ in range(3):
            for index in range(50):
                flagged = 1 if (index + 4) % 4 == 0 else 0
                profiler.record(f"app{index}", "u", total_msgs=1, flagged_msgs=flagged)
            self.advance_days(1)
        stats = profiler.stats()
        assert stats["summary_count"] == 50
        profiler.close()

    def test_multi_app_50_5_3914(self) -> None:
        """Each app archives independently for the shared user."""
        profiler: UserProfiler = UserProfiler(":memory:", ":memory:", 3)
        for _ in range(3):
            for index in range(50):
                flagged = 1 if (index + 5) % 4 == 0 else 0
                profiler.record(f"app{index}", "u", total_msgs=1, flagged_msgs=flagged)
            self.advance_days(1)
        stats = profiler.stats()
        assert stats["summary_count"] == 50
        profiler.close()

    def test_multi_app_50_6_3915(self) -> None:
        """Each app archives independently for the shared user."""
        profiler: UserProfiler = UserProfiler(":memory:", ":memory:", 3)
        for _ in range(3):
            for index in range(50):
                flagged = 1 if (index + 6) % 4 == 0 else 0
                profiler.record(f"app{index}", "u", total_msgs=1, flagged_msgs=flagged)
            self.advance_days(1)
        stats = profiler.stats()
        assert stats["summary_count"] == 50
        profiler.close()

    def test_multi_app_50_7_3916(self) -> None:
        """Each app archives independently for the shared user."""
        profiler: UserProfiler = UserProfiler(":memory:", ":memory:", 3)
        for _ in range(3):
            for index in range(50):
                flagged = 1 if (index + 7) % 4 == 0 else 0
                profiler.record(f"app{index}", "u", total_msgs=1, flagged_msgs=flagged)
            self.advance_days(1)
        stats = profiler.stats()
        assert stats["summary_count"] == 50
        profiler.close()

    def test_multi_app_50_8_3917(self) -> None:
        """Each app archives independently for the shared user."""
        profiler: UserProfiler = UserProfiler(":memory:", ":memory:", 3)
        for _ in range(3):
            for index in range(50):
                flagged = 1 if (index + 8) % 4 == 0 else 0
                profiler.record(f"app{index}", "u", total_msgs=1, flagged_msgs=flagged)
            self.advance_days(1)
        stats = profiler.stats()
        assert stats["summary_count"] == 50
        profiler.close()

    def test_multi_app_50_9_3918(self) -> None:
        """Each app archives independently for the shared user."""
        profiler: UserProfiler = UserProfiler(":memory:", ":memory:", 3)
        for _ in range(3):
            for index in range(50):
                flagged = 1 if (index + 9) % 4 == 0 else 0
                profiler.record(f"app{index}", "u", total_msgs=1, flagged_msgs=flagged)
            self.advance_days(1)
        stats = profiler.stats()
        assert stats["summary_count"] == 50
        profiler.close()

    def test_multi_app_50_10_3919(self) -> None:
        """Each app archives independently for the shared user."""
        profiler: UserProfiler = UserProfiler(":memory:", ":memory:", 3)
        for _ in range(3):
            for index in range(50):
                flagged = 1 if (index + 10) % 4 == 0 else 0
                profiler.record(f"app{index}", "u", total_msgs=1, flagged_msgs=flagged)
            self.advance_days(1)
        stats = profiler.stats()
        assert stats["summary_count"] == 50
        profiler.close()

    def test_multi_app_50_11_3920(self) -> None:
        """Each app archives independently for the shared user."""
        profiler: UserProfiler = UserProfiler(":memory:", ":memory:", 3)
        for _ in range(3):
            for index in range(50):
                flagged = 1 if (index + 11) % 4 == 0 else 0
                profiler.record(f"app{index}", "u", total_msgs=1, flagged_msgs=flagged)
            self.advance_days(1)
        stats = profiler.stats()
        assert stats["summary_count"] == 50
        profiler.close()

    def test_multi_app_50_12_3921(self) -> None:
        """Each app archives independently for the shared user."""
        profiler: UserProfiler = UserProfiler(":memory:", ":memory:", 3)
        for _ in range(3):
            for index in range(50):
                flagged = 1 if (index + 12) % 4 == 0 else 0
                profiler.record(f"app{index}", "u", total_msgs=1, flagged_msgs=flagged)
            self.advance_days(1)
        stats = profiler.stats()
        assert stats["summary_count"] == 50
        profiler.close()

    def test_multi_app_50_13_3922(self) -> None:
        """Each app archives independently for the shared user."""
        profiler: UserProfiler = UserProfiler(":memory:", ":memory:", 3)
        for _ in range(3):
            for index in range(50):
                flagged = 1 if (index + 13) % 4 == 0 else 0
                profiler.record(f"app{index}", "u", total_msgs=1, flagged_msgs=flagged)
            self.advance_days(1)
        stats = profiler.stats()
        assert stats["summary_count"] == 50
        profiler.close()

    def test_multi_app_50_14_3923(self) -> None:
        """Each app archives independently for the shared user."""
        profiler: UserProfiler = UserProfiler(":memory:", ":memory:", 3)
        for _ in range(3):
            for index in range(50):
                flagged = 1 if (index + 14) % 4 == 0 else 0
                profiler.record(f"app{index}", "u", total_msgs=1, flagged_msgs=flagged)
            self.advance_days(1)
        stats = profiler.stats()
        assert stats["summary_count"] == 50
        profiler.close()

    def test_multi_app_50_15_3924(self) -> None:
        """Each app archives independently for the shared user."""
        profiler: UserProfiler = UserProfiler(":memory:", ":memory:", 3)
        for _ in range(3):
            for index in range(50):
                flagged = 1 if (index + 15) % 4 == 0 else 0
                profiler.record(f"app{index}", "u", total_msgs=1, flagged_msgs=flagged)
            self.advance_days(1)
        stats = profiler.stats()
        assert stats["summary_count"] == 50
        profiler.close()

    def test_multi_app_50_16_3925(self) -> None:
        """Each app archives independently for the shared user."""
        profiler: UserProfiler = UserProfiler(":memory:", ":memory:", 3)
        for _ in range(3):
            for index in range(50):
                flagged = 1 if (index + 16) % 4 == 0 else 0
                profiler.record(f"app{index}", "u", total_msgs=1, flagged_msgs=flagged)
            self.advance_days(1)
        stats = profiler.stats()
        assert stats["summary_count"] == 50
        profiler.close()

    def test_multi_app_50_17_3926(self) -> None:
        """Each app archives independently for the shared user."""
        profiler: UserProfiler = UserProfiler(":memory:", ":memory:", 3)
        for _ in range(3):
            for index in range(50):
                flagged = 1 if (index + 17) % 4 == 0 else 0
                profiler.record(f"app{index}", "u", total_msgs=1, flagged_msgs=flagged)
            self.advance_days(1)
        stats = profiler.stats()
        assert stats["summary_count"] == 50
        profiler.close()

    def test_multi_app_50_18_3927(self) -> None:
        """Each app archives independently for the shared user."""
        profiler: UserProfiler = UserProfiler(":memory:", ":memory:", 3)
        for _ in range(3):
            for index in range(50):
                flagged = 1 if (index + 18) % 4 == 0 else 0
                profiler.record(f"app{index}", "u", total_msgs=1, flagged_msgs=flagged)
            self.advance_days(1)
        stats = profiler.stats()
        assert stats["summary_count"] == 50
        profiler.close()

    def test_multi_app_50_19_3928(self) -> None:
        """Each app archives independently for the shared user."""
        profiler: UserProfiler = UserProfiler(":memory:", ":memory:", 3)
        for _ in range(3):
            for index in range(50):
                flagged = 1 if (index + 19) % 4 == 0 else 0
                profiler.record(f"app{index}", "u", total_msgs=1, flagged_msgs=flagged)
            self.advance_days(1)
        stats = profiler.stats()
        assert stats["summary_count"] == 50
        profiler.close()

    def test_multi_app_50_20_3929(self) -> None:
        """Each app archives independently for the shared user."""
        profiler: UserProfiler = UserProfiler(":memory:", ":memory:", 3)
        for _ in range(3):
            for index in range(50):
                flagged = 1 if (index + 20) % 4 == 0 else 0
                profiler.record(f"app{index}", "u", total_msgs=1, flagged_msgs=flagged)
            self.advance_days(1)
        stats = profiler.stats()
        assert stats["summary_count"] == 50
        profiler.close()

    def test_multi_app_50_21_3930(self) -> None:
        """Each app archives independently for the shared user."""
        profiler: UserProfiler = UserProfiler(":memory:", ":memory:", 3)
        for _ in range(3):
            for index in range(50):
                flagged = 1 if (index + 21) % 4 == 0 else 0
                profiler.record(f"app{index}", "u", total_msgs=1, flagged_msgs=flagged)
            self.advance_days(1)
        stats = profiler.stats()
        assert stats["summary_count"] == 50
        profiler.close()

    def test_multi_app_50_22_3931(self) -> None:
        """Each app archives independently for the shared user."""
        profiler: UserProfiler = UserProfiler(":memory:", ":memory:", 3)
        for _ in range(3):
            for index in range(50):
                flagged = 1 if (index + 22) % 4 == 0 else 0
                profiler.record(f"app{index}", "u", total_msgs=1, flagged_msgs=flagged)
            self.advance_days(1)
        stats = profiler.stats()
        assert stats["summary_count"] == 50
        profiler.close()

    def test_multi_app_50_23_3932(self) -> None:
        """Each app archives independently for the shared user."""
        profiler: UserProfiler = UserProfiler(":memory:", ":memory:", 3)
        for _ in range(3):
            for index in range(50):
                flagged = 1 if (index + 23) % 4 == 0 else 0
                profiler.record(f"app{index}", "u", total_msgs=1, flagged_msgs=flagged)
            self.advance_days(1)
        stats = profiler.stats()
        assert stats["summary_count"] == 50
        profiler.close()

    def test_multi_app_50_24_3933(self) -> None:
        """Each app archives independently for the shared user."""
        profiler: UserProfiler = UserProfiler(":memory:", ":memory:", 3)
        for _ in range(3):
            for index in range(50):
                flagged = 1 if (index + 24) % 4 == 0 else 0
                profiler.record(f"app{index}", "u", total_msgs=1, flagged_msgs=flagged)
            self.advance_days(1)
        stats = profiler.stats()
        assert stats["summary_count"] == 50
        profiler.close()

    def test_multi_app_100_0_3934(self) -> None:
        """Each app archives independently for the shared user."""
        profiler: UserProfiler = UserProfiler(":memory:", ":memory:", 3)
        for _ in range(3):
            for index in range(100):
                flagged = 1 if (index + 0) % 4 == 0 else 0
                profiler.record(f"app{index}", "u", total_msgs=1, flagged_msgs=flagged)
            self.advance_days(1)
        stats = profiler.stats()
        assert stats["summary_count"] == 100
        profiler.close()

    def test_multi_app_100_1_3935(self) -> None:
        """Each app archives independently for the shared user."""
        profiler: UserProfiler = UserProfiler(":memory:", ":memory:", 3)
        for _ in range(3):
            for index in range(100):
                flagged = 1 if (index + 1) % 4 == 0 else 0
                profiler.record(f"app{index}", "u", total_msgs=1, flagged_msgs=flagged)
            self.advance_days(1)
        stats = profiler.stats()
        assert stats["summary_count"] == 100
        profiler.close()

    def test_multi_app_100_2_3936(self) -> None:
        """Each app archives independently for the shared user."""
        profiler: UserProfiler = UserProfiler(":memory:", ":memory:", 3)
        for _ in range(3):
            for index in range(100):
                flagged = 1 if (index + 2) % 4 == 0 else 0
                profiler.record(f"app{index}", "u", total_msgs=1, flagged_msgs=flagged)
            self.advance_days(1)
        stats = profiler.stats()
        assert stats["summary_count"] == 100
        profiler.close()

    def test_multi_app_100_3_3937(self) -> None:
        """Each app archives independently for the shared user."""
        profiler: UserProfiler = UserProfiler(":memory:", ":memory:", 3)
        for _ in range(3):
            for index in range(100):
                flagged = 1 if (index + 3) % 4 == 0 else 0
                profiler.record(f"app{index}", "u", total_msgs=1, flagged_msgs=flagged)
            self.advance_days(1)
        stats = profiler.stats()
        assert stats["summary_count"] == 100
        profiler.close()

    def test_multi_app_100_4_3938(self) -> None:
        """Each app archives independently for the shared user."""
        profiler: UserProfiler = UserProfiler(":memory:", ":memory:", 3)
        for _ in range(3):
            for index in range(100):
                flagged = 1 if (index + 4) % 4 == 0 else 0
                profiler.record(f"app{index}", "u", total_msgs=1, flagged_msgs=flagged)
            self.advance_days(1)
        stats = profiler.stats()
        assert stats["summary_count"] == 100
        profiler.close()

    def test_multi_app_100_5_3939(self) -> None:
        """Each app archives independently for the shared user."""
        profiler: UserProfiler = UserProfiler(":memory:", ":memory:", 3)
        for _ in range(3):
            for index in range(100):
                flagged = 1 if (index + 5) % 4 == 0 else 0
                profiler.record(f"app{index}", "u", total_msgs=1, flagged_msgs=flagged)
            self.advance_days(1)
        stats = profiler.stats()
        assert stats["summary_count"] == 100
        profiler.close()

    def test_multi_app_100_6_3940(self) -> None:
        """Each app archives independently for the shared user."""
        profiler: UserProfiler = UserProfiler(":memory:", ":memory:", 3)
        for _ in range(3):
            for index in range(100):
                flagged = 1 if (index + 6) % 4 == 0 else 0
                profiler.record(f"app{index}", "u", total_msgs=1, flagged_msgs=flagged)
            self.advance_days(1)
        stats = profiler.stats()
        assert stats["summary_count"] == 100
        profiler.close()

    def test_multi_app_100_7_3941(self) -> None:
        """Each app archives independently for the shared user."""
        profiler: UserProfiler = UserProfiler(":memory:", ":memory:", 3)
        for _ in range(3):
            for index in range(100):
                flagged = 1 if (index + 7) % 4 == 0 else 0
                profiler.record(f"app{index}", "u", total_msgs=1, flagged_msgs=flagged)
            self.advance_days(1)
        stats = profiler.stats()
        assert stats["summary_count"] == 100
        profiler.close()

    def test_multi_app_100_8_3942(self) -> None:
        """Each app archives independently for the shared user."""
        profiler: UserProfiler = UserProfiler(":memory:", ":memory:", 3)
        for _ in range(3):
            for index in range(100):
                flagged = 1 if (index + 8) % 4 == 0 else 0
                profiler.record(f"app{index}", "u", total_msgs=1, flagged_msgs=flagged)
            self.advance_days(1)
        stats = profiler.stats()
        assert stats["summary_count"] == 100
        profiler.close()

    def test_multi_app_100_9_3943(self) -> None:
        """Each app archives independently for the shared user."""
        profiler: UserProfiler = UserProfiler(":memory:", ":memory:", 3)
        for _ in range(3):
            for index in range(100):
                flagged = 1 if (index + 9) % 4 == 0 else 0
                profiler.record(f"app{index}", "u", total_msgs=1, flagged_msgs=flagged)
            self.advance_days(1)
        stats = profiler.stats()
        assert stats["summary_count"] == 100
        profiler.close()

    def test_multi_app_100_10_3944(self) -> None:
        """Each app archives independently for the shared user."""
        profiler: UserProfiler = UserProfiler(":memory:", ":memory:", 3)
        for _ in range(3):
            for index in range(100):
                flagged = 1 if (index + 10) % 4 == 0 else 0
                profiler.record(f"app{index}", "u", total_msgs=1, flagged_msgs=flagged)
            self.advance_days(1)
        stats = profiler.stats()
        assert stats["summary_count"] == 100
        profiler.close()

    def test_multi_app_100_11_3945(self) -> None:
        """Each app archives independently for the shared user."""
        profiler: UserProfiler = UserProfiler(":memory:", ":memory:", 3)
        for _ in range(3):
            for index in range(100):
                flagged = 1 if (index + 11) % 4 == 0 else 0
                profiler.record(f"app{index}", "u", total_msgs=1, flagged_msgs=flagged)
            self.advance_days(1)
        stats = profiler.stats()
        assert stats["summary_count"] == 100
        profiler.close()

    def test_multi_app_100_12_3946(self) -> None:
        """Each app archives independently for the shared user."""
        profiler: UserProfiler = UserProfiler(":memory:", ":memory:", 3)
        for _ in range(3):
            for index in range(100):
                flagged = 1 if (index + 12) % 4 == 0 else 0
                profiler.record(f"app{index}", "u", total_msgs=1, flagged_msgs=flagged)
            self.advance_days(1)
        stats = profiler.stats()
        assert stats["summary_count"] == 100
        profiler.close()

    def test_multi_app_100_13_3947(self) -> None:
        """Each app archives independently for the shared user."""
        profiler: UserProfiler = UserProfiler(":memory:", ":memory:", 3)
        for _ in range(3):
            for index in range(100):
                flagged = 1 if (index + 13) % 4 == 0 else 0
                profiler.record(f"app{index}", "u", total_msgs=1, flagged_msgs=flagged)
            self.advance_days(1)
        stats = profiler.stats()
        assert stats["summary_count"] == 100
        profiler.close()

    def test_multi_app_100_14_3948(self) -> None:
        """Each app archives independently for the shared user."""
        profiler: UserProfiler = UserProfiler(":memory:", ":memory:", 3)
        for _ in range(3):
            for index in range(100):
                flagged = 1 if (index + 14) % 4 == 0 else 0
                profiler.record(f"app{index}", "u", total_msgs=1, flagged_msgs=flagged)
            self.advance_days(1)
        stats = profiler.stats()
        assert stats["summary_count"] == 100
        profiler.close()

    def test_multi_app_100_15_3949(self) -> None:
        """Each app archives independently for the shared user."""
        profiler: UserProfiler = UserProfiler(":memory:", ":memory:", 3)
        for _ in range(3):
            for index in range(100):
                flagged = 1 if (index + 15) % 4 == 0 else 0
                profiler.record(f"app{index}", "u", total_msgs=1, flagged_msgs=flagged)
            self.advance_days(1)
        stats = profiler.stats()
        assert stats["summary_count"] == 100
        profiler.close()

    def test_multi_app_100_16_3950(self) -> None:
        """Each app archives independently for the shared user."""
        profiler: UserProfiler = UserProfiler(":memory:", ":memory:", 3)
        for _ in range(3):
            for index in range(100):
                flagged = 1 if (index + 16) % 4 == 0 else 0
                profiler.record(f"app{index}", "u", total_msgs=1, flagged_msgs=flagged)
            self.advance_days(1)
        stats = profiler.stats()
        assert stats["summary_count"] == 100
        profiler.close()

    def test_multi_app_100_17_3951(self) -> None:
        """Each app archives independently for the shared user."""
        profiler: UserProfiler = UserProfiler(":memory:", ":memory:", 3)
        for _ in range(3):
            for index in range(100):
                flagged = 1 if (index + 17) % 4 == 0 else 0
                profiler.record(f"app{index}", "u", total_msgs=1, flagged_msgs=flagged)
            self.advance_days(1)
        stats = profiler.stats()
        assert stats["summary_count"] == 100
        profiler.close()

    def test_multi_app_100_18_3952(self) -> None:
        """Each app archives independently for the shared user."""
        profiler: UserProfiler = UserProfiler(":memory:", ":memory:", 3)
        for _ in range(3):
            for index in range(100):
                flagged = 1 if (index + 18) % 4 == 0 else 0
                profiler.record(f"app{index}", "u", total_msgs=1, flagged_msgs=flagged)
            self.advance_days(1)
        stats = profiler.stats()
        assert stats["summary_count"] == 100
        profiler.close()

    def test_multi_app_100_19_3953(self) -> None:
        """Each app archives independently for the shared user."""
        profiler: UserProfiler = UserProfiler(":memory:", ":memory:", 3)
        for _ in range(3):
            for index in range(100):
                flagged = 1 if (index + 19) % 4 == 0 else 0
                profiler.record(f"app{index}", "u", total_msgs=1, flagged_msgs=flagged)
            self.advance_days(1)
        stats = profiler.stats()
        assert stats["summary_count"] == 100
        profiler.close()

    def test_multi_app_100_20_3954(self) -> None:
        """Each app archives independently for the shared user."""
        profiler: UserProfiler = UserProfiler(":memory:", ":memory:", 3)
        for _ in range(3):
            for index in range(100):
                flagged = 1 if (index + 20) % 4 == 0 else 0
                profiler.record(f"app{index}", "u", total_msgs=1, flagged_msgs=flagged)
            self.advance_days(1)
        stats = profiler.stats()
        assert stats["summary_count"] == 100
        profiler.close()

    def test_multi_app_100_21_3955(self) -> None:
        """Each app archives independently for the shared user."""
        profiler: UserProfiler = UserProfiler(":memory:", ":memory:", 3)
        for _ in range(3):
            for index in range(100):
                flagged = 1 if (index + 21) % 4 == 0 else 0
                profiler.record(f"app{index}", "u", total_msgs=1, flagged_msgs=flagged)
            self.advance_days(1)
        stats = profiler.stats()
        assert stats["summary_count"] == 100
        profiler.close()

    def test_multi_app_100_22_3956(self) -> None:
        """Each app archives independently for the shared user."""
        profiler: UserProfiler = UserProfiler(":memory:", ":memory:", 3)
        for _ in range(3):
            for index in range(100):
                flagged = 1 if (index + 22) % 4 == 0 else 0
                profiler.record(f"app{index}", "u", total_msgs=1, flagged_msgs=flagged)
            self.advance_days(1)
        stats = profiler.stats()
        assert stats["summary_count"] == 100
        profiler.close()

    def test_multi_app_100_23_3957(self) -> None:
        """Each app archives independently for the shared user."""
        profiler: UserProfiler = UserProfiler(":memory:", ":memory:", 3)
        for _ in range(3):
            for index in range(100):
                flagged = 1 if (index + 23) % 4 == 0 else 0
                profiler.record(f"app{index}", "u", total_msgs=1, flagged_msgs=flagged)
            self.advance_days(1)
        stats = profiler.stats()
        assert stats["summary_count"] == 100
        profiler.close()

    def test_multi_app_100_24_3958(self) -> None:
        """Each app archives independently for the shared user."""
        profiler: UserProfiler = UserProfiler(":memory:", ":memory:", 3)
        for _ in range(3):
            for index in range(100):
                flagged = 1 if (index + 24) % 4 == 0 else 0
                profiler.record(f"app{index}", "u", total_msgs=1, flagged_msgs=flagged)
            self.advance_days(1)
        stats = profiler.stats()
        assert stats["summary_count"] == 100
        profiler.close()


class TestMixedArchive(BaseTest):
    """MixedArchive scenarios."""

    def test_mixed_v10_f10_b5_r5_3959(self) -> None:
        """Mixed-verdict windows archive each counter correctly."""
        profiler: UserProfiler = UserProfiler(":memory:", ":memory:", 91)
        for _ in range(91):
            profiler.record(
                "app",
                "u",
                total_msgs=10,
                flagged_msgs=1,
                blocked_msgs=0,
                reviewed_msgs=0,
            )
            self.advance_days(1)
        profile = profiler.get_profile("app", "u")
        assert len(profile["summaries"]) == 1
        assert profiler.get_ratio("app", "u") == 0.1
        profiler.close()

    def test_mixed_v20_f10_b5_r5_3960(self) -> None:
        """Mixed-verdict windows archive each counter correctly."""
        profiler: UserProfiler = UserProfiler(":memory:", ":memory:", 91)
        for _ in range(91):
            profiler.record(
                "app",
                "u",
                total_msgs=20,
                flagged_msgs=2,
                blocked_msgs=1,
                reviewed_msgs=1,
            )
            self.advance_days(1)
        profile = profiler.get_profile("app", "u")
        assert len(profile["summaries"]) == 1
        assert profiler.get_ratio("app", "u") == 0.15
        profiler.close()

    def test_mixed_v50_f10_b5_r5_3961(self) -> None:
        """Mixed-verdict windows archive each counter correctly."""
        profiler: UserProfiler = UserProfiler(":memory:", ":memory:", 91)
        for _ in range(91):
            profiler.record(
                "app",
                "u",
                total_msgs=50,
                flagged_msgs=5,
                blocked_msgs=2,
                reviewed_msgs=2,
            )
            self.advance_days(1)
        profile = profiler.get_profile("app", "u")
        assert len(profile["summaries"]) == 1
        assert profiler.get_ratio("app", "u") == 0.14
        profiler.close()

    def test_mixed_v100_f10_b5_r5_3962(self) -> None:
        """Mixed-verdict windows archive each counter correctly."""
        profiler: UserProfiler = UserProfiler(":memory:", ":memory:", 91)
        for _ in range(91):
            profiler.record(
                "app",
                "u",
                total_msgs=100,
                flagged_msgs=10,
                blocked_msgs=5,
                reviewed_msgs=5,
            )
            self.advance_days(1)
        profile = profiler.get_profile("app", "u")
        assert len(profile["summaries"]) == 1
        assert profiler.get_ratio("app", "u") == 0.15
        profiler.close()

    def test_mixed_v200_f10_b5_r5_3963(self) -> None:
        """Mixed-verdict windows archive each counter correctly."""
        profiler: UserProfiler = UserProfiler(":memory:", ":memory:", 91)
        for _ in range(91):
            profiler.record(
                "app",
                "u",
                total_msgs=200,
                flagged_msgs=20,
                blocked_msgs=10,
                reviewed_msgs=10,
            )
            self.advance_days(1)
        profile = profiler.get_profile("app", "u")
        assert len(profile["summaries"]) == 1
        assert profiler.get_ratio("app", "u") == 0.15
        profiler.close()

    def test_mixed_v500_f10_b5_r5_3964(self) -> None:
        """Mixed-verdict windows archive each counter correctly."""
        profiler: UserProfiler = UserProfiler(":memory:", ":memory:", 91)
        for _ in range(91):
            profiler.record(
                "app",
                "u",
                total_msgs=500,
                flagged_msgs=50,
                blocked_msgs=25,
                reviewed_msgs=25,
            )
            self.advance_days(1)
        profile = profiler.get_profile("app", "u")
        assert len(profile["summaries"]) == 1
        assert profiler.get_ratio("app", "u") == 0.15
        profiler.close()

    def test_mixed_v1000_f10_b5_r5_3965(self) -> None:
        """Mixed-verdict windows archive each counter correctly."""
        profiler: UserProfiler = UserProfiler(":memory:", ":memory:", 91)
        for _ in range(91):
            profiler.record(
                "app",
                "u",
                total_msgs=1000,
                flagged_msgs=100,
                blocked_msgs=50,
                reviewed_msgs=50,
            )
            self.advance_days(1)
        profile = profiler.get_profile("app", "u")
        assert len(profile["summaries"]) == 1
        assert profiler.get_ratio("app", "u") == 0.15
        profiler.close()

    def test_mixed_v2500_f10_b5_r5_3966(self) -> None:
        """Mixed-verdict windows archive each counter correctly."""
        profiler: UserProfiler = UserProfiler(":memory:", ":memory:", 91)
        for _ in range(91):
            profiler.record(
                "app",
                "u",
                total_msgs=2500,
                flagged_msgs=250,
                blocked_msgs=125,
                reviewed_msgs=125,
            )
            self.advance_days(1)
        profile = profiler.get_profile("app", "u")
        assert len(profile["summaries"]) == 1
        assert profiler.get_ratio("app", "u") == 0.15
        profiler.close()

    def test_mixed_v5000_f10_b5_r5_3967(self) -> None:
        """Mixed-verdict windows archive each counter correctly."""
        profiler: UserProfiler = UserProfiler(":memory:", ":memory:", 91)
        for _ in range(91):
            profiler.record(
                "app",
                "u",
                total_msgs=5000,
                flagged_msgs=500,
                blocked_msgs=250,
                reviewed_msgs=250,
            )
            self.advance_days(1)
        profile = profiler.get_profile("app", "u")
        assert len(profile["summaries"]) == 1
        assert profiler.get_ratio("app", "u") == 0.15
        profiler.close()

    def test_mixed_v7500_f10_b5_r5_3968(self) -> None:
        """Mixed-verdict windows archive each counter correctly."""
        profiler: UserProfiler = UserProfiler(":memory:", ":memory:", 91)
        for _ in range(91):
            profiler.record(
                "app",
                "u",
                total_msgs=7500,
                flagged_msgs=750,
                blocked_msgs=375,
                reviewed_msgs=375,
            )
            self.advance_days(1)
        profile = profiler.get_profile("app", "u")
        assert len(profile["summaries"]) == 1
        assert profiler.get_ratio("app", "u") == 0.15
        profiler.close()

    def test_mixed_v10_f20_b10_r5_3969(self) -> None:
        """Mixed-verdict windows archive each counter correctly."""
        profiler: UserProfiler = UserProfiler(":memory:", ":memory:", 91)
        for _ in range(91):
            profiler.record(
                "app",
                "u",
                total_msgs=10,
                flagged_msgs=2,
                blocked_msgs=1,
                reviewed_msgs=0,
            )
            self.advance_days(1)
        profile = profiler.get_profile("app", "u")
        assert len(profile["summaries"]) == 1
        assert profiler.get_ratio("app", "u") == 0.3
        profiler.close()

    def test_mixed_v20_f20_b10_r5_3970(self) -> None:
        """Mixed-verdict windows archive each counter correctly."""
        profiler: UserProfiler = UserProfiler(":memory:", ":memory:", 91)
        for _ in range(91):
            profiler.record(
                "app",
                "u",
                total_msgs=20,
                flagged_msgs=4,
                blocked_msgs=2,
                reviewed_msgs=1,
            )
            self.advance_days(1)
        profile = profiler.get_profile("app", "u")
        assert len(profile["summaries"]) == 1
        assert profiler.get_ratio("app", "u") == 0.3
        profiler.close()

    def test_mixed_v50_f20_b10_r5_3971(self) -> None:
        """Mixed-verdict windows archive each counter correctly."""
        profiler: UserProfiler = UserProfiler(":memory:", ":memory:", 91)
        for _ in range(91):
            profiler.record(
                "app",
                "u",
                total_msgs=50,
                flagged_msgs=10,
                blocked_msgs=5,
                reviewed_msgs=2,
            )
            self.advance_days(1)
        profile = profiler.get_profile("app", "u")
        assert len(profile["summaries"]) == 1
        assert profiler.get_ratio("app", "u") == 0.3
        profiler.close()

    def test_mixed_v100_f20_b10_r5_3972(self) -> None:
        """Mixed-verdict windows archive each counter correctly."""
        profiler: UserProfiler = UserProfiler(":memory:", ":memory:", 91)
        for _ in range(91):
            profiler.record(
                "app",
                "u",
                total_msgs=100,
                flagged_msgs=20,
                blocked_msgs=10,
                reviewed_msgs=5,
            )
            self.advance_days(1)
        profile = profiler.get_profile("app", "u")
        assert len(profile["summaries"]) == 1
        assert profiler.get_ratio("app", "u") == 0.3
        profiler.close()

    def test_mixed_v200_f20_b10_r5_3973(self) -> None:
        """Mixed-verdict windows archive each counter correctly."""
        profiler: UserProfiler = UserProfiler(":memory:", ":memory:", 91)
        for _ in range(91):
            profiler.record(
                "app",
                "u",
                total_msgs=200,
                flagged_msgs=40,
                blocked_msgs=20,
                reviewed_msgs=10,
            )
            self.advance_days(1)
        profile = profiler.get_profile("app", "u")
        assert len(profile["summaries"]) == 1
        assert profiler.get_ratio("app", "u") == 0.3
        profiler.close()

    def test_mixed_v500_f20_b10_r5_3974(self) -> None:
        """Mixed-verdict windows archive each counter correctly."""
        profiler: UserProfiler = UserProfiler(":memory:", ":memory:", 91)
        for _ in range(91):
            profiler.record(
                "app",
                "u",
                total_msgs=500,
                flagged_msgs=100,
                blocked_msgs=50,
                reviewed_msgs=25,
            )
            self.advance_days(1)
        profile = profiler.get_profile("app", "u")
        assert len(profile["summaries"]) == 1
        assert profiler.get_ratio("app", "u") == 0.3
        profiler.close()

    def test_mixed_v1000_f20_b10_r5_3975(self) -> None:
        """Mixed-verdict windows archive each counter correctly."""
        profiler: UserProfiler = UserProfiler(":memory:", ":memory:", 91)
        for _ in range(91):
            profiler.record(
                "app",
                "u",
                total_msgs=1000,
                flagged_msgs=200,
                blocked_msgs=100,
                reviewed_msgs=50,
            )
            self.advance_days(1)
        profile = profiler.get_profile("app", "u")
        assert len(profile["summaries"]) == 1
        assert profiler.get_ratio("app", "u") == 0.3
        profiler.close()

    def test_mixed_v2500_f20_b10_r5_3976(self) -> None:
        """Mixed-verdict windows archive each counter correctly."""
        profiler: UserProfiler = UserProfiler(":memory:", ":memory:", 91)
        for _ in range(91):
            profiler.record(
                "app",
                "u",
                total_msgs=2500,
                flagged_msgs=500,
                blocked_msgs=250,
                reviewed_msgs=125,
            )
            self.advance_days(1)
        profile = profiler.get_profile("app", "u")
        assert len(profile["summaries"]) == 1
        assert profiler.get_ratio("app", "u") == 0.3
        profiler.close()

    def test_mixed_v5000_f20_b10_r5_3977(self) -> None:
        """Mixed-verdict windows archive each counter correctly."""
        profiler: UserProfiler = UserProfiler(":memory:", ":memory:", 91)
        for _ in range(91):
            profiler.record(
                "app",
                "u",
                total_msgs=5000,
                flagged_msgs=1000,
                blocked_msgs=500,
                reviewed_msgs=250,
            )
            self.advance_days(1)
        profile = profiler.get_profile("app", "u")
        assert len(profile["summaries"]) == 1
        assert profiler.get_ratio("app", "u") == 0.3
        profiler.close()

    def test_mixed_v7500_f20_b10_r5_3978(self) -> None:
        """Mixed-verdict windows archive each counter correctly."""
        profiler: UserProfiler = UserProfiler(":memory:", ":memory:", 91)
        for _ in range(91):
            profiler.record(
                "app",
                "u",
                total_msgs=7500,
                flagged_msgs=1500,
                blocked_msgs=750,
                reviewed_msgs=375,
            )
            self.advance_days(1)
        profile = profiler.get_profile("app", "u")
        assert len(profile["summaries"]) == 1
        assert profiler.get_ratio("app", "u") == 0.3
        profiler.close()

    def test_mixed_v10_f30_b15_r10_3979(self) -> None:
        """Mixed-verdict windows archive each counter correctly."""
        profiler: UserProfiler = UserProfiler(":memory:", ":memory:", 91)
        for _ in range(91):
            profiler.record(
                "app",
                "u",
                total_msgs=10,
                flagged_msgs=3,
                blocked_msgs=2,
                reviewed_msgs=1,
            )
            self.advance_days(1)
        profile = profiler.get_profile("app", "u")
        assert len(profile["summaries"]) == 1
        assert profiler.get_ratio("app", "u") == 0.5
        profiler.close()

    def test_mixed_v20_f30_b15_r10_3980(self) -> None:
        """Mixed-verdict windows archive each counter correctly."""
        profiler: UserProfiler = UserProfiler(":memory:", ":memory:", 91)
        for _ in range(91):
            profiler.record(
                "app",
                "u",
                total_msgs=20,
                flagged_msgs=6,
                blocked_msgs=3,
                reviewed_msgs=2,
            )
            self.advance_days(1)
        profile = profiler.get_profile("app", "u")
        assert len(profile["summaries"]) == 1
        assert profiler.get_ratio("app", "u") == 0.45
        profiler.close()

    def test_mixed_v50_f30_b15_r10_3981(self) -> None:
        """Mixed-verdict windows archive each counter correctly."""
        profiler: UserProfiler = UserProfiler(":memory:", ":memory:", 91)
        for _ in range(91):
            profiler.record(
                "app",
                "u",
                total_msgs=50,
                flagged_msgs=15,
                blocked_msgs=8,
                reviewed_msgs=5,
            )
            self.advance_days(1)
        profile = profiler.get_profile("app", "u")
        assert len(profile["summaries"]) == 1
        assert profiler.get_ratio("app", "u") == 0.46
        profiler.close()

    def test_mixed_v100_f30_b15_r10_3982(self) -> None:
        """Mixed-verdict windows archive each counter correctly."""
        profiler: UserProfiler = UserProfiler(":memory:", ":memory:", 91)
        for _ in range(91):
            profiler.record(
                "app",
                "u",
                total_msgs=100,
                flagged_msgs=30,
                blocked_msgs=15,
                reviewed_msgs=10,
            )
            self.advance_days(1)
        profile = profiler.get_profile("app", "u")
        assert len(profile["summaries"]) == 1
        assert profiler.get_ratio("app", "u") == 0.45
        profiler.close()

    def test_mixed_v200_f30_b15_r10_3983(self) -> None:
        """Mixed-verdict windows archive each counter correctly."""
        profiler: UserProfiler = UserProfiler(":memory:", ":memory:", 91)
        for _ in range(91):
            profiler.record(
                "app",
                "u",
                total_msgs=200,
                flagged_msgs=60,
                blocked_msgs=30,
                reviewed_msgs=20,
            )
            self.advance_days(1)
        profile = profiler.get_profile("app", "u")
        assert len(profile["summaries"]) == 1
        assert profiler.get_ratio("app", "u") == 0.45
        profiler.close()

    def test_mixed_v500_f30_b15_r10_3984(self) -> None:
        """Mixed-verdict windows archive each counter correctly."""
        profiler: UserProfiler = UserProfiler(":memory:", ":memory:", 91)
        for _ in range(91):
            profiler.record(
                "app",
                "u",
                total_msgs=500,
                flagged_msgs=150,
                blocked_msgs=75,
                reviewed_msgs=50,
            )
            self.advance_days(1)
        profile = profiler.get_profile("app", "u")
        assert len(profile["summaries"]) == 1
        assert profiler.get_ratio("app", "u") == 0.45
        profiler.close()

    def test_mixed_v1000_f30_b15_r10_3985(self) -> None:
        """Mixed-verdict windows archive each counter correctly."""
        profiler: UserProfiler = UserProfiler(":memory:", ":memory:", 91)
        for _ in range(91):
            profiler.record(
                "app",
                "u",
                total_msgs=1000,
                flagged_msgs=300,
                blocked_msgs=150,
                reviewed_msgs=100,
            )
            self.advance_days(1)
        profile = profiler.get_profile("app", "u")
        assert len(profile["summaries"]) == 1
        assert profiler.get_ratio("app", "u") == 0.45
        profiler.close()

    def test_mixed_v2500_f30_b15_r10_3986(self) -> None:
        """Mixed-verdict windows archive each counter correctly."""
        profiler: UserProfiler = UserProfiler(":memory:", ":memory:", 91)
        for _ in range(91):
            profiler.record(
                "app",
                "u",
                total_msgs=2500,
                flagged_msgs=750,
                blocked_msgs=375,
                reviewed_msgs=250,
            )
            self.advance_days(1)
        profile = profiler.get_profile("app", "u")
        assert len(profile["summaries"]) == 1
        assert profiler.get_ratio("app", "u") == 0.45
        profiler.close()

    def test_mixed_v5000_f30_b15_r10_3987(self) -> None:
        """Mixed-verdict windows archive each counter correctly."""
        profiler: UserProfiler = UserProfiler(":memory:", ":memory:", 91)
        for _ in range(91):
            profiler.record(
                "app",
                "u",
                total_msgs=5000,
                flagged_msgs=1500,
                blocked_msgs=750,
                reviewed_msgs=500,
            )
            self.advance_days(1)
        profile = profiler.get_profile("app", "u")
        assert len(profile["summaries"]) == 1
        assert profiler.get_ratio("app", "u") == 0.45
        profiler.close()

    def test_mixed_v7500_f30_b15_r10_3988(self) -> None:
        """Mixed-verdict windows archive each counter correctly."""
        profiler: UserProfiler = UserProfiler(":memory:", ":memory:", 91)
        for _ in range(91):
            profiler.record(
                "app",
                "u",
                total_msgs=7500,
                flagged_msgs=2250,
                blocked_msgs=1125,
                reviewed_msgs=750,
            )
            self.advance_days(1)
        profile = profiler.get_profile("app", "u")
        assert len(profile["summaries"]) == 1
        assert profiler.get_ratio("app", "u") == 0.45
        profiler.close()

    def test_mixed_v10_f40_b20_r15_3989(self) -> None:
        """Mixed-verdict windows archive each counter correctly."""
        profiler: UserProfiler = UserProfiler(":memory:", ":memory:", 91)
        for _ in range(91):
            profiler.record(
                "app",
                "u",
                total_msgs=10,
                flagged_msgs=4,
                blocked_msgs=2,
                reviewed_msgs=2,
            )
            self.advance_days(1)
        profile = profiler.get_profile("app", "u")
        assert len(profile["summaries"]) == 1
        assert profiler.get_ratio("app", "u") == 0.6
        profiler.close()

    def test_mixed_v20_f40_b20_r15_3990(self) -> None:
        """Mixed-verdict windows archive each counter correctly."""
        profiler: UserProfiler = UserProfiler(":memory:", ":memory:", 91)
        for _ in range(91):
            profiler.record(
                "app",
                "u",
                total_msgs=20,
                flagged_msgs=8,
                blocked_msgs=4,
                reviewed_msgs=3,
            )
            self.advance_days(1)
        profile = profiler.get_profile("app", "u")
        assert len(profile["summaries"]) == 1
        assert profiler.get_ratio("app", "u") == 0.6
        profiler.close()

    def test_mixed_v50_f40_b20_r15_3991(self) -> None:
        """Mixed-verdict windows archive each counter correctly."""
        profiler: UserProfiler = UserProfiler(":memory:", ":memory:", 91)
        for _ in range(91):
            profiler.record(
                "app",
                "u",
                total_msgs=50,
                flagged_msgs=20,
                blocked_msgs=10,
                reviewed_msgs=8,
            )
            self.advance_days(1)
        profile = profiler.get_profile("app", "u")
        assert len(profile["summaries"]) == 1
        assert profiler.get_ratio("app", "u") == 0.6
        profiler.close()

    def test_mixed_v100_f40_b20_r15_3992(self) -> None:
        """Mixed-verdict windows archive each counter correctly."""
        profiler: UserProfiler = UserProfiler(":memory:", ":memory:", 91)
        for _ in range(91):
            profiler.record(
                "app",
                "u",
                total_msgs=100,
                flagged_msgs=40,
                blocked_msgs=20,
                reviewed_msgs=15,
            )
            self.advance_days(1)
        profile = profiler.get_profile("app", "u")
        assert len(profile["summaries"]) == 1
        assert profiler.get_ratio("app", "u") == 0.6
        profiler.close()

    def test_mixed_v200_f40_b20_r15_3993(self) -> None:
        """Mixed-verdict windows archive each counter correctly."""
        profiler: UserProfiler = UserProfiler(":memory:", ":memory:", 91)
        for _ in range(91):
            profiler.record(
                "app",
                "u",
                total_msgs=200,
                flagged_msgs=80,
                blocked_msgs=40,
                reviewed_msgs=30,
            )
            self.advance_days(1)
        profile = profiler.get_profile("app", "u")
        assert len(profile["summaries"]) == 1
        assert profiler.get_ratio("app", "u") == 0.6
        profiler.close()

    def test_mixed_v500_f40_b20_r15_3994(self) -> None:
        """Mixed-verdict windows archive each counter correctly."""
        profiler: UserProfiler = UserProfiler(":memory:", ":memory:", 91)
        for _ in range(91):
            profiler.record(
                "app",
                "u",
                total_msgs=500,
                flagged_msgs=200,
                blocked_msgs=100,
                reviewed_msgs=75,
            )
            self.advance_days(1)
        profile = profiler.get_profile("app", "u")
        assert len(profile["summaries"]) == 1
        assert profiler.get_ratio("app", "u") == 0.6
        profiler.close()

    def test_mixed_v1000_f40_b20_r15_3995(self) -> None:
        """Mixed-verdict windows archive each counter correctly."""
        profiler: UserProfiler = UserProfiler(":memory:", ":memory:", 91)
        for _ in range(91):
            profiler.record(
                "app",
                "u",
                total_msgs=1000,
                flagged_msgs=400,
                blocked_msgs=200,
                reviewed_msgs=150,
            )
            self.advance_days(1)
        profile = profiler.get_profile("app", "u")
        assert len(profile["summaries"]) == 1
        assert profiler.get_ratio("app", "u") == 0.6
        profiler.close()

    def test_mixed_v2500_f40_b20_r15_3996(self) -> None:
        """Mixed-verdict windows archive each counter correctly."""
        profiler: UserProfiler = UserProfiler(":memory:", ":memory:", 91)
        for _ in range(91):
            profiler.record(
                "app",
                "u",
                total_msgs=2500,
                flagged_msgs=1000,
                blocked_msgs=500,
                reviewed_msgs=375,
            )
            self.advance_days(1)
        profile = profiler.get_profile("app", "u")
        assert len(profile["summaries"]) == 1
        assert profiler.get_ratio("app", "u") == 0.6
        profiler.close()

    def test_mixed_v5000_f40_b20_r15_3997(self) -> None:
        """Mixed-verdict windows archive each counter correctly."""
        profiler: UserProfiler = UserProfiler(":memory:", ":memory:", 91)
        for _ in range(91):
            profiler.record(
                "app",
                "u",
                total_msgs=5000,
                flagged_msgs=2000,
                blocked_msgs=1000,
                reviewed_msgs=750,
            )
            self.advance_days(1)
        profile = profiler.get_profile("app", "u")
        assert len(profile["summaries"]) == 1
        assert profiler.get_ratio("app", "u") == 0.6
        profiler.close()

    def test_mixed_v7500_f40_b20_r15_3998(self) -> None:
        """Mixed-verdict windows archive each counter correctly."""
        profiler: UserProfiler = UserProfiler(":memory:", ":memory:", 91)
        for _ in range(91):
            profiler.record(
                "app",
                "u",
                total_msgs=7500,
                flagged_msgs=3000,
                blocked_msgs=1500,
                reviewed_msgs=1125,
            )
            self.advance_days(1)
        profile = profiler.get_profile("app", "u")
        assert len(profile["summaries"]) == 1
        assert profiler.get_ratio("app", "u") == 0.6
        profiler.close()

    def test_mixed_v10_f50_b25_r10_3999(self) -> None:
        """Mixed-verdict windows archive each counter correctly."""
        profiler: UserProfiler = UserProfiler(":memory:", ":memory:", 91)
        for _ in range(91):
            profiler.record(
                "app",
                "u",
                total_msgs=10,
                flagged_msgs=5,
                blocked_msgs=2,
                reviewed_msgs=1,
            )
            self.advance_days(1)
        profile = profiler.get_profile("app", "u")
        assert len(profile["summaries"]) == 1
        assert profiler.get_ratio("app", "u") == 0.7
        profiler.close()

    def test_mixed_v20_f50_b25_r10_4000(self) -> None:
        """Mixed-verdict windows archive each counter correctly."""
        profiler: UserProfiler = UserProfiler(":memory:", ":memory:", 91)
        for _ in range(91):
            profiler.record(
                "app",
                "u",
                total_msgs=20,
                flagged_msgs=10,
                blocked_msgs=5,
                reviewed_msgs=2,
            )
            self.advance_days(1)
        profile = profiler.get_profile("app", "u")
        assert len(profile["summaries"]) == 1
        assert profiler.get_ratio("app", "u") == 0.75
        profiler.close()

    def test_mixed_v50_f50_b25_r10_4001(self) -> None:
        """Mixed-verdict windows archive each counter correctly."""
        profiler: UserProfiler = UserProfiler(":memory:", ":memory:", 91)
        for _ in range(91):
            profiler.record(
                "app",
                "u",
                total_msgs=50,
                flagged_msgs=25,
                blocked_msgs=12,
                reviewed_msgs=5,
            )
            self.advance_days(1)
        profile = profiler.get_profile("app", "u")
        assert len(profile["summaries"]) == 1
        assert profiler.get_ratio("app", "u") == 0.74
        profiler.close()

    def test_mixed_v100_f50_b25_r10_4002(self) -> None:
        """Mixed-verdict windows archive each counter correctly."""
        profiler: UserProfiler = UserProfiler(":memory:", ":memory:", 91)
        for _ in range(91):
            profiler.record(
                "app",
                "u",
                total_msgs=100,
                flagged_msgs=50,
                blocked_msgs=25,
                reviewed_msgs=10,
            )
            self.advance_days(1)
        profile = profiler.get_profile("app", "u")
        assert len(profile["summaries"]) == 1
        assert profiler.get_ratio("app", "u") == 0.75
        profiler.close()

    def test_mixed_v200_f50_b25_r10_4003(self) -> None:
        """Mixed-verdict windows archive each counter correctly."""
        profiler: UserProfiler = UserProfiler(":memory:", ":memory:", 91)
        for _ in range(91):
            profiler.record(
                "app",
                "u",
                total_msgs=200,
                flagged_msgs=100,
                blocked_msgs=50,
                reviewed_msgs=20,
            )
            self.advance_days(1)
        profile = profiler.get_profile("app", "u")
        assert len(profile["summaries"]) == 1
        assert profiler.get_ratio("app", "u") == 0.75
        profiler.close()

    def test_mixed_v500_f50_b25_r10_4004(self) -> None:
        """Mixed-verdict windows archive each counter correctly."""
        profiler: UserProfiler = UserProfiler(":memory:", ":memory:", 91)
        for _ in range(91):
            profiler.record(
                "app",
                "u",
                total_msgs=500,
                flagged_msgs=250,
                blocked_msgs=125,
                reviewed_msgs=50,
            )
            self.advance_days(1)
        profile = profiler.get_profile("app", "u")
        assert len(profile["summaries"]) == 1
        assert profiler.get_ratio("app", "u") == 0.75
        profiler.close()

    def test_mixed_v1000_f50_b25_r10_4005(self) -> None:
        """Mixed-verdict windows archive each counter correctly."""
        profiler: UserProfiler = UserProfiler(":memory:", ":memory:", 91)
        for _ in range(91):
            profiler.record(
                "app",
                "u",
                total_msgs=1000,
                flagged_msgs=500,
                blocked_msgs=250,
                reviewed_msgs=100,
            )
            self.advance_days(1)
        profile = profiler.get_profile("app", "u")
        assert len(profile["summaries"]) == 1
        assert profiler.get_ratio("app", "u") == 0.75
        profiler.close()

    def test_mixed_v2500_f50_b25_r10_4006(self) -> None:
        """Mixed-verdict windows archive each counter correctly."""
        profiler: UserProfiler = UserProfiler(":memory:", ":memory:", 91)
        for _ in range(91):
            profiler.record(
                "app",
                "u",
                total_msgs=2500,
                flagged_msgs=1250,
                blocked_msgs=625,
                reviewed_msgs=250,
            )
            self.advance_days(1)
        profile = profiler.get_profile("app", "u")
        assert len(profile["summaries"]) == 1
        assert profiler.get_ratio("app", "u") == 0.75
        profiler.close()

    def test_mixed_v5000_f50_b25_r10_4007(self) -> None:
        """Mixed-verdict windows archive each counter correctly."""
        profiler: UserProfiler = UserProfiler(":memory:", ":memory:", 91)
        for _ in range(91):
            profiler.record(
                "app",
                "u",
                total_msgs=5000,
                flagged_msgs=2500,
                blocked_msgs=1250,
                reviewed_msgs=500,
            )
            self.advance_days(1)
        profile = profiler.get_profile("app", "u")
        assert len(profile["summaries"]) == 1
        assert profiler.get_ratio("app", "u") == 0.75
        profiler.close()

    def test_mixed_v7500_f50_b25_r10_4008(self) -> None:
        """Mixed-verdict windows archive each counter correctly."""
        profiler: UserProfiler = UserProfiler(":memory:", ":memory:", 91)
        for _ in range(91):
            profiler.record(
                "app",
                "u",
                total_msgs=7500,
                flagged_msgs=3750,
                blocked_msgs=1875,
                reviewed_msgs=750,
            )
            self.advance_days(1)
        profile = profiler.get_profile("app", "u")
        assert len(profile["summaries"]) == 1
        assert profiler.get_ratio("app", "u") == 0.75
        profiler.close()
