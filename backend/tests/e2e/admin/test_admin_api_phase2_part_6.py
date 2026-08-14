"""Phase 2 admin API tests (generated).

Word CRUD, import/export, app policies, settings, logs and dashboard
stats; see tests/tools/phase2_generator.py."""

# multilingual fixtures use non-ASCII on purpose
from __future__ import annotations

from typing import Any

import pytest

from tests.base_test import BaseTest

_STATS_SCENARIO_CASES: tuple[tuple[int, int], ...] = (
    (1, 8023,),
    (2, 8024,),
    (3, 8025,),
    (4, 8026,),
    (5, 8027,),
    (6, 8028,),
    (7, 8029,),
    (8, 8030,),
    (9, 8031,),
    (10, 8032,),
    (11, 8033,),
    (12, 8034,),
    (13, 8035,),
    (14, 8036,),
    (15, 8037,),
    (16, 8038,),
    (17, 8039,),
    (18, 8040,),
    (19, 8041,),
    (20, 8042,),
    (21, 8043,),
    (22, 8044,),
    (23, 8045,),
    (24, 8046,),
    (25, 8047,),
    (26, 8048,),
    (27, 8049,),
    (28, 8050,),
    (29, 8051,),
    (30, 8052,),
    (31, 8053,),
    (32, 8054,),
    (33, 8055,),
    (34, 8056,),
    (35, 8057,),
    (36, 8058,),
    (37, 8059,),
    (38, 8060,),
    (39, 8061,),
    (40, 8062,),
    (41, 8063,),
    (42, 8064,),
    (43, 8065,),
    (44, 8066,),
    (45, 8067,),
    (46, 8068,),
    (47, 8069,),
    (48, 8070,),
    (49, 8071,),
    (50, 8072,),
    (51, 8073,),
    (52, 8074,),
    (53, 8075,),
    (54, 8076,),
    (55, 8077,),
    (56, 8078,),
    (57, 8079,),
    (58, 8080,),
    (59, 8081,),
    (60, 8082,),
    (61, 8083,),
    (62, 8084,),
    (63, 8085,),
    (64, 8086,),
    (65, 8087,),
    (66, 8088,),
    (67, 8089,),
    (68, 8090,),
    (69, 8091,),
    (70, 8092,),
    (71, 8093,),
    (72, 8094,),
    (73, 8095,),
    (74, 8096,),
    (75, 8097,),
    (76, 8098,),
    (77, 8099,),
    (78, 8100,),
    (79, 8101,),
    (80, 8102,),
    (81, 8103,),
    (82, 8104,),
    (83, 8105,),
    (84, 8106,),
    (85, 8107,),
    (86, 8108,),
    (87, 8109,),
    (88, 8110,),
    (89, 8111,),
    (90, 8112,),
    (91, 8113,),
    (92, 8114,),
    (93, 8115,),
    (94, 8116,),
    (95, 8117,),
    (96, 8118,),
    (97, 8119,),
    (98, 8120,),
    (99, 8121,),
    (100, 8122,),
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
