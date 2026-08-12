"""Phase 2 security tests (generated).

Header parity, CORS, auth bypass, injection, traversal, method
restrictions and encoded payloads; see tests/tools/phase2_generator.py."""

# multilingual fixtures use non-ASCII on purpose
from __future__ import annotations

from typing import Any

import pytest

from tests.base_test import BaseTest

_INJECTION_SAFE_CASES: tuple[tuple[str, int], ...] = (
    (
        "'; DROP TABLE users; --",
        8882,
    ),
    (
        "'; DROP TABLE users; --",
        8883,
    ),
    (
        "'; DROP TABLE users; --",
        8884,
    ),
    (
        "'; DROP TABLE users; --",
        8885,
    ),
    (
        "' OR 1=1 --",
        8886,
    ),
    (
        "' OR 1=1 --",
        8887,
    ),
    (
        "' OR 1=1 --",
        8888,
    ),
    (
        "' OR 1=1 --",
        8889,
    ),
    (
        "<script>alert(1)</script>",
        8890,
    ),
    (
        "<script>alert(1)</script>",
        8891,
    ),
    (
        "<script>alert(1)</script>",
        8892,
    ),
    (
        "<script>alert(1)</script>",
        8893,
    ),
    (
        "{{ 7 * 7 }}",
        8894,
    ),
    (
        "{{ 7 * 7 }}",
        8895,
    ),
    (
        "{{ 7 * 7 }}",
        8896,
    ),
    (
        "{{ 7 * 7 }}",
        8897,
    ),
    (
        "${7*7}",
        8898,
    ),
    (
        "${7*7}",
        8899,
    ),
    (
        "${7*7}",
        8900,
    ),
    (
        "${7*7}",
        8901,
    ),
    (
        "javascript:alert(1)",
        8902,
    ),
    (
        "javascript:alert(1)",
        8903,
    ),
    (
        "javascript:alert(1)",
        8904,
    ),
    (
        "javascript:alert(1)",
        8905,
    ),
    (
        "SELECT * FROM users WHERE 1=1",
        8906,
    ),
    (
        "SELECT * FROM users WHERE 1=1",
        8907,
    ),
    (
        "SELECT * FROM users WHERE 1=1",
        8908,
    ),
    (
        "SELECT * FROM users WHERE 1=1",
        8909,
    ),
    (
        "UNION SELECT password FROM admin --",
        8910,
    ),
    (
        "UNION SELECT password FROM admin --",
        8911,
    ),
    (
        "UNION SELECT password FROM admin --",
        8912,
    ),
    (
        "UNION SELECT password FROM admin --",
        8913,
    ),
    (
        "x' OR '1'='1",
        8914,
    ),
    (
        "x' OR '1'='1",
        8915,
    ),
    (
        "x' OR '1'='1",
        8916,
    ),
    (
        "x' OR '1'='1",
        8917,
    ),
    (
        "'; EXEC xp_cmdshell('dir'); --",
        8918,
    ),
    (
        "'; EXEC xp_cmdshell('dir'); --",
        8919,
    ),
    (
        "'; EXEC xp_cmdshell('dir'); --",
        8920,
    ),
    (
        "'; EXEC xp_cmdshell('dir'); --",
        8921,
    ),
    (
        "<!--#exec cmd='ls' -->",
        8922,
    ),
    (
        "<!--#exec cmd='ls' -->",
        8923,
    ),
    (
        "<!--#exec cmd='ls' -->",
        8924,
    ),
    (
        "<!--#exec cmd='ls' -->",
        8925,
    ),
    (
        "cmd | sh -i",
        8926,
    ),
    (
        "cmd | sh -i",
        8927,
    ),
    (
        "cmd | sh -i",
        8928,
    ),
    (
        "cmd | sh -i",
        8929,
    ),
    (
        "`whoami`",
        8930,
    ),
    (
        "`whoami`",
        8931,
    ),
    (
        "`whoami`",
        8932,
    ),
    (
        "`whoami`",
        8933,
    ),
    (
        "$(cat /etc/passwd)",
        8934,
    ),
    (
        "$(cat /etc/passwd)",
        8935,
    ),
    (
        "$(cat /etc/passwd)",
        8936,
    ),
    (
        "$(cat /etc/passwd)",
        8937,
    ),
    (
        "%3Cscript%3Ealert(1)%3C/script%3E",
        8938,
    ),
    (
        "%3Cscript%3Ealert(1)%3C/script%3E",
        8939,
    ),
    (
        "%3Cscript%3Ealert(1)%3C/script%3E",
        8940,
    ),
    (
        "%3Cscript%3Ealert(1)%3C/script%3E",
        8941,
    ),
    (
        "\\u003cscript\\u003e",
        8942,
    ),
    (
        "\\u003cscript\\u003e",
        8943,
    ),
    (
        "\\u003cscript\\u003e",
        8944,
    ),
    (
        "\\u003cscript\\u003e",
        8945,
    ),
    (
        "&#60;script&#62;",
        8946,
    ),
    (
        "&#60;script&#62;",
        8947,
    ),
    (
        "&#60;script&#62;",
        8948,
    ),
    (
        "&#60;script&#62;",
        8949,
    ),
    (
        "'''''''''''",
        8950,
    ),
    (
        "'''''''''''",
        8951,
    ),
    (
        "'''''''''''",
        8952,
    ),
    (
        "'''''''''''",
        8953,
    ),
    (
        "1; DROP TABLE",
        8954,
    ),
    (
        "1; DROP TABLE",
        8955,
    ),
    (
        "1; DROP TABLE",
        8956,
    ),
    (
        "1; DROP TABLE",
        8957,
    ),
    (
        "../../../etc/passwd",
        8958,
    ),
    (
        "../../../etc/passwd",
        8959,
    ),
    (
        "../../../etc/passwd",
        8960,
    ),
    (
        "../../../etc/passwd",
        8961,
    ),
    (
        "C:\\boot.ini",
        8962,
    ),
    (
        "C:\\boot.ini",
        8963,
    ),
    (
        "C:\\boot.ini",
        8964,
    ),
    (
        "C:\\boot.ini",
        8965,
    ),
    (
        "<IMG SRC=javascript:alert('XSS')>",
        8966,
    ),
    (
        "<IMG SRC=javascript:alert('XSS')>",
        8967,
    ),
    (
        "<IMG SRC=javascript:alert('XSS')>",
        8968,
    ),
    (
        "<IMG SRC=javascript:alert('XSS')>",
        8969,
    ),
    (
        "<svg onload=alert(1)>",
        8970,
    ),
    (
        "<svg onload=alert(1)>",
        8971,
    ),
    (
        "<svg onload=alert(1)>",
        8972,
    ),
    (
        "<svg onload=alert(1)>",
        8973,
    ),
    (
        "<iframe src=evil>",
        8974,
    ),
    (
        "<iframe src=evil>",
        8975,
    ),
    (
        "<iframe src=evil>",
        8976,
    ),
    (
        "<iframe src=evil>",
        8977,
    ),
    (
        "SELECT 'a' AS b WHERE 1=1 UNION SELECT NULL",
        8978,
    ),
    (
        "SELECT 'a' AS b WHERE 1=1 UNION SELECT NULL",
        8979,
    ),
    (
        "SELECT 'a' AS b WHERE 1=1 UNION SELECT NULL",
        8980,
    ),
    (
        "SELECT 'a' AS b WHERE 1=1 UNION SELECT NULL",
        8981,
    ),
)


class TestInjectionSafe(BaseTest):
    """Injection payloads never crash the moderator."""

    @pytest.mark.parametrize(
        (
            "payload",
            "uid",
        ),
        _INJECTION_SAFE_CASES,
    )
    def test_injection_safe(self, client: Any, payload: str, uid: int) -> None:
        """Injection payloads never crash the moderator."""
        response = client.post("/moderate", json={"text": payload, "app_name": "a"})
        assert response.status_code == 200
        assert response.json()["verdict"] in ("PASS", "BLOCK", "REVIEW")
