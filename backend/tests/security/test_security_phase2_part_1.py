"""Phase 2 security tests (generated).

Header parity, CORS, auth bypass, injection, traversal, method
restrictions and encoded payloads; see tests/tools/phase2_generator.py."""

# multilingual fixtures use non-ASCII on purpose
from __future__ import annotations

from typing import Any

import pytest

from tests.base_test import BaseTest

_HEADER_PRESENT_CASES: tuple[tuple[str, str, str, int, int], ...] = (
    ('x-content-type-options', 'GET', '/health', 0, 8731,),
    ('x-content-type-options', 'GET', '/health', 1, 8732,),
    ('x-content-type-options', 'GET', '/health', 2, 8733,),
    ('x-content-type-options', 'GET', '/health', 3, 8734,),
    ('x-content-type-options', 'POST', '/moderate', 0, 8735,),
    ('x-content-type-options', 'POST', '/moderate', 1, 8736,),
    ('x-content-type-options', 'POST', '/moderate', 2, 8737,),
    ('x-content-type-options', 'POST', '/moderate', 3, 8738,),
    ('x-content-type-options', 'GET', '/metrics', 0, 8739,),
    ('x-content-type-options', 'GET', '/metrics', 1, 8740,),
    ('x-content-type-options', 'GET', '/metrics', 2, 8741,),
    ('x-content-type-options', 'GET', '/metrics', 3, 8742,),
    ('x-content-type-options', 'POST', '/moderate/batch', 0, 8743,),
    ('x-content-type-options', 'POST', '/moderate/batch', 1, 8744,),
    ('x-content-type-options', 'POST', '/moderate/batch', 2, 8745,),
    ('x-content-type-options', 'POST', '/moderate/batch', 3, 8746,),
    ('x-content-type-options', 'GET', '/', 0, 8747,),
    ('x-content-type-options', 'GET', '/', 1, 8748,),
    ('x-content-type-options', 'GET', '/', 2, 8749,),
    ('x-content-type-options', 'GET', '/', 3, 8750,),
    ('x-frame-options', 'GET', '/health', 0, 8751,),
    ('x-frame-options', 'GET', '/health', 1, 8752,),
    ('x-frame-options', 'GET', '/health', 2, 8753,),
    ('x-frame-options', 'GET', '/health', 3, 8754,),
    ('x-frame-options', 'POST', '/moderate', 0, 8755,),
    ('x-frame-options', 'POST', '/moderate', 1, 8756,),
    ('x-frame-options', 'POST', '/moderate', 2, 8757,),
    ('x-frame-options', 'POST', '/moderate', 3, 8758,),
    ('x-frame-options', 'GET', '/metrics', 0, 8759,),
    ('x-frame-options', 'GET', '/metrics', 1, 8760,),
    ('x-frame-options', 'GET', '/metrics', 2, 8761,),
    ('x-frame-options', 'GET', '/metrics', 3, 8762,),
    ('x-frame-options', 'POST', '/moderate/batch', 0, 8763,),
    ('x-frame-options', 'POST', '/moderate/batch', 1, 8764,),
    ('x-frame-options', 'POST', '/moderate/batch', 2, 8765,),
    ('x-frame-options', 'POST', '/moderate/batch', 3, 8766,),
    ('x-frame-options', 'GET', '/', 0, 8767,),
    ('x-frame-options', 'GET', '/', 1, 8768,),
    ('x-frame-options', 'GET', '/', 2, 8769,),
    ('x-frame-options', 'GET', '/', 3, 8770,),
    ('content-security-policy', 'GET', '/health', 0, 8771,),
    ('content-security-policy', 'GET', '/health', 1, 8772,),
    ('content-security-policy', 'GET', '/health', 2, 8773,),
    ('content-security-policy', 'GET', '/health', 3, 8774,),
    ('content-security-policy', 'POST', '/moderate', 0, 8775,),
    ('content-security-policy', 'POST', '/moderate', 1, 8776,),
    ('content-security-policy', 'POST', '/moderate', 2, 8777,),
    ('content-security-policy', 'POST', '/moderate', 3, 8778,),
    ('content-security-policy', 'GET', '/metrics', 0, 8779,),
    ('content-security-policy', 'GET', '/metrics', 1, 8780,),
    ('content-security-policy', 'GET', '/metrics', 2, 8781,),
    ('content-security-policy', 'GET', '/metrics', 3, 8782,),
    ('content-security-policy', 'POST', '/moderate/batch', 0, 8783,),
    ('content-security-policy', 'POST', '/moderate/batch', 1, 8784,),
    ('content-security-policy', 'POST', '/moderate/batch', 2, 8785,),
    ('content-security-policy', 'POST', '/moderate/batch', 3, 8786,),
    ('content-security-policy', 'GET', '/', 0, 8787,),
    ('content-security-policy', 'GET', '/', 1, 8788,),
    ('content-security-policy', 'GET', '/', 2, 8789,),
    ('content-security-policy', 'GET', '/', 3, 8790,),
    ('strict-transport-security', 'GET', '/health', 0, 8791,),
    ('strict-transport-security', 'GET', '/health', 1, 8792,),
    ('strict-transport-security', 'GET', '/health', 2, 8793,),
    ('strict-transport-security', 'GET', '/health', 3, 8794,),
    ('strict-transport-security', 'POST', '/moderate', 0, 8795,),
    ('strict-transport-security', 'POST', '/moderate', 1, 8796,),
    ('strict-transport-security', 'POST', '/moderate', 2, 8797,),
    ('strict-transport-security', 'POST', '/moderate', 3, 8798,),
    ('strict-transport-security', 'GET', '/metrics', 0, 8799,),
    ('strict-transport-security', 'GET', '/metrics', 1, 8800,),
    ('strict-transport-security', 'GET', '/metrics', 2, 8801,),
    ('strict-transport-security', 'GET', '/metrics', 3, 8802,),
    ('strict-transport-security', 'POST', '/moderate/batch', 0, 8803,),
    ('strict-transport-security', 'POST', '/moderate/batch', 1, 8804,),
    ('strict-transport-security', 'POST', '/moderate/batch', 2, 8805,),
    ('strict-transport-security', 'POST', '/moderate/batch', 3, 8806,),
    ('strict-transport-security', 'GET', '/', 0, 8807,),
    ('strict-transport-security', 'GET', '/', 1, 8808,),
    ('strict-transport-security', 'GET', '/', 2, 8809,),
    ('strict-transport-security', 'GET', '/', 3, 8810,),
    ('x-xss-protection', 'GET', '/health', 0, 8811,),
    ('x-xss-protection', 'GET', '/health', 1, 8812,),
    ('x-xss-protection', 'GET', '/health', 2, 8813,),
    ('x-xss-protection', 'GET', '/health', 3, 8814,),
    ('x-xss-protection', 'POST', '/moderate', 0, 8815,),
    ('x-xss-protection', 'POST', '/moderate', 1, 8816,),
    ('x-xss-protection', 'POST', '/moderate', 2, 8817,),
    ('x-xss-protection', 'POST', '/moderate', 3, 8818,),
    ('x-xss-protection', 'GET', '/metrics', 0, 8819,),
    ('x-xss-protection', 'GET', '/metrics', 1, 8820,),
    ('x-xss-protection', 'GET', '/metrics', 2, 8821,),
    ('x-xss-protection', 'GET', '/metrics', 3, 8822,),
    ('x-xss-protection', 'POST', '/moderate/batch', 0, 8823,),
    ('x-xss-protection', 'POST', '/moderate/batch', 1, 8824,),
    ('x-xss-protection', 'POST', '/moderate/batch', 2, 8825,),
    ('x-xss-protection', 'POST', '/moderate/batch', 3, 8826,),
    ('x-xss-protection', 'GET', '/', 0, 8827,),
    ('x-xss-protection', 'GET', '/', 1, 8828,),
    ('x-xss-protection', 'GET', '/', 2, 8829,),
    ('x-xss-protection', 'GET', '/', 3, 8830,),
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
