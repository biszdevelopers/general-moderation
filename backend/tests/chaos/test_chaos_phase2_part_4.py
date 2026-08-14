"""Phase 2 chaos and resilience tests (generated).

Hash storms, malformed databases, package adapter failures, engine
recovery and API bursts."""

# multilingual fixtures use non-ASCII on purpose
from __future__ import annotations

from typing import Any

import pytest

from tests.base_test import BaseTest

_ENGINE_RESILIENCE_CASES: tuple[tuple[int, int], ...] = (
    (1, 9805,),
    (2, 9806,),
    (3, 9807,),
    (4, 9808,),
    (5, 9809,),
    (6, 9810,),
    (7, 9811,),
    (8, 9812,),
    (9, 9813,),
    (10, 9814,),
    (11, 9815,),
    (12, 9816,),
    (13, 9817,),
    (14, 9818,),
    (15, 9819,),
    (16, 9820,),
    (17, 9821,),
    (18, 9822,),
    (19, 9823,),
    (20, 9824,),
    (21, 9825,),
    (22, 9826,),
    (23, 9827,),
    (24, 9828,),
    (25, 9829,),
    (26, 9830,),
    (27, 9831,),
    (28, 9832,),
    (29, 9833,),
    (30, 9834,),
    (31, 9835,),
    (32, 9836,),
    (33, 9837,),
    (34, 9838,),
    (35, 9839,),
    (36, 9840,),
    (37, 9841,),
    (38, 9842,),
    (39, 9843,),
    (40, 9844,),
    (41, 9845,),
    (42, 9846,),
    (43, 9847,),
    (44, 9848,),
    (45, 9849,),
    (46, 9850,),
    (47, 9851,),
    (48, 9852,),
    (49, 9853,),
    (50, 9854,),
    (51, 9855,),
    (52, 9856,),
    (53, 9857,),
    (54, 9858,),
    (55, 9859,),
    (56, 9860,),
    (57, 9861,),
    (58, 9862,),
    (59, 9863,),
    (60, 9864,),
    (61, 9865,),
    (62, 9866,),
    (63, 9867,),
    (64, 9868,),
    (65, 9869,),
    (66, 9870,),
    (67, 9871,),
    (68, 9872,),
    (69, 9873,),
    (70, 9874,),
    (71, 9875,),
    (72, 9876,),
    (73, 9877,),
    (74, 9878,),
    (75, 9879,),
    (76, 9880,),
    (77, 9881,),
    (78, 9882,),
    (79, 9883,),
    (80, 9884,),
    (81, 9885,),
    (82, 9886,),
    (83, 9887,),
    (84, 9888,),
    (85, 9889,),
    (86, 9890,),
    (87, 9891,),
    (88, 9892,),
    (89, 9893,),
    (90, 9894,),
    (91, 9895,),
    (92, 9896,),
    (93, 9897,),
    (94, 9898,),
    (95, 9899,),
    (96, 9900,),
    (97, 9901,),
    (98, 9902,),
    (99, 9903,),
    (100, 9904,),
)

class TestEngineResilience(BaseTest):
    """The engine recovers across clear, refresh and re-moderate."""

    @pytest.mark.parametrize(('n_moderations', 'uid',), _ENGINE_RESILIENCE_CASES)
    def test_engine_resilience(self, engine: Any, word_bank: Any, n_moderations: int, uid: int) -> None:
        """The engine recovers across clear, refresh and re-moderate."""
        from app.models.request import ModerationRequest
        for index in range(n_moderations):
            engine.moderate(ModerationRequest(text=f'resilient {index}', app_name='a'))
        engine.clear_cache()
        assert isinstance(engine.metrics(), dict)
        engine.refresh_detectors()
        result = engine.moderate(ModerationRequest(text='after refresh', app_name='a'))
        assert result.verdict is not None
