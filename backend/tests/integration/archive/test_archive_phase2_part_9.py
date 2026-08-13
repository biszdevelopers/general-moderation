"""Phase 2 archive cycle tests (generated).

Volume and percentage matrices, multi-cycle chains, multi-user/app
archives and boundary edges under the frozen clock."""

# multilingual fixtures use non-ASCII on purpose
from __future__ import annotations

import pytest

from app.profiling.user_profiler import UserProfiler
from tests.base_test import BaseTest

_MIXED_ARCHIVE_CASES: tuple[tuple[int, int, int, int, int, float, int], ...] = (
    (10, 6, 1, 2, 1, 0.7, 4109,),
    (20, 13, 2, 5, 1, 0.75, 4110,),
    (50, 32, 5, 12, 1, 0.74, 4111,),
    (100, 65, 10, 25, 1, 0.75, 4112,),
    (200, 130, 20, 50, 1, 0.75, 4113,),
    (500, 325, 50, 125, 1, 0.75, 4114,),
    (1000, 650, 100, 250, 1, 0.75, 4115,),
    (2500, 1625, 250, 625, 1, 0.75, 4116,),
    (5000, 3250, 500, 1250, 1, 0.75, 4117,),
    (7500, 4875, 750, 1875, 1, 0.75, 4118,),
    (10, 8, 2, 1, 1, 1.0, 4119,),
    (20, 15, 3, 2, 1, 0.9, 4120,),
    (50, 38, 8, 5, 1, 0.92, 4121,),
    (100, 75, 15, 10, 1, 0.9, 4122,),
    (200, 150, 30, 20, 1, 0.9, 4123,),
    (500, 375, 75, 50, 1, 0.9, 4124,),
    (1000, 750, 150, 100, 1, 0.9, 4125,),
    (2500, 1875, 375, 250, 1, 0.9, 4126,),
    (5000, 3750, 750, 500, 1, 0.9, 4127,),
    (7500, 5625, 1125, 750, 1, 0.9, 4128,),
    (10, 8, 0, 1, 1, 0.8, 4129,),
    (20, 17, 1, 2, 1, 0.9, 4130,),
    (50, 42, 2, 5, 1, 0.88, 4131,),
    (100, 85, 5, 10, 1, 0.9, 4132,),
    (200, 170, 10, 20, 1, 0.9, 4133,),
    (500, 425, 25, 50, 1, 0.9, 4134,),
    (1000, 850, 50, 100, 1, 0.9, 4135,),
    (2500, 2125, 125, 250, 1, 0.9, 4136,),
    (5000, 4250, 250, 500, 1, 0.9, 4137,),
    (7500, 6375, 375, 750, 1, 0.9, 4138,),
    (10, 10, 0, 0, 1, 1.0, 4139,),
    (20, 19, 0, 1, 1, 0.95, 4140,),
    (50, 48, 0, 2, 1, 0.96, 4141,),
    (100, 95, 0, 5, 1, 0.95, 4142,),
    (200, 190, 0, 10, 1, 0.95, 4143,),
    (500, 475, 0, 25, 1, 0.95, 4144,),
    (1000, 950, 0, 50, 1, 0.95, 4145,),
    (2500, 2375, 0, 125, 1, 0.95, 4146,),
    (5000, 4750, 0, 250, 1, 0.95, 4147,),
    (7500, 7125, 0, 375, 1, 0.95, 4148,),
    (10, 1, 1, 0, 1, 0.2, 4149,),
    (20, 2, 2, 1, 1, 0.2, 4150,),
    (50, 6, 4, 2, 1, 0.2, 4151,),
    (100, 12, 8, 4, 1, 0.2, 4152,),
    (200, 24, 16, 8, 1, 0.2, 4153,),
    (500, 60, 40, 20, 1, 0.2, 4154,),
    (1000, 120, 80, 40, 1, 0.2, 4155,),
    (2500, 300, 200, 100, 1, 0.2, 4156,),
    (5000, 600, 400, 200, 1, 0.2, 4157,),
    (7500, 900, 600, 300, 1, 0.2, 4158,),
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


_EDGE_ARCHIVE_CASES: tuple[tuple[int, int, int, int, int, int, float, int, int, int], ...] = (
    (1, 1, 1, 1, 0, 0, 1.0, 1, 1, 4159,),
    (1, 1, 1, 0, 0, 0, 0.0, 1, 1, 4160,),
    (1, 1, 1, 0, 0, 0, 0.0, 1, 1, 4161,),
    (1, 1, 1, 0, 1, 0, 1.0, 1, 1, 4162,),
    (1, 1, 1, 0, 0, 1, 0.0, 1, 1, 4163,),
    (1, 1, 2, 2, 0, 0, 1.0, 1, 2, 4164,),
    (1, 1, 2, 0, 0, 0, 0.0, 1, 2, 4165,),
    (1, 1, 2, 1, 0, 0, 0.5, 1, 2, 4166,),
    (1, 1, 2, 0, 2, 0, 1.0, 1, 2, 4167,),
    (1, 1, 2, 0, 0, 2, 0.0, 1, 2, 4168,),
    (1, 1, 5, 5, 0, 0, 1.0, 1, 5, 4169,),
    (1, 1, 5, 0, 0, 0, 0.0, 1, 5, 4170,),
    (1, 1, 5, 2, 0, 0, 0.4, 1, 5, 4171,),
    (1, 1, 5, 0, 5, 0, 1.0, 1, 5, 4172,),
    (1, 1, 5, 0, 0, 5, 0.0, 1, 5, 4173,),
    (1, 1, 10, 10, 0, 0, 1.0, 1, 10, 4174,),
    (1, 1, 10, 0, 0, 0, 0.0, 1, 10, 4175,),
    (1, 1, 10, 5, 0, 0, 0.5, 1, 10, 4176,),
    (1, 1, 10, 0, 10, 0, 1.0, 1, 10, 4177,),
    (1, 1, 10, 0, 0, 10, 0.0, 1, 10, 4178,),
    (1, 1, 1, 1, 0, 0, 1.0, 1, 1, 4179,),
    (1, 1, 1, 0, 0, 0, 0.0, 1, 1, 4180,),
    (1, 1, 1, 0, 0, 0, 0.0, 1, 1, 4181,),
    (1, 1, 1, 0, 1, 0, 1.0, 1, 1, 4182,),
    (1, 1, 1, 0, 0, 1, 0.0, 1, 1, 4183,),
    (1, 1, 2, 2, 0, 0, 1.0, 1, 2, 4184,),
    (1, 1, 2, 0, 0, 0, 0.0, 1, 2, 4185,),
    (1, 1, 2, 1, 0, 0, 0.5, 1, 2, 4186,),
    (1, 1, 2, 0, 2, 0, 1.0, 1, 2, 4187,),
    (1, 1, 2, 0, 0, 2, 0.0, 1, 2, 4188,),
    (1, 1, 5, 5, 0, 0, 1.0, 1, 5, 4189,),
    (1, 1, 5, 0, 0, 0, 0.0, 1, 5, 4190,),
    (1, 1, 5, 2, 0, 0, 0.4, 1, 5, 4191,),
    (1, 1, 5, 0, 5, 0, 1.0, 1, 5, 4192,),
    (1, 1, 5, 0, 0, 5, 0.0, 1, 5, 4193,),
    (1, 1, 10, 10, 0, 0, 1.0, 1, 10, 4194,),
    (1, 1, 10, 0, 0, 0, 0.0, 1, 10, 4195,),
    (1, 1, 10, 5, 0, 0, 0.5, 1, 10, 4196,),
    (1, 1, 10, 0, 10, 0, 1.0, 1, 10, 4197,),
    (1, 1, 10, 0, 0, 10, 0.0, 1, 10, 4198,),
    (1, 2, 1, 1, 0, 0, 1.0, 2, 1, 4199,),
    (1, 2, 1, 0, 0, 0, 0.0, 2, 1, 4200,),
    (1, 2, 1, 0, 0, 0, 0.0, 2, 1, 4201,),
    (1, 2, 1, 0, 1, 0, 1.0, 2, 1, 4202,),
    (1, 2, 1, 0, 0, 1, 0.0, 2, 1, 4203,),
    (1, 2, 2, 2, 0, 0, 1.0, 2, 2, 4204,),
    (1, 2, 2, 0, 0, 0, 0.0, 2, 2, 4205,),
    (1, 2, 2, 1, 0, 0, 0.5, 2, 2, 4206,),
    (1, 2, 2, 0, 2, 0, 1.0, 2, 2, 4207,),
    (1, 2, 2, 0, 0, 2, 0.0, 2, 2, 4208,),
)

class TestEdgeArchive(BaseTest):
    """Boundary window and verdict states keep archive invariants."""

    @pytest.mark.parametrize(('window', 'days', 'volume', 'flagged', 'blocked', 'reviewed', 'expected_ratio', 'expected_summaries', 'expected_total', 'uid',), _EDGE_ARCHIVE_CASES)
    def test_edge_archive(self, window: int, days: int, volume: int, flagged: int, blocked: int, reviewed: int, expected_ratio: float, expected_summaries: int, expected_total: int, uid: int) -> None:
        """Boundary window and verdict states keep archive invariants."""
        profiler: UserProfiler = UserProfiler(':memory:', ':memory:', window)
        for _ in range(days):
            profiler.record(
                'app', 'u',
                total_msgs=volume,
                flagged_msgs=flagged,
                blocked_msgs=blocked,
                reviewed_msgs=reviewed,
            )
            self.advance_days(1)
        profile = profiler.get_profile('app', 'u')
        assert profiler.get_ratio('app', 'u') == expected_ratio
        assert len(profile['summaries']) == expected_summaries
        if expected_summaries:
            assert profile['summaries'][0]['total_msgs'] == expected_total
        profiler.close()
