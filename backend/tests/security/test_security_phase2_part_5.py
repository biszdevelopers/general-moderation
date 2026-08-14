"""Phase 2 security tests (generated).

Header parity, CORS, auth bypass, injection, traversal, method
restrictions and encoded payloads; see tests/tools/phase2_generator.py."""

# multilingual fixtures use non-ASCII on purpose
from __future__ import annotations

from typing import Any

import pytest

from tests.base_test import BaseTest

_INJECTION_SAFE_CASES: tuple[tuple[str, int], ...] = (
    ('DROP DATABASE production', 9141,),
    ('DROP%20DATABASE%20production', 9142,),
    ('DROP DATABASE production', 9143,),
    ('DROP DATABASE production', 9144,),
    ('TRUNCATE TABLE logs', 9145,),
    ('TRUNCATE%20TABLE%20logs', 9146,),
    ('TRUNCATE TABLE logs', 9147,),
    ('TRUNCATE TABLE logs', 9148,),
    ("REPLACE INTO words VALUES (1, 'x')", 9149,),
    ('REPLACE%20INTO%20words%20VALUES%20%281%2C%20%27x%27%29', 9150,),
    ("REPLACE INTO words VALUES (1, 'x')", 9151,),
    ('REPLACE INTO words VALUES (1, \\u0027x\\u0027)', 9152,),
    ('alert(document.cookie)', 9153,),
    ('alert%28document.cookie%29', 9154,),
    ('alert(document.cookie)', 9155,),
    ('alert(document.cookie)', 9156,),
    ("eval('alert(1)')", 9157,),
    ('eval%28%27alert%281%29%27%29', 9158,),
    ("eval('alert(1)')", 9159,),
    ('eval(\\u0027alert(1)\\u0027)', 9160,),
    ("new Function('alert(1)')()", 9161,),
    ('new%20Function%28%27alert%281%29%27%29%28%29', 9162,),
    ("new Function('alert(1)')()", 9163,),
    ('new Function(\\u0027alert(1)\\u0027)()', 9164,),
    ('{% raw %}{% endraw %}', 9165,),
    ('%7B%25%20raw%20%25%7D%7B%25%20endraw%20%25%7D', 9166,),
    ('{% raw %}{% endraw %}', 9167,),
    ('{% raw %}{% endraw %}', 9168,),
    ('{{config}}', 9169,),
    ('%7B%7Bconfig%7D%7D', 9170,),
    ('{{config}}', 9171,),
    ('{{config}}', 9172,),
    ('[[$5*5]]', 9173,),
    ('%5B%5B%245%2A5%5D%5D', 9174,),
    ('[[$5*5]]', 9175,),
    ('[[$5*5]]', 9176,),
    ('<%= 7*7 %>', 9177,),
    ('%3C%25%3D%207%2A7%20%25%3E', 9178,),
    ('&#60;%= 7*7 %&#62;', 9179,),
    ('<%= 7*7 %>', 9180,),
    ("; sh -c 'rm -rf /'", 9181,),
    ('%3B%20sh%20-c%20%27rm%20-rf%20/%27', 9182,),
    ("; sh -c 'rm -rf /'", 9183,),
    ('; sh -c \\u0027rm -rf /\\u0027', 9184,),
    ('| cat /etc/shadow', 9185,),
    ('%7C%20cat%20/etc/shadow', 9186,),
    ('| cat /etc/shadow', 9187,),
    ('| cat /etc/shadow', 9188,),
    ('&& whoami', 9189,),
    ('%26%26%20whoami', 9190,),
)

class TestInjectionSafe(BaseTest):
    """Injection payloads never crash the moderator."""

    @pytest.mark.parametrize(('payload', 'uid',), _INJECTION_SAFE_CASES)
    def test_injection_safe(self, client: Any, payload: str, uid: int) -> None:
        """Injection payloads never crash the moderator."""
        response = client.post('/moderate', json={'text': payload, 'app_name': 'a'})
        assert response.status_code == 200
        assert response.json()['verdict'] in ('PASS', 'BLOCK', 'REVIEW')


_TRAVERSAL_REJECTED_CASES: tuple[tuple[str, int], ...] = (
    ('../etc/passwd', 9209,),
    ('../etc/passwd', 9210,),
    ('../etc/passwd%00', 9211,),
    ('..%2Fetc%2Fpasswd', 9212,),
    ('..\\windows\\system32', 9213,),
    ('..%5Cwindows%5Csystem32', 9214,),
    ('..\\windows\\system32%00', 9215,),
    ('..%5Cwindows%5Csystem32', 9216,),
    ('%2e%2e%2fetc%2fpasswd', 9217,),
    ('%252e%252e%252fetc%252fpasswd', 9218,),
    ('%2e%2e%2fetc%2fpasswd%00', 9219,),
    ('%252e%252e%252fetc%252fpasswd', 9220,),
    ('..%2f..%2fsecret', 9221,),
    ('..%252f..%252fsecret', 9222,),
    ('..%2f..%2fsecret%00', 9223,),
    ('..%252f..%252fsecret', 9224,),
    ('etc/passwd', 9225,),
    ('etc/passwd', 9226,),
    ('etc/passwd%00', 9227,),
    ('etc%2Fpasswd', 9228,),
    ('../../../etc/passwd', 9229,),
    ('../../../etc/passwd', 9230,),
    ('../../../etc/passwd%00', 9231,),
    ('..%2F..%2F..%2Fetc%2Fpasswd', 9232,),
    ('....//....//etc/passwd', 9233,),
    ('....//....//etc/passwd', 9234,),
    ('....//....//etc/passwd%00', 9235,),
    ('....%2F%2F....%2F%2Fetc%2Fpasswd', 9236,),
    ('..%252f..%252f', 9237,),
    ('..%25252f..%25252f', 9238,),
    ('..%252f..%252f%00', 9239,),
    ('..%25252f..%25252f', 9240,),
    ('..', 9241,),
    ('..', 9242,),
    ('..%00', 9243,),
    ('..', 9244,),
    ('a/../../b', 9245,),
    ('a/../../b', 9246,),
    ('a/../../b%00', 9247,),
    ('a%2F..%2F..%2Fb', 9248,),
    ('..\\..\\..\\boot.ini', 9249,),
    ('..%5C..%5C..%5Cboot.ini', 9250,),
    ('..\\..\\..\\boot.ini%00', 9251,),
    ('..%5C..%5C..%5Cboot.ini', 9252,),
    ('..%2f..%2f..%2fetc%2fpasswd', 9253,),
    ('..%252f..%252f..%252fetc%252fpasswd', 9254,),
    ('..%2f..%2f..%2fetc%2fpasswd%00', 9255,),
    ('..%252f..%252f..%252fetc%252fpasswd', 9256,),
    ('..././.../etc/passwd', 9257,),
    ('..././.../etc/passwd', 9258,),
)

class TestTraversalRejected(BaseTest):
    """Traversal filenames never reach the filesystem."""

    @pytest.mark.parametrize(('payload', 'uid',), _TRAVERSAL_REJECTED_CASES)
    def test_traversal_rejected(self, client: Any, admin_headers: dict[str, str], payload: str, uid: int) -> None:
        """Traversal filenames never reach the filesystem."""
        response = client.get(f'/admin/logs/{payload}', headers=admin_headers)
        assert response.status_code in (400, 404)
