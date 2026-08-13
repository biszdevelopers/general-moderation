"""Phase 2 admin API tests (generated).

Word CRUD, import/export, app policies, settings, logs and dashboard
stats; see tests/tools/phase2_generator.py."""

# multilingual fixtures use non-ASCII on purpose
from __future__ import annotations

from typing import Any

import pytest

from tests.base_test import BaseTest

_STATS_SCENARIO_CASES: tuple[tuple[int, int], ...] = (
    (1, 7824,),
    (2, 7825,),
    (3, 7826,),
    (4, 7827,),
    (5, 7828,),
    (6, 7829,),
    (7, 7830,),
    (8, 7831,),
    (9, 7832,),
    (10, 7833,),
    (11, 7834,),
    (12, 7835,),
    (13, 7836,),
    (14, 7837,),
    (15, 7838,),
    (16, 7839,),
    (17, 7840,),
    (18, 7841,),
    (19, 7842,),
    (20, 7843,),
    (21, 7844,),
    (22, 7845,),
    (23, 7846,),
    (24, 7847,),
    (25, 7848,),
    (26, 7849,),
    (27, 7850,),
    (28, 7851,),
    (29, 7852,),
    (30, 7853,),
    (31, 7854,),
    (32, 7855,),
    (33, 7856,),
    (34, 7857,),
    (35, 7858,),
    (36, 7859,),
    (37, 7860,),
    (38, 7861,),
    (39, 7862,),
    (40, 7863,),
    (41, 7864,),
    (42, 7865,),
    (43, 7866,),
    (44, 7867,),
    (45, 7868,),
    (46, 7869,),
    (47, 7870,),
    (48, 7871,),
    (49, 7872,),
    (50, 7873,),
    (51, 7874,),
    (52, 7875,),
    (53, 7876,),
    (54, 7877,),
    (55, 7878,),
    (56, 7879,),
    (57, 7880,),
    (58, 7881,),
    (59, 7882,),
    (60, 7883,),
    (61, 7884,),
    (62, 7885,),
    (63, 7886,),
    (64, 7887,),
    (65, 7888,),
    (66, 7889,),
    (67, 7890,),
    (68, 7891,),
    (69, 7892,),
    (70, 7893,),
    (71, 7894,),
    (72, 7895,),
    (73, 7896,),
    (74, 7897,),
    (75, 7898,),
    (76, 7899,),
    (77, 7900,),
    (78, 7901,),
    (79, 7902,),
    (80, 7903,),
    (81, 7904,),
    (82, 7905,),
    (83, 7906,),
    (84, 7907,),
    (85, 7908,),
    (86, 7909,),
    (87, 7910,),
    (88, 7911,),
    (89, 7912,),
    (90, 7913,),
    (91, 7914,),
    (92, 7915,),
    (93, 7916,),
    (94, 7917,),
    (95, 7918,),
    (96, 7919,),
    (97, 7920,),
    (98, 7921,),
    (99, 7922,),
    (100, 7923,),
)

class TestStatsScenario(BaseTest):
    """Dashboard stats reflect exact API activity."""

    @pytest.mark.parametrize(('n_mods', 'uid',), _STATS_SCENARIO_CASES)
    def test_stats_scenario(self, client: Any, admin_headers: dict[str, str], n_mods: int, uid: int) -> None:
        """Dashboard stats reflect exact API activity."""
        for index in range(n_mods):
            client.post('/moderate', json={'text': f'stats message {index}', 'app_name': 'a'})
        stats = client.get('/admin/stats', headers=admin_headers)
        assert stats.status_code == 200
        body = stats.json()
        assert body['metrics']['requests_total'] == n_mods
        assert 'profiling' in body
        assert 'word_bank' in body
        assert body['detector_count'] >= 4
        health = client.get('/admin/health', headers=admin_headers)
        assert health.json()['status'] == 'ok'
        spot = client.get('/admin/spot-check', headers=admin_headers)
        assert 'sample' in spot.json()
