"""Phase 2 user profiling tests (generated).

Ratio matrices, window sweeps, multi-user/app archives and cycle
chains under the frozen clock; see tests/tools/phase2_generator.py."""

# multilingual fixtures use non-ASCII on purpose
from __future__ import annotations

from app.profiling.user_profiler import UserProfiler
from tests.base_test import BaseTest


class TestMultiApp(BaseTest):
    """MultiApp scenarios."""

    def test_multi_app_20_9_3101(self) -> None:
        """Each app archives independently for the shared user."""
        profiler: UserProfiler = UserProfiler(":memory:", ":memory:", 3)
        for _ in range(3):
            for index in range(20):
                flagged = 1 if (index + 9) % 3 == 0 else 0
                profiler.record(f"app{index}", "u", total_msgs=1, flagged_msgs=flagged)
            self.advance_days(1)
        stats = profiler.stats()
        assert stats["summary_count"] == 20
        profiler.close()

    def test_multi_app_20_10_3102(self) -> None:
        """Each app archives independently for the shared user."""
        profiler: UserProfiler = UserProfiler(":memory:", ":memory:", 3)
        for _ in range(3):
            for index in range(20):
                flagged = 1 if (index + 10) % 3 == 0 else 0
                profiler.record(f"app{index}", "u", total_msgs=1, flagged_msgs=flagged)
            self.advance_days(1)
        stats = profiler.stats()
        assert stats["summary_count"] == 20
        profiler.close()

    def test_multi_app_20_11_3103(self) -> None:
        """Each app archives independently for the shared user."""
        profiler: UserProfiler = UserProfiler(":memory:", ":memory:", 3)
        for _ in range(3):
            for index in range(20):
                flagged = 1 if (index + 11) % 3 == 0 else 0
                profiler.record(f"app{index}", "u", total_msgs=1, flagged_msgs=flagged)
            self.advance_days(1)
        stats = profiler.stats()
        assert stats["summary_count"] == 20
        profiler.close()

    def test_multi_app_20_12_3104(self) -> None:
        """Each app archives independently for the shared user."""
        profiler: UserProfiler = UserProfiler(":memory:", ":memory:", 3)
        for _ in range(3):
            for index in range(20):
                flagged = 1 if (index + 12) % 3 == 0 else 0
                profiler.record(f"app{index}", "u", total_msgs=1, flagged_msgs=flagged)
            self.advance_days(1)
        stats = profiler.stats()
        assert stats["summary_count"] == 20
        profiler.close()

    def test_multi_app_20_13_3105(self) -> None:
        """Each app archives independently for the shared user."""
        profiler: UserProfiler = UserProfiler(":memory:", ":memory:", 3)
        for _ in range(3):
            for index in range(20):
                flagged = 1 if (index + 13) % 3 == 0 else 0
                profiler.record(f"app{index}", "u", total_msgs=1, flagged_msgs=flagged)
            self.advance_days(1)
        stats = profiler.stats()
        assert stats["summary_count"] == 20
        profiler.close()

    def test_multi_app_20_14_3106(self) -> None:
        """Each app archives independently for the shared user."""
        profiler: UserProfiler = UserProfiler(":memory:", ":memory:", 3)
        for _ in range(3):
            for index in range(20):
                flagged = 1 if (index + 14) % 3 == 0 else 0
                profiler.record(f"app{index}", "u", total_msgs=1, flagged_msgs=flagged)
            self.advance_days(1)
        stats = profiler.stats()
        assert stats["summary_count"] == 20
        profiler.close()

    def test_multi_app_20_15_3107(self) -> None:
        """Each app archives independently for the shared user."""
        profiler: UserProfiler = UserProfiler(":memory:", ":memory:", 3)
        for _ in range(3):
            for index in range(20):
                flagged = 1 if (index + 15) % 3 == 0 else 0
                profiler.record(f"app{index}", "u", total_msgs=1, flagged_msgs=flagged)
            self.advance_days(1)
        stats = profiler.stats()
        assert stats["summary_count"] == 20
        profiler.close()

    def test_multi_app_20_16_3108(self) -> None:
        """Each app archives independently for the shared user."""
        profiler: UserProfiler = UserProfiler(":memory:", ":memory:", 3)
        for _ in range(3):
            for index in range(20):
                flagged = 1 if (index + 16) % 3 == 0 else 0
                profiler.record(f"app{index}", "u", total_msgs=1, flagged_msgs=flagged)
            self.advance_days(1)
        stats = profiler.stats()
        assert stats["summary_count"] == 20
        profiler.close()

    def test_multi_app_50_0_3109(self) -> None:
        """Each app archives independently for the shared user."""
        profiler: UserProfiler = UserProfiler(":memory:", ":memory:", 3)
        for _ in range(3):
            for index in range(50):
                flagged = 1 if (index + 0) % 3 == 0 else 0
                profiler.record(f"app{index}", "u", total_msgs=1, flagged_msgs=flagged)
            self.advance_days(1)
        stats = profiler.stats()
        assert stats["summary_count"] == 50
        profiler.close()

    def test_multi_app_50_1_3110(self) -> None:
        """Each app archives independently for the shared user."""
        profiler: UserProfiler = UserProfiler(":memory:", ":memory:", 3)
        for _ in range(3):
            for index in range(50):
                flagged = 1 if (index + 1) % 3 == 0 else 0
                profiler.record(f"app{index}", "u", total_msgs=1, flagged_msgs=flagged)
            self.advance_days(1)
        stats = profiler.stats()
        assert stats["summary_count"] == 50
        profiler.close()

    def test_multi_app_50_2_3111(self) -> None:
        """Each app archives independently for the shared user."""
        profiler: UserProfiler = UserProfiler(":memory:", ":memory:", 3)
        for _ in range(3):
            for index in range(50):
                flagged = 1 if (index + 2) % 3 == 0 else 0
                profiler.record(f"app{index}", "u", total_msgs=1, flagged_msgs=flagged)
            self.advance_days(1)
        stats = profiler.stats()
        assert stats["summary_count"] == 50
        profiler.close()

    def test_multi_app_50_3_3112(self) -> None:
        """Each app archives independently for the shared user."""
        profiler: UserProfiler = UserProfiler(":memory:", ":memory:", 3)
        for _ in range(3):
            for index in range(50):
                flagged = 1 if (index + 3) % 3 == 0 else 0
                profiler.record(f"app{index}", "u", total_msgs=1, flagged_msgs=flagged)
            self.advance_days(1)
        stats = profiler.stats()
        assert stats["summary_count"] == 50
        profiler.close()

    def test_multi_app_50_4_3113(self) -> None:
        """Each app archives independently for the shared user."""
        profiler: UserProfiler = UserProfiler(":memory:", ":memory:", 3)
        for _ in range(3):
            for index in range(50):
                flagged = 1 if (index + 4) % 3 == 0 else 0
                profiler.record(f"app{index}", "u", total_msgs=1, flagged_msgs=flagged)
            self.advance_days(1)
        stats = profiler.stats()
        assert stats["summary_count"] == 50
        profiler.close()

    def test_multi_app_50_5_3114(self) -> None:
        """Each app archives independently for the shared user."""
        profiler: UserProfiler = UserProfiler(":memory:", ":memory:", 3)
        for _ in range(3):
            for index in range(50):
                flagged = 1 if (index + 5) % 3 == 0 else 0
                profiler.record(f"app{index}", "u", total_msgs=1, flagged_msgs=flagged)
            self.advance_days(1)
        stats = profiler.stats()
        assert stats["summary_count"] == 50
        profiler.close()

    def test_multi_app_50_6_3115(self) -> None:
        """Each app archives independently for the shared user."""
        profiler: UserProfiler = UserProfiler(":memory:", ":memory:", 3)
        for _ in range(3):
            for index in range(50):
                flagged = 1 if (index + 6) % 3 == 0 else 0
                profiler.record(f"app{index}", "u", total_msgs=1, flagged_msgs=flagged)
            self.advance_days(1)
        stats = profiler.stats()
        assert stats["summary_count"] == 50
        profiler.close()

    def test_multi_app_50_7_3116(self) -> None:
        """Each app archives independently for the shared user."""
        profiler: UserProfiler = UserProfiler(":memory:", ":memory:", 3)
        for _ in range(3):
            for index in range(50):
                flagged = 1 if (index + 7) % 3 == 0 else 0
                profiler.record(f"app{index}", "u", total_msgs=1, flagged_msgs=flagged)
            self.advance_days(1)
        stats = profiler.stats()
        assert stats["summary_count"] == 50
        profiler.close()

    def test_multi_app_50_8_3117(self) -> None:
        """Each app archives independently for the shared user."""
        profiler: UserProfiler = UserProfiler(":memory:", ":memory:", 3)
        for _ in range(3):
            for index in range(50):
                flagged = 1 if (index + 8) % 3 == 0 else 0
                profiler.record(f"app{index}", "u", total_msgs=1, flagged_msgs=flagged)
            self.advance_days(1)
        stats = profiler.stats()
        assert stats["summary_count"] == 50
        profiler.close()

    def test_multi_app_50_9_3118(self) -> None:
        """Each app archives independently for the shared user."""
        profiler: UserProfiler = UserProfiler(":memory:", ":memory:", 3)
        for _ in range(3):
            for index in range(50):
                flagged = 1 if (index + 9) % 3 == 0 else 0
                profiler.record(f"app{index}", "u", total_msgs=1, flagged_msgs=flagged)
            self.advance_days(1)
        stats = profiler.stats()
        assert stats["summary_count"] == 50
        profiler.close()

    def test_multi_app_50_10_3119(self) -> None:
        """Each app archives independently for the shared user."""
        profiler: UserProfiler = UserProfiler(":memory:", ":memory:", 3)
        for _ in range(3):
            for index in range(50):
                flagged = 1 if (index + 10) % 3 == 0 else 0
                profiler.record(f"app{index}", "u", total_msgs=1, flagged_msgs=flagged)
            self.advance_days(1)
        stats = profiler.stats()
        assert stats["summary_count"] == 50
        profiler.close()

    def test_multi_app_50_11_3120(self) -> None:
        """Each app archives independently for the shared user."""
        profiler: UserProfiler = UserProfiler(":memory:", ":memory:", 3)
        for _ in range(3):
            for index in range(50):
                flagged = 1 if (index + 11) % 3 == 0 else 0
                profiler.record(f"app{index}", "u", total_msgs=1, flagged_msgs=flagged)
            self.advance_days(1)
        stats = profiler.stats()
        assert stats["summary_count"] == 50
        profiler.close()

    def test_multi_app_50_12_3121(self) -> None:
        """Each app archives independently for the shared user."""
        profiler: UserProfiler = UserProfiler(":memory:", ":memory:", 3)
        for _ in range(3):
            for index in range(50):
                flagged = 1 if (index + 12) % 3 == 0 else 0
                profiler.record(f"app{index}", "u", total_msgs=1, flagged_msgs=flagged)
            self.advance_days(1)
        stats = profiler.stats()
        assert stats["summary_count"] == 50
        profiler.close()

    def test_multi_app_50_13_3122(self) -> None:
        """Each app archives independently for the shared user."""
        profiler: UserProfiler = UserProfiler(":memory:", ":memory:", 3)
        for _ in range(3):
            for index in range(50):
                flagged = 1 if (index + 13) % 3 == 0 else 0
                profiler.record(f"app{index}", "u", total_msgs=1, flagged_msgs=flagged)
            self.advance_days(1)
        stats = profiler.stats()
        assert stats["summary_count"] == 50
        profiler.close()

    def test_multi_app_50_14_3123(self) -> None:
        """Each app archives independently for the shared user."""
        profiler: UserProfiler = UserProfiler(":memory:", ":memory:", 3)
        for _ in range(3):
            for index in range(50):
                flagged = 1 if (index + 14) % 3 == 0 else 0
                profiler.record(f"app{index}", "u", total_msgs=1, flagged_msgs=flagged)
            self.advance_days(1)
        stats = profiler.stats()
        assert stats["summary_count"] == 50
        profiler.close()

    def test_multi_app_50_15_3124(self) -> None:
        """Each app archives independently for the shared user."""
        profiler: UserProfiler = UserProfiler(":memory:", ":memory:", 3)
        for _ in range(3):
            for index in range(50):
                flagged = 1 if (index + 15) % 3 == 0 else 0
                profiler.record(f"app{index}", "u", total_msgs=1, flagged_msgs=flagged)
            self.advance_days(1)
        stats = profiler.stats()
        assert stats["summary_count"] == 50
        profiler.close()

    def test_multi_app_50_16_3125(self) -> None:
        """Each app archives independently for the shared user."""
        profiler: UserProfiler = UserProfiler(":memory:", ":memory:", 3)
        for _ in range(3):
            for index in range(50):
                flagged = 1 if (index + 16) % 3 == 0 else 0
                profiler.record(f"app{index}", "u", total_msgs=1, flagged_msgs=flagged)
            self.advance_days(1)
        stats = profiler.stats()
        assert stats["summary_count"] == 50
        profiler.close()

    def test_multi_app_100_0_3126(self) -> None:
        """Each app archives independently for the shared user."""
        profiler: UserProfiler = UserProfiler(":memory:", ":memory:", 3)
        for _ in range(3):
            for index in range(100):
                flagged = 1 if (index + 0) % 3 == 0 else 0
                profiler.record(f"app{index}", "u", total_msgs=1, flagged_msgs=flagged)
            self.advance_days(1)
        stats = profiler.stats()
        assert stats["summary_count"] == 100
        profiler.close()

    def test_multi_app_100_1_3127(self) -> None:
        """Each app archives independently for the shared user."""
        profiler: UserProfiler = UserProfiler(":memory:", ":memory:", 3)
        for _ in range(3):
            for index in range(100):
                flagged = 1 if (index + 1) % 3 == 0 else 0
                profiler.record(f"app{index}", "u", total_msgs=1, flagged_msgs=flagged)
            self.advance_days(1)
        stats = profiler.stats()
        assert stats["summary_count"] == 100
        profiler.close()

    def test_multi_app_100_2_3128(self) -> None:
        """Each app archives independently for the shared user."""
        profiler: UserProfiler = UserProfiler(":memory:", ":memory:", 3)
        for _ in range(3):
            for index in range(100):
                flagged = 1 if (index + 2) % 3 == 0 else 0
                profiler.record(f"app{index}", "u", total_msgs=1, flagged_msgs=flagged)
            self.advance_days(1)
        stats = profiler.stats()
        assert stats["summary_count"] == 100
        profiler.close()

    def test_multi_app_100_3_3129(self) -> None:
        """Each app archives independently for the shared user."""
        profiler: UserProfiler = UserProfiler(":memory:", ":memory:", 3)
        for _ in range(3):
            for index in range(100):
                flagged = 1 if (index + 3) % 3 == 0 else 0
                profiler.record(f"app{index}", "u", total_msgs=1, flagged_msgs=flagged)
            self.advance_days(1)
        stats = profiler.stats()
        assert stats["summary_count"] == 100
        profiler.close()

    def test_multi_app_100_4_3130(self) -> None:
        """Each app archives independently for the shared user."""
        profiler: UserProfiler = UserProfiler(":memory:", ":memory:", 3)
        for _ in range(3):
            for index in range(100):
                flagged = 1 if (index + 4) % 3 == 0 else 0
                profiler.record(f"app{index}", "u", total_msgs=1, flagged_msgs=flagged)
            self.advance_days(1)
        stats = profiler.stats()
        assert stats["summary_count"] == 100
        profiler.close()

    def test_multi_app_100_5_3131(self) -> None:
        """Each app archives independently for the shared user."""
        profiler: UserProfiler = UserProfiler(":memory:", ":memory:", 3)
        for _ in range(3):
            for index in range(100):
                flagged = 1 if (index + 5) % 3 == 0 else 0
                profiler.record(f"app{index}", "u", total_msgs=1, flagged_msgs=flagged)
            self.advance_days(1)
        stats = profiler.stats()
        assert stats["summary_count"] == 100
        profiler.close()

    def test_multi_app_100_6_3132(self) -> None:
        """Each app archives independently for the shared user."""
        profiler: UserProfiler = UserProfiler(":memory:", ":memory:", 3)
        for _ in range(3):
            for index in range(100):
                flagged = 1 if (index + 6) % 3 == 0 else 0
                profiler.record(f"app{index}", "u", total_msgs=1, flagged_msgs=flagged)
            self.advance_days(1)
        stats = profiler.stats()
        assert stats["summary_count"] == 100
        profiler.close()

    def test_multi_app_100_7_3133(self) -> None:
        """Each app archives independently for the shared user."""
        profiler: UserProfiler = UserProfiler(":memory:", ":memory:", 3)
        for _ in range(3):
            for index in range(100):
                flagged = 1 if (index + 7) % 3 == 0 else 0
                profiler.record(f"app{index}", "u", total_msgs=1, flagged_msgs=flagged)
            self.advance_days(1)
        stats = profiler.stats()
        assert stats["summary_count"] == 100
        profiler.close()

    def test_multi_app_100_8_3134(self) -> None:
        """Each app archives independently for the shared user."""
        profiler: UserProfiler = UserProfiler(":memory:", ":memory:", 3)
        for _ in range(3):
            for index in range(100):
                flagged = 1 if (index + 8) % 3 == 0 else 0
                profiler.record(f"app{index}", "u", total_msgs=1, flagged_msgs=flagged)
            self.advance_days(1)
        stats = profiler.stats()
        assert stats["summary_count"] == 100
        profiler.close()

    def test_multi_app_100_9_3135(self) -> None:
        """Each app archives independently for the shared user."""
        profiler: UserProfiler = UserProfiler(":memory:", ":memory:", 3)
        for _ in range(3):
            for index in range(100):
                flagged = 1 if (index + 9) % 3 == 0 else 0
                profiler.record(f"app{index}", "u", total_msgs=1, flagged_msgs=flagged)
            self.advance_days(1)
        stats = profiler.stats()
        assert stats["summary_count"] == 100
        profiler.close()

    def test_multi_app_100_10_3136(self) -> None:
        """Each app archives independently for the shared user."""
        profiler: UserProfiler = UserProfiler(":memory:", ":memory:", 3)
        for _ in range(3):
            for index in range(100):
                flagged = 1 if (index + 10) % 3 == 0 else 0
                profiler.record(f"app{index}", "u", total_msgs=1, flagged_msgs=flagged)
            self.advance_days(1)
        stats = profiler.stats()
        assert stats["summary_count"] == 100
        profiler.close()

    def test_multi_app_100_11_3137(self) -> None:
        """Each app archives independently for the shared user."""
        profiler: UserProfiler = UserProfiler(":memory:", ":memory:", 3)
        for _ in range(3):
            for index in range(100):
                flagged = 1 if (index + 11) % 3 == 0 else 0
                profiler.record(f"app{index}", "u", total_msgs=1, flagged_msgs=flagged)
            self.advance_days(1)
        stats = profiler.stats()
        assert stats["summary_count"] == 100
        profiler.close()

    def test_multi_app_100_12_3138(self) -> None:
        """Each app archives independently for the shared user."""
        profiler: UserProfiler = UserProfiler(":memory:", ":memory:", 3)
        for _ in range(3):
            for index in range(100):
                flagged = 1 if (index + 12) % 3 == 0 else 0
                profiler.record(f"app{index}", "u", total_msgs=1, flagged_msgs=flagged)
            self.advance_days(1)
        stats = profiler.stats()
        assert stats["summary_count"] == 100
        profiler.close()

    def test_multi_app_100_13_3139(self) -> None:
        """Each app archives independently for the shared user."""
        profiler: UserProfiler = UserProfiler(":memory:", ":memory:", 3)
        for _ in range(3):
            for index in range(100):
                flagged = 1 if (index + 13) % 3 == 0 else 0
                profiler.record(f"app{index}", "u", total_msgs=1, flagged_msgs=flagged)
            self.advance_days(1)
        stats = profiler.stats()
        assert stats["summary_count"] == 100
        profiler.close()

    def test_multi_app_100_14_3140(self) -> None:
        """Each app archives independently for the shared user."""
        profiler: UserProfiler = UserProfiler(":memory:", ":memory:", 3)
        for _ in range(3):
            for index in range(100):
                flagged = 1 if (index + 14) % 3 == 0 else 0
                profiler.record(f"app{index}", "u", total_msgs=1, flagged_msgs=flagged)
            self.advance_days(1)
        stats = profiler.stats()
        assert stats["summary_count"] == 100
        profiler.close()


