"""Phase 2 security tests (generated).

Header parity, CORS, auth bypass, injection, traversal, method
restrictions and encoded payloads; see tests/tools/phase2_generator.py."""

# multilingual fixtures use non-ASCII on purpose
from __future__ import annotations

from typing import Any

import pytest

from tests.base_test import BaseTest

_CORS_PREFLIGHT_CASES: tuple[tuple[str, str, str, int, int], ...] = (
    ('http://localhost:3000', 'GET', '/moderate', 200, 8851,),
    ('http://localhost:3000', 'GET', '/health', 200, 8852,),
    ('http://localhost:3000', 'GET', '/metrics', 200, 8853,),
    ('http://localhost:3000', 'GET', '/', 200, 8854,),
    ('http://localhost:3000', 'POST', '/moderate', 200, 8855,),
    ('http://localhost:3000', 'POST', '/health', 200, 8856,),
    ('http://localhost:3000', 'POST', '/metrics', 200, 8857,),
    ('http://localhost:3000', 'POST', '/', 200, 8858,),
    ('http://localhost:3000', 'PUT', '/moderate', 200, 8859,),
    ('http://localhost:3000', 'PUT', '/health', 200, 8860,),
    ('http://localhost:3000', 'PUT', '/metrics', 200, 8861,),
    ('http://localhost:3000', 'PUT', '/', 200, 8862,),
    ('http://localhost:3000', 'DELETE', '/moderate', 200, 8863,),
    ('http://localhost:3000', 'DELETE', '/health', 200, 8864,),
    ('http://localhost:3000', 'DELETE', '/metrics', 200, 8865,),
    ('http://localhost:3000', 'DELETE', '/', 200, 8866,),
    ('http://localhost:3000', 'OPTIONS', '/moderate', 200, 8867,),
    ('http://localhost:3000', 'OPTIONS', '/health', 200, 8868,),
    ('http://localhost:3000', 'OPTIONS', '/metrics', 200, 8869,),
    ('http://localhost:3000', 'OPTIONS', '/', 200, 8870,),
    ('https://mod.example.com', 'GET', '/moderate', 200, 8871,),
    ('https://mod.example.com', 'GET', '/health', 200, 8872,),
    ('https://mod.example.com', 'GET', '/metrics', 200, 8873,),
    ('https://mod.example.com', 'GET', '/', 200, 8874,),
    ('https://mod.example.com', 'POST', '/moderate', 200, 8875,),
    ('https://mod.example.com', 'POST', '/health', 200, 8876,),
    ('https://mod.example.com', 'POST', '/metrics', 200, 8877,),
    ('https://mod.example.com', 'POST', '/', 200, 8878,),
    ('https://mod.example.com', 'PUT', '/moderate', 200, 8879,),
    ('https://mod.example.com', 'PUT', '/health', 200, 8880,),
    ('https://mod.example.com', 'PUT', '/metrics', 200, 8881,),
    ('https://mod.example.com', 'PUT', '/', 200, 8882,),
    ('https://mod.example.com', 'DELETE', '/moderate', 200, 8883,),
    ('https://mod.example.com', 'DELETE', '/health', 200, 8884,),
    ('https://mod.example.com', 'DELETE', '/metrics', 200, 8885,),
    ('https://mod.example.com', 'DELETE', '/', 200, 8886,),
    ('https://mod.example.com', 'OPTIONS', '/moderate', 200, 8887,),
    ('https://mod.example.com', 'OPTIONS', '/health', 200, 8888,),
    ('https://mod.example.com', 'OPTIONS', '/metrics', 200, 8889,),
    ('https://mod.example.com', 'OPTIONS', '/', 200, 8890,),
    ('http://evil.example', 'GET', '/moderate', 400, 8891,),
    ('http://evil.example', 'GET', '/health', 400, 8892,),
    ('http://evil.example', 'GET', '/metrics', 400, 8893,),
    ('http://evil.example', 'GET', '/', 400, 8894,),
    ('http://evil.example', 'POST', '/moderate', 400, 8895,),
    ('http://evil.example', 'POST', '/health', 400, 8896,),
    ('http://evil.example', 'POST', '/metrics', 400, 8897,),
    ('http://evil.example', 'POST', '/', 400, 8898,),
    ('http://evil.example', 'PUT', '/moderate', 400, 8899,),
    ('http://evil.example', 'PUT', '/health', 400, 8900,),
    ('http://evil.example', 'PUT', '/metrics', 400, 8901,),
    ('http://evil.example', 'PUT', '/', 400, 8902,),
    ('http://evil.example', 'DELETE', '/moderate', 400, 8903,),
    ('http://evil.example', 'DELETE', '/health', 400, 8904,),
    ('http://evil.example', 'DELETE', '/metrics', 400, 8905,),
    ('http://evil.example', 'DELETE', '/', 400, 8906,),
    ('http://evil.example', 'OPTIONS', '/moderate', 400, 8907,),
    ('http://evil.example', 'OPTIONS', '/health', 400, 8908,),
    ('http://evil.example', 'OPTIONS', '/metrics', 400, 8909,),
    ('http://evil.example', 'OPTIONS', '/', 400, 8910,),
    ('https://attacker.com', 'GET', '/moderate', 400, 8911,),
    ('https://attacker.com', 'GET', '/health', 400, 8912,),
    ('https://attacker.com', 'GET', '/metrics', 400, 8913,),
    ('https://attacker.com', 'GET', '/', 400, 8914,),
    ('https://attacker.com', 'POST', '/moderate', 400, 8915,),
    ('https://attacker.com', 'POST', '/health', 400, 8916,),
    ('https://attacker.com', 'POST', '/metrics', 400, 8917,),
    ('https://attacker.com', 'POST', '/', 400, 8918,),
    ('https://attacker.com', 'PUT', '/moderate', 400, 8919,),
    ('https://attacker.com', 'PUT', '/health', 400, 8920,),
    ('https://attacker.com', 'PUT', '/metrics', 400, 8921,),
    ('https://attacker.com', 'PUT', '/', 400, 8922,),
    ('https://attacker.com', 'DELETE', '/moderate', 400, 8923,),
    ('https://attacker.com', 'DELETE', '/health', 400, 8924,),
    ('https://attacker.com', 'DELETE', '/metrics', 400, 8925,),
    ('https://attacker.com', 'DELETE', '/', 400, 8926,),
    ('https://attacker.com', 'OPTIONS', '/moderate', 400, 8927,),
    ('https://attacker.com', 'OPTIONS', '/health', 400, 8928,),
    ('https://attacker.com', 'OPTIONS', '/metrics', 400, 8929,),
    ('https://attacker.com', 'OPTIONS', '/', 400, 8930,),
    ('null', 'GET', '/moderate', 400, 8931,),
    ('null', 'GET', '/health', 400, 8932,),
    ('null', 'GET', '/metrics', 400, 8933,),
    ('null', 'GET', '/', 400, 8934,),
    ('null', 'POST', '/moderate', 400, 8935,),
    ('null', 'POST', '/health', 400, 8936,),
    ('null', 'POST', '/metrics', 400, 8937,),
    ('null', 'POST', '/', 400, 8938,),
    ('null', 'PUT', '/moderate', 400, 8939,),
    ('null', 'PUT', '/health', 400, 8940,),
    ('null', 'PUT', '/metrics', 400, 8941,),
    ('null', 'PUT', '/', 400, 8942,),
    ('null', 'DELETE', '/moderate', 400, 8943,),
    ('null', 'DELETE', '/health', 400, 8944,),
    ('null', 'DELETE', '/metrics', 400, 8945,),
    ('null', 'DELETE', '/', 400, 8946,),
    ('null', 'OPTIONS', '/moderate', 400, 8947,),
    ('null', 'OPTIONS', '/health', 400, 8948,),
    ('null', 'OPTIONS', '/metrics', 400, 8949,),
    ('null', 'OPTIONS', '/', 400, 8950,),
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
