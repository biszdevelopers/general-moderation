"""Phase 2 user profiling tests (generated).

Ratio matrices, window sweeps, multi-user/app archives and cycle
chains under the frozen clock; see tests/tools/phase2_generator.py."""

# multilingual fixtures use non-ASCII on purpose
from __future__ import annotations

import pytest

from app.profiling.user_profiler import UserProfiler
from tests.base_test import BaseTest

_MULTI_APP_CASES: tuple[tuple[int, int, int, int], ...] = (
    (20, 9, 20, 3101,),
    (20, 10, 20, 3102,),
    (20, 11, 20, 3103,),
    (20, 12, 20, 3104,),
    (20, 13, 20, 3105,),
    (20, 14, 20, 3106,),
    (20, 15, 20, 3107,),
    (20, 16, 20, 3108,),
    (50, 0, 50, 3109,),
    (50, 1, 50, 3110,),
    (50, 2, 50, 3111,),
    (50, 3, 50, 3112,),
    (50, 4, 50, 3113,),
    (50, 5, 50, 3114,),
    (50, 6, 50, 3115,),
    (50, 7, 50, 3116,),
    (50, 8, 50, 3117,),
    (50, 9, 50, 3118,),
    (50, 10, 50, 3119,),
    (50, 11, 50, 3120,),
    (50, 12, 50, 3121,),
    (50, 13, 50, 3122,),
    (50, 14, 50, 3123,),
    (50, 15, 50, 3124,),
    (50, 16, 50, 3125,),
    (100, 0, 100, 3126,),
    (100, 1, 100, 3127,),
    (100, 2, 100, 3128,),
    (100, 3, 100, 3129,),
    (100, 4, 100, 3130,),
    (100, 5, 100, 3131,),
    (100, 6, 100, 3132,),
    (100, 7, 100, 3133,),
    (100, 8, 100, 3134,),
    (100, 9, 100, 3135,),
    (100, 10, 100, 3136,),
    (100, 11, 100, 3137,),
    (100, 12, 100, 3138,),
    (100, 13, 100, 3139,),
    (100, 14, 100, 3140,),
)

class TestMultiApp(BaseTest):
    """Each app archives independently for the shared user."""

    @pytest.mark.parametrize(('app_count', 'scenario', 'expected_summary', 'uid',), _MULTI_APP_CASES)
    def test_multi_app(self, app_count: int, scenario: int, expected_summary: int, uid: int) -> None:
        """Each app archives independently for the shared user."""
        profiler: UserProfiler = UserProfiler(':memory:', ':memory:', 3)
        for _ in range(3):
            for index in range(app_count):
                flagged = 1 if (index + scenario) % 3 == 0 else 0
                profiler.record(f'app{index}', 'u', total_msgs=1, flagged_msgs=flagged)
            self.advance_days(1)
        stats = profiler.stats()
        assert stats['summary_count'] == expected_summary
        profiler.close()


_CYCLES_CASES: tuple[tuple[int, int, int, int], ...] = (
    (2, 0, 2, 3143,),
    (2, 1, 2, 3144,),
    (2, 2, 2, 3145,),
    (2, 3, 2, 3146,),
    (2, 4, 2, 3147,),
    (2, 5, 2, 3148,),
    (2, 6, 2, 3149,),
    (2, 7, 2, 3150,),
    (2, 8, 2, 3151,),
    (2, 9, 2, 3152,),
    (2, 10, 2, 3153,),
    (2, 11, 2, 3154,),
    (3, 0, 3, 3155,),
    (3, 1, 3, 3156,),
    (3, 2, 3, 3157,),
    (3, 3, 3, 3158,),
    (3, 4, 3, 3159,),
    (3, 5, 3, 3160,),
    (3, 6, 3, 3161,),
    (3, 7, 3, 3162,),
    (3, 8, 3, 3163,),
    (3, 9, 3, 3164,),
    (3, 10, 3, 3165,),
    (3, 11, 3, 3166,),
    (4, 0, 4, 3167,),
    (4, 1, 4, 3168,),
    (4, 2, 4, 3169,),
    (4, 3, 4, 3170,),
    (4, 4, 4, 3171,),
    (4, 5, 4, 3172,),
    (4, 6, 4, 3173,),
    (4, 7, 4, 3174,),
    (4, 8, 4, 3175,),
    (4, 9, 4, 3176,),
    (4, 10, 4, 3177,),
    (4, 11, 4, 3178,),
    (5, 0, 5, 3179,),
    (5, 1, 5, 3180,),
    (5, 2, 5, 3181,),
    (5, 3, 5, 3182,),
    (5, 4, 5, 3183,),
    (5, 5, 5, 3184,),
    (5, 6, 5, 3185,),
    (5, 7, 5, 3186,),
    (5, 8, 5, 3187,),
    (5, 9, 5, 3188,),
    (5, 10, 5, 3189,),
    (5, 11, 5, 3190,),
    (10, 0, 10, 3191,),
    (10, 1, 10, 3192,),
    (10, 2, 10, 3193,),
    (10, 3, 10, 3194,),
    (10, 4, 10, 3195,),
    (10, 5, 10, 3196,),
    (10, 6, 10, 3197,),
    (10, 7, 10, 3198,),
    (10, 8, 10, 3199,),
    (10, 9, 10, 3200,),
    (10, 10, 10, 3201,),
    (10, 11, 10, 3202,),
)

class TestCycles(BaseTest):
    """Repeated short windows produce the expected cycle count."""

    @pytest.mark.parametrize(('cycle_count', 'pattern', 'expected_cycles', 'uid',), _CYCLES_CASES)
    def test_cycles(self, cycle_count: int, pattern: int, expected_cycles: int, uid: int) -> None:
        """Repeated short windows produce the expected cycle count."""
        profiler: UserProfiler = UserProfiler(':memory:', ':memory:', 2)
        for _ in range(cycle_count * 2):
            profiler.record('app', 'u', total_msgs=1, flagged_msgs=pattern % 2)
            self.advance_days(1)
        profile = profiler.get_profile('app', 'u')
        assert len(profile['summaries']) == expected_cycles
        profiler.close()
