"""Phase 2 user profiling tests (generated).

Ratio matrices, window sweeps, multi-user/app archives and cycle
chains under the frozen clock; see tests/tools/phase2_generator.py."""

# multilingual fixtures use non-ASCII on purpose
from __future__ import annotations

import pytest

from app.profiling.user_profiler import UserProfiler
from tests.base_test import BaseTest

_WINDOW_LENGTH_CASES: tuple[tuple[int, int, float, int], ...] = (
    (1, 0, 0.0, 2801,),
    (1, 1, 0.5, 2802,),
    (2, 0, 0.0, 2806,),
    (2, 1, 0.5, 2807,),
    (3, 0, 0.0, 2811,),
    (3, 1, 0.5, 2812,),
    (4, 0, 0.0, 2816,),
    (4, 1, 0.5, 2817,),
    (5, 0, 0.0, 2821,),
    (5, 1, 0.5, 2822,),
    (6, 0, 0.0, 2826,),
    (6, 1, 0.5, 2827,),
    (7, 0, 0.0, 2831,),
    (7, 1, 0.5, 2832,),
    (10, 0, 0.0, 2836,),
    (10, 1, 0.5, 2837,),
    (14, 0, 0.0, 2841,),
    (14, 1, 0.5, 2842,),
    (15, 0, 0.0, 2846,),
    (15, 1, 0.5, 2847,),
    (21, 0, 0.0, 2851,),
    (21, 1, 0.5, 2852,),
    (28, 0, 0.0, 2856,),
    (28, 1, 0.5, 2857,),
    (30, 0, 0.0, 2861,),
    (30, 1, 0.5, 2862,),
    (45, 0, 0.0, 2866,),
    (45, 1, 0.5, 2867,),
    (60, 0, 0.0, 2871,),
    (60, 1, 0.5, 2872,),
    (90, 0, 0.0, 2876,),
    (90, 1, 0.5, 2877,),
    (91, 0, 0.0, 2881,),
    (91, 1, 0.5, 2882,),
    (120, 0, 0.0, 2886,),
    (120, 1, 0.5, 2887,),
    (180, 0, 0.0, 2891,),
    (180, 1, 0.5, 2892,),
    (365, 0, 0.0, 2896,),
    (365, 1, 0.5, 2897,),
)

class TestWindowLength(BaseTest):
    """Ratios hold for every supported window length."""

    @pytest.mark.parametrize(('window', 'flagged', 'expected', 'uid',), _WINDOW_LENGTH_CASES)
    def test_window_length(self, window: int, flagged: int, expected: float, uid: int) -> None:
        """Ratios hold for every supported window length."""
        profiler: UserProfiler = UserProfiler(':memory:', ':memory:', window)
        profiler.record('app', 'u', total_msgs=2, flagged_msgs=flagged)
        assert profiler.get_ratio('app', 'u') == expected
        profiler.close()


_WINDOW_LENGTH_HIGH_CASES: tuple[tuple[int, int, float, int], ...] = (
    (1, 2, 0.5, 2803,),
    (1, 3, 0.75, 2804,),
    (2, 2, 0.5, 2808,),
    (2, 3, 0.75, 2809,),
    (3, 2, 0.5, 2813,),
    (3, 3, 0.75, 2814,),
    (4, 2, 0.5, 2818,),
    (4, 3, 0.75, 2819,),
    (5, 2, 0.5, 2823,),
    (5, 3, 0.75, 2824,),
    (6, 2, 0.5, 2828,),
    (6, 3, 0.75, 2829,),
    (7, 2, 0.5, 2833,),
    (7, 3, 0.75, 2834,),
    (10, 2, 0.5, 2838,),
    (10, 3, 0.75, 2839,),
    (14, 2, 0.5, 2843,),
    (14, 3, 0.75, 2844,),
    (15, 2, 0.5, 2848,),
    (15, 3, 0.75, 2849,),
    (21, 2, 0.5, 2853,),
    (21, 3, 0.75, 2854,),
    (28, 2, 0.5, 2858,),
    (28, 3, 0.75, 2859,),
    (30, 2, 0.5, 2863,),
    (30, 3, 0.75, 2864,),
    (45, 2, 0.5, 2868,),
    (45, 3, 0.75, 2869,),
    (60, 2, 0.5, 2873,),
    (60, 3, 0.75, 2874,),
    (90, 2, 0.5, 2878,),
    (90, 3, 0.75, 2879,),
    (91, 2, 0.5, 2883,),
    (91, 3, 0.75, 2884,),
    (120, 2, 0.5, 2888,),
    (120, 3, 0.75, 2889,),
    (180, 2, 0.5, 2893,),
    (180, 3, 0.75, 2894,),
    (365, 2, 0.5, 2898,),
    (365, 3, 0.75, 2899,),
)

class TestWindowLengthHigh(BaseTest):
    """Higher flag counts keep the window invariant."""

    @pytest.mark.parametrize(('window', 'flagged', 'expected', 'uid',), _WINDOW_LENGTH_HIGH_CASES)
    def test_window_length_high(self, window: int, flagged: int, expected: float, uid: int) -> None:
        """Higher flag counts keep the window invariant."""
        profiler: UserProfiler = UserProfiler(':memory:', ':memory:', window)
        profiler.record('app', 'u', total_msgs=4, flagged_msgs=flagged)
        assert profiler.get_ratio('app', 'u') == expected
        profiler.close()


_WINDOW_BOUNDARY_CASES: tuple[tuple[int, int, int], ...] = (
    (1, 1, 2805,),
    (2, 1, 2810,),
    (3, 1, 2815,),
    (4, 1, 2820,),
    (5, 1, 2825,),
    (6, 1, 2830,),
    (7, 1, 2835,),
    (10, 1, 2840,),
    (14, 1, 2845,),
    (15, 1, 2850,),
    (21, 1, 2855,),
    (28, 1, 2860,),
    (30, 1, 2865,),
    (45, 1, 2870,),
    (60, 1, 2875,),
    (90, 1, 2880,),
    (91, 1, 2885,),
    (120, 1, 2890,),
    (180, 1, 2895,),
    (365, 1, 2900,),
)

class TestWindowBoundary(BaseTest):
    """Reaching the window day closes the cycle."""

    @pytest.mark.parametrize(('window', 'expected', 'uid',), _WINDOW_BOUNDARY_CASES)
    def test_window_boundary(self, window: int, expected: int, uid: int) -> None:
        """Reaching the window day closes the cycle."""
        profiler: UserProfiler = UserProfiler(':memory:', ':memory:', window)
        for _ in range(window):
            profiler.record('app', 'u', total_msgs=1)
            self.advance_days(1)
        profile = profiler.get_profile('app', 'u')
        assert len(profile['summaries']) == expected
        profiler.close()
