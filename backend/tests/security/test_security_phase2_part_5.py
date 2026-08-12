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
        "DROP DATABASE production",
        8982,
    ),
    (
        "DROP DATABASE production",
        8983,
    ),
    (
        "DROP DATABASE production",
        8984,
    ),
    (
        "DROP DATABASE production",
        8985,
    ),
    (
        "TRUNCATE TABLE logs",
        8986,
    ),
    (
        "TRUNCATE TABLE logs",
        8987,
    ),
    (
        "TRUNCATE TABLE logs",
        8988,
    ),
    (
        "TRUNCATE TABLE logs",
        8989,
    ),
    (
        "REPLACE INTO words VALUES (1, 'x')",
        8990,
    ),
    (
        "REPLACE INTO words VALUES (1, 'x')",
        8991,
    ),
    (
        "REPLACE INTO words VALUES (1, 'x')",
        8992,
    ),
    (
        "REPLACE INTO words VALUES (1, 'x')",
        8993,
    ),
    (
        "alert(document.cookie)",
        8994,
    ),
    (
        "alert(document.cookie)",
        8995,
    ),
    (
        "alert(document.cookie)",
        8996,
    ),
    (
        "alert(document.cookie)",
        8997,
    ),
    (
        "eval('alert(1)')",
        8998,
    ),
    (
        "eval('alert(1)')",
        8999,
    ),
    (
        "eval('alert(1)')",
        9000,
    ),
    (
        "eval('alert(1)')",
        9001,
    ),
    (
        "new Function('alert(1)')()",
        9002,
    ),
    (
        "new Function('alert(1)')()",
        9003,
    ),
    (
        "new Function('alert(1)')()",
        9004,
    ),
    (
        "new Function('alert(1)')()",
        9005,
    ),
    (
        "{% raw %}{% endraw %}",
        9006,
    ),
    (
        "{% raw %}{% endraw %}",
        9007,
    ),
    (
        "{% raw %}{% endraw %}",
        9008,
    ),
    (
        "{% raw %}{% endraw %}",
        9009,
    ),
    (
        "{{config}}",
        9010,
    ),
    (
        "{{config}}",
        9011,
    ),
    (
        "{{config}}",
        9012,
    ),
    (
        "{{config}}",
        9013,
    ),
    (
        "[[$5*5]]",
        9014,
    ),
    (
        "[[$5*5]]",
        9015,
    ),
    (
        "[[$5*5]]",
        9016,
    ),
    (
        "[[$5*5]]",
        9017,
    ),
    (
        "<%= 7*7 %>",
        9018,
    ),
    (
        "<%= 7*7 %>",
        9019,
    ),
    (
        "<%= 7*7 %>",
        9020,
    ),
    (
        "<%= 7*7 %>",
        9021,
    ),
    (
        "; sh -c 'rm -rf /'",
        9022,
    ),
    (
        "; sh -c 'rm -rf /'",
        9023,
    ),
    (
        "; sh -c 'rm -rf /'",
        9024,
    ),
    (
        "; sh -c 'rm -rf /'",
        9025,
    ),
    (
        "| cat /etc/shadow",
        9026,
    ),
    (
        "| cat /etc/shadow",
        9027,
    ),
    (
        "| cat /etc/shadow",
        9028,
    ),
    (
        "| cat /etc/shadow",
        9029,
    ),
    (
        "&& whoami",
        9030,
    ),
    (
        "&& whoami",
        9031,
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


_TRAVERSAL_REJECTED_CASES: tuple[tuple[str, int], ...] = (
    (
        "../etc/passwd",
        9050,
    ),
    (
        "../etc/passwd",
        9051,
    ),
    (
        "../etc/passwd",
        9052,
    ),
    (
        "../etc/passwd",
        9053,
    ),
    (
        "../etc/passwd",
        9054,
    ),
    (
        "../etc/passwd",
        9055,
    ),
    (
        "..\\windows\\system32",
        9056,
    ),
    (
        "..\\windows\\system32",
        9057,
    ),
    (
        "..\\windows\\system32",
        9058,
    ),
    (
        "..\\windows\\system32",
        9059,
    ),
    (
        "..\\windows\\system32",
        9060,
    ),
    (
        "..\\windows\\system32",
        9061,
    ),
    (
        "%2e%2e%2fetc%2fpasswd",
        9062,
    ),
    (
        "%2e%2e%2fetc%2fpasswd",
        9063,
    ),
    (
        "%2e%2e%2fetc%2fpasswd",
        9064,
    ),
    (
        "%2e%2e%2fetc%2fpasswd",
        9065,
    ),
    (
        "%2e%2e%2fetc%2fpasswd",
        9066,
    ),
    (
        "%2e%2e%2fetc%2fpasswd",
        9067,
    ),
    (
        "..%2f..%2fsecret",
        9068,
    ),
    (
        "..%2f..%2fsecret",
        9069,
    ),
    (
        "..%2f..%2fsecret",
        9070,
    ),
    (
        "..%2f..%2fsecret",
        9071,
    ),
    (
        "..%2f..%2fsecret",
        9072,
    ),
    (
        "..%2f..%2fsecret",
        9073,
    ),
    (
        "etc/passwd",
        9074,
    ),
    (
        "etc/passwd",
        9075,
    ),
    (
        "etc/passwd",
        9076,
    ),
    (
        "etc/passwd",
        9077,
    ),
    (
        "etc/passwd",
        9078,
    ),
    (
        "etc/passwd",
        9079,
    ),
    (
        "../../../etc/passwd",
        9080,
    ),
    (
        "../../../etc/passwd",
        9081,
    ),
    (
        "../../../etc/passwd",
        9082,
    ),
    (
        "../../../etc/passwd",
        9083,
    ),
    (
        "../../../etc/passwd",
        9084,
    ),
    (
        "../../../etc/passwd",
        9085,
    ),
    (
        "....//....//etc/passwd",
        9086,
    ),
    (
        "....//....//etc/passwd",
        9087,
    ),
    (
        "....//....//etc/passwd",
        9088,
    ),
    (
        "....//....//etc/passwd",
        9089,
    ),
    (
        "....//....//etc/passwd",
        9090,
    ),
    (
        "....//....//etc/passwd",
        9091,
    ),
    (
        "..%252f..%252f",
        9092,
    ),
    (
        "..%252f..%252f",
        9093,
    ),
    (
        "..%252f..%252f",
        9094,
    ),
    (
        "..%252f..%252f",
        9095,
    ),
    (
        "..%252f..%252f",
        9096,
    ),
    (
        "..%252f..%252f",
        9097,
    ),
    (
        "..",
        9098,
    ),
    (
        "..",
        9099,
    ),
)


class TestTraversalRejected(BaseTest):
    """Traversal filenames never reach the filesystem."""

    @pytest.mark.parametrize(
        (
            "payload",
            "uid",
        ),
        _TRAVERSAL_REJECTED_CASES,
    )
    def test_traversal_rejected(
        self, client: Any, admin_headers: dict[str, str], payload: str, uid: int
    ) -> None:
        """Traversal filenames never reach the filesystem."""
        response = client.get(f"/admin/logs/{payload}", headers=admin_headers)
        assert response.status_code in (400, 404)
