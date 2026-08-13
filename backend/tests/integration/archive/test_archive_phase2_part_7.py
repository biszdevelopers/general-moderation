"""Phase 2 archive cycle tests (generated).

Volume and percentage matrices, multi-cycle chains, multi-user/app
archives and boundary edges under the frozen clock."""

# multilingual fixtures use non-ASCII on purpose
from __future__ import annotations

import pytest

from app.profiling.user_profiler import UserProfiler
from tests.base_test import BaseTest

_MULTI_APP_ARCHIVE_CASES: tuple[tuple[int, int, int, int], ...] = (
    (50, 0, 50, 3909,),
    (50, 1, 50, 3910,),
    (50, 2, 50, 3911,),
    (50, 3, 50, 3912,),
    (50, 4, 50, 3913,),
    (50, 5, 50, 3914,),
    (50, 6, 50, 3915,),
    (50, 7, 50, 3916,),
    (50, 8, 50, 3917,),
    (50, 9, 50, 3918,),
    (50, 10, 50, 3919,),
    (50, 11, 50, 3920,),
    (50, 12, 50, 3921,),
    (50, 13, 50, 3922,),
    (50, 14, 50, 3923,),
    (50, 15, 50, 3924,),
    (50, 16, 50, 3925,),
    (50, 17, 50, 3926,),
    (50, 18, 50, 3927,),
    (50, 19, 50, 3928,),
    (50, 20, 50, 3929,),
    (50, 21, 50, 3930,),
    (50, 22, 50, 3931,),
    (50, 23, 50, 3932,),
    (50, 24, 50, 3933,),
    (100, 0, 100, 3934,),
    (100, 1, 100, 3935,),
    (100, 2, 100, 3936,),
    (100, 3, 100, 3937,),
    (100, 4, 100, 3938,),
    (100, 5, 100, 3939,),
    (100, 6, 100, 3940,),
    (100, 7, 100, 3941,),
    (100, 8, 100, 3942,),
    (100, 9, 100, 3943,),
    (100, 10, 100, 3944,),
    (100, 11, 100, 3945,),
    (100, 12, 100, 3946,),
    (100, 13, 100, 3947,),
    (100, 14, 100, 3948,),
    (100, 15, 100, 3949,),
    (100, 16, 100, 3950,),
    (100, 17, 100, 3951,),
    (100, 18, 100, 3952,),
    (100, 19, 100, 3953,),
    (100, 20, 100, 3954,),
    (100, 21, 100, 3955,),
    (100, 22, 100, 3956,),
    (100, 23, 100, 3957,),
    (100, 24, 100, 3958,),
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


_MIXED_ARCHIVE_CASES: tuple[tuple[int, int, int, int, int, float, int], ...] = (
    (10, 1, 0, 0, 1, 0.1, 3959,),
    (20, 2, 1, 1, 1, 0.15, 3960,),
    (50, 5, 2, 2, 1, 0.14, 3961,),
    (100, 10, 5, 5, 1, 0.15, 3962,),
    (200, 20, 10, 10, 1, 0.15, 3963,),
    (500, 50, 25, 25, 1, 0.15, 3964,),
    (1000, 100, 50, 50, 1, 0.15, 3965,),
    (2500, 250, 125, 125, 1, 0.15, 3966,),
    (5000, 500, 250, 250, 1, 0.15, 3967,),
    (7500, 750, 375, 375, 1, 0.15, 3968,),
    (10, 2, 1, 0, 1, 0.3, 3969,),
    (20, 4, 2, 1, 1, 0.3, 3970,),
    (50, 10, 5, 2, 1, 0.3, 3971,),
    (100, 20, 10, 5, 1, 0.3, 3972,),
    (200, 40, 20, 10, 1, 0.3, 3973,),
    (500, 100, 50, 25, 1, 0.3, 3974,),
    (1000, 200, 100, 50, 1, 0.3, 3975,),
    (2500, 500, 250, 125, 1, 0.3, 3976,),
    (5000, 1000, 500, 250, 1, 0.3, 3977,),
    (7500, 1500, 750, 375, 1, 0.3, 3978,),
    (10, 3, 2, 1, 1, 0.5, 3979,),
    (20, 6, 3, 2, 1, 0.45, 3980,),
    (50, 15, 8, 5, 1, 0.46, 3981,),
    (100, 30, 15, 10, 1, 0.45, 3982,),
    (200, 60, 30, 20, 1, 0.45, 3983,),
    (500, 150, 75, 50, 1, 0.45, 3984,),
    (1000, 300, 150, 100, 1, 0.45, 3985,),
    (2500, 750, 375, 250, 1, 0.45, 3986,),
    (5000, 1500, 750, 500, 1, 0.45, 3987,),
    (7500, 2250, 1125, 750, 1, 0.45, 3988,),
    (10, 4, 2, 2, 1, 0.6, 3989,),
    (20, 8, 4, 3, 1, 0.6, 3990,),
    (50, 20, 10, 8, 1, 0.6, 3991,),
    (100, 40, 20, 15, 1, 0.6, 3992,),
    (200, 80, 40, 30, 1, 0.6, 3993,),
    (500, 200, 100, 75, 1, 0.6, 3994,),
    (1000, 400, 200, 150, 1, 0.6, 3995,),
    (2500, 1000, 500, 375, 1, 0.6, 3996,),
    (5000, 2000, 1000, 750, 1, 0.6, 3997,),
    (7500, 3000, 1500, 1125, 1, 0.6, 3998,),
    (10, 5, 2, 1, 1, 0.7, 3999,),
    (20, 10, 5, 2, 1, 0.75, 4000,),
    (50, 25, 12, 5, 1, 0.74, 4001,),
    (100, 50, 25, 10, 1, 0.75, 4002,),
    (200, 100, 50, 20, 1, 0.75, 4003,),
    (500, 250, 125, 50, 1, 0.75, 4004,),
    (1000, 500, 250, 100, 1, 0.75, 4005,),
    (2500, 1250, 625, 250, 1, 0.75, 4006,),
    (5000, 2500, 1250, 500, 1, 0.75, 4007,),
    (7500, 3750, 1875, 750, 1, 0.75, 4008,),
)

class TestMixedArchive(BaseTest):
    """Mixed-verdict windows archive each counter correctly."""

    @pytest.mark.parametrize(('volume', 'flagged', 'blocked', 'reviewed', 'expected_summaries', 'expected_ratio', 'uid',), _MIXED_ARCHIVE_CASES)
    def test_mixed_archive(self, volume: int, flagged: int, blocked: int, reviewed: int, expected_summaries: int, expected_ratio: float, uid: int) -> None:
        """Mixed-verdict windows archive each counter correctly."""
        profiler: UserProfiler = UserProfiler(':memory:', ':memory:', 91)
        for _ in range(91):
            profiler.record(
                'app', 'u',
                total_msgs=volume,
                flagged_msgs=flagged,
                blocked_msgs=blocked,
                reviewed_msgs=reviewed,
            )
            self.advance_days(1)
        profile = profiler.get_profile('app', 'u')
        assert len(profile['summaries']) == expected_summaries
        assert profiler.get_ratio('app', 'u') == expected_ratio
        profiler.close()
