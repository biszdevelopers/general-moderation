"""Phase 2 chaos and resilience tests (generated).

Hash storms, malformed databases, package adapter failures, engine
recovery and API bursts."""

# multilingual fixtures use non-ASCII on purpose
from __future__ import annotations

from typing import Any

import pytest

from tests.base_test import BaseTest

_ENGINE_RESILIENCE_CASES: tuple[tuple[int, int], ...] = (
    (1, 9765,),
    (2, 9766,),
    (3, 9767,),
    (4, 9768,),
    (5, 9769,),
    (6, 9770,),
    (7, 9771,),
    (8, 9772,),
    (9, 9773,),
    (10, 9774,),
    (11, 9775,),
    (12, 9776,),
    (13, 9777,),
    (14, 9778,),
    (15, 9779,),
    (16, 9780,),
    (17, 9781,),
    (18, 9782,),
    (19, 9783,),
    (20, 9784,),
    (21, 9785,),
    (22, 9786,),
    (23, 9787,),
    (24, 9788,),
    (25, 9789,),
    (26, 9790,),
    (27, 9791,),
    (28, 9792,),
    (29, 9793,),
    (30, 9794,),
    (31, 9795,),
    (32, 9796,),
    (33, 9797,),
    (34, 9798,),
    (35, 9799,),
    (36, 9800,),
    (37, 9801,),
    (38, 9802,),
    (39, 9803,),
    (40, 9804,),
    (41, 9805,),
    (42, 9806,),
    (43, 9807,),
    (44, 9808,),
    (45, 9809,),
    (46, 9810,),
    (47, 9811,),
    (48, 9812,),
    (49, 9813,),
    (50, 9814,),
    (51, 9815,),
    (52, 9816,),
    (53, 9817,),
    (54, 9818,),
    (55, 9819,),
    (56, 9820,),
    (57, 9821,),
    (58, 9822,),
    (59, 9823,),
    (60, 9824,),
    (61, 9825,),
    (62, 9826,),
    (63, 9827,),
    (64, 9828,),
    (65, 9829,),
    (66, 9830,),
    (67, 9831,),
    (68, 9832,),
    (69, 9833,),
    (70, 9834,),
    (71, 9835,),
    (72, 9836,),
    (73, 9837,),
    (74, 9838,),
    (75, 9839,),
    (76, 9840,),
    (77, 9841,),
    (78, 9842,),
    (79, 9843,),
    (80, 9844,),
    (81, 9845,),
    (82, 9846,),
    (83, 9847,),
    (84, 9848,),
    (85, 9849,),
    (86, 9850,),
    (87, 9851,),
    (88, 9852,),
    (89, 9853,),
    (90, 9854,),
    (91, 9855,),
    (92, 9856,),
    (93, 9857,),
    (94, 9858,),
    (95, 9859,),
    (96, 9860,),
    (97, 9861,),
    (98, 9862,),
    (99, 9863,),
    (100, 9864,),
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