class TestCycles(BaseTest):
    """Cycles scenarios."""

    def test_cycles_2_0_3143(self) -> None:
        """Repeated short windows produce the expected cycle count."""
        profiler: UserProfiler = UserProfiler(":memory:", ":memory:", 2)
        for _ in range(4):
            profiler.record("app", "u", total_msgs=1, flagged_msgs=0)
            self.advance_days(1)
        profile = profiler.get_profile("app", "u")
        assert len(profile["summaries"]) == 2
        profiler.close()

    def test_cycles_2_1_3144(self) -> None:
        """Repeated short windows produce the expected cycle count."""
        profiler: UserProfiler = UserProfiler(":memory:", ":memory:", 2)
        for _ in range(4):
            profiler.record("app", "u", total_msgs=1, flagged_msgs=1)
            self.advance_days(1)
        profile = profiler.get_profile("app", "u")
        assert len(profile["summaries"]) == 2
        profiler.close()

    def test_cycles_2_2_3145(self) -> None:
        """Repeated short windows produce the expected cycle count."""
        profiler: UserProfiler = UserProfiler(":memory:", ":memory:", 2)
        for _ in range(4):
            profiler.record("app", "u", total_msgs=1, flagged_msgs=0)
            self.advance_days(1)
        profile = profiler.get_profile("app", "u")
        assert len(profile["summaries"]) == 2
        profiler.close()

    def test_cycles_2_3_3146(self) -> None:
        """Repeated short windows produce the expected cycle count."""
        profiler: UserProfiler = UserProfiler(":memory:", ":memory:", 2)
        for _ in range(4):
            profiler.record("app", "u", total_msgs=1, flagged_msgs=1)
            self.advance_days(1)
        profile = profiler.get_profile("app", "u")
        assert len(profile["summaries"]) == 2
        profiler.close()

    def test_cycles_2_4_3147(self) -> None:
        """Repeated short windows produce the expected cycle count."""
        profiler: UserProfiler = UserProfiler(":memory:", ":memory:", 2)
        for _ in range(4):
            profiler.record("app", "u", total_msgs=1, flagged_msgs=0)
            self.advance_days(1)
        profile = profiler.get_profile("app", "u")
        assert len(profile["summaries"]) == 2
        profiler.close()

    def test_cycles_2_5_3148(self) -> None:
        """Repeated short windows produce the expected cycle count."""
        profiler: UserProfiler = UserProfiler(":memory:", ":memory:", 2)
        for _ in range(4):
            profiler.record("app", "u", total_msgs=1, flagged_msgs=1)
            self.advance_days(1)
        profile = profiler.get_profile("app", "u")
        assert len(profile["summaries"]) == 2
        profiler.close()

    def test_cycles_2_6_3149(self) -> None:
        """Repeated short windows produce the expected cycle count."""
        profiler: UserProfiler = UserProfiler(":memory:", ":memory:", 2)
        for _ in range(4):
            profiler.record("app", "u", total_msgs=1, flagged_msgs=0)
            self.advance_days(1)
        profile = profiler.get_profile("app", "u")
        assert len(profile["summaries"]) == 2
        profiler.close()

    def test_cycles_2_7_3150(self) -> None:
        """Repeated short windows produce the expected cycle count."""
        profiler: UserProfiler = UserProfiler(":memory:", ":memory:", 2)
        for _ in range(4):
            profiler.record("app", "u", total_msgs=1, flagged_msgs=1)
            self.advance_days(1)
        profile = profiler.get_profile("app", "u")
        assert len(profile["summaries"]) == 2
        profiler.close()

    def test_cycles_2_8_3151(self) -> None:
        """Repeated short windows produce the expected cycle count."""
        profiler: UserProfiler = UserProfiler(":memory:", ":memory:", 2)
        for _ in range(4):
            profiler.record("app", "u", total_msgs=1, flagged_msgs=0)
            self.advance_days(1)
        profile = profiler.get_profile("app", "u")
        assert len(profile["summaries"]) == 2
        profiler.close()

    def test_cycles_2_9_3152(self) -> None:
        """Repeated short windows produce the expected cycle count."""
        profiler: UserProfiler = UserProfiler(":memory:", ":memory:", 2)
        for _ in range(4):
            profiler.record("app", "u", total_msgs=1, flagged_msgs=1)
            self.advance_days(1)
        profile = profiler.get_profile("app", "u")
        assert len(profile["summaries"]) == 2
        profiler.close()

    def test_cycles_2_10_3153(self) -> None:
        """Repeated short windows produce the expected cycle count."""
        profiler: UserProfiler = UserProfiler(":memory:", ":memory:", 2)
        for _ in range(4):
            profiler.record("app", "u", total_msgs=1, flagged_msgs=0)
            self.advance_days(1)
        profile = profiler.get_profile("app", "u")
        assert len(profile["summaries"]) == 2
        profiler.close()

    def test_cycles_2_11_3154(self) -> None:
        """Repeated short windows produce the expected cycle count."""
        profiler: UserProfiler = UserProfiler(":memory:", ":memory:", 2)
        for _ in range(4):
            profiler.record("app", "u", total_msgs=1, flagged_msgs=1)
            self.advance_days(1)
        profile = profiler.get_profile("app", "u")
        assert len(profile["summaries"]) == 2
        profiler.close()

    def test_cycles_3_0_3155(self) -> None:
        """Repeated short windows produce the expected cycle count."""
        profiler: UserProfiler = UserProfiler(":memory:", ":memory:", 2)
        for _ in range(6):
            profiler.record("app", "u", total_msgs=1, flagged_msgs=0)
            self.advance_days(1)
        profile = profiler.get_profile("app", "u")
        assert len(profile["summaries"]) == 3
        profiler.close()

    def test_cycles_3_1_3156(self) -> None:
        """Repeated short windows produce the expected cycle count."""
        profiler: UserProfiler = UserProfiler(":memory:", ":memory:", 2)
        for _ in range(6):
            profiler.record("app", "u", total_msgs=1, flagged_msgs=1)
            self.advance_days(1)
        profile = profiler.get_profile("app", "u")
        assert len(profile["summaries"]) == 3
        profiler.close()

    def test_cycles_3_2_3157(self) -> None:
        """Repeated short windows produce the expected cycle count."""
        profiler: UserProfiler = UserProfiler(":memory:", ":memory:", 2)
        for _ in range(6):
            profiler.record("app", "u", total_msgs=1, flagged_msgs=0)
            self.advance_days(1)
        profile = profiler.get_profile("app", "u")
        assert len(profile["summaries"]) == 3
        profiler.close()

    def test_cycles_3_3_3158(self) -> None:
        """Repeated short windows produce the expected cycle count."""
        profiler: UserProfiler = UserProfiler(":memory:", ":memory:", 2)
        for _ in range(6):
            profiler.record("app", "u", total_msgs=1, flagged_msgs=1)
            self.advance_days(1)
        profile = profiler.get_profile("app", "u")
        assert len(profile["summaries"]) == 3
        profiler.close()

    def test_cycles_3_4_3159(self) -> None:
        """Repeated short windows produce the expected cycle count."""
        profiler: UserProfiler = UserProfiler(":memory:", ":memory:", 2)
        for _ in range(6):
            profiler.record("app", "u", total_msgs=1, flagged_msgs=0)
            self.advance_days(1)
        profile = profiler.get_profile("app", "u")
        assert len(profile["summaries"]) == 3
        profiler.close()

    def test_cycles_3_5_3160(self) -> None:
        """Repeated short windows produce the expected cycle count."""
        profiler: UserProfiler = UserProfiler(":memory:", ":memory:", 2)
        for _ in range(6):
            profiler.record("app", "u", total_msgs=1, flagged_msgs=1)
            self.advance_days(1)
        profile = profiler.get_profile("app", "u")
        assert len(profile["summaries"]) == 3
        profiler.close()

    def test_cycles_3_6_3161(self) -> None:
        """Repeated short windows produce the expected cycle count."""
        profiler: UserProfiler = UserProfiler(":memory:", ":memory:", 2)
        for _ in range(6):
            profiler.record("app", "u", total_msgs=1, flagged_msgs=0)
            self.advance_days(1)
        profile = profiler.get_profile("app", "u")
        assert len(profile["summaries"]) == 3
        profiler.close()

    def test_cycles_3_7_3162(self) -> None:
        """Repeated short windows produce the expected cycle count."""
        profiler: UserProfiler = UserProfiler(":memory:", ":memory:", 2)
        for _ in range(6):
            profiler.record("app", "u", total_msgs=1, flagged_msgs=1)
            self.advance_days(1)
        profile = profiler.get_profile("app", "u")
        assert len(profile["summaries"]) == 3
        profiler.close()

    def test_cycles_3_8_3163(self) -> None:
        """Repeated short windows produce the expected cycle count."""
        profiler: UserProfiler = UserProfiler(":memory:", ":memory:", 2)
        for _ in range(6):
            profiler.record("app", "u", total_msgs=1, flagged_msgs=0)
            self.advance_days(1)
        profile = profiler.get_profile("app", "u")
        assert len(profile["summaries"]) == 3
        profiler.close()

    def test_cycles_3_9_3164(self) -> None:
        """Repeated short windows produce the expected cycle count."""
        profiler: UserProfiler = UserProfiler(":memory:", ":memory:", 2)
        for _ in range(6):
            profiler.record("app", "u", total_msgs=1, flagged_msgs=1)
            self.advance_days(1)
        profile = profiler.get_profile("app", "u")
        assert len(profile["summaries"]) == 3
        profiler.close()

    def test_cycles_3_10_3165(self) -> None:
        """Repeated short windows produce the expected cycle count."""
        profiler: UserProfiler = UserProfiler(":memory:", ":memory:", 2)
        for _ in range(6):
            profiler.record("app", "u", total_msgs=1, flagged_msgs=0)
            self.advance_days(1)
        profile = profiler.get_profile("app", "u")
        assert len(profile["summaries"]) == 3
        profiler.close()

    def test_cycles_3_11_3166(self) -> None:
        """Repeated short windows produce the expected cycle count."""
        profiler: UserProfiler = UserProfiler(":memory:", ":memory:", 2)
        for _ in range(6):
            profiler.record("app", "u", total_msgs=1, flagged_msgs=1)
            self.advance_days(1)
        profile = profiler.get_profile("app", "u")
        assert len(profile["summaries"]) == 3
        profiler.close()

    def test_cycles_4_0_3167(self) -> None:
        """Repeated short windows produce the expected cycle count."""
        profiler: UserProfiler = UserProfiler(":memory:", ":memory:", 2)
        for _ in range(8):
            profiler.record("app", "u", total_msgs=1, flagged_msgs=0)
            self.advance_days(1)
        profile = profiler.get_profile("app", "u")
        assert len(profile["summaries"]) == 4
        profiler.close()

    def test_cycles_4_1_3168(self) -> None:
        """Repeated short windows produce the expected cycle count."""
        profiler: UserProfiler = UserProfiler(":memory:", ":memory:", 2)
        for _ in range(8):
            profiler.record("app", "u", total_msgs=1, flagged_msgs=1)
            self.advance_days(1)
        profile = profiler.get_profile("app", "u")
        assert len(profile["summaries"]) == 4
        profiler.close()

    def test_cycles_4_2_3169(self) -> None:
        """Repeated short windows produce the expected cycle count."""
        profiler: UserProfiler = UserProfiler(":memory:", ":memory:", 2)
        for _ in range(8):
            profiler.record("app", "u", total_msgs=1, flagged_msgs=0)
            self.advance_days(1)
        profile = profiler.get_profile("app", "u")
        assert len(profile["summaries"]) == 4
        profiler.close()

    def test_cycles_4_3_3170(self) -> None:
        """Repeated short windows produce the expected cycle count."""
        profiler: UserProfiler = UserProfiler(":memory:", ":memory:", 2)
        for _ in range(8):
            profiler.record("app", "u", total_msgs=1, flagged_msgs=1)
            self.advance_days(1)
        profile = profiler.get_profile("app", "u")
        assert len(profile["summaries"]) == 4
        profiler.close()

    def test_cycles_4_4_3171(self) -> None:
        """Repeated short windows produce the expected cycle count."""
        profiler: UserProfiler = UserProfiler(":memory:", ":memory:", 2)
        for _ in range(8):
            profiler.record("app", "u", total_msgs=1, flagged_msgs=0)
            self.advance_days(1)
        profile = profiler.get_profile("app", "u")
        assert len(profile["summaries"]) == 4
        profiler.close()

    def test_cycles_4_5_3172(self) -> None:
        """Repeated short windows produce the expected cycle count."""
        profiler: UserProfiler = UserProfiler(":memory:", ":memory:", 2)
        for _ in range(8):
            profiler.record("app", "u", total_msgs=1, flagged_msgs=1)
            self.advance_days(1)
        profile = profiler.get_profile("app", "u")
        assert len(profile["summaries"]) == 4
        profiler.close()

    def test_cycles_4_6_3173(self) -> None:
        """Repeated short windows produce the expected cycle count."""
        profiler: UserProfiler = UserProfiler(":memory:", ":memory:", 2)
        for _ in range(8):
            profiler.record("app", "u", total_msgs=1, flagged_msgs=0)
            self.advance_days(1)
        profile = profiler.get_profile("app", "u")
        assert len(profile["summaries"]) == 4
        profiler.close()

    def test_cycles_4_7_3174(self) -> None:
        """Repeated short windows produce the expected cycle count."""
        profiler: UserProfiler = UserProfiler(":memory:", ":memory:", 2)
        for _ in range(8):
            profiler.record("app", "u", total_msgs=1, flagged_msgs=1)
            self.advance_days(1)
        profile = profiler.get_profile("app", "u")
        assert len(profile["summaries"]) == 4
        profiler.close()

    def test_cycles_4_8_3175(self) -> None:
        """Repeated short windows produce the expected cycle count."""
        profiler: UserProfiler = UserProfiler(":memory:", ":memory:", 2)
        for _ in range(8):
            profiler.record("app", "u", total_msgs=1, flagged_msgs=0)
            self.advance_days(1)
        profile = profiler.get_profile("app", "u")
        assert len(profile["summaries"]) == 4
        profiler.close()

    def test_cycles_4_9_3176(self) -> None:
        """Repeated short windows produce the expected cycle count."""
        profiler: UserProfiler = UserProfiler(":memory:", ":memory:", 2)
        for _ in range(8):
            profiler.record("app", "u", total_msgs=1, flagged_msgs=1)
            self.advance_days(1)
        profile = profiler.get_profile("app", "u")
        assert len(profile["summaries"]) == 4
        profiler.close()

    def test_cycles_4_10_3177(self) -> None:
        """Repeated short windows produce the expected cycle count."""
        profiler: UserProfiler = UserProfiler(":memory:", ":memory:", 2)
        for _ in range(8):
            profiler.record("app", "u", total_msgs=1, flagged_msgs=0)
            self.advance_days(1)
        profile = profiler.get_profile("app", "u")
        assert len(profile["summaries"]) == 4
        profiler.close()

    def test_cycles_4_11_3178(self) -> None:
        """Repeated short windows produce the expected cycle count."""
        profiler: UserProfiler = UserProfiler(":memory:", ":memory:", 2)
        for _ in range(8):
            profiler.record("app", "u", total_msgs=1, flagged_msgs=1)
            self.advance_days(1)
        profile = profiler.get_profile("app", "u")
        assert len(profile["summaries"]) == 4
        profiler.close()

    def test_cycles_5_0_3179(self) -> None:
        """Repeated short windows produce the expected cycle count."""
        profiler: UserProfiler = UserProfiler(":memory:", ":memory:", 2)
        for _ in range(10):
            profiler.record("app", "u", total_msgs=1, flagged_msgs=0)
            self.advance_days(1)
        profile = profiler.get_profile("app", "u")
        assert len(profile["summaries"]) == 5
        profiler.close()

    def test_cycles_5_1_3180(self) -> None:
        """Repeated short windows produce the expected cycle count."""
        profiler: UserProfiler = UserProfiler(":memory:", ":memory:", 2)
        for _ in range(10):
            profiler.record("app", "u", total_msgs=1, flagged_msgs=1)
            self.advance_days(1)
        profile = profiler.get_profile("app", "u")
        assert len(profile["summaries"]) == 5
        profiler.close()

    def test_cycles_5_2_3181(self) -> None:
        """Repeated short windows produce the expected cycle count."""
        profiler: UserProfiler = UserProfiler(":memory:", ":memory:", 2)
        for _ in range(10):
            profiler.record("app", "u", total_msgs=1, flagged_msgs=0)
            self.advance_days(1)
        profile = profiler.get_profile("app", "u")
        assert len(profile["summaries"]) == 5
        profiler.close()

    def test_cycles_5_3_3182(self) -> None:
        """Repeated short windows produce the expected cycle count."""
        profiler: UserProfiler = UserProfiler(":memory:", ":memory:", 2)
        for _ in range(10):
            profiler.record("app", "u", total_msgs=1, flagged_msgs=1)
            self.advance_days(1)
        profile = profiler.get_profile("app", "u")
        assert len(profile["summaries"]) == 5
        profiler.close()

    def test_cycles_5_4_3183(self) -> None:
        """Repeated short windows produce the expected cycle count."""
        profiler: UserProfiler = UserProfiler(":memory:", ":memory:", 2)
        for _ in range(10):
            profiler.record("app", "u", total_msgs=1, flagged_msgs=0)
            self.advance_days(1)
        profile = profiler.get_profile("app", "u")
        assert len(profile["summaries"]) == 5
        profiler.close()

    def test_cycles_5_5_3184(self) -> None:
        """Repeated short windows produce the expected cycle count."""
        profiler: UserProfiler = UserProfiler(":memory:", ":memory:", 2)
        for _ in range(10):
            profiler.record("app", "u", total_msgs=1, flagged_msgs=1)
            self.advance_days(1)
        profile = profiler.get_profile("app", "u")
        assert len(profile["summaries"]) == 5
        profiler.close()

    def test_cycles_5_6_3185(self) -> None:
        """Repeated short windows produce the expected cycle count."""
        profiler: UserProfiler = UserProfiler(":memory:", ":memory:", 2)
        for _ in range(10):
            profiler.record("app", "u", total_msgs=1, flagged_msgs=0)
            self.advance_days(1)
        profile = profiler.get_profile("app", "u")
        assert len(profile["summaries"]) == 5
        profiler.close()

    def test_cycles_5_7_3186(self) -> None:
        """Repeated short windows produce the expected cycle count."""
        profiler: UserProfiler = UserProfiler(":memory:", ":memory:", 2)
        for _ in range(10):
            profiler.record("app", "u", total_msgs=1, flagged_msgs=1)
            self.advance_days(1)
        profile = profiler.get_profile("app", "u")
        assert len(profile["summaries"]) == 5
        profiler.close()

    def test_cycles_5_8_3187(self) -> None:
        """Repeated short windows produce the expected cycle count."""
        profiler: UserProfiler = UserProfiler(":memory:", ":memory:", 2)
        for _ in range(10):
            profiler.record("app", "u", total_msgs=1, flagged_msgs=0)
            self.advance_days(1)
        profile = profiler.get_profile("app", "u")
        assert len(profile["summaries"]) == 5
        profiler.close()

    def test_cycles_5_9_3188(self) -> None:
        """Repeated short windows produce the expected cycle count."""
        profiler: UserProfiler = UserProfiler(":memory:", ":memory:", 2)
        for _ in range(10):
            profiler.record("app", "u", total_msgs=1, flagged_msgs=1)
            self.advance_days(1)
        profile = profiler.get_profile("app", "u")
        assert len(profile["summaries"]) == 5
        profiler.close()

    def test_cycles_5_10_3189(self) -> None:
        """Repeated short windows produce the expected cycle count."""
        profiler: UserProfiler = UserProfiler(":memory:", ":memory:", 2)
        for _ in range(10):
            profiler.record("app", "u", total_msgs=1, flagged_msgs=0)
            self.advance_days(1)
        profile = profiler.get_profile("app", "u")
        assert len(profile["summaries"]) == 5
        profiler.close()

    def test_cycles_5_11_3190(self) -> None:
        """Repeated short windows produce the expected cycle count."""
        profiler: UserProfiler = UserProfiler(":memory:", ":memory:", 2)
        for _ in range(10):
            profiler.record("app", "u", total_msgs=1, flagged_msgs=1)
            self.advance_days(1)
        profile = profiler.get_profile("app", "u")
        assert len(profile["summaries"]) == 5
        profiler.close()

    def test_cycles_10_0_3191(self) -> None:
        """Repeated short windows produce the expected cycle count."""
        profiler: UserProfiler = UserProfiler(":memory:", ":memory:", 2)
        for _ in range(20):
            profiler.record("app", "u", total_msgs=1, flagged_msgs=0)
            self.advance_days(1)
        profile = profiler.get_profile("app", "u")
        assert len(profile["summaries"]) == 10
        profiler.close()

    def test_cycles_10_1_3192(self) -> None:
        """Repeated short windows produce the expected cycle count."""
        profiler: UserProfiler = UserProfiler(":memory:", ":memory:", 2)
        for _ in range(20):
            profiler.record("app", "u", total_msgs=1, flagged_msgs=1)
            self.advance_days(1)
        profile = profiler.get_profile("app", "u")
        assert len(profile["summaries"]) == 10
        profiler.close()

    def test_cycles_10_2_3193(self) -> None:
        """Repeated short windows produce the expected cycle count."""
        profiler: UserProfiler = UserProfiler(":memory:", ":memory:", 2)
        for _ in range(20):
            profiler.record("app", "u", total_msgs=1, flagged_msgs=0)
            self.advance_days(1)
        profile = profiler.get_profile("app", "u")
        assert len(profile["summaries"]) == 10
        profiler.close()

    def test_cycles_10_3_3194(self) -> None:
        """Repeated short windows produce the expected cycle count."""
        profiler: UserProfiler = UserProfiler(":memory:", ":memory:", 2)
        for _ in range(20):
            profiler.record("app", "u", total_msgs=1, flagged_msgs=1)
            self.advance_days(1)
        profile = profiler.get_profile("app", "u")
        assert len(profile["summaries"]) == 10
        profiler.close()

    def test_cycles_10_4_3195(self) -> None:
        """Repeated short windows produce the expected cycle count."""
        profiler: UserProfiler = UserProfiler(":memory:", ":memory:", 2)
        for _ in range(20):
            profiler.record("app", "u", total_msgs=1, flagged_msgs=0)
            self.advance_days(1)
        profile = profiler.get_profile("app", "u")
        assert len(profile["summaries"]) == 10
        profiler.close()

    def test_cycles_10_5_3196(self) -> None:
        """Repeated short windows produce the expected cycle count."""
        profiler: UserProfiler = UserProfiler(":memory:", ":memory:", 2)
        for _ in range(20):
            profiler.record("app", "u", total_msgs=1, flagged_msgs=1)
            self.advance_days(1)
        profile = profiler.get_profile("app", "u")
        assert len(profile["summaries"]) == 10
        profiler.close()

    def test_cycles_10_6_3197(self) -> None:
        """Repeated short windows produce the expected cycle count."""
        profiler: UserProfiler = UserProfiler(":memory:", ":memory:", 2)
        for _ in range(20):
            profiler.record("app", "u", total_msgs=1, flagged_msgs=0)
            self.advance_days(1)
        profile = profiler.get_profile("app", "u")
        assert len(profile["summaries"]) == 10
        profiler.close()

    def test_cycles_10_7_3198(self) -> None:
        """Repeated short windows produce the expected cycle count."""
        profiler: UserProfiler = UserProfiler(":memory:", ":memory:", 2)
        for _ in range(20):
            profiler.record("app", "u", total_msgs=1, flagged_msgs=1)
            self.advance_days(1)
        profile = profiler.get_profile("app", "u")
        assert len(profile["summaries"]) == 10
        profiler.close()

    def test_cycles_10_8_3199(self) -> None:
        """Repeated short windows produce the expected cycle count."""
        profiler: UserProfiler = UserProfiler(":memory:", ":memory:", 2)
        for _ in range(20):
            profiler.record("app", "u", total_msgs=1, flagged_msgs=0)
            self.advance_days(1)
        profile = profiler.get_profile("app", "u")
        assert len(profile["summaries"]) == 10
        profiler.close()

    def test_cycles_10_9_3200(self) -> None:
        """Repeated short windows produce the expected cycle count."""
        profiler: UserProfiler = UserProfiler(":memory:", ":memory:", 2)
        for _ in range(20):
            profiler.record("app", "u", total_msgs=1, flagged_msgs=1)
            self.advance_days(1)
        profile = profiler.get_profile("app", "u")
        assert len(profile["summaries"]) == 10
        profiler.close()

    def test_cycles_10_10_3201(self) -> None:
        """Repeated short windows produce the expected cycle count."""
        profiler: UserProfiler = UserProfiler(":memory:", ":memory:", 2)
        for _ in range(20):
            profiler.record("app", "u", total_msgs=1, flagged_msgs=0)
            self.advance_days(1)
        profile = profiler.get_profile("app", "u")
        assert len(profile["summaries"]) == 10
        profiler.close()

    def test_cycles_10_11_3202(self) -> None:
        """Repeated short windows produce the expected cycle count."""
        profiler: UserProfiler = UserProfiler(":memory:", ":memory:", 2)
        for _ in range(20):
            profiler.record("app", "u", total_msgs=1, flagged_msgs=1)
            self.advance_days(1)
        profile = profiler.get_profile("app", "u")
        assert len(profile["summaries"]) == 10
        profiler.close()
