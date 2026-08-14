"""Phase 2 security tests (generated).

Header parity, CORS, auth bypass, injection, traversal, method
restrictions and encoded payloads; see tests/tools/phase2_generator.py."""

# multilingual fixtures use non-ASCII on purpose
from __future__ import annotations

from typing import Any

import pytest

from tests.base_test import BaseTest

_INJECTION_SAFE_CASES: tuple[tuple[str, int], ...] = (
    ('DROP DATABASE production', 9181,),
    ('DROP%20DATABASE%20production', 9182,),
    ('DROP DATABASE production', 9183,),
    ('DROP DATABASE production', 9184,),
    ('TRUNCATE TABLE logs', 9185,),
    ('TRUNCATE%20TABLE%20logs', 9186,),
    ('TRUNCATE TABLE logs', 9187,),
    ('TRUNCATE TABLE logs', 9188,),
    ("REPLACE INTO words VALUES (1, 'x')", 9189,),
    ('REPLACE%20INTO%20words%20VALUES%20%281%2C%20%27x%27%29', 9190,),
    ("REPLACE INTO words VALUES (1, 'x')", 9191,),
    ('REPLACE INTO words VALUES (1, \\u0027x\\u0027)', 9192,),
    ('alert(document.cookie)', 9193,),
    ('alert%28document.cookie%29', 9194,),
    ('alert(document.cookie)', 9195,),
    ('alert(document.cookie)', 9196,),
    ("eval('alert(1)')", 9197,),
    ('eval%28%27alert%281%29%27%29', 9198,),
    ("eval('alert(1)')", 9199,),
    ('eval(\\u0027alert(1)\\u0027)', 9200,),
    ("new Function('alert(1)')()", 9201,),
    ('new%20Function%28%27alert%281%29%27%29%28%29', 9202,),
    ("new Function('alert(1)')()", 9203,),
    ('new Function(\\u0027alert(1)\\u0027)()', 9204,),
    ('{% raw %}{% endraw %}', 9205,),
    ('%7B%25%20raw%20%25%7D%7B%25%20endraw%20%25%7D', 9206,),
    ('{% raw %}{% endraw %}', 9207,),
    ('{% raw %}{% endraw %}', 9208,),
    ('{{config}}', 9209,),
    ('%7B%7Bconfig%7D%7D', 9210,),
    ('{{config}}', 9211,),
    ('{{config}}', 9212,),
    ('[[$5*5]]', 9213,),
    ('%5B%5B%245%2A5%5D%5D', 9214,),
    ('[[$5*5]]', 9215,),
    ('[[$5*5]]', 9216,),
    ('<%= 7*7 %>', 9217,),
    ('%3C%25%3D%207%2A7%20%25%3E', 9218,),
    ('&#60;%= 7*7 %&#62;', 9219,),
    ('<%= 7*7 %>', 9220,),
    ("; sh -c 'rm -rf /'", 9221,),
    ('%3B%20sh%20-c%20%27rm%20-rf%20/%27', 9222,),
    ("; sh -c 'rm -rf /'", 9223,),
    ('; sh -c \\u0027rm -rf /\\u0027', 9224,),
    ('| cat /etc/shadow', 9225,),
    ('%7C%20cat%20/etc/shadow', 9226,),
    ('| cat /etc/shadow', 9227,),
    ('| cat /etc/shadow', 9228,),
    ('&& whoami', 9229,),
    ('%26%26%20whoami', 9230,),
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
    ('../etc/passwd', 9249,),
    ('../etc/passwd', 9250,),
    ('../etc/passwd%00', 9251,),
    ('..%2Fetc%2Fpasswd', 9252,),
    ('..\\windows\\system32', 9253,),
    ('..%5Cwindows%5Csystem32', 9254,),
    ('..\\windows\\system32%00', 9255,),
    ('..%5Cwindows%5Csystem32', 9256,),
    ('%2e%2e%2fetc%2fpasswd', 9257,),
    ('%252e%252e%252fetc%252fpasswd', 9258,),
    ('%2e%2e%2fetc%2fpasswd%00', 9259,),
    ('%252e%252e%252fetc%252fpasswd', 9260,),
    ('..%2f..%2fsecret', 9261,),
    ('..%252f..%252fsecret', 9262,),
    ('..%2f..%2fsecret%00', 9263,),
    ('..%252f..%252fsecret', 9264,),
    ('etc/passwd', 9265,),
    ('etc/passwd', 9266,),
    ('etc/passwd%00', 9267,),
    ('etc%2Fpasswd', 9268,),
    ('../../../etc/passwd', 9269,),
    ('../../../etc/passwd', 9270,),
    ('../../../etc/passwd%00', 9271,),
    ('..%2F..%2F..%2Fetc%2Fpasswd', 9272,),
    ('....//....//etc/passwd', 9273,),
    ('....//....//etc/passwd', 9274,),
    ('....//....//etc/passwd%00', 9275,),
    ('....%2F%2F....%2F%2Fetc%2Fpasswd', 9276,),
    ('..%252f..%252f', 9277,),
    ('..%25252f..%25252f', 9278,),
    ('..%252f..%252f%00', 9279,),
    ('..%25252f..%25252f', 9280,),
    ('..', 9281,),
    ('..', 9282,),
    ('..%00', 9283,),
    ('..', 9284,),
    ('a/../../b', 9285,),
    ('a/../../b', 9286,),
    ('a/../../b%00', 9287,),
    ('a%2F..%2F..%2Fb', 9288,),
    ('..\\..\\..\\boot.ini', 9289,),
    ('..%5C..%5C..%5Cboot.ini', 9290,),
    ('..\\..\\..\\boot.ini%00', 9291,),
    ('..%5C..%5C..%5Cboot.ini', 9292,),
    ('..%2f..%2f..%2fetc%2fpasswd', 9293,),
    ('..%252f..%252f..%252fetc%252fpasswd', 9294,),
    ('..%2f..%2f..%2fetc%2fpasswd%00', 9295,),
    ('..%252f..%252f..%252fetc%252fpasswd', 9296,),
    ('..././.../etc/passwd', 9297,),
    ('..././.../etc/passwd', 9298,),
)

class TestTraversalRejected(BaseTest):
    """Traversal filenames never reach the filesystem."""

    @pytest.mark.parametrize(('payload', 'uid',), _TRAVERSAL_REJECTED_CASES)
    def test_traversal_rejected(self, client: Any, admin_headers: dict[str, str], payload: str, uid: int) -> None:
        """Traversal filenames never reach the filesystem."""
        response = client.get(f'/admin/logs/{payload}', headers=admin_headers)
        assert response.status_code in (400, 404)
