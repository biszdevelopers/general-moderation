"""Phase 2 security tests (generated).

Header parity, CORS, auth bypass, injection, traversal, method
restrictions and encoded payloads; see tests/tools/phase2_generator.py."""

# multilingual fixtures use non-ASCII on purpose
from __future__ import annotations

from typing import Any

import pytest

from tests.base_test import BaseTest

_ENCODED_PAYLOAD_CASES: tuple[tuple[str, int], ...] = (
    ("'; DROP TABLE users; --", 9361,),
    ('%27%3B%20DROP%20TABLE%20users%3B%20--', 9362,),
    ("'; DROP TABLE users; --", 9363,),
    ('\\u0027; DROP TABLE users; --', 9364,),
    ("' OR 1=1 --", 9365,),
    ('%27%20OR%201%3D1%20--', 9366,),
    ("' OR 1=1 --", 9367,),
    ('\\u0027 OR 1=1 --', 9368,),
    ('<script>alert(1)</script>', 9369,),
    ('%3Cscript%3Ealert%281%29%3C/script%3E', 9370,),
    ('&#60;script&#62;alert(1)&#60;/script&#62;', 9371,),
    ('<script>alert(1)</script>', 9372,),
    ('{{ 7 * 7 }}', 9373,),
    ('%7B%7B%207%20%2A%207%20%7D%7D', 9374,),
    ('{{ 7 * 7 }}', 9375,),
    ('{{ 7 * 7 }}', 9376,),
    ('${7*7}', 9377,),
    ('%24%7B7%2A7%7D', 9378,),
    ('${7*7}', 9379,),
    ('${7*7}', 9380,),
    ('javascript:alert(1)', 9381,),
    ('javascript%3Aalert%281%29', 9382,),
    ('javascript:alert(1)', 9383,),
    ('javascript:alert(1)', 9384,),
    ('SELECT * FROM users WHERE 1=1', 9385,),
    ('SELECT%20%2A%20FROM%20users%20WHERE%201%3D1', 9386,),
    ('SELECT * FROM users WHERE 1=1', 9387,),
    ('SELECT * FROM users WHERE 1=1', 9388,),
    ('UNION SELECT password FROM admin --', 9389,),
    ('UNION%20SELECT%20password%20FROM%20admin%20--', 9390,),
    ('UNION SELECT password FROM admin --', 9391,),
    ('UNION SELECT password FROM admin --', 9392,),
    ("x' OR '1'='1", 9393,),
    ('x%27%20OR%20%271%27%3D%271', 9394,),
    ("x' OR '1'='1", 9395,),
    ('x\\u0027 OR \\u00271\\u0027=\\u00271', 9396,),
    ("'; EXEC xp_cmdshell('dir'); --", 9397,),
    ('%27%3B%20EXEC%20xp_cmdshell%28%27dir%27%29%3B%20--', 9398,),
    ("'; EXEC xp_cmdshell('dir'); --", 9399,),
    ('\\u0027; EXEC xp_cmdshell(\\u0027dir\\u0027); --', 9400,),
    ("<!--#exec cmd='ls' -->", 9401,),
    ('%3C%21--%23exec%20cmd%3D%27ls%27%20--%3E', 9402,),
    ("&#60;!--#exec cmd='ls' --&#62;", 9403,),
    ('<!--#exec cmd=\\u0027ls\\u0027 -->', 9404,),
    ('cmd | sh -i', 9405,),
    ('cmd%20%7C%20sh%20-i', 9406,),
    ('cmd | sh -i', 9407,),
    ('cmd | sh -i', 9408,),
    ('`whoami`', 9409,),
    ('%60whoami%60', 9410,),
    ('`whoami`', 9411,),
    ('`whoami`', 9412,),
    ('$(cat /etc/passwd)', 9413,),
    ('%24%28cat%20/etc/passwd%29', 9414,),
    ('$(cat /etc/passwd)', 9415,),
    ('$(cat /etc/passwd)', 9416,),
    ('%3Cscript%3Ealert(1)%3C/script%3E', 9417,),
    ('%253Cscript%253Ealert%281%29%253C/script%253E', 9418,),
    ('%3Cscript%3Ealert(1)%3C/script%3E', 9419,),
    ('%3Cscript%3Ealert(1)%3C/script%3E', 9420,),
    ('\\u003cscript\\u003e', 9421,),
    ('%5Cu003cscript%5Cu003e', 9422,),
    ('\\u003cscript\\u003e', 9423,),
    ('\\u003cscript\\u003e', 9424,),
    ('&#60;script&#62;', 9425,),
    ('%26%2360%3Bscript%26%2362%3B', 9426,),
    ('&#60;script&#62;', 9427,),
    ('&#60;script&#62;', 9428,),
    ("'''''''''''", 9429,),
    ('%27%27%27%27%27%27%27%27%27%27%27', 9430,),
    ("'''''''''''", 9431,),
    ('\\u0027\\u0027\\u0027\\u0027\\u0027\\u0027\\u0027\\u0027\\u0027\\u0027\\u0027', 9432,),
    ('1; DROP TABLE', 9433,),
    ('1%3B%20DROP%20TABLE', 9434,),
    ('1; DROP TABLE', 9435,),
    ('1; DROP TABLE', 9436,),
    ('../../../etc/passwd', 9437,),
    ('../../../etc/passwd', 9438,),
    ('../../../etc/passwd', 9439,),
    ('../../../etc/passwd', 9440,),
    ('C:\\boot.ini', 9441,),
    ('C%3A%5Cboot.ini', 9442,),
    ('C:\\boot.ini', 9443,),
    ('C:\\boot.ini', 9444,),
    ("<IMG SRC=javascript:alert('XSS')>", 9445,),
    ('%3CIMG%20SRC%3Djavascript%3Aalert%28%27XSS%27%29%3E', 9446,),
    ("&#60;IMG SRC=javascript:alert('XSS')&#62;", 9447,),
    ('<IMG SRC=javascript:alert(\\u0027XSS\\u0027)>', 9448,),
    ('<svg onload=alert(1)>', 9449,),
    ('%3Csvg%20onload%3Dalert%281%29%3E', 9450,),
    ('&#60;svg onload=alert(1)&#62;', 9451,),
    ('<svg onload=alert(1)>', 9452,),
    ('<iframe src=evil>', 9453,),
    ('%3Ciframe%20src%3Devil%3E', 9454,),
    ('&#60;iframe src=evil&#62;', 9455,),
    ('<iframe src=evil>', 9456,),
    ("SELECT 'a' AS b WHERE 1=1 UNION SELECT NULL", 9457,),
    ('SELECT%20%27a%27%20AS%20b%20WHERE%201%3D1%20UNION%20SELECT%20NULL', 9458,),
    ("SELECT 'a' AS b WHERE 1=1 UNION SELECT NULL", 9459,),
    ('SELECT \\u0027a\\u0027 AS b WHERE 1=1 UNION SELECT NULL', 9460,),
)

class TestEncodedPayload(BaseTest):
    """Encoded payloads never crash the moderator."""

    @pytest.mark.parametrize(('payload', 'uid',), _ENCODED_PAYLOAD_CASES)
    def test_encoded_payload(self, client: Any, payload: str, uid: int) -> None:
        """Encoded payloads never crash the moderator."""
        response = client.post('/moderate', json={'text': payload, 'app_name': 'a'})
        assert response.status_code == 200
        assert response.json()['verdict'] in ('PASS', 'BLOCK', 'REVIEW')
