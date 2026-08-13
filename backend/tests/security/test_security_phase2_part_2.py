"""Phase 2 security tests (generated).

Header parity, CORS, auth bypass, injection, traversal, method
restrictions and encoded payloads; see tests/tools/phase2_generator.py."""

# multilingual fixtures use non-ASCII on purpose
from __future__ import annotations

from typing import Any

import pytest

from tests.base_test import BaseTest

_CORS_PREFLIGHT_CASES: tuple[tuple[str, str, str, int, int], ...] = (
    ('http://localhost:3000', 'GET', '/moderate', 200, 8652,),
    ('http://localhost:3000', 'GET', '/health', 200, 8653,),
    ('http://localhost:3000', 'GET', '/metrics', 200, 8654,),
    ('http://localhost:3000', 'GET', '/', 200, 8655,),
    ('http://localhost:3000', 'POST', '/moderate', 200, 8656,),
    ('http://localhost:3000', 'POST', '/health', 200, 8657,),
    ('http://localhost:3000', 'POST', '/metrics', 200, 8658,),
    ('http://localhost:3000', 'POST', '/', 200, 8659,),
    ('http://localhost:3000', 'PUT', '/moderate', 200, 8660,),
    ('http://localhost:3000', 'PUT', '/health', 200, 8661,),
    ('http://localhost:3000', 'PUT', '/metrics', 200, 8662,),
    ('http://localhost:3000', 'PUT', '/', 200, 8663,),
    ('http://localhost:3000', 'DELETE', '/moderate', 200, 8664,),
    ('http://localhost:3000', 'DELETE', '/health', 200, 8665,),
    ('http://localhost:3000', 'DELETE', '/metrics', 200, 8666,),
    ('http://localhost:3000', 'DELETE', '/', 200, 8667,),
    ('http://localhost:3000', 'OPTIONS', '/moderate', 200, 8668,),
    ('http://localhost:3000', 'OPTIONS', '/health', 200, 8669,),
    ('http://localhost:3000', 'OPTIONS', '/metrics', 200, 8670,),
    ('http://localhost:3000', 'OPTIONS', '/', 200, 8671,),
    ('https://mod.example.com', 'GET', '/moderate', 200, 8672,),
    ('https://mod.example.com', 'GET', '/health', 200, 8673,),
    ('https://mod.example.com', 'GET', '/metrics', 200, 8674,),
    ('https://mod.example.com', 'GET', '/', 200, 8675,),
    ('https://mod.example.com', 'POST', '/moderate', 200, 8676,),
    ('https://mod.example.com', 'POST', '/health', 200, 8677,),
    ('https://mod.example.com', 'POST', '/metrics', 200, 8678,),
    ('https://mod.example.com', 'POST', '/', 200, 8679,),
    ('https://mod.example.com', 'PUT', '/moderate', 200, 8680,),
    ('https://mod.example.com', 'PUT', '/health', 200, 8681,),
    ('https://mod.example.com', 'PUT', '/metrics', 200, 8682,),
    ('https://mod.example.com', 'PUT', '/', 200, 8683,),
    ('https://mod.example.com', 'DELETE', '/moderate', 200, 8684,),
    ('https://mod.example.com', 'DELETE', '/health', 200, 8685,),
    ('https://mod.example.com', 'DELETE', '/metrics', 200, 8686,),
    ('https://mod.example.com', 'DELETE', '/', 200, 8687,),
    ('https://mod.example.com', 'OPTIONS', '/moderate', 200, 8688,),
    ('https://mod.example.com', 'OPTIONS', '/health', 200, 8689,),
    ('https://mod.example.com', 'OPTIONS', '/metrics', 200, 8690,),
    ('https://mod.example.com', 'OPTIONS', '/', 200, 8691,),
    ('http://evil.example', 'GET', '/moderate', 400, 8692,),
    ('http://evil.example', 'GET', '/health', 400, 8693,),
    ('http://evil.example', 'GET', '/metrics', 400, 8694,),
    ('http://evil.example', 'GET', '/', 400, 8695,),
    ('http://evil.example', 'POST', '/moderate', 400, 8696,),
    ('http://evil.example', 'POST', '/health', 400, 8697,),
    ('http://evil.example', 'POST', '/metrics', 400, 8698,),
    ('http://evil.example', 'POST', '/', 400, 8699,),
    ('http://evil.example', 'PUT', '/moderate', 400, 8700,),
    ('http://evil.example', 'PUT', '/health', 400, 8701,),
    ('http://evil.example', 'PUT', '/metrics', 400, 8702,),
    ('http://evil.example', 'PUT', '/', 400, 8703,),
    ('http://evil.example', 'DELETE', '/moderate', 400, 8704,),
    ('http://evil.example', 'DELETE', '/health', 400, 8705,),
    ('http://evil.example', 'DELETE', '/metrics', 400, 8706,),
    ('http://evil.example', 'DELETE', '/', 400, 8707,),
    ('http://evil.example', 'OPTIONS', '/moderate', 400, 8708,),
    ('http://evil.example', 'OPTIONS', '/health', 400, 8709,),
    ('http://evil.example', 'OPTIONS', '/metrics', 400, 8710,),
    ('http://evil.example', 'OPTIONS', '/', 400, 8711,),
    ('https://attacker.com', 'GET', '/moderate', 400, 8712,),
    ('https://attacker.com', 'GET', '/health', 400, 8713,),
    ('https://attacker.com', 'GET', '/metrics', 400, 8714,),
    ('https://attacker.com', 'GET', '/', 400, 8715,),
    ('https://attacker.com', 'POST', '/moderate', 400, 8716,),
    ('https://attacker.com', 'POST', '/health', 400, 8717,),
    ('https://attacker.com', 'POST', '/metrics', 400, 8718,),
    ('https://attacker.com', 'POST', '/', 400, 8719,),
    ('https://attacker.com', 'PUT', '/moderate', 400, 8720,),
    ('https://attacker.com', 'PUT', '/health', 400, 8721,),
    ('https://attacker.com', 'PUT', '/metrics', 400, 8722,),
    ('https://attacker.com', 'PUT', '/', 400, 8723,),
    ('https://attacker.com', 'DELETE', '/moderate', 400, 8724,),
    ('https://attacker.com', 'DELETE', '/health', 400, 8725,),
    ('https://attacker.com', 'DELETE', '/metrics', 400, 8726,),
    ('https://attacker.com', 'DELETE', '/', 400, 8727,),
    ('https://attacker.com', 'OPTIONS', '/moderate', 400, 8728,),
    ('https://attacker.com', 'OPTIONS', '/health', 400, 8729,),
    ('https://attacker.com', 'OPTIONS', '/metrics', 400, 8730,),
    ('https://attacker.com', 'OPTIONS', '/', 400, 8731,),
    ('null', 'GET', '/moderate', 400, 8732,),
    ('null', 'GET', '/health', 400, 8733,),
    ('null', 'GET', '/metrics', 400, 8734,),
    ('null', 'GET', '/', 400, 8735,),
    ('null', 'POST', '/moderate', 400, 8736,),
    ('null', 'POST', '/health', 400, 8737,),
    ('null', 'POST', '/metrics', 400, 8738,),
    ('null', 'POST', '/', 400, 8739,),
    ('null', 'PUT', '/moderate', 400, 8740,),
    ('null', 'PUT', '/health', 400, 8741,),
    ('null', 'PUT', '/metrics', 400, 8742,),
    ('null', 'PUT', '/', 400, 8743,),
    ('null', 'DELETE', '/moderate', 400, 8744,),
    ('null', 'DELETE', '/health', 400, 8745,),
    ('null', 'DELETE', '/metrics', 400, 8746,),
    ('null', 'DELETE', '/', 400, 8747,),
    ('null', 'OPTIONS', '/moderate', 400, 8748,),
    ('null', 'OPTIONS', '/health', 400, 8749,),
    ('null', 'OPTIONS', '/metrics', 400, 8750,),
    ('null', 'OPTIONS', '/', 400, 8751,),
)

class TestCorsPreflight(BaseTest):
    """Preflight and CORS responses are handled without error."""

    @pytest.mark.parametrize(('origin', 'method', 'path', 'expected_status', 'uid',), _CORS_PREFLIGHT_CASES)
    def test_cors_preflight(self, client: Any, origin: str, method: str, path: str, expected_status: int, uid: int) -> None:
        """Preflight and CORS responses are handled without error."""
        response = client.options(
            path,
            headers={'Origin': origin, 'Access-Control-Request-Method': method},
        )
        assert response.status_code == expected_status
