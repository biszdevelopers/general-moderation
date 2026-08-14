"""Phase 2 security tests (generated).

Header parity, CORS, auth bypass, injection, traversal, method
restrictions and encoded payloads; see tests/tools/phase2_generator.py."""

# multilingual fixtures use non-ASCII on purpose
from __future__ import annotations

from typing import Any

import pytest

from tests.base_test import BaseTest

_AUTH_REJECTED_CASES: tuple[tuple[str, str, int], ...] = (
    ('', '/admin/wordbank/stats', 8931,),
    ('', '/admin/wordbank/words', 8932,),
    ('', '/admin/wordbank/export', 8933,),
    ('', '/admin/wordbank/languages', 8934,),
    ('', '/admin/wordbank/categories', 8935,),
    ('', '/admin/app-config', 8936,),
    ('', '/admin/settings', 8937,),
    ('', '/admin/logs', 8938,),
    ('', '/admin/health', 8939,),
    ('', '/admin/spot-check', 8940,),
    (' ', '/admin/wordbank/stats', 8941,),
    (' ', '/admin/wordbank/words', 8942,),
    (' ', '/admin/wordbank/export', 8943,),
    (' ', '/admin/wordbank/languages', 8944,),
    (' ', '/admin/wordbank/categories', 8945,),
    (' ', '/admin/app-config', 8946,),
    (' ', '/admin/settings', 8947,),
    (' ', '/admin/logs', 8948,),
    (' ', '/admin/health', 8949,),
    (' ', '/admin/spot-check', 8950,),
    ('null', '/admin/wordbank/stats', 8951,),
    ('null', '/admin/wordbank/words', 8952,),
    ('null', '/admin/wordbank/export', 8953,),
    ('null', '/admin/wordbank/languages', 8954,),
    ('null', '/admin/wordbank/categories', 8955,),
    ('null', '/admin/app-config', 8956,),
    ('null', '/admin/settings', 8957,),
    ('null', '/admin/logs', 8958,),
    ('null', '/admin/health', 8959,),
    ('null', '/admin/spot-check', 8960,),
    ('None', '/admin/wordbank/stats', 8961,),
    ('None', '/admin/wordbank/words', 8962,),
    ('None', '/admin/wordbank/export', 8963,),
    ('None', '/admin/wordbank/languages', 8964,),
    ('None', '/admin/wordbank/categories', 8965,),
    ('None', '/admin/app-config', 8966,),
    ('None', '/admin/settings', 8967,),
    ('None', '/admin/logs', 8968,),
    ('None', '/admin/health', 8969,),
    ('None', '/admin/spot-check', 8970,),
    ('CHANGE_ME', '/admin/wordbank/stats', 8971,),
    ('CHANGE_ME', '/admin/wordbank/words', 8972,),
    ('CHANGE_ME', '/admin/wordbank/export', 8973,),
    ('CHANGE_ME', '/admin/wordbank/languages', 8974,),
    ('CHANGE_ME', '/admin/wordbank/categories', 8975,),
    ('CHANGE_ME', '/admin/app-config', 8976,),
    ('CHANGE_ME', '/admin/settings', 8977,),
    ('CHANGE_ME', '/admin/logs', 8978,),
    ('CHANGE_ME', '/admin/health', 8979,),
    ('CHANGE_ME', '/admin/spot-check', 8980,),
    ('wrong-key', '/admin/wordbank/stats', 8981,),
    ('wrong-key', '/admin/wordbank/words', 8982,),
    ('wrong-key', '/admin/wordbank/export', 8983,),
    ('wrong-key', '/admin/wordbank/languages', 8984,),
    ('wrong-key', '/admin/wordbank/categories', 8985,),
    ('wrong-key', '/admin/app-config', 8986,),
    ('wrong-key', '/admin/settings', 8987,),
    ('wrong-key', '/admin/logs', 8988,),
    ('wrong-key', '/admin/health', 8989,),
    ('wrong-key', '/admin/spot-check', 8990,),
    ('test-admin-key ', '/admin/wordbank/stats', 8991,),
    ('test-admin-key ', '/admin/wordbank/words', 8992,),
    ('test-admin-key ', '/admin/wordbank/export', 8993,),
    ('test-admin-key ', '/admin/wordbank/languages', 8994,),
    ('test-admin-key ', '/admin/wordbank/categories', 8995,),
    ('test-admin-key ', '/admin/app-config', 8996,),
    ('test-admin-key ', '/admin/settings', 8997,),
    ('test-admin-key ', '/admin/logs', 8998,),
    ('test-admin-key ', '/admin/health', 8999,),
    ('test-admin-key ', '/admin/spot-check', 9000,),
    ('TEST-ADMIN-KEY', '/admin/wordbank/stats', 9001,),
    ('TEST-ADMIN-KEY', '/admin/wordbank/words', 9002,),
    ('TEST-ADMIN-KEY', '/admin/wordbank/export', 9003,),
    ('TEST-ADMIN-KEY', '/admin/wordbank/languages', 9004,),
    ('TEST-ADMIN-KEY', '/admin/wordbank/categories', 9005,),
    ('TEST-ADMIN-KEY', '/admin/app-config', 9006,),
    ('TEST-ADMIN-KEY', '/admin/settings', 9007,),
    ('TEST-ADMIN-KEY', '/admin/logs', 9008,),
    ('TEST-ADMIN-KEY', '/admin/health', 9009,),
    ('TEST-ADMIN-KEY', '/admin/spot-check', 9010,),
    ('bearer-token', '/admin/wordbank/stats', 9011,),
    ('bearer-token', '/admin/wordbank/words', 9012,),
    ('bearer-token', '/admin/wordbank/export', 9013,),
    ('bearer-token', '/admin/wordbank/languages', 9014,),
    ('bearer-token', '/admin/wordbank/categories', 9015,),
    ('bearer-token', '/admin/app-config', 9016,),
    ('bearer-token', '/admin/settings', 9017,),
    ('bearer-token', '/admin/logs', 9018,),
    ('bearer-token', '/admin/health', 9019,),
    ('bearer-token', '/admin/spot-check', 9020,),
    ('leaked-secret', '/admin/wordbank/stats', 9021,),
    ('leaked-secret', '/admin/wordbank/words', 9022,),
    ('leaked-secret', '/admin/wordbank/export', 9023,),
    ('leaked-secret', '/admin/wordbank/languages', 9024,),
    ('leaked-secret', '/admin/wordbank/categories', 9025,),
    ('leaked-secret', '/admin/app-config', 9026,),
    ('leaked-secret', '/admin/settings', 9027,),
    ('leaked-secret', '/admin/logs', 9028,),
    ('leaked-secret', '/admin/health', 9029,),
    ('leaked-secret', '/admin/spot-check', 9030,),
)

class TestAuthRejected(BaseTest):
    """Invalid credentials are rejected on admin endpoints."""

    @pytest.mark.parametrize(('key', 'endpoint', 'uid',), _AUTH_REJECTED_CASES)
    def test_auth_rejected(self, client: Any, key: str, endpoint: str, uid: int) -> None:
        """Invalid credentials are rejected on admin endpoints."""
        response = client.get(endpoint, headers={'X-API-Key': key})
        assert response.status_code == 401
        bearer = client.get(endpoint, headers={'Authorization': f'Bearer {key}'})
        assert bearer.status_code == 401
