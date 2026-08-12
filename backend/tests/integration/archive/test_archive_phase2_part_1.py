"""Phase 2 archive cycle tests (generated).

Volume and percentage matrices, multi-cycle chains, multi-user/app
archives and boundary edges under the frozen clock."""

# multilingual fixtures use non-ASCII on purpose
from __future__ import annotations

from app.profiling.user_profiler import UserProfiler
from tests.base_test import BaseTest


class TestSingleCycle(BaseTest):
    """SingleCycle scenarios."""

    def test_single_cycle_v2_f0_b0_3303(self) -> None:
        """A full window archives totals that match the configured rates."""
        profiler: UserProfiler = UserProfiler(":memory:", ":memory:", 91)
        for _ in range(91):
            profiler.record(
                "app",
                "u",
                total_msgs=2,
                flagged_msgs=0,
                blocked_msgs=0,
            )
            self.advance_days(1)
        profile = profiler.get_profile("app", "u")
        assert len(profile["summaries"]) == 1
        assert profiler.get_ratio("app", "u") == 0.0
        if profile["summaries"]:
            summary = profile["summaries"][0]
            assert summary["total_msgs"] == 182
        profiler.close()

    def test_single_cycle_v2_f5_b0_3304(self) -> None:
        """A full window archives totals that match the configured rates."""
        profiler: UserProfiler = UserProfiler(":memory:", ":memory:", 91)
        for _ in range(91):
            profiler.record(
                "app",
                "u",
                total_msgs=2,
                flagged_msgs=0,
                blocked_msgs=0,
            )
            self.advance_days(1)
        profile = profiler.get_profile("app", "u")
        assert len(profile["summaries"]) == 1
        assert profiler.get_ratio("app", "u") == 0.0
        if profile["summaries"]:
            summary = profile["summaries"][0]
            assert summary["total_msgs"] == 182
        profiler.close()

    def test_single_cycle_v2_f10_b5_3305(self) -> None:
        """A full window archives totals that match the configured rates."""
        profiler: UserProfiler = UserProfiler(":memory:", ":memory:", 91)
        for _ in range(91):
            profiler.record(
                "app",
                "u",
                total_msgs=2,
                flagged_msgs=0,
                blocked_msgs=0,
            )
            self.advance_days(1)
        profile = profiler.get_profile("app", "u")
        assert len(profile["summaries"]) == 1
        assert profiler.get_ratio("app", "u") == 0.0
        if profile["summaries"]:
            summary = profile["summaries"][0]
            assert summary["total_msgs"] == 182
        profiler.close()

    def test_single_cycle_v2_f15_b10_3306(self) -> None:
        """A full window archives totals that match the configured rates."""
        profiler: UserProfiler = UserProfiler(":memory:", ":memory:", 91)
        for _ in range(91):
            profiler.record(
                "app",
                "u",
                total_msgs=2,
                flagged_msgs=0,
                blocked_msgs=0,
            )
            self.advance_days(1)
        profile = profiler.get_profile("app", "u")
        assert len(profile["summaries"]) == 1
        assert profiler.get_ratio("app", "u") == 0.0
        if profile["summaries"]:
            summary = profile["summaries"][0]
            assert summary["total_msgs"] == 182
        profiler.close()

    def test_single_cycle_v2_f20_b20_3307(self) -> None:
        """A full window archives totals that match the configured rates."""
        profiler: UserProfiler = UserProfiler(":memory:", ":memory:", 91)
        for _ in range(91):
            profiler.record(
                "app",
                "u",
                total_msgs=2,
                flagged_msgs=0,
                blocked_msgs=0,
            )
            self.advance_days(1)
        profile = profiler.get_profile("app", "u")
        assert len(profile["summaries"]) == 1
        assert profiler.get_ratio("app", "u") == 0.0
        if profile["summaries"]:
            summary = profile["summaries"][0]
            assert summary["total_msgs"] == 182
        profiler.close()

    def test_single_cycle_v2_f25_b0_3308(self) -> None:
        """A full window archives totals that match the configured rates."""
        profiler: UserProfiler = UserProfiler(":memory:", ":memory:", 91)
        for _ in range(91):
            profiler.record(
                "app",
                "u",
                total_msgs=2,
                flagged_msgs=0,
                blocked_msgs=0,
            )
            self.advance_days(1)
        profile = profiler.get_profile("app", "u")
        assert len(profile["summaries"]) == 1
        assert profiler.get_ratio("app", "u") == 0.0
        if profile["summaries"]:
            summary = profile["summaries"][0]
            assert summary["total_msgs"] == 182
        profiler.close()

    def test_single_cycle_v2_f30_b15_3309(self) -> None:
        """A full window archives totals that match the configured rates."""
        profiler: UserProfiler = UserProfiler(":memory:", ":memory:", 91)
        for _ in range(91):
            profiler.record(
                "app",
                "u",
                total_msgs=2,
                flagged_msgs=1,
                blocked_msgs=0,
            )
            self.advance_days(1)
        profile = profiler.get_profile("app", "u")
        assert len(profile["summaries"]) == 1
        assert profiler.get_ratio("app", "u") == 0.5
        if profile["summaries"]:
            summary = profile["summaries"][0]
            assert summary["total_msgs"] == 182
        profiler.close()

    def test_single_cycle_v2_f35_b5_3310(self) -> None:
        """A full window archives totals that match the configured rates."""
        profiler: UserProfiler = UserProfiler(":memory:", ":memory:", 91)
        for _ in range(91):
            profiler.record(
                "app",
                "u",
                total_msgs=2,
                flagged_msgs=1,
                blocked_msgs=0,
            )
            self.advance_days(1)
        profile = profiler.get_profile("app", "u")
        assert len(profile["summaries"]) == 1
        assert profiler.get_ratio("app", "u") == 0.5
        if profile["summaries"]:
            summary = profile["summaries"][0]
            assert summary["total_msgs"] == 182
        profiler.close()

    def test_single_cycle_v2_f40_b40_3311(self) -> None:
        """A full window archives totals that match the configured rates."""
        profiler: UserProfiler = UserProfiler(":memory:", ":memory:", 91)
        for _ in range(91):
            profiler.record(
                "app",
                "u",
                total_msgs=2,
                flagged_msgs=1,
                blocked_msgs=1,
            )
            self.advance_days(1)
        profile = profiler.get_profile("app", "u")
        assert len(profile["summaries"]) == 1
        assert profiler.get_ratio("app", "u") == 1.0
        if profile["summaries"]:
            summary = profile["summaries"][0]
            assert summary["total_msgs"] == 182
        profiler.close()

    def test_single_cycle_v2_f45_b0_3312(self) -> None:
        """A full window archives totals that match the configured rates."""
        profiler: UserProfiler = UserProfiler(":memory:", ":memory:", 91)
        for _ in range(91):
            profiler.record(
                "app",
                "u",
                total_msgs=2,
                flagged_msgs=1,
                blocked_msgs=0,
            )
            self.advance_days(1)
        profile = profiler.get_profile("app", "u")
        assert len(profile["summaries"]) == 1
        assert profiler.get_ratio("app", "u") == 0.5
        if profile["summaries"]:
            summary = profile["summaries"][0]
            assert summary["total_msgs"] == 182
        profiler.close()

    def test_single_cycle_v2_f50_b25_3313(self) -> None:
        """A full window archives totals that match the configured rates."""
        profiler: UserProfiler = UserProfiler(":memory:", ":memory:", 91)
        for _ in range(91):
            profiler.record(
                "app",
                "u",
                total_msgs=2,
                flagged_msgs=1,
                blocked_msgs=0,
            )
            self.advance_days(1)
        profile = profiler.get_profile("app", "u")
        assert len(profile["summaries"]) == 1
        assert profiler.get_ratio("app", "u") == 0.5
        if profile["summaries"]:
            summary = profile["summaries"][0]
            assert summary["total_msgs"] == 182
        profiler.close()

    def test_single_cycle_v2_f55_b10_3314(self) -> None:
        """A full window archives totals that match the configured rates."""
        profiler: UserProfiler = UserProfiler(":memory:", ":memory:", 91)
        for _ in range(91):
            profiler.record(
                "app",
                "u",
                total_msgs=2,
                flagged_msgs=1,
                blocked_msgs=0,
            )
            self.advance_days(1)
        profile = profiler.get_profile("app", "u")
        assert len(profile["summaries"]) == 1
        assert profiler.get_ratio("app", "u") == 0.5
        if profile["summaries"]:
            summary = profile["summaries"][0]
            assert summary["total_msgs"] == 182
        profiler.close()

    def test_single_cycle_v2_f60_b30_3315(self) -> None:
        """A full window archives totals that match the configured rates."""
        profiler: UserProfiler = UserProfiler(":memory:", ":memory:", 91)
        for _ in range(91):
            profiler.record(
                "app",
                "u",
                total_msgs=2,
                flagged_msgs=1,
                blocked_msgs=1,
            )
            self.advance_days(1)
        profile = profiler.get_profile("app", "u")
        assert len(profile["summaries"]) == 1
        assert profiler.get_ratio("app", "u") == 1.0
        if profile["summaries"]:
            summary = profile["summaries"][0]
            assert summary["total_msgs"] == 182
        profiler.close()

    def test_single_cycle_v2_f65_b0_3316(self) -> None:
        """A full window archives totals that match the configured rates."""
        profiler: UserProfiler = UserProfiler(":memory:", ":memory:", 91)
        for _ in range(91):
            profiler.record(
                "app",
                "u",
                total_msgs=2,
                flagged_msgs=1,
                blocked_msgs=0,
            )
            self.advance_days(1)
        profile = profiler.get_profile("app", "u")
        assert len(profile["summaries"]) == 1
        assert profiler.get_ratio("app", "u") == 0.5
        if profile["summaries"]:
            summary = profile["summaries"][0]
            assert summary["total_msgs"] == 182
        profiler.close()

    def test_single_cycle_v2_f70_b20_3317(self) -> None:
        """A full window archives totals that match the configured rates."""
        profiler: UserProfiler = UserProfiler(":memory:", ":memory:", 91)
        for _ in range(91):
            profiler.record(
                "app",
                "u",
                total_msgs=2,
                flagged_msgs=1,
                blocked_msgs=0,
            )
            self.advance_days(1)
        profile = profiler.get_profile("app", "u")
        assert len(profile["summaries"]) == 1
        assert profiler.get_ratio("app", "u") == 0.5
        if profile["summaries"]:
            summary = profile["summaries"][0]
            assert summary["total_msgs"] == 182
        profiler.close()

    def test_single_cycle_v2_f75_b35_3318(self) -> None:
        """A full window archives totals that match the configured rates."""
        profiler: UserProfiler = UserProfiler(":memory:", ":memory:", 91)
        for _ in range(91):
            profiler.record(
                "app",
                "u",
                total_msgs=2,
                flagged_msgs=2,
                blocked_msgs=1,
            )
            self.advance_days(1)
        profile = profiler.get_profile("app", "u")
        assert len(profile["summaries"]) == 1
        assert profiler.get_ratio("app", "u") == 1.5
        if profile["summaries"]:
            summary = profile["summaries"][0]
            assert summary["total_msgs"] == 182
        profiler.close()

    def test_single_cycle_v2_f80_b0_3319(self) -> None:
        """A full window archives totals that match the configured rates."""
        profiler: UserProfiler = UserProfiler(":memory:", ":memory:", 91)
        for _ in range(91):
            profiler.record(
                "app",
                "u",
                total_msgs=2,
                flagged_msgs=2,
                blocked_msgs=0,
            )
            self.advance_days(1)
        profile = profiler.get_profile("app", "u")
        assert len(profile["summaries"]) == 1
        assert profiler.get_ratio("app", "u") == 1.0
        if profile["summaries"]:
            summary = profile["summaries"][0]
            assert summary["total_msgs"] == 182
        profiler.close()

    def test_single_cycle_v2_f85_b40_3320(self) -> None:
        """A full window archives totals that match the configured rates."""
        profiler: UserProfiler = UserProfiler(":memory:", ":memory:", 91)
        for _ in range(91):
            profiler.record(
                "app",
                "u",
                total_msgs=2,
                flagged_msgs=2,
                blocked_msgs=1,
            )
            self.advance_days(1)
        profile = profiler.get_profile("app", "u")
        assert len(profile["summaries"]) == 1
        assert profiler.get_ratio("app", "u") == 1.5
        if profile["summaries"]:
            summary = profile["summaries"][0]
            assert summary["total_msgs"] == 182
        profiler.close()

    def test_single_cycle_v2_f90_b5_3321(self) -> None:
        """A full window archives totals that match the configured rates."""
        profiler: UserProfiler = UserProfiler(":memory:", ":memory:", 91)
        for _ in range(91):
            profiler.record(
                "app",
                "u",
                total_msgs=2,
                flagged_msgs=2,
                blocked_msgs=0,
            )
            self.advance_days(1)
        profile = profiler.get_profile("app", "u")
        assert len(profile["summaries"]) == 1
        assert profiler.get_ratio("app", "u") == 1.0
        if profile["summaries"]:
            summary = profile["summaries"][0]
            assert summary["total_msgs"] == 182
        profiler.close()

    def test_single_cycle_v2_f95_b10_3322(self) -> None:
        """A full window archives totals that match the configured rates."""
        profiler: UserProfiler = UserProfiler(":memory:", ":memory:", 91)
        for _ in range(91):
            profiler.record(
                "app",
                "u",
                total_msgs=2,
                flagged_msgs=2,
                blocked_msgs=0,
            )
            self.advance_days(1)
        profile = profiler.get_profile("app", "u")
        assert len(profile["summaries"]) == 1
        assert profiler.get_ratio("app", "u") == 1.0
        if profile["summaries"]:
            summary = profile["summaries"][0]
            assert summary["total_msgs"] == 182
        profiler.close()

    def test_single_cycle_v2_f100_b0_3323(self) -> None:
        """A full window archives totals that match the configured rates."""
        profiler: UserProfiler = UserProfiler(":memory:", ":memory:", 91)
        for _ in range(91):
            profiler.record(
                "app",
                "u",
                total_msgs=2,
                flagged_msgs=2,
                blocked_msgs=0,
            )
            self.advance_days(1)
        profile = profiler.get_profile("app", "u")
        assert len(profile["summaries"]) == 1
        assert profiler.get_ratio("app", "u") == 1.0
        if profile["summaries"]:
            summary = profile["summaries"][0]
            assert summary["total_msgs"] == 182
        profiler.close()

    def test_single_cycle_v5_f0_b0_3324(self) -> None:
        """A full window archives totals that match the configured rates."""
        profiler: UserProfiler = UserProfiler(":memory:", ":memory:", 91)
        for _ in range(91):
            profiler.record(
                "app",
                "u",
                total_msgs=5,
                flagged_msgs=0,
                blocked_msgs=0,
            )
            self.advance_days(1)
        profile = profiler.get_profile("app", "u")
        assert len(profile["summaries"]) == 1
        assert profiler.get_ratio("app", "u") == 0.0
        if profile["summaries"]:
            summary = profile["summaries"][0]
            assert summary["total_msgs"] == 455
        profiler.close()

    def test_single_cycle_v5_f5_b0_3325(self) -> None:
        """A full window archives totals that match the configured rates."""
        profiler: UserProfiler = UserProfiler(":memory:", ":memory:", 91)
        for _ in range(91):
            profiler.record(
                "app",
                "u",
                total_msgs=5,
                flagged_msgs=0,
                blocked_msgs=0,
            )
            self.advance_days(1)
        profile = profiler.get_profile("app", "u")
        assert len(profile["summaries"]) == 1
        assert profiler.get_ratio("app", "u") == 0.0
        if profile["summaries"]:
            summary = profile["summaries"][0]
            assert summary["total_msgs"] == 455
        profiler.close()

    def test_single_cycle_v5_f10_b5_3326(self) -> None:
        """A full window archives totals that match the configured rates."""
        profiler: UserProfiler = UserProfiler(":memory:", ":memory:", 91)
        for _ in range(91):
            profiler.record(
                "app",
                "u",
                total_msgs=5,
                flagged_msgs=0,
                blocked_msgs=0,
            )
            self.advance_days(1)
        profile = profiler.get_profile("app", "u")
        assert len(profile["summaries"]) == 1
        assert profiler.get_ratio("app", "u") == 0.0
        if profile["summaries"]:
            summary = profile["summaries"][0]
            assert summary["total_msgs"] == 455
        profiler.close()

    def test_single_cycle_v5_f15_b10_3327(self) -> None:
        """A full window archives totals that match the configured rates."""
        profiler: UserProfiler = UserProfiler(":memory:", ":memory:", 91)
        for _ in range(91):
            profiler.record(
                "app",
                "u",
                total_msgs=5,
                flagged_msgs=1,
                blocked_msgs=0,
            )
            self.advance_days(1)
        profile = profiler.get_profile("app", "u")
        assert len(profile["summaries"]) == 1
        assert profiler.get_ratio("app", "u") == 0.2
        if profile["summaries"]:
            summary = profile["summaries"][0]
            assert summary["total_msgs"] == 455
        profiler.close()

    def test_single_cycle_v5_f20_b20_3328(self) -> None:
        """A full window archives totals that match the configured rates."""
        profiler: UserProfiler = UserProfiler(":memory:", ":memory:", 91)
        for _ in range(91):
            profiler.record(
                "app",
                "u",
                total_msgs=5,
                flagged_msgs=1,
                blocked_msgs=1,
            )
            self.advance_days(1)
        profile = profiler.get_profile("app", "u")
        assert len(profile["summaries"]) == 1
        assert profiler.get_ratio("app", "u") == 0.4
        if profile["summaries"]:
            summary = profile["summaries"][0]
            assert summary["total_msgs"] == 455
        profiler.close()

    def test_single_cycle_v5_f25_b0_3329(self) -> None:
        """A full window archives totals that match the configured rates."""
        profiler: UserProfiler = UserProfiler(":memory:", ":memory:", 91)
        for _ in range(91):
            profiler.record(
                "app",
                "u",
                total_msgs=5,
                flagged_msgs=1,
                blocked_msgs=0,
            )
            self.advance_days(1)
        profile = profiler.get_profile("app", "u")
        assert len(profile["summaries"]) == 1
        assert profiler.get_ratio("app", "u") == 0.2
        if profile["summaries"]:
            summary = profile["summaries"][0]
            assert summary["total_msgs"] == 455
        profiler.close()

    def test_single_cycle_v5_f30_b15_3330(self) -> None:
        """A full window archives totals that match the configured rates."""
        profiler: UserProfiler = UserProfiler(":memory:", ":memory:", 91)
        for _ in range(91):
            profiler.record(
                "app",
                "u",
                total_msgs=5,
                flagged_msgs=2,
                blocked_msgs=1,
            )
            self.advance_days(1)
        profile = profiler.get_profile("app", "u")
        assert len(profile["summaries"]) == 1
        assert profiler.get_ratio("app", "u") == 0.6
        if profile["summaries"]:
            summary = profile["summaries"][0]
            assert summary["total_msgs"] == 455
        profiler.close()

    def test_single_cycle_v5_f35_b5_3331(self) -> None:
        """A full window archives totals that match the configured rates."""
        profiler: UserProfiler = UserProfiler(":memory:", ":memory:", 91)
        for _ in range(91):
            profiler.record(
                "app",
                "u",
                total_msgs=5,
                flagged_msgs=2,
                blocked_msgs=0,
            )
            self.advance_days(1)
        profile = profiler.get_profile("app", "u")
        assert len(profile["summaries"]) == 1
        assert profiler.get_ratio("app", "u") == 0.4
        if profile["summaries"]:
            summary = profile["summaries"][0]
            assert summary["total_msgs"] == 455
        profiler.close()

    def test_single_cycle_v5_f40_b40_3332(self) -> None:
        """A full window archives totals that match the configured rates."""
        profiler: UserProfiler = UserProfiler(":memory:", ":memory:", 91)
        for _ in range(91):
            profiler.record(
                "app",
                "u",
                total_msgs=5,
                flagged_msgs=2,
                blocked_msgs=2,
            )
            self.advance_days(1)
        profile = profiler.get_profile("app", "u")
        assert len(profile["summaries"]) == 1
        assert profiler.get_ratio("app", "u") == 0.8
        if profile["summaries"]:
            summary = profile["summaries"][0]
            assert summary["total_msgs"] == 455
        profiler.close()

    def test_single_cycle_v5_f45_b0_3333(self) -> None:
        """A full window archives totals that match the configured rates."""
        profiler: UserProfiler = UserProfiler(":memory:", ":memory:", 91)
        for _ in range(91):
            profiler.record(
                "app",
                "u",
                total_msgs=5,
                flagged_msgs=2,
                blocked_msgs=0,
            )
            self.advance_days(1)
        profile = profiler.get_profile("app", "u")
        assert len(profile["summaries"]) == 1
        assert profiler.get_ratio("app", "u") == 0.4
        if profile["summaries"]:
            summary = profile["summaries"][0]
            assert summary["total_msgs"] == 455
        profiler.close()

    def test_single_cycle_v5_f50_b25_3334(self) -> None:
        """A full window archives totals that match the configured rates."""
        profiler: UserProfiler = UserProfiler(":memory:", ":memory:", 91)
        for _ in range(91):
            profiler.record(
                "app",
                "u",
                total_msgs=5,
                flagged_msgs=2,
                blocked_msgs=1,
            )
            self.advance_days(1)
        profile = profiler.get_profile("app", "u")
        assert len(profile["summaries"]) == 1
        assert profiler.get_ratio("app", "u") == 0.6
        if profile["summaries"]:
            summary = profile["summaries"][0]
            assert summary["total_msgs"] == 455
        profiler.close()

    def test_single_cycle_v5_f55_b10_3335(self) -> None:
        """A full window archives totals that match the configured rates."""
        profiler: UserProfiler = UserProfiler(":memory:", ":memory:", 91)
        for _ in range(91):
            profiler.record(
                "app",
                "u",
                total_msgs=5,
                flagged_msgs=3,
                blocked_msgs=0,
            )
            self.advance_days(1)
        profile = profiler.get_profile("app", "u")
        assert len(profile["summaries"]) == 1
        assert profiler.get_ratio("app", "u") == 0.6
        if profile["summaries"]:
            summary = profile["summaries"][0]
            assert summary["total_msgs"] == 455
        profiler.close()

    def test_single_cycle_v5_f60_b30_3336(self) -> None:
        """A full window archives totals that match the configured rates."""
        profiler: UserProfiler = UserProfiler(":memory:", ":memory:", 91)
        for _ in range(91):
            profiler.record(
                "app",
                "u",
                total_msgs=5,
                flagged_msgs=3,
                blocked_msgs=2,
            )
            self.advance_days(1)
        profile = profiler.get_profile("app", "u")
        assert len(profile["summaries"]) == 1
        assert profiler.get_ratio("app", "u") == 1.0
        if profile["summaries"]:
            summary = profile["summaries"][0]
            assert summary["total_msgs"] == 455
        profiler.close()

    def test_single_cycle_v5_f65_b0_3337(self) -> None:
        """A full window archives totals that match the configured rates."""
        profiler: UserProfiler = UserProfiler(":memory:", ":memory:", 91)
        for _ in range(91):
            profiler.record(
                "app",
                "u",
                total_msgs=5,
                flagged_msgs=3,
                blocked_msgs=0,
            )
            self.advance_days(1)
        profile = profiler.get_profile("app", "u")
        assert len(profile["summaries"]) == 1
        assert profiler.get_ratio("app", "u") == 0.6
        if profile["summaries"]:
            summary = profile["summaries"][0]
            assert summary["total_msgs"] == 455
        profiler.close()

    def test_single_cycle_v5_f70_b20_3338(self) -> None:
        """A full window archives totals that match the configured rates."""
        profiler: UserProfiler = UserProfiler(":memory:", ":memory:", 91)
        for _ in range(91):
            profiler.record(
                "app",
                "u",
                total_msgs=5,
                flagged_msgs=4,
                blocked_msgs=1,
            )
            self.advance_days(1)
        profile = profiler.get_profile("app", "u")
        assert len(profile["summaries"]) == 1
        assert profiler.get_ratio("app", "u") == 1.0
        if profile["summaries"]:
            summary = profile["summaries"][0]
            assert summary["total_msgs"] == 455
        profiler.close()

    def test_single_cycle_v5_f75_b35_3339(self) -> None:
        """A full window archives totals that match the configured rates."""
        profiler: UserProfiler = UserProfiler(":memory:", ":memory:", 91)
        for _ in range(91):
            profiler.record(
                "app",
                "u",
                total_msgs=5,
                flagged_msgs=4,
                blocked_msgs=2,
            )
            self.advance_days(1)
        profile = profiler.get_profile("app", "u")
        assert len(profile["summaries"]) == 1
        assert profiler.get_ratio("app", "u") == 1.2
        if profile["summaries"]:
            summary = profile["summaries"][0]
            assert summary["total_msgs"] == 455
        profiler.close()

    def test_single_cycle_v5_f80_b0_3340(self) -> None:
        """A full window archives totals that match the configured rates."""
        profiler: UserProfiler = UserProfiler(":memory:", ":memory:", 91)
        for _ in range(91):
            profiler.record(
                "app",
                "u",
                total_msgs=5,
                flagged_msgs=4,
                blocked_msgs=0,
            )
            self.advance_days(1)
        profile = profiler.get_profile("app", "u")
        assert len(profile["summaries"]) == 1
        assert profiler.get_ratio("app", "u") == 0.8
        if profile["summaries"]:
            summary = profile["summaries"][0]
            assert summary["total_msgs"] == 455
        profiler.close()

    def test_single_cycle_v5_f85_b40_3341(self) -> None:
        """A full window archives totals that match the configured rates."""
        profiler: UserProfiler = UserProfiler(":memory:", ":memory:", 91)
        for _ in range(91):
            profiler.record(
                "app",
                "u",
                total_msgs=5,
                flagged_msgs=4,
                blocked_msgs=2,
            )
            self.advance_days(1)
        profile = profiler.get_profile("app", "u")
        assert len(profile["summaries"]) == 1
        assert profiler.get_ratio("app", "u") == 1.2
        if profile["summaries"]:
            summary = profile["summaries"][0]
            assert summary["total_msgs"] == 455
        profiler.close()

    def test_single_cycle_v5_f90_b5_3342(self) -> None:
        """A full window archives totals that match the configured rates."""
        profiler: UserProfiler = UserProfiler(":memory:", ":memory:", 91)
        for _ in range(91):
            profiler.record(
                "app",
                "u",
                total_msgs=5,
                flagged_msgs=4,
                blocked_msgs=0,
            )
            self.advance_days(1)
        profile = profiler.get_profile("app", "u")
        assert len(profile["summaries"]) == 1
        assert profiler.get_ratio("app", "u") == 0.8
        if profile["summaries"]:
            summary = profile["summaries"][0]
            assert summary["total_msgs"] == 455
        profiler.close()

    def test_single_cycle_v5_f95_b10_3343(self) -> None:
        """A full window archives totals that match the configured rates."""
        profiler: UserProfiler = UserProfiler(":memory:", ":memory:", 91)
        for _ in range(91):
            profiler.record(
                "app",
                "u",
                total_msgs=5,
                flagged_msgs=5,
                blocked_msgs=0,
            )
            self.advance_days(1)
        profile = profiler.get_profile("app", "u")
        assert len(profile["summaries"]) == 1
        assert profiler.get_ratio("app", "u") == 1.0
        if profile["summaries"]:
            summary = profile["summaries"][0]
            assert summary["total_msgs"] == 455
        profiler.close()

    def test_single_cycle_v5_f100_b0_3344(self) -> None:
        """A full window archives totals that match the configured rates."""
        profiler: UserProfiler = UserProfiler(":memory:", ":memory:", 91)
        for _ in range(91):
            profiler.record(
                "app",
                "u",
                total_msgs=5,
                flagged_msgs=5,
                blocked_msgs=0,
            )
            self.advance_days(1)
        profile = profiler.get_profile("app", "u")
        assert len(profile["summaries"]) == 1
        assert profiler.get_ratio("app", "u") == 1.0
        if profile["summaries"]:
            summary = profile["summaries"][0]
            assert summary["total_msgs"] == 455
        profiler.close()

    def test_single_cycle_v20_f0_b0_3345(self) -> None:
        """A full window archives totals that match the configured rates."""
        profiler: UserProfiler = UserProfiler(":memory:", ":memory:", 91)
        for _ in range(91):
            profiler.record(
                "app",
                "u",
                total_msgs=20,
                flagged_msgs=0,
                blocked_msgs=0,
            )
            self.advance_days(1)
        profile = profiler.get_profile("app", "u")
        assert len(profile["summaries"]) == 1
        assert profiler.get_ratio("app", "u") == 0.0
        if profile["summaries"]:
            summary = profile["summaries"][0]
            assert summary["total_msgs"] == 1820
        profiler.close()

    def test_single_cycle_v20_f5_b0_3346(self) -> None:
        """A full window archives totals that match the configured rates."""
        profiler: UserProfiler = UserProfiler(":memory:", ":memory:", 91)
        for _ in range(91):
            profiler.record(
                "app",
                "u",
                total_msgs=20,
                flagged_msgs=1,
                blocked_msgs=0,
            )
            self.advance_days(1)
        profile = profiler.get_profile("app", "u")
        assert len(profile["summaries"]) == 1
        assert profiler.get_ratio("app", "u") == 0.05
        if profile["summaries"]:
            summary = profile["summaries"][0]
            assert summary["total_msgs"] == 1820
        profiler.close()

    def test_single_cycle_v20_f10_b5_3347(self) -> None:
        """A full window archives totals that match the configured rates."""
        profiler: UserProfiler = UserProfiler(":memory:", ":memory:", 91)
        for _ in range(91):
            profiler.record(
                "app",
                "u",
                total_msgs=20,
                flagged_msgs=2,
                blocked_msgs=1,
            )
            self.advance_days(1)
        profile = profiler.get_profile("app", "u")
        assert len(profile["summaries"]) == 1
        assert profiler.get_ratio("app", "u") == 0.15
        if profile["summaries"]:
            summary = profile["summaries"][0]
            assert summary["total_msgs"] == 1820
        profiler.close()

    def test_single_cycle_v20_f15_b10_3348(self) -> None:
        """A full window archives totals that match the configured rates."""
        profiler: UserProfiler = UserProfiler(":memory:", ":memory:", 91)
        for _ in range(91):
            profiler.record(
                "app",
                "u",
                total_msgs=20,
                flagged_msgs=3,
                blocked_msgs=2,
            )
            self.advance_days(1)
        profile = profiler.get_profile("app", "u")
        assert len(profile["summaries"]) == 1
        assert profiler.get_ratio("app", "u") == 0.25
        if profile["summaries"]:
            summary = profile["summaries"][0]
            assert summary["total_msgs"] == 1820
        profiler.close()

    def test_single_cycle_v20_f20_b20_3349(self) -> None:
        """A full window archives totals that match the configured rates."""
        profiler: UserProfiler = UserProfiler(":memory:", ":memory:", 91)
        for _ in range(91):
            profiler.record(
                "app",
                "u",
                total_msgs=20,
                flagged_msgs=4,
                blocked_msgs=4,
            )
            self.advance_days(1)
        profile = profiler.get_profile("app", "u")
        assert len(profile["summaries"]) == 1
        assert profiler.get_ratio("app", "u") == 0.4
        if profile["summaries"]:
            summary = profile["summaries"][0]
            assert summary["total_msgs"] == 1820
        profiler.close()

    def test_single_cycle_v20_f25_b0_3350(self) -> None:
        """A full window archives totals that match the configured rates."""
        profiler: UserProfiler = UserProfiler(":memory:", ":memory:", 91)
        for _ in range(91):
            profiler.record(
                "app",
                "u",
                total_msgs=20,
                flagged_msgs=5,
                blocked_msgs=0,
            )
            self.advance_days(1)
        profile = profiler.get_profile("app", "u")
        assert len(profile["summaries"]) == 1
        assert profiler.get_ratio("app", "u") == 0.25
        if profile["summaries"]:
            summary = profile["summaries"][0]
            assert summary["total_msgs"] == 1820
        profiler.close()

    def test_single_cycle_v20_f30_b15_3351(self) -> None:
        """A full window archives totals that match the configured rates."""
        profiler: UserProfiler = UserProfiler(":memory:", ":memory:", 91)
        for _ in range(91):
            profiler.record(
                "app",
                "u",
                total_msgs=20,
                flagged_msgs=6,
                blocked_msgs=3,
            )
            self.advance_days(1)
        profile = profiler.get_profile("app", "u")
        assert len(profile["summaries"]) == 1
        assert profiler.get_ratio("app", "u") == 0.45
        if profile["summaries"]:
            summary = profile["summaries"][0]
            assert summary["total_msgs"] == 1820
        profiler.close()

    def test_single_cycle_v20_f35_b5_3352(self) -> None:
        """A full window archives totals that match the configured rates."""
        profiler: UserProfiler = UserProfiler(":memory:", ":memory:", 91)
        for _ in range(91):
            profiler.record(
                "app",
                "u",
                total_msgs=20,
                flagged_msgs=7,
                blocked_msgs=1,
            )
            self.advance_days(1)
        profile = profiler.get_profile("app", "u")
        assert len(profile["summaries"]) == 1
        assert profiler.get_ratio("app", "u") == 0.4
        if profile["summaries"]:
            summary = profile["summaries"][0]
            assert summary["total_msgs"] == 1820
        profiler.close()

    def test_single_cycle_v20_f40_b40_3353(self) -> None:
        """A full window archives totals that match the configured rates."""
        profiler: UserProfiler = UserProfiler(":memory:", ":memory:", 91)
        for _ in range(91):
            profiler.record(
                "app",
                "u",
                total_msgs=20,
                flagged_msgs=8,
                blocked_msgs=8,
            )
            self.advance_days(1)
        profile = profiler.get_profile("app", "u")
        assert len(profile["summaries"]) == 1
        assert profiler.get_ratio("app", "u") == 0.8
        if profile["summaries"]:
            summary = profile["summaries"][0]
            assert summary["total_msgs"] == 1820
        profiler.close()

    def test_single_cycle_v20_f45_b0_3354(self) -> None:
        """A full window archives totals that match the configured rates."""
        profiler: UserProfiler = UserProfiler(":memory:", ":memory:", 91)
        for _ in range(91):
            profiler.record(
                "app",
                "u",
                total_msgs=20,
                flagged_msgs=9,
                blocked_msgs=0,
            )
            self.advance_days(1)
        profile = profiler.get_profile("app", "u")
        assert len(profile["summaries"]) == 1
        assert profiler.get_ratio("app", "u") == 0.45
        if profile["summaries"]:
            summary = profile["summaries"][0]
            assert summary["total_msgs"] == 1820
        profiler.close()

    def test_single_cycle_v20_f50_b25_3355(self) -> None:
        """A full window archives totals that match the configured rates."""
        profiler: UserProfiler = UserProfiler(":memory:", ":memory:", 91)
        for _ in range(91):
            profiler.record(
                "app",
                "u",
                total_msgs=20,
                flagged_msgs=10,
                blocked_msgs=5,
            )
            self.advance_days(1)
        profile = profiler.get_profile("app", "u")
        assert len(profile["summaries"]) == 1
        assert profiler.get_ratio("app", "u") == 0.75
        if profile["summaries"]:
            summary = profile["summaries"][0]
            assert summary["total_msgs"] == 1820
        profiler.close()

    def test_single_cycle_v20_f55_b10_3356(self) -> None:
        """A full window archives totals that match the configured rates."""
        profiler: UserProfiler = UserProfiler(":memory:", ":memory:", 91)
        for _ in range(91):
            profiler.record(
                "app",
                "u",
                total_msgs=20,
                flagged_msgs=11,
                blocked_msgs=2,
            )
            self.advance_days(1)
        profile = profiler.get_profile("app", "u")
        assert len(profile["summaries"]) == 1
        assert profiler.get_ratio("app", "u") == 0.65
        if profile["summaries"]:
            summary = profile["summaries"][0]
            assert summary["total_msgs"] == 1820
        profiler.close()

    def test_single_cycle_v20_f60_b30_3357(self) -> None:
        """A full window archives totals that match the configured rates."""
        profiler: UserProfiler = UserProfiler(":memory:", ":memory:", 91)
        for _ in range(91):
            profiler.record(
                "app",
                "u",
                total_msgs=20,
                flagged_msgs=12,
                blocked_msgs=6,
            )
            self.advance_days(1)
        profile = profiler.get_profile("app", "u")
        assert len(profile["summaries"]) == 1
        assert profiler.get_ratio("app", "u") == 0.9
        if profile["summaries"]:
            summary = profile["summaries"][0]
            assert summary["total_msgs"] == 1820
        profiler.close()

    def test_single_cycle_v20_f65_b0_3358(self) -> None:
        """A full window archives totals that match the configured rates."""
        profiler: UserProfiler = UserProfiler(":memory:", ":memory:", 91)
        for _ in range(91):
            profiler.record(
                "app",
                "u",
                total_msgs=20,
                flagged_msgs=13,
                blocked_msgs=0,
            )
            self.advance_days(1)
        profile = profiler.get_profile("app", "u")
        assert len(profile["summaries"]) == 1
        assert profiler.get_ratio("app", "u") == 0.65
        if profile["summaries"]:
            summary = profile["summaries"][0]
            assert summary["total_msgs"] == 1820
        profiler.close()

    def test_single_cycle_v20_f70_b20_3359(self) -> None:
        """A full window archives totals that match the configured rates."""
        profiler: UserProfiler = UserProfiler(":memory:", ":memory:", 91)
        for _ in range(91):
            profiler.record(
                "app",
                "u",
                total_msgs=20,
                flagged_msgs=14,
                blocked_msgs=4,
            )
            self.advance_days(1)
        profile = profiler.get_profile("app", "u")
        assert len(profile["summaries"]) == 1
        assert profiler.get_ratio("app", "u") == 0.9
        if profile["summaries"]:
            summary = profile["summaries"][0]
            assert summary["total_msgs"] == 1820
        profiler.close()

    def test_single_cycle_v20_f75_b35_3360(self) -> None:
        """A full window archives totals that match the configured rates."""
        profiler: UserProfiler = UserProfiler(":memory:", ":memory:", 91)
        for _ in range(91):
            profiler.record(
                "app",
                "u",
                total_msgs=20,
                flagged_msgs=15,
                blocked_msgs=7,
            )
            self.advance_days(1)
        profile = profiler.get_profile("app", "u")
        assert len(profile["summaries"]) == 1
        assert profiler.get_ratio("app", "u") == 1.1
        if profile["summaries"]:
            summary = profile["summaries"][0]
            assert summary["total_msgs"] == 1820
        profiler.close()

    def test_single_cycle_v20_f80_b0_3361(self) -> None:
        """A full window archives totals that match the configured rates."""
        profiler: UserProfiler = UserProfiler(":memory:", ":memory:", 91)
        for _ in range(91):
            profiler.record(
                "app",
                "u",
                total_msgs=20,
                flagged_msgs=16,
                blocked_msgs=0,
            )
            self.advance_days(1)
        profile = profiler.get_profile("app", "u")
        assert len(profile["summaries"]) == 1
        assert profiler.get_ratio("app", "u") == 0.8
        if profile["summaries"]:
            summary = profile["summaries"][0]
            assert summary["total_msgs"] == 1820
        profiler.close()

    def test_single_cycle_v20_f85_b40_3362(self) -> None:
        """A full window archives totals that match the configured rates."""
        profiler: UserProfiler = UserProfiler(":memory:", ":memory:", 91)
        for _ in range(91):
            profiler.record(
                "app",
                "u",
                total_msgs=20,
                flagged_msgs=17,
                blocked_msgs=8,
            )
            self.advance_days(1)
        profile = profiler.get_profile("app", "u")
        assert len(profile["summaries"]) == 1
        assert profiler.get_ratio("app", "u") == 1.25
        if profile["summaries"]:
            summary = profile["summaries"][0]
            assert summary["total_msgs"] == 1820
        profiler.close()

    def test_single_cycle_v20_f90_b5_3363(self) -> None:
        """A full window archives totals that match the configured rates."""
        profiler: UserProfiler = UserProfiler(":memory:", ":memory:", 91)
        for _ in range(91):
            profiler.record(
                "app",
                "u",
                total_msgs=20,
                flagged_msgs=18,
                blocked_msgs=1,
            )
            self.advance_days(1)
        profile = profiler.get_profile("app", "u")
        assert len(profile["summaries"]) == 1
        assert profiler.get_ratio("app", "u") == 0.95
        if profile["summaries"]:
            summary = profile["summaries"][0]
            assert summary["total_msgs"] == 1820
        profiler.close()

    def test_single_cycle_v20_f95_b10_3364(self) -> None:
        """A full window archives totals that match the configured rates."""
        profiler: UserProfiler = UserProfiler(":memory:", ":memory:", 91)
        for _ in range(91):
            profiler.record(
                "app",
                "u",
                total_msgs=20,
                flagged_msgs=19,
                blocked_msgs=2,
            )
            self.advance_days(1)
        profile = profiler.get_profile("app", "u")
        assert len(profile["summaries"]) == 1
        assert profiler.get_ratio("app", "u") == 1.05
        if profile["summaries"]:
            summary = profile["summaries"][0]
            assert summary["total_msgs"] == 1820
        profiler.close()

    def test_single_cycle_v20_f100_b0_3365(self) -> None:
        """A full window archives totals that match the configured rates."""
        profiler: UserProfiler = UserProfiler(":memory:", ":memory:", 91)
        for _ in range(91):
            profiler.record(
                "app",
                "u",
                total_msgs=20,
                flagged_msgs=20,
                blocked_msgs=0,
            )
            self.advance_days(1)
        profile = profiler.get_profile("app", "u")
        assert len(profile["summaries"]) == 1
        assert profiler.get_ratio("app", "u") == 1.0
        if profile["summaries"]:
            summary = profile["summaries"][0]
            assert summary["total_msgs"] == 1820
        profiler.close()

    def test_single_cycle_v40_f0_b0_3366(self) -> None:
        """A full window archives totals that match the configured rates."""
        profiler: UserProfiler = UserProfiler(":memory:", ":memory:", 91)
        for _ in range(91):
            profiler.record(
                "app",
                "u",
                total_msgs=40,
                flagged_msgs=0,
                blocked_msgs=0,
            )
            self.advance_days(1)
        profile = profiler.get_profile("app", "u")
        assert len(profile["summaries"]) == 1
        assert profiler.get_ratio("app", "u") == 0.0
        if profile["summaries"]:
            summary = profile["summaries"][0]
            assert summary["total_msgs"] == 3640
        profiler.close()

    def test_single_cycle_v40_f5_b0_3367(self) -> None:
        """A full window archives totals that match the configured rates."""
        profiler: UserProfiler = UserProfiler(":memory:", ":memory:", 91)
        for _ in range(91):
            profiler.record(
                "app",
                "u",
                total_msgs=40,
                flagged_msgs=2,
                blocked_msgs=0,
            )
            self.advance_days(1)
        profile = profiler.get_profile("app", "u")
        assert len(profile["summaries"]) == 1
        assert profiler.get_ratio("app", "u") == 0.05
        if profile["summaries"]:
            summary = profile["summaries"][0]
            assert summary["total_msgs"] == 3640
        profiler.close()

    def test_single_cycle_v40_f10_b5_3368(self) -> None:
        """A full window archives totals that match the configured rates."""
        profiler: UserProfiler = UserProfiler(":memory:", ":memory:", 91)
        for _ in range(91):
            profiler.record(
                "app",
                "u",
                total_msgs=40,
                flagged_msgs=4,
                blocked_msgs=2,
            )
            self.advance_days(1)
        profile = profiler.get_profile("app", "u")
        assert len(profile["summaries"]) == 1
        assert profiler.get_ratio("app", "u") == 0.15
        if profile["summaries"]:
            summary = profile["summaries"][0]
            assert summary["total_msgs"] == 3640
        profiler.close()

    def test_single_cycle_v40_f15_b10_3369(self) -> None:
        """A full window archives totals that match the configured rates."""
        profiler: UserProfiler = UserProfiler(":memory:", ":memory:", 91)
        for _ in range(91):
            profiler.record(
                "app",
                "u",
                total_msgs=40,
                flagged_msgs=6,
                blocked_msgs=4,
            )
            self.advance_days(1)
        profile = profiler.get_profile("app", "u")
        assert len(profile["summaries"]) == 1
        assert profiler.get_ratio("app", "u") == 0.25
        if profile["summaries"]:
            summary = profile["summaries"][0]
            assert summary["total_msgs"] == 3640
        profiler.close()

    def test_single_cycle_v40_f20_b20_3370(self) -> None:
        """A full window archives totals that match the configured rates."""
        profiler: UserProfiler = UserProfiler(":memory:", ":memory:", 91)
        for _ in range(91):
            profiler.record(
                "app",
                "u",
                total_msgs=40,
                flagged_msgs=8,
                blocked_msgs=8,
            )
            self.advance_days(1)
        profile = profiler.get_profile("app", "u")
        assert len(profile["summaries"]) == 1
        assert profiler.get_ratio("app", "u") == 0.4
        if profile["summaries"]:
            summary = profile["summaries"][0]
            assert summary["total_msgs"] == 3640
        profiler.close()

    def test_single_cycle_v40_f25_b0_3371(self) -> None:
        """A full window archives totals that match the configured rates."""
        profiler: UserProfiler = UserProfiler(":memory:", ":memory:", 91)
        for _ in range(91):
            profiler.record(
                "app",
                "u",
                total_msgs=40,
                flagged_msgs=10,
                blocked_msgs=0,
            )
            self.advance_days(1)
        profile = profiler.get_profile("app", "u")
        assert len(profile["summaries"]) == 1
        assert profiler.get_ratio("app", "u") == 0.25
        if profile["summaries"]:
            summary = profile["summaries"][0]
            assert summary["total_msgs"] == 3640
        profiler.close()

    def test_single_cycle_v40_f30_b15_3372(self) -> None:
        """A full window archives totals that match the configured rates."""
        profiler: UserProfiler = UserProfiler(":memory:", ":memory:", 91)
        for _ in range(91):
            profiler.record(
                "app",
                "u",
                total_msgs=40,
                flagged_msgs=12,
                blocked_msgs=6,
            )
            self.advance_days(1)
        profile = profiler.get_profile("app", "u")
        assert len(profile["summaries"]) == 1
        assert profiler.get_ratio("app", "u") == 0.45
        if profile["summaries"]:
            summary = profile["summaries"][0]
            assert summary["total_msgs"] == 3640
        profiler.close()

    def test_single_cycle_v40_f35_b5_3373(self) -> None:
        """A full window archives totals that match the configured rates."""
        profiler: UserProfiler = UserProfiler(":memory:", ":memory:", 91)
        for _ in range(91):
            profiler.record(
                "app",
                "u",
                total_msgs=40,
                flagged_msgs=14,
                blocked_msgs=2,
            )
            self.advance_days(1)
        profile = profiler.get_profile("app", "u")
        assert len(profile["summaries"]) == 1
        assert profiler.get_ratio("app", "u") == 0.4
        if profile["summaries"]:
            summary = profile["summaries"][0]
            assert summary["total_msgs"] == 3640
        profiler.close()

    def test_single_cycle_v40_f40_b40_3374(self) -> None:
        """A full window archives totals that match the configured rates."""
        profiler: UserProfiler = UserProfiler(":memory:", ":memory:", 91)
        for _ in range(91):
            profiler.record(
                "app",
                "u",
                total_msgs=40,
                flagged_msgs=16,
                blocked_msgs=16,
            )
            self.advance_days(1)
        profile = profiler.get_profile("app", "u")
        assert len(profile["summaries"]) == 1
        assert profiler.get_ratio("app", "u") == 0.8
        if profile["summaries"]:
            summary = profile["summaries"][0]
            assert summary["total_msgs"] == 3640
        profiler.close()

    def test_single_cycle_v40_f45_b0_3375(self) -> None:
        """A full window archives totals that match the configured rates."""
        profiler: UserProfiler = UserProfiler(":memory:", ":memory:", 91)
        for _ in range(91):
            profiler.record(
                "app",
                "u",
                total_msgs=40,
                flagged_msgs=18,
                blocked_msgs=0,
            )
            self.advance_days(1)
        profile = profiler.get_profile("app", "u")
        assert len(profile["summaries"]) == 1
        assert profiler.get_ratio("app", "u") == 0.45
        if profile["summaries"]:
            summary = profile["summaries"][0]
            assert summary["total_msgs"] == 3640
        profiler.close()

    def test_single_cycle_v40_f50_b25_3376(self) -> None:
        """A full window archives totals that match the configured rates."""
        profiler: UserProfiler = UserProfiler(":memory:", ":memory:", 91)
        for _ in range(91):
            profiler.record(
                "app",
                "u",
                total_msgs=40,
                flagged_msgs=20,
                blocked_msgs=10,
            )
            self.advance_days(1)
        profile = profiler.get_profile("app", "u")
        assert len(profile["summaries"]) == 1
        assert profiler.get_ratio("app", "u") == 0.75
        if profile["summaries"]:
            summary = profile["summaries"][0]
            assert summary["total_msgs"] == 3640
        profiler.close()

    def test_single_cycle_v40_f55_b10_3377(self) -> None:
        """A full window archives totals that match the configured rates."""
        profiler: UserProfiler = UserProfiler(":memory:", ":memory:", 91)
        for _ in range(91):
            profiler.record(
                "app",
                "u",
                total_msgs=40,
                flagged_msgs=22,
                blocked_msgs=4,
            )
            self.advance_days(1)
        profile = profiler.get_profile("app", "u")
        assert len(profile["summaries"]) == 1
        assert profiler.get_ratio("app", "u") == 0.65
        if profile["summaries"]:
            summary = profile["summaries"][0]
            assert summary["total_msgs"] == 3640
        profiler.close()

    def test_single_cycle_v40_f60_b30_3378(self) -> None:
        """A full window archives totals that match the configured rates."""
        profiler: UserProfiler = UserProfiler(":memory:", ":memory:", 91)
        for _ in range(91):
            profiler.record(
                "app",
                "u",
                total_msgs=40,
                flagged_msgs=24,
                blocked_msgs=12,
            )
            self.advance_days(1)
        profile = profiler.get_profile("app", "u")
        assert len(profile["summaries"]) == 1
        assert profiler.get_ratio("app", "u") == 0.9
        if profile["summaries"]:
            summary = profile["summaries"][0]
            assert summary["total_msgs"] == 3640
        profiler.close()

    def test_single_cycle_v40_f65_b0_3379(self) -> None:
        """A full window archives totals that match the configured rates."""
        profiler: UserProfiler = UserProfiler(":memory:", ":memory:", 91)
        for _ in range(91):
            profiler.record(
                "app",
                "u",
                total_msgs=40,
                flagged_msgs=26,
                blocked_msgs=0,
            )
            self.advance_days(1)
        profile = profiler.get_profile("app", "u")
        assert len(profile["summaries"]) == 1
        assert profiler.get_ratio("app", "u") == 0.65
        if profile["summaries"]:
            summary = profile["summaries"][0]
            assert summary["total_msgs"] == 3640
        profiler.close()

    def test_single_cycle_v40_f70_b20_3380(self) -> None:
        """A full window archives totals that match the configured rates."""
        profiler: UserProfiler = UserProfiler(":memory:", ":memory:", 91)
        for _ in range(91):
            profiler.record(
                "app",
                "u",
                total_msgs=40,
                flagged_msgs=28,
                blocked_msgs=8,
            )
            self.advance_days(1)
        profile = profiler.get_profile("app", "u")
        assert len(profile["summaries"]) == 1
        assert profiler.get_ratio("app", "u") == 0.9
        if profile["summaries"]:
            summary = profile["summaries"][0]
            assert summary["total_msgs"] == 3640
        profiler.close()

    def test_single_cycle_v40_f75_b35_3381(self) -> None:
        """A full window archives totals that match the configured rates."""
        profiler: UserProfiler = UserProfiler(":memory:", ":memory:", 91)
        for _ in range(91):
            profiler.record(
                "app",
                "u",
                total_msgs=40,
                flagged_msgs=30,
                blocked_msgs=14,
            )
            self.advance_days(1)
        profile = profiler.get_profile("app", "u")
        assert len(profile["summaries"]) == 1
        assert profiler.get_ratio("app", "u") == 1.1
        if profile["summaries"]:
            summary = profile["summaries"][0]
            assert summary["total_msgs"] == 3640
        profiler.close()

    def test_single_cycle_v40_f80_b0_3382(self) -> None:
        """A full window archives totals that match the configured rates."""
        profiler: UserProfiler = UserProfiler(":memory:", ":memory:", 91)
        for _ in range(91):
            profiler.record(
                "app",
                "u",
                total_msgs=40,
                flagged_msgs=32,
                blocked_msgs=0,
            )
            self.advance_days(1)
        profile = profiler.get_profile("app", "u")
        assert len(profile["summaries"]) == 1
        assert profiler.get_ratio("app", "u") == 0.8
        if profile["summaries"]:
            summary = profile["summaries"][0]
            assert summary["total_msgs"] == 3640
        profiler.close()

    def test_single_cycle_v40_f85_b40_3383(self) -> None:
        """A full window archives totals that match the configured rates."""
        profiler: UserProfiler = UserProfiler(":memory:", ":memory:", 91)
        for _ in range(91):
            profiler.record(
                "app",
                "u",
                total_msgs=40,
                flagged_msgs=34,
                blocked_msgs=16,
            )
            self.advance_days(1)
        profile = profiler.get_profile("app", "u")
        assert len(profile["summaries"]) == 1
        assert profiler.get_ratio("app", "u") == 1.25
        if profile["summaries"]:
            summary = profile["summaries"][0]
            assert summary["total_msgs"] == 3640
        profiler.close()

    def test_single_cycle_v40_f90_b5_3384(self) -> None:
        """A full window archives totals that match the configured rates."""
        profiler: UserProfiler = UserProfiler(":memory:", ":memory:", 91)
        for _ in range(91):
            profiler.record(
                "app",
                "u",
                total_msgs=40,
                flagged_msgs=36,
                blocked_msgs=2,
            )
            self.advance_days(1)
        profile = profiler.get_profile("app", "u")
        assert len(profile["summaries"]) == 1
        assert profiler.get_ratio("app", "u") == 0.95
        if profile["summaries"]:
            summary = profile["summaries"][0]
            assert summary["total_msgs"] == 3640
        profiler.close()

    def test_single_cycle_v40_f95_b10_3385(self) -> None:
        """A full window archives totals that match the configured rates."""
        profiler: UserProfiler = UserProfiler(":memory:", ":memory:", 91)
        for _ in range(91):
            profiler.record(
                "app",
                "u",
                total_msgs=40,
                flagged_msgs=38,
                blocked_msgs=4,
            )
            self.advance_days(1)
        profile = profiler.get_profile("app", "u")
        assert len(profile["summaries"]) == 1
        assert profiler.get_ratio("app", "u") == 1.05
        if profile["summaries"]:
            summary = profile["summaries"][0]
            assert summary["total_msgs"] == 3640
        profiler.close()

    def test_single_cycle_v40_f100_b0_3386(self) -> None:
        """A full window archives totals that match the configured rates."""
        profiler: UserProfiler = UserProfiler(":memory:", ":memory:", 91)
        for _ in range(91):
            profiler.record(
                "app",
                "u",
                total_msgs=40,
                flagged_msgs=40,
                blocked_msgs=0,
            )
            self.advance_days(1)
        profile = profiler.get_profile("app", "u")
        assert len(profile["summaries"]) == 1
        assert profiler.get_ratio("app", "u") == 1.0
        if profile["summaries"]:
            summary = profile["summaries"][0]
            assert summary["total_msgs"] == 3640
        profiler.close()

    def test_single_cycle_v75_f0_b0_3387(self) -> None:
        """A full window archives totals that match the configured rates."""
        profiler: UserProfiler = UserProfiler(":memory:", ":memory:", 91)
        for _ in range(91):
            profiler.record(
                "app",
                "u",
                total_msgs=75,
                flagged_msgs=0,
                blocked_msgs=0,
            )
            self.advance_days(1)
        profile = profiler.get_profile("app", "u")
        assert len(profile["summaries"]) == 1
        assert profiler.get_ratio("app", "u") == 0.0
        if profile["summaries"]:
            summary = profile["summaries"][0]
            assert summary["total_msgs"] == 6825
        profiler.close()

    def test_single_cycle_v75_f5_b0_3388(self) -> None:
        """A full window archives totals that match the configured rates."""
        profiler: UserProfiler = UserProfiler(":memory:", ":memory:", 91)
        for _ in range(91):
            profiler.record(
                "app",
                "u",
                total_msgs=75,
                flagged_msgs=4,
                blocked_msgs=0,
            )
            self.advance_days(1)
        profile = profiler.get_profile("app", "u")
        assert len(profile["summaries"]) == 1
        assert profiler.get_ratio("app", "u") == 0.05333333333333334
        if profile["summaries"]:
            summary = profile["summaries"][0]
            assert summary["total_msgs"] == 6825
        profiler.close()

    def test_single_cycle_v75_f10_b5_3389(self) -> None:
        """A full window archives totals that match the configured rates."""
        profiler: UserProfiler = UserProfiler(":memory:", ":memory:", 91)
        for _ in range(91):
            profiler.record(
                "app",
                "u",
                total_msgs=75,
                flagged_msgs=8,
                blocked_msgs=4,
            )
            self.advance_days(1)
        profile = profiler.get_profile("app", "u")
        assert len(profile["summaries"]) == 1
        assert profiler.get_ratio("app", "u") == 0.16
        if profile["summaries"]:
            summary = profile["summaries"][0]
            assert summary["total_msgs"] == 6825
        profiler.close()

    def test_single_cycle_v75_f15_b10_3390(self) -> None:
        """A full window archives totals that match the configured rates."""
        profiler: UserProfiler = UserProfiler(":memory:", ":memory:", 91)
        for _ in range(91):
            profiler.record(
                "app",
                "u",
                total_msgs=75,
                flagged_msgs=11,
                blocked_msgs=8,
            )
            self.advance_days(1)
        profile = profiler.get_profile("app", "u")
        assert len(profile["summaries"]) == 1
        assert profiler.get_ratio("app", "u") == 0.25333333333333335
        if profile["summaries"]:
            summary = profile["summaries"][0]
            assert summary["total_msgs"] == 6825
        profiler.close()

    def test_single_cycle_v75_f20_b20_3391(self) -> None:
        """A full window archives totals that match the configured rates."""
        profiler: UserProfiler = UserProfiler(":memory:", ":memory:", 91)
        for _ in range(91):
            profiler.record(
                "app",
                "u",
                total_msgs=75,
                flagged_msgs=15,
                blocked_msgs=15,
            )
            self.advance_days(1)
        profile = profiler.get_profile("app", "u")
        assert len(profile["summaries"]) == 1
        assert profiler.get_ratio("app", "u") == 0.4
        if profile["summaries"]:
            summary = profile["summaries"][0]
            assert summary["total_msgs"] == 6825
        profiler.close()

    def test_single_cycle_v75_f25_b0_3392(self) -> None:
        """A full window archives totals that match the configured rates."""
        profiler: UserProfiler = UserProfiler(":memory:", ":memory:", 91)
        for _ in range(91):
            profiler.record(
                "app",
                "u",
                total_msgs=75,
                flagged_msgs=19,
                blocked_msgs=0,
            )
            self.advance_days(1)
        profile = profiler.get_profile("app", "u")
        assert len(profile["summaries"]) == 1
        assert profiler.get_ratio("app", "u") == 0.25333333333333335
        if profile["summaries"]:
            summary = profile["summaries"][0]
            assert summary["total_msgs"] == 6825
        profiler.close()

    def test_single_cycle_v75_f30_b15_3393(self) -> None:
        """A full window archives totals that match the configured rates."""
        profiler: UserProfiler = UserProfiler(":memory:", ":memory:", 91)
        for _ in range(91):
            profiler.record(
                "app",
                "u",
                total_msgs=75,
                flagged_msgs=22,
                blocked_msgs=11,
            )
            self.advance_days(1)
        profile = profiler.get_profile("app", "u")
        assert len(profile["summaries"]) == 1
        assert profiler.get_ratio("app", "u") == 0.44
        if profile["summaries"]:
            summary = profile["summaries"][0]
            assert summary["total_msgs"] == 6825
        profiler.close()

    def test_single_cycle_v75_f35_b5_3394(self) -> None:
        """A full window archives totals that match the configured rates."""
        profiler: UserProfiler = UserProfiler(":memory:", ":memory:", 91)
        for _ in range(91):
            profiler.record(
                "app",
                "u",
                total_msgs=75,
                flagged_msgs=26,
                blocked_msgs=4,
            )
            self.advance_days(1)
        profile = profiler.get_profile("app", "u")
        assert len(profile["summaries"]) == 1
        assert profiler.get_ratio("app", "u") == 0.4
        if profile["summaries"]:
            summary = profile["summaries"][0]
            assert summary["total_msgs"] == 6825
        profiler.close()

    def test_single_cycle_v75_f40_b40_3395(self) -> None:
        """A full window archives totals that match the configured rates."""
        profiler: UserProfiler = UserProfiler(":memory:", ":memory:", 91)
        for _ in range(91):
            profiler.record(
                "app",
                "u",
                total_msgs=75,
                flagged_msgs=30,
                blocked_msgs=30,
            )
            self.advance_days(1)
        profile = profiler.get_profile("app", "u")
        assert len(profile["summaries"]) == 1
        assert profiler.get_ratio("app", "u") == 0.8
        if profile["summaries"]:
            summary = profile["summaries"][0]
            assert summary["total_msgs"] == 6825
        profiler.close()

    def test_single_cycle_v75_f45_b0_3396(self) -> None:
        """A full window archives totals that match the configured rates."""
        profiler: UserProfiler = UserProfiler(":memory:", ":memory:", 91)
        for _ in range(91):
            profiler.record(
                "app",
                "u",
                total_msgs=75,
                flagged_msgs=34,
                blocked_msgs=0,
            )
            self.advance_days(1)
        profile = profiler.get_profile("app", "u")
        assert len(profile["summaries"]) == 1
        assert profiler.get_ratio("app", "u") == 0.4533333333333333
        if profile["summaries"]:
            summary = profile["summaries"][0]
            assert summary["total_msgs"] == 6825
        profiler.close()

    def test_single_cycle_v75_f50_b25_3397(self) -> None:
        """A full window archives totals that match the configured rates."""
        profiler: UserProfiler = UserProfiler(":memory:", ":memory:", 91)
        for _ in range(91):
            profiler.record(
                "app",
                "u",
                total_msgs=75,
                flagged_msgs=38,
                blocked_msgs=19,
            )
            self.advance_days(1)
        profile = profiler.get_profile("app", "u")
        assert len(profile["summaries"]) == 1
        assert profiler.get_ratio("app", "u") == 0.76
        if profile["summaries"]:
            summary = profile["summaries"][0]
            assert summary["total_msgs"] == 6825
        profiler.close()

    def test_single_cycle_v75_f55_b10_3398(self) -> None:
        """A full window archives totals that match the configured rates."""
        profiler: UserProfiler = UserProfiler(":memory:", ":memory:", 91)
        for _ in range(91):
            profiler.record(
                "app",
                "u",
                total_msgs=75,
                flagged_msgs=41,
                blocked_msgs=8,
            )
            self.advance_days(1)
        profile = profiler.get_profile("app", "u")
        assert len(profile["summaries"]) == 1
        assert profiler.get_ratio("app", "u") == 0.6533333333333333
        if profile["summaries"]:
            summary = profile["summaries"][0]
            assert summary["total_msgs"] == 6825
        profiler.close()

    def test_single_cycle_v75_f60_b30_3399(self) -> None:
        """A full window archives totals that match the configured rates."""
        profiler: UserProfiler = UserProfiler(":memory:", ":memory:", 91)
        for _ in range(91):
            profiler.record(
                "app",
                "u",
                total_msgs=75,
                flagged_msgs=45,
                blocked_msgs=22,
            )
            self.advance_days(1)
        profile = profiler.get_profile("app", "u")
        assert len(profile["summaries"]) == 1
        assert profiler.get_ratio("app", "u") == 0.8933333333333333
        if profile["summaries"]:
            summary = profile["summaries"][0]
            assert summary["total_msgs"] == 6825
        profiler.close()

    def test_single_cycle_v75_f65_b0_3400(self) -> None:
        """A full window archives totals that match the configured rates."""
        profiler: UserProfiler = UserProfiler(":memory:", ":memory:", 91)
        for _ in range(91):
            profiler.record(
                "app",
                "u",
                total_msgs=75,
                flagged_msgs=49,
                blocked_msgs=0,
            )
            self.advance_days(1)
        profile = profiler.get_profile("app", "u")
        assert len(profile["summaries"]) == 1
        assert profiler.get_ratio("app", "u") == 0.6533333333333333
        if profile["summaries"]:
            summary = profile["summaries"][0]
            assert summary["total_msgs"] == 6825
        profiler.close()

    def test_single_cycle_v75_f70_b20_3401(self) -> None:
        """A full window archives totals that match the configured rates."""
        profiler: UserProfiler = UserProfiler(":memory:", ":memory:", 91)
        for _ in range(91):
            profiler.record(
                "app",
                "u",
                total_msgs=75,
                flagged_msgs=52,
                blocked_msgs=15,
            )
            self.advance_days(1)
        profile = profiler.get_profile("app", "u")
        assert len(profile["summaries"]) == 1
        assert profiler.get_ratio("app", "u") == 0.8933333333333333
        if profile["summaries"]:
            summary = profile["summaries"][0]
            assert summary["total_msgs"] == 6825
        profiler.close()

    def test_single_cycle_v75_f75_b35_3402(self) -> None:
        """A full window archives totals that match the configured rates."""
        profiler: UserProfiler = UserProfiler(":memory:", ":memory:", 91)
        for _ in range(91):
            profiler.record(
                "app",
                "u",
                total_msgs=75,
                flagged_msgs=56,
                blocked_msgs=26,
            )
            self.advance_days(1)
        profile = profiler.get_profile("app", "u")
        assert len(profile["summaries"]) == 1
        assert profiler.get_ratio("app", "u") == 1.0933333333333333
        if profile["summaries"]:
            summary = profile["summaries"][0]
            assert summary["total_msgs"] == 6825
        profiler.close()
