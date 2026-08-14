"""Phase 2 archive cycle tests (generated).

Volume and percentage matrices, multi-cycle chains, multi-user/app
archives and boundary edges under the frozen clock."""

# multilingual fixtures use non-ASCII on purpose
from __future__ import annotations

import pytest

from app.profiling.user_profiler import UserProfiler
from tests.base_test import BaseTest

_MULTI_CYCLE_CASES: tuple[tuple[int, int, int, int], ...] = (
    (20, 5, 20, 3603,),
    (20, 6, 20, 3604,),
    (20, 7, 20, 3605,),
    (20, 8, 20, 3606,),
    (20, 9, 20, 3607,),
    (20, 10, 20, 3608,),
    (20, 11, 20, 3609,),
    (20, 12, 20, 3610,),
    (20, 13, 20, 3611,),
    (20, 14, 20, 3612,),
    (20, 15, 20, 3613,),
    (20, 16, 20, 3614,),
    (20, 17, 20, 3615,),
    (20, 18, 20, 3616,),
    (50, 0, 50, 3617,),
    (50, 1, 50, 3618,),
    (50, 2, 50, 3619,),
    (50, 3, 50, 3620,),
    (50, 4, 50, 3621,),
    (50, 5, 50, 3622,),
    (50, 6, 50, 3623,),
    (50, 7, 50, 3624,),
    (50, 8, 50, 3625,),
    (50, 9, 50, 3626,),
    (50, 10, 50, 3627,),
    (50, 11, 50, 3628,),
    (50, 12, 50, 3629,),
    (50, 13, 50, 3630,),
    (50, 14, 50, 3631,),
    (50, 15, 50, 3632,),
    (50, 16, 50, 3633,),
    (50, 17, 50, 3634,),
    (50, 18, 50, 3635,),
    (100, 0, 100, 3636,),
    (100, 1, 100, 3637,),
    (100, 2, 100, 3638,),
    (100, 3, 100, 3639,),
    (100, 4, 100, 3640,),
    (100, 5, 100, 3641,),
    (100, 6, 100, 3642,),
    (100, 7, 100, 3643,),
    (100, 8, 100, 3644,),
    (100, 9, 100, 3645,),
    (100, 10, 100, 3646,),
    (100, 11, 100, 3647,),
    (100, 12, 100, 3648,),
    (100, 13, 100, 3649,),
    (100, 14, 100, 3650,),
    (100, 15, 100, 3651,),
    (100, 16, 100, 3652,),
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


_MULTI_USER_ARCHIVE_CASES: tuple[tuple[int, int, int, int], ...] = (
    (10, 0, 10, 3655,),
    (10, 1, 10, 3656,),
    (10, 2, 10, 3657,),
    (10, 3, 10, 3658,),
    (10, 4, 10, 3659,),
    (10, 5, 10, 3660,),
    (10, 6, 10, 3661,),
    (10, 7, 10, 3662,),
    (10, 8, 10, 3663,),
    (10, 9, 10, 3664,),
    (10, 10, 10, 3665,),
    (10, 11, 10, 3666,),
    (10, 12, 10, 3667,),
    (10, 13, 10, 3668,),
    (10, 14, 10, 3669,),
    (10, 15, 10, 3670,),
    (10, 16, 10, 3671,),
    (10, 17, 10, 3672,),
    (10, 18, 10, 3673,),
    (10, 19, 10, 3674,),
    (10, 20, 10, 3675,),
    (10, 21, 10, 3676,),
    (25, 0, 25, 3677,),
    (25, 1, 25, 3678,),
    (25, 2, 25, 3679,),
    (25, 3, 25, 3680,),
    (25, 4, 25, 3681,),
    (25, 5, 25, 3682,),
    (25, 6, 25, 3683,),
    (25, 7, 25, 3684,),
    (25, 8, 25, 3685,),
    (25, 9, 25, 3686,),
    (25, 10, 25, 3687,),
    (25, 11, 25, 3688,),
    (25, 12, 25, 3689,),
    (25, 13, 25, 3690,),
    (25, 14, 25, 3691,),
    (25, 15, 25, 3692,),
    (25, 16, 25, 3693,),
    (25, 17, 25, 3694,),
    (25, 18, 25, 3695,),
    (25, 19, 25, 3696,),
    (25, 20, 25, 3697,),
    (25, 21, 25, 3698,),
    (50, 0, 50, 3699,),
    (50, 1, 50, 3700,),
    (50, 2, 50, 3701,),
    (50, 3, 50, 3702,),
    (50, 4, 50, 3703,),
    (50, 5, 50, 3704,),
)

class TestMultiUserArchive(BaseTest):
    """Every user archives independently within one app."""

    @pytest.mark.parametrize(('user_count', 'pattern', 'expected_summary', 'uid',), _MULTI_USER_ARCHIVE_CASES)
    def test_multi_user_archive(self, user_count: int, pattern: int, expected_summary: int, uid: int) -> None:
        """Every user archives independently within one app."""
        profiler: UserProfiler = UserProfiler(':memory:', ':memory:', 3)
        for _ in range(3):
            for index in range(user_count):
                flagged = 1 if index % 3 == pattern % 3 else 0
                profiler.record('app', f'u{index}', total_msgs=1, flagged_msgs=flagged)
            self.advance_days(1)
        stats = profiler.stats()
        assert stats['summary_count'] == expected_summary
        profiler.close()
