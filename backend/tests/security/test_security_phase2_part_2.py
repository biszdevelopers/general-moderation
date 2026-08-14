"""Phase 2 security tests (generated).

Header parity, CORS, auth bypass, injection, traversal, method
restrictions and encoded payloads; see tests/tools/phase2_generator.py."""

# multilingual fixtures use non-ASCII on purpose
from __future__ import annotations

from typing import Any

import pytest

from tests.base_test import BaseTest

_CORS_PREFLIGHT_CASES: tuple[tuple[str, str, str, int, int], ...] = (
    ('http://localhost:3000', 'GET', '/moderate', 200, 8811,),
    ('http://localhost:3000', 'GET', '/health', 200, 8812,),
    ('http://localhost:3000', 'GET', '/metrics', 200, 8813,),
    ('http://localhost:3000', 'GET', '/', 200, 8814,),
    ('http://localhost:3000', 'POST', '/moderate', 200, 8815,),
    ('http://localhost:3000', 'POST', '/health', 200, 8816,),
    ('http://localhost:3000', 'POST', '/metrics', 200, 8817,),
    ('http://localhost:3000', 'POST', '/', 200, 8818,),
    ('http://localhost:3000', 'PUT', '/moderate', 200, 8819,),
    ('http://localhost:3000', 'PUT', '/health', 200, 8820,),
    ('http://localhost:3000', 'PUT', '/metrics', 200, 8821,),
    ('http://localhost:3000', 'PUT', '/', 200, 8822,),
    ('http://localhost:3000', 'DELETE', '/moderate', 200, 8823,),
    ('http://localhost:3000', 'DELETE', '/health', 200, 8824,),
    ('http://localhost:3000', 'DELETE', '/metrics', 200, 8825,),
    ('http://localhost:3000', 'DELETE', '/', 200, 8826,),
    ('http://localhost:3000', 'OPTIONS', '/moderate', 200, 8827,),
    ('http://localhost:3000', 'OPTIONS', '/health', 200, 8828,),
    ('http://localhost:3000', 'OPTIONS', '/metrics', 200, 8829,),
    ('http://localhost:3000', 'OPTIONS', '/', 200, 8830,),
    ('https://mod.example.com', 'GET', '/moderate', 200, 8831,),
    ('https://mod.example.com', 'GET', '/health', 200, 8832,),
    ('https://mod.example.com', 'GET', '/metrics', 200, 8833,),
    ('https://mod.example.com', 'GET', '/', 200, 8834,),
    ('https://mod.example.com', 'POST', '/moderate', 200, 8835,),
    ('https://mod.example.com', 'POST', '/health', 200, 8836,),
    ('https://mod.example.com', 'POST', '/metrics', 200, 8837,),
    ('https://mod.example.com', 'POST', '/', 200, 8838,),
    ('https://mod.example.com', 'PUT', '/moderate', 200, 8839,),
    ('https://mod.example.com', 'PUT', '/health', 200, 8840,),
    ('https://mod.example.com', 'PUT', '/metrics', 200, 8841,),
    ('https://mod.example.com', 'PUT', '/', 200, 8842,),
    ('https://mod.example.com', 'DELETE', '/moderate', 200, 8843,),
    ('https://mod.example.com', 'DELETE', '/health', 200, 8844,),
    ('https://mod.example.com', 'DELETE', '/metrics', 200, 8845,),
    ('https://mod.example.com', 'DELETE', '/', 200, 8846,),
    ('https://mod.example.com', 'OPTIONS', '/moderate', 200, 8847,),
    ('https://mod.example.com', 'OPTIONS', '/health', 200, 8848,),
    ('https://mod.example.com', 'OPTIONS', '/metrics', 200, 8849,),
    ('https://mod.example.com', 'OPTIONS', '/', 200, 8850,),
    ('http://evil.example', 'GET', '/moderate', 400, 8851,),
    ('http://evil.example', 'GET', '/health', 400, 8852,),
    ('http://evil.example', 'GET', '/metrics', 400, 8853,),
    ('http://evil.example', 'GET', '/', 400, 8854,),
    ('http://evil.example', 'POST', '/moderate', 400, 8855,),
    ('http://evil.example', 'POST', '/health', 400, 8856,),
    ('http://evil.example', 'POST', '/metrics', 400, 8857,),
    ('http://evil.example', 'POST', '/', 400, 8858,),
    ('http://evil.example', 'PUT', '/moderate', 400, 8859,),
    ('http://evil.example', 'PUT', '/health', 400, 8860,),
    ('http://evil.example', 'PUT', '/metrics', 400, 8861,),
    ('http://evil.example', 'PUT', '/', 400, 8862,),
    ('http://evil.example', 'DELETE', '/moderate', 400, 8863,),
    ('http://evil.example', 'DELETE', '/health', 400, 8864,),
    ('http://evil.example', 'DELETE', '/metrics', 400, 8865,),
    ('http://evil.example', 'DELETE', '/', 400, 8866,),
    ('http://evil.example', 'OPTIONS', '/moderate', 400, 8867,),
    ('http://evil.example', 'OPTIONS', '/health', 400, 8868,),
    ('http://evil.example', 'OPTIONS', '/metrics', 400, 8869,),
    ('http://evil.example', 'OPTIONS', '/', 400, 8870,),
    ('https://attacker.com', 'GET', '/moderate', 400, 8871,),
    ('https://attacker.com', 'GET', '/health', 400, 8872,),
    ('https://attacker.com', 'GET', '/metrics', 400, 8873,),
    ('https://attacker.com', 'GET', '/', 400, 8874,),
    ('https://attacker.com', 'POST', '/moderate', 400, 8875,),
    ('https://attacker.com', 'POST', '/health', 400, 8876,),
    ('https://attacker.com', 'POST', '/metrics', 400, 8877,),
    ('https://attacker.com', 'POST', '/', 400, 8878,),
    ('https://attacker.com', 'PUT', '/moderate', 400, 8879,),
    ('https://attacker.com', 'PUT', '/health', 400, 8880,),
    ('https://attacker.com', 'PUT', '/metrics', 400, 8881,),
    ('https://attacker.com', 'PUT', '/', 400, 8882,),
    ('https://attacker.com', 'DELETE', '/moderate', 400, 8883,),
    ('https://attacker.com', 'DELETE', '/health', 400, 8884,),
    ('https://attacker.com', 'DELETE', '/metrics', 400, 8885,),
    ('https://attacker.com', 'DELETE', '/', 400, 8886,),
    ('https://attacker.com', 'OPTIONS', '/moderate', 400, 8887,),
    ('https://attacker.com', 'OPTIONS', '/health', 400, 8888,),
    ('https://attacker.com', 'OPTIONS', '/metrics', 400, 8889,),
    ('https://attacker.com', 'OPTIONS', '/', 400, 8890,),
    ('null', 'GET', '/moderate', 400, 8891,),
    ('null', 'GET', '/health', 400, 8892,),
    ('null', 'GET', '/metrics', 400, 8893,),
    ('null', 'GET', '/', 400, 8894,),
    ('null', 'POST', '/moderate', 400, 8895,),
    ('null', 'POST', '/health', 400, 8896,),
    ('null', 'POST', '/metrics', 400, 8897,),
    ('null', 'POST', '/', 400, 8898,),
    ('null', 'PUT', '/moderate', 400, 8899,),
    ('null', 'PUT', '/health', 400, 8900,),
    ('null', 'PUT', '/metrics', 400, 8901,),
    ('null', 'PUT', '/', 400, 8902,),
    ('null', 'DELETE', '/moderate', 400, 8903,),
    ('null', 'DELETE', '/health', 400, 8904,),
    ('null', 'DELETE', '/metrics', 400, 8905,),
    ('null', 'DELETE', '/', 400, 8906,),
    ('null', 'OPTIONS', '/moderate', 400, 8907,),
    ('null', 'OPTIONS', '/health', 400, 8908,),
    ('null', 'OPTIONS', '/metrics', 400, 8909,),
    ('null', 'OPTIONS', '/', 400, 8910,),
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
