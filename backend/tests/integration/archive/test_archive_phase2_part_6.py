"""Phase 2 archive cycle tests (generated).

Volume and percentage matrices, multi-cycle chains, multi-user/app
archives and boundary edges under the frozen clock."""

# multilingual fixtures use non-ASCII on purpose
from __future__ import annotations

import pytest

from app.profiling.user_profiler import UserProfiler
from tests.base_test import BaseTest

_MULTI_APP_ARCHIVE_CASES: tuple[tuple[int, int, int, int], ...] = (
    (4, 0, 4, 3809,),
    (4, 1, 4, 3810,),
    (4, 2, 4, 3811,),
    (4, 3, 4, 3812,),
    (4, 4, 4, 3813,),
    (4, 5, 4, 3814,),
    (4, 6, 4, 3815,),
    (4, 7, 4, 3816,),
    (4, 8, 4, 3817,),
    (4, 9, 4, 3818,),
    (4, 10, 4, 3819,),
    (4, 11, 4, 3820,),
    (4, 12, 4, 3821,),
    (4, 13, 4, 3822,),
    (4, 14, 4, 3823,),
    (4, 15, 4, 3824,),
    (4, 16, 4, 3825,),
    (4, 17, 4, 3826,),
    (4, 18, 4, 3827,),
    (4, 19, 4, 3828,),
    (4, 20, 4, 3829,),
    (4, 21, 4, 3830,),
    (4, 22, 4, 3831,),
    (4, 23, 4, 3832,),
    (4, 24, 4, 3833,),
    (5, 0, 5, 3834,),
    (5, 1, 5, 3835,),
    (5, 2, 5, 3836,),
    (5, 3, 5, 3837,),
    (5, 4, 5, 3838,),
    (5, 5, 5, 3839,),
    (5, 6, 5, 3840,),
    (5, 7, 5, 3841,),
    (5, 8, 5, 3842,),
    (5, 9, 5, 3843,),
    (5, 10, 5, 3844,),
    (5, 11, 5, 3845,),
    (5, 12, 5, 3846,),
    (5, 13, 5, 3847,),
    (5, 14, 5, 3848,),
    (5, 15, 5, 3849,),
    (5, 16, 5, 3850,),
    (5, 17, 5, 3851,),
    (5, 18, 5, 3852,),
    (5, 19, 5, 3853,),
    (5, 20, 5, 3854,),
    (5, 21, 5, 3855,),
    (5, 22, 5, 3856,),
    (5, 23, 5, 3857,),
    (5, 24, 5, 3858,),
    (10, 0, 10, 3859,),
    (10, 1, 10, 3860,),
    (10, 2, 10, 3861,),
    (10, 3, 10, 3862,),
    (10, 4, 10, 3863,),
    (10, 5, 10, 3864,),
    (10, 6, 10, 3865,),
    (10, 7, 10, 3866,),
    (10, 8, 10, 3867,),
    (10, 9, 10, 3868,),
    (10, 10, 10, 3869,),
    (10, 11, 10, 3870,),
    (10, 12, 10, 3871,),
    (10, 13, 10, 3872,),
    (10, 14, 10, 3873,),
    (10, 15, 10, 3874,),
    (10, 16, 10, 3875,),
    (10, 17, 10, 3876,),
    (10, 18, 10, 3877,),
    (10, 19, 10, 3878,),
    (10, 20, 10, 3879,),
    (10, 21, 10, 3880,),
    (10, 22, 10, 3881,),
    (10, 23, 10, 3882,),
    (10, 24, 10, 3883,),
    (20, 0, 20, 3884,),
    (20, 1, 20, 3885,),
    (20, 2, 20, 3886,),
    (20, 3, 20, 3887,),
    (20, 4, 20, 3888,),
    (20, 5, 20, 3889,),
    (20, 6, 20, 3890,),
    (20, 7, 20, 3891,),
    (20, 8, 20, 3892,),
    (20, 9, 20, 3893,),
    (20, 10, 20, 3894,),
    (20, 11, 20, 3895,),
    (20, 12, 20, 3896,),
    (20, 13, 20, 3897,),
    (20, 14, 20, 3898,),
    (20, 15, 20, 3899,),
    (20, 16, 20, 3900,),
    (20, 17, 20, 3901,),
    (20, 18, 20, 3902,),
    (20, 19, 20, 3903,),
    (20, 20, 20, 3904,),
    (20, 21, 20, 3905,),
    (20, 22, 20, 3906,),
    (20, 23, 20, 3907,),
    (20, 24, 20, 3908,),
)

class TestMultiAppArchive(BaseTest):
    """Each app archives independently for the shared user."""

    @pytest.mark.parametrize(('app_count', 'pattern', 'expected_summary', 'uid',), _MULTI_APP_ARCHIVE_CASES)
    def test_multi_app_archive(self, app_count: int, pattern: int, expected_summary: int, uid: int) -> None:
        """Each app archives independently for the shared user."""
        profiler: UserProfiler = UserProfiler(':memory:', ':memory:', 3)
        for _ in range(3):
            for index in range(app_count):
                flagged = 1 if (index + pattern) % 4 == 0 else 0
                profiler.record(f'app{index}', 'u', total_msgs=1, flagged_msgs=flagged)
            self.advance_days(1)
        stats = profiler.stats()
        assert stats['summary_count'] == expected_summary
        profiler.close()
