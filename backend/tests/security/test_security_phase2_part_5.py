"""Phase 2 security tests (generated).

Header parity, CORS, auth bypass, injection, traversal, method
restrictions and encoded payloads; see tests/tools/phase2_generator.py."""

# multilingual fixtures use non-ASCII on purpose
from __future__ import annotations

from typing import Any

import pytest

from tests.base_test import BaseTest

_INJECTION_SAFE_CASES: tuple[tuple[str, int], ...] = (
    ('DROP DATABASE production', 8982,),
    ('DROP%20DATABASE%20production', 8983,),
    ('DROP DATABASE production', 8984,),
    ('DROP DATABASE production', 8985,),
    ('TRUNCATE TABLE logs', 8986,),
    ('TRUNCATE%20TABLE%20logs', 8987,),
    ('TRUNCATE TABLE logs', 8988,),
    ('TRUNCATE TABLE logs', 8989,),
    ("REPLACE INTO words VALUES (1, 'x')", 8990,),
    ('REPLACE%20INTO%20words%20VALUES%20%281%2C%20%27x%27%29', 8991,),
    ("REPLACE INTO words VALUES (1, 'x')", 8992,),
    ('REPLACE INTO words VALUES (1, \\u0027x\\u0027)', 8993,),
    ('alert(document.cookie)', 8994,),
    ('alert%28document.cookie%29', 8995,),
    ('alert(document.cookie)', 8996,),
    ('alert(document.cookie)', 8997,),
    ("eval('alert(1)')", 8998,),
    ('eval%28%27alert%281%29%27%29', 8999,),
    ("eval('alert(1)')", 9000,),
    ('eval(\\u0027alert(1)\\u0027)', 9001,),
    ("new Function('alert(1)')()", 9002,),
    ('new%20Function%28%27alert%281%29%27%29%28%29', 9003,),
    ("new Function('alert(1)')()", 9004,),
    ('new Function(\\u0027alert(1)\\u0027)()', 9005,),
    ('{% raw %}{% endraw %}', 9006,),
    ('%7B%25%20raw%20%25%7D%7B%25%20endraw%20%25%7D', 9007,),
    ('{% raw %}{% endraw %}', 9008,),
    ('{% raw %}{% endraw %}', 9009,),
    ('{{config}}', 9010,),
    ('%7B%7Bconfig%7D%7D', 9011,),
    ('{{config}}', 9012,),
    ('{{config}}', 9013,),
    ('[[$5*5]]', 9014,),
    ('%5B%5B%245%2A5%5D%5D', 9015,),
    ('[[$5*5]]', 9016,),
    ('[[$5*5]]', 9017,),
    ('<%= 7*7 %>', 9018,),
    ('%3C%25%3D%207%2A7%20%25%3E', 9019,),
    ('&#60;%= 7*7 %&#62;', 9020,),
    ('<%= 7*7 %>', 9021,),
    ("; sh -c 'rm -rf /'", 9022,),
    ('%3B%20sh%20-c%20%27rm%20-rf%20/%27', 9023,),
    ("; sh -c 'rm -rf /'", 9024,),
    ('; sh -c \\u0027rm -rf /\\u0027', 9025,),
    ('| cat /etc/shadow', 9026,),
    ('%7C%20cat%20/etc/shadow', 9027,),
    ('| cat /etc/shadow', 9028,),
    ('| cat /etc/shadow', 9029,),
    ('&& whoami', 9030,),
    ('%26%26%20whoami', 9031,),
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
    ('../etc/passwd', 9050,),
    ('../etc/passwd', 9051,),
    ('../etc/passwd%00', 9052,),
    ('..%2Fetc%2Fpasswd', 9053,),
    ('..\\windows\\system32', 9054,),
    ('..%5Cwindows%5Csystem32', 9055,),
    ('..\\windows\\system32%00', 9056,),
    ('..%5Cwindows%5Csystem32', 9057,),
    ('%2e%2e%2fetc%2fpasswd', 9058,),
    ('%252e%252e%252fetc%252fpasswd', 9059,),
    ('%2e%2e%2fetc%2fpasswd%00', 9060,),
    ('%252e%252e%252fetc%252fpasswd', 9061,),
    ('..%2f..%2fsecret', 9062,),
    ('..%252f..%252fsecret', 9063,),
    ('..%2f..%2fsecret%00', 9064,),
    ('..%252f..%252fsecret', 9065,),
    ('etc/passwd', 9066,),
    ('etc/passwd', 9067,),
    ('etc/passwd%00', 9068,),
    ('etc%2Fpasswd', 9069,),
    ('../../../etc/passwd', 9070,),
    ('../../../etc/passwd', 9071,),
    ('../../../etc/passwd%00', 9072,),
    ('..%2F..%2F..%2Fetc%2Fpasswd', 9073,),
    ('....//....//etc/passwd', 9074,),
    ('....//....//etc/passwd', 9075,),
    ('....//....//etc/passwd%00', 9076,),
    ('....%2F%2F....%2F%2Fetc%2Fpasswd', 9077,),
    ('..%252f..%252f', 9078,),
    ('..%25252f..%25252f', 9079,),
    ('..%252f..%252f%00', 9080,),
    ('..%25252f..%25252f', 9081,),
    ('..', 9082,),
    ('..', 9083,),
    ('..%00', 9084,),
    ('..', 9085,),
    ('a/../../b', 9086,),
    ('a/../../b', 9087,),
    ('a/../../b%00', 9088,),
    ('a%2F..%2F..%2Fb', 9089,),
    ('..\\..\\..\\boot.ini', 9090,),
    ('..%5C..%5C..%5Cboot.ini', 9091,),
    ('..\\..\\..\\boot.ini%00', 9092,),
    ('..%5C..%5C..%5Cboot.ini', 9093,),
    ('..%2f..%2f..%2fetc%2fpasswd', 9094,),
    ('..%252f..%252f..%252fetc%252fpasswd', 9095,),
    ('..%2f..%2f..%2fetc%2fpasswd%00', 9096,),
    ('..%252f..%252f..%252fetc%252fpasswd', 9097,),
    ('..././.../etc/passwd', 9098,),
    ('..././.../etc/passwd', 9099,),
)

class TestTraversalRejected(BaseTest):
    """Traversal filenames never reach the filesystem."""

    @pytest.mark.parametrize(('payload', 'uid',), _TRAVERSAL_REJECTED_CASES)
    def test_traversal_rejected(self, client: Any, admin_headers: dict[str, str], payload: str, uid: int) -> None:
        """Traversal filenames never reach the filesystem."""
        response = client.get(f'/admin/logs/{payload}', headers=admin_headers)
        assert response.status_code in (400, 404)
