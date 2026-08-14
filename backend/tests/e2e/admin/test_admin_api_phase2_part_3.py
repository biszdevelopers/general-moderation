"""Phase 2 admin API tests (generated).

Word CRUD, import/export, app policies, settings, logs and dashboard
stats; see tests/tools/phase2_generator.py."""

# multilingual fixtures use non-ASCII on purpose
from __future__ import annotations

from typing import Any

import pytest

from tests.base_test import BaseTest

_IMPORT_WORDS_CASES: tuple[tuple[int, int, int], ...] = (
    (10, 5, 7678,),
    (10, 6, 7679,),
    (10, 7, 7680,),
    (10, 8, 7681,),
    (10, 9, 7682,),
    (10, 10, 7683,),
    (10, 11, 7684,),
    (10, 12, 7685,),
    (10, 13, 7686,),
    (10, 14, 7687,),
    (25, 0, 7688,),
    (25, 1, 7689,),
    (25, 2, 7690,),
    (25, 3, 7691,),
    (25, 4, 7692,),
    (25, 5, 7693,),
    (25, 6, 7694,),
    (25, 7, 7695,),
    (25, 8, 7696,),
    (25, 9, 7697,),
    (25, 10, 7698,),
    (25, 11, 7699,),
    (25, 12, 7700,),
    (25, 13, 7701,),
    (25, 14, 7702,),
    (50, 0, 7703,),
    (50, 1, 7704,),
    (50, 2, 7705,),
    (50, 3, 7706,),
    (50, 4, 7707,),
    (50, 5, 7708,),
    (50, 6, 7709,),
    (50, 7, 7710,),
    (50, 8, 7711,),
    (50, 9, 7712,),
    (50, 10, 7713,),
    (50, 11, 7714,),
    (50, 12, 7715,),
    (50, 13, 7716,),
    (50, 14, 7717,),
    (100, 0, 7718,),
    (100, 1, 7719,),
    (100, 2, 7720,),
    (100, 3, 7721,),
    (100, 4, 7722,),
    (100, 5, 7723,),
    (100, 6, 7724,),
    (100, 7, 7725,),
    (100, 8, 7726,),
    (100, 9, 7727,),
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
    ('cfgapp', 0, 'or', True, True, 7733,),
    ('cfgapp', 0, 'or', True, False, 7734,),
    ('cfgapp', 0, 'or', False, True, 7735,),
    ('cfgapp', 0, 'or', False, False, 7736,),
    ('cfgapp', 0, 'and', True, True, 7737,),
    ('cfgapp', 0, 'and', True, False, 7738,),
    ('cfgapp', 0, 'and', False, True, 7739,),
    ('cfgapp', 0, 'and', False, False, 7740,),
    ('cfgapp', 10, 'or', True, True, 7741,),
    ('cfgapp', 10, 'or', True, False, 7742,),
    ('cfgapp', 10, 'or', False, True, 7743,),
    ('cfgapp', 10, 'or', False, False, 7744,),
    ('cfgapp', 10, 'and', True, True, 7745,),
    ('cfgapp', 10, 'and', True, False, 7746,),
    ('cfgapp', 10, 'and', False, True, 7747,),
    ('cfgapp', 10, 'and', False, False, 7748,),
    ('cfgapp', 20, 'or', True, True, 7749,),
    ('cfgapp', 20, 'or', True, False, 7750,),
    ('cfgapp', 20, 'or', False, True, 7751,),
    ('cfgapp', 20, 'or', False, False, 7752,),
    ('cfgapp', 20, 'and', True, True, 7753,),
    ('cfgapp', 20, 'and', True, False, 7754,),
    ('cfgapp', 20, 'and', False, True, 7755,),
    ('cfgapp', 20, 'and', False, False, 7756,),
    ('cfgapp', 30, 'or', True, True, 7757,),
    ('cfgapp', 30, 'or', True, False, 7758,),
    ('cfgapp', 30, 'or', False, True, 7759,),
    ('cfgapp', 30, 'or', False, False, 7760,),
    ('cfgapp', 30, 'and', True, True, 7761,),
    ('cfgapp', 30, 'and', True, False, 7762,),
    ('cfgapp', 30, 'and', False, True, 7763,),
    ('cfgapp', 30, 'and', False, False, 7764,),
    ('cfgapp', 40, 'or', True, True, 7765,),
    ('cfgapp', 40, 'or', True, False, 7766,),
    ('cfgapp', 40, 'or', False, True, 7767,),
    ('cfgapp', 40, 'or', False, False, 7768,),
    ('cfgapp', 40, 'and', True, True, 7769,),
    ('cfgapp', 40, 'and', True, False, 7770,),
    ('cfgapp', 40, 'and', False, True, 7771,),
    ('cfgapp', 40, 'and', False, False, 7772,),
    ('cfgapp', 50, 'or', True, True, 7773,),
    ('cfgapp', 50, 'or', True, False, 7774,),
    ('cfgapp', 50, 'or', False, True, 7775,),
    ('cfgapp', 50, 'or', False, False, 7776,),
    ('cfgapp', 50, 'and', True, True, 7777,),
    ('cfgapp', 50, 'and', True, False, 7778,),
    ('cfgapp', 50, 'and', False, True, 7779,),
    ('cfgapp', 50, 'and', False, False, 7780,),
    ('cfgapp', 60, 'or', True, True, 7781,),
    ('cfgapp', 60, 'or', True, False, 7782,),
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
