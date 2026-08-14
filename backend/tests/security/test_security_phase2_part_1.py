"""Phase 2 security tests (generated).

Header parity, CORS, auth bypass, injection, traversal, method
restrictions and encoded payloads; see tests/tools/phase2_generator.py."""

# multilingual fixtures use non-ASCII on purpose
from __future__ import annotations

from typing import Any

import pytest

from tests.base_test import BaseTest

_HEADER_PRESENT_CASES: tuple[tuple[str, str, str, int, int], ...] = (
    ('x-content-type-options', 'GET', '/health', 0, 8691,),
    ('x-content-type-options', 'GET', '/health', 1, 8692,),
    ('x-content-type-options', 'GET', '/health', 2, 8693,),
    ('x-content-type-options', 'GET', '/health', 3, 8694,),
    ('x-content-type-options', 'POST', '/moderate', 0, 8695,),
    ('x-content-type-options', 'POST', '/moderate', 1, 8696,),
    ('x-content-type-options', 'POST', '/moderate', 2, 8697,),
    ('x-content-type-options', 'POST', '/moderate', 3, 8698,),
    ('x-content-type-options', 'GET', '/metrics', 0, 8699,),
    ('x-content-type-options', 'GET', '/metrics', 1, 8700,),
    ('x-content-type-options', 'GET', '/metrics', 2, 8701,),
    ('x-content-type-options', 'GET', '/metrics', 3, 8702,),
    ('x-content-type-options', 'POST', '/moderate/batch', 0, 8703,),
    ('x-content-type-options', 'POST', '/moderate/batch', 1, 8704,),
    ('x-content-type-options', 'POST', '/moderate/batch', 2, 8705,),
    ('x-content-type-options', 'POST', '/moderate/batch', 3, 8706,),
    ('x-content-type-options', 'GET', '/', 0, 8707,),
    ('x-content-type-options', 'GET', '/', 1, 8708,),
    ('x-content-type-options', 'GET', '/', 2, 8709,),
    ('x-content-type-options', 'GET', '/', 3, 8710,),
    ('x-frame-options', 'GET', '/health', 0, 8711,),
    ('x-frame-options', 'GET', '/health', 1, 8712,),
    ('x-frame-options', 'GET', '/health', 2, 8713,),
    ('x-frame-options', 'GET', '/health', 3, 8714,),
    ('x-frame-options', 'POST', '/moderate', 0, 8715,),
    ('x-frame-options', 'POST', '/moderate', 1, 8716,),
    ('x-frame-options', 'POST', '/moderate', 2, 8717,),
    ('x-frame-options', 'POST', '/moderate', 3, 8718,),
    ('x-frame-options', 'GET', '/metrics', 0, 8719,),
    ('x-frame-options', 'GET', '/metrics', 1, 8720,),
    ('x-frame-options', 'GET', '/metrics', 2, 8721,),
    ('x-frame-options', 'GET', '/metrics', 3, 8722,),
    ('x-frame-options', 'POST', '/moderate/batch', 0, 8723,),
    ('x-frame-options', 'POST', '/moderate/batch', 1, 8724,),
    ('x-frame-options', 'POST', '/moderate/batch', 2, 8725,),
    ('x-frame-options', 'POST', '/moderate/batch', 3, 8726,),
    ('x-frame-options', 'GET', '/', 0, 8727,),
    ('x-frame-options', 'GET', '/', 1, 8728,),
    ('x-frame-options', 'GET', '/', 2, 8729,),
    ('x-frame-options', 'GET', '/', 3, 8730,),
    ('content-security-policy', 'GET', '/health', 0, 8731,),
    ('content-security-policy', 'GET', '/health', 1, 8732,),
    ('content-security-policy', 'GET', '/health', 2, 8733,),
    ('content-security-policy', 'GET', '/health', 3, 8734,),
    ('content-security-policy', 'POST', '/moderate', 0, 8735,),
    ('content-security-policy', 'POST', '/moderate', 1, 8736,),
    ('content-security-policy', 'POST', '/moderate', 2, 8737,),
    ('content-security-policy', 'POST', '/moderate', 3, 8738,),
    ('content-security-policy', 'GET', '/metrics', 0, 8739,),
    ('content-security-policy', 'GET', '/metrics', 1, 8740,),
    ('content-security-policy', 'GET', '/metrics', 2, 8741,),
    ('content-security-policy', 'GET', '/metrics', 3, 8742,),
    ('content-security-policy', 'POST', '/moderate/batch', 0, 8743,),
    ('content-security-policy', 'POST', '/moderate/batch', 1, 8744,),
    ('content-security-policy', 'POST', '/moderate/batch', 2, 8745,),
    ('content-security-policy', 'POST', '/moderate/batch', 3, 8746,),
    ('content-security-policy', 'GET', '/', 0, 8747,),
    ('content-security-policy', 'GET', '/', 1, 8748,),
    ('content-security-policy', 'GET', '/', 2, 8749,),
    ('content-security-policy', 'GET', '/', 3, 8750,),
    ('strict-transport-security', 'GET', '/health', 0, 8751,),
    ('strict-transport-security', 'GET', '/health', 1, 8752,),
    ('strict-transport-security', 'GET', '/health', 2, 8753,),
    ('strict-transport-security', 'GET', '/health', 3, 8754,),
    ('strict-transport-security', 'POST', '/moderate', 0, 8755,),
    ('strict-transport-security', 'POST', '/moderate', 1, 8756,),
    ('strict-transport-security', 'POST', '/moderate', 2, 8757,),
    ('strict-transport-security', 'POST', '/moderate', 3, 8758,),
    ('strict-transport-security', 'GET', '/metrics', 0, 8759,),
    ('strict-transport-security', 'GET', '/metrics', 1, 8760,),
    ('strict-transport-security', 'GET', '/metrics', 2, 8761,),
    ('strict-transport-security', 'GET', '/metrics', 3, 8762,),
    ('strict-transport-security', 'POST', '/moderate/batch', 0, 8763,),
    ('strict-transport-security', 'POST', '/moderate/batch', 1, 8764,),
    ('strict-transport-security', 'POST', '/moderate/batch', 2, 8765,),
    ('strict-transport-security', 'POST', '/moderate/batch', 3, 8766,),
    ('strict-transport-security', 'GET', '/', 0, 8767,),
    ('strict-transport-security', 'GET', '/', 1, 8768,),
    ('strict-transport-security', 'GET', '/', 2, 8769,),
    ('strict-transport-security', 'GET', '/', 3, 8770,),
    ('x-xss-protection', 'GET', '/health', 0, 8771,),
    ('x-xss-protection', 'GET', '/health', 1, 8772,),
    ('x-xss-protection', 'GET', '/health', 2, 8773,),
    ('x-xss-protection', 'GET', '/health', 3, 8774,),
    ('x-xss-protection', 'POST', '/moderate', 0, 8775,),
    ('x-xss-protection', 'POST', '/moderate', 1, 8776,),
    ('x-xss-protection', 'POST', '/moderate', 2, 8777,),
    ('x-xss-protection', 'POST', '/moderate', 3, 8778,),
    ('x-xss-protection', 'GET', '/metrics', 0, 8779,),
    ('x-xss-protection', 'GET', '/metrics', 1, 8780,),
    ('x-xss-protection', 'GET', '/metrics', 2, 8781,),
    ('x-xss-protection', 'GET', '/metrics', 3, 8782,),
    ('x-xss-protection', 'POST', '/moderate/batch', 0, 8783,),
    ('x-xss-protection', 'POST', '/moderate/batch', 1, 8784,),
    ('x-xss-protection', 'POST', '/moderate/batch', 2, 8785,),
    ('x-xss-protection', 'POST', '/moderate/batch', 3, 8786,),
    ('x-xss-protection', 'GET', '/', 0, 8787,),
    ('x-xss-protection', 'GET', '/', 1, 8788,),
    ('x-xss-protection', 'GET', '/', 2, 8789,),
    ('x-xss-protection', 'GET', '/', 3, 8790,),
)

class TestHeaderPresent(BaseTest):
    """Every security header appears on every endpoint."""

    @pytest.mark.parametrize(('header', 'method', 'endpoint', 'variant', 'uid',), _HEADER_PRESENT_CASES)
    def test_header_present(self, client: Any, header: str, method: str, endpoint: str, variant: int, uid: int) -> None:
        """Every security header appears on every endpoint."""
        payload = {'text': f'hi {variant}', 'app_name': 'a'} if endpoint == '/moderate' else None
        if method == 'POST' and payload is not None:
            response = client.post(endpoint, json=payload)
        else:
            response = client.request(method, endpoint)
        assert header in response.headers
