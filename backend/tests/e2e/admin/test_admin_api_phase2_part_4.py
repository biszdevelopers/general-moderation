"""Phase 2 admin API tests (generated).

Word CRUD, import/export, app policies, settings, logs and dashboard
stats; see tests/tools/phase2_generator.py."""

# multilingual fixtures use non-ASCII on purpose
from __future__ import annotations

from typing import Any

import pytest

from tests.base_test import BaseTest

_APP_CONFIG_CASES: tuple[tuple[str, int, str, bool, bool, int], ...] = (
    ('cfgapp', 60, 'or', False, True, 7783,),
    ('cfgapp', 60, 'or', False, False, 7784,),
    ('cfgapp', 60, 'and', True, True, 7785,),
    ('cfgapp', 60, 'and', True, False, 7786,),
    ('cfgapp', 60, 'and', False, True, 7787,),
    ('cfgapp', 60, 'and', False, False, 7788,),
    ('cfgapp', 70, 'or', True, True, 7789,),
    ('cfgapp', 70, 'or', True, False, 7790,),
    ('cfgapp', 70, 'or', False, True, 7791,),
    ('cfgapp', 70, 'or', False, False, 7792,),
    ('cfgapp', 70, 'and', True, True, 7793,),
    ('cfgapp', 70, 'and', True, False, 7794,),
    ('cfgapp', 70, 'and', False, True, 7795,),
    ('cfgapp', 70, 'and', False, False, 7796,),
    ('cfgapp', 80, 'or', True, True, 7797,),
    ('cfgapp', 80, 'or', True, False, 7798,),
    ('cfgapp', 80, 'or', False, True, 7799,),
    ('cfgapp', 80, 'or', False, False, 7800,),
    ('cfgapp', 80, 'and', True, True, 7801,),
    ('cfgapp', 80, 'and', True, False, 7802,),
    ('cfgapp', 80, 'and', False, True, 7803,),
    ('cfgapp', 80, 'and', False, False, 7804,),
    ('cfgapp', 90, 'or', True, True, 7805,),
    ('cfgapp', 90, 'or', True, False, 7806,),
    ('cfgapp', 90, 'or', False, True, 7807,),
    ('cfgapp', 90, 'or', False, False, 7808,),
    ('cfgapp', 90, 'and', True, True, 7809,),
    ('cfgapp', 90, 'and', True, False, 7810,),
    ('cfgapp', 90, 'and', False, True, 7811,),
    ('cfgapp', 90, 'and', False, False, 7812,),
    ('cfgapp', 100, 'or', True, True, 7813,),
    ('cfgapp', 100, 'or', True, False, 7814,),
    ('cfgapp', 100, 'or', False, True, 7815,),
    ('cfgapp', 100, 'or', False, False, 7816,),
    ('cfgapp', 100, 'and', True, True, 7817,),
    ('cfgapp', 100, 'and', True, False, 7818,),
    ('cfgapp', 100, 'and', False, True, 7819,),
    ('cfgapp', 100, 'and', False, False, 7820,),
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
    (-1, 7821,),
    (101, 7822,),
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
    ('ghost0', 7823,),
    ('ghost1', 7824,),
    ('ghost2', 7825,),
    ('ghost3', 7826,),
    ('ghost4', 7827,),
    ('ghost5', 7828,),
    ('ghost6', 7829,),
    ('ghost7', 7830,),
    ('ghost8', 7831,),
    ('ghost9', 7832,),
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
    ('WEIGHT_DETECTOR_AHO', 5, 7833,),
    ('WEIGHT_DETECTOR_AHO', 8, 7834,),
    ('WEIGHT_DETECTOR_AHO', 10, 7835,),
    ('WEIGHT_DETECTOR_AHO', 12, 7836,),
    ('WEIGHT_DETECTOR_AHO', 15, 7837,),
    ('WEIGHT_DETECTOR_AHO', 18, 7838,),
    ('WEIGHT_DETECTOR_AHO', 20, 7839,),
    ('WEIGHT_DETECTOR_AHO', 22, 7840,),
    ('WEIGHT_DETECTOR_AHO', 25, 7841,),
    ('WEIGHT_DETECTOR_AHO', 28, 7842,),
    ('WEIGHT_DETECTOR_AHO', 30, 7843,),
    ('WEIGHT_DETECTOR_AHO', 32, 7844,),
    ('WEIGHT_DETECTOR_AHO', 35, 7845,),
    ('WEIGHT_DETECTOR_AHO', 38, 7846,),
    ('WEIGHT_DETECTOR_AHO', 40, 7847,),
    ('WEIGHT_DETECTOR_AHO', 42, 7848,),
    ('WEIGHT_DETECTOR_AHO', 45, 7849,),
    ('WEIGHT_DETECTOR_AHO', 47, 7850,),
    ('WEIGHT_DETECTOR_AHO', 49, 7851,),
    ('WEIGHT_DETECTOR_AHO', 50, 7852,),
    ('WEIGHT_USER', 5, 7853,),
    ('WEIGHT_USER', 7, 7854,),
    ('WEIGHT_USER', 9, 7855,),
    ('WEIGHT_USER', 11, 7856,),
    ('WEIGHT_USER', 13, 7857,),
    ('WEIGHT_USER', 16, 7858,),
    ('WEIGHT_USER', 19, 7859,),
    ('WEIGHT_USER', 21, 7860,),
    ('WEIGHT_USER', 24, 7861,),
    ('WEIGHT_USER', 26, 7862,),
    ('WEIGHT_USER', 29, 7863,),
    ('WEIGHT_USER', 31, 7864,),
    ('WEIGHT_USER', 34, 7865,),
    ('WEIGHT_USER', 36, 7866,),
    ('WEIGHT_USER', 39, 7867,),
    ('WEIGHT_USER', 41, 7868,),
    ('WEIGHT_USER', 44, 7869,),
    ('WEIGHT_USER', 46, 7870,),
    ('WEIGHT_USER', 48, 7871,),
    ('WEIGHT_USER', 50, 7872,),
    ('SEMANTIC_TOP_K', 1, 7873,),
    ('SEMANTIC_TOP_K', 2, 7874,),
    ('SEMANTIC_TOP_K', 3, 7875,),
    ('SEMANTIC_TOP_K', 5, 7876,),
    ('SEMANTIC_TOP_K', 8, 7877,),
    ('SEMANTIC_TOP_K', 10, 7878,),
    ('SEMANTIC_TOP_K', 12, 7879,),
    ('SEMANTIC_TOP_K', 16, 7880,),
    ('SEMANTIC_TOP_K', 20, 7881,),
    ('SEMANTIC_TOP_K', 25, 7882,),
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
