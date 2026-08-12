"""Phase 2 archive cycle tests (generated).

Volume and percentage matrices, multi-cycle chains, multi-user/app
archives and boundary edges under the frozen clock."""

# multilingual fixtures use non-ASCII on purpose
from __future__ import annotations

from app.profiling.user_profiler import UserProfiler
from tests.base_test import BaseTest


class TestMixedArchive(BaseTest):
    """MixedArchive scenarios."""

    def test_mixed_v10_f65_b10_r25_4109(self) -> None:
        """Mixed-verdict windows archive each counter correctly."""
        profiler: UserProfiler = UserProfiler(":memory:", ":memory:", 91)
        for _ in range(91):
            profiler.record(
                "app",
                "u",
                total_msgs=10,
                flagged_msgs=6,
                blocked_msgs=1,
                reviewed_msgs=2,
            )
            self.advance_days(1)
        profile = profiler.get_profile("app", "u")
        assert len(profile["summaries"]) == 1
        assert profiler.get_ratio("app", "u") == 0.7
        profiler.close()

    def test_mixed_v20_f65_b10_r25_4110(self) -> None:
        """Mixed-verdict windows archive each counter correctly."""
        profiler: UserProfiler = UserProfiler(":memory:", ":memory:", 91)
        for _ in range(91):
            profiler.record(
                "app",
                "u",
                total_msgs=20,
                flagged_msgs=13,
                blocked_msgs=2,
                reviewed_msgs=5,
            )
            self.advance_days(1)
        profile = profiler.get_profile("app", "u")
        assert len(profile["summaries"]) == 1
        assert profiler.get_ratio("app", "u") == 0.75
        profiler.close()

    def test_mixed_v50_f65_b10_r25_4111(self) -> None:
        """Mixed-verdict windows archive each counter correctly."""
        profiler: UserProfiler = UserProfiler(":memory:", ":memory:", 91)
        for _ in range(91):
            profiler.record(
                "app",
                "u",
                total_msgs=50,
                flagged_msgs=32,
                blocked_msgs=5,
                reviewed_msgs=12,
            )
            self.advance_days(1)
        profile = profiler.get_profile("app", "u")
        assert len(profile["summaries"]) == 1
        assert profiler.get_ratio("app", "u") == 0.74
        profiler.close()

    def test_mixed_v100_f65_b10_r25_4112(self) -> None:
        """Mixed-verdict windows archive each counter correctly."""
        profiler: UserProfiler = UserProfiler(":memory:", ":memory:", 91)
        for _ in range(91):
            profiler.record(
                "app",
                "u",
                total_msgs=100,
                flagged_msgs=65,
                blocked_msgs=10,
                reviewed_msgs=25,
            )
            self.advance_days(1)
        profile = profiler.get_profile("app", "u")
        assert len(profile["summaries"]) == 1
        assert profiler.get_ratio("app", "u") == 0.75
        profiler.close()

    def test_mixed_v200_f65_b10_r25_4113(self) -> None:
        """Mixed-verdict windows archive each counter correctly."""
        profiler: UserProfiler = UserProfiler(":memory:", ":memory:", 91)
        for _ in range(91):
            profiler.record(
                "app",
                "u",
                total_msgs=200,
                flagged_msgs=130,
                blocked_msgs=20,
                reviewed_msgs=50,
            )
            self.advance_days(1)
        profile = profiler.get_profile("app", "u")
        assert len(profile["summaries"]) == 1
        assert profiler.get_ratio("app", "u") == 0.75
        profiler.close()

    def test_mixed_v500_f65_b10_r25_4114(self) -> None:
        """Mixed-verdict windows archive each counter correctly."""
        profiler: UserProfiler = UserProfiler(":memory:", ":memory:", 91)
        for _ in range(91):
            profiler.record(
                "app",
                "u",
                total_msgs=500,
                flagged_msgs=325,
                blocked_msgs=50,
                reviewed_msgs=125,
            )
            self.advance_days(1)
        profile = profiler.get_profile("app", "u")
        assert len(profile["summaries"]) == 1
        assert profiler.get_ratio("app", "u") == 0.75
        profiler.close()

    def test_mixed_v1000_f65_b10_r25_4115(self) -> None:
        """Mixed-verdict windows archive each counter correctly."""
        profiler: UserProfiler = UserProfiler(":memory:", ":memory:", 91)
        for _ in range(91):
            profiler.record(
                "app",
                "u",
                total_msgs=1000,
                flagged_msgs=650,
                blocked_msgs=100,
                reviewed_msgs=250,
            )
            self.advance_days(1)
        profile = profiler.get_profile("app", "u")
        assert len(profile["summaries"]) == 1
        assert profiler.get_ratio("app", "u") == 0.75
        profiler.close()

    def test_mixed_v2500_f65_b10_r25_4116(self) -> None:
        """Mixed-verdict windows archive each counter correctly."""
        profiler: UserProfiler = UserProfiler(":memory:", ":memory:", 91)
        for _ in range(91):
            profiler.record(
                "app",
                "u",
                total_msgs=2500,
                flagged_msgs=1625,
                blocked_msgs=250,
                reviewed_msgs=625,
            )
            self.advance_days(1)
        profile = profiler.get_profile("app", "u")
        assert len(profile["summaries"]) == 1
        assert profiler.get_ratio("app", "u") == 0.75
        profiler.close()

    def test_mixed_v5000_f65_b10_r25_4117(self) -> None:
        """Mixed-verdict windows archive each counter correctly."""
        profiler: UserProfiler = UserProfiler(":memory:", ":memory:", 91)
        for _ in range(91):
            profiler.record(
                "app",
                "u",
                total_msgs=5000,
                flagged_msgs=3250,
                blocked_msgs=500,
                reviewed_msgs=1250,
            )
            self.advance_days(1)
        profile = profiler.get_profile("app", "u")
        assert len(profile["summaries"]) == 1
        assert profiler.get_ratio("app", "u") == 0.75
        profiler.close()

    def test_mixed_v7500_f65_b10_r25_4118(self) -> None:
        """Mixed-verdict windows archive each counter correctly."""
        profiler: UserProfiler = UserProfiler(":memory:", ":memory:", 91)
        for _ in range(91):
            profiler.record(
                "app",
                "u",
                total_msgs=7500,
                flagged_msgs=4875,
                blocked_msgs=750,
                reviewed_msgs=1875,
            )
            self.advance_days(1)
        profile = profiler.get_profile("app", "u")
        assert len(profile["summaries"]) == 1
        assert profiler.get_ratio("app", "u") == 0.75
        profiler.close()

    def test_mixed_v10_f75_b15_r10_4119(self) -> None:
        """Mixed-verdict windows archive each counter correctly."""
        profiler: UserProfiler = UserProfiler(":memory:", ":memory:", 91)
        for _ in range(91):
            profiler.record(
                "app",
                "u",
                total_msgs=10,
                flagged_msgs=8,
                blocked_msgs=2,
                reviewed_msgs=1,
            )
            self.advance_days(1)
        profile = profiler.get_profile("app", "u")
        assert len(profile["summaries"]) == 1
        assert profiler.get_ratio("app", "u") == 1.0
        profiler.close()

    def test_mixed_v20_f75_b15_r10_4120(self) -> None:
        """Mixed-verdict windows archive each counter correctly."""
        profiler: UserProfiler = UserProfiler(":memory:", ":memory:", 91)
        for _ in range(91):
            profiler.record(
                "app",
                "u",
                total_msgs=20,
                flagged_msgs=15,
                blocked_msgs=3,
                reviewed_msgs=2,
            )
            self.advance_days(1)
        profile = profiler.get_profile("app", "u")
        assert len(profile["summaries"]) == 1
        assert profiler.get_ratio("app", "u") == 0.9
        profiler.close()

    def test_mixed_v50_f75_b15_r10_4121(self) -> None:
        """Mixed-verdict windows archive each counter correctly."""
        profiler: UserProfiler = UserProfiler(":memory:", ":memory:", 91)
        for _ in range(91):
            profiler.record(
                "app",
                "u",
                total_msgs=50,
                flagged_msgs=38,
                blocked_msgs=8,
                reviewed_msgs=5,
            )
            self.advance_days(1)
        profile = profiler.get_profile("app", "u")
        assert len(profile["summaries"]) == 1
        assert profiler.get_ratio("app", "u") == 0.92
        profiler.close()

    def test_mixed_v100_f75_b15_r10_4122(self) -> None:
        """Mixed-verdict windows archive each counter correctly."""
        profiler: UserProfiler = UserProfiler(":memory:", ":memory:", 91)
        for _ in range(91):
            profiler.record(
                "app",
                "u",
                total_msgs=100,
                flagged_msgs=75,
                blocked_msgs=15,
                reviewed_msgs=10,
            )
            self.advance_days(1)
        profile = profiler.get_profile("app", "u")
        assert len(profile["summaries"]) == 1
        assert profiler.get_ratio("app", "u") == 0.9
        profiler.close()

    def test_mixed_v200_f75_b15_r10_4123(self) -> None:
        """Mixed-verdict windows archive each counter correctly."""
        profiler: UserProfiler = UserProfiler(":memory:", ":memory:", 91)
        for _ in range(91):
            profiler.record(
                "app",
                "u",
                total_msgs=200,
                flagged_msgs=150,
                blocked_msgs=30,
                reviewed_msgs=20,
            )
            self.advance_days(1)
        profile = profiler.get_profile("app", "u")
        assert len(profile["summaries"]) == 1
        assert profiler.get_ratio("app", "u") == 0.9
        profiler.close()

    def test_mixed_v500_f75_b15_r10_4124(self) -> None:
        """Mixed-verdict windows archive each counter correctly."""
        profiler: UserProfiler = UserProfiler(":memory:", ":memory:", 91)
        for _ in range(91):
            profiler.record(
                "app",
                "u",
                total_msgs=500,
                flagged_msgs=375,
                blocked_msgs=75,
                reviewed_msgs=50,
            )
            self.advance_days(1)
        profile = profiler.get_profile("app", "u")
        assert len(profile["summaries"]) == 1
        assert profiler.get_ratio("app", "u") == 0.9
        profiler.close()

    def test_mixed_v1000_f75_b15_r10_4125(self) -> None:
        """Mixed-verdict windows archive each counter correctly."""
        profiler: UserProfiler = UserProfiler(":memory:", ":memory:", 91)
        for _ in range(91):
            profiler.record(
                "app",
                "u",
                total_msgs=1000,
                flagged_msgs=750,
                blocked_msgs=150,
                reviewed_msgs=100,
            )
            self.advance_days(1)
        profile = profiler.get_profile("app", "u")
        assert len(profile["summaries"]) == 1
        assert profiler.get_ratio("app", "u") == 0.9
        profiler.close()

    def test_mixed_v2500_f75_b15_r10_4126(self) -> None:
        """Mixed-verdict windows archive each counter correctly."""
        profiler: UserProfiler = UserProfiler(":memory:", ":memory:", 91)
        for _ in range(91):
            profiler.record(
                "app",
                "u",
                total_msgs=2500,
                flagged_msgs=1875,
                blocked_msgs=375,
                reviewed_msgs=250,
            )
            self.advance_days(1)
        profile = profiler.get_profile("app", "u")
        assert len(profile["summaries"]) == 1
        assert profiler.get_ratio("app", "u") == 0.9
        profiler.close()

    def test_mixed_v5000_f75_b15_r10_4127(self) -> None:
        """Mixed-verdict windows archive each counter correctly."""
        profiler: UserProfiler = UserProfiler(":memory:", ":memory:", 91)
        for _ in range(91):
            profiler.record(
                "app",
                "u",
                total_msgs=5000,
                flagged_msgs=3750,
                blocked_msgs=750,
                reviewed_msgs=500,
            )
            self.advance_days(1)
        profile = profiler.get_profile("app", "u")
        assert len(profile["summaries"]) == 1
        assert profiler.get_ratio("app", "u") == 0.9
        profiler.close()

    def test_mixed_v7500_f75_b15_r10_4128(self) -> None:
        """Mixed-verdict windows archive each counter correctly."""
        profiler: UserProfiler = UserProfiler(":memory:", ":memory:", 91)
        for _ in range(91):
            profiler.record(
                "app",
                "u",
                total_msgs=7500,
                flagged_msgs=5625,
                blocked_msgs=1125,
                reviewed_msgs=750,
            )
            self.advance_days(1)
        profile = profiler.get_profile("app", "u")
        assert len(profile["summaries"]) == 1
        assert profiler.get_ratio("app", "u") == 0.9
        profiler.close()

    def test_mixed_v10_f85_b5_r10_4129(self) -> None:
        """Mixed-verdict windows archive each counter correctly."""
        profiler: UserProfiler = UserProfiler(":memory:", ":memory:", 91)
        for _ in range(91):
            profiler.record(
                "app",
                "u",
                total_msgs=10,
                flagged_msgs=8,
                blocked_msgs=0,
                reviewed_msgs=1,
            )
            self.advance_days(1)
        profile = profiler.get_profile("app", "u")
        assert len(profile["summaries"]) == 1
        assert profiler.get_ratio("app", "u") == 0.8
        profiler.close()

    def test_mixed_v20_f85_b5_r10_4130(self) -> None:
        """Mixed-verdict windows archive each counter correctly."""
        profiler: UserProfiler = UserProfiler(":memory:", ":memory:", 91)
        for _ in range(91):
            profiler.record(
                "app",
                "u",
                total_msgs=20,
                flagged_msgs=17,
                blocked_msgs=1,
                reviewed_msgs=2,
            )
            self.advance_days(1)
        profile = profiler.get_profile("app", "u")
        assert len(profile["summaries"]) == 1
        assert profiler.get_ratio("app", "u") == 0.9
        profiler.close()

    def test_mixed_v50_f85_b5_r10_4131(self) -> None:
        """Mixed-verdict windows archive each counter correctly."""
        profiler: UserProfiler = UserProfiler(":memory:", ":memory:", 91)
        for _ in range(91):
            profiler.record(
                "app",
                "u",
                total_msgs=50,
                flagged_msgs=42,
                blocked_msgs=2,
                reviewed_msgs=5,
            )
            self.advance_days(1)
        profile = profiler.get_profile("app", "u")
        assert len(profile["summaries"]) == 1
        assert profiler.get_ratio("app", "u") == 0.88
        profiler.close()

    def test_mixed_v100_f85_b5_r10_4132(self) -> None:
        """Mixed-verdict windows archive each counter correctly."""
        profiler: UserProfiler = UserProfiler(":memory:", ":memory:", 91)
        for _ in range(91):
            profiler.record(
                "app",
                "u",
                total_msgs=100,
                flagged_msgs=85,
                blocked_msgs=5,
                reviewed_msgs=10,
            )
            self.advance_days(1)
        profile = profiler.get_profile("app", "u")
        assert len(profile["summaries"]) == 1
        assert profiler.get_ratio("app", "u") == 0.9
        profiler.close()

    def test_mixed_v200_f85_b5_r10_4133(self) -> None:
        """Mixed-verdict windows archive each counter correctly."""
        profiler: UserProfiler = UserProfiler(":memory:", ":memory:", 91)
        for _ in range(91):
            profiler.record(
                "app",
                "u",
                total_msgs=200,
                flagged_msgs=170,
                blocked_msgs=10,
                reviewed_msgs=20,
            )
            self.advance_days(1)
        profile = profiler.get_profile("app", "u")
        assert len(profile["summaries"]) == 1
        assert profiler.get_ratio("app", "u") == 0.9
        profiler.close()

    def test_mixed_v500_f85_b5_r10_4134(self) -> None:
        """Mixed-verdict windows archive each counter correctly."""
        profiler: UserProfiler = UserProfiler(":memory:", ":memory:", 91)
        for _ in range(91):
            profiler.record(
                "app",
                "u",
                total_msgs=500,
                flagged_msgs=425,
                blocked_msgs=25,
                reviewed_msgs=50,
            )
            self.advance_days(1)
        profile = profiler.get_profile("app", "u")
        assert len(profile["summaries"]) == 1
        assert profiler.get_ratio("app", "u") == 0.9
        profiler.close()

    def test_mixed_v1000_f85_b5_r10_4135(self) -> None:
        """Mixed-verdict windows archive each counter correctly."""
        profiler: UserProfiler = UserProfiler(":memory:", ":memory:", 91)
        for _ in range(91):
            profiler.record(
                "app",
                "u",
                total_msgs=1000,
                flagged_msgs=850,
                blocked_msgs=50,
                reviewed_msgs=100,
            )
            self.advance_days(1)
        profile = profiler.get_profile("app", "u")
        assert len(profile["summaries"]) == 1
        assert profiler.get_ratio("app", "u") == 0.9
        profiler.close()

    def test_mixed_v2500_f85_b5_r10_4136(self) -> None:
        """Mixed-verdict windows archive each counter correctly."""
        profiler: UserProfiler = UserProfiler(":memory:", ":memory:", 91)
        for _ in range(91):
            profiler.record(
                "app",
                "u",
                total_msgs=2500,
                flagged_msgs=2125,
                blocked_msgs=125,
                reviewed_msgs=250,
            )
            self.advance_days(1)
        profile = profiler.get_profile("app", "u")
        assert len(profile["summaries"]) == 1
        assert profiler.get_ratio("app", "u") == 0.9
        profiler.close()

    def test_mixed_v5000_f85_b5_r10_4137(self) -> None:
        """Mixed-verdict windows archive each counter correctly."""
        profiler: UserProfiler = UserProfiler(":memory:", ":memory:", 91)
        for _ in range(91):
            profiler.record(
                "app",
                "u",
                total_msgs=5000,
                flagged_msgs=4250,
                blocked_msgs=250,
                reviewed_msgs=500,
            )
            self.advance_days(1)
        profile = profiler.get_profile("app", "u")
        assert len(profile["summaries"]) == 1
        assert profiler.get_ratio("app", "u") == 0.9
        profiler.close()

    def test_mixed_v7500_f85_b5_r10_4138(self) -> None:
        """Mixed-verdict windows archive each counter correctly."""
        profiler: UserProfiler = UserProfiler(":memory:", ":memory:", 91)
        for _ in range(91):
            profiler.record(
                "app",
                "u",
                total_msgs=7500,
                flagged_msgs=6375,
                blocked_msgs=375,
                reviewed_msgs=750,
            )
            self.advance_days(1)
        profile = profiler.get_profile("app", "u")
        assert len(profile["summaries"]) == 1
        assert profiler.get_ratio("app", "u") == 0.9
        profiler.close()

    def test_mixed_v10_f95_b0_r5_4139(self) -> None:
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

    def test_mixed_v20_f95_b0_r5_4140(self) -> None:
        """Mixed-verdict windows archive each counter correctly."""
        profiler: UserProfiler = UserProfiler(":memory:", ":memory:", 91)
        for _ in range(91):
            profiler.record(
                "app",
                "u",
                total_msgs=20,
                flagged_msgs=19,
                blocked_msgs=0,
                reviewed_msgs=1,
            )
            self.advance_days(1)
        profile = profiler.get_profile("app", "u")
        assert len(profile["summaries"]) == 1
        assert profiler.get_ratio("app", "u") == 0.95
        profiler.close()

    def test_mixed_v50_f95_b0_r5_4141(self) -> None:
        """Mixed-verdict windows archive each counter correctly."""
        profiler: UserProfiler = UserProfiler(":memory:", ":memory:", 91)
        for _ in range(91):
            profiler.record(
                "app",
                "u",
                total_msgs=50,
                flagged_msgs=48,
                blocked_msgs=0,
                reviewed_msgs=2,
            )
            self.advance_days(1)
        profile = profiler.get_profile("app", "u")
        assert len(profile["summaries"]) == 1
        assert profiler.get_ratio("app", "u") == 0.96
        profiler.close()

    def test_mixed_v100_f95_b0_r5_4142(self) -> None:
        """Mixed-verdict windows archive each counter correctly."""
        profiler: UserProfiler = UserProfiler(":memory:", ":memory:", 91)
        for _ in range(91):
            profiler.record(
                "app",
                "u",
                total_msgs=100,
                flagged_msgs=95,
                blocked_msgs=0,
                reviewed_msgs=5,
            )
            self.advance_days(1)
        profile = profiler.get_profile("app", "u")
        assert len(profile["summaries"]) == 1
        assert profiler.get_ratio("app", "u") == 0.95
        profiler.close()

    def test_mixed_v200_f95_b0_r5_4143(self) -> None:
        """Mixed-verdict windows archive each counter correctly."""
        profiler: UserProfiler = UserProfiler(":memory:", ":memory:", 91)
        for _ in range(91):
            profiler.record(
                "app",
                "u",
                total_msgs=200,
                flagged_msgs=190,
                blocked_msgs=0,
                reviewed_msgs=10,
            )
            self.advance_days(1)
        profile = profiler.get_profile("app", "u")
        assert len(profile["summaries"]) == 1
        assert profiler.get_ratio("app", "u") == 0.95
        profiler.close()

    def test_mixed_v500_f95_b0_r5_4144(self) -> None:
        """Mixed-verdict windows archive each counter correctly."""
        profiler: UserProfiler = UserProfiler(":memory:", ":memory:", 91)
        for _ in range(91):
            profiler.record(
                "app",
                "u",
                total_msgs=500,
                flagged_msgs=475,
                blocked_msgs=0,
                reviewed_msgs=25,
            )
            self.advance_days(1)
        profile = profiler.get_profile("app", "u")
        assert len(profile["summaries"]) == 1
        assert profiler.get_ratio("app", "u") == 0.95
        profiler.close()

    def test_mixed_v1000_f95_b0_r5_4145(self) -> None:
        """Mixed-verdict windows archive each counter correctly."""
        profiler: UserProfiler = UserProfiler(":memory:", ":memory:", 91)
        for _ in range(91):
            profiler.record(
                "app",
                "u",
                total_msgs=1000,
                flagged_msgs=950,
                blocked_msgs=0,
                reviewed_msgs=50,
            )
            self.advance_days(1)
        profile = profiler.get_profile("app", "u")
        assert len(profile["summaries"]) == 1
        assert profiler.get_ratio("app", "u") == 0.95
        profiler.close()

    def test_mixed_v2500_f95_b0_r5_4146(self) -> None:
        """Mixed-verdict windows archive each counter correctly."""
        profiler: UserProfiler = UserProfiler(":memory:", ":memory:", 91)
        for _ in range(91):
            profiler.record(
                "app",
                "u",
                total_msgs=2500,
                flagged_msgs=2375,
                blocked_msgs=0,
                reviewed_msgs=125,
            )
            self.advance_days(1)
        profile = profiler.get_profile("app", "u")
        assert len(profile["summaries"]) == 1
        assert profiler.get_ratio("app", "u") == 0.95
        profiler.close()

    def test_mixed_v5000_f95_b0_r5_4147(self) -> None:
        """Mixed-verdict windows archive each counter correctly."""
        profiler: UserProfiler = UserProfiler(":memory:", ":memory:", 91)
        for _ in range(91):
            profiler.record(
                "app",
                "u",
                total_msgs=5000,
                flagged_msgs=4750,
                blocked_msgs=0,
                reviewed_msgs=250,
            )
            self.advance_days(1)
        profile = profiler.get_profile("app", "u")
        assert len(profile["summaries"]) == 1
        assert profiler.get_ratio("app", "u") == 0.95
        profiler.close()

    def test_mixed_v7500_f95_b0_r5_4148(self) -> None:
        """Mixed-verdict windows archive each counter correctly."""
        profiler: UserProfiler = UserProfiler(":memory:", ":memory:", 91)
        for _ in range(91):
            profiler.record(
                "app",
                "u",
                total_msgs=7500,
                flagged_msgs=7125,
                blocked_msgs=0,
                reviewed_msgs=375,
            )
            self.advance_days(1)
        profile = profiler.get_profile("app", "u")
        assert len(profile["summaries"]) == 1
        assert profiler.get_ratio("app", "u") == 0.95
        profiler.close()

    def test_mixed_v10_f12_b8_r4_4149(self) -> None:
        """Mixed-verdict windows archive each counter correctly."""
        profiler: UserProfiler = UserProfiler(":memory:", ":memory:", 91)
        for _ in range(91):
            profiler.record(
                "app",
                "u",
                total_msgs=10,
                flagged_msgs=1,
                blocked_msgs=1,
                reviewed_msgs=0,
            )
            self.advance_days(1)
        profile = profiler.get_profile("app", "u")
        assert len(profile["summaries"]) == 1
        assert profiler.get_ratio("app", "u") == 0.2
        profiler.close()

    def test_mixed_v20_f12_b8_r4_4150(self) -> None:
        """Mixed-verdict windows archive each counter correctly."""
        profiler: UserProfiler = UserProfiler(":memory:", ":memory:", 91)
        for _ in range(91):
            profiler.record(
                "app",
                "u",
                total_msgs=20,
                flagged_msgs=2,
                blocked_msgs=2,
                reviewed_msgs=1,
            )
            self.advance_days(1)
        profile = profiler.get_profile("app", "u")
        assert len(profile["summaries"]) == 1
        assert profiler.get_ratio("app", "u") == 0.2
        profiler.close()

    def test_mixed_v50_f12_b8_r4_4151(self) -> None:
        """Mixed-verdict windows archive each counter correctly."""
        profiler: UserProfiler = UserProfiler(":memory:", ":memory:", 91)
        for _ in range(91):
            profiler.record(
                "app",
                "u",
                total_msgs=50,
                flagged_msgs=6,
                blocked_msgs=4,
                reviewed_msgs=2,
            )
            self.advance_days(1)
        profile = profiler.get_profile("app", "u")
        assert len(profile["summaries"]) == 1
        assert profiler.get_ratio("app", "u") == 0.2
        profiler.close()

    def test_mixed_v100_f12_b8_r4_4152(self) -> None:
        """Mixed-verdict windows archive each counter correctly."""
        profiler: UserProfiler = UserProfiler(":memory:", ":memory:", 91)
        for _ in range(91):
            profiler.record(
                "app",
                "u",
                total_msgs=100,
                flagged_msgs=12,
                blocked_msgs=8,
                reviewed_msgs=4,
            )
            self.advance_days(1)
        profile = profiler.get_profile("app", "u")
        assert len(profile["summaries"]) == 1
        assert profiler.get_ratio("app", "u") == 0.2
        profiler.close()

    def test_mixed_v200_f12_b8_r4_4153(self) -> None:
        """Mixed-verdict windows archive each counter correctly."""
        profiler: UserProfiler = UserProfiler(":memory:", ":memory:", 91)
        for _ in range(91):
            profiler.record(
                "app",
                "u",
                total_msgs=200,
                flagged_msgs=24,
                blocked_msgs=16,
                reviewed_msgs=8,
            )
            self.advance_days(1)
        profile = profiler.get_profile("app", "u")
        assert len(profile["summaries"]) == 1
        assert profiler.get_ratio("app", "u") == 0.2
        profiler.close()

    def test_mixed_v500_f12_b8_r4_4154(self) -> None:
        """Mixed-verdict windows archive each counter correctly."""
        profiler: UserProfiler = UserProfiler(":memory:", ":memory:", 91)
        for _ in range(91):
            profiler.record(
                "app",
                "u",
                total_msgs=500,
                flagged_msgs=60,
                blocked_msgs=40,
                reviewed_msgs=20,
            )
            self.advance_days(1)
        profile = profiler.get_profile("app", "u")
        assert len(profile["summaries"]) == 1
        assert profiler.get_ratio("app", "u") == 0.2
        profiler.close()

    def test_mixed_v1000_f12_b8_r4_4155(self) -> None:
        """Mixed-verdict windows archive each counter correctly."""
        profiler: UserProfiler = UserProfiler(":memory:", ":memory:", 91)
        for _ in range(91):
            profiler.record(
                "app",
                "u",
                total_msgs=1000,
                flagged_msgs=120,
                blocked_msgs=80,
                reviewed_msgs=40,
            )
            self.advance_days(1)
        profile = profiler.get_profile("app", "u")
        assert len(profile["summaries"]) == 1
        assert profiler.get_ratio("app", "u") == 0.2
        profiler.close()

    def test_mixed_v2500_f12_b8_r4_4156(self) -> None:
        """Mixed-verdict windows archive each counter correctly."""
        profiler: UserProfiler = UserProfiler(":memory:", ":memory:", 91)
        for _ in range(91):
            profiler.record(
                "app",
                "u",
                total_msgs=2500,
                flagged_msgs=300,
                blocked_msgs=200,
                reviewed_msgs=100,
            )
            self.advance_days(1)
        profile = profiler.get_profile("app", "u")
        assert len(profile["summaries"]) == 1
        assert profiler.get_ratio("app", "u") == 0.2
        profiler.close()

    def test_mixed_v5000_f12_b8_r4_4157(self) -> None:
        """Mixed-verdict windows archive each counter correctly."""
        profiler: UserProfiler = UserProfiler(":memory:", ":memory:", 91)
        for _ in range(91):
            profiler.record(
                "app",
                "u",
                total_msgs=5000,
                flagged_msgs=600,
                blocked_msgs=400,
                reviewed_msgs=200,
            )
            self.advance_days(1)
        profile = profiler.get_profile("app", "u")
        assert len(profile["summaries"]) == 1
        assert profiler.get_ratio("app", "u") == 0.2
        profiler.close()

    def test_mixed_v7500_f12_b8_r4_4158(self) -> None:
        """Mixed-verdict windows archive each counter correctly."""
        profiler: UserProfiler = UserProfiler(":memory:", ":memory:", 91)
        for _ in range(91):
            profiler.record(
                "app",
                "u",
                total_msgs=7500,
                flagged_msgs=900,
                blocked_msgs=600,
                reviewed_msgs=300,
            )
            self.advance_days(1)
        profile = profiler.get_profile("app", "u")
        assert len(profile["summaries"]) == 1
        assert profiler.get_ratio("app", "u") == 0.2
        profiler.close()


