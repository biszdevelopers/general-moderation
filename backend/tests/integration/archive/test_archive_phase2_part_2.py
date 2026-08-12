"""Phase 2 archive cycle tests (generated).

Volume and percentage matrices, multi-cycle chains, multi-user/app
archives and boundary edges under the frozen clock."""

# multilingual fixtures use non-ASCII on purpose
from __future__ import annotations

from app.profiling.user_profiler import UserProfiler
from tests.base_test import BaseTest


class TestSingleCycle(BaseTest):
    """SingleCycle scenarios."""

    def test_single_cycle_v75_f80_b0_3403(self) -> None:
        """A full window archives totals that match the configured rates."""
        profiler: UserProfiler = UserProfiler(":memory:", ":memory:", 91)
        for _ in range(91):
            profiler.record(
                "app",
                "u",
                total_msgs=75,
                flagged_msgs=60,
                blocked_msgs=0,
            )
            self.advance_days(1)
        profile = profiler.get_profile("app", "u")
        assert len(profile["summaries"]) == 1
        assert profiler.get_ratio("app", "u") == 0.8
        if profile["summaries"]:
            summary = profile["summaries"][0]
            assert summary["total_msgs"] == 6825
        profiler.close()

    def test_single_cycle_v75_f85_b40_3404(self) -> None:
        """A full window archives totals that match the configured rates."""
        profiler: UserProfiler = UserProfiler(":memory:", ":memory:", 91)
        for _ in range(91):
            profiler.record(
                "app",
                "u",
                total_msgs=75,
                flagged_msgs=64,
                blocked_msgs=30,
            )
            self.advance_days(1)
        profile = profiler.get_profile("app", "u")
        assert len(profile["summaries"]) == 1
        assert profiler.get_ratio("app", "u") == 1.2533333333333334
        if profile["summaries"]:
            summary = profile["summaries"][0]
            assert summary["total_msgs"] == 6825
        profiler.close()

    def test_single_cycle_v75_f90_b5_3405(self) -> None:
        """A full window archives totals that match the configured rates."""
        profiler: UserProfiler = UserProfiler(":memory:", ":memory:", 91)
        for _ in range(91):
            profiler.record(
                "app",
                "u",
                total_msgs=75,
                flagged_msgs=68,
                blocked_msgs=4,
            )
            self.advance_days(1)
        profile = profiler.get_profile("app", "u")
        assert len(profile["summaries"]) == 1
        assert profiler.get_ratio("app", "u") == 0.96
        if profile["summaries"]:
            summary = profile["summaries"][0]
            assert summary["total_msgs"] == 6825
        profiler.close()

    def test_single_cycle_v75_f95_b10_3406(self) -> None:
        """A full window archives totals that match the configured rates."""
        profiler: UserProfiler = UserProfiler(":memory:", ":memory:", 91)
        for _ in range(91):
            profiler.record(
                "app",
                "u",
                total_msgs=75,
                flagged_msgs=71,
                blocked_msgs=8,
            )
            self.advance_days(1)
        profile = profiler.get_profile("app", "u")
        assert len(profile["summaries"]) == 1
        assert profiler.get_ratio("app", "u") == 1.0533333333333332
        if profile["summaries"]:
            summary = profile["summaries"][0]
            assert summary["total_msgs"] == 6825
        profiler.close()

    def test_single_cycle_v75_f100_b0_3407(self) -> None:
        """A full window archives totals that match the configured rates."""
        profiler: UserProfiler = UserProfiler(":memory:", ":memory:", 91)
        for _ in range(91):
            profiler.record(
                "app",
                "u",
                total_msgs=75,
                flagged_msgs=75,
                blocked_msgs=0,
            )
            self.advance_days(1)
        profile = profiler.get_profile("app", "u")
        assert len(profile["summaries"]) == 1
        assert profiler.get_ratio("app", "u") == 1.0
        if profile["summaries"]:
            summary = profile["summaries"][0]
            assert summary["total_msgs"] == 6825
        profiler.close()

    def test_single_cycle_v150_f0_b0_3408(self) -> None:
        """A full window archives totals that match the configured rates."""
        profiler: UserProfiler = UserProfiler(":memory:", ":memory:", 91)
        for _ in range(91):
            profiler.record(
                "app",
                "u",
                total_msgs=150,
                flagged_msgs=0,
                blocked_msgs=0,
            )
            self.advance_days(1)
        profile = profiler.get_profile("app", "u")
        assert len(profile["summaries"]) == 1
        assert profiler.get_ratio("app", "u") == 0.0
        if profile["summaries"]:
            summary = profile["summaries"][0]
            assert summary["total_msgs"] == 13650
        profiler.close()

    def test_single_cycle_v150_f5_b0_3409(self) -> None:
        """A full window archives totals that match the configured rates."""
        profiler: UserProfiler = UserProfiler(":memory:", ":memory:", 91)
        for _ in range(91):
            profiler.record(
                "app",
                "u",
                total_msgs=150,
                flagged_msgs=8,
                blocked_msgs=0,
            )
            self.advance_days(1)
        profile = profiler.get_profile("app", "u")
        assert len(profile["summaries"]) == 1
        assert profiler.get_ratio("app", "u") == 0.05333333333333334
        if profile["summaries"]:
            summary = profile["summaries"][0]
            assert summary["total_msgs"] == 13650
        profiler.close()

    def test_single_cycle_v150_f10_b5_3410(self) -> None:
        """A full window archives totals that match the configured rates."""
        profiler: UserProfiler = UserProfiler(":memory:", ":memory:", 91)
        for _ in range(91):
            profiler.record(
                "app",
                "u",
                total_msgs=150,
                flagged_msgs=15,
                blocked_msgs=8,
            )
            self.advance_days(1)
        profile = profiler.get_profile("app", "u")
        assert len(profile["summaries"]) == 1
        assert profiler.get_ratio("app", "u") == 0.15333333333333332
        if profile["summaries"]:
            summary = profile["summaries"][0]
            assert summary["total_msgs"] == 13650
        profiler.close()

    def test_single_cycle_v150_f15_b10_3411(self) -> None:
        """A full window archives totals that match the configured rates."""
        profiler: UserProfiler = UserProfiler(":memory:", ":memory:", 91)
        for _ in range(91):
            profiler.record(
                "app",
                "u",
                total_msgs=150,
                flagged_msgs=22,
                blocked_msgs=15,
            )
            self.advance_days(1)
        profile = profiler.get_profile("app", "u")
        assert len(profile["summaries"]) == 1
        assert profiler.get_ratio("app", "u") == 0.24666666666666667
        if profile["summaries"]:
            summary = profile["summaries"][0]
            assert summary["total_msgs"] == 13650
        profiler.close()

    def test_single_cycle_v150_f20_b20_3412(self) -> None:
        """A full window archives totals that match the configured rates."""
        profiler: UserProfiler = UserProfiler(":memory:", ":memory:", 91)
        for _ in range(91):
            profiler.record(
                "app",
                "u",
                total_msgs=150,
                flagged_msgs=30,
                blocked_msgs=30,
            )
            self.advance_days(1)
        profile = profiler.get_profile("app", "u")
        assert len(profile["summaries"]) == 1
        assert profiler.get_ratio("app", "u") == 0.4
        if profile["summaries"]:
            summary = profile["summaries"][0]
            assert summary["total_msgs"] == 13650
        profiler.close()

    def test_single_cycle_v150_f25_b0_3413(self) -> None:
        """A full window archives totals that match the configured rates."""
        profiler: UserProfiler = UserProfiler(":memory:", ":memory:", 91)
        for _ in range(91):
            profiler.record(
                "app",
                "u",
                total_msgs=150,
                flagged_msgs=38,
                blocked_msgs=0,
            )
            self.advance_days(1)
        profile = profiler.get_profile("app", "u")
        assert len(profile["summaries"]) == 1
        assert profiler.get_ratio("app", "u") == 0.25333333333333335
        if profile["summaries"]:
            summary = profile["summaries"][0]
            assert summary["total_msgs"] == 13650
        profiler.close()

    def test_single_cycle_v150_f30_b15_3414(self) -> None:
        """A full window archives totals that match the configured rates."""
        profiler: UserProfiler = UserProfiler(":memory:", ":memory:", 91)
        for _ in range(91):
            profiler.record(
                "app",
                "u",
                total_msgs=150,
                flagged_msgs=45,
                blocked_msgs=22,
            )
            self.advance_days(1)
        profile = profiler.get_profile("app", "u")
        assert len(profile["summaries"]) == 1
        assert profiler.get_ratio("app", "u") == 0.44666666666666666
        if profile["summaries"]:
            summary = profile["summaries"][0]
            assert summary["total_msgs"] == 13650
        profiler.close()

    def test_single_cycle_v150_f35_b5_3415(self) -> None:
        """A full window archives totals that match the configured rates."""
        profiler: UserProfiler = UserProfiler(":memory:", ":memory:", 91)
        for _ in range(91):
            profiler.record(
                "app",
                "u",
                total_msgs=150,
                flagged_msgs=52,
                blocked_msgs=8,
            )
            self.advance_days(1)
        profile = profiler.get_profile("app", "u")
        assert len(profile["summaries"]) == 1
        assert profiler.get_ratio("app", "u") == 0.4
        if profile["summaries"]:
            summary = profile["summaries"][0]
            assert summary["total_msgs"] == 13650
        profiler.close()

    def test_single_cycle_v150_f40_b40_3416(self) -> None:
        """A full window archives totals that match the configured rates."""
        profiler: UserProfiler = UserProfiler(":memory:", ":memory:", 91)
        for _ in range(91):
            profiler.record(
                "app",
                "u",
                total_msgs=150,
                flagged_msgs=60,
                blocked_msgs=60,
            )
            self.advance_days(1)
        profile = profiler.get_profile("app", "u")
        assert len(profile["summaries"]) == 1
        assert profiler.get_ratio("app", "u") == 0.8
        if profile["summaries"]:
            summary = profile["summaries"][0]
            assert summary["total_msgs"] == 13650
        profiler.close()

    def test_single_cycle_v150_f45_b0_3417(self) -> None:
        """A full window archives totals that match the configured rates."""
        profiler: UserProfiler = UserProfiler(":memory:", ":memory:", 91)
        for _ in range(91):
            profiler.record(
                "app",
                "u",
                total_msgs=150,
                flagged_msgs=68,
                blocked_msgs=0,
            )
            self.advance_days(1)
        profile = profiler.get_profile("app", "u")
        assert len(profile["summaries"]) == 1
        assert profiler.get_ratio("app", "u") == 0.4533333333333333
        if profile["summaries"]:
            summary = profile["summaries"][0]
            assert summary["total_msgs"] == 13650
        profiler.close()

    def test_single_cycle_v150_f50_b25_3418(self) -> None:
        """A full window archives totals that match the configured rates."""
        profiler: UserProfiler = UserProfiler(":memory:", ":memory:", 91)
        for _ in range(91):
            profiler.record(
                "app",
                "u",
                total_msgs=150,
                flagged_msgs=75,
                blocked_msgs=38,
            )
            self.advance_days(1)
        profile = profiler.get_profile("app", "u")
        assert len(profile["summaries"]) == 1
        assert profiler.get_ratio("app", "u") == 0.7533333333333333
        if profile["summaries"]:
            summary = profile["summaries"][0]
            assert summary["total_msgs"] == 13650
        profiler.close()

    def test_single_cycle_v150_f55_b10_3419(self) -> None:
        """A full window archives totals that match the configured rates."""
        profiler: UserProfiler = UserProfiler(":memory:", ":memory:", 91)
        for _ in range(91):
            profiler.record(
                "app",
                "u",
                total_msgs=150,
                flagged_msgs=82,
                blocked_msgs=15,
            )
            self.advance_days(1)
        profile = profiler.get_profile("app", "u")
        assert len(profile["summaries"]) == 1
        assert profiler.get_ratio("app", "u") == 0.6466666666666666
        if profile["summaries"]:
            summary = profile["summaries"][0]
            assert summary["total_msgs"] == 13650
        profiler.close()

    def test_single_cycle_v150_f60_b30_3420(self) -> None:
        """A full window archives totals that match the configured rates."""
        profiler: UserProfiler = UserProfiler(":memory:", ":memory:", 91)
        for _ in range(91):
            profiler.record(
                "app",
                "u",
                total_msgs=150,
                flagged_msgs=90,
                blocked_msgs=45,
            )
            self.advance_days(1)
        profile = profiler.get_profile("app", "u")
        assert len(profile["summaries"]) == 1
        assert profiler.get_ratio("app", "u") == 0.9
        if profile["summaries"]:
            summary = profile["summaries"][0]
            assert summary["total_msgs"] == 13650
        profiler.close()

    def test_single_cycle_v150_f65_b0_3421(self) -> None:
        """A full window archives totals that match the configured rates."""
        profiler: UserProfiler = UserProfiler(":memory:", ":memory:", 91)
        for _ in range(91):
            profiler.record(
                "app",
                "u",
                total_msgs=150,
                flagged_msgs=98,
                blocked_msgs=0,
            )
            self.advance_days(1)
        profile = profiler.get_profile("app", "u")
        assert len(profile["summaries"]) == 1
        assert profiler.get_ratio("app", "u") == 0.6533333333333333
        if profile["summaries"]:
            summary = profile["summaries"][0]
            assert summary["total_msgs"] == 13650
        profiler.close()

    def test_single_cycle_v150_f70_b20_3422(self) -> None:
        """A full window archives totals that match the configured rates."""
        profiler: UserProfiler = UserProfiler(":memory:", ":memory:", 91)
        for _ in range(91):
            profiler.record(
                "app",
                "u",
                total_msgs=150,
                flagged_msgs=105,
                blocked_msgs=30,
            )
            self.advance_days(1)
        profile = profiler.get_profile("app", "u")
        assert len(profile["summaries"]) == 1
        assert profiler.get_ratio("app", "u") == 0.9
        if profile["summaries"]:
            summary = profile["summaries"][0]
            assert summary["total_msgs"] == 13650
        profiler.close()

    def test_single_cycle_v150_f75_b35_3423(self) -> None:
        """A full window archives totals that match the configured rates."""
        profiler: UserProfiler = UserProfiler(":memory:", ":memory:", 91)
        for _ in range(91):
            profiler.record(
                "app",
                "u",
                total_msgs=150,
                flagged_msgs=112,
                blocked_msgs=52,
            )
            self.advance_days(1)
        profile = profiler.get_profile("app", "u")
        assert len(profile["summaries"]) == 1
        assert profiler.get_ratio("app", "u") == 1.0933333333333333
        if profile["summaries"]:
            summary = profile["summaries"][0]
            assert summary["total_msgs"] == 13650
        profiler.close()

    def test_single_cycle_v150_f80_b0_3424(self) -> None:
        """A full window archives totals that match the configured rates."""
        profiler: UserProfiler = UserProfiler(":memory:", ":memory:", 91)
        for _ in range(91):
            profiler.record(
                "app",
                "u",
                total_msgs=150,
                flagged_msgs=120,
                blocked_msgs=0,
            )
            self.advance_days(1)
        profile = profiler.get_profile("app", "u")
        assert len(profile["summaries"]) == 1
        assert profiler.get_ratio("app", "u") == 0.8
        if profile["summaries"]:
            summary = profile["summaries"][0]
            assert summary["total_msgs"] == 13650
        profiler.close()

    def test_single_cycle_v150_f85_b40_3425(self) -> None:
        """A full window archives totals that match the configured rates."""
        profiler: UserProfiler = UserProfiler(":memory:", ":memory:", 91)
        for _ in range(91):
            profiler.record(
                "app",
                "u",
                total_msgs=150,
                flagged_msgs=128,
                blocked_msgs=60,
            )
            self.advance_days(1)
        profile = profiler.get_profile("app", "u")
        assert len(profile["summaries"]) == 1
        assert profiler.get_ratio("app", "u") == 1.2533333333333334
        if profile["summaries"]:
            summary = profile["summaries"][0]
            assert summary["total_msgs"] == 13650
        profiler.close()

    def test_single_cycle_v150_f90_b5_3426(self) -> None:
        """A full window archives totals that match the configured rates."""
        profiler: UserProfiler = UserProfiler(":memory:", ":memory:", 91)
        for _ in range(91):
            profiler.record(
                "app",
                "u",
                total_msgs=150,
                flagged_msgs=135,
                blocked_msgs=8,
            )
            self.advance_days(1)
        profile = profiler.get_profile("app", "u")
        assert len(profile["summaries"]) == 1
        assert profiler.get_ratio("app", "u") == 0.9533333333333334
        if profile["summaries"]:
            summary = profile["summaries"][0]
            assert summary["total_msgs"] == 13650
        profiler.close()

    def test_single_cycle_v150_f95_b10_3427(self) -> None:
        """A full window archives totals that match the configured rates."""
        profiler: UserProfiler = UserProfiler(":memory:", ":memory:", 91)
        for _ in range(91):
            profiler.record(
                "app",
                "u",
                total_msgs=150,
                flagged_msgs=142,
                blocked_msgs=15,
            )
            self.advance_days(1)
        profile = profiler.get_profile("app", "u")
        assert len(profile["summaries"]) == 1
        assert profiler.get_ratio("app", "u") == 1.0466666666666666
        if profile["summaries"]:
            summary = profile["summaries"][0]
            assert summary["total_msgs"] == 13650
        profiler.close()

    def test_single_cycle_v150_f100_b0_3428(self) -> None:
        """A full window archives totals that match the configured rates."""
        profiler: UserProfiler = UserProfiler(":memory:", ":memory:", 91)
        for _ in range(91):
            profiler.record(
                "app",
                "u",
                total_msgs=150,
                flagged_msgs=150,
                blocked_msgs=0,
            )
            self.advance_days(1)
        profile = profiler.get_profile("app", "u")
        assert len(profile["summaries"]) == 1
        assert profiler.get_ratio("app", "u") == 1.0
        if profile["summaries"]:
            summary = profile["summaries"][0]
            assert summary["total_msgs"] == 13650
        profiler.close()

    def test_single_cycle_v300_f0_b0_3429(self) -> None:
        """A full window archives totals that match the configured rates."""
        profiler: UserProfiler = UserProfiler(":memory:", ":memory:", 91)
        for _ in range(91):
            profiler.record(
                "app",
                "u",
                total_msgs=300,
                flagged_msgs=0,
                blocked_msgs=0,
            )
            self.advance_days(1)
        profile = profiler.get_profile("app", "u")
        assert len(profile["summaries"]) == 1
        assert profiler.get_ratio("app", "u") == 0.0
        if profile["summaries"]:
            summary = profile["summaries"][0]
            assert summary["total_msgs"] == 27300
        profiler.close()

    def test_single_cycle_v300_f5_b0_3430(self) -> None:
        """A full window archives totals that match the configured rates."""
        profiler: UserProfiler = UserProfiler(":memory:", ":memory:", 91)
        for _ in range(91):
            profiler.record(
                "app",
                "u",
                total_msgs=300,
                flagged_msgs=15,
                blocked_msgs=0,
            )
            self.advance_days(1)
        profile = profiler.get_profile("app", "u")
        assert len(profile["summaries"]) == 1
        assert profiler.get_ratio("app", "u") == 0.05
        if profile["summaries"]:
            summary = profile["summaries"][0]
            assert summary["total_msgs"] == 27300
        profiler.close()

    def test_single_cycle_v300_f10_b5_3431(self) -> None:
        """A full window archives totals that match the configured rates."""
        profiler: UserProfiler = UserProfiler(":memory:", ":memory:", 91)
        for _ in range(91):
            profiler.record(
                "app",
                "u",
                total_msgs=300,
                flagged_msgs=30,
                blocked_msgs=15,
            )
            self.advance_days(1)
        profile = profiler.get_profile("app", "u")
        assert len(profile["summaries"]) == 1
        assert profiler.get_ratio("app", "u") == 0.15
        if profile["summaries"]:
            summary = profile["summaries"][0]
            assert summary["total_msgs"] == 27300
        profiler.close()

    def test_single_cycle_v300_f15_b10_3432(self) -> None:
        """A full window archives totals that match the configured rates."""
        profiler: UserProfiler = UserProfiler(":memory:", ":memory:", 91)
        for _ in range(91):
            profiler.record(
                "app",
                "u",
                total_msgs=300,
                flagged_msgs=45,
                blocked_msgs=30,
            )
            self.advance_days(1)
        profile = profiler.get_profile("app", "u")
        assert len(profile["summaries"]) == 1
        assert profiler.get_ratio("app", "u") == 0.25
        if profile["summaries"]:
            summary = profile["summaries"][0]
            assert summary["total_msgs"] == 27300
        profiler.close()

    def test_single_cycle_v300_f20_b20_3433(self) -> None:
        """A full window archives totals that match the configured rates."""
        profiler: UserProfiler = UserProfiler(":memory:", ":memory:", 91)
        for _ in range(91):
            profiler.record(
                "app",
                "u",
                total_msgs=300,
                flagged_msgs=60,
                blocked_msgs=60,
            )
            self.advance_days(1)
        profile = profiler.get_profile("app", "u")
        assert len(profile["summaries"]) == 1
        assert profiler.get_ratio("app", "u") == 0.4
        if profile["summaries"]:
            summary = profile["summaries"][0]
            assert summary["total_msgs"] == 27300
        profiler.close()

    def test_single_cycle_v300_f25_b0_3434(self) -> None:
        """A full window archives totals that match the configured rates."""
        profiler: UserProfiler = UserProfiler(":memory:", ":memory:", 91)
        for _ in range(91):
            profiler.record(
                "app",
                "u",
                total_msgs=300,
                flagged_msgs=75,
                blocked_msgs=0,
            )
            self.advance_days(1)
        profile = profiler.get_profile("app", "u")
        assert len(profile["summaries"]) == 1
        assert profiler.get_ratio("app", "u") == 0.25
        if profile["summaries"]:
            summary = profile["summaries"][0]
            assert summary["total_msgs"] == 27300
        profiler.close()

    def test_single_cycle_v300_f30_b15_3435(self) -> None:
        """A full window archives totals that match the configured rates."""
        profiler: UserProfiler = UserProfiler(":memory:", ":memory:", 91)
        for _ in range(91):
            profiler.record(
                "app",
                "u",
                total_msgs=300,
                flagged_msgs=90,
                blocked_msgs=45,
            )
            self.advance_days(1)
        profile = profiler.get_profile("app", "u")
        assert len(profile["summaries"]) == 1
        assert profiler.get_ratio("app", "u") == 0.45
        if profile["summaries"]:
            summary = profile["summaries"][0]
            assert summary["total_msgs"] == 27300
        profiler.close()

    def test_single_cycle_v300_f35_b5_3436(self) -> None:
        """A full window archives totals that match the configured rates."""
        profiler: UserProfiler = UserProfiler(":memory:", ":memory:", 91)
        for _ in range(91):
            profiler.record(
                "app",
                "u",
                total_msgs=300,
                flagged_msgs=105,
                blocked_msgs=15,
            )
            self.advance_days(1)
        profile = profiler.get_profile("app", "u")
        assert len(profile["summaries"]) == 1
        assert profiler.get_ratio("app", "u") == 0.4
        if profile["summaries"]:
            summary = profile["summaries"][0]
            assert summary["total_msgs"] == 27300
        profiler.close()

    def test_single_cycle_v300_f40_b40_3437(self) -> None:
        """A full window archives totals that match the configured rates."""
        profiler: UserProfiler = UserProfiler(":memory:", ":memory:", 91)
        for _ in range(91):
            profiler.record(
                "app",
                "u",
                total_msgs=300,
                flagged_msgs=120,
                blocked_msgs=120,
            )
            self.advance_days(1)
        profile = profiler.get_profile("app", "u")
        assert len(profile["summaries"]) == 1
        assert profiler.get_ratio("app", "u") == 0.8
        if profile["summaries"]:
            summary = profile["summaries"][0]
            assert summary["total_msgs"] == 27300
        profiler.close()

    def test_single_cycle_v300_f45_b0_3438(self) -> None:
        """A full window archives totals that match the configured rates."""
        profiler: UserProfiler = UserProfiler(":memory:", ":memory:", 91)
        for _ in range(91):
            profiler.record(
                "app",
                "u",
                total_msgs=300,
                flagged_msgs=135,
                blocked_msgs=0,
            )
            self.advance_days(1)
        profile = profiler.get_profile("app", "u")
        assert len(profile["summaries"]) == 1
        assert profiler.get_ratio("app", "u") == 0.45
        if profile["summaries"]:
            summary = profile["summaries"][0]
            assert summary["total_msgs"] == 27300
        profiler.close()

    def test_single_cycle_v300_f50_b25_3439(self) -> None:
        """A full window archives totals that match the configured rates."""
        profiler: UserProfiler = UserProfiler(":memory:", ":memory:", 91)
        for _ in range(91):
            profiler.record(
                "app",
                "u",
                total_msgs=300,
                flagged_msgs=150,
                blocked_msgs=75,
            )
            self.advance_days(1)
        profile = profiler.get_profile("app", "u")
        assert len(profile["summaries"]) == 1
        assert profiler.get_ratio("app", "u") == 0.75
        if profile["summaries"]:
            summary = profile["summaries"][0]
            assert summary["total_msgs"] == 27300
        profiler.close()

    def test_single_cycle_v300_f55_b10_3440(self) -> None:
        """A full window archives totals that match the configured rates."""
        profiler: UserProfiler = UserProfiler(":memory:", ":memory:", 91)
        for _ in range(91):
            profiler.record(
                "app",
                "u",
                total_msgs=300,
                flagged_msgs=165,
                blocked_msgs=30,
            )
            self.advance_days(1)
        profile = profiler.get_profile("app", "u")
        assert len(profile["summaries"]) == 1
        assert profiler.get_ratio("app", "u") == 0.65
        if profile["summaries"]:
            summary = profile["summaries"][0]
            assert summary["total_msgs"] == 27300
        profiler.close()

    def test_single_cycle_v300_f60_b30_3441(self) -> None:
        """A full window archives totals that match the configured rates."""
        profiler: UserProfiler = UserProfiler(":memory:", ":memory:", 91)
        for _ in range(91):
            profiler.record(
                "app",
                "u",
                total_msgs=300,
                flagged_msgs=180,
                blocked_msgs=90,
            )
            self.advance_days(1)
        profile = profiler.get_profile("app", "u")
        assert len(profile["summaries"]) == 1
        assert profiler.get_ratio("app", "u") == 0.9
        if profile["summaries"]:
            summary = profile["summaries"][0]
            assert summary["total_msgs"] == 27300
        profiler.close()

    def test_single_cycle_v300_f65_b0_3442(self) -> None:
        """A full window archives totals that match the configured rates."""
        profiler: UserProfiler = UserProfiler(":memory:", ":memory:", 91)
        for _ in range(91):
            profiler.record(
                "app",
                "u",
                total_msgs=300,
                flagged_msgs=195,
                blocked_msgs=0,
            )
            self.advance_days(1)
        profile = profiler.get_profile("app", "u")
        assert len(profile["summaries"]) == 1
        assert profiler.get_ratio("app", "u") == 0.65
        if profile["summaries"]:
            summary = profile["summaries"][0]
            assert summary["total_msgs"] == 27300
        profiler.close()

    def test_single_cycle_v300_f70_b20_3443(self) -> None:
        """A full window archives totals that match the configured rates."""
        profiler: UserProfiler = UserProfiler(":memory:", ":memory:", 91)
        for _ in range(91):
            profiler.record(
                "app",
                "u",
                total_msgs=300,
                flagged_msgs=210,
                blocked_msgs=60,
            )
            self.advance_days(1)
        profile = profiler.get_profile("app", "u")
        assert len(profile["summaries"]) == 1
        assert profiler.get_ratio("app", "u") == 0.9
        if profile["summaries"]:
            summary = profile["summaries"][0]
            assert summary["total_msgs"] == 27300
        profiler.close()

    def test_single_cycle_v300_f75_b35_3444(self) -> None:
        """A full window archives totals that match the configured rates."""
        profiler: UserProfiler = UserProfiler(":memory:", ":memory:", 91)
        for _ in range(91):
            profiler.record(
                "app",
                "u",
                total_msgs=300,
                flagged_msgs=225,
                blocked_msgs=105,
            )
            self.advance_days(1)
        profile = profiler.get_profile("app", "u")
        assert len(profile["summaries"]) == 1
        assert profiler.get_ratio("app", "u") == 1.1
        if profile["summaries"]:
            summary = profile["summaries"][0]
            assert summary["total_msgs"] == 27300
        profiler.close()

    def test_single_cycle_v300_f80_b0_3445(self) -> None:
        """A full window archives totals that match the configured rates."""
        profiler: UserProfiler = UserProfiler(":memory:", ":memory:", 91)
        for _ in range(91):
            profiler.record(
                "app",
                "u",
                total_msgs=300,
                flagged_msgs=240,
                blocked_msgs=0,
            )
            self.advance_days(1)
        profile = profiler.get_profile("app", "u")
        assert len(profile["summaries"]) == 1
        assert profiler.get_ratio("app", "u") == 0.8
        if profile["summaries"]:
            summary = profile["summaries"][0]
            assert summary["total_msgs"] == 27300
        profiler.close()

    def test_single_cycle_v300_f85_b40_3446(self) -> None:
        """A full window archives totals that match the configured rates."""
        profiler: UserProfiler = UserProfiler(":memory:", ":memory:", 91)
        for _ in range(91):
            profiler.record(
                "app",
                "u",
                total_msgs=300,
                flagged_msgs=255,
                blocked_msgs=120,
            )
            self.advance_days(1)
        profile = profiler.get_profile("app", "u")
        assert len(profile["summaries"]) == 1
        assert profiler.get_ratio("app", "u") == 1.25
        if profile["summaries"]:
            summary = profile["summaries"][0]
            assert summary["total_msgs"] == 27300
        profiler.close()

    def test_single_cycle_v300_f90_b5_3447(self) -> None:
        """A full window archives totals that match the configured rates."""
        profiler: UserProfiler = UserProfiler(":memory:", ":memory:", 91)
        for _ in range(91):
            profiler.record(
                "app",
                "u",
                total_msgs=300,
                flagged_msgs=270,
                blocked_msgs=15,
            )
            self.advance_days(1)
        profile = profiler.get_profile("app", "u")
        assert len(profile["summaries"]) == 1
        assert profiler.get_ratio("app", "u") == 0.95
        if profile["summaries"]:
            summary = profile["summaries"][0]
            assert summary["total_msgs"] == 27300
        profiler.close()

    def test_single_cycle_v300_f95_b10_3448(self) -> None:
        """A full window archives totals that match the configured rates."""
        profiler: UserProfiler = UserProfiler(":memory:", ":memory:", 91)
        for _ in range(91):
            profiler.record(
                "app",
                "u",
                total_msgs=300,
                flagged_msgs=285,
                blocked_msgs=30,
            )
            self.advance_days(1)
        profile = profiler.get_profile("app", "u")
        assert len(profile["summaries"]) == 1
        assert profiler.get_ratio("app", "u") == 1.05
        if profile["summaries"]:
            summary = profile["summaries"][0]
            assert summary["total_msgs"] == 27300
        profiler.close()

    def test_single_cycle_v300_f100_b0_3449(self) -> None:
        """A full window archives totals that match the configured rates."""
        profiler: UserProfiler = UserProfiler(":memory:", ":memory:", 91)
        for _ in range(91):
            profiler.record(
                "app",
                "u",
                total_msgs=300,
                flagged_msgs=300,
                blocked_msgs=0,
            )
            self.advance_days(1)
        profile = profiler.get_profile("app", "u")
        assert len(profile["summaries"]) == 1
        assert profiler.get_ratio("app", "u") == 1.0
        if profile["summaries"]:
            summary = profile["summaries"][0]
            assert summary["total_msgs"] == 27300
        profiler.close()

    def test_single_cycle_v800_f0_b0_3450(self) -> None:
        """A full window archives totals that match the configured rates."""
        profiler: UserProfiler = UserProfiler(":memory:", ":memory:", 91)
        for _ in range(91):
            profiler.record(
                "app",
                "u",
                total_msgs=800,
                flagged_msgs=0,
                blocked_msgs=0,
            )
            self.advance_days(1)
        profile = profiler.get_profile("app", "u")
        assert len(profile["summaries"]) == 1
        assert profiler.get_ratio("app", "u") == 0.0
        if profile["summaries"]:
            summary = profile["summaries"][0]
            assert summary["total_msgs"] == 72800
        profiler.close()

    def test_single_cycle_v800_f5_b0_3451(self) -> None:
        """A full window archives totals that match the configured rates."""
        profiler: UserProfiler = UserProfiler(":memory:", ":memory:", 91)
        for _ in range(91):
            profiler.record(
                "app",
                "u",
                total_msgs=800,
                flagged_msgs=40,
                blocked_msgs=0,
            )
            self.advance_days(1)
        profile = profiler.get_profile("app", "u")
        assert len(profile["summaries"]) == 1
        assert profiler.get_ratio("app", "u") == 0.05
        if profile["summaries"]:
            summary = profile["summaries"][0]
            assert summary["total_msgs"] == 72800
        profiler.close()

    def test_single_cycle_v800_f10_b5_3452(self) -> None:
        """A full window archives totals that match the configured rates."""
        profiler: UserProfiler = UserProfiler(":memory:", ":memory:", 91)
        for _ in range(91):
            profiler.record(
                "app",
                "u",
                total_msgs=800,
                flagged_msgs=80,
                blocked_msgs=40,
            )
            self.advance_days(1)
        profile = profiler.get_profile("app", "u")
        assert len(profile["summaries"]) == 1
        assert profiler.get_ratio("app", "u") == 0.15
        if profile["summaries"]:
            summary = profile["summaries"][0]
            assert summary["total_msgs"] == 72800
        profiler.close()

    def test_single_cycle_v800_f15_b10_3453(self) -> None:
        """A full window archives totals that match the configured rates."""
        profiler: UserProfiler = UserProfiler(":memory:", ":memory:", 91)
        for _ in range(91):
            profiler.record(
                "app",
                "u",
                total_msgs=800,
                flagged_msgs=120,
                blocked_msgs=80,
            )
            self.advance_days(1)
        profile = profiler.get_profile("app", "u")
        assert len(profile["summaries"]) == 1
        assert profiler.get_ratio("app", "u") == 0.25
        if profile["summaries"]:
            summary = profile["summaries"][0]
            assert summary["total_msgs"] == 72800
        profiler.close()

    def test_single_cycle_v800_f20_b20_3454(self) -> None:
        """A full window archives totals that match the configured rates."""
        profiler: UserProfiler = UserProfiler(":memory:", ":memory:", 91)
        for _ in range(91):
            profiler.record(
                "app",
                "u",
                total_msgs=800,
                flagged_msgs=160,
                blocked_msgs=160,
            )
            self.advance_days(1)
        profile = profiler.get_profile("app", "u")
        assert len(profile["summaries"]) == 1
        assert profiler.get_ratio("app", "u") == 0.4
        if profile["summaries"]:
            summary = profile["summaries"][0]
            assert summary["total_msgs"] == 72800
        profiler.close()

    def test_single_cycle_v800_f25_b0_3455(self) -> None:
        """A full window archives totals that match the configured rates."""
        profiler: UserProfiler = UserProfiler(":memory:", ":memory:", 91)
        for _ in range(91):
            profiler.record(
                "app",
                "u",
                total_msgs=800,
                flagged_msgs=200,
                blocked_msgs=0,
            )
            self.advance_days(1)
        profile = profiler.get_profile("app", "u")
        assert len(profile["summaries"]) == 1
        assert profiler.get_ratio("app", "u") == 0.25
        if profile["summaries"]:
            summary = profile["summaries"][0]
            assert summary["total_msgs"] == 72800
        profiler.close()

    def test_single_cycle_v800_f30_b15_3456(self) -> None:
        """A full window archives totals that match the configured rates."""
        profiler: UserProfiler = UserProfiler(":memory:", ":memory:", 91)
        for _ in range(91):
            profiler.record(
                "app",
                "u",
                total_msgs=800,
                flagged_msgs=240,
                blocked_msgs=120,
            )
            self.advance_days(1)
        profile = profiler.get_profile("app", "u")
        assert len(profile["summaries"]) == 1
        assert profiler.get_ratio("app", "u") == 0.45
        if profile["summaries"]:
            summary = profile["summaries"][0]
            assert summary["total_msgs"] == 72800
        profiler.close()

    def test_single_cycle_v800_f35_b5_3457(self) -> None:
        """A full window archives totals that match the configured rates."""
        profiler: UserProfiler = UserProfiler(":memory:", ":memory:", 91)
        for _ in range(91):
            profiler.record(
                "app",
                "u",
                total_msgs=800,
                flagged_msgs=280,
                blocked_msgs=40,
            )
            self.advance_days(1)
        profile = profiler.get_profile("app", "u")
        assert len(profile["summaries"]) == 1
        assert profiler.get_ratio("app", "u") == 0.4
        if profile["summaries"]:
            summary = profile["summaries"][0]
            assert summary["total_msgs"] == 72800
        profiler.close()

    def test_single_cycle_v800_f40_b40_3458(self) -> None:
        """A full window archives totals that match the configured rates."""
        profiler: UserProfiler = UserProfiler(":memory:", ":memory:", 91)
        for _ in range(91):
            profiler.record(
                "app",
                "u",
                total_msgs=800,
                flagged_msgs=320,
                blocked_msgs=320,
            )
            self.advance_days(1)
        profile = profiler.get_profile("app", "u")
        assert len(profile["summaries"]) == 1
        assert profiler.get_ratio("app", "u") == 0.8
        if profile["summaries"]:
            summary = profile["summaries"][0]
            assert summary["total_msgs"] == 72800
        profiler.close()

    def test_single_cycle_v800_f45_b0_3459(self) -> None:
        """A full window archives totals that match the configured rates."""
        profiler: UserProfiler = UserProfiler(":memory:", ":memory:", 91)
        for _ in range(91):
            profiler.record(
                "app",
                "u",
                total_msgs=800,
                flagged_msgs=360,
                blocked_msgs=0,
            )
            self.advance_days(1)
        profile = profiler.get_profile("app", "u")
        assert len(profile["summaries"]) == 1
        assert profiler.get_ratio("app", "u") == 0.45
        if profile["summaries"]:
            summary = profile["summaries"][0]
            assert summary["total_msgs"] == 72800
        profiler.close()

    def test_single_cycle_v800_f50_b25_3460(self) -> None:
        """A full window archives totals that match the configured rates."""
        profiler: UserProfiler = UserProfiler(":memory:", ":memory:", 91)
        for _ in range(91):
            profiler.record(
                "app",
                "u",
                total_msgs=800,
                flagged_msgs=400,
                blocked_msgs=200,
            )
            self.advance_days(1)
        profile = profiler.get_profile("app", "u")
        assert len(profile["summaries"]) == 1
        assert profiler.get_ratio("app", "u") == 0.75
        if profile["summaries"]:
            summary = profile["summaries"][0]
            assert summary["total_msgs"] == 72800
        profiler.close()

    def test_single_cycle_v800_f55_b10_3461(self) -> None:
        """A full window archives totals that match the configured rates."""
        profiler: UserProfiler = UserProfiler(":memory:", ":memory:", 91)
        for _ in range(91):
            profiler.record(
                "app",
                "u",
                total_msgs=800,
                flagged_msgs=440,
                blocked_msgs=80,
            )
            self.advance_days(1)
        profile = profiler.get_profile("app", "u")
        assert len(profile["summaries"]) == 1
        assert profiler.get_ratio("app", "u") == 0.65
        if profile["summaries"]:
            summary = profile["summaries"][0]
            assert summary["total_msgs"] == 72800
        profiler.close()

    def test_single_cycle_v800_f60_b30_3462(self) -> None:
        """A full window archives totals that match the configured rates."""
        profiler: UserProfiler = UserProfiler(":memory:", ":memory:", 91)
        for _ in range(91):
            profiler.record(
                "app",
                "u",
                total_msgs=800,
                flagged_msgs=480,
                blocked_msgs=240,
            )
            self.advance_days(1)
        profile = profiler.get_profile("app", "u")
        assert len(profile["summaries"]) == 1
        assert profiler.get_ratio("app", "u") == 0.9
        if profile["summaries"]:
            summary = profile["summaries"][0]
            assert summary["total_msgs"] == 72800
        profiler.close()

    def test_single_cycle_v800_f65_b0_3463(self) -> None:
        """A full window archives totals that match the configured rates."""
        profiler: UserProfiler = UserProfiler(":memory:", ":memory:", 91)
        for _ in range(91):
            profiler.record(
                "app",
                "u",
                total_msgs=800,
                flagged_msgs=520,
                blocked_msgs=0,
            )
            self.advance_days(1)
        profile = profiler.get_profile("app", "u")
        assert len(profile["summaries"]) == 1
        assert profiler.get_ratio("app", "u") == 0.65
        if profile["summaries"]:
            summary = profile["summaries"][0]
            assert summary["total_msgs"] == 72800
        profiler.close()

    def test_single_cycle_v800_f70_b20_3464(self) -> None:
        """A full window archives totals that match the configured rates."""
        profiler: UserProfiler = UserProfiler(":memory:", ":memory:", 91)
        for _ in range(91):
            profiler.record(
                "app",
                "u",
                total_msgs=800,
                flagged_msgs=560,
                blocked_msgs=160,
            )
            self.advance_days(1)
        profile = profiler.get_profile("app", "u")
        assert len(profile["summaries"]) == 1
        assert profiler.get_ratio("app", "u") == 0.9
        if profile["summaries"]:
            summary = profile["summaries"][0]
            assert summary["total_msgs"] == 72800
        profiler.close()

    def test_single_cycle_v800_f75_b35_3465(self) -> None:
        """A full window archives totals that match the configured rates."""
        profiler: UserProfiler = UserProfiler(":memory:", ":memory:", 91)
        for _ in range(91):
            profiler.record(
                "app",
                "u",
                total_msgs=800,
                flagged_msgs=600,
                blocked_msgs=280,
            )
            self.advance_days(1)
        profile = profiler.get_profile("app", "u")
        assert len(profile["summaries"]) == 1
        assert profiler.get_ratio("app", "u") == 1.1
        if profile["summaries"]:
            summary = profile["summaries"][0]
            assert summary["total_msgs"] == 72800
        profiler.close()

    def test_single_cycle_v800_f80_b0_3466(self) -> None:
        """A full window archives totals that match the configured rates."""
        profiler: UserProfiler = UserProfiler(":memory:", ":memory:", 91)
        for _ in range(91):
            profiler.record(
                "app",
                "u",
                total_msgs=800,
                flagged_msgs=640,
                blocked_msgs=0,
            )
            self.advance_days(1)
        profile = profiler.get_profile("app", "u")
        assert len(profile["summaries"]) == 1
        assert profiler.get_ratio("app", "u") == 0.8
        if profile["summaries"]:
            summary = profile["summaries"][0]
            assert summary["total_msgs"] == 72800
        profiler.close()

    def test_single_cycle_v800_f85_b40_3467(self) -> None:
        """A full window archives totals that match the configured rates."""
        profiler: UserProfiler = UserProfiler(":memory:", ":memory:", 91)
        for _ in range(91):
            profiler.record(
                "app",
                "u",
                total_msgs=800,
                flagged_msgs=680,
                blocked_msgs=320,
            )
            self.advance_days(1)
        profile = profiler.get_profile("app", "u")
        assert len(profile["summaries"]) == 1
        assert profiler.get_ratio("app", "u") == 1.25
        if profile["summaries"]:
            summary = profile["summaries"][0]
            assert summary["total_msgs"] == 72800
        profiler.close()

    def test_single_cycle_v800_f90_b5_3468(self) -> None:
        """A full window archives totals that match the configured rates."""
        profiler: UserProfiler = UserProfiler(":memory:", ":memory:", 91)
        for _ in range(91):
            profiler.record(
                "app",
                "u",
                total_msgs=800,
                flagged_msgs=720,
                blocked_msgs=40,
            )
            self.advance_days(1)
        profile = profiler.get_profile("app", "u")
        assert len(profile["summaries"]) == 1
        assert profiler.get_ratio("app", "u") == 0.95
        if profile["summaries"]:
            summary = profile["summaries"][0]
            assert summary["total_msgs"] == 72800
        profiler.close()

    def test_single_cycle_v800_f95_b10_3469(self) -> None:
        """A full window archives totals that match the configured rates."""
        profiler: UserProfiler = UserProfiler(":memory:", ":memory:", 91)
        for _ in range(91):
            profiler.record(
                "app",
                "u",
                total_msgs=800,
                flagged_msgs=760,
                blocked_msgs=80,
            )
            self.advance_days(1)
        profile = profiler.get_profile("app", "u")
        assert len(profile["summaries"]) == 1
        assert profiler.get_ratio("app", "u") == 1.05
        if profile["summaries"]:
            summary = profile["summaries"][0]
            assert summary["total_msgs"] == 72800
        profiler.close()

    def test_single_cycle_v800_f100_b0_3470(self) -> None:
        """A full window archives totals that match the configured rates."""
        profiler: UserProfiler = UserProfiler(":memory:", ":memory:", 91)
        for _ in range(91):
            profiler.record(
                "app",
                "u",
                total_msgs=800,
                flagged_msgs=800,
                blocked_msgs=0,
            )
            self.advance_days(1)
        profile = profiler.get_profile("app", "u")
        assert len(profile["summaries"]) == 1
        assert profiler.get_ratio("app", "u") == 1.0
        if profile["summaries"]:
            summary = profile["summaries"][0]
            assert summary["total_msgs"] == 72800
        profiler.close()

    def test_single_cycle_v1500_f0_b0_3471(self) -> None:
        """A full window archives totals that match the configured rates."""
        profiler: UserProfiler = UserProfiler(":memory:", ":memory:", 91)
        for _ in range(91):
            profiler.record(
                "app",
                "u",
                total_msgs=1500,
                flagged_msgs=0,
                blocked_msgs=0,
            )
            self.advance_days(1)
        profile = profiler.get_profile("app", "u")
        assert len(profile["summaries"]) == 1
        assert profiler.get_ratio("app", "u") == 0.0
        if profile["summaries"]:
            summary = profile["summaries"][0]
            assert summary["total_msgs"] == 136500
        profiler.close()

    def test_single_cycle_v1500_f5_b0_3472(self) -> None:
        """A full window archives totals that match the configured rates."""
        profiler: UserProfiler = UserProfiler(":memory:", ":memory:", 91)
        for _ in range(91):
            profiler.record(
                "app",
                "u",
                total_msgs=1500,
                flagged_msgs=75,
                blocked_msgs=0,
            )
            self.advance_days(1)
        profile = profiler.get_profile("app", "u")
        assert len(profile["summaries"]) == 1
        assert profiler.get_ratio("app", "u") == 0.05
        if profile["summaries"]:
            summary = profile["summaries"][0]
            assert summary["total_msgs"] == 136500
        profiler.close()

    def test_single_cycle_v1500_f10_b5_3473(self) -> None:
        """A full window archives totals that match the configured rates."""
        profiler: UserProfiler = UserProfiler(":memory:", ":memory:", 91)
        for _ in range(91):
            profiler.record(
                "app",
                "u",
                total_msgs=1500,
                flagged_msgs=150,
                blocked_msgs=75,
            )
            self.advance_days(1)
        profile = profiler.get_profile("app", "u")
        assert len(profile["summaries"]) == 1
        assert profiler.get_ratio("app", "u") == 0.15
        if profile["summaries"]:
            summary = profile["summaries"][0]
            assert summary["total_msgs"] == 136500
        profiler.close()

    def test_single_cycle_v1500_f15_b10_3474(self) -> None:
        """A full window archives totals that match the configured rates."""
        profiler: UserProfiler = UserProfiler(":memory:", ":memory:", 91)
        for _ in range(91):
            profiler.record(
                "app",
                "u",
                total_msgs=1500,
                flagged_msgs=225,
                blocked_msgs=150,
            )
            self.advance_days(1)
        profile = profiler.get_profile("app", "u")
        assert len(profile["summaries"]) == 1
        assert profiler.get_ratio("app", "u") == 0.25
        if profile["summaries"]:
            summary = profile["summaries"][0]
            assert summary["total_msgs"] == 136500
        profiler.close()

    def test_single_cycle_v1500_f20_b20_3475(self) -> None:
        """A full window archives totals that match the configured rates."""
        profiler: UserProfiler = UserProfiler(":memory:", ":memory:", 91)
        for _ in range(91):
            profiler.record(
                "app",
                "u",
                total_msgs=1500,
                flagged_msgs=300,
                blocked_msgs=300,
            )
            self.advance_days(1)
        profile = profiler.get_profile("app", "u")
        assert len(profile["summaries"]) == 1
        assert profiler.get_ratio("app", "u") == 0.4
        if profile["summaries"]:
            summary = profile["summaries"][0]
            assert summary["total_msgs"] == 136500
        profiler.close()

    def test_single_cycle_v1500_f25_b0_3476(self) -> None:
        """A full window archives totals that match the configured rates."""
        profiler: UserProfiler = UserProfiler(":memory:", ":memory:", 91)
        for _ in range(91):
            profiler.record(
                "app",
                "u",
                total_msgs=1500,
                flagged_msgs=375,
                blocked_msgs=0,
            )
            self.advance_days(1)
        profile = profiler.get_profile("app", "u")
        assert len(profile["summaries"]) == 1
        assert profiler.get_ratio("app", "u") == 0.25
        if profile["summaries"]:
            summary = profile["summaries"][0]
            assert summary["total_msgs"] == 136500
        profiler.close()

    def test_single_cycle_v1500_f30_b15_3477(self) -> None:
        """A full window archives totals that match the configured rates."""
        profiler: UserProfiler = UserProfiler(":memory:", ":memory:", 91)
        for _ in range(91):
            profiler.record(
                "app",
                "u",
                total_msgs=1500,
                flagged_msgs=450,
                blocked_msgs=225,
            )
            self.advance_days(1)
        profile = profiler.get_profile("app", "u")
        assert len(profile["summaries"]) == 1
        assert profiler.get_ratio("app", "u") == 0.45
        if profile["summaries"]:
            summary = profile["summaries"][0]
            assert summary["total_msgs"] == 136500
        profiler.close()

    def test_single_cycle_v1500_f35_b5_3478(self) -> None:
        """A full window archives totals that match the configured rates."""
        profiler: UserProfiler = UserProfiler(":memory:", ":memory:", 91)
        for _ in range(91):
            profiler.record(
                "app",
                "u",
                total_msgs=1500,
                flagged_msgs=525,
                blocked_msgs=75,
            )
            self.advance_days(1)
        profile = profiler.get_profile("app", "u")
        assert len(profile["summaries"]) == 1
        assert profiler.get_ratio("app", "u") == 0.4
        if profile["summaries"]:
            summary = profile["summaries"][0]
            assert summary["total_msgs"] == 136500
        profiler.close()

    def test_single_cycle_v1500_f40_b40_3479(self) -> None:
        """A full window archives totals that match the configured rates."""
        profiler: UserProfiler = UserProfiler(":memory:", ":memory:", 91)
        for _ in range(91):
            profiler.record(
                "app",
                "u",
                total_msgs=1500,
                flagged_msgs=600,
                blocked_msgs=600,
            )
            self.advance_days(1)
        profile = profiler.get_profile("app", "u")
        assert len(profile["summaries"]) == 1
        assert profiler.get_ratio("app", "u") == 0.8
        if profile["summaries"]:
            summary = profile["summaries"][0]
            assert summary["total_msgs"] == 136500
        profiler.close()

    def test_single_cycle_v1500_f45_b0_3480(self) -> None:
        """A full window archives totals that match the configured rates."""
        profiler: UserProfiler = UserProfiler(":memory:", ":memory:", 91)
        for _ in range(91):
            profiler.record(
                "app",
                "u",
                total_msgs=1500,
                flagged_msgs=675,
                blocked_msgs=0,
            )
            self.advance_days(1)
        profile = profiler.get_profile("app", "u")
        assert len(profile["summaries"]) == 1
        assert profiler.get_ratio("app", "u") == 0.45
        if profile["summaries"]:
            summary = profile["summaries"][0]
            assert summary["total_msgs"] == 136500
        profiler.close()

    def test_single_cycle_v1500_f50_b25_3481(self) -> None:
        """A full window archives totals that match the configured rates."""
        profiler: UserProfiler = UserProfiler(":memory:", ":memory:", 91)
        for _ in range(91):
            profiler.record(
                "app",
                "u",
                total_msgs=1500,
                flagged_msgs=750,
                blocked_msgs=375,
            )
            self.advance_days(1)
        profile = profiler.get_profile("app", "u")
        assert len(profile["summaries"]) == 1
        assert profiler.get_ratio("app", "u") == 0.75
        if profile["summaries"]:
            summary = profile["summaries"][0]
            assert summary["total_msgs"] == 136500
        profiler.close()

    def test_single_cycle_v1500_f55_b10_3482(self) -> None:
        """A full window archives totals that match the configured rates."""
        profiler: UserProfiler = UserProfiler(":memory:", ":memory:", 91)
        for _ in range(91):
            profiler.record(
                "app",
                "u",
                total_msgs=1500,
                flagged_msgs=825,
                blocked_msgs=150,
            )
            self.advance_days(1)
        profile = profiler.get_profile("app", "u")
        assert len(profile["summaries"]) == 1
        assert profiler.get_ratio("app", "u") == 0.65
        if profile["summaries"]:
            summary = profile["summaries"][0]
            assert summary["total_msgs"] == 136500
        profiler.close()

    def test_single_cycle_v1500_f60_b30_3483(self) -> None:
        """A full window archives totals that match the configured rates."""
        profiler: UserProfiler = UserProfiler(":memory:", ":memory:", 91)
        for _ in range(91):
            profiler.record(
                "app",
                "u",
                total_msgs=1500,
                flagged_msgs=900,
                blocked_msgs=450,
            )
            self.advance_days(1)
        profile = profiler.get_profile("app", "u")
        assert len(profile["summaries"]) == 1
        assert profiler.get_ratio("app", "u") == 0.9
        if profile["summaries"]:
            summary = profile["summaries"][0]
            assert summary["total_msgs"] == 136500
        profiler.close()

    def test_single_cycle_v1500_f65_b0_3484(self) -> None:
        """A full window archives totals that match the configured rates."""
        profiler: UserProfiler = UserProfiler(":memory:", ":memory:", 91)
        for _ in range(91):
            profiler.record(
                "app",
                "u",
                total_msgs=1500,
                flagged_msgs=975,
                blocked_msgs=0,
            )
            self.advance_days(1)
        profile = profiler.get_profile("app", "u")
        assert len(profile["summaries"]) == 1
        assert profiler.get_ratio("app", "u") == 0.65
        if profile["summaries"]:
            summary = profile["summaries"][0]
            assert summary["total_msgs"] == 136500
        profiler.close()

    def test_single_cycle_v1500_f70_b20_3485(self) -> None:
        """A full window archives totals that match the configured rates."""
        profiler: UserProfiler = UserProfiler(":memory:", ":memory:", 91)
        for _ in range(91):
            profiler.record(
                "app",
                "u",
                total_msgs=1500,
                flagged_msgs=1050,
                blocked_msgs=300,
            )
            self.advance_days(1)
        profile = profiler.get_profile("app", "u")
        assert len(profile["summaries"]) == 1
        assert profiler.get_ratio("app", "u") == 0.9
        if profile["summaries"]:
            summary = profile["summaries"][0]
            assert summary["total_msgs"] == 136500
        profiler.close()

    def test_single_cycle_v1500_f75_b35_3486(self) -> None:
        """A full window archives totals that match the configured rates."""
        profiler: UserProfiler = UserProfiler(":memory:", ":memory:", 91)
        for _ in range(91):
            profiler.record(
                "app",
                "u",
                total_msgs=1500,
                flagged_msgs=1125,
                blocked_msgs=525,
            )
            self.advance_days(1)
        profile = profiler.get_profile("app", "u")
        assert len(profile["summaries"]) == 1
        assert profiler.get_ratio("app", "u") == 1.1
        if profile["summaries"]:
            summary = profile["summaries"][0]
            assert summary["total_msgs"] == 136500
        profiler.close()

    def test_single_cycle_v1500_f80_b0_3487(self) -> None:
        """A full window archives totals that match the configured rates."""
        profiler: UserProfiler = UserProfiler(":memory:", ":memory:", 91)
        for _ in range(91):
            profiler.record(
                "app",
                "u",
                total_msgs=1500,
                flagged_msgs=1200,
                blocked_msgs=0,
            )
            self.advance_days(1)
        profile = profiler.get_profile("app", "u")
        assert len(profile["summaries"]) == 1
        assert profiler.get_ratio("app", "u") == 0.8
        if profile["summaries"]:
            summary = profile["summaries"][0]
            assert summary["total_msgs"] == 136500
        profiler.close()

    def test_single_cycle_v1500_f85_b40_3488(self) -> None:
        """A full window archives totals that match the configured rates."""
        profiler: UserProfiler = UserProfiler(":memory:", ":memory:", 91)
        for _ in range(91):
            profiler.record(
                "app",
                "u",
                total_msgs=1500,
                flagged_msgs=1275,
                blocked_msgs=600,
            )
            self.advance_days(1)
        profile = profiler.get_profile("app", "u")
        assert len(profile["summaries"]) == 1
        assert profiler.get_ratio("app", "u") == 1.25
        if profile["summaries"]:
            summary = profile["summaries"][0]
            assert summary["total_msgs"] == 136500
        profiler.close()

    def test_single_cycle_v1500_f90_b5_3489(self) -> None:
        """A full window archives totals that match the configured rates."""
        profiler: UserProfiler = UserProfiler(":memory:", ":memory:", 91)
        for _ in range(91):
            profiler.record(
                "app",
                "u",
                total_msgs=1500,
                flagged_msgs=1350,
                blocked_msgs=75,
            )
            self.advance_days(1)
        profile = profiler.get_profile("app", "u")
        assert len(profile["summaries"]) == 1
        assert profiler.get_ratio("app", "u") == 0.95
        if profile["summaries"]:
            summary = profile["summaries"][0]
            assert summary["total_msgs"] == 136500
        profiler.close()

    def test_single_cycle_v1500_f95_b10_3490(self) -> None:
        """A full window archives totals that match the configured rates."""
        profiler: UserProfiler = UserProfiler(":memory:", ":memory:", 91)
        for _ in range(91):
            profiler.record(
                "app",
                "u",
                total_msgs=1500,
                flagged_msgs=1425,
                blocked_msgs=150,
            )
            self.advance_days(1)
        profile = profiler.get_profile("app", "u")
        assert len(profile["summaries"]) == 1
        assert profiler.get_ratio("app", "u") == 1.05
        if profile["summaries"]:
            summary = profile["summaries"][0]
            assert summary["total_msgs"] == 136500
        profiler.close()

    def test_single_cycle_v1500_f100_b0_3491(self) -> None:
        """A full window archives totals that match the configured rates."""
        profiler: UserProfiler = UserProfiler(":memory:", ":memory:", 91)
        for _ in range(91):
            profiler.record(
                "app",
                "u",
                total_msgs=1500,
                flagged_msgs=1500,
                blocked_msgs=0,
            )
            self.advance_days(1)
        profile = profiler.get_profile("app", "u")
        assert len(profile["summaries"]) == 1
        assert profiler.get_ratio("app", "u") == 1.0
        if profile["summaries"]:
            summary = profile["summaries"][0]
            assert summary["total_msgs"] == 136500
        profiler.close()

    def test_single_cycle_v3000_f0_b0_3492(self) -> None:
        """A full window archives totals that match the configured rates."""
        profiler: UserProfiler = UserProfiler(":memory:", ":memory:", 91)
        for _ in range(91):
            profiler.record(
                "app",
                "u",
                total_msgs=3000,
                flagged_msgs=0,
                blocked_msgs=0,
            )
            self.advance_days(1)
        profile = profiler.get_profile("app", "u")
        assert len(profile["summaries"]) == 1
        assert profiler.get_ratio("app", "u") == 0.0
        if profile["summaries"]:
            summary = profile["summaries"][0]
            assert summary["total_msgs"] == 273000
        profiler.close()

    def test_single_cycle_v3000_f5_b0_3493(self) -> None:
        """A full window archives totals that match the configured rates."""
        profiler: UserProfiler = UserProfiler(":memory:", ":memory:", 91)
        for _ in range(91):
            profiler.record(
                "app",
                "u",
                total_msgs=3000,
                flagged_msgs=150,
                blocked_msgs=0,
            )
            self.advance_days(1)
        profile = profiler.get_profile("app", "u")
        assert len(profile["summaries"]) == 1
        assert profiler.get_ratio("app", "u") == 0.05
        if profile["summaries"]:
            summary = profile["summaries"][0]
            assert summary["total_msgs"] == 273000
        profiler.close()

    def test_single_cycle_v3000_f10_b5_3494(self) -> None:
        """A full window archives totals that match the configured rates."""
        profiler: UserProfiler = UserProfiler(":memory:", ":memory:", 91)
        for _ in range(91):
            profiler.record(
                "app",
                "u",
                total_msgs=3000,
                flagged_msgs=300,
                blocked_msgs=150,
            )
            self.advance_days(1)
        profile = profiler.get_profile("app", "u")
        assert len(profile["summaries"]) == 1
        assert profiler.get_ratio("app", "u") == 0.15
        if profile["summaries"]:
            summary = profile["summaries"][0]
            assert summary["total_msgs"] == 273000
        profiler.close()

    def test_single_cycle_v3000_f15_b10_3495(self) -> None:
        """A full window archives totals that match the configured rates."""
        profiler: UserProfiler = UserProfiler(":memory:", ":memory:", 91)
        for _ in range(91):
            profiler.record(
                "app",
                "u",
                total_msgs=3000,
                flagged_msgs=450,
                blocked_msgs=300,
            )
            self.advance_days(1)
        profile = profiler.get_profile("app", "u")
        assert len(profile["summaries"]) == 1
        assert profiler.get_ratio("app", "u") == 0.25
        if profile["summaries"]:
            summary = profile["summaries"][0]
            assert summary["total_msgs"] == 273000
        profiler.close()

    def test_single_cycle_v3000_f20_b20_3496(self) -> None:
        """A full window archives totals that match the configured rates."""
        profiler: UserProfiler = UserProfiler(":memory:", ":memory:", 91)
        for _ in range(91):
            profiler.record(
                "app",
                "u",
                total_msgs=3000,
                flagged_msgs=600,
                blocked_msgs=600,
            )
            self.advance_days(1)
        profile = profiler.get_profile("app", "u")
        assert len(profile["summaries"]) == 1
        assert profiler.get_ratio("app", "u") == 0.4
        if profile["summaries"]:
            summary = profile["summaries"][0]
            assert summary["total_msgs"] == 273000
        profiler.close()

    def test_single_cycle_v3000_f25_b0_3497(self) -> None:
        """A full window archives totals that match the configured rates."""
        profiler: UserProfiler = UserProfiler(":memory:", ":memory:", 91)
        for _ in range(91):
            profiler.record(
                "app",
                "u",
                total_msgs=3000,
                flagged_msgs=750,
                blocked_msgs=0,
            )
            self.advance_days(1)
        profile = profiler.get_profile("app", "u")
        assert len(profile["summaries"]) == 1
        assert profiler.get_ratio("app", "u") == 0.25
        if profile["summaries"]:
            summary = profile["summaries"][0]
            assert summary["total_msgs"] == 273000
        profiler.close()

    def test_single_cycle_v3000_f30_b15_3498(self) -> None:
        """A full window archives totals that match the configured rates."""
        profiler: UserProfiler = UserProfiler(":memory:", ":memory:", 91)
        for _ in range(91):
            profiler.record(
                "app",
                "u",
                total_msgs=3000,
                flagged_msgs=900,
                blocked_msgs=450,
            )
            self.advance_days(1)
        profile = profiler.get_profile("app", "u")
        assert len(profile["summaries"]) == 1
        assert profiler.get_ratio("app", "u") == 0.45
        if profile["summaries"]:
            summary = profile["summaries"][0]
            assert summary["total_msgs"] == 273000
        profiler.close()

    def test_single_cycle_v3000_f35_b5_3499(self) -> None:
        """A full window archives totals that match the configured rates."""
        profiler: UserProfiler = UserProfiler(":memory:", ":memory:", 91)
        for _ in range(91):
            profiler.record(
                "app",
                "u",
                total_msgs=3000,
                flagged_msgs=1050,
                blocked_msgs=150,
            )
            self.advance_days(1)
        profile = profiler.get_profile("app", "u")
        assert len(profile["summaries"]) == 1
        assert profiler.get_ratio("app", "u") == 0.4
        if profile["summaries"]:
            summary = profile["summaries"][0]
            assert summary["total_msgs"] == 273000
        profiler.close()

    def test_single_cycle_v3000_f40_b40_3500(self) -> None:
        """A full window archives totals that match the configured rates."""
        profiler: UserProfiler = UserProfiler(":memory:", ":memory:", 91)
        for _ in range(91):
            profiler.record(
                "app",
                "u",
                total_msgs=3000,
                flagged_msgs=1200,
                blocked_msgs=1200,
            )
            self.advance_days(1)
        profile = profiler.get_profile("app", "u")
        assert len(profile["summaries"]) == 1
        assert profiler.get_ratio("app", "u") == 0.8
        if profile["summaries"]:
            summary = profile["summaries"][0]
            assert summary["total_msgs"] == 273000
        profiler.close()

    def test_single_cycle_v3000_f45_b0_3501(self) -> None:
        """A full window archives totals that match the configured rates."""
        profiler: UserProfiler = UserProfiler(":memory:", ":memory:", 91)
        for _ in range(91):
            profiler.record(
                "app",
                "u",
                total_msgs=3000,
                flagged_msgs=1350,
                blocked_msgs=0,
            )
            self.advance_days(1)
        profile = profiler.get_profile("app", "u")
        assert len(profile["summaries"]) == 1
        assert profiler.get_ratio("app", "u") == 0.45
        if profile["summaries"]:
            summary = profile["summaries"][0]
            assert summary["total_msgs"] == 273000
        profiler.close()

    def test_single_cycle_v3000_f50_b25_3502(self) -> None:
        """A full window archives totals that match the configured rates."""
        profiler: UserProfiler = UserProfiler(":memory:", ":memory:", 91)
        for _ in range(91):
            profiler.record(
                "app",
                "u",
                total_msgs=3000,
                flagged_msgs=1500,
                blocked_msgs=750,
            )
            self.advance_days(1)
        profile = profiler.get_profile("app", "u")
        assert len(profile["summaries"]) == 1
        assert profiler.get_ratio("app", "u") == 0.75
        if profile["summaries"]:
            summary = profile["summaries"][0]
            assert summary["total_msgs"] == 273000
        profiler.close()
