"""Phase 2 security tests (generated).

Header parity, CORS, auth bypass, injection, traversal, method
restrictions and encoded payloads; see tests/tools/phase2_generator.py."""

# multilingual fixtures use non-ASCII on purpose
from __future__ import annotations

from typing import Any

import pytest

from tests.base_test import BaseTest

_METHOD_RESTRICTION_CASES: tuple[tuple[str, str, int, int], ...] = (
    ('POST', '/moderate', 200, 9301,),
    ('GET', '/moderate', 405, 9302,),
    ('PUT', '/moderate', 405, 9303,),
    ('DELETE', '/moderate', 405, 9304,),
    ('PATCH', '/moderate', 405, 9305,),
    ('POST', '/moderate/batch', 200, 9306,),
    ('GET', '/moderate/batch', 405, 9307,),
    ('PUT', '/moderate/batch', 405, 9308,),
    ('DELETE', '/moderate/batch', 405, 9309,),
    ('PATCH', '/moderate/batch', 405, 9310,),
    ('GET', '/health', 200, 9311,),
    ('POST', '/health', 405, 9312,),
    ('PUT', '/health', 405, 9313,),
    ('DELETE', '/health', 405, 9314,),
    ('PATCH', '/health', 405, 9315,),
    ('GET', '/metrics', 200, 9316,),
    ('POST', '/metrics', 405, 9317,),
    ('PUT', '/metrics', 405, 9318,),
    ('DELETE', '/metrics', 405, 9319,),
    ('PATCH', '/metrics', 405, 9320,),
    ('GET', '/', 200, 9321,),
    ('POST', '/', 405, 9322,),
    ('PUT', '/', 405, 9323,),
    ('DELETE', '/', 405, 9324,),
    ('PATCH', '/', 405, 9325,),
    ('GET', '/admin/wordbank/stats', 200, 9326,),
    ('POST', '/admin/wordbank/stats', 405, 9327,),
    ('PUT', '/admin/wordbank/stats', 405, 9328,),
    ('DELETE', '/admin/wordbank/stats', 405, 9329,),
    ('PATCH', '/admin/wordbank/stats', 405, 9330,),
    ('GET', '/admin/wordbank/words', 200, 9331,),
    ('POST', '/admin/wordbank/words', 422, 9332,),
    ('PUT', '/admin/wordbank/words', 405, 9333,),
    ('DELETE', '/admin/wordbank/words', 422, 9334,),
    ('PATCH', '/admin/wordbank/words', 405, 9335,),
    ('GET', '/admin/wordbank/export', 200, 9336,),
    ('POST', '/admin/wordbank/export', 405, 9337,),
    ('PUT', '/admin/wordbank/export', 405, 9338,),
    ('DELETE', '/admin/wordbank/export', 405, 9339,),
    ('PATCH', '/admin/wordbank/export', 405, 9340,),
    ('GET', '/admin/wordbank/languages', 200, 9341,),
    ('POST', '/admin/wordbank/languages', 405, 9342,),
    ('PUT', '/admin/wordbank/languages', 405, 9343,),
    ('DELETE', '/admin/wordbank/languages', 405, 9344,),
    ('PATCH', '/admin/wordbank/languages', 405, 9345,),
    ('GET', '/admin/wordbank/categories', 200, 9346,),
    ('POST', '/admin/wordbank/categories', 405, 9347,),
    ('PUT', '/admin/wordbank/categories', 405, 9348,),
    ('DELETE', '/admin/wordbank/categories', 405, 9349,),
    ('PATCH', '/admin/wordbank/categories', 405, 9350,),
    ('POST', '/admin/wordbank/import', 200, 9351,),
    ('GET', '/admin/wordbank/import', 405, 9352,),
    ('PUT', '/admin/wordbank/import', 405, 9353,),
    ('DELETE', '/admin/wordbank/import', 405, 9354,),
    ('PATCH', '/admin/wordbank/import', 405, 9355,),
    ('POST', '/admin/reload', 200, 9356,),
    ('GET', '/admin/reload', 405, 9357,),
    ('PUT', '/admin/reload', 405, 9358,),
    ('DELETE', '/admin/reload', 405, 9359,),
    ('PATCH', '/admin/reload', 405, 9360,),
    ('GET', '/admin/app-config', 200, 9361,),
    ('POST', '/admin/app-config', 200, 9362,),
    ('PUT', '/admin/app-config', 405, 9363,),
    ('DELETE', '/admin/app-config', 405, 9364,),
    ('PATCH', '/admin/app-config', 405, 9365,),
    ('GET', '/admin/app-config/demo', 200, 9366,),
    ('POST', '/admin/app-config/demo', 405, 9367,),
    ('PUT', '/admin/app-config/demo', 405, 9368,),
    ('DELETE', '/admin/app-config/demo', 405, 9369,),
    ('PATCH', '/admin/app-config/demo', 405, 9370,),
    ('GET', '/admin/app-config/other', 200, 9371,),
    ('POST', '/admin/app-config/other', 405, 9372,),
    ('PUT', '/admin/app-config/other', 405, 9373,),
    ('DELETE', '/admin/app-config/other', 405, 9374,),
    ('PATCH', '/admin/app-config/other', 405, 9375,),
    ('GET', '/admin/settings', 200, 9376,),
    ('POST', '/admin/settings', 200, 9377,),
    ('PUT', '/admin/settings', 405, 9378,),
    ('DELETE', '/admin/settings', 405, 9379,),
    ('PATCH', '/admin/settings', 405, 9380,),
    ('GET', '/admin/logs', 200, 9381,),
    ('POST', '/admin/logs', 405, 9382,),
    ('PUT', '/admin/logs', 405, 9383,),
    ('DELETE', '/admin/logs', 405, 9384,),
    ('PATCH', '/admin/logs', 405, 9385,),
    ('GET', '/admin/stats', 200, 9386,),
    ('POST', '/admin/stats', 405, 9387,),
    ('PUT', '/admin/stats', 405, 9388,),
    ('DELETE', '/admin/stats', 405, 9389,),
    ('PATCH', '/admin/stats', 405, 9390,),
    ('GET', '/admin/health', 200, 9391,),
    ('POST', '/admin/health', 405, 9392,),
    ('PUT', '/admin/health', 405, 9393,),
    ('DELETE', '/admin/health', 405, 9394,),
    ('PATCH', '/admin/health', 405, 9395,),
    ('GET', '/admin/spot-check', 200, 9396,),
    ('POST', '/admin/spot-check', 405, 9397,),
    ('PUT', '/admin/spot-check', 405, 9398,),
    ('DELETE', '/admin/spot-check', 405, 9399,),
    ('PATCH', '/admin/spot-check', 405, 9400,),
)

class TestMethodRestriction(BaseTest):
    """Disallowed methods are rejected without error."""

    @pytest.mark.parametrize(('method', 'endpoint', 'expected_status', 'uid',), _METHOD_RESTRICTION_CASES)
    def test_method_restriction(self, client: Any, admin_headers: dict[str, str], method: str, endpoint: str, expected_status: int, uid: int) -> None:
        """Disallowed methods are rejected without error."""
        body = None
        if method == 'POST' and 'moderate' in endpoint:
            body = {'text': 'hi'} if endpoint == '/moderate' else {'items': [{'text': 'hi'}]}
        elif method == 'POST' and endpoint == '/admin/wordbank/import':
            body = {'items': [{'word': 'probe'}]}
        elif method == 'POST' and endpoint == '/admin/app-config':
            body = {'app_name': 'x', 'score_threshold': 50}
        elif method == 'POST' and endpoint == '/admin/settings':
            body = {'settings': {'WEIGHT_USER': 25}}
        headers = admin_headers if endpoint.startswith('/admin') else None
        response = client.request(method, endpoint, json=body, headers=headers)
        assert response.status_code == expected_status
