"""Phase 2 archive cycle tests (generated).

Volume and percentage matrices, multi-cycle chains, multi-user/app
archives and boundary edges under the frozen clock."""

# multilingual fixtures use non-ASCII on purpose
from __future__ import annotations

from app.profiling.user_profiler import UserProfiler
from tests.base_test import BaseTest


class TestMultiCycle(BaseTest):
    """MultiCycle scenarios."""

    def test_multi_cycle_2_0_3503(self) -> None:
        """Repeated short windows link into the expected cycle chain."""
        profiler: UserProfiler = UserProfiler(":memory:", ":memory:", 2)
        for _ in range(4):
            profiler.record("app", "u", total_msgs=1, flagged_msgs=0, blocked_msgs=0)
            self.advance_days(1)
        profile = profiler.get_profile("app", "u")
        assert len(profile["summaries"]) == 2
        chain = [summary["next_cycle_id"] for summary in profile["summaries"]]
        assert chain[-1] is None
        profiler.close()

    def test_multi_cycle_2_1_3504(self) -> None:
        """Repeated short windows link into the expected cycle chain."""
        profiler: UserProfiler = UserProfiler(":memory:", ":memory:", 2)
        for _ in range(4):
            profiler.record("app", "u", total_msgs=1, flagged_msgs=1, blocked_msgs=0)
            self.advance_days(1)
        profile = profiler.get_profile("app", "u")
        assert len(profile["summaries"]) == 2
        chain = [summary["next_cycle_id"] for summary in profile["summaries"]]
        assert chain[-1] is None
        profiler.close()

    def test_multi_cycle_2_2_3505(self) -> None:
        """Repeated short windows link into the expected cycle chain."""
        profiler: UserProfiler = UserProfiler(":memory:", ":memory:", 2)
        for _ in range(4):
            profiler.record("app", "u", total_msgs=1, flagged_msgs=0, blocked_msgs=1)
            self.advance_days(1)
        profile = profiler.get_profile("app", "u")
        assert len(profile["summaries"]) == 2
        chain = [summary["next_cycle_id"] for summary in profile["summaries"]]
        assert chain[-1] is None
        profiler.close()

    def test_multi_cycle_2_3_3506(self) -> None:
        """Repeated short windows link into the expected cycle chain."""
        profiler: UserProfiler = UserProfiler(":memory:", ":memory:", 2)
        for _ in range(4):
            profiler.record("app", "u", total_msgs=1, flagged_msgs=1, blocked_msgs=1)
            self.advance_days(1)
        profile = profiler.get_profile("app", "u")
        assert len(profile["summaries"]) == 2
        chain = [summary["next_cycle_id"] for summary in profile["summaries"]]
        assert chain[-1] is None
        profiler.close()

    def test_multi_cycle_2_4_3507(self) -> None:
        """Repeated short windows link into the expected cycle chain."""
        profiler: UserProfiler = UserProfiler(":memory:", ":memory:", 2)
        for _ in range(4):
            profiler.record("app", "u", total_msgs=1, flagged_msgs=0, blocked_msgs=0)
            self.advance_days(1)
        profile = profiler.get_profile("app", "u")
        assert len(profile["summaries"]) == 2
        chain = [summary["next_cycle_id"] for summary in profile["summaries"]]
        assert chain[-1] is None
        profiler.close()

    def test_multi_cycle_2_5_3508(self) -> None:
        """Repeated short windows link into the expected cycle chain."""
        profiler: UserProfiler = UserProfiler(":memory:", ":memory:", 2)
        for _ in range(4):
            profiler.record("app", "u", total_msgs=1, flagged_msgs=1, blocked_msgs=0)
            self.advance_days(1)
        profile = profiler.get_profile("app", "u")
        assert len(profile["summaries"]) == 2
        chain = [summary["next_cycle_id"] for summary in profile["summaries"]]
        assert chain[-1] is None
        profiler.close()

    def test_multi_cycle_2_6_3509(self) -> None:
        """Repeated short windows link into the expected cycle chain."""
        profiler: UserProfiler = UserProfiler(":memory:", ":memory:", 2)
        for _ in range(4):
            profiler.record("app", "u", total_msgs=1, flagged_msgs=0, blocked_msgs=1)
            self.advance_days(1)
        profile = profiler.get_profile("app", "u")
        assert len(profile["summaries"]) == 2
        chain = [summary["next_cycle_id"] for summary in profile["summaries"]]
        assert chain[-1] is None
        profiler.close()

    def test_multi_cycle_2_7_3510(self) -> None:
        """Repeated short windows link into the expected cycle chain."""
        profiler: UserProfiler = UserProfiler(":memory:", ":memory:", 2)
        for _ in range(4):
            profiler.record("app", "u", total_msgs=1, flagged_msgs=1, blocked_msgs=1)
            self.advance_days(1)
        profile = profiler.get_profile("app", "u")
        assert len(profile["summaries"]) == 2
        chain = [summary["next_cycle_id"] for summary in profile["summaries"]]
        assert chain[-1] is None
        profiler.close()

    def test_multi_cycle_2_8_3511(self) -> None:
        """Repeated short windows link into the expected cycle chain."""
        profiler: UserProfiler = UserProfiler(":memory:", ":memory:", 2)
        for _ in range(4):
            profiler.record("app", "u", total_msgs=1, flagged_msgs=0, blocked_msgs=0)
            self.advance_days(1)
        profile = profiler.get_profile("app", "u")
        assert len(profile["summaries"]) == 2
        chain = [summary["next_cycle_id"] for summary in profile["summaries"]]
        assert chain[-1] is None
        profiler.close()

    def test_multi_cycle_2_9_3512(self) -> None:
        """Repeated short windows link into the expected cycle chain."""
        profiler: UserProfiler = UserProfiler(":memory:", ":memory:", 2)
        for _ in range(4):
            profiler.record("app", "u", total_msgs=1, flagged_msgs=1, blocked_msgs=0)
            self.advance_days(1)
        profile = profiler.get_profile("app", "u")
        assert len(profile["summaries"]) == 2
        chain = [summary["next_cycle_id"] for summary in profile["summaries"]]
        assert chain[-1] is None
        profiler.close()

    def test_multi_cycle_2_10_3513(self) -> None:
        """Repeated short windows link into the expected cycle chain."""
        profiler: UserProfiler = UserProfiler(":memory:", ":memory:", 2)
        for _ in range(4):
            profiler.record("app", "u", total_msgs=1, flagged_msgs=0, blocked_msgs=1)
            self.advance_days(1)
        profile = profiler.get_profile("app", "u")
        assert len(profile["summaries"]) == 2
        chain = [summary["next_cycle_id"] for summary in profile["summaries"]]
        assert chain[-1] is None
        profiler.close()

    def test_multi_cycle_2_11_3514(self) -> None:
        """Repeated short windows link into the expected cycle chain."""
        profiler: UserProfiler = UserProfiler(":memory:", ":memory:", 2)
        for _ in range(4):
            profiler.record("app", "u", total_msgs=1, flagged_msgs=1, blocked_msgs=1)
            self.advance_days(1)
        profile = profiler.get_profile("app", "u")
        assert len(profile["summaries"]) == 2
        chain = [summary["next_cycle_id"] for summary in profile["summaries"]]
        assert chain[-1] is None
        profiler.close()

    def test_multi_cycle_2_12_3515(self) -> None:
        """Repeated short windows link into the expected cycle chain."""
        profiler: UserProfiler = UserProfiler(":memory:", ":memory:", 2)
        for _ in range(4):
            profiler.record("app", "u", total_msgs=1, flagged_msgs=0, blocked_msgs=0)
            self.advance_days(1)
        profile = profiler.get_profile("app", "u")
        assert len(profile["summaries"]) == 2
        chain = [summary["next_cycle_id"] for summary in profile["summaries"]]
        assert chain[-1] is None
        profiler.close()

    def test_multi_cycle_2_13_3516(self) -> None:
        """Repeated short windows link into the expected cycle chain."""
        profiler: UserProfiler = UserProfiler(":memory:", ":memory:", 2)
        for _ in range(4):
            profiler.record("app", "u", total_msgs=1, flagged_msgs=1, blocked_msgs=0)
            self.advance_days(1)
        profile = profiler.get_profile("app", "u")
        assert len(profile["summaries"]) == 2
        chain = [summary["next_cycle_id"] for summary in profile["summaries"]]
        assert chain[-1] is None
        profiler.close()

    def test_multi_cycle_2_14_3517(self) -> None:
        """Repeated short windows link into the expected cycle chain."""
        profiler: UserProfiler = UserProfiler(":memory:", ":memory:", 2)
        for _ in range(4):
            profiler.record("app", "u", total_msgs=1, flagged_msgs=0, blocked_msgs=1)
            self.advance_days(1)
        profile = profiler.get_profile("app", "u")
        assert len(profile["summaries"]) == 2
        chain = [summary["next_cycle_id"] for summary in profile["summaries"]]
        assert chain[-1] is None
        profiler.close()

    def test_multi_cycle_2_15_3518(self) -> None:
        """Repeated short windows link into the expected cycle chain."""
        profiler: UserProfiler = UserProfiler(":memory:", ":memory:", 2)
        for _ in range(4):
            profiler.record("app", "u", total_msgs=1, flagged_msgs=1, blocked_msgs=1)
            self.advance_days(1)
        profile = profiler.get_profile("app", "u")
        assert len(profile["summaries"]) == 2
        chain = [summary["next_cycle_id"] for summary in profile["summaries"]]
        assert chain[-1] is None
        profiler.close()

    def test_multi_cycle_2_16_3519(self) -> None:
        """Repeated short windows link into the expected cycle chain."""
        profiler: UserProfiler = UserProfiler(":memory:", ":memory:", 2)
        for _ in range(4):
            profiler.record("app", "u", total_msgs=1, flagged_msgs=0, blocked_msgs=0)
            self.advance_days(1)
        profile = profiler.get_profile("app", "u")
        assert len(profile["summaries"]) == 2
        chain = [summary["next_cycle_id"] for summary in profile["summaries"]]
        assert chain[-1] is None
        profiler.close()

    def test_multi_cycle_2_17_3520(self) -> None:
        """Repeated short windows link into the expected cycle chain."""
        profiler: UserProfiler = UserProfiler(":memory:", ":memory:", 2)
        for _ in range(4):
            profiler.record("app", "u", total_msgs=1, flagged_msgs=1, blocked_msgs=0)
            self.advance_days(1)
        profile = profiler.get_profile("app", "u")
        assert len(profile["summaries"]) == 2
        chain = [summary["next_cycle_id"] for summary in profile["summaries"]]
        assert chain[-1] is None
        profiler.close()

    def test_multi_cycle_2_18_3521(self) -> None:
        """Repeated short windows link into the expected cycle chain."""
        profiler: UserProfiler = UserProfiler(":memory:", ":memory:", 2)
        for _ in range(4):
            profiler.record("app", "u", total_msgs=1, flagged_msgs=0, blocked_msgs=1)
            self.advance_days(1)
        profile = profiler.get_profile("app", "u")
        assert len(profile["summaries"]) == 2
        chain = [summary["next_cycle_id"] for summary in profile["summaries"]]
        assert chain[-1] is None
        profiler.close()

    def test_multi_cycle_3_0_3522(self) -> None:
        """Repeated short windows link into the expected cycle chain."""
        profiler: UserProfiler = UserProfiler(":memory:", ":memory:", 2)
        for _ in range(6):
            profiler.record("app", "u", total_msgs=1, flagged_msgs=0, blocked_msgs=0)
            self.advance_days(1)
        profile = profiler.get_profile("app", "u")
        assert len(profile["summaries"]) == 3
        chain = [summary["next_cycle_id"] for summary in profile["summaries"]]
        assert chain[-1] is None
        profiler.close()

    def test_multi_cycle_3_1_3523(self) -> None:
        """Repeated short windows link into the expected cycle chain."""
        profiler: UserProfiler = UserProfiler(":memory:", ":memory:", 2)
        for _ in range(6):
            profiler.record("app", "u", total_msgs=1, flagged_msgs=1, blocked_msgs=0)
            self.advance_days(1)
        profile = profiler.get_profile("app", "u")
        assert len(profile["summaries"]) == 3
        chain = [summary["next_cycle_id"] for summary in profile["summaries"]]
        assert chain[-1] is None
        profiler.close()

    def test_multi_cycle_3_2_3524(self) -> None:
        """Repeated short windows link into the expected cycle chain."""
        profiler: UserProfiler = UserProfiler(":memory:", ":memory:", 2)
        for _ in range(6):
            profiler.record("app", "u", total_msgs=1, flagged_msgs=0, blocked_msgs=1)
            self.advance_days(1)
        profile = profiler.get_profile("app", "u")
        assert len(profile["summaries"]) == 3
        chain = [summary["next_cycle_id"] for summary in profile["summaries"]]
        assert chain[-1] is None
        profiler.close()

    def test_multi_cycle_3_3_3525(self) -> None:
        """Repeated short windows link into the expected cycle chain."""
        profiler: UserProfiler = UserProfiler(":memory:", ":memory:", 2)
        for _ in range(6):
            profiler.record("app", "u", total_msgs=1, flagged_msgs=1, blocked_msgs=1)
            self.advance_days(1)
        profile = profiler.get_profile("app", "u")
        assert len(profile["summaries"]) == 3
        chain = [summary["next_cycle_id"] for summary in profile["summaries"]]
        assert chain[-1] is None
        profiler.close()

    def test_multi_cycle_3_4_3526(self) -> None:
        """Repeated short windows link into the expected cycle chain."""
        profiler: UserProfiler = UserProfiler(":memory:", ":memory:", 2)
        for _ in range(6):
            profiler.record("app", "u", total_msgs=1, flagged_msgs=0, blocked_msgs=0)
            self.advance_days(1)
        profile = profiler.get_profile("app", "u")
        assert len(profile["summaries"]) == 3
        chain = [summary["next_cycle_id"] for summary in profile["summaries"]]
        assert chain[-1] is None
        profiler.close()

    def test_multi_cycle_3_5_3527(self) -> None:
        """Repeated short windows link into the expected cycle chain."""
        profiler: UserProfiler = UserProfiler(":memory:", ":memory:", 2)
        for _ in range(6):
            profiler.record("app", "u", total_msgs=1, flagged_msgs=1, blocked_msgs=0)
            self.advance_days(1)
        profile = profiler.get_profile("app", "u")
        assert len(profile["summaries"]) == 3
        chain = [summary["next_cycle_id"] for summary in profile["summaries"]]
        assert chain[-1] is None
        profiler.close()

    def test_multi_cycle_3_6_3528(self) -> None:
        """Repeated short windows link into the expected cycle chain."""
        profiler: UserProfiler = UserProfiler(":memory:", ":memory:", 2)
        for _ in range(6):
            profiler.record("app", "u", total_msgs=1, flagged_msgs=0, blocked_msgs=1)
            self.advance_days(1)
        profile = profiler.get_profile("app", "u")
        assert len(profile["summaries"]) == 3
        chain = [summary["next_cycle_id"] for summary in profile["summaries"]]
        assert chain[-1] is None
        profiler.close()

    def test_multi_cycle_3_7_3529(self) -> None:
        """Repeated short windows link into the expected cycle chain."""
        profiler: UserProfiler = UserProfiler(":memory:", ":memory:", 2)
        for _ in range(6):
            profiler.record("app", "u", total_msgs=1, flagged_msgs=1, blocked_msgs=1)
            self.advance_days(1)
        profile = profiler.get_profile("app", "u")
        assert len(profile["summaries"]) == 3
        chain = [summary["next_cycle_id"] for summary in profile["summaries"]]
        assert chain[-1] is None
        profiler.close()

    def test_multi_cycle_3_8_3530(self) -> None:
        """Repeated short windows link into the expected cycle chain."""
        profiler: UserProfiler = UserProfiler(":memory:", ":memory:", 2)
        for _ in range(6):
            profiler.record("app", "u", total_msgs=1, flagged_msgs=0, blocked_msgs=0)
            self.advance_days(1)
        profile = profiler.get_profile("app", "u")
        assert len(profile["summaries"]) == 3
        chain = [summary["next_cycle_id"] for summary in profile["summaries"]]
        assert chain[-1] is None
        profiler.close()

    def test_multi_cycle_3_9_3531(self) -> None:
        """Repeated short windows link into the expected cycle chain."""
        profiler: UserProfiler = UserProfiler(":memory:", ":memory:", 2)
        for _ in range(6):
            profiler.record("app", "u", total_msgs=1, flagged_msgs=1, blocked_msgs=0)
            self.advance_days(1)
        profile = profiler.get_profile("app", "u")
        assert len(profile["summaries"]) == 3
        chain = [summary["next_cycle_id"] for summary in profile["summaries"]]
        assert chain[-1] is None
        profiler.close()

    def test_multi_cycle_3_10_3532(self) -> None:
        """Repeated short windows link into the expected cycle chain."""
        profiler: UserProfiler = UserProfiler(":memory:", ":memory:", 2)
        for _ in range(6):
            profiler.record("app", "u", total_msgs=1, flagged_msgs=0, blocked_msgs=1)
            self.advance_days(1)
        profile = profiler.get_profile("app", "u")
        assert len(profile["summaries"]) == 3
        chain = [summary["next_cycle_id"] for summary in profile["summaries"]]
        assert chain[-1] is None
        profiler.close()

    def test_multi_cycle_3_11_3533(self) -> None:
        """Repeated short windows link into the expected cycle chain."""
        profiler: UserProfiler = UserProfiler(":memory:", ":memory:", 2)
        for _ in range(6):
            profiler.record("app", "u", total_msgs=1, flagged_msgs=1, blocked_msgs=1)
            self.advance_days(1)
        profile = profiler.get_profile("app", "u")
        assert len(profile["summaries"]) == 3
        chain = [summary["next_cycle_id"] for summary in profile["summaries"]]
        assert chain[-1] is None
        profiler.close()

    def test_multi_cycle_3_12_3534(self) -> None:
        """Repeated short windows link into the expected cycle chain."""
        profiler: UserProfiler = UserProfiler(":memory:", ":memory:", 2)
        for _ in range(6):
            profiler.record("app", "u", total_msgs=1, flagged_msgs=0, blocked_msgs=0)
            self.advance_days(1)
        profile = profiler.get_profile("app", "u")
        assert len(profile["summaries"]) == 3
        chain = [summary["next_cycle_id"] for summary in profile["summaries"]]
        assert chain[-1] is None
        profiler.close()

    def test_multi_cycle_3_13_3535(self) -> None:
        """Repeated short windows link into the expected cycle chain."""
        profiler: UserProfiler = UserProfiler(":memory:", ":memory:", 2)
        for _ in range(6):
            profiler.record("app", "u", total_msgs=1, flagged_msgs=1, blocked_msgs=0)
            self.advance_days(1)
        profile = profiler.get_profile("app", "u")
        assert len(profile["summaries"]) == 3
        chain = [summary["next_cycle_id"] for summary in profile["summaries"]]
        assert chain[-1] is None
        profiler.close()

    def test_multi_cycle_3_14_3536(self) -> None:
        """Repeated short windows link into the expected cycle chain."""
        profiler: UserProfiler = UserProfiler(":memory:", ":memory:", 2)
        for _ in range(6):
            profiler.record("app", "u", total_msgs=1, flagged_msgs=0, blocked_msgs=1)
            self.advance_days(1)
        profile = profiler.get_profile("app", "u")
        assert len(profile["summaries"]) == 3
        chain = [summary["next_cycle_id"] for summary in profile["summaries"]]
        assert chain[-1] is None
        profiler.close()

    def test_multi_cycle_3_15_3537(self) -> None:
        """Repeated short windows link into the expected cycle chain."""
        profiler: UserProfiler = UserProfiler(":memory:", ":memory:", 2)
        for _ in range(6):
            profiler.record("app", "u", total_msgs=1, flagged_msgs=1, blocked_msgs=1)
            self.advance_days(1)
        profile = profiler.get_profile("app", "u")
        assert len(profile["summaries"]) == 3
        chain = [summary["next_cycle_id"] for summary in profile["summaries"]]
        assert chain[-1] is None
        profiler.close()

    def test_multi_cycle_3_16_3538(self) -> None:
        """Repeated short windows link into the expected cycle chain."""
        profiler: UserProfiler = UserProfiler(":memory:", ":memory:", 2)
        for _ in range(6):
            profiler.record("app", "u", total_msgs=1, flagged_msgs=0, blocked_msgs=0)
            self.advance_days(1)
        profile = profiler.get_profile("app", "u")
        assert len(profile["summaries"]) == 3
        chain = [summary["next_cycle_id"] for summary in profile["summaries"]]
        assert chain[-1] is None
        profiler.close()

    def test_multi_cycle_3_17_3539(self) -> None:
        """Repeated short windows link into the expected cycle chain."""
        profiler: UserProfiler = UserProfiler(":memory:", ":memory:", 2)
        for _ in range(6):
            profiler.record("app", "u", total_msgs=1, flagged_msgs=1, blocked_msgs=0)
            self.advance_days(1)
        profile = profiler.get_profile("app", "u")
        assert len(profile["summaries"]) == 3
        chain = [summary["next_cycle_id"] for summary in profile["summaries"]]
        assert chain[-1] is None
        profiler.close()

    def test_multi_cycle_3_18_3540(self) -> None:
        """Repeated short windows link into the expected cycle chain."""
        profiler: UserProfiler = UserProfiler(":memory:", ":memory:", 2)
        for _ in range(6):
            profiler.record("app", "u", total_msgs=1, flagged_msgs=0, blocked_msgs=1)
            self.advance_days(1)
        profile = profiler.get_profile("app", "u")
        assert len(profile["summaries"]) == 3
        chain = [summary["next_cycle_id"] for summary in profile["summaries"]]
        assert chain[-1] is None
        profiler.close()

    def test_multi_cycle_4_0_3541(self) -> None:
        """Repeated short windows link into the expected cycle chain."""
        profiler: UserProfiler = UserProfiler(":memory:", ":memory:", 2)
        for _ in range(8):
            profiler.record("app", "u", total_msgs=1, flagged_msgs=0, blocked_msgs=0)
            self.advance_days(1)
        profile = profiler.get_profile("app", "u")
        assert len(profile["summaries"]) == 4
        chain = [summary["next_cycle_id"] for summary in profile["summaries"]]
        assert chain[-1] is None
        profiler.close()

    def test_multi_cycle_4_1_3542(self) -> None:
        """Repeated short windows link into the expected cycle chain."""
        profiler: UserProfiler = UserProfiler(":memory:", ":memory:", 2)
        for _ in range(8):
            profiler.record("app", "u", total_msgs=1, flagged_msgs=1, blocked_msgs=0)
            self.advance_days(1)
        profile = profiler.get_profile("app", "u")
        assert len(profile["summaries"]) == 4
        chain = [summary["next_cycle_id"] for summary in profile["summaries"]]
        assert chain[-1] is None
        profiler.close()

    def test_multi_cycle_4_2_3543(self) -> None:
        """Repeated short windows link into the expected cycle chain."""
        profiler: UserProfiler = UserProfiler(":memory:", ":memory:", 2)
        for _ in range(8):
            profiler.record("app", "u", total_msgs=1, flagged_msgs=0, blocked_msgs=1)
            self.advance_days(1)
        profile = profiler.get_profile("app", "u")
        assert len(profile["summaries"]) == 4
        chain = [summary["next_cycle_id"] for summary in profile["summaries"]]
        assert chain[-1] is None
        profiler.close()

    def test_multi_cycle_4_3_3544(self) -> None:
        """Repeated short windows link into the expected cycle chain."""
        profiler: UserProfiler = UserProfiler(":memory:", ":memory:", 2)
        for _ in range(8):
            profiler.record("app", "u", total_msgs=1, flagged_msgs=1, blocked_msgs=1)
            self.advance_days(1)
        profile = profiler.get_profile("app", "u")
        assert len(profile["summaries"]) == 4
        chain = [summary["next_cycle_id"] for summary in profile["summaries"]]
        assert chain[-1] is None
        profiler.close()

    def test_multi_cycle_4_4_3545(self) -> None:
        """Repeated short windows link into the expected cycle chain."""
        profiler: UserProfiler = UserProfiler(":memory:", ":memory:", 2)
        for _ in range(8):
            profiler.record("app", "u", total_msgs=1, flagged_msgs=0, blocked_msgs=0)
            self.advance_days(1)
        profile = profiler.get_profile("app", "u")
        assert len(profile["summaries"]) == 4
        chain = [summary["next_cycle_id"] for summary in profile["summaries"]]
        assert chain[-1] is None
        profiler.close()

    def test_multi_cycle_4_5_3546(self) -> None:
        """Repeated short windows link into the expected cycle chain."""
        profiler: UserProfiler = UserProfiler(":memory:", ":memory:", 2)
        for _ in range(8):
            profiler.record("app", "u", total_msgs=1, flagged_msgs=1, blocked_msgs=0)
            self.advance_days(1)
        profile = profiler.get_profile("app", "u")
        assert len(profile["summaries"]) == 4
        chain = [summary["next_cycle_id"] for summary in profile["summaries"]]
        assert chain[-1] is None
        profiler.close()

    def test_multi_cycle_4_6_3547(self) -> None:
        """Repeated short windows link into the expected cycle chain."""
        profiler: UserProfiler = UserProfiler(":memory:", ":memory:", 2)
        for _ in range(8):
            profiler.record("app", "u", total_msgs=1, flagged_msgs=0, blocked_msgs=1)
            self.advance_days(1)
        profile = profiler.get_profile("app", "u")
        assert len(profile["summaries"]) == 4
        chain = [summary["next_cycle_id"] for summary in profile["summaries"]]
        assert chain[-1] is None
        profiler.close()

    def test_multi_cycle_4_7_3548(self) -> None:
        """Repeated short windows link into the expected cycle chain."""
        profiler: UserProfiler = UserProfiler(":memory:", ":memory:", 2)
        for _ in range(8):
            profiler.record("app", "u", total_msgs=1, flagged_msgs=1, blocked_msgs=1)
            self.advance_days(1)
        profile = profiler.get_profile("app", "u")
        assert len(profile["summaries"]) == 4
        chain = [summary["next_cycle_id"] for summary in profile["summaries"]]
        assert chain[-1] is None
        profiler.close()

    def test_multi_cycle_4_8_3549(self) -> None:
        """Repeated short windows link into the expected cycle chain."""
        profiler: UserProfiler = UserProfiler(":memory:", ":memory:", 2)
        for _ in range(8):
            profiler.record("app", "u", total_msgs=1, flagged_msgs=0, blocked_msgs=0)
            self.advance_days(1)
        profile = profiler.get_profile("app", "u")
        assert len(profile["summaries"]) == 4
        chain = [summary["next_cycle_id"] for summary in profile["summaries"]]
        assert chain[-1] is None
        profiler.close()

    def test_multi_cycle_4_9_3550(self) -> None:
        """Repeated short windows link into the expected cycle chain."""
        profiler: UserProfiler = UserProfiler(":memory:", ":memory:", 2)
        for _ in range(8):
            profiler.record("app", "u", total_msgs=1, flagged_msgs=1, blocked_msgs=0)
            self.advance_days(1)
        profile = profiler.get_profile("app", "u")
        assert len(profile["summaries"]) == 4
        chain = [summary["next_cycle_id"] for summary in profile["summaries"]]
        assert chain[-1] is None
        profiler.close()

    def test_multi_cycle_4_10_3551(self) -> None:
        """Repeated short windows link into the expected cycle chain."""
        profiler: UserProfiler = UserProfiler(":memory:", ":memory:", 2)
        for _ in range(8):
            profiler.record("app", "u", total_msgs=1, flagged_msgs=0, blocked_msgs=1)
            self.advance_days(1)
        profile = profiler.get_profile("app", "u")
        assert len(profile["summaries"]) == 4
        chain = [summary["next_cycle_id"] for summary in profile["summaries"]]
        assert chain[-1] is None
        profiler.close()

    def test_multi_cycle_4_11_3552(self) -> None:
        """Repeated short windows link into the expected cycle chain."""
        profiler: UserProfiler = UserProfiler(":memory:", ":memory:", 2)
        for _ in range(8):
            profiler.record("app", "u", total_msgs=1, flagged_msgs=1, blocked_msgs=1)
            self.advance_days(1)
        profile = profiler.get_profile("app", "u")
        assert len(profile["summaries"]) == 4
        chain = [summary["next_cycle_id"] for summary in profile["summaries"]]
        assert chain[-1] is None
        profiler.close()

    def test_multi_cycle_4_12_3553(self) -> None:
        """Repeated short windows link into the expected cycle chain."""
        profiler: UserProfiler = UserProfiler(":memory:", ":memory:", 2)
        for _ in range(8):
            profiler.record("app", "u", total_msgs=1, flagged_msgs=0, blocked_msgs=0)
            self.advance_days(1)
        profile = profiler.get_profile("app", "u")
        assert len(profile["summaries"]) == 4
        chain = [summary["next_cycle_id"] for summary in profile["summaries"]]
        assert chain[-1] is None
        profiler.close()

    def test_multi_cycle_4_13_3554(self) -> None:
        """Repeated short windows link into the expected cycle chain."""
        profiler: UserProfiler = UserProfiler(":memory:", ":memory:", 2)
        for _ in range(8):
            profiler.record("app", "u", total_msgs=1, flagged_msgs=1, blocked_msgs=0)
            self.advance_days(1)
        profile = profiler.get_profile("app", "u")
        assert len(profile["summaries"]) == 4
        chain = [summary["next_cycle_id"] for summary in profile["summaries"]]
        assert chain[-1] is None
        profiler.close()

    def test_multi_cycle_4_14_3555(self) -> None:
        """Repeated short windows link into the expected cycle chain."""
        profiler: UserProfiler = UserProfiler(":memory:", ":memory:", 2)
        for _ in range(8):
            profiler.record("app", "u", total_msgs=1, flagged_msgs=0, blocked_msgs=1)
            self.advance_days(1)
        profile = profiler.get_profile("app", "u")
        assert len(profile["summaries"]) == 4
        chain = [summary["next_cycle_id"] for summary in profile["summaries"]]
        assert chain[-1] is None
        profiler.close()

    def test_multi_cycle_4_15_3556(self) -> None:
        """Repeated short windows link into the expected cycle chain."""
        profiler: UserProfiler = UserProfiler(":memory:", ":memory:", 2)
        for _ in range(8):
            profiler.record("app", "u", total_msgs=1, flagged_msgs=1, blocked_msgs=1)
            self.advance_days(1)
        profile = profiler.get_profile("app", "u")
        assert len(profile["summaries"]) == 4
        chain = [summary["next_cycle_id"] for summary in profile["summaries"]]
        assert chain[-1] is None
        profiler.close()

    def test_multi_cycle_4_16_3557(self) -> None:
        """Repeated short windows link into the expected cycle chain."""
        profiler: UserProfiler = UserProfiler(":memory:", ":memory:", 2)
        for _ in range(8):
            profiler.record("app", "u", total_msgs=1, flagged_msgs=0, blocked_msgs=0)
            self.advance_days(1)
        profile = profiler.get_profile("app", "u")
        assert len(profile["summaries"]) == 4
        chain = [summary["next_cycle_id"] for summary in profile["summaries"]]
        assert chain[-1] is None
        profiler.close()

    def test_multi_cycle_4_17_3558(self) -> None:
        """Repeated short windows link into the expected cycle chain."""
        profiler: UserProfiler = UserProfiler(":memory:", ":memory:", 2)
        for _ in range(8):
            profiler.record("app", "u", total_msgs=1, flagged_msgs=1, blocked_msgs=0)
            self.advance_days(1)
        profile = profiler.get_profile("app", "u")
        assert len(profile["summaries"]) == 4
        chain = [summary["next_cycle_id"] for summary in profile["summaries"]]
        assert chain[-1] is None
        profiler.close()

    def test_multi_cycle_4_18_3559(self) -> None:
        """Repeated short windows link into the expected cycle chain."""
        profiler: UserProfiler = UserProfiler(":memory:", ":memory:", 2)
        for _ in range(8):
            profiler.record("app", "u", total_msgs=1, flagged_msgs=0, blocked_msgs=1)
            self.advance_days(1)
        profile = profiler.get_profile("app", "u")
        assert len(profile["summaries"]) == 4
        chain = [summary["next_cycle_id"] for summary in profile["summaries"]]
        assert chain[-1] is None
        profiler.close()

    def test_multi_cycle_5_0_3560(self) -> None:
        """Repeated short windows link into the expected cycle chain."""
        profiler: UserProfiler = UserProfiler(":memory:", ":memory:", 2)
        for _ in range(10):
            profiler.record("app", "u", total_msgs=1, flagged_msgs=0, blocked_msgs=0)
            self.advance_days(1)
        profile = profiler.get_profile("app", "u")
        assert len(profile["summaries"]) == 5
        chain = [summary["next_cycle_id"] for summary in profile["summaries"]]
        assert chain[-1] is None
        profiler.close()

    def test_multi_cycle_5_1_3561(self) -> None:
        """Repeated short windows link into the expected cycle chain."""
        profiler: UserProfiler = UserProfiler(":memory:", ":memory:", 2)
        for _ in range(10):
            profiler.record("app", "u", total_msgs=1, flagged_msgs=1, blocked_msgs=0)
            self.advance_days(1)
        profile = profiler.get_profile("app", "u")
        assert len(profile["summaries"]) == 5
        chain = [summary["next_cycle_id"] for summary in profile["summaries"]]
        assert chain[-1] is None
        profiler.close()

    def test_multi_cycle_5_2_3562(self) -> None:
        """Repeated short windows link into the expected cycle chain."""
        profiler: UserProfiler = UserProfiler(":memory:", ":memory:", 2)
        for _ in range(10):
            profiler.record("app", "u", total_msgs=1, flagged_msgs=0, blocked_msgs=1)
            self.advance_days(1)
        profile = profiler.get_profile("app", "u")
        assert len(profile["summaries"]) == 5
        chain = [summary["next_cycle_id"] for summary in profile["summaries"]]
        assert chain[-1] is None
        profiler.close()

    def test_multi_cycle_5_3_3563(self) -> None:
        """Repeated short windows link into the expected cycle chain."""
        profiler: UserProfiler = UserProfiler(":memory:", ":memory:", 2)
        for _ in range(10):
            profiler.record("app", "u", total_msgs=1, flagged_msgs=1, blocked_msgs=1)
            self.advance_days(1)
        profile = profiler.get_profile("app", "u")
        assert len(profile["summaries"]) == 5
        chain = [summary["next_cycle_id"] for summary in profile["summaries"]]
        assert chain[-1] is None
        profiler.close()

    def test_multi_cycle_5_4_3564(self) -> None:
        """Repeated short windows link into the expected cycle chain."""
        profiler: UserProfiler = UserProfiler(":memory:", ":memory:", 2)
        for _ in range(10):
            profiler.record("app", "u", total_msgs=1, flagged_msgs=0, blocked_msgs=0)
            self.advance_days(1)
        profile = profiler.get_profile("app", "u")
        assert len(profile["summaries"]) == 5
        chain = [summary["next_cycle_id"] for summary in profile["summaries"]]
        assert chain[-1] is None
        profiler.close()

    def test_multi_cycle_5_5_3565(self) -> None:
        """Repeated short windows link into the expected cycle chain."""
        profiler: UserProfiler = UserProfiler(":memory:", ":memory:", 2)
        for _ in range(10):
            profiler.record("app", "u", total_msgs=1, flagged_msgs=1, blocked_msgs=0)
            self.advance_days(1)
        profile = profiler.get_profile("app", "u")
        assert len(profile["summaries"]) == 5
        chain = [summary["next_cycle_id"] for summary in profile["summaries"]]
        assert chain[-1] is None
        profiler.close()

    def test_multi_cycle_5_6_3566(self) -> None:
        """Repeated short windows link into the expected cycle chain."""
        profiler: UserProfiler = UserProfiler(":memory:", ":memory:", 2)
        for _ in range(10):
            profiler.record("app", "u", total_msgs=1, flagged_msgs=0, blocked_msgs=1)
            self.advance_days(1)
        profile = profiler.get_profile("app", "u")
        assert len(profile["summaries"]) == 5
        chain = [summary["next_cycle_id"] for summary in profile["summaries"]]
        assert chain[-1] is None
        profiler.close()

    def test_multi_cycle_5_7_3567(self) -> None:
        """Repeated short windows link into the expected cycle chain."""
        profiler: UserProfiler = UserProfiler(":memory:", ":memory:", 2)
        for _ in range(10):
            profiler.record("app", "u", total_msgs=1, flagged_msgs=1, blocked_msgs=1)
            self.advance_days(1)
        profile = profiler.get_profile("app", "u")
        assert len(profile["summaries"]) == 5
        chain = [summary["next_cycle_id"] for summary in profile["summaries"]]
        assert chain[-1] is None
        profiler.close()

    def test_multi_cycle_5_8_3568(self) -> None:
        """Repeated short windows link into the expected cycle chain."""
        profiler: UserProfiler = UserProfiler(":memory:", ":memory:", 2)
        for _ in range(10):
            profiler.record("app", "u", total_msgs=1, flagged_msgs=0, blocked_msgs=0)
            self.advance_days(1)
        profile = profiler.get_profile("app", "u")
        assert len(profile["summaries"]) == 5
        chain = [summary["next_cycle_id"] for summary in profile["summaries"]]
        assert chain[-1] is None
        profiler.close()

    def test_multi_cycle_5_9_3569(self) -> None:
        """Repeated short windows link into the expected cycle chain."""
        profiler: UserProfiler = UserProfiler(":memory:", ":memory:", 2)
        for _ in range(10):
            profiler.record("app", "u", total_msgs=1, flagged_msgs=1, blocked_msgs=0)
            self.advance_days(1)
        profile = profiler.get_profile("app", "u")
        assert len(profile["summaries"]) == 5
        chain = [summary["next_cycle_id"] for summary in profile["summaries"]]
        assert chain[-1] is None
        profiler.close()

    def test_multi_cycle_5_10_3570(self) -> None:
        """Repeated short windows link into the expected cycle chain."""
        profiler: UserProfiler = UserProfiler(":memory:", ":memory:", 2)
        for _ in range(10):
            profiler.record("app", "u", total_msgs=1, flagged_msgs=0, blocked_msgs=1)
            self.advance_days(1)
        profile = profiler.get_profile("app", "u")
        assert len(profile["summaries"]) == 5
        chain = [summary["next_cycle_id"] for summary in profile["summaries"]]
        assert chain[-1] is None
        profiler.close()

    def test_multi_cycle_5_11_3571(self) -> None:
        """Repeated short windows link into the expected cycle chain."""
        profiler: UserProfiler = UserProfiler(":memory:", ":memory:", 2)
        for _ in range(10):
            profiler.record("app", "u", total_msgs=1, flagged_msgs=1, blocked_msgs=1)
            self.advance_days(1)
        profile = profiler.get_profile("app", "u")
        assert len(profile["summaries"]) == 5
        chain = [summary["next_cycle_id"] for summary in profile["summaries"]]
        assert chain[-1] is None
        profiler.close()

    def test_multi_cycle_5_12_3572(self) -> None:
        """Repeated short windows link into the expected cycle chain."""
        profiler: UserProfiler = UserProfiler(":memory:", ":memory:", 2)
        for _ in range(10):
            profiler.record("app", "u", total_msgs=1, flagged_msgs=0, blocked_msgs=0)
            self.advance_days(1)
        profile = profiler.get_profile("app", "u")
        assert len(profile["summaries"]) == 5
        chain = [summary["next_cycle_id"] for summary in profile["summaries"]]
        assert chain[-1] is None
        profiler.close()

    def test_multi_cycle_5_13_3573(self) -> None:
        """Repeated short windows link into the expected cycle chain."""
        profiler: UserProfiler = UserProfiler(":memory:", ":memory:", 2)
        for _ in range(10):
            profiler.record("app", "u", total_msgs=1, flagged_msgs=1, blocked_msgs=0)
            self.advance_days(1)
        profile = profiler.get_profile("app", "u")
        assert len(profile["summaries"]) == 5
        chain = [summary["next_cycle_id"] for summary in profile["summaries"]]
        assert chain[-1] is None
        profiler.close()

    def test_multi_cycle_5_14_3574(self) -> None:
        """Repeated short windows link into the expected cycle chain."""
        profiler: UserProfiler = UserProfiler(":memory:", ":memory:", 2)
        for _ in range(10):
            profiler.record("app", "u", total_msgs=1, flagged_msgs=0, blocked_msgs=1)
            self.advance_days(1)
        profile = profiler.get_profile("app", "u")
        assert len(profile["summaries"]) == 5
        chain = [summary["next_cycle_id"] for summary in profile["summaries"]]
        assert chain[-1] is None
        profiler.close()

    def test_multi_cycle_5_15_3575(self) -> None:
        """Repeated short windows link into the expected cycle chain."""
        profiler: UserProfiler = UserProfiler(":memory:", ":memory:", 2)
        for _ in range(10):
            profiler.record("app", "u", total_msgs=1, flagged_msgs=1, blocked_msgs=1)
            self.advance_days(1)
        profile = profiler.get_profile("app", "u")
        assert len(profile["summaries"]) == 5
        chain = [summary["next_cycle_id"] for summary in profile["summaries"]]
        assert chain[-1] is None
        profiler.close()

    def test_multi_cycle_5_16_3576(self) -> None:
        """Repeated short windows link into the expected cycle chain."""
        profiler: UserProfiler = UserProfiler(":memory:", ":memory:", 2)
        for _ in range(10):
            profiler.record("app", "u", total_msgs=1, flagged_msgs=0, blocked_msgs=0)
            self.advance_days(1)
        profile = profiler.get_profile("app", "u")
        assert len(profile["summaries"]) == 5
        chain = [summary["next_cycle_id"] for summary in profile["summaries"]]
        assert chain[-1] is None
        profiler.close()

    def test_multi_cycle_5_17_3577(self) -> None:
        """Repeated short windows link into the expected cycle chain."""
        profiler: UserProfiler = UserProfiler(":memory:", ":memory:", 2)
        for _ in range(10):
            profiler.record("app", "u", total_msgs=1, flagged_msgs=1, blocked_msgs=0)
            self.advance_days(1)
        profile = profiler.get_profile("app", "u")
        assert len(profile["summaries"]) == 5
        chain = [summary["next_cycle_id"] for summary in profile["summaries"]]
        assert chain[-1] is None
        profiler.close()

    def test_multi_cycle_5_18_3578(self) -> None:
        """Repeated short windows link into the expected cycle chain."""
        profiler: UserProfiler = UserProfiler(":memory:", ":memory:", 2)
        for _ in range(10):
            profiler.record("app", "u", total_msgs=1, flagged_msgs=0, blocked_msgs=1)
            self.advance_days(1)
        profile = profiler.get_profile("app", "u")
        assert len(profile["summaries"]) == 5
        chain = [summary["next_cycle_id"] for summary in profile["summaries"]]
        assert chain[-1] is None
        profiler.close()

    def test_multi_cycle_10_0_3579(self) -> None:
        """Repeated short windows link into the expected cycle chain."""
        profiler: UserProfiler = UserProfiler(":memory:", ":memory:", 2)
        for _ in range(20):
            profiler.record("app", "u", total_msgs=1, flagged_msgs=0, blocked_msgs=0)
            self.advance_days(1)
        profile = profiler.get_profile("app", "u")
        assert len(profile["summaries"]) == 10
        chain = [summary["next_cycle_id"] for summary in profile["summaries"]]
        assert chain[-1] is None
        profiler.close()

    def test_multi_cycle_10_1_3580(self) -> None:
        """Repeated short windows link into the expected cycle chain."""
        profiler: UserProfiler = UserProfiler(":memory:", ":memory:", 2)
        for _ in range(20):
            profiler.record("app", "u", total_msgs=1, flagged_msgs=1, blocked_msgs=0)
            self.advance_days(1)
        profile = profiler.get_profile("app", "u")
        assert len(profile["summaries"]) == 10
        chain = [summary["next_cycle_id"] for summary in profile["summaries"]]
        assert chain[-1] is None
        profiler.close()

    def test_multi_cycle_10_2_3581(self) -> None:
        """Repeated short windows link into the expected cycle chain."""
        profiler: UserProfiler = UserProfiler(":memory:", ":memory:", 2)
        for _ in range(20):
            profiler.record("app", "u", total_msgs=1, flagged_msgs=0, blocked_msgs=1)
            self.advance_days(1)
        profile = profiler.get_profile("app", "u")
        assert len(profile["summaries"]) == 10
        chain = [summary["next_cycle_id"] for summary in profile["summaries"]]
        assert chain[-1] is None
        profiler.close()

    def test_multi_cycle_10_3_3582(self) -> None:
        """Repeated short windows link into the expected cycle chain."""
        profiler: UserProfiler = UserProfiler(":memory:", ":memory:", 2)
        for _ in range(20):
            profiler.record("app", "u", total_msgs=1, flagged_msgs=1, blocked_msgs=1)
            self.advance_days(1)
        profile = profiler.get_profile("app", "u")
        assert len(profile["summaries"]) == 10
        chain = [summary["next_cycle_id"] for summary in profile["summaries"]]
        assert chain[-1] is None
        profiler.close()

    def test_multi_cycle_10_4_3583(self) -> None:
        """Repeated short windows link into the expected cycle chain."""
        profiler: UserProfiler = UserProfiler(":memory:", ":memory:", 2)
        for _ in range(20):
            profiler.record("app", "u", total_msgs=1, flagged_msgs=0, blocked_msgs=0)
            self.advance_days(1)
        profile = profiler.get_profile("app", "u")
        assert len(profile["summaries"]) == 10
        chain = [summary["next_cycle_id"] for summary in profile["summaries"]]
        assert chain[-1] is None
        profiler.close()

    def test_multi_cycle_10_5_3584(self) -> None:
        """Repeated short windows link into the expected cycle chain."""
        profiler: UserProfiler = UserProfiler(":memory:", ":memory:", 2)
        for _ in range(20):
            profiler.record("app", "u", total_msgs=1, flagged_msgs=1, blocked_msgs=0)
            self.advance_days(1)
        profile = profiler.get_profile("app", "u")
        assert len(profile["summaries"]) == 10
        chain = [summary["next_cycle_id"] for summary in profile["summaries"]]
        assert chain[-1] is None
        profiler.close()

    def test_multi_cycle_10_6_3585(self) -> None:
        """Repeated short windows link into the expected cycle chain."""
        profiler: UserProfiler = UserProfiler(":memory:", ":memory:", 2)
        for _ in range(20):
            profiler.record("app", "u", total_msgs=1, flagged_msgs=0, blocked_msgs=1)
            self.advance_days(1)
        profile = profiler.get_profile("app", "u")
        assert len(profile["summaries"]) == 10
        chain = [summary["next_cycle_id"] for summary in profile["summaries"]]
        assert chain[-1] is None
        profiler.close()

    def test_multi_cycle_10_7_3586(self) -> None:
        """Repeated short windows link into the expected cycle chain."""
        profiler: UserProfiler = UserProfiler(":memory:", ":memory:", 2)
        for _ in range(20):
            profiler.record("app", "u", total_msgs=1, flagged_msgs=1, blocked_msgs=1)
            self.advance_days(1)
        profile = profiler.get_profile("app", "u")
        assert len(profile["summaries"]) == 10
        chain = [summary["next_cycle_id"] for summary in profile["summaries"]]
        assert chain[-1] is None
        profiler.close()

    def test_multi_cycle_10_8_3587(self) -> None:
        """Repeated short windows link into the expected cycle chain."""
        profiler: UserProfiler = UserProfiler(":memory:", ":memory:", 2)
        for _ in range(20):
            profiler.record("app", "u", total_msgs=1, flagged_msgs=0, blocked_msgs=0)
            self.advance_days(1)
        profile = profiler.get_profile("app", "u")
        assert len(profile["summaries"]) == 10
        chain = [summary["next_cycle_id"] for summary in profile["summaries"]]
        assert chain[-1] is None
        profiler.close()

    def test_multi_cycle_10_9_3588(self) -> None:
        """Repeated short windows link into the expected cycle chain."""
        profiler: UserProfiler = UserProfiler(":memory:", ":memory:", 2)
        for _ in range(20):
            profiler.record("app", "u", total_msgs=1, flagged_msgs=1, blocked_msgs=0)
            self.advance_days(1)
        profile = profiler.get_profile("app", "u")
        assert len(profile["summaries"]) == 10
        chain = [summary["next_cycle_id"] for summary in profile["summaries"]]
        assert chain[-1] is None
        profiler.close()

    def test_multi_cycle_10_10_3589(self) -> None:
        """Repeated short windows link into the expected cycle chain."""
        profiler: UserProfiler = UserProfiler(":memory:", ":memory:", 2)
        for _ in range(20):
            profiler.record("app", "u", total_msgs=1, flagged_msgs=0, blocked_msgs=1)
            self.advance_days(1)
        profile = profiler.get_profile("app", "u")
        assert len(profile["summaries"]) == 10
        chain = [summary["next_cycle_id"] for summary in profile["summaries"]]
        assert chain[-1] is None
        profiler.close()

    def test_multi_cycle_10_11_3590(self) -> None:
        """Repeated short windows link into the expected cycle chain."""
        profiler: UserProfiler = UserProfiler(":memory:", ":memory:", 2)
        for _ in range(20):
            profiler.record("app", "u", total_msgs=1, flagged_msgs=1, blocked_msgs=1)
            self.advance_days(1)
        profile = profiler.get_profile("app", "u")
        assert len(profile["summaries"]) == 10
        chain = [summary["next_cycle_id"] for summary in profile["summaries"]]
        assert chain[-1] is None
        profiler.close()

    def test_multi_cycle_10_12_3591(self) -> None:
        """Repeated short windows link into the expected cycle chain."""
        profiler: UserProfiler = UserProfiler(":memory:", ":memory:", 2)
        for _ in range(20):
            profiler.record("app", "u", total_msgs=1, flagged_msgs=0, blocked_msgs=0)
            self.advance_days(1)
        profile = profiler.get_profile("app", "u")
        assert len(profile["summaries"]) == 10
        chain = [summary["next_cycle_id"] for summary in profile["summaries"]]
        assert chain[-1] is None
        profiler.close()

    def test_multi_cycle_10_13_3592(self) -> None:
        """Repeated short windows link into the expected cycle chain."""
        profiler: UserProfiler = UserProfiler(":memory:", ":memory:", 2)
        for _ in range(20):
            profiler.record("app", "u", total_msgs=1, flagged_msgs=1, blocked_msgs=0)
            self.advance_days(1)
        profile = profiler.get_profile("app", "u")
        assert len(profile["summaries"]) == 10
        chain = [summary["next_cycle_id"] for summary in profile["summaries"]]
        assert chain[-1] is None
        profiler.close()

    def test_multi_cycle_10_14_3593(self) -> None:
        """Repeated short windows link into the expected cycle chain."""
        profiler: UserProfiler = UserProfiler(":memory:", ":memory:", 2)
        for _ in range(20):
            profiler.record("app", "u", total_msgs=1, flagged_msgs=0, blocked_msgs=1)
            self.advance_days(1)
        profile = profiler.get_profile("app", "u")
        assert len(profile["summaries"]) == 10
        chain = [summary["next_cycle_id"] for summary in profile["summaries"]]
        assert chain[-1] is None
        profiler.close()

    def test_multi_cycle_10_15_3594(self) -> None:
        """Repeated short windows link into the expected cycle chain."""
        profiler: UserProfiler = UserProfiler(":memory:", ":memory:", 2)
        for _ in range(20):
            profiler.record("app", "u", total_msgs=1, flagged_msgs=1, blocked_msgs=1)
            self.advance_days(1)
        profile = profiler.get_profile("app", "u")
        assert len(profile["summaries"]) == 10
        chain = [summary["next_cycle_id"] for summary in profile["summaries"]]
        assert chain[-1] is None
        profiler.close()

    def test_multi_cycle_10_16_3595(self) -> None:
        """Repeated short windows link into the expected cycle chain."""
        profiler: UserProfiler = UserProfiler(":memory:", ":memory:", 2)
        for _ in range(20):
            profiler.record("app", "u", total_msgs=1, flagged_msgs=0, blocked_msgs=0)
            self.advance_days(1)
        profile = profiler.get_profile("app", "u")
        assert len(profile["summaries"]) == 10
        chain = [summary["next_cycle_id"] for summary in profile["summaries"]]
        assert chain[-1] is None
        profiler.close()

    def test_multi_cycle_10_17_3596(self) -> None:
        """Repeated short windows link into the expected cycle chain."""
        profiler: UserProfiler = UserProfiler(":memory:", ":memory:", 2)
        for _ in range(20):
            profiler.record("app", "u", total_msgs=1, flagged_msgs=1, blocked_msgs=0)
            self.advance_days(1)
        profile = profiler.get_profile("app", "u")
        assert len(profile["summaries"]) == 10
        chain = [summary["next_cycle_id"] for summary in profile["summaries"]]
        assert chain[-1] is None
        profiler.close()

    def test_multi_cycle_10_18_3597(self) -> None:
        """Repeated short windows link into the expected cycle chain."""
        profiler: UserProfiler = UserProfiler(":memory:", ":memory:", 2)
        for _ in range(20):
            profiler.record("app", "u", total_msgs=1, flagged_msgs=0, blocked_msgs=1)
            self.advance_days(1)
        profile = profiler.get_profile("app", "u")
        assert len(profile["summaries"]) == 10
        chain = [summary["next_cycle_id"] for summary in profile["summaries"]]
        assert chain[-1] is None
        profiler.close()

    def test_multi_cycle_20_0_3598(self) -> None:
        """Repeated short windows link into the expected cycle chain."""
        profiler: UserProfiler = UserProfiler(":memory:", ":memory:", 2)
        for _ in range(40):
            profiler.record("app", "u", total_msgs=1, flagged_msgs=0, blocked_msgs=0)
            self.advance_days(1)
        profile = profiler.get_profile("app", "u")
        assert len(profile["summaries"]) == 20
        chain = [summary["next_cycle_id"] for summary in profile["summaries"]]
        assert chain[-1] is None
        profiler.close()

    def test_multi_cycle_20_1_3599(self) -> None:
        """Repeated short windows link into the expected cycle chain."""
        profiler: UserProfiler = UserProfiler(":memory:", ":memory:", 2)
        for _ in range(40):
            profiler.record("app", "u", total_msgs=1, flagged_msgs=1, blocked_msgs=0)
            self.advance_days(1)
        profile = profiler.get_profile("app", "u")
        assert len(profile["summaries"]) == 20
        chain = [summary["next_cycle_id"] for summary in profile["summaries"]]
        assert chain[-1] is None
        profiler.close()

    def test_multi_cycle_20_2_3600(self) -> None:
        """Repeated short windows link into the expected cycle chain."""
        profiler: UserProfiler = UserProfiler(":memory:", ":memory:", 2)
        for _ in range(40):
            profiler.record("app", "u", total_msgs=1, flagged_msgs=0, blocked_msgs=1)
            self.advance_days(1)
        profile = profiler.get_profile("app", "u")
        assert len(profile["summaries"]) == 20
        chain = [summary["next_cycle_id"] for summary in profile["summaries"]]
        assert chain[-1] is None
        profiler.close()

    def test_multi_cycle_20_3_3601(self) -> None:
        """Repeated short windows link into the expected cycle chain."""
        profiler: UserProfiler = UserProfiler(":memory:", ":memory:", 2)
        for _ in range(40):
            profiler.record("app", "u", total_msgs=1, flagged_msgs=1, blocked_msgs=1)
            self.advance_days(1)
        profile = profiler.get_profile("app", "u")
        assert len(profile["summaries"]) == 20
        chain = [summary["next_cycle_id"] for summary in profile["summaries"]]
        assert chain[-1] is None
        profiler.close()

    def test_multi_cycle_20_4_3602(self) -> None:
        """Repeated short windows link into the expected cycle chain."""
        profiler: UserProfiler = UserProfiler(":memory:", ":memory:", 2)
        for _ in range(40):
            profiler.record("app", "u", total_msgs=1, flagged_msgs=0, blocked_msgs=0)
            self.advance_days(1)
        profile = profiler.get_profile("app", "u")
        assert len(profile["summaries"]) == 20
        chain = [summary["next_cycle_id"] for summary in profile["summaries"]]
        assert chain[-1] is None
        profiler.close()
