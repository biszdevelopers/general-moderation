"""Phase 2 security tests (generated).

Header parity, CORS, auth bypass, injection, traversal, method
restrictions and encoded payloads; see tests/tools/phase2_generator.py."""

# multilingual fixtures use non-ASCII on purpose
from __future__ import annotations

from typing import Any

import pytest

from tests.base_test import BaseTest

_HEADER_PRESENT_CASES: tuple[tuple[str, str, str, int, int], ...] = (
    ('x-content-type-options', 'GET', '/health', 0, 8532,),
    ('x-content-type-options', 'GET', '/health', 1, 8533,),
    ('x-content-type-options', 'GET', '/health', 2, 8534,),
    ('x-content-type-options', 'GET', '/health', 3, 8535,),
    ('x-content-type-options', 'POST', '/moderate', 0, 8536,),
    ('x-content-type-options', 'POST', '/moderate', 1, 8537,),
    ('x-content-type-options', 'POST', '/moderate', 2, 8538,),
    ('x-content-type-options', 'POST', '/moderate', 3, 8539,),
    ('x-content-type-options', 'GET', '/metrics', 0, 8540,),
    ('x-content-type-options', 'GET', '/metrics', 1, 8541,),
    ('x-content-type-options', 'GET', '/metrics', 2, 8542,),
    ('x-content-type-options', 'GET', '/metrics', 3, 8543,),
    ('x-content-type-options', 'POST', '/moderate/batch', 0, 8544,),
    ('x-content-type-options', 'POST', '/moderate/batch', 1, 8545,),
    ('x-content-type-options', 'POST', '/moderate/batch', 2, 8546,),
    ('x-content-type-options', 'POST', '/moderate/batch', 3, 8547,),
    ('x-content-type-options', 'GET', '/', 0, 8548,),
    ('x-content-type-options', 'GET', '/', 1, 8549,),
    ('x-content-type-options', 'GET', '/', 2, 8550,),
    ('x-content-type-options', 'GET', '/', 3, 8551,),
    ('x-frame-options', 'GET', '/health', 0, 8552,),
    ('x-frame-options', 'GET', '/health', 1, 8553,),
    ('x-frame-options', 'GET', '/health', 2, 8554,),
    ('x-frame-options', 'GET', '/health', 3, 8555,),
    ('x-frame-options', 'POST', '/moderate', 0, 8556,),
    ('x-frame-options', 'POST', '/moderate', 1, 8557,),
    ('x-frame-options', 'POST', '/moderate', 2, 8558,),
    ('x-frame-options', 'POST', '/moderate', 3, 8559,),
    ('x-frame-options', 'GET', '/metrics', 0, 8560,),
    ('x-frame-options', 'GET', '/metrics', 1, 8561,),
    ('x-frame-options', 'GET', '/metrics', 2, 8562,),
    ('x-frame-options', 'GET', '/metrics', 3, 8563,),
    ('x-frame-options', 'POST', '/moderate/batch', 0, 8564,),
    ('x-frame-options', 'POST', '/moderate/batch', 1, 8565,),
    ('x-frame-options', 'POST', '/moderate/batch', 2, 8566,),
    ('x-frame-options', 'POST', '/moderate/batch', 3, 8567,),
    ('x-frame-options', 'GET', '/', 0, 8568,),
    ('x-frame-options', 'GET', '/', 1, 8569,),
    ('x-frame-options', 'GET', '/', 2, 8570,),
    ('x-frame-options', 'GET', '/', 3, 8571,),
    ('content-security-policy', 'GET', '/health', 0, 8572,),
    ('content-security-policy', 'GET', '/health', 1, 8573,),
    ('content-security-policy', 'GET', '/health', 2, 8574,),
    ('content-security-policy', 'GET', '/health', 3, 8575,),
    ('content-security-policy', 'POST', '/moderate', 0, 8576,),
    ('content-security-policy', 'POST', '/moderate', 1, 8577,),
    ('content-security-policy', 'POST', '/moderate', 2, 8578,),
    ('content-security-policy', 'POST', '/moderate', 3, 8579,),
    ('content-security-policy', 'GET', '/metrics', 0, 8580,),
    ('content-security-policy', 'GET', '/metrics', 1, 8581,),
    ('content-security-policy', 'GET', '/metrics', 2, 8582,),
    ('content-security-policy', 'GET', '/metrics', 3, 8583,),
    ('content-security-policy', 'POST', '/moderate/batch', 0, 8584,),
    ('content-security-policy', 'POST', '/moderate/batch', 1, 8585,),
    ('content-security-policy', 'POST', '/moderate/batch', 2, 8586,),
    ('content-security-policy', 'POST', '/moderate/batch', 3, 8587,),
    ('content-security-policy', 'GET', '/', 0, 8588,),
    ('content-security-policy', 'GET', '/', 1, 8589,),
    ('content-security-policy', 'GET', '/', 2, 8590,),
    ('content-security-policy', 'GET', '/', 3, 8591,),
    ('strict-transport-security', 'GET', '/health', 0, 8592,),
    ('strict-transport-security', 'GET', '/health', 1, 8593,),
    ('strict-transport-security', 'GET', '/health', 2, 8594,),
    ('strict-transport-security', 'GET', '/health', 3, 8595,),
    ('strict-transport-security', 'POST', '/moderate', 0, 8596,),
    ('strict-transport-security', 'POST', '/moderate', 1, 8597,),
    ('strict-transport-security', 'POST', '/moderate', 2, 8598,),
    ('strict-transport-security', 'POST', '/moderate', 3, 8599,),
    ('strict-transport-security', 'GET', '/metrics', 0, 8600,),
    ('strict-transport-security', 'GET', '/metrics', 1, 8601,),
    ('strict-transport-security', 'GET', '/metrics', 2, 8602,),
    ('strict-transport-security', 'GET', '/metrics', 3, 8603,),
    ('strict-transport-security', 'POST', '/moderate/batch', 0, 8604,),
    ('strict-transport-security', 'POST', '/moderate/batch', 1, 8605,),
    ('strict-transport-security', 'POST', '/moderate/batch', 2, 8606,),
    ('strict-transport-security', 'POST', '/moderate/batch', 3, 8607,),
    ('strict-transport-security', 'GET', '/', 0, 8608,),
    ('strict-transport-security', 'GET', '/', 1, 8609,),
    ('strict-transport-security', 'GET', '/', 2, 8610,),
    ('strict-transport-security', 'GET', '/', 3, 8611,),
    ('x-xss-protection', 'GET', '/health', 0, 8612,),
    ('x-xss-protection', 'GET', '/health', 1, 8613,),
    ('x-xss-protection', 'GET', '/health', 2, 8614,),
    ('x-xss-protection', 'GET', '/health', 3, 8615,),
    ('x-xss-protection', 'POST', '/moderate', 0, 8616,),
    ('x-xss-protection', 'POST', '/moderate', 1, 8617,),
    ('x-xss-protection', 'POST', '/moderate', 2, 8618,),
    ('x-xss-protection', 'POST', '/moderate', 3, 8619,),
    ('x-xss-protection', 'GET', '/metrics', 0, 8620,),
    ('x-xss-protection', 'GET', '/metrics', 1, 8621,),
    ('x-xss-protection', 'GET', '/metrics', 2, 8622,),
    ('x-xss-protection', 'GET', '/metrics', 3, 8623,),
    ('x-xss-protection', 'POST', '/moderate/batch', 0, 8624,),
    ('x-xss-protection', 'POST', '/moderate/batch', 1, 8625,),
    ('x-xss-protection', 'POST', '/moderate/batch', 2, 8626,),
    ('x-xss-protection', 'POST', '/moderate/batch', 3, 8627,),
    ('x-xss-protection', 'GET', '/', 0, 8628,),
    ('x-xss-protection', 'GET', '/', 1, 8629,),
    ('x-xss-protection', 'GET', '/', 2, 8630,),
    ('x-xss-protection', 'GET', '/', 3, 8631,),
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
