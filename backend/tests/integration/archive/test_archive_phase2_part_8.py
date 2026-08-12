"""Phase 2 archive cycle tests (generated).

Volume and percentage matrices, multi-cycle chains, multi-user/app
archives and boundary edges under the frozen clock."""

# multilingual fixtures use non-ASCII on purpose
from __future__ import annotations

from app.profiling.user_profiler import UserProfiler
from tests.base_test import BaseTest


class TestMixedArchive(BaseTest):
    """MixedArchive scenarios."""

    def test_mixed_v10_f60_b30_r5_4009(self) -> None:
        """Mixed-verdict windows archive each counter correctly."""
        profiler: UserProfiler = UserProfiler(":memory:", ":memory:", 91)
        for _ in range(91):
            profiler.record(
                "app",
                "u",
                total_msgs=10,
                flagged_msgs=6,
                blocked_msgs=3,
                reviewed_msgs=0,
            )
            self.advance_days(1)
        profile = profiler.get_profile("app", "u")
        assert len(profile["summaries"]) == 1
        assert profiler.get_ratio("app", "u") == 0.9
        profiler.close()

    def test_mixed_v20_f60_b30_r5_4010(self) -> None:
        """Mixed-verdict windows archive each counter correctly."""
        profiler: UserProfiler = UserProfiler(":memory:", ":memory:", 91)
        for _ in range(91):
            profiler.record(
                "app",
                "u",
                total_msgs=20,
                flagged_msgs=12,
                blocked_msgs=6,
                reviewed_msgs=1,
            )
            self.advance_days(1)
        profile = profiler.get_profile("app", "u")
        assert len(profile["summaries"]) == 1
        assert profiler.get_ratio("app", "u") == 0.9
        profiler.close()

    def test_mixed_v50_f60_b30_r5_4011(self) -> None:
        """Mixed-verdict windows archive each counter correctly."""
        profiler: UserProfiler = UserProfiler(":memory:", ":memory:", 91)
        for _ in range(91):
            profiler.record(
                "app",
                "u",
                total_msgs=50,
                flagged_msgs=30,
                blocked_msgs=15,
                reviewed_msgs=2,
            )
            self.advance_days(1)
        profile = profiler.get_profile("app", "u")
        assert len(profile["summaries"]) == 1
        assert profiler.get_ratio("app", "u") == 0.9
        profiler.close()

    def test_mixed_v100_f60_b30_r5_4012(self) -> None:
        """Mixed-verdict windows archive each counter correctly."""
        profiler: UserProfiler = UserProfiler(":memory:", ":memory:", 91)
        for _ in range(91):
            profiler.record(
                "app",
                "u",
                total_msgs=100,
                flagged_msgs=60,
                blocked_msgs=30,
                reviewed_msgs=5,
            )
            self.advance_days(1)
        profile = profiler.get_profile("app", "u")
        assert len(profile["summaries"]) == 1
        assert profiler.get_ratio("app", "u") == 0.9
        profiler.close()

    def test_mixed_v200_f60_b30_r5_4013(self) -> None:
        """Mixed-verdict windows archive each counter correctly."""
        profiler: UserProfiler = UserProfiler(":memory:", ":memory:", 91)
        for _ in range(91):
            profiler.record(
                "app",
                "u",
                total_msgs=200,
                flagged_msgs=120,
                blocked_msgs=60,
                reviewed_msgs=10,
            )
            self.advance_days(1)
        profile = profiler.get_profile("app", "u")
        assert len(profile["summaries"]) == 1
        assert profiler.get_ratio("app", "u") == 0.9
        profiler.close()

    def test_mixed_v500_f60_b30_r5_4014(self) -> None:
        """Mixed-verdict windows archive each counter correctly."""
        profiler: UserProfiler = UserProfiler(":memory:", ":memory:", 91)
        for _ in range(91):
            profiler.record(
                "app",
                "u",
                total_msgs=500,
                flagged_msgs=300,
                blocked_msgs=150,
                reviewed_msgs=25,
            )
            self.advance_days(1)
        profile = profiler.get_profile("app", "u")
        assert len(profile["summaries"]) == 1
        assert profiler.get_ratio("app", "u") == 0.9
        profiler.close()

    def test_mixed_v1000_f60_b30_r5_4015(self) -> None:
        """Mixed-verdict windows archive each counter correctly."""
        profiler: UserProfiler = UserProfiler(":memory:", ":memory:", 91)
        for _ in range(91):
            profiler.record(
                "app",
                "u",
                total_msgs=1000,
                flagged_msgs=600,
                blocked_msgs=300,
                reviewed_msgs=50,
            )
            self.advance_days(1)
        profile = profiler.get_profile("app", "u")
        assert len(profile["summaries"]) == 1
        assert profiler.get_ratio("app", "u") == 0.9
        profiler.close()

    def test_mixed_v2500_f60_b30_r5_4016(self) -> None:
        """Mixed-verdict windows archive each counter correctly."""
        profiler: UserProfiler = UserProfiler(":memory:", ":memory:", 91)
        for _ in range(91):
            profiler.record(
                "app",
                "u",
                total_msgs=2500,
                flagged_msgs=1500,
                blocked_msgs=750,
                reviewed_msgs=125,
            )
            self.advance_days(1)
        profile = profiler.get_profile("app", "u")
        assert len(profile["summaries"]) == 1
        assert profiler.get_ratio("app", "u") == 0.9
        profiler.close()

    def test_mixed_v5000_f60_b30_r5_4017(self) -> None:
        """Mixed-verdict windows archive each counter correctly."""
        profiler: UserProfiler = UserProfiler(":memory:", ":memory:", 91)
        for _ in range(91):
            profiler.record(
                "app",
                "u",
                total_msgs=5000,
                flagged_msgs=3000,
                blocked_msgs=1500,
                reviewed_msgs=250,
            )
            self.advance_days(1)
        profile = profiler.get_profile("app", "u")
        assert len(profile["summaries"]) == 1
        assert profiler.get_ratio("app", "u") == 0.9
        profiler.close()

    def test_mixed_v7500_f60_b30_r5_4018(self) -> None:
        """Mixed-verdict windows archive each counter correctly."""
        profiler: UserProfiler = UserProfiler(":memory:", ":memory:", 91)
        for _ in range(91):
            profiler.record(
                "app",
                "u",
                total_msgs=7500,
                flagged_msgs=4500,
                blocked_msgs=2250,
                reviewed_msgs=375,
            )
            self.advance_days(1)
        profile = profiler.get_profile("app", "u")
        assert len(profile["summaries"]) == 1
        assert profiler.get_ratio("app", "u") == 0.9
        profiler.close()

    def test_mixed_v10_f70_b20_r10_4019(self) -> None:
        """Mixed-verdict windows archive each counter correctly."""
        profiler: UserProfiler = UserProfiler(":memory:", ":memory:", 91)
        for _ in range(91):
            profiler.record(
                "app",
                "u",
                total_msgs=10,
                flagged_msgs=7,
                blocked_msgs=2,
                reviewed_msgs=1,
            )
            self.advance_days(1)
        profile = profiler.get_profile("app", "u")
        assert len(profile["summaries"]) == 1
        assert profiler.get_ratio("app", "u") == 0.9
        profiler.close()

    def test_mixed_v20_f70_b20_r10_4020(self) -> None:
        """Mixed-verdict windows archive each counter correctly."""
        profiler: UserProfiler = UserProfiler(":memory:", ":memory:", 91)
        for _ in range(91):
            profiler.record(
                "app",
                "u",
                total_msgs=20,
                flagged_msgs=14,
                blocked_msgs=4,
                reviewed_msgs=2,
            )
            self.advance_days(1)
        profile = profiler.get_profile("app", "u")
        assert len(profile["summaries"]) == 1
        assert profiler.get_ratio("app", "u") == 0.9
        profiler.close()

    def test_mixed_v50_f70_b20_r10_4021(self) -> None:
        """Mixed-verdict windows archive each counter correctly."""
        profiler: UserProfiler = UserProfiler(":memory:", ":memory:", 91)
        for _ in range(91):
            profiler.record(
                "app",
                "u",
                total_msgs=50,
                flagged_msgs=35,
                blocked_msgs=10,
                reviewed_msgs=5,
            )
            self.advance_days(1)
        profile = profiler.get_profile("app", "u")
        assert len(profile["summaries"]) == 1
        assert profiler.get_ratio("app", "u") == 0.9
        profiler.close()

    def test_mixed_v100_f70_b20_r10_4022(self) -> None:
        """Mixed-verdict windows archive each counter correctly."""
        profiler: UserProfiler = UserProfiler(":memory:", ":memory:", 91)
        for _ in range(91):
            profiler.record(
                "app",
                "u",
                total_msgs=100,
                flagged_msgs=70,
                blocked_msgs=20,
                reviewed_msgs=10,
            )
            self.advance_days(1)
        profile = profiler.get_profile("app", "u")
        assert len(profile["summaries"]) == 1
        assert profiler.get_ratio("app", "u") == 0.9
        profiler.close()

    def test_mixed_v200_f70_b20_r10_4023(self) -> None:
        """Mixed-verdict windows archive each counter correctly."""
        profiler: UserProfiler = UserProfiler(":memory:", ":memory:", 91)
        for _ in range(91):
            profiler.record(
                "app",
                "u",
                total_msgs=200,
                flagged_msgs=140,
                blocked_msgs=40,
                reviewed_msgs=20,
            )
            self.advance_days(1)
        profile = profiler.get_profile("app", "u")
        assert len(profile["summaries"]) == 1
        assert profiler.get_ratio("app", "u") == 0.9
        profiler.close()

    def test_mixed_v500_f70_b20_r10_4024(self) -> None:
        """Mixed-verdict windows archive each counter correctly."""
        profiler: UserProfiler = UserProfiler(":memory:", ":memory:", 91)
        for _ in range(91):
            profiler.record(
                "app",
                "u",
                total_msgs=500,
                flagged_msgs=350,
                blocked_msgs=100,
                reviewed_msgs=50,
            )
            self.advance_days(1)
        profile = profiler.get_profile("app", "u")
        assert len(profile["summaries"]) == 1
        assert profiler.get_ratio("app", "u") == 0.9
        profiler.close()

    def test_mixed_v1000_f70_b20_r10_4025(self) -> None:
        """Mixed-verdict windows archive each counter correctly."""
        profiler: UserProfiler = UserProfiler(":memory:", ":memory:", 91)
        for _ in range(91):
            profiler.record(
                "app",
                "u",
                total_msgs=1000,
                flagged_msgs=700,
                blocked_msgs=200,
                reviewed_msgs=100,
            )
            self.advance_days(1)
        profile = profiler.get_profile("app", "u")
        assert len(profile["summaries"]) == 1
        assert profiler.get_ratio("app", "u") == 0.9
        profiler.close()

    def test_mixed_v2500_f70_b20_r10_4026(self) -> None:
        """Mixed-verdict windows archive each counter correctly."""
        profiler: UserProfiler = UserProfiler(":memory:", ":memory:", 91)
        for _ in range(91):
            profiler.record(
                "app",
                "u",
                total_msgs=2500,
                flagged_msgs=1750,
                blocked_msgs=500,
                reviewed_msgs=250,
            )
            self.advance_days(1)
        profile = profiler.get_profile("app", "u")
        assert len(profile["summaries"]) == 1
        assert profiler.get_ratio("app", "u") == 0.9
        profiler.close()

    def test_mixed_v5000_f70_b20_r10_4027(self) -> None:
        """Mixed-verdict windows archive each counter correctly."""
        profiler: UserProfiler = UserProfiler(":memory:", ":memory:", 91)
        for _ in range(91):
            profiler.record(
                "app",
                "u",
                total_msgs=5000,
                flagged_msgs=3500,
                blocked_msgs=1000,
                reviewed_msgs=500,
            )
            self.advance_days(1)
        profile = profiler.get_profile("app", "u")
        assert len(profile["summaries"]) == 1
        assert profiler.get_ratio("app", "u") == 0.9
        profiler.close()

    def test_mixed_v7500_f70_b20_r10_4028(self) -> None:
        """Mixed-verdict windows archive each counter correctly."""
        profiler: UserProfiler = UserProfiler(":memory:", ":memory:", 91)
        for _ in range(91):
            profiler.record(
                "app",
                "u",
                total_msgs=7500,
                flagged_msgs=5250,
                blocked_msgs=1500,
                reviewed_msgs=750,
            )
            self.advance_days(1)
        profile = profiler.get_profile("app", "u")
        assert len(profile["summaries"]) == 1
        assert profiler.get_ratio("app", "u") == 0.9
        profiler.close()

    def test_mixed_v10_f80_b10_r5_4029(self) -> None:
        """Mixed-verdict windows archive each counter correctly."""
        profiler: UserProfiler = UserProfiler(":memory:", ":memory:", 91)
        for _ in range(91):
            profiler.record(
                "app",
                "u",
                total_msgs=10,
                flagged_msgs=8,
                blocked_msgs=1,
                reviewed_msgs=0,
            )
            self.advance_days(1)
        profile = profiler.get_profile("app", "u")
        assert len(profile["summaries"]) == 1
        assert profiler.get_ratio("app", "u") == 0.9
        profiler.close()

    def test_mixed_v20_f80_b10_r5_4030(self) -> None:
        """Mixed-verdict windows archive each counter correctly."""
        profiler: UserProfiler = UserProfiler(":memory:", ":memory:", 91)
        for _ in range(91):
            profiler.record(
                "app",
                "u",
                total_msgs=20,
                flagged_msgs=16,
                blocked_msgs=2,
                reviewed_msgs=1,
            )
            self.advance_days(1)
        profile = profiler.get_profile("app", "u")
        assert len(profile["summaries"]) == 1
        assert profiler.get_ratio("app", "u") == 0.9
        profiler.close()

    def test_mixed_v50_f80_b10_r5_4031(self) -> None:
        """Mixed-verdict windows archive each counter correctly."""
        profiler: UserProfiler = UserProfiler(":memory:", ":memory:", 91)
        for _ in range(91):
            profiler.record(
                "app",
                "u",
                total_msgs=50,
                flagged_msgs=40,
                blocked_msgs=5,
                reviewed_msgs=2,
            )
            self.advance_days(1)
        profile = profiler.get_profile("app", "u")
        assert len(profile["summaries"]) == 1
        assert profiler.get_ratio("app", "u") == 0.9
        profiler.close()

    def test_mixed_v100_f80_b10_r5_4032(self) -> None:
        """Mixed-verdict windows archive each counter correctly."""
        profiler: UserProfiler = UserProfiler(":memory:", ":memory:", 91)
        for _ in range(91):
            profiler.record(
                "app",
                "u",
                total_msgs=100,
                flagged_msgs=80,
                blocked_msgs=10,
                reviewed_msgs=5,
            )
            self.advance_days(1)
        profile = profiler.get_profile("app", "u")
        assert len(profile["summaries"]) == 1
        assert profiler.get_ratio("app", "u") == 0.9
        profiler.close()

    def test_mixed_v200_f80_b10_r5_4033(self) -> None:
        """Mixed-verdict windows archive each counter correctly."""
        profiler: UserProfiler = UserProfiler(":memory:", ":memory:", 91)
        for _ in range(91):
            profiler.record(
                "app",
                "u",
                total_msgs=200,
                flagged_msgs=160,
                blocked_msgs=20,
                reviewed_msgs=10,
            )
            self.advance_days(1)
        profile = profiler.get_profile("app", "u")
        assert len(profile["summaries"]) == 1
        assert profiler.get_ratio("app", "u") == 0.9
        profiler.close()

    def test_mixed_v500_f80_b10_r5_4034(self) -> None:
        """Mixed-verdict windows archive each counter correctly."""
        profiler: UserProfiler = UserProfiler(":memory:", ":memory:", 91)
        for _ in range(91):
            profiler.record(
                "app",
                "u",
                total_msgs=500,
                flagged_msgs=400,
                blocked_msgs=50,
                reviewed_msgs=25,
            )
            self.advance_days(1)
        profile = profiler.get_profile("app", "u")
        assert len(profile["summaries"]) == 1
        assert profiler.get_ratio("app", "u") == 0.9
        profiler.close()

    def test_mixed_v1000_f80_b10_r5_4035(self) -> None:
        """Mixed-verdict windows archive each counter correctly."""
        profiler: UserProfiler = UserProfiler(":memory:", ":memory:", 91)
        for _ in range(91):
            profiler.record(
                "app",
                "u",
                total_msgs=1000,
                flagged_msgs=800,
                blocked_msgs=100,
                reviewed_msgs=50,
            )
            self.advance_days(1)
        profile = profiler.get_profile("app", "u")
        assert len(profile["summaries"]) == 1
        assert profiler.get_ratio("app", "u") == 0.9
        profiler.close()

    def test_mixed_v2500_f80_b10_r5_4036(self) -> None:
        """Mixed-verdict windows archive each counter correctly."""
        profiler: UserProfiler = UserProfiler(":memory:", ":memory:", 91)
        for _ in range(91):
            profiler.record(
                "app",
                "u",
                total_msgs=2500,
                flagged_msgs=2000,
                blocked_msgs=250,
                reviewed_msgs=125,
            )
            self.advance_days(1)
        profile = profiler.get_profile("app", "u")
        assert len(profile["summaries"]) == 1
        assert profiler.get_ratio("app", "u") == 0.9
        profiler.close()

    def test_mixed_v5000_f80_b10_r5_4037(self) -> None:
        """Mixed-verdict windows archive each counter correctly."""
        profiler: UserProfiler = UserProfiler(":memory:", ":memory:", 91)
        for _ in range(91):
            profiler.record(
                "app",
                "u",
                total_msgs=5000,
                flagged_msgs=4000,
                blocked_msgs=500,
                reviewed_msgs=250,
            )
            self.advance_days(1)
        profile = profiler.get_profile("app", "u")
        assert len(profile["summaries"]) == 1
        assert profiler.get_ratio("app", "u") == 0.9
        profiler.close()

    def test_mixed_v7500_f80_b10_r5_4038(self) -> None:
        """Mixed-verdict windows archive each counter correctly."""
        profiler: UserProfiler = UserProfiler(":memory:", ":memory:", 91)
        for _ in range(91):
            profiler.record(
                "app",
                "u",
                total_msgs=7500,
                flagged_msgs=6000,
                blocked_msgs=750,
                reviewed_msgs=375,
            )
            self.advance_days(1)
        profile = profiler.get_profile("app", "u")
        assert len(profile["summaries"]) == 1
        assert profiler.get_ratio("app", "u") == 0.9
        profiler.close()

    def test_mixed_v10_f90_b5_r5_4039(self) -> None:
        """Mixed-verdict windows archive each counter correctly."""
        profiler: UserProfiler = UserProfiler(":memory:", ":memory:", 91)
        for _ in range(91):
            profiler.record(
                "app",
                "u",
                total_msgs=10,
                flagged_msgs=9,
                blocked_msgs=0,
                reviewed_msgs=0,
            )
            self.advance_days(1)
        profile = profiler.get_profile("app", "u")
        assert len(profile["summaries"]) == 1
        assert profiler.get_ratio("app", "u") == 0.9
        profiler.close()

    def test_mixed_v20_f90_b5_r5_4040(self) -> None:
        """Mixed-verdict windows archive each counter correctly."""
        profiler: UserProfiler = UserProfiler(":memory:", ":memory:", 91)
        for _ in range(91):
            profiler.record(
                "app",
                "u",
                total_msgs=20,
                flagged_msgs=18,
                blocked_msgs=1,
                reviewed_msgs=1,
            )
            self.advance_days(1)
        profile = profiler.get_profile("app", "u")
        assert len(profile["summaries"]) == 1
        assert profiler.get_ratio("app", "u") == 0.95
        profiler.close()

    def test_mixed_v50_f90_b5_r5_4041(self) -> None:
        """Mixed-verdict windows archive each counter correctly."""
        profiler: UserProfiler = UserProfiler(":memory:", ":memory:", 91)
        for _ in range(91):
            profiler.record(
                "app",
                "u",
                total_msgs=50,
                flagged_msgs=45,
                blocked_msgs=2,
                reviewed_msgs=2,
            )
            self.advance_days(1)
        profile = profiler.get_profile("app", "u")
        assert len(profile["summaries"]) == 1
        assert profiler.get_ratio("app", "u") == 0.94
        profiler.close()

    def test_mixed_v100_f90_b5_r5_4042(self) -> None:
        """Mixed-verdict windows archive each counter correctly."""
        profiler: UserProfiler = UserProfiler(":memory:", ":memory:", 91)
        for _ in range(91):
            profiler.record(
                "app",
                "u",
                total_msgs=100,
                flagged_msgs=90,
                blocked_msgs=5,
                reviewed_msgs=5,
            )
            self.advance_days(1)
        profile = profiler.get_profile("app", "u")
        assert len(profile["summaries"]) == 1
        assert profiler.get_ratio("app", "u") == 0.95
        profiler.close()

    def test_mixed_v200_f90_b5_r5_4043(self) -> None:
        """Mixed-verdict windows archive each counter correctly."""
        profiler: UserProfiler = UserProfiler(":memory:", ":memory:", 91)
        for _ in range(91):
            profiler.record(
                "app",
                "u",
                total_msgs=200,
                flagged_msgs=180,
                blocked_msgs=10,
                reviewed_msgs=10,
            )
            self.advance_days(1)
        profile = profiler.get_profile("app", "u")
        assert len(profile["summaries"]) == 1
        assert profiler.get_ratio("app", "u") == 0.95
        profiler.close()

    def test_mixed_v500_f90_b5_r5_4044(self) -> None:
        """Mixed-verdict windows archive each counter correctly."""
        profiler: UserProfiler = UserProfiler(":memory:", ":memory:", 91)
        for _ in range(91):
            profiler.record(
                "app",
                "u",
                total_msgs=500,
                flagged_msgs=450,
                blocked_msgs=25,
                reviewed_msgs=25,
            )
            self.advance_days(1)
        profile = profiler.get_profile("app", "u")
        assert len(profile["summaries"]) == 1
        assert profiler.get_ratio("app", "u") == 0.95
        profiler.close()

    def test_mixed_v1000_f90_b5_r5_4045(self) -> None:
        """Mixed-verdict windows archive each counter correctly."""
        profiler: UserProfiler = UserProfiler(":memory:", ":memory:", 91)
        for _ in range(91):
            profiler.record(
                "app",
                "u",
                total_msgs=1000,
                flagged_msgs=900,
                blocked_msgs=50,
                reviewed_msgs=50,
            )
            self.advance_days(1)
        profile = profiler.get_profile("app", "u")
        assert len(profile["summaries"]) == 1
        assert profiler.get_ratio("app", "u") == 0.95
        profiler.close()

    def test_mixed_v2500_f90_b5_r5_4046(self) -> None:
        """Mixed-verdict windows archive each counter correctly."""
        profiler: UserProfiler = UserProfiler(":memory:", ":memory:", 91)
        for _ in range(91):
            profiler.record(
                "app",
                "u",
                total_msgs=2500,
                flagged_msgs=2250,
                blocked_msgs=125,
                reviewed_msgs=125,
            )
            self.advance_days(1)
        profile = profiler.get_profile("app", "u")
        assert len(profile["summaries"]) == 1
        assert profiler.get_ratio("app", "u") == 0.95
        profiler.close()

    def test_mixed_v5000_f90_b5_r5_4047(self) -> None:
        """Mixed-verdict windows archive each counter correctly."""
        profiler: UserProfiler = UserProfiler(":memory:", ":memory:", 91)
        for _ in range(91):
            profiler.record(
                "app",
                "u",
                total_msgs=5000,
                flagged_msgs=4500,
                blocked_msgs=250,
                reviewed_msgs=250,
            )
            self.advance_days(1)
        profile = profiler.get_profile("app", "u")
        assert len(profile["summaries"]) == 1
        assert profiler.get_ratio("app", "u") == 0.95
        profiler.close()

    def test_mixed_v7500_f90_b5_r5_4048(self) -> None:
        """Mixed-verdict windows archive each counter correctly."""
        profiler: UserProfiler = UserProfiler(":memory:", ":memory:", 91)
        for _ in range(91):
            profiler.record(
                "app",
                "u",
                total_msgs=7500,
                flagged_msgs=6750,
                blocked_msgs=375,
                reviewed_msgs=375,
            )
            self.advance_days(1)
        profile = profiler.get_profile("app", "u")
        assert len(profile["summaries"]) == 1
        assert profiler.get_ratio("app", "u") == 0.95
        profiler.close()

    def test_mixed_v10_f100_b0_r0_4049(self) -> None:
        """Mixed-verdict windows archive each counter correctly."""
        profiler: UserProfiler = UserProfiler(":memory:", ":memory:", 91)
        for _ in range(91):
            profiler.record(
                "app",
                "u",
                total_msgs=10,
                flagged_msgs=10,
                blocked_msgs=0,
                reviewed_msgs=0,
            )
            self.advance_days(1)
        profile = profiler.get_profile("app", "u")
        assert len(profile["summaries"]) == 1
        assert profiler.get_ratio("app", "u") == 1.0
        profiler.close()

    def test_mixed_v20_f100_b0_r0_4050(self) -> None:
        """Mixed-verdict windows archive each counter correctly."""
        profiler: UserProfiler = UserProfiler(":memory:", ":memory:", 91)
        for _ in range(91):
            profiler.record(
                "app",
                "u",
                total_msgs=20,
                flagged_msgs=20,
                blocked_msgs=0,
                reviewed_msgs=0,
            )
            self.advance_days(1)
        profile = profiler.get_profile("app", "u")
        assert len(profile["summaries"]) == 1
        assert profiler.get_ratio("app", "u") == 1.0
        profiler.close()

    def test_mixed_v50_f100_b0_r0_4051(self) -> None:
        """Mixed-verdict windows archive each counter correctly."""
        profiler: UserProfiler = UserProfiler(":memory:", ":memory:", 91)
        for _ in range(91):
            profiler.record(
                "app",
                "u",
                total_msgs=50,
                flagged_msgs=50,
                blocked_msgs=0,
                reviewed_msgs=0,
            )
            self.advance_days(1)
        profile = profiler.get_profile("app", "u")
        assert len(profile["summaries"]) == 1
        assert profiler.get_ratio("app", "u") == 1.0
        profiler.close()

    def test_mixed_v100_f100_b0_r0_4052(self) -> None:
        """Mixed-verdict windows archive each counter correctly."""
        profiler: UserProfiler = UserProfiler(":memory:", ":memory:", 91)
        for _ in range(91):
            profiler.record(
                "app",
                "u",
                total_msgs=100,
                flagged_msgs=100,
                blocked_msgs=0,
                reviewed_msgs=0,
            )
            self.advance_days(1)
        profile = profiler.get_profile("app", "u")
        assert len(profile["summaries"]) == 1
        assert profiler.get_ratio("app", "u") == 1.0
        profiler.close()

    def test_mixed_v200_f100_b0_r0_4053(self) -> None:
        """Mixed-verdict windows archive each counter correctly."""
        profiler: UserProfiler = UserProfiler(":memory:", ":memory:", 91)
        for _ in range(91):
            profiler.record(
                "app",
                "u",
                total_msgs=200,
                flagged_msgs=200,
                blocked_msgs=0,
                reviewed_msgs=0,
            )
            self.advance_days(1)
        profile = profiler.get_profile("app", "u")
        assert len(profile["summaries"]) == 1
        assert profiler.get_ratio("app", "u") == 1.0
        profiler.close()

    def test_mixed_v500_f100_b0_r0_4054(self) -> None:
        """Mixed-verdict windows archive each counter correctly."""
        profiler: UserProfiler = UserProfiler(":memory:", ":memory:", 91)
        for _ in range(91):
            profiler.record(
                "app",
                "u",
                total_msgs=500,
                flagged_msgs=500,
                blocked_msgs=0,
                reviewed_msgs=0,
            )
            self.advance_days(1)
        profile = profiler.get_profile("app", "u")
        assert len(profile["summaries"]) == 1
        assert profiler.get_ratio("app", "u") == 1.0
        profiler.close()

    def test_mixed_v1000_f100_b0_r0_4055(self) -> None:
        """Mixed-verdict windows archive each counter correctly."""
        profiler: UserProfiler = UserProfiler(":memory:", ":memory:", 91)
        for _ in range(91):
            profiler.record(
                "app",
                "u",
                total_msgs=1000,
                flagged_msgs=1000,
                blocked_msgs=0,
                reviewed_msgs=0,
            )
            self.advance_days(1)
        profile = profiler.get_profile("app", "u")
        assert len(profile["summaries"]) == 1
        assert profiler.get_ratio("app", "u") == 1.0
        profiler.close()

    def test_mixed_v2500_f100_b0_r0_4056(self) -> None:
        """Mixed-verdict windows archive each counter correctly."""
        profiler: UserProfiler = UserProfiler(":memory:", ":memory:", 91)
        for _ in range(91):
            profiler.record(
                "app",
                "u",
                total_msgs=2500,
                flagged_msgs=2500,
                blocked_msgs=0,
                reviewed_msgs=0,
            )
            self.advance_days(1)
        profile = profiler.get_profile("app", "u")
        assert len(profile["summaries"]) == 1
        assert profiler.get_ratio("app", "u") == 1.0
        profiler.close()

    def test_mixed_v5000_f100_b0_r0_4057(self) -> None:
        """Mixed-verdict windows archive each counter correctly."""
        profiler: UserProfiler = UserProfiler(":memory:", ":memory:", 91)
        for _ in range(91):
            profiler.record(
                "app",
                "u",
                total_msgs=5000,
                flagged_msgs=5000,
                blocked_msgs=0,
                reviewed_msgs=0,
            )
            self.advance_days(1)
        profile = profiler.get_profile("app", "u")
        assert len(profile["summaries"]) == 1
        assert profiler.get_ratio("app", "u") == 1.0
        profiler.close()

    def test_mixed_v7500_f100_b0_r0_4058(self) -> None:
        """Mixed-verdict windows archive each counter correctly."""
        profiler: UserProfiler = UserProfiler(":memory:", ":memory:", 91)
        for _ in range(91):
            profiler.record(
                "app",
                "u",
                total_msgs=7500,
                flagged_msgs=7500,
                blocked_msgs=0,
                reviewed_msgs=0,
            )
            self.advance_days(1)
        profile = profiler.get_profile("app", "u")
        assert len(profile["summaries"]) == 1
        assert profiler.get_ratio("app", "u") == 1.0
        profiler.close()

    def test_mixed_v10_f15_b15_r15_4059(self) -> None:
        """Mixed-verdict windows archive each counter correctly."""
        profiler: UserProfiler = UserProfiler(":memory:", ":memory:", 91)
        for _ in range(91):
            profiler.record(
                "app",
                "u",
                total_msgs=10,
                flagged_msgs=2,
                blocked_msgs=2,
                reviewed_msgs=2,
            )
            self.advance_days(1)
        profile = profiler.get_profile("app", "u")
        assert len(profile["summaries"]) == 1
        assert profiler.get_ratio("app", "u") == 0.4
        profiler.close()

    def test_mixed_v20_f15_b15_r15_4060(self) -> None:
        """Mixed-verdict windows archive each counter correctly."""
        profiler: UserProfiler = UserProfiler(":memory:", ":memory:", 91)
        for _ in range(91):
            profiler.record(
                "app",
                "u",
                total_msgs=20,
                flagged_msgs=3,
                blocked_msgs=3,
                reviewed_msgs=3,
            )
            self.advance_days(1)
        profile = profiler.get_profile("app", "u")
        assert len(profile["summaries"]) == 1
        assert profiler.get_ratio("app", "u") == 0.3
        profiler.close()

    def test_mixed_v50_f15_b15_r15_4061(self) -> None:
        """Mixed-verdict windows archive each counter correctly."""
        profiler: UserProfiler = UserProfiler(":memory:", ":memory:", 91)
        for _ in range(91):
            profiler.record(
                "app",
                "u",
                total_msgs=50,
                flagged_msgs=8,
                blocked_msgs=8,
                reviewed_msgs=8,
            )
            self.advance_days(1)
        profile = profiler.get_profile("app", "u")
        assert len(profile["summaries"]) == 1
        assert profiler.get_ratio("app", "u") == 0.32
        profiler.close()

    def test_mixed_v100_f15_b15_r15_4062(self) -> None:
        """Mixed-verdict windows archive each counter correctly."""
        profiler: UserProfiler = UserProfiler(":memory:", ":memory:", 91)
        for _ in range(91):
            profiler.record(
                "app",
                "u",
                total_msgs=100,
                flagged_msgs=15,
                blocked_msgs=15,
                reviewed_msgs=15,
            )
            self.advance_days(1)
        profile = profiler.get_profile("app", "u")
        assert len(profile["summaries"]) == 1
        assert profiler.get_ratio("app", "u") == 0.3
        profiler.close()

    def test_mixed_v200_f15_b15_r15_4063(self) -> None:
        """Mixed-verdict windows archive each counter correctly."""
        profiler: UserProfiler = UserProfiler(":memory:", ":memory:", 91)
        for _ in range(91):
            profiler.record(
                "app",
                "u",
                total_msgs=200,
                flagged_msgs=30,
                blocked_msgs=30,
                reviewed_msgs=30,
            )
            self.advance_days(1)
        profile = profiler.get_profile("app", "u")
        assert len(profile["summaries"]) == 1
        assert profiler.get_ratio("app", "u") == 0.3
        profiler.close()

    def test_mixed_v500_f15_b15_r15_4064(self) -> None:
        """Mixed-verdict windows archive each counter correctly."""
        profiler: UserProfiler = UserProfiler(":memory:", ":memory:", 91)
        for _ in range(91):
            profiler.record(
                "app",
                "u",
                total_msgs=500,
                flagged_msgs=75,
                blocked_msgs=75,
                reviewed_msgs=75,
            )
            self.advance_days(1)
        profile = profiler.get_profile("app", "u")
        assert len(profile["summaries"]) == 1
        assert profiler.get_ratio("app", "u") == 0.3
        profiler.close()

    def test_mixed_v1000_f15_b15_r15_4065(self) -> None:
        """Mixed-verdict windows archive each counter correctly."""
        profiler: UserProfiler = UserProfiler(":memory:", ":memory:", 91)
        for _ in range(91):
            profiler.record(
                "app",
                "u",
                total_msgs=1000,
                flagged_msgs=150,
                blocked_msgs=150,
                reviewed_msgs=150,
            )
            self.advance_days(1)
        profile = profiler.get_profile("app", "u")
        assert len(profile["summaries"]) == 1
        assert profiler.get_ratio("app", "u") == 0.3
        profiler.close()

    def test_mixed_v2500_f15_b15_r15_4066(self) -> None:
        """Mixed-verdict windows archive each counter correctly."""
        profiler: UserProfiler = UserProfiler(":memory:", ":memory:", 91)
        for _ in range(91):
            profiler.record(
                "app",
                "u",
                total_msgs=2500,
                flagged_msgs=375,
                blocked_msgs=375,
                reviewed_msgs=375,
            )
            self.advance_days(1)
        profile = profiler.get_profile("app", "u")
        assert len(profile["summaries"]) == 1
        assert profiler.get_ratio("app", "u") == 0.3
        profiler.close()

    def test_mixed_v5000_f15_b15_r15_4067(self) -> None:
        """Mixed-verdict windows archive each counter correctly."""
        profiler: UserProfiler = UserProfiler(":memory:", ":memory:", 91)
        for _ in range(91):
            profiler.record(
                "app",
                "u",
                total_msgs=5000,
                flagged_msgs=750,
                blocked_msgs=750,
                reviewed_msgs=750,
            )
            self.advance_days(1)
        profile = profiler.get_profile("app", "u")
        assert len(profile["summaries"]) == 1
        assert profiler.get_ratio("app", "u") == 0.3
        profiler.close()

    def test_mixed_v7500_f15_b15_r15_4068(self) -> None:
        """Mixed-verdict windows archive each counter correctly."""
        profiler: UserProfiler = UserProfiler(":memory:", ":memory:", 91)
        for _ in range(91):
            profiler.record(
                "app",
                "u",
                total_msgs=7500,
                flagged_msgs=1125,
                blocked_msgs=1125,
                reviewed_msgs=1125,
            )
            self.advance_days(1)
        profile = profiler.get_profile("app", "u")
        assert len(profile["summaries"]) == 1
        assert profiler.get_ratio("app", "u") == 0.3
        profiler.close()

    def test_mixed_v10_f25_b25_r25_4069(self) -> None:
        """Mixed-verdict windows archive each counter correctly."""
        profiler: UserProfiler = UserProfiler(":memory:", ":memory:", 91)
        for _ in range(91):
            profiler.record(
                "app",
                "u",
                total_msgs=10,
                flagged_msgs=2,
                blocked_msgs=2,
                reviewed_msgs=2,
            )
            self.advance_days(1)
        profile = profiler.get_profile("app", "u")
        assert len(profile["summaries"]) == 1
        assert profiler.get_ratio("app", "u") == 0.4
        profiler.close()

    def test_mixed_v20_f25_b25_r25_4070(self) -> None:
        """Mixed-verdict windows archive each counter correctly."""
        profiler: UserProfiler = UserProfiler(":memory:", ":memory:", 91)
        for _ in range(91):
            profiler.record(
                "app",
                "u",
                total_msgs=20,
                flagged_msgs=5,
                blocked_msgs=5,
                reviewed_msgs=5,
            )
            self.advance_days(1)
        profile = profiler.get_profile("app", "u")
        assert len(profile["summaries"]) == 1
        assert profiler.get_ratio("app", "u") == 0.5
        profiler.close()

    def test_mixed_v50_f25_b25_r25_4071(self) -> None:
        """Mixed-verdict windows archive each counter correctly."""
        profiler: UserProfiler = UserProfiler(":memory:", ":memory:", 91)
        for _ in range(91):
            profiler.record(
                "app",
                "u",
                total_msgs=50,
                flagged_msgs=12,
                blocked_msgs=12,
                reviewed_msgs=12,
            )
            self.advance_days(1)
        profile = profiler.get_profile("app", "u")
        assert len(profile["summaries"]) == 1
        assert profiler.get_ratio("app", "u") == 0.48
        profiler.close()

    def test_mixed_v100_f25_b25_r25_4072(self) -> None:
        """Mixed-verdict windows archive each counter correctly."""
        profiler: UserProfiler = UserProfiler(":memory:", ":memory:", 91)
        for _ in range(91):
            profiler.record(
                "app",
                "u",
                total_msgs=100,
                flagged_msgs=25,
                blocked_msgs=25,
                reviewed_msgs=25,
            )
            self.advance_days(1)
        profile = profiler.get_profile("app", "u")
        assert len(profile["summaries"]) == 1
        assert profiler.get_ratio("app", "u") == 0.5
        profiler.close()

    def test_mixed_v200_f25_b25_r25_4073(self) -> None:
        """Mixed-verdict windows archive each counter correctly."""
        profiler: UserProfiler = UserProfiler(":memory:", ":memory:", 91)
        for _ in range(91):
            profiler.record(
                "app",
                "u",
                total_msgs=200,
                flagged_msgs=50,
                blocked_msgs=50,
                reviewed_msgs=50,
            )
            self.advance_days(1)
        profile = profiler.get_profile("app", "u")
        assert len(profile["summaries"]) == 1
        assert profiler.get_ratio("app", "u") == 0.5
        profiler.close()

    def test_mixed_v500_f25_b25_r25_4074(self) -> None:
        """Mixed-verdict windows archive each counter correctly."""
        profiler: UserProfiler = UserProfiler(":memory:", ":memory:", 91)
        for _ in range(91):
            profiler.record(
                "app",
                "u",
                total_msgs=500,
                flagged_msgs=125,
                blocked_msgs=125,
                reviewed_msgs=125,
            )
            self.advance_days(1)
        profile = profiler.get_profile("app", "u")
        assert len(profile["summaries"]) == 1
        assert profiler.get_ratio("app", "u") == 0.5
        profiler.close()

    def test_mixed_v1000_f25_b25_r25_4075(self) -> None:
        """Mixed-verdict windows archive each counter correctly."""
        profiler: UserProfiler = UserProfiler(":memory:", ":memory:", 91)
        for _ in range(91):
            profiler.record(
                "app",
                "u",
                total_msgs=1000,
                flagged_msgs=250,
                blocked_msgs=250,
                reviewed_msgs=250,
            )
            self.advance_days(1)
        profile = profiler.get_profile("app", "u")
        assert len(profile["summaries"]) == 1
        assert profiler.get_ratio("app", "u") == 0.5
        profiler.close()

    def test_mixed_v2500_f25_b25_r25_4076(self) -> None:
        """Mixed-verdict windows archive each counter correctly."""
        profiler: UserProfiler = UserProfiler(":memory:", ":memory:", 91)
        for _ in range(91):
            profiler.record(
                "app",
                "u",
                total_msgs=2500,
                flagged_msgs=625,
                blocked_msgs=625,
                reviewed_msgs=625,
            )
            self.advance_days(1)
        profile = profiler.get_profile("app", "u")
        assert len(profile["summaries"]) == 1
        assert profiler.get_ratio("app", "u") == 0.5
        profiler.close()

    def test_mixed_v5000_f25_b25_r25_4077(self) -> None:
        """Mixed-verdict windows archive each counter correctly."""
        profiler: UserProfiler = UserProfiler(":memory:", ":memory:", 91)
        for _ in range(91):
            profiler.record(
                "app",
                "u",
                total_msgs=5000,
                flagged_msgs=1250,
                blocked_msgs=1250,
                reviewed_msgs=1250,
            )
            self.advance_days(1)
        profile = profiler.get_profile("app", "u")
        assert len(profile["summaries"]) == 1
        assert profiler.get_ratio("app", "u") == 0.5
        profiler.close()

    def test_mixed_v7500_f25_b25_r25_4078(self) -> None:
        """Mixed-verdict windows archive each counter correctly."""
        profiler: UserProfiler = UserProfiler(":memory:", ":memory:", 91)
        for _ in range(91):
            profiler.record(
                "app",
                "u",
                total_msgs=7500,
                flagged_msgs=1875,
                blocked_msgs=1875,
                reviewed_msgs=1875,
            )
            self.advance_days(1)
        profile = profiler.get_profile("app", "u")
        assert len(profile["summaries"]) == 1
        assert profiler.get_ratio("app", "u") == 0.5
        profiler.close()

    def test_mixed_v10_f33_b33_r33_4079(self) -> None:
        """Mixed-verdict windows archive each counter correctly."""
        profiler: UserProfiler = UserProfiler(":memory:", ":memory:", 91)
        for _ in range(91):
            profiler.record(
                "app",
                "u",
                total_msgs=10,
                flagged_msgs=3,
                blocked_msgs=3,
                reviewed_msgs=3,
            )
            self.advance_days(1)
        profile = profiler.get_profile("app", "u")
        assert len(profile["summaries"]) == 1
        assert profiler.get_ratio("app", "u") == 0.6
        profiler.close()

    def test_mixed_v20_f33_b33_r33_4080(self) -> None:
        """Mixed-verdict windows archive each counter correctly."""
        profiler: UserProfiler = UserProfiler(":memory:", ":memory:", 91)
        for _ in range(91):
            profiler.record(
                "app",
                "u",
                total_msgs=20,
                flagged_msgs=7,
                blocked_msgs=7,
                reviewed_msgs=7,
            )
            self.advance_days(1)
        profile = profiler.get_profile("app", "u")
        assert len(profile["summaries"]) == 1
        assert profiler.get_ratio("app", "u") == 0.7
        profiler.close()

    def test_mixed_v50_f33_b33_r33_4081(self) -> None:
        """Mixed-verdict windows archive each counter correctly."""
        profiler: UserProfiler = UserProfiler(":memory:", ":memory:", 91)
        for _ in range(91):
            profiler.record(
                "app",
                "u",
                total_msgs=50,
                flagged_msgs=16,
                blocked_msgs=16,
                reviewed_msgs=16,
            )
            self.advance_days(1)
        profile = profiler.get_profile("app", "u")
        assert len(profile["summaries"]) == 1
        assert profiler.get_ratio("app", "u") == 0.64
        profiler.close()

    def test_mixed_v100_f33_b33_r33_4082(self) -> None:
        """Mixed-verdict windows archive each counter correctly."""
        profiler: UserProfiler = UserProfiler(":memory:", ":memory:", 91)
        for _ in range(91):
            profiler.record(
                "app",
                "u",
                total_msgs=100,
                flagged_msgs=33,
                blocked_msgs=33,
                reviewed_msgs=33,
            )
            self.advance_days(1)
        profile = profiler.get_profile("app", "u")
        assert len(profile["summaries"]) == 1
        assert profiler.get_ratio("app", "u") == 0.66
        profiler.close()

    def test_mixed_v200_f33_b33_r33_4083(self) -> None:
        """Mixed-verdict windows archive each counter correctly."""
        profiler: UserProfiler = UserProfiler(":memory:", ":memory:", 91)
        for _ in range(91):
            profiler.record(
                "app",
                "u",
                total_msgs=200,
                flagged_msgs=66,
                blocked_msgs=66,
                reviewed_msgs=66,
            )
            self.advance_days(1)
        profile = profiler.get_profile("app", "u")
        assert len(profile["summaries"]) == 1
        assert profiler.get_ratio("app", "u") == 0.66
        profiler.close()

    def test_mixed_v500_f33_b33_r33_4084(self) -> None:
        """Mixed-verdict windows archive each counter correctly."""
        profiler: UserProfiler = UserProfiler(":memory:", ":memory:", 91)
        for _ in range(91):
            profiler.record(
                "app",
                "u",
                total_msgs=500,
                flagged_msgs=165,
                blocked_msgs=165,
                reviewed_msgs=165,
            )
            self.advance_days(1)
        profile = profiler.get_profile("app", "u")
        assert len(profile["summaries"]) == 1
        assert profiler.get_ratio("app", "u") == 0.66
        profiler.close()

    def test_mixed_v1000_f33_b33_r33_4085(self) -> None:
        """Mixed-verdict windows archive each counter correctly."""
        profiler: UserProfiler = UserProfiler(":memory:", ":memory:", 91)
        for _ in range(91):
            profiler.record(
                "app",
                "u",
                total_msgs=1000,
                flagged_msgs=330,
                blocked_msgs=330,
                reviewed_msgs=330,
            )
            self.advance_days(1)
        profile = profiler.get_profile("app", "u")
        assert len(profile["summaries"]) == 1
        assert profiler.get_ratio("app", "u") == 0.66
        profiler.close()

    def test_mixed_v2500_f33_b33_r33_4086(self) -> None:
        """Mixed-verdict windows archive each counter correctly."""
        profiler: UserProfiler = UserProfiler(":memory:", ":memory:", 91)
        for _ in range(91):
            profiler.record(
                "app",
                "u",
                total_msgs=2500,
                flagged_msgs=825,
                blocked_msgs=825,
                reviewed_msgs=825,
            )
            self.advance_days(1)
        profile = profiler.get_profile("app", "u")
        assert len(profile["summaries"]) == 1
        assert profiler.get_ratio("app", "u") == 0.66
        profiler.close()

    def test_mixed_v5000_f33_b33_r33_4087(self) -> None:
        """Mixed-verdict windows archive each counter correctly."""
        profiler: UserProfiler = UserProfiler(":memory:", ":memory:", 91)
        for _ in range(91):
            profiler.record(
                "app",
                "u",
                total_msgs=5000,
                flagged_msgs=1650,
                blocked_msgs=1650,
                reviewed_msgs=1650,
            )
            self.advance_days(1)
        profile = profiler.get_profile("app", "u")
        assert len(profile["summaries"]) == 1
        assert profiler.get_ratio("app", "u") == 0.66
        profiler.close()

    def test_mixed_v7500_f33_b33_r33_4088(self) -> None:
        """Mixed-verdict windows archive each counter correctly."""
        profiler: UserProfiler = UserProfiler(":memory:", ":memory:", 91)
        for _ in range(91):
            profiler.record(
                "app",
                "u",
                total_msgs=7500,
                flagged_msgs=2475,
                blocked_msgs=2475,
                reviewed_msgs=2475,
            )
            self.advance_days(1)
        profile = profiler.get_profile("app", "u")
        assert len(profile["summaries"]) == 1
        assert profiler.get_ratio("app", "u") == 0.66
        profiler.close()

    def test_mixed_v10_f45_b45_r10_4089(self) -> None:
        """Mixed-verdict windows archive each counter correctly."""
        profiler: UserProfiler = UserProfiler(":memory:", ":memory:", 91)
        for _ in range(91):
            profiler.record(
                "app",
                "u",
                total_msgs=10,
                flagged_msgs=4,
                blocked_msgs=4,
                reviewed_msgs=1,
            )
            self.advance_days(1)
        profile = profiler.get_profile("app", "u")
        assert len(profile["summaries"]) == 1
        assert profiler.get_ratio("app", "u") == 0.8
        profiler.close()

    def test_mixed_v20_f45_b45_r10_4090(self) -> None:
        """Mixed-verdict windows archive each counter correctly."""
        profiler: UserProfiler = UserProfiler(":memory:", ":memory:", 91)
        for _ in range(91):
            profiler.record(
                "app",
                "u",
                total_msgs=20,
                flagged_msgs=9,
                blocked_msgs=9,
                reviewed_msgs=2,
            )
            self.advance_days(1)
        profile = profiler.get_profile("app", "u")
        assert len(profile["summaries"]) == 1
        assert profiler.get_ratio("app", "u") == 0.9
        profiler.close()

    def test_mixed_v50_f45_b45_r10_4091(self) -> None:
        """Mixed-verdict windows archive each counter correctly."""
        profiler: UserProfiler = UserProfiler(":memory:", ":memory:", 91)
        for _ in range(91):
            profiler.record(
                "app",
                "u",
                total_msgs=50,
                flagged_msgs=22,
                blocked_msgs=22,
                reviewed_msgs=5,
            )
            self.advance_days(1)
        profile = profiler.get_profile("app", "u")
        assert len(profile["summaries"]) == 1
        assert profiler.get_ratio("app", "u") == 0.88
        profiler.close()

    def test_mixed_v100_f45_b45_r10_4092(self) -> None:
        """Mixed-verdict windows archive each counter correctly."""
        profiler: UserProfiler = UserProfiler(":memory:", ":memory:", 91)
        for _ in range(91):
            profiler.record(
                "app",
                "u",
                total_msgs=100,
                flagged_msgs=45,
                blocked_msgs=45,
                reviewed_msgs=10,
            )
            self.advance_days(1)
        profile = profiler.get_profile("app", "u")
        assert len(profile["summaries"]) == 1
        assert profiler.get_ratio("app", "u") == 0.9
        profiler.close()

    def test_mixed_v200_f45_b45_r10_4093(self) -> None:
        """Mixed-verdict windows archive each counter correctly."""
        profiler: UserProfiler = UserProfiler(":memory:", ":memory:", 91)
        for _ in range(91):
            profiler.record(
                "app",
                "u",
                total_msgs=200,
                flagged_msgs=90,
                blocked_msgs=90,
                reviewed_msgs=20,
            )
            self.advance_days(1)
        profile = profiler.get_profile("app", "u")
        assert len(profile["summaries"]) == 1
        assert profiler.get_ratio("app", "u") == 0.9
        profiler.close()

    def test_mixed_v500_f45_b45_r10_4094(self) -> None:
        """Mixed-verdict windows archive each counter correctly."""
        profiler: UserProfiler = UserProfiler(":memory:", ":memory:", 91)
        for _ in range(91):
            profiler.record(
                "app",
                "u",
                total_msgs=500,
                flagged_msgs=225,
                blocked_msgs=225,
                reviewed_msgs=50,
            )
            self.advance_days(1)
        profile = profiler.get_profile("app", "u")
        assert len(profile["summaries"]) == 1
        assert profiler.get_ratio("app", "u") == 0.9
        profiler.close()

    def test_mixed_v1000_f45_b45_r10_4095(self) -> None:
        """Mixed-verdict windows archive each counter correctly."""
        profiler: UserProfiler = UserProfiler(":memory:", ":memory:", 91)
        for _ in range(91):
            profiler.record(
                "app",
                "u",
                total_msgs=1000,
                flagged_msgs=450,
                blocked_msgs=450,
                reviewed_msgs=100,
            )
            self.advance_days(1)
        profile = profiler.get_profile("app", "u")
        assert len(profile["summaries"]) == 1
        assert profiler.get_ratio("app", "u") == 0.9
        profiler.close()

    def test_mixed_v2500_f45_b45_r10_4096(self) -> None:
        """Mixed-verdict windows archive each counter correctly."""
        profiler: UserProfiler = UserProfiler(":memory:", ":memory:", 91)
        for _ in range(91):
            profiler.record(
                "app",
                "u",
                total_msgs=2500,
                flagged_msgs=1125,
                blocked_msgs=1125,
                reviewed_msgs=250,
            )
            self.advance_days(1)
        profile = profiler.get_profile("app", "u")
        assert len(profile["summaries"]) == 1
        assert profiler.get_ratio("app", "u") == 0.9
        profiler.close()

    def test_mixed_v5000_f45_b45_r10_4097(self) -> None:
        """Mixed-verdict windows archive each counter correctly."""
        profiler: UserProfiler = UserProfiler(":memory:", ":memory:", 91)
        for _ in range(91):
            profiler.record(
                "app",
                "u",
                total_msgs=5000,
                flagged_msgs=2250,
                blocked_msgs=2250,
                reviewed_msgs=500,
            )
            self.advance_days(1)
        profile = profiler.get_profile("app", "u")
        assert len(profile["summaries"]) == 1
        assert profiler.get_ratio("app", "u") == 0.9
        profiler.close()

    def test_mixed_v7500_f45_b45_r10_4098(self) -> None:
        """Mixed-verdict windows archive each counter correctly."""
        profiler: UserProfiler = UserProfiler(":memory:", ":memory:", 91)
        for _ in range(91):
            profiler.record(
                "app",
                "u",
                total_msgs=7500,
                flagged_msgs=3375,
                blocked_msgs=3375,
                reviewed_msgs=750,
            )
            self.advance_days(1)
        profile = profiler.get_profile("app", "u")
        assert len(profile["summaries"]) == 1
        assert profiler.get_ratio("app", "u") == 0.9
        profiler.close()

    def test_mixed_v10_f55_b20_r20_4099(self) -> None:
        """Mixed-verdict windows archive each counter correctly."""
        profiler: UserProfiler = UserProfiler(":memory:", ":memory:", 91)
        for _ in range(91):
            profiler.record(
                "app",
                "u",
                total_msgs=10,
                flagged_msgs=6,
                blocked_msgs=2,
                reviewed_msgs=2,
            )
            self.advance_days(1)
        profile = profiler.get_profile("app", "u")
        assert len(profile["summaries"]) == 1
        assert profiler.get_ratio("app", "u") == 0.8
        profiler.close()

    def test_mixed_v20_f55_b20_r20_4100(self) -> None:
        """Mixed-verdict windows archive each counter correctly."""
        profiler: UserProfiler = UserProfiler(":memory:", ":memory:", 91)
        for _ in range(91):
            profiler.record(
                "app",
                "u",
                total_msgs=20,
                flagged_msgs=11,
                blocked_msgs=4,
                reviewed_msgs=4,
            )
            self.advance_days(1)
        profile = profiler.get_profile("app", "u")
        assert len(profile["summaries"]) == 1
        assert profiler.get_ratio("app", "u") == 0.75
        profiler.close()

    def test_mixed_v50_f55_b20_r20_4101(self) -> None:
        """Mixed-verdict windows archive each counter correctly."""
        profiler: UserProfiler = UserProfiler(":memory:", ":memory:", 91)
        for _ in range(91):
            profiler.record(
                "app",
                "u",
                total_msgs=50,
                flagged_msgs=28,
                blocked_msgs=10,
                reviewed_msgs=10,
            )
            self.advance_days(1)
        profile = profiler.get_profile("app", "u")
        assert len(profile["summaries"]) == 1
        assert profiler.get_ratio("app", "u") == 0.76
        profiler.close()

    def test_mixed_v100_f55_b20_r20_4102(self) -> None:
        """Mixed-verdict windows archive each counter correctly."""
        profiler: UserProfiler = UserProfiler(":memory:", ":memory:", 91)
        for _ in range(91):
            profiler.record(
                "app",
                "u",
                total_msgs=100,
                flagged_msgs=55,
                blocked_msgs=20,
                reviewed_msgs=20,
            )
            self.advance_days(1)
        profile = profiler.get_profile("app", "u")
        assert len(profile["summaries"]) == 1
        assert profiler.get_ratio("app", "u") == 0.75
        profiler.close()

    def test_mixed_v200_f55_b20_r20_4103(self) -> None:
        """Mixed-verdict windows archive each counter correctly."""
        profiler: UserProfiler = UserProfiler(":memory:", ":memory:", 91)
        for _ in range(91):
            profiler.record(
                "app",
                "u",
                total_msgs=200,
                flagged_msgs=110,
                blocked_msgs=40,
                reviewed_msgs=40,
            )
            self.advance_days(1)
        profile = profiler.get_profile("app", "u")
        assert len(profile["summaries"]) == 1
        assert profiler.get_ratio("app", "u") == 0.75
        profiler.close()

    def test_mixed_v500_f55_b20_r20_4104(self) -> None:
        """Mixed-verdict windows archive each counter correctly."""
        profiler: UserProfiler = UserProfiler(":memory:", ":memory:", 91)
        for _ in range(91):
            profiler.record(
                "app",
                "u",
                total_msgs=500,
                flagged_msgs=275,
                blocked_msgs=100,
                reviewed_msgs=100,
            )
            self.advance_days(1)
        profile = profiler.get_profile("app", "u")
        assert len(profile["summaries"]) == 1
        assert profiler.get_ratio("app", "u") == 0.75
        profiler.close()

    def test_mixed_v1000_f55_b20_r20_4105(self) -> None:
        """Mixed-verdict windows archive each counter correctly."""
        profiler: UserProfiler = UserProfiler(":memory:", ":memory:", 91)
        for _ in range(91):
            profiler.record(
                "app",
                "u",
                total_msgs=1000,
                flagged_msgs=550,
                blocked_msgs=200,
                reviewed_msgs=200,
            )
            self.advance_days(1)
        profile = profiler.get_profile("app", "u")
        assert len(profile["summaries"]) == 1
        assert profiler.get_ratio("app", "u") == 0.75
        profiler.close()

    def test_mixed_v2500_f55_b20_r20_4106(self) -> None:
        """Mixed-verdict windows archive each counter correctly."""
        profiler: UserProfiler = UserProfiler(":memory:", ":memory:", 91)
        for _ in range(91):
            profiler.record(
                "app",
                "u",
                total_msgs=2500,
                flagged_msgs=1375,
                blocked_msgs=500,
                reviewed_msgs=500,
            )
            self.advance_days(1)
        profile = profiler.get_profile("app", "u")
        assert len(profile["summaries"]) == 1
        assert profiler.get_ratio("app", "u") == 0.75
        profiler.close()

    def test_mixed_v5000_f55_b20_r20_4107(self) -> None:
        """Mixed-verdict windows archive each counter correctly."""
        profiler: UserProfiler = UserProfiler(":memory:", ":memory:", 91)
        for _ in range(91):
            profiler.record(
                "app",
                "u",
                total_msgs=5000,
                flagged_msgs=2750,
                blocked_msgs=1000,
                reviewed_msgs=1000,
            )
            self.advance_days(1)
        profile = profiler.get_profile("app", "u")
        assert len(profile["summaries"]) == 1
        assert profiler.get_ratio("app", "u") == 0.75
        profiler.close()

    def test_mixed_v7500_f55_b20_r20_4108(self) -> None:
        """Mixed-verdict windows archive each counter correctly."""
        profiler: UserProfiler = UserProfiler(":memory:", ":memory:", 91)
        for _ in range(91):
            profiler.record(
                "app",
                "u",
                total_msgs=7500,
                flagged_msgs=4125,
                blocked_msgs=1500,
                reviewed_msgs=1500,
            )
            self.advance_days(1)
        profile = profiler.get_profile("app", "u")
        assert len(profile["summaries"]) == 1
        assert profiler.get_ratio("app", "u") == 0.75
        profiler.close()
