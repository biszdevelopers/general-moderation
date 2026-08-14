"""Phase 2 admin API tests (generated).

Word CRUD, import/export, app policies, settings, logs and dashboard
stats; see tests/tools/phase2_generator.py."""

# multilingual fixtures use non-ASCII on purpose
from __future__ import annotations

from typing import Any

import pytest

from tests.base_test import BaseTest

_SETTINGS_ENDPOINT_CASES: tuple[tuple[str, int, int], ...] = (
    ('SEMANTIC_TOP_K', 32, 7883,),
    ('SEMANTIC_TOP_K', 40, 7884,),
    ('SEMANTIC_TOP_K', 50, 7885,),
    ('SEMANTIC_TOP_K', 60, 7886,),
    ('SEMANTIC_TOP_K', 70, 7887,),
    ('SEMANTIC_TOP_K', 80, 7888,),
    ('SEMANTIC_TOP_K', 88, 7889,),
    ('SEMANTIC_TOP_K', 92, 7890,),
    ('SEMANTIC_TOP_K', 96, 7891,),
    ('SEMANTIC_TOP_K', 100, 7892,),
    ('CACHE_MAX_SIZE', 1, 7893,),
    ('CACHE_MAX_SIZE', 5, 7894,),
    ('CACHE_MAX_SIZE', 10, 7895,),
    ('CACHE_MAX_SIZE', 50, 7896,),
    ('CACHE_MAX_SIZE', 100, 7897,),
    ('CACHE_MAX_SIZE', 500, 7898,),
    ('CACHE_MAX_SIZE', 1000, 7899,),
    ('CACHE_MAX_SIZE', 2500, 7900,),
    ('CACHE_MAX_SIZE', 5000, 7901,),
    ('CACHE_MAX_SIZE', 10000, 7902,),
    ('CACHE_MAX_SIZE', 20000, 7903,),
    ('CACHE_MAX_SIZE', 30000, 7904,),
    ('CACHE_MAX_SIZE', 40000, 7905,),
    ('CACHE_MAX_SIZE', 50000, 7906,),
    ('CACHE_MAX_SIZE', 60000, 7907,),
    ('CACHE_MAX_SIZE', 70000, 7908,),
    ('CACHE_MAX_SIZE', 80000, 7909,),
    ('CACHE_MAX_SIZE', 90000, 7910,),
    ('CACHE_MAX_SIZE', 95000, 7911,),
    ('CACHE_MAX_SIZE', 100000, 7912,),
    ('RATE_LIMIT_PERIOD', 1, 7913,),
    ('RATE_LIMIT_PERIOD', 5, 7914,),
    ('RATE_LIMIT_PERIOD', 10, 7915,),
    ('RATE_LIMIT_PERIOD', 30, 7916,),
    ('RATE_LIMIT_PERIOD', 60, 7917,),
    ('RATE_LIMIT_PERIOD', 120, 7918,),
    ('RATE_LIMIT_PERIOD', 300, 7919,),
    ('RATE_LIMIT_PERIOD', 600, 7920,),
    ('RATE_LIMIT_PERIOD', 900, 7921,),
    ('RATE_LIMIT_PERIOD', 1800, 7922,),
    ('RATE_LIMIT_PERIOD', 3600, 7923,),
    ('RATE_LIMIT_PERIOD', 7200, 7924,),
    ('RATE_LIMIT_PERIOD', 10800, 7925,),
    ('RATE_LIMIT_PERIOD', 14400, 7926,),
    ('RATE_LIMIT_PERIOD', 21600, 7927,),
    ('RATE_LIMIT_PERIOD', 28800, 7928,),
    ('RATE_LIMIT_PERIOD', 43200, 7929,),
    ('RATE_LIMIT_PERIOD', 57600, 7930,),
    ('RATE_LIMIT_PERIOD', 72000, 7931,),
    ('RATE_LIMIT_PERIOD', 86400, 7932,),
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


_LOGS_CASES: tuple[tuple[str, int], ...] = (
    ('..%2F..%2Fetc%2Fpasswd.0', 7933,),
    ('..%2F..%2Fetc%2Fpasswd.1', 7934,),
    ('..%2F..%2Fetc%2Fpasswd.2', 7935,),
    ('..%2F..%2Fetc%2Fpasswd.3', 7936,),
    ('..%2F..%2Fetc%2Fpasswd.4', 7937,),
    ('..%2F..%2Fetc%2Fpasswd.5', 7938,),
    ('..%2F..%2Fetc%2Fpasswd.6', 7939,),
    ('..%2F..%2Fetc%2Fpasswd.7', 7940,),
    ('..%2F..%2Fetc%2Fpasswd.8', 7941,),
    ('..%2F..%2Fetc%2Fpasswd.9', 7942,),
    ('..%2F..%2Fetc%2Fpasswd.10', 7943,),
    ('..%2F..%2Fetc%2Fpasswd.11', 7944,),
    ('..%2F..%2Fetc%2Fpasswd.12', 7945,),
    ('..%2F..%2Fetc%2Fpasswd.13', 7946,),
    ('..%2F..%2Fetc%2Fpasswd.14', 7947,),
    ('..%2F..%2Fetc%2Fpasswd.15', 7948,),
    ('..%2F..%2Fetc%2Fpasswd.16', 7949,),
    ('..%2F..%2Fetc%2Fpasswd.17', 7950,),
    ('..%2F..%2Fetc%2Fpasswd.18', 7951,),
    ('..%2F..%2Fetc%2Fpasswd.19', 7952,),
    ('..%2F..%2Fetc%2Fpasswd.20', 7953,),
    ('..%2F..%2Fetc%2Fpasswd.21', 7954,),
    ('..%2F..%2Fetc%2Fpasswd.22', 7955,),
    ('..%2F..%2Fetc%2Fpasswd.23', 7956,),
    ('..%2F..%2Fetc%2Fpasswd.24', 7957,),
    ('..%2F..%2Fetc%2Fpasswd.25', 7958,),
    ('..%2F..%2Fetc%2Fpasswd.26', 7959,),
    ('..%2F..%2Fetc%2Fpasswd.27', 7960,),
    ('..%2F..%2Fetc%2Fpasswd.28', 7961,),
    ('..%2F..%2Fetc%2Fpasswd.29', 7962,),
    ('..%2F..%2Fetc%2Fpasswd.30', 7963,),
    ('..%2F..%2Fetc%2Fpasswd.31', 7964,),
    ('..%2F..%2Fetc%2Fpasswd.32', 7965,),
    ('..%2F..%2Fetc%2Fpasswd.33', 7966,),
    ('..%2F..%2Fetc%2Fpasswd.34', 7967,),
    ('..%2F..%2Fetc%2Fpasswd.35', 7968,),
    ('..%2F..%2Fetc%2Fpasswd.36', 7969,),
    ('..%2F..%2Fetc%2Fpasswd.37', 7970,),
    ('..%2F..%2Fetc%2Fpasswd.38', 7971,),
    ('..%2F..%2Fetc%2Fpasswd.39', 7972,),
    ('..%2F..%2Fetc%2Fpasswd.40', 7973,),
    ('..%2F..%2Fetc%2Fpasswd.41', 7974,),
    ('..%2F..%2Fetc%2Fpasswd.42', 7975,),
    ('..%2F..%2Fetc%2Fpasswd.43', 7976,),
    ('..%2F..%2Fetc%2Fpasswd.44', 7977,),
    ('..%2F..%2Fetc%2Fpasswd.45', 7978,),
    ('..%2F..%2Fetc%2Fpasswd.46', 7979,),
    ('..%2F..%2Fetc%2Fpasswd.47', 7980,),
    ('..%2F..%2Fetc%2Fpasswd.48', 7981,),
    ('..%2F..%2Fetc%2Fpasswd.49', 7982,),
)

class TestLogs(BaseTest):
    """Log listing and downloads stay consistent."""

    @pytest.mark.parametrize(('target', 'uid',), _LOGS_CASES)
    def test_logs(self, client: Any, admin_headers: dict[str, str], target: str, uid: int) -> None:
        """Log listing and downloads stay consistent."""
        response = client.get('/admin/logs', headers=admin_headers)
        assert response.status_code == 200
        assert isinstance(response.json(), list)
        invalid = client.get(f'/admin/logs/{target}', headers=admin_headers)
        assert invalid.status_code in (400, 404)
        assert 'passwd' not in invalid.text
