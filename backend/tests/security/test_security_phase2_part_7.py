"""Phase 2 security tests (generated).

Header parity, CORS, auth bypass, injection, traversal, method
restrictions and encoded payloads; see tests/tools/phase2_generator.py."""

# multilingual fixtures use non-ASCII on purpose
from __future__ import annotations

from typing import Any

import pytest

from tests.base_test import BaseTest

_ENCODED_PAYLOAD_CASES: tuple[tuple[str, int], ...] = (
    ("'; DROP TABLE users; --", 9202,),
    ('%27%3B%20DROP%20TABLE%20users%3B%20--', 9203,),
    ("'; DROP TABLE users; --", 9204,),
    ('\\u0027; DROP TABLE users; --', 9205,),
    ("' OR 1=1 --", 9206,),
    ('%27%20OR%201%3D1%20--', 9207,),
    ("' OR 1=1 --", 9208,),
    ('\\u0027 OR 1=1 --', 9209,),
    ('<script>alert(1)</script>', 9210,),
    ('%3Cscript%3Ealert%281%29%3C/script%3E', 9211,),
    ('&#60;script&#62;alert(1)&#60;/script&#62;', 9212,),
    ('<script>alert(1)</script>', 9213,),
    ('{{ 7 * 7 }}', 9214,),
    ('%7B%7B%207%20%2A%207%20%7D%7D', 9215,),
    ('{{ 7 * 7 }}', 9216,),
    ('{{ 7 * 7 }}', 9217,),
    ('${7*7}', 9218,),
    ('%24%7B7%2A7%7D', 9219,),
    ('${7*7}', 9220,),
    ('${7*7}', 9221,),
    ('javascript:alert(1)', 9222,),
    ('javascript%3Aalert%281%29', 9223,),
    ('javascript:alert(1)', 9224,),
    ('javascript:alert(1)', 9225,),
    ('SELECT * FROM users WHERE 1=1', 9226,),
    ('SELECT%20%2A%20FROM%20users%20WHERE%201%3D1', 9227,),
    ('SELECT * FROM users WHERE 1=1', 9228,),
    ('SELECT * FROM users WHERE 1=1', 9229,),
    ('UNION SELECT password FROM admin --', 9230,),
    ('UNION%20SELECT%20password%20FROM%20admin%20--', 9231,),
    ('UNION SELECT password FROM admin --', 9232,),
    ('UNION SELECT password FROM admin --', 9233,),
    ("x' OR '1'='1", 9234,),
    ('x%27%20OR%20%271%27%3D%271', 9235,),
    ("x' OR '1'='1", 9236,),
    ('x\\u0027 OR \\u00271\\u0027=\\u00271', 9237,),
    ("'; EXEC xp_cmdshell('dir'); --", 9238,),
    ('%27%3B%20EXEC%20xp_cmdshell%28%27dir%27%29%3B%20--', 9239,),
    ("'; EXEC xp_cmdshell('dir'); --", 9240,),
    ('\\u0027; EXEC xp_cmdshell(\\u0027dir\\u0027); --', 9241,),
    ("<!--#exec cmd='ls' -->", 9242,),
    ('%3C%21--%23exec%20cmd%3D%27ls%27%20--%3E', 9243,),
    ("&#60;!--#exec cmd='ls' --&#62;", 9244,),
    ('<!--#exec cmd=\\u0027ls\\u0027 -->', 9245,),
    ('cmd | sh -i', 9246,),
    ('cmd%20%7C%20sh%20-i', 9247,),
    ('cmd | sh -i', 9248,),
    ('cmd | sh -i', 9249,),
    ('`whoami`', 9250,),
    ('%60whoami%60', 9251,),
    ('`whoami`', 9252,),
    ('`whoami`', 9253,),
    ('$(cat /etc/passwd)', 9254,),
    ('%24%28cat%20/etc/passwd%29', 9255,),
    ('$(cat /etc/passwd)', 9256,),
    ('$(cat /etc/passwd)', 9257,),
    ('%3Cscript%3Ealert(1)%3C/script%3E', 9258,),
    ('%253Cscript%253Ealert%281%29%253C/script%253E', 9259,),
    ('%3Cscript%3Ealert(1)%3C/script%3E', 9260,),
    ('%3Cscript%3Ealert(1)%3C/script%3E', 9261,),
    ('\\u003cscript\\u003e', 9262,),
    ('%5Cu003cscript%5Cu003e', 9263,),
    ('\\u003cscript\\u003e', 9264,),
    ('\\u003cscript\\u003e', 9265,),
    ('&#60;script&#62;', 9266,),
    ('%26%2360%3Bscript%26%2362%3B', 9267,),
    ('&#60;script&#62;', 9268,),
    ('&#60;script&#62;', 9269,),
    ("'''''''''''", 9270,),
    ('%27%27%27%27%27%27%27%27%27%27%27', 9271,),
    ("'''''''''''", 9272,),
    ('\\u0027\\u0027\\u0027\\u0027\\u0027\\u0027\\u0027\\u0027\\u0027\\u0027\\u0027', 9273,),
    ('1; DROP TABLE', 9274,),
    ('1%3B%20DROP%20TABLE', 9275,),
    ('1; DROP TABLE', 9276,),
    ('1; DROP TABLE', 9277,),
    ('../../../etc/passwd', 9278,),
    ('../../../etc/passwd', 9279,),
    ('../../../etc/passwd', 9280,),
    ('../../../etc/passwd', 9281,),
    ('C:\\boot.ini', 9282,),
    ('C%3A%5Cboot.ini', 9283,),
    ('C:\\boot.ini', 9284,),
    ('C:\\boot.ini', 9285,),
    ("<IMG SRC=javascript:alert('XSS')>", 9286,),
    ('%3CIMG%20SRC%3Djavascript%3Aalert%28%27XSS%27%29%3E', 9287,),
    ("&#60;IMG SRC=javascript:alert('XSS')&#62;", 9288,),
    ('<IMG SRC=javascript:alert(\\u0027XSS\\u0027)>', 9289,),
    ('<svg onload=alert(1)>', 9290,),
    ('%3Csvg%20onload%3Dalert%281%29%3E', 9291,),
    ('&#60;svg onload=alert(1)&#62;', 9292,),
    ('<svg onload=alert(1)>', 9293,),
    ('<iframe src=evil>', 9294,),
    ('%3Ciframe%20src%3Devil%3E', 9295,),
    ('&#60;iframe src=evil&#62;', 9296,),
    ('<iframe src=evil>', 9297,),
    ("SELECT 'a' AS b WHERE 1=1 UNION SELECT NULL", 9298,),
    ('SELECT%20%27a%27%20AS%20b%20WHERE%201%3D1%20UNION%20SELECT%20NULL', 9299,),
    ("SELECT 'a' AS b WHERE 1=1 UNION SELECT NULL", 9300,),
    ('SELECT \\u0027a\\u0027 AS b WHERE 1=1 UNION SELECT NULL', 9301,),
)

class TestEncodedPayload(BaseTest):
    """Encoded payloads never crash the moderator."""

    @pytest.mark.parametrize(('payload', 'uid',), _ENCODED_PAYLOAD_CASES)
    def test_encoded_payload(self, client: Any, payload: str, uid: int) -> None:
        """Encoded payloads never crash the moderator."""
        response = client.post('/moderate', json={'text': payload, 'app_name': 'a'})
        assert response.status_code == 200
        assert response.json()['verdict'] in ('PASS', 'BLOCK', 'REVIEW')
