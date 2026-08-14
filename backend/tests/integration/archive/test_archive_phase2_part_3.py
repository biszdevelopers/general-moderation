"""Phase 2 archive cycle tests (generated).

Volume and percentage matrices, multi-cycle chains, multi-user/app
archives and boundary edges under the frozen clock."""

# multilingual fixtures use non-ASCII on purpose
from __future__ import annotations

import pytest

from app.profiling.user_profiler import UserProfiler
from tests.base_test import BaseTest

_MULTI_CYCLE_CASES: tuple[tuple[int, int, int, int], ...] = (
    (2, 0, 2, 3503,),
    (2, 1, 2, 3504,),
    (2, 2, 2, 3505,),
    (2, 3, 2, 3506,),
    (2, 4, 2, 3507,),
    (2, 5, 2, 3508,),
    (2, 6, 2, 3509,),
    (2, 7, 2, 3510,),
    (2, 8, 2, 3511,),
    (2, 9, 2, 3512,),
    (2, 10, 2, 3513,),
    (2, 11, 2, 3514,),
    (2, 12, 2, 3515,),
    (2, 13, 2, 3516,),
    (2, 14, 2, 3517,),
    (2, 15, 2, 3518,),
    (2, 16, 2, 3519,),
    (2, 17, 2, 3520,),
    (2, 18, 2, 3521,),
    (3, 0, 3, 3522,),
    (3, 1, 3, 3523,),
    (3, 2, 3, 3524,),
    (3, 3, 3, 3525,),
    (3, 4, 3, 3526,),
    (3, 5, 3, 3527,),
    (3, 6, 3, 3528,),
    (3, 7, 3, 3529,),
    (3, 8, 3, 3530,),
    (3, 9, 3, 3531,),
    (3, 10, 3, 3532,),
    (3, 11, 3, 3533,),
    (3, 12, 3, 3534,),
    (3, 13, 3, 3535,),
    (3, 14, 3, 3536,),
    (3, 15, 3, 3537,),
    (3, 16, 3, 3538,),
    (3, 17, 3, 3539,),
    (3, 18, 3, 3540,),
    (4, 0, 4, 3541,),
    (4, 1, 4, 3542,),
    (4, 2, 4, 3543,),
    (4, 3, 4, 3544,),
    (4, 4, 4, 3545,),
    (4, 5, 4, 3546,),
    (4, 6, 4, 3547,),
    (4, 7, 4, 3548,),
    (4, 8, 4, 3549,),
    (4, 9, 4, 3550,),
    (4, 10, 4, 3551,),
    (4, 11, 4, 3552,),
    (4, 12, 4, 3553,),
    (4, 13, 4, 3554,),
    (4, 14, 4, 3555,),
    (4, 15, 4, 3556,),
    (4, 16, 4, 3557,),
    (4, 17, 4, 3558,),
    (4, 18, 4, 3559,),
    (5, 0, 5, 3560,),
    (5, 1, 5, 3561,),
    (5, 2, 5, 3562,),
    (5, 3, 5, 3563,),
    (5, 4, 5, 3564,),
    (5, 5, 5, 3565,),
    (5, 6, 5, 3566,),
    (5, 7, 5, 3567,),
    (5, 8, 5, 3568,),
    (5, 9, 5, 3569,),
    (5, 10, 5, 3570,),
    (5, 11, 5, 3571,),
    (5, 12, 5, 3572,),
    (5, 13, 5, 3573,),
    (5, 14, 5, 3574,),
    (5, 15, 5, 3575,),
    (5, 16, 5, 3576,),
    (5, 17, 5, 3577,),
    (5, 18, 5, 3578,),
    (10, 0, 10, 3579,),
    (10, 1, 10, 3580,),
    (10, 2, 10, 3581,),
    (10, 3, 10, 3582,),
    (10, 4, 10, 3583,),
    (10, 5, 10, 3584,),
    (10, 6, 10, 3585,),
    (10, 7, 10, 3586,),
    (10, 8, 10, 3587,),
    (10, 9, 10, 3588,),
    (10, 10, 10, 3589,),
    (10, 11, 10, 3590,),
    (10, 12, 10, 3591,),
    (10, 13, 10, 3592,),
    (10, 14, 10, 3593,),
    (10, 15, 10, 3594,),
    (10, 16, 10, 3595,),
    (10, 17, 10, 3596,),
    (10, 18, 10, 3597,),
    (20, 0, 20, 3598,),
    (20, 1, 20, 3599,),
    (20, 2, 20, 3600,),
    (20, 3, 20, 3601,),
    (20, 4, 20, 3602,),
)

class TestMultiCycle(BaseTest):
    """Repeated short windows link into the expected cycle chain."""

    @pytest.mark.parametrize(('cycles', 'flag_pattern', 'expected_summaries', 'uid',), _MULTI_CYCLE_CASES)
    def test_multi_cycle(self, cycles: int, flag_pattern: int, expected_summaries: int, uid: int) -> None:
        """Repeated short windows link into the expected cycle chain."""
        profiler: UserProfiler = UserProfiler(':memory:', ':memory:', 2)
        for _ in range(cycles * 2):
            profiler.record(
                'app', 'u',
                total_msgs=1,
                flagged_msgs=flag_pattern % 2,
                blocked_msgs=(flag_pattern // 2) % 2,
            )
            self.advance_days(1)
        profile = profiler.get_profile('app', 'u')
        assert len(profile['summaries']) == expected_summaries
        chain = [summary['next_cycle_id'] for summary in profile['summaries']]
        assert chain[-1] is None
        profiler.close()
