"""Phase 2 security tests (generated).

Header parity, CORS, auth bypass, injection, traversal, method
restrictions and encoded payloads; see tests/tools/phase2_generator.py."""

# multilingual fixtures use non-ASCII on purpose
from __future__ import annotations

from typing import Any

import pytest

from tests.base_test import BaseTest

_AUTH_REJECTED_CASES: tuple[tuple[str, str, int], ...] = (
    ('', '/admin/wordbank/stats', 8971,),
    ('', '/admin/wordbank/words', 8972,),
    ('', '/admin/wordbank/export', 8973,),
    ('', '/admin/wordbank/languages', 8974,),
    ('', '/admin/wordbank/categories', 8975,),
    ('', '/admin/app-config', 8976,),
    ('', '/admin/settings', 8977,),
    ('', '/admin/logs', 8978,),
    ('', '/admin/health', 8979,),
    ('', '/admin/spot-check', 8980,),
    (' ', '/admin/wordbank/stats', 8981,),
    (' ', '/admin/wordbank/words', 8982,),
    (' ', '/admin/wordbank/export', 8983,),
    (' ', '/admin/wordbank/languages', 8984,),
    (' ', '/admin/wordbank/categories', 8985,),
    (' ', '/admin/app-config', 8986,),
    (' ', '/admin/settings', 8987,),
    (' ', '/admin/logs', 8988,),
    (' ', '/admin/health', 8989,),
    (' ', '/admin/spot-check', 8990,),
    ('null', '/admin/wordbank/stats', 8991,),
    ('null', '/admin/wordbank/words', 8992,),
    ('null', '/admin/wordbank/export', 8993,),
    ('null', '/admin/wordbank/languages', 8994,),
    ('null', '/admin/wordbank/categories', 8995,),
    ('null', '/admin/app-config', 8996,),
    ('null', '/admin/settings', 8997,),
    ('null', '/admin/logs', 8998,),
    ('null', '/admin/health', 8999,),
    ('null', '/admin/spot-check', 9000,),
    ('None', '/admin/wordbank/stats', 9001,),
    ('None', '/admin/wordbank/words', 9002,),
    ('None', '/admin/wordbank/export', 9003,),
    ('None', '/admin/wordbank/languages', 9004,),
    ('None', '/admin/wordbank/categories', 9005,),
    ('None', '/admin/app-config', 9006,),
    ('None', '/admin/settings', 9007,),
    ('None', '/admin/logs', 9008,),
    ('None', '/admin/health', 9009,),
    ('None', '/admin/spot-check', 9010,),
    ('CHANGE_ME', '/admin/wordbank/stats', 9011,),
    ('CHANGE_ME', '/admin/wordbank/words', 9012,),
    ('CHANGE_ME', '/admin/wordbank/export', 9013,),
    ('CHANGE_ME', '/admin/wordbank/languages', 9014,),
    ('CHANGE_ME', '/admin/wordbank/categories', 9015,),
    ('CHANGE_ME', '/admin/app-config', 9016,),
    ('CHANGE_ME', '/admin/settings', 9017,),
    ('CHANGE_ME', '/admin/logs', 9018,),
    ('CHANGE_ME', '/admin/health', 9019,),
    ('CHANGE_ME', '/admin/spot-check', 9020,),
    ('wrong-key', '/admin/wordbank/stats', 9021,),
    ('wrong-key', '/admin/wordbank/words', 9022,),
    ('wrong-key', '/admin/wordbank/export', 9023,),
    ('wrong-key', '/admin/wordbank/languages', 9024,),
    ('wrong-key', '/admin/wordbank/categories', 9025,),
    ('wrong-key', '/admin/app-config', 9026,),
    ('wrong-key', '/admin/settings', 9027,),
    ('wrong-key', '/admin/logs', 9028,),
    ('wrong-key', '/admin/health', 9029,),
    ('wrong-key', '/admin/spot-check', 9030,),
    ('test-admin-key ', '/admin/wordbank/stats', 9031,),
    ('test-admin-key ', '/admin/wordbank/words', 9032,),
    ('test-admin-key ', '/admin/wordbank/export', 9033,),
    ('test-admin-key ', '/admin/wordbank/languages', 9034,),
    ('test-admin-key ', '/admin/wordbank/categories', 9035,),
    ('test-admin-key ', '/admin/app-config', 9036,),
    ('test-admin-key ', '/admin/settings', 9037,),
    ('test-admin-key ', '/admin/logs', 9038,),
    ('test-admin-key ', '/admin/health', 9039,),
    ('test-admin-key ', '/admin/spot-check', 9040,),
    ('TEST-ADMIN-KEY', '/admin/wordbank/stats', 9041,),
    ('TEST-ADMIN-KEY', '/admin/wordbank/words', 9042,),
    ('TEST-ADMIN-KEY', '/admin/wordbank/export', 9043,),
    ('TEST-ADMIN-KEY', '/admin/wordbank/languages', 9044,),
    ('TEST-ADMIN-KEY', '/admin/wordbank/categories', 9045,),
    ('TEST-ADMIN-KEY', '/admin/app-config', 9046,),
    ('TEST-ADMIN-KEY', '/admin/settings', 9047,),
    ('TEST-ADMIN-KEY', '/admin/logs', 9048,),
    ('TEST-ADMIN-KEY', '/admin/health', 9049,),
    ('TEST-ADMIN-KEY', '/admin/spot-check', 9050,),
    ('bearer-token', '/admin/wordbank/stats', 9051,),
    ('bearer-token', '/admin/wordbank/words', 9052,),
    ('bearer-token', '/admin/wordbank/export', 9053,),
    ('bearer-token', '/admin/wordbank/languages', 9054,),
    ('bearer-token', '/admin/wordbank/categories', 9055,),
    ('bearer-token', '/admin/app-config', 9056,),
    ('bearer-token', '/admin/settings', 9057,),
    ('bearer-token', '/admin/logs', 9058,),
    ('bearer-token', '/admin/health', 9059,),
    ('bearer-token', '/admin/spot-check', 9060,),
    ('leaked-secret', '/admin/wordbank/stats', 9061,),
    ('leaked-secret', '/admin/wordbank/words', 9062,),
    ('leaked-secret', '/admin/wordbank/export', 9063,),
    ('leaked-secret', '/admin/wordbank/languages', 9064,),
    ('leaked-secret', '/admin/wordbank/categories', 9065,),
    ('leaked-secret', '/admin/app-config', 9066,),
    ('leaked-secret', '/admin/settings', 9067,),
    ('leaked-secret', '/admin/logs', 9068,),
    ('leaked-secret', '/admin/health', 9069,),
    ('leaked-secret', '/admin/spot-check', 9070,),
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
