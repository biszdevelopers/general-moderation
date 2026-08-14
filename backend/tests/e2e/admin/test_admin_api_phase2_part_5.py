"""Phase 2 admin API tests (generated).

Word CRUD, import/export, app policies, settings, logs and dashboard
stats; see tests/tools/phase2_generator.py."""

# multilingual fixtures use non-ASCII on purpose
from __future__ import annotations

from typing import Any

import pytest

from tests.base_test import BaseTest

_SETTINGS_ENDPOINT_CASES: tuple[tuple[str, int, int], ...] = (
    ('SEMANTIC_TOP_K', 32, 7923,),
    ('SEMANTIC_TOP_K', 40, 7924,),
    ('SEMANTIC_TOP_K', 50, 7925,),
    ('SEMANTIC_TOP_K', 60, 7926,),
    ('SEMANTIC_TOP_K', 70, 7927,),
    ('SEMANTIC_TOP_K', 80, 7928,),
    ('SEMANTIC_TOP_K', 88, 7929,),
    ('SEMANTIC_TOP_K', 92, 7930,),
    ('SEMANTIC_TOP_K', 96, 7931,),
    ('SEMANTIC_TOP_K', 100, 7932,),
    ('CACHE_MAX_SIZE', 1, 7933,),
    ('CACHE_MAX_SIZE', 5, 7934,),
    ('CACHE_MAX_SIZE', 10, 7935,),
    ('CACHE_MAX_SIZE', 50, 7936,),
    ('CACHE_MAX_SIZE', 100, 7937,),
    ('CACHE_MAX_SIZE', 500, 7938,),
    ('CACHE_MAX_SIZE', 1000, 7939,),
    ('CACHE_MAX_SIZE', 2500, 7940,),
    ('CACHE_MAX_SIZE', 5000, 7941,),
    ('CACHE_MAX_SIZE', 10000, 7942,),
    ('CACHE_MAX_SIZE', 20000, 7943,),
    ('CACHE_MAX_SIZE', 30000, 7944,),
    ('CACHE_MAX_SIZE', 40000, 7945,),
    ('CACHE_MAX_SIZE', 50000, 7946,),
    ('CACHE_MAX_SIZE', 60000, 7947,),
    ('CACHE_MAX_SIZE', 70000, 7948,),
    ('CACHE_MAX_SIZE', 80000, 7949,),
    ('CACHE_MAX_SIZE', 90000, 7950,),
    ('CACHE_MAX_SIZE', 95000, 7951,),
    ('CACHE_MAX_SIZE', 100000, 7952,),
    ('RATE_LIMIT_PERIOD', 1, 7953,),
    ('RATE_LIMIT_PERIOD', 5, 7954,),
    ('RATE_LIMIT_PERIOD', 10, 7955,),
    ('RATE_LIMIT_PERIOD', 30, 7956,),
    ('RATE_LIMIT_PERIOD', 60, 7957,),
    ('RATE_LIMIT_PERIOD', 120, 7958,),
    ('RATE_LIMIT_PERIOD', 300, 7959,),
    ('RATE_LIMIT_PERIOD', 600, 7960,),
    ('RATE_LIMIT_PERIOD', 900, 7961,),
    ('RATE_LIMIT_PERIOD', 1800, 7962,),
    ('RATE_LIMIT_PERIOD', 3600, 7963,),
    ('RATE_LIMIT_PERIOD', 7200, 7964,),
    ('RATE_LIMIT_PERIOD', 10800, 7965,),
    ('RATE_LIMIT_PERIOD', 14400, 7966,),
    ('RATE_LIMIT_PERIOD', 21600, 7967,),
    ('RATE_LIMIT_PERIOD', 28800, 7968,),
    ('RATE_LIMIT_PERIOD', 43200, 7969,),
    ('RATE_LIMIT_PERIOD', 57600, 7970,),
    ('RATE_LIMIT_PERIOD', 72000, 7971,),
    ('RATE_LIMIT_PERIOD', 86400, 7972,),
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
    ('..%2F..%2Fetc%2Fpasswd.0', 7973,),
    ('..%2F..%2Fetc%2Fpasswd.1', 7974,),
    ('..%2F..%2Fetc%2Fpasswd.2', 7975,),
    ('..%2F..%2Fetc%2Fpasswd.3', 7976,),
    ('..%2F..%2Fetc%2Fpasswd.4', 7977,),
    ('..%2F..%2Fetc%2Fpasswd.5', 7978,),
    ('..%2F..%2Fetc%2Fpasswd.6', 7979,),
    ('..%2F..%2Fetc%2Fpasswd.7', 7980,),
    ('..%2F..%2Fetc%2Fpasswd.8', 7981,),
    ('..%2F..%2Fetc%2Fpasswd.9', 7982,),
    ('..%2F..%2Fetc%2Fpasswd.10', 7983,),
    ('..%2F..%2Fetc%2Fpasswd.11', 7984,),
    ('..%2F..%2Fetc%2Fpasswd.12', 7985,),
    ('..%2F..%2Fetc%2Fpasswd.13', 7986,),
    ('..%2F..%2Fetc%2Fpasswd.14', 7987,),
    ('..%2F..%2Fetc%2Fpasswd.15', 7988,),
    ('..%2F..%2Fetc%2Fpasswd.16', 7989,),
    ('..%2F..%2Fetc%2Fpasswd.17', 7990,),
    ('..%2F..%2Fetc%2Fpasswd.18', 7991,),
    ('..%2F..%2Fetc%2Fpasswd.19', 7992,),
    ('..%2F..%2Fetc%2Fpasswd.20', 7993,),
    ('..%2F..%2Fetc%2Fpasswd.21', 7994,),
    ('..%2F..%2Fetc%2Fpasswd.22', 7995,),
    ('..%2F..%2Fetc%2Fpasswd.23', 7996,),
    ('..%2F..%2Fetc%2Fpasswd.24', 7997,),
    ('..%2F..%2Fetc%2Fpasswd.25', 7998,),
    ('..%2F..%2Fetc%2Fpasswd.26', 7999,),
    ('..%2F..%2Fetc%2Fpasswd.27', 8000,),
    ('..%2F..%2Fetc%2Fpasswd.28', 8001,),
    ('..%2F..%2Fetc%2Fpasswd.29', 8002,),
    ('..%2F..%2Fetc%2Fpasswd.30', 8003,),
    ('..%2F..%2Fetc%2Fpasswd.31', 8004,),
    ('..%2F..%2Fetc%2Fpasswd.32', 8005,),
    ('..%2F..%2Fetc%2Fpasswd.33', 8006,),
    ('..%2F..%2Fetc%2Fpasswd.34', 8007,),
    ('..%2F..%2Fetc%2Fpasswd.35', 8008,),
    ('..%2F..%2Fetc%2Fpasswd.36', 8009,),
    ('..%2F..%2Fetc%2Fpasswd.37', 8010,),
    ('..%2F..%2Fetc%2Fpasswd.38', 8011,),
    ('..%2F..%2Fetc%2Fpasswd.39', 8012,),
    ('..%2F..%2Fetc%2Fpasswd.40', 8013,),
    ('..%2F..%2Fetc%2Fpasswd.41', 8014,),
    ('..%2F..%2Fetc%2Fpasswd.42', 8015,),
    ('..%2F..%2Fetc%2Fpasswd.43', 8016,),
    ('..%2F..%2Fetc%2Fpasswd.44', 8017,),
    ('..%2F..%2Fetc%2Fpasswd.45', 8018,),
    ('..%2F..%2Fetc%2Fpasswd.46', 8019,),
    ('..%2F..%2Fetc%2Fpasswd.47', 8020,),
    ('..%2F..%2Fetc%2Fpasswd.48', 8021,),
    ('..%2F..%2Fetc%2Fpasswd.49', 8022,),
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
