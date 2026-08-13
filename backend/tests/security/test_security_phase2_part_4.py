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
        "%27%3B%20DROP%20TABLE%20users%3B%20--",
        8883,
    ),
    (
        "'; DROP TABLE users; --",
        8884,
    ),
    (
        "\\u0027; DROP TABLE users; --",
        8885,
    ),
    (
        "' OR 1=1 --",
        8886,
    ),
    (
        "%27%20OR%201%3D1%20--",
        8887,
    ),
    (
        "' OR 1=1 --",
        8888,
    ),
    (
        "\\u0027 OR 1=1 --",
        8889,
    ),
    (
        "<script>alert(1)</script>",
        8890,
    ),
    (
        "%3Cscript%3Ealert%281%29%3C/script%3E",
        8891,
    ),
    (
        "&#60;script&#62;alert(1)&#60;/script&#62;",
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
        "%7B%7B%207%20%2A%207%20%7D%7D",
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
        "%24%7B7%2A7%7D",
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
        "javascript%3Aalert%281%29",
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
        "SELECT%20%2A%20FROM%20users%20WHERE%201%3D1",
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
        "UNION%20SELECT%20password%20FROM%20admin%20--",
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
        "x%27%20OR%20%271%27%3D%271",
        8915,
    ),
    (
        "x' OR '1'='1",
        8916,
    ),
    (
        "x\\u0027 OR \\u00271\\u0027=\\u00271",
        8917,
    ),
    (
        "'; EXEC xp_cmdshell('dir'); --",
        8918,
    ),
    (
        "%27%3B%20EXEC%20xp_cmdshell%28%27dir%27%29%3B%20--",
        8919,
    ),
    (
        "'; EXEC xp_cmdshell('dir'); --",
        8920,
    ),
    (
        "\\u0027; EXEC xp_cmdshell(\\u0027dir\\u0027); --",
        8921,
    ),
    (
        "<!--#exec cmd='ls' -->",
        8922,
    ),
    (
        "%3C%21--%23exec%20cmd%3D%27ls%27%20--%3E",
        8923,
    ),
    (
        "&#60;!--#exec cmd='ls' --&#62;",
        8924,
    ),
    (
        "<!--#exec cmd=\\u0027ls\\u0027 -->",
        8925,
    ),
    (
        "cmd | sh -i",
        8926,
    ),
    (
        "cmd%20%7C%20sh%20-i",
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
        "%60whoami%60",
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
        "%24%28cat%20/etc/passwd%29",
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
        "%253Cscript%253Ealert%281%29%253C/script%253E",
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
        "%5Cu003cscript%5Cu003e",
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
        "%26%2360%3Bscript%26%2362%3B",
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
        "%27%27%27%27%27%27%27%27%27%27%27",
        8951,
    ),
    (
        "'''''''''''",
        8952,
    ),
    (
        "\\u0027\\u0027\\u0027\\u0027\\u0027\\u0027\\u0027\\u0027\\u0027\\u0027\\u0027",
        8953,
    ),
    (
        "1; DROP TABLE",
        8954,
    ),
    (
        "1%3B%20DROP%20TABLE",
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
        "C%3A%5Cboot.ini",
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
        "%3CIMG%20SRC%3Djavascript%3Aalert%28%27XSS%27%29%3E",
        8967,
    ),
    (
        "&#60;IMG SRC=javascript:alert('XSS')&#62;",
        8968,
    ),
    (
        "<IMG SRC=javascript:alert(\\u0027XSS\\u0027)>",
        8969,
    ),
    (
        "<svg onload=alert(1)>",
        8970,
    ),
    (
        "%3Csvg%20onload%3Dalert%281%29%3E",
        8971,
    ),
    (
        "&#60;svg onload=alert(1)&#62;",
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
        "%3Ciframe%20src%3Devil%3E",
        8975,
    ),
    (
        "&#60;iframe src=evil&#62;",
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
        "SELECT%20%27a%27%20AS%20b%20WHERE%201%3D1%20UNION%20SELECT%20NULL",
        8979,
    ),
    (
        "SELECT 'a' AS b WHERE 1=1 UNION SELECT NULL",
        8980,
    ),
    (
        "SELECT \\u0027a\\u0027 AS b WHERE 1=1 UNION SELECT NULL",
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