class TestArchiveEdges(BaseTest):
    """ArchiveEdges scenarios."""

    def test_edge_0_4159(self) -> None:
        """Rare boundary states keep archive invariants."""
        profiler: UserProfiler = UserProfiler(":memory:", ":memory:", 91)
        for _ in range(91):
            profiler.record("app", "u", total_msgs=1, flagged_msgs=1)
            self.advance_days(1)
        assert profiler.get_ratio("app", "u") == 1.0
        profiler.close()

    def test_edge_1_4160(self) -> None:
        """Rare boundary states keep archive invariants."""
        profiler: UserProfiler = UserProfiler(":memory:", ":memory:", 91)
        for _ in range(91):
            profiler.record("app", "u", total_msgs=1)
            self.advance_days(1)
        assert profiler.get_ratio("app", "u") == 0.0
        profiler.close()

    def test_edge_2_4161(self) -> None:
        """Rare boundary states keep archive invariants."""
        profiler: UserProfiler = UserProfiler(":memory:", ":memory:", 3)
        for _ in range(3):
            profiler.record("app", "u", total_msgs=0)
            self.advance_days(1)
        summary = profiler.get_profile("app", "u")["summaries"][0]
        assert summary["total_msgs"] == 0
        profiler.close()

    def test_edge_3_4162(self) -> None:
        """Rare boundary states keep archive invariants."""
        profiler: UserProfiler = UserProfiler(":memory:", ":memory:", 91)
        profiler.record("app", "u", total_msgs=1)
        self.advance_days(1)
        self.advance_days(150)
        profiler.record("app", "u", total_msgs=1)
        stats = profiler.stats()
        assert stats["summary_count"] >= 1
        profiler.close()

    def test_edge_4_4163(self) -> None:
        """Rare boundary states keep archive invariants."""
        profiler: UserProfiler = UserProfiler(":memory:", ":memory:", 3)
        for _ in range(3):
            profiler.record("app", "u", total_msgs=1)
            self.advance_days(1)
        assert profiler.get_ratio("app", "ghost") == 0.0
        profiler.close()

    def test_edge_5_4164(self) -> None:
        """Rare boundary states keep archive invariants."""
        profiler: UserProfiler = UserProfiler(":memory:", ":memory:", 3)
        for _ in range(3):
            profiler.record("app", "u", total_msgs=1, blocked_msgs=1)
            self.advance_days(1)
        assert profiler.get_ratio("app", "u") == 1.0
        profiler.close()

    def test_edge_6_4165(self) -> None:
        """Rare boundary states keep archive invariants."""
        profiler: UserProfiler = UserProfiler(":memory:", ":memory:", 3)
        for _ in range(3):
            profiler.record("app", "u", total_msgs=1, reviewed_msgs=1)
            self.advance_days(1)
        assert profiler.get_ratio("app", "u") == 0.0
        profiler.close()

    def test_edge_7_4166(self) -> None:
        """Rare boundary states keep archive invariants."""
        profiler: UserProfiler = UserProfiler(":memory:", ":memory:", 3)
        for _ in range(3):
            profiler.record("app", "u", total_msgs=2, flagged_msgs=1)
            self.advance_days(1)
        assert profiler.get_ratio("app", "u") == 0.5
        profiler.close()

    def test_edge_8_4167(self) -> None:
        """Rare boundary states keep archive invariants."""
        profiler: UserProfiler = UserProfiler(":memory:", ":memory:", 91)
        for _ in range(91):
            profiler.record("app", "u", total_msgs=1, flagged_msgs=1)
            self.advance_days(1)
        assert profiler.get_ratio("app", "u") == 1.0
        profiler.close()

    def test_edge_9_4168(self) -> None:
        """Rare boundary states keep archive invariants."""
        profiler: UserProfiler = UserProfiler(":memory:", ":memory:", 91)
        for _ in range(91):
            profiler.record("app", "u", total_msgs=1)
            self.advance_days(1)
        assert profiler.get_ratio("app", "u") == 0.0
        profiler.close()

    def test_edge_10_4169(self) -> None:
        """Rare boundary states keep archive invariants."""
        profiler: UserProfiler = UserProfiler(":memory:", ":memory:", 3)
        for _ in range(3):
            profiler.record("app", "u", total_msgs=0)
            self.advance_days(1)
        summary = profiler.get_profile("app", "u")["summaries"][0]
        assert summary["total_msgs"] == 0
        profiler.close()

    def test_edge_11_4170(self) -> None:
        """Rare boundary states keep archive invariants."""
        profiler: UserProfiler = UserProfiler(":memory:", ":memory:", 91)
        profiler.record("app", "u", total_msgs=1)
        self.advance_days(1)
        self.advance_days(150)
        profiler.record("app", "u", total_msgs=1)
        stats = profiler.stats()
        assert stats["summary_count"] >= 1
        profiler.close()

    def test_edge_12_4171(self) -> None:
        """Rare boundary states keep archive invariants."""
        profiler: UserProfiler = UserProfiler(":memory:", ":memory:", 3)
        for _ in range(3):
            profiler.record("app", "u", total_msgs=1)
            self.advance_days(1)
        assert profiler.get_ratio("app", "ghost") == 0.0
        profiler.close()

    def test_edge_13_4172(self) -> None:
        """Rare boundary states keep archive invariants."""
        profiler: UserProfiler = UserProfiler(":memory:", ":memory:", 3)
        for _ in range(3):
            profiler.record("app", "u", total_msgs=1, blocked_msgs=1)
            self.advance_days(1)
        assert profiler.get_ratio("app", "u") == 1.0
        profiler.close()

    def test_edge_14_4173(self) -> None:
        """Rare boundary states keep archive invariants."""
        profiler: UserProfiler = UserProfiler(":memory:", ":memory:", 3)
        for _ in range(3):
            profiler.record("app", "u", total_msgs=1, reviewed_msgs=1)
            self.advance_days(1)
        assert profiler.get_ratio("app", "u") == 0.0
        profiler.close()

    def test_edge_15_4174(self) -> None:
        """Rare boundary states keep archive invariants."""
        profiler: UserProfiler = UserProfiler(":memory:", ":memory:", 3)
        for _ in range(3):
            profiler.record("app", "u", total_msgs=2, flagged_msgs=1)
            self.advance_days(1)
        assert profiler.get_ratio("app", "u") == 0.5
        profiler.close()

    def test_edge_16_4175(self) -> None:
        """Rare boundary states keep archive invariants."""
        profiler: UserProfiler = UserProfiler(":memory:", ":memory:", 91)
        for _ in range(91):
            profiler.record("app", "u", total_msgs=1, flagged_msgs=1)
            self.advance_days(1)
        assert profiler.get_ratio("app", "u") == 1.0
        profiler.close()

    def test_edge_17_4176(self) -> None:
        """Rare boundary states keep archive invariants."""
        profiler: UserProfiler = UserProfiler(":memory:", ":memory:", 91)
        for _ in range(91):
            profiler.record("app", "u", total_msgs=1)
            self.advance_days(1)
        assert profiler.get_ratio("app", "u") == 0.0
        profiler.close()

    def test_edge_18_4177(self) -> None:
        """Rare boundary states keep archive invariants."""
        profiler: UserProfiler = UserProfiler(":memory:", ":memory:", 3)
        for _ in range(3):
            profiler.record("app", "u", total_msgs=0)
            self.advance_days(1)
        summary = profiler.get_profile("app", "u")["summaries"][0]
        assert summary["total_msgs"] == 0
        profiler.close()

    def test_edge_19_4178(self) -> None:
        """Rare boundary states keep archive invariants."""
        profiler: UserProfiler = UserProfiler(":memory:", ":memory:", 91)
        profiler.record("app", "u", total_msgs=1)
        self.advance_days(1)
        self.advance_days(150)
        profiler.record("app", "u", total_msgs=1)
        stats = profiler.stats()
        assert stats["summary_count"] >= 1
        profiler.close()

    def test_edge_20_4179(self) -> None:
        """Rare boundary states keep archive invariants."""
        profiler: UserProfiler = UserProfiler(":memory:", ":memory:", 3)
        for _ in range(3):
            profiler.record("app", "u", total_msgs=1)
            self.advance_days(1)
        assert profiler.get_ratio("app", "ghost") == 0.0
        profiler.close()

    def test_edge_21_4180(self) -> None:
        """Rare boundary states keep archive invariants."""
        profiler: UserProfiler = UserProfiler(":memory:", ":memory:", 3)
        for _ in range(3):
            profiler.record("app", "u", total_msgs=1, blocked_msgs=1)
            self.advance_days(1)
        assert profiler.get_ratio("app", "u") == 1.0
        profiler.close()

    def test_edge_22_4181(self) -> None:
        """Rare boundary states keep archive invariants."""
        profiler: UserProfiler = UserProfiler(":memory:", ":memory:", 3)
        for _ in range(3):
            profiler.record("app", "u", total_msgs=1, reviewed_msgs=1)
            self.advance_days(1)
        assert profiler.get_ratio("app", "u") == 0.0
        profiler.close()

    def test_edge_23_4182(self) -> None:
        """Rare boundary states keep archive invariants."""
        profiler: UserProfiler = UserProfiler(":memory:", ":memory:", 3)
        for _ in range(3):
            profiler.record("app", "u", total_msgs=2, flagged_msgs=1)
            self.advance_days(1)
        assert profiler.get_ratio("app", "u") == 0.5
        profiler.close()

    def test_edge_24_4183(self) -> None:
        """Rare boundary states keep archive invariants."""
        profiler: UserProfiler = UserProfiler(":memory:", ":memory:", 91)
        for _ in range(91):
            profiler.record("app", "u", total_msgs=1, flagged_msgs=1)
            self.advance_days(1)
        assert profiler.get_ratio("app", "u") == 1.0
        profiler.close()

    def test_edge_25_4184(self) -> None:
        """Rare boundary states keep archive invariants."""
        profiler: UserProfiler = UserProfiler(":memory:", ":memory:", 91)
        for _ in range(91):
            profiler.record("app", "u", total_msgs=1)
            self.advance_days(1)
        assert profiler.get_ratio("app", "u") == 0.0
        profiler.close()

    def test_edge_26_4185(self) -> None:
        """Rare boundary states keep archive invariants."""
        profiler: UserProfiler = UserProfiler(":memory:", ":memory:", 3)
        for _ in range(3):
            profiler.record("app", "u", total_msgs=0)
            self.advance_days(1)
        summary = profiler.get_profile("app", "u")["summaries"][0]
        assert summary["total_msgs"] == 0
        profiler.close()

    def test_edge_27_4186(self) -> None:
        """Rare boundary states keep archive invariants."""
        profiler: UserProfiler = UserProfiler(":memory:", ":memory:", 91)
        profiler.record("app", "u", total_msgs=1)
        self.advance_days(1)
        self.advance_days(150)
        profiler.record("app", "u", total_msgs=1)
        stats = profiler.stats()
        assert stats["summary_count"] >= 1
        profiler.close()

    def test_edge_28_4187(self) -> None:
        """Rare boundary states keep archive invariants."""
        profiler: UserProfiler = UserProfiler(":memory:", ":memory:", 3)
        for _ in range(3):
            profiler.record("app", "u", total_msgs=1)
            self.advance_days(1)
        assert profiler.get_ratio("app", "ghost") == 0.0
        profiler.close()

    def test_edge_29_4188(self) -> None:
        """Rare boundary states keep archive invariants."""
        profiler: UserProfiler = UserProfiler(":memory:", ":memory:", 3)
        for _ in range(3):
            profiler.record("app", "u", total_msgs=1, blocked_msgs=1)
            self.advance_days(1)
        assert profiler.get_ratio("app", "u") == 1.0
        profiler.close()

    def test_edge_30_4189(self) -> None:
        """Rare boundary states keep archive invariants."""
        profiler: UserProfiler = UserProfiler(":memory:", ":memory:", 3)
        for _ in range(3):
            profiler.record("app", "u", total_msgs=1, reviewed_msgs=1)
            self.advance_days(1)
        assert profiler.get_ratio("app", "u") == 0.0
        profiler.close()

    def test_edge_31_4190(self) -> None:
        """Rare boundary states keep archive invariants."""
        profiler: UserProfiler = UserProfiler(":memory:", ":memory:", 3)
        for _ in range(3):
            profiler.record("app", "u", total_msgs=2, flagged_msgs=1)
            self.advance_days(1)
        assert profiler.get_ratio("app", "u") == 0.5
        profiler.close()

    def test_edge_32_4191(self) -> None:
        """Rare boundary states keep archive invariants."""
        profiler: UserProfiler = UserProfiler(":memory:", ":memory:", 91)
        for _ in range(91):
            profiler.record("app", "u", total_msgs=1, flagged_msgs=1)
            self.advance_days(1)
        assert profiler.get_ratio("app", "u") == 1.0
        profiler.close()

    def test_edge_33_4192(self) -> None:
        """Rare boundary states keep archive invariants."""
        profiler: UserProfiler = UserProfiler(":memory:", ":memory:", 91)
        for _ in range(91):
            profiler.record("app", "u", total_msgs=1)
            self.advance_days(1)
        assert profiler.get_ratio("app", "u") == 0.0
        profiler.close()

    def test_edge_34_4193(self) -> None:
        """Rare boundary states keep archive invariants."""
        profiler: UserProfiler = UserProfiler(":memory:", ":memory:", 3)
        for _ in range(3):
            profiler.record("app", "u", total_msgs=0)
            self.advance_days(1)
        summary = profiler.get_profile("app", "u")["summaries"][0]
        assert summary["total_msgs"] == 0
        profiler.close()

    def test_edge_35_4194(self) -> None:
        """Rare boundary states keep archive invariants."""
        profiler: UserProfiler = UserProfiler(":memory:", ":memory:", 91)
        profiler.record("app", "u", total_msgs=1)
        self.advance_days(1)
        self.advance_days(150)
        profiler.record("app", "u", total_msgs=1)
        stats = profiler.stats()
        assert stats["summary_count"] >= 1
        profiler.close()

    def test_edge_36_4195(self) -> None:
        """Rare boundary states keep archive invariants."""
        profiler: UserProfiler = UserProfiler(":memory:", ":memory:", 3)
        for _ in range(3):
            profiler.record("app", "u", total_msgs=1)
            self.advance_days(1)
        assert profiler.get_ratio("app", "ghost") == 0.0
        profiler.close()

    def test_edge_37_4196(self) -> None:
        """Rare boundary states keep archive invariants."""
        profiler: UserProfiler = UserProfiler(":memory:", ":memory:", 3)
        for _ in range(3):
            profiler.record("app", "u", total_msgs=1, blocked_msgs=1)
            self.advance_days(1)
        assert profiler.get_ratio("app", "u") == 1.0
        profiler.close()

    def test_edge_38_4197(self) -> None:
        """Rare boundary states keep archive invariants."""
        profiler: UserProfiler = UserProfiler(":memory:", ":memory:", 3)
        for _ in range(3):
            profiler.record("app", "u", total_msgs=1, reviewed_msgs=1)
            self.advance_days(1)
        assert profiler.get_ratio("app", "u") == 0.0
        profiler.close()

    def test_edge_39_4198(self) -> None:
        """Rare boundary states keep archive invariants."""
        profiler: UserProfiler = UserProfiler(":memory:", ":memory:", 3)
        for _ in range(3):
            profiler.record("app", "u", total_msgs=2, flagged_msgs=1)
            self.advance_days(1)
        assert profiler.get_ratio("app", "u") == 0.5
        profiler.close()

    def test_edge_40_4199(self) -> None:
        """Rare boundary states keep archive invariants."""
        profiler: UserProfiler = UserProfiler(":memory:", ":memory:", 91)
        for _ in range(91):
            profiler.record("app", "u", total_msgs=1, flagged_msgs=1)
            self.advance_days(1)
        assert profiler.get_ratio("app", "u") == 1.0
        profiler.close()

    def test_edge_41_4200(self) -> None:
        """Rare boundary states keep archive invariants."""
        profiler: UserProfiler = UserProfiler(":memory:", ":memory:", 91)
        for _ in range(91):
            profiler.record("app", "u", total_msgs=1)
            self.advance_days(1)
        assert profiler.get_ratio("app", "u") == 0.0
        profiler.close()

    def test_edge_42_4201(self) -> None:
        """Rare boundary states keep archive invariants."""
        profiler: UserProfiler = UserProfiler(":memory:", ":memory:", 3)
        for _ in range(3):
            profiler.record("app", "u", total_msgs=0)
            self.advance_days(1)
        summary = profiler.get_profile("app", "u")["summaries"][0]
        assert summary["total_msgs"] == 0
        profiler.close()

    def test_edge_43_4202(self) -> None:
        """Rare boundary states keep archive invariants."""
        profiler: UserProfiler = UserProfiler(":memory:", ":memory:", 91)
        profiler.record("app", "u", total_msgs=1)
        self.advance_days(1)
        self.advance_days(150)
        profiler.record("app", "u", total_msgs=1)
        stats = profiler.stats()
        assert stats["summary_count"] >= 1
        profiler.close()

    def test_edge_44_4203(self) -> None:
        """Rare boundary states keep archive invariants."""
        profiler: UserProfiler = UserProfiler(":memory:", ":memory:", 3)
        for _ in range(3):
            profiler.record("app", "u", total_msgs=1)
            self.advance_days(1)
        assert profiler.get_ratio("app", "ghost") == 0.0
        profiler.close()

    def test_edge_45_4204(self) -> None:
        """Rare boundary states keep archive invariants."""
        profiler: UserProfiler = UserProfiler(":memory:", ":memory:", 3)
        for _ in range(3):
            profiler.record("app", "u", total_msgs=1, blocked_msgs=1)
            self.advance_days(1)
        assert profiler.get_ratio("app", "u") == 1.0
        profiler.close()

    def test_edge_46_4205(self) -> None:
        """Rare boundary states keep archive invariants."""
        profiler: UserProfiler = UserProfiler(":memory:", ":memory:", 3)
        for _ in range(3):
            profiler.record("app", "u", total_msgs=1, reviewed_msgs=1)
            self.advance_days(1)
        assert profiler.get_ratio("app", "u") == 0.0
        profiler.close()

    def test_edge_47_4206(self) -> None:
        """Rare boundary states keep archive invariants."""
        profiler: UserProfiler = UserProfiler(":memory:", ":memory:", 3)
        for _ in range(3):
            profiler.record("app", "u", total_msgs=2, flagged_msgs=1)
            self.advance_days(1)
        assert profiler.get_ratio("app", "u") == 0.5
        profiler.close()

    def test_edge_48_4207(self) -> None:
        """Rare boundary states keep archive invariants."""
        profiler: UserProfiler = UserProfiler(":memory:", ":memory:", 91)
        for _ in range(91):
            profiler.record("app", "u", total_msgs=1, flagged_msgs=1)
            self.advance_days(1)
        assert profiler.get_ratio("app", "u") == 1.0
        profiler.close()

    def test_edge_49_4208(self) -> None:
        """Rare boundary states keep archive invariants."""
        profiler: UserProfiler = UserProfiler(":memory:", ":memory:", 91)
        for _ in range(91):
            profiler.record("app", "u", total_msgs=1)
            self.advance_days(1)
        assert profiler.get_ratio("app", "u") == 0.0
        profiler.close()
