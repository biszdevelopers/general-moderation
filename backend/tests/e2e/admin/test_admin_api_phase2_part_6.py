"""Phase 2 admin API tests (generated).

Word CRUD, import/export, app policies, settings, logs and dashboard
stats; see tests/tools/phase2_generator.py."""

# multilingual fixtures use non-ASCII on purpose
from __future__ import annotations

from typing import Any

import pytest

from tests.base_test import BaseTest

_STATS_SCENARIO_CASES: tuple[tuple[int, int], ...] = (
    (1, 7983,),
    (2, 7984,),
    (3, 7985,),
    (4, 7986,),
    (5, 7987,),
    (6, 7988,),
    (7, 7989,),
    (8, 7990,),
    (9, 7991,),
    (10, 7992,),
    (11, 7993,),
    (12, 7994,),
    (13, 7995,),
    (14, 7996,),
    (15, 7997,),
    (16, 7998,),
    (17, 7999,),
    (18, 8000,),
    (19, 8001,),
    (20, 8002,),
    (21, 8003,),
    (22, 8004,),
    (23, 8005,),
    (24, 8006,),
    (25, 8007,),
    (26, 8008,),
    (27, 8009,),
    (28, 8010,),
    (29, 8011,),
    (30, 8012,),
    (31, 8013,),
    (32, 8014,),
    (33, 8015,),
    (34, 8016,),
    (35, 8017,),
    (36, 8018,),
    (37, 8019,),
    (38, 8020,),
    (39, 8021,),
    (40, 8022,),
    (41, 8023,),
    (42, 8024,),
    (43, 8025,),
    (44, 8026,),
    (45, 8027,),
    (46, 8028,),
    (47, 8029,),
    (48, 8030,),
    (49, 8031,),
    (50, 8032,),
    (51, 8033,),
    (52, 8034,),
    (53, 8035,),
    (54, 8036,),
    (55, 8037,),
    (56, 8038,),
    (57, 8039,),
    (58, 8040,),
    (59, 8041,),
    (60, 8042,),
    (61, 8043,),
    (62, 8044,),
    (63, 8045,),
    (64, 8046,),
    (65, 8047,),
    (66, 8048,),
    (67, 8049,),
    (68, 8050,),
    (69, 8051,),
    (70, 8052,),
    (71, 8053,),
    (72, 8054,),
    (73, 8055,),
    (74, 8056,),
    (75, 8057,),
    (76, 8058,),
    (77, 8059,),
    (78, 8060,),
    (79, 8061,),
    (80, 8062,),
    (81, 8063,),
    (82, 8064,),
    (83, 8065,),
    (84, 8066,),
    (85, 8067,),
    (86, 8068,),
    (87, 8069,),
    (88, 8070,),
    (89, 8071,),
    (90, 8072,),
    (91, 8073,),
    (92, 8074,),
    (93, 8075,),
    (94, 8076,),
    (95, 8077,),
    (96, 8078,),
    (97, 8079,),
    (98, 8080,),
    (99, 8081,),
    (100, 8082,),
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
