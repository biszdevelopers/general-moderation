"""Phase 2 admin API tests (generated).

Word CRUD, import/export, app policies, settings, logs and dashboard
stats; see tests/tools/phase2_generator.py."""

# multilingual fixtures use non-ASCII on purpose
from __future__ import annotations

from typing import Any

import pytest

from tests.base_test import BaseTest

_APP_CONFIG_CASES: tuple[tuple[str, int, str, bool, bool, int], ...] = (
    ('cfgapp', 60, 'or', False, True, 7823,),
    ('cfgapp', 60, 'or', False, False, 7824,),
    ('cfgapp', 60, 'and', True, True, 7825,),
    ('cfgapp', 60, 'and', True, False, 7826,),
    ('cfgapp', 60, 'and', False, True, 7827,),
    ('cfgapp', 60, 'and', False, False, 7828,),
    ('cfgapp', 70, 'or', True, True, 7829,),
    ('cfgapp', 70, 'or', True, False, 7830,),
    ('cfgapp', 70, 'or', False, True, 7831,),
    ('cfgapp', 70, 'or', False, False, 7832,),
    ('cfgapp', 70, 'and', True, True, 7833,),
    ('cfgapp', 70, 'and', True, False, 7834,),
    ('cfgapp', 70, 'and', False, True, 7835,),
    ('cfgapp', 70, 'and', False, False, 7836,),
    ('cfgapp', 80, 'or', True, True, 7837,),
    ('cfgapp', 80, 'or', True, False, 7838,),
    ('cfgapp', 80, 'or', False, True, 7839,),
    ('cfgapp', 80, 'or', False, False, 7840,),
    ('cfgapp', 80, 'and', True, True, 7841,),
    ('cfgapp', 80, 'and', True, False, 7842,),
    ('cfgapp', 80, 'and', False, True, 7843,),
    ('cfgapp', 80, 'and', False, False, 7844,),
    ('cfgapp', 90, 'or', True, True, 7845,),
    ('cfgapp', 90, 'or', True, False, 7846,),
    ('cfgapp', 90, 'or', False, True, 7847,),
    ('cfgapp', 90, 'or', False, False, 7848,),
    ('cfgapp', 90, 'and', True, True, 7849,),
    ('cfgapp', 90, 'and', True, False, 7850,),
    ('cfgapp', 90, 'and', False, True, 7851,),
    ('cfgapp', 90, 'and', False, False, 7852,),
    ('cfgapp', 100, 'or', True, True, 7853,),
    ('cfgapp', 100, 'or', True, False, 7854,),
    ('cfgapp', 100, 'or', False, True, 7855,),
    ('cfgapp', 100, 'or', False, False, 7856,),
    ('cfgapp', 100, 'and', True, True, 7857,),
    ('cfgapp', 100, 'and', True, False, 7858,),
    ('cfgapp', 100, 'and', False, True, 7859,),
    ('cfgapp', 100, 'and', False, False, 7860,),
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


_APP_CONFIG_INVALID_CASES: tuple[tuple[int, int], ...] = (
    (-1, 7861,),
    (101, 7862,),
)

class TestAppConfigInvalid(BaseTest):
    """Out-of-range thresholds are rejected."""

    @pytest.mark.parametrize(('threshold', 'uid',), _APP_CONFIG_INVALID_CASES)
    def test_app_config_invalid(self, client: Any, admin_headers: dict[str, str], threshold: int, uid: int) -> None:
        """Out-of-range thresholds are rejected."""
        payload = {'app_name': 'bad', 'score_threshold': threshold}
        response = client.post('/admin/app-config', headers=admin_headers, json=payload)
        assert response.status_code == 422


_APP_CONFIG_DEFAULT_CASES: tuple[tuple[str, int], ...] = (
    ('ghost0', 7863,),
    ('ghost1', 7864,),
    ('ghost2', 7865,),
    ('ghost3', 7866,),
    ('ghost4', 7867,),
    ('ghost5', 7868,),
    ('ghost6', 7869,),
    ('ghost7', 7870,),
    ('ghost8', 7871,),
    ('ghost9', 7872,),
)

class TestAppConfigDefault(BaseTest):
    """Unknown apps fall back to the default policy."""

    @pytest.mark.parametrize(('app_name', 'uid',), _APP_CONFIG_DEFAULT_CASES)
    def test_app_config_default(self, client: Any, admin_headers: dict[str, str], app_name: str, uid: int) -> None:
        """Unknown apps fall back to the default policy."""
        response = client.get(f'/admin/app-config/{app_name}', headers=admin_headers)
        assert response.status_code == 200
        assert response.json()['score_threshold'] == 50


_SETTINGS_ENDPOINT_CASES: tuple[tuple[str, int, int], ...] = (
    ('WEIGHT_DETECTOR_AHO', 5, 7873,),
    ('WEIGHT_DETECTOR_AHO', 8, 7874,),
    ('WEIGHT_DETECTOR_AHO', 10, 7875,),
    ('WEIGHT_DETECTOR_AHO', 12, 7876,),
    ('WEIGHT_DETECTOR_AHO', 15, 7877,),
    ('WEIGHT_DETECTOR_AHO', 18, 7878,),
    ('WEIGHT_DETECTOR_AHO', 20, 7879,),
    ('WEIGHT_DETECTOR_AHO', 22, 7880,),
    ('WEIGHT_DETECTOR_AHO', 25, 7881,),
    ('WEIGHT_DETECTOR_AHO', 28, 7882,),
    ('WEIGHT_DETECTOR_AHO', 30, 7883,),
    ('WEIGHT_DETECTOR_AHO', 32, 7884,),
    ('WEIGHT_DETECTOR_AHO', 35, 7885,),
    ('WEIGHT_DETECTOR_AHO', 38, 7886,),
    ('WEIGHT_DETECTOR_AHO', 40, 7887,),
    ('WEIGHT_DETECTOR_AHO', 42, 7888,),
    ('WEIGHT_DETECTOR_AHO', 45, 7889,),
    ('WEIGHT_DETECTOR_AHO', 47, 7890,),
    ('WEIGHT_DETECTOR_AHO', 49, 7891,),
    ('WEIGHT_DETECTOR_AHO', 50, 7892,),
    ('WEIGHT_USER', 5, 7893,),
    ('WEIGHT_USER', 7, 7894,),
    ('WEIGHT_USER', 9, 7895,),
    ('WEIGHT_USER', 11, 7896,),
    ('WEIGHT_USER', 13, 7897,),
    ('WEIGHT_USER', 16, 7898,),
    ('WEIGHT_USER', 19, 7899,),
    ('WEIGHT_USER', 21, 7900,),
    ('WEIGHT_USER', 24, 7901,),
    ('WEIGHT_USER', 26, 7902,),
    ('WEIGHT_USER', 29, 7903,),
    ('WEIGHT_USER', 31, 7904,),
    ('WEIGHT_USER', 34, 7905,),
    ('WEIGHT_USER', 36, 7906,),
    ('WEIGHT_USER', 39, 7907,),
    ('WEIGHT_USER', 41, 7908,),
    ('WEIGHT_USER', 44, 7909,),
    ('WEIGHT_USER', 46, 7910,),
    ('WEIGHT_USER', 48, 7911,),
    ('WEIGHT_USER', 50, 7912,),
    ('SEMANTIC_TOP_K', 1, 7913,),
    ('SEMANTIC_TOP_K', 2, 7914,),
    ('SEMANTIC_TOP_K', 3, 7915,),
    ('SEMANTIC_TOP_K', 5, 7916,),
    ('SEMANTIC_TOP_K', 8, 7917,),
    ('SEMANTIC_TOP_K', 10, 7918,),
    ('SEMANTIC_TOP_K', 12, 7919,),
    ('SEMANTIC_TOP_K', 16, 7920,),
    ('SEMANTIC_TOP_K', 20, 7921,),
    ('SEMANTIC_TOP_K', 25, 7922,),
)

class TestSettingsEndpoint(BaseTest):
    """The settings endpoint accepts valid values."""

    @pytest.mark.parametrize(('key', 'value', 'uid',), _SETTINGS_ENDPOINT_CASES)
    def test_settings_endpoint(self, client: Any, admin_headers: dict[str, str], key: str, value: int, uid: int) -> None:
        """The settings endpoint accepts valid values."""
        payload = {'settings': {key: value}}
        response = client.post('/admin/settings', headers=admin_headers, json=payload)
        assert response.status_code == 200
        assert key in response.json()['updated']
