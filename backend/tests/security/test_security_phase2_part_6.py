"""Phase 2 security tests (generated).

Header parity, CORS, auth bypass, injection, traversal, method
restrictions and encoded payloads; see tests/tools/phase2_generator.py."""

# multilingual fixtures use non-ASCII on purpose
from __future__ import annotations

from typing import Any

import pytest

from tests.base_test import BaseTest

_METHOD_RESTRICTION_CASES: tuple[tuple[str, str, int, int], ...] = (
    ('POST', '/moderate', 200, 9261,),
    ('GET', '/moderate', 405, 9262,),
    ('PUT', '/moderate', 405, 9263,),
    ('DELETE', '/moderate', 405, 9264,),
    ('PATCH', '/moderate', 405, 9265,),
    ('POST', '/moderate/batch', 200, 9266,),
    ('GET', '/moderate/batch', 405, 9267,),
    ('PUT', '/moderate/batch', 405, 9268,),
    ('DELETE', '/moderate/batch', 405, 9269,),
    ('PATCH', '/moderate/batch', 405, 9270,),
    ('GET', '/health', 200, 9271,),
    ('POST', '/health', 405, 9272,),
    ('PUT', '/health', 405, 9273,),
    ('DELETE', '/health', 405, 9274,),
    ('PATCH', '/health', 405, 9275,),
    ('GET', '/metrics', 200, 9276,),
    ('POST', '/metrics', 405, 9277,),
    ('PUT', '/metrics', 405, 9278,),
    ('DELETE', '/metrics', 405, 9279,),
    ('PATCH', '/metrics', 405, 9280,),
    ('GET', '/', 200, 9281,),
    ('POST', '/', 405, 9282,),
    ('PUT', '/', 405, 9283,),
    ('DELETE', '/', 405, 9284,),
    ('PATCH', '/', 405, 9285,),
    ('GET', '/admin/wordbank/stats', 200, 9286,),
    ('POST', '/admin/wordbank/stats', 405, 9287,),
    ('PUT', '/admin/wordbank/stats', 405, 9288,),
    ('DELETE', '/admin/wordbank/stats', 405, 9289,),
    ('PATCH', '/admin/wordbank/stats', 405, 9290,),
    ('GET', '/admin/wordbank/words', 200, 9291,),
    ('POST', '/admin/wordbank/words', 422, 9292,),
    ('PUT', '/admin/wordbank/words', 405, 9293,),
    ('DELETE', '/admin/wordbank/words', 422, 9294,),
    ('PATCH', '/admin/wordbank/words', 405, 9295,),
    ('GET', '/admin/wordbank/export', 200, 9296,),
    ('POST', '/admin/wordbank/export', 405, 9297,),
    ('PUT', '/admin/wordbank/export', 405, 9298,),
    ('DELETE', '/admin/wordbank/export', 405, 9299,),
    ('PATCH', '/admin/wordbank/export', 405, 9300,),
    ('GET', '/admin/wordbank/languages', 200, 9301,),
    ('POST', '/admin/wordbank/languages', 405, 9302,),
    ('PUT', '/admin/wordbank/languages', 405, 9303,),
    ('DELETE', '/admin/wordbank/languages', 405, 9304,),
    ('PATCH', '/admin/wordbank/languages', 405, 9305,),
    ('GET', '/admin/wordbank/categories', 200, 9306,),
    ('POST', '/admin/wordbank/categories', 405, 9307,),
    ('PUT', '/admin/wordbank/categories', 405, 9308,),
    ('DELETE', '/admin/wordbank/categories', 405, 9309,),
    ('PATCH', '/admin/wordbank/categories', 405, 9310,),
    ('POST', '/admin/wordbank/import', 200, 9311,),
    ('GET', '/admin/wordbank/import', 405, 9312,),
    ('PUT', '/admin/wordbank/import', 405, 9313,),
    ('DELETE', '/admin/wordbank/import', 405, 9314,),
    ('PATCH', '/admin/wordbank/import', 405, 9315,),
    ('POST', '/admin/reload', 200, 9316,),
    ('GET', '/admin/reload', 405, 9317,),
    ('PUT', '/admin/reload', 405, 9318,),
    ('DELETE', '/admin/reload', 405, 9319,),
    ('PATCH', '/admin/reload', 405, 9320,),
    ('GET', '/admin/app-config', 200, 9321,),
    ('POST', '/admin/app-config', 200, 9322,),
    ('PUT', '/admin/app-config', 405, 9323,),
    ('DELETE', '/admin/app-config', 405, 9324,),
    ('PATCH', '/admin/app-config', 405, 9325,),
    ('GET', '/admin/app-config/demo', 200, 9326,),
    ('POST', '/admin/app-config/demo', 405, 9327,),
    ('PUT', '/admin/app-config/demo', 405, 9328,),
    ('DELETE', '/admin/app-config/demo', 405, 9329,),
    ('PATCH', '/admin/app-config/demo', 405, 9330,),
    ('GET', '/admin/app-config/other', 200, 9331,),
    ('POST', '/admin/app-config/other', 405, 9332,),
    ('PUT', '/admin/app-config/other', 405, 9333,),
    ('DELETE', '/admin/app-config/other', 405, 9334,),
    ('PATCH', '/admin/app-config/other', 405, 9335,),
    ('GET', '/admin/settings', 200, 9336,),
    ('POST', '/admin/settings', 200, 9337,),
    ('PUT', '/admin/settings', 405, 9338,),
    ('DELETE', '/admin/settings', 405, 9339,),
    ('PATCH', '/admin/settings', 405, 9340,),
    ('GET', '/admin/logs', 200, 9341,),
    ('POST', '/admin/logs', 405, 9342,),
    ('PUT', '/admin/logs', 405, 9343,),
    ('DELETE', '/admin/logs', 405, 9344,),
    ('PATCH', '/admin/logs', 405, 9345,),
    ('GET', '/admin/stats', 200, 9346,),
    ('POST', '/admin/stats', 405, 9347,),
    ('PUT', '/admin/stats', 405, 9348,),
    ('DELETE', '/admin/stats', 405, 9349,),
    ('PATCH', '/admin/stats', 405, 9350,),
    ('GET', '/admin/health', 200, 9351,),
    ('POST', '/admin/health', 405, 9352,),
    ('PUT', '/admin/health', 405, 9353,),
    ('DELETE', '/admin/health', 405, 9354,),
    ('PATCH', '/admin/health', 405, 9355,),
    ('GET', '/admin/spot-check', 200, 9356,),
    ('POST', '/admin/spot-check', 405, 9357,),
    ('PUT', '/admin/spot-check', 405, 9358,),
    ('DELETE', '/admin/spot-check', 405, 9359,),
    ('PATCH', '/admin/spot-check', 405, 9360,),
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
