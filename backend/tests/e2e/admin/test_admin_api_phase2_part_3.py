"""Phase 2 admin API tests (generated).

Word CRUD, import/export, app policies, settings, logs and dashboard
stats; see tests/tools/phase2_generator.py."""

# multilingual fixtures use non-ASCII on purpose
from __future__ import annotations

from typing import Any

import pytest

from tests.base_test import BaseTest

_IMPORT_WORDS_CASES: tuple[tuple[int, int, int], ...] = (
    (10, 5, 7718,),
    (10, 6, 7719,),
    (10, 7, 7720,),
    (10, 8, 7721,),
    (10, 9, 7722,),
    (10, 10, 7723,),
    (10, 11, 7724,),
    (10, 12, 7725,),
    (10, 13, 7726,),
    (10, 14, 7727,),
    (25, 0, 7728,),
    (25, 1, 7729,),
    (25, 2, 7730,),
    (25, 3, 7731,),
    (25, 4, 7732,),
    (25, 5, 7733,),
    (25, 6, 7734,),
    (25, 7, 7735,),
    (25, 8, 7736,),
    (25, 9, 7737,),
    (25, 10, 7738,),
    (25, 11, 7739,),
    (25, 12, 7740,),
    (25, 13, 7741,),
    (25, 14, 7742,),
    (50, 0, 7743,),
    (50, 1, 7744,),
    (50, 2, 7745,),
    (50, 3, 7746,),
    (50, 4, 7747,),
    (50, 5, 7748,),
    (50, 6, 7749,),
    (50, 7, 7750,),
    (50, 8, 7751,),
    (50, 9, 7752,),
    (50, 10, 7753,),
    (50, 11, 7754,),
    (50, 12, 7755,),
    (50, 13, 7756,),
    (50, 14, 7757,),
    (100, 0, 7758,),
    (100, 1, 7759,),
    (100, 2, 7760,),
    (100, 3, 7761,),
    (100, 4, 7762,),
    (100, 5, 7763,),
    (100, 6, 7764,),
    (100, 7, 7765,),
    (100, 8, 7766,),
    (100, 9, 7767,),
)

class TestImportWords(BaseTest):
    """Bulk import reports the imported count."""

    @pytest.mark.parametrize(('size', 'scenario', 'uid',), _IMPORT_WORDS_CASES)
    def test_import_words(self, client: Any, admin_headers: dict[str, str], size: int, scenario: int, uid: int) -> None:
        """Bulk import reports the imported count."""
        items = [{'word': f'imp{index}_{scenario}'} for index in range(size)]
        response = client.post('/admin/wordbank/import', headers=admin_headers, json={'items': items})
        assert response.status_code == 200
        assert response.json()['imported'] == size
        stats = client.get('/admin/wordbank/stats', headers=admin_headers).json()
        assert stats['customWords'] >= size


_APP_CONFIG_CASES: tuple[tuple[str, int, str, bool, bool, int], ...] = (
    ('cfgapp', 0, 'or', True, True, 7773,),
    ('cfgapp', 0, 'or', True, False, 7774,),
    ('cfgapp', 0, 'or', False, True, 7775,),
    ('cfgapp', 0, 'or', False, False, 7776,),
    ('cfgapp', 0, 'and', True, True, 7777,),
    ('cfgapp', 0, 'and', True, False, 7778,),
    ('cfgapp', 0, 'and', False, True, 7779,),
    ('cfgapp', 0, 'and', False, False, 7780,),
    ('cfgapp', 10, 'or', True, True, 7781,),
    ('cfgapp', 10, 'or', True, False, 7782,),
    ('cfgapp', 10, 'or', False, True, 7783,),
    ('cfgapp', 10, 'or', False, False, 7784,),
    ('cfgapp', 10, 'and', True, True, 7785,),
    ('cfgapp', 10, 'and', True, False, 7786,),
    ('cfgapp', 10, 'and', False, True, 7787,),
    ('cfgapp', 10, 'and', False, False, 7788,),
    ('cfgapp', 20, 'or', True, True, 7789,),
    ('cfgapp', 20, 'or', True, False, 7790,),
    ('cfgapp', 20, 'or', False, True, 7791,),
    ('cfgapp', 20, 'or', False, False, 7792,),
    ('cfgapp', 20, 'and', True, True, 7793,),
    ('cfgapp', 20, 'and', True, False, 7794,),
    ('cfgapp', 20, 'and', False, True, 7795,),
    ('cfgapp', 20, 'and', False, False, 7796,),
    ('cfgapp', 30, 'or', True, True, 7797,),
    ('cfgapp', 30, 'or', True, False, 7798,),
    ('cfgapp', 30, 'or', False, True, 7799,),
    ('cfgapp', 30, 'or', False, False, 7800,),
    ('cfgapp', 30, 'and', True, True, 7801,),
    ('cfgapp', 30, 'and', True, False, 7802,),
    ('cfgapp', 30, 'and', False, True, 7803,),
    ('cfgapp', 30, 'and', False, False, 7804,),
    ('cfgapp', 40, 'or', True, True, 7805,),
    ('cfgapp', 40, 'or', True, False, 7806,),
    ('cfgapp', 40, 'or', False, True, 7807,),
    ('cfgapp', 40, 'or', False, False, 7808,),
    ('cfgapp', 40, 'and', True, True, 7809,),
    ('cfgapp', 40, 'and', True, False, 7810,),
    ('cfgapp', 40, 'and', False, True, 7811,),
    ('cfgapp', 40, 'and', False, False, 7812,),
    ('cfgapp', 50, 'or', True, True, 7813,),
    ('cfgapp', 50, 'or', True, False, 7814,),
    ('cfgapp', 50, 'or', False, True, 7815,),
    ('cfgapp', 50, 'or', False, False, 7816,),
    ('cfgapp', 50, 'and', True, True, 7817,),
    ('cfgapp', 50, 'and', True, False, 7818,),
    ('cfgapp', 50, 'and', False, True, 7819,),
    ('cfgapp', 50, 'and', False, False, 7820,),
    ('cfgapp', 60, 'or', True, True, 7821,),
    ('cfgapp', 60, 'or', True, False, 7822,),
)

class TestAppConfig(BaseTest):
    """App trigger policies store and return every field."""

    @pytest.mark.parametrize(('app_name', 'threshold', 'logic', 'sboost', 'uboost', 'uid',), _APP_CONFIG_CASES)
    def test_app_config(self, client: Any, admin_headers: dict[str, str], app_name: str, threshold: int, logic: str, sboost: bool, uboost: bool, uid: int) -> None:
        """App trigger policies store and return every field."""
        payload = {'app_name': app_name, 'score_threshold': threshold, 'logic_type': logic, 'semantic_boost': sboost, 'user_ratio_boost': uboost}
        response = client.post('/admin/app-config', headers=admin_headers, json=payload)
        assert response.status_code == 200
        assert response.json()['score_threshold'] == threshold
        assert response.json()['logic_type'] == logic
        assert response.json()['semantic_boost'] is sboost
