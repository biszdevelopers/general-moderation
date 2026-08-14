"""Phase 2 security tests (generated).

Header parity, CORS, auth bypass, injection, traversal, method
restrictions and encoded payloads; see tests/tools/phase2_generator.py."""

# multilingual fixtures use non-ASCII on purpose
from __future__ import annotations

from typing import Any

import pytest

from tests.base_test import BaseTest

_ENCODED_PAYLOAD_CASES: tuple[tuple[str, int], ...] = (
    ("'; DROP TABLE users; --", 9401,),
    ('%27%3B%20DROP%20TABLE%20users%3B%20--', 9402,),
    ("'; DROP TABLE users; --", 9403,),
    ('\\u0027; DROP TABLE users; --', 9404,),
    ("' OR 1=1 --", 9405,),
    ('%27%20OR%201%3D1%20--', 9406,),
    ("' OR 1=1 --", 9407,),
    ('\\u0027 OR 1=1 --', 9408,),
    ('<script>alert(1)</script>', 9409,),
    ('%3Cscript%3Ealert%281%29%3C/script%3E', 9410,),
    ('&#60;script&#62;alert(1)&#60;/script&#62;', 9411,),
    ('<script>alert(1)</script>', 9412,),
    ('{{ 7 * 7 }}', 9413,),
    ('%7B%7B%207%20%2A%207%20%7D%7D', 9414,),
    ('{{ 7 * 7 }}', 9415,),
    ('{{ 7 * 7 }}', 9416,),
    ('${7*7}', 9417,),
    ('%24%7B7%2A7%7D', 9418,),
    ('${7*7}', 9419,),
    ('${7*7}', 9420,),
    ('javascript:alert(1)', 9421,),
    ('javascript%3Aalert%281%29', 9422,),
    ('javascript:alert(1)', 9423,),
    ('javascript:alert(1)', 9424,),
    ('SELECT * FROM users WHERE 1=1', 9425,),
    ('SELECT%20%2A%20FROM%20users%20WHERE%201%3D1', 9426,),
    ('SELECT * FROM users WHERE 1=1', 9427,),
    ('SELECT * FROM users WHERE 1=1', 9428,),
    ('UNION SELECT password FROM admin --', 9429,),
    ('UNION%20SELECT%20password%20FROM%20admin%20--', 9430,),
    ('UNION SELECT password FROM admin --', 9431,),
    ('UNION SELECT password FROM admin --', 9432,),
    ("x' OR '1'='1", 9433,),
    ('x%27%20OR%20%271%27%3D%271', 9434,),
    ("x' OR '1'='1", 9435,),
    ('x\\u0027 OR \\u00271\\u0027=\\u00271', 9436,),
    ("'; EXEC xp_cmdshell('dir'); --", 9437,),
    ('%27%3B%20EXEC%20xp_cmdshell%28%27dir%27%29%3B%20--', 9438,),
    ("'; EXEC xp_cmdshell('dir'); --", 9439,),
    ('\\u0027; EXEC xp_cmdshell(\\u0027dir\\u0027); --', 9440,),
    ("<!--#exec cmd='ls' -->", 9441,),
    ('%3C%21--%23exec%20cmd%3D%27ls%27%20--%3E', 9442,),
    ("&#60;!--#exec cmd='ls' --&#62;", 9443,),
    ('<!--#exec cmd=\\u0027ls\\u0027 -->', 9444,),
    ('cmd | sh -i', 9445,),
    ('cmd%20%7C%20sh%20-i', 9446,),
    ('cmd | sh -i', 9447,),
    ('cmd | sh -i', 9448,),
    ('`whoami`', 9449,),
    ('%60whoami%60', 9450,),
    ('`whoami`', 9451,),
    ('`whoami`', 9452,),
    ('$(cat /etc/passwd)', 9453,),
    ('%24%28cat%20/etc/passwd%29', 9454,),
    ('$(cat /etc/passwd)', 9455,),
    ('$(cat /etc/passwd)', 9456,),
    ('%3Cscript%3Ealert(1)%3C/script%3E', 9457,),
    ('%253Cscript%253Ealert%281%29%253C/script%253E', 9458,),
    ('%3Cscript%3Ealert(1)%3C/script%3E', 9459,),
    ('%3Cscript%3Ealert(1)%3C/script%3E', 9460,),
    ('\\u003cscript\\u003e', 9461,),
    ('%5Cu003cscript%5Cu003e', 9462,),
    ('\\u003cscript\\u003e', 9463,),
    ('\\u003cscript\\u003e', 9464,),
    ('&#60;script&#62;', 9465,),
    ('%26%2360%3Bscript%26%2362%3B', 9466,),
    ('&#60;script&#62;', 9467,),
    ('&#60;script&#62;', 9468,),
    ("'''''''''''", 9469,),
    ('%27%27%27%27%27%27%27%27%27%27%27', 9470,),
    ("'''''''''''", 9471,),
    ('\\u0027\\u0027\\u0027\\u0027\\u0027\\u0027\\u0027\\u0027\\u0027\\u0027\\u0027', 9472,),
    ('1; DROP TABLE', 9473,),
    ('1%3B%20DROP%20TABLE', 9474,),
    ('1; DROP TABLE', 9475,),
    ('1; DROP TABLE', 9476,),
    ('../../../etc/passwd', 9477,),
    ('../../../etc/passwd', 9478,),
    ('../../../etc/passwd', 9479,),
    ('../../../etc/passwd', 9480,),
    ('C:\\boot.ini', 9481,),
    ('C%3A%5Cboot.ini', 9482,),
    ('C:\\boot.ini', 9483,),
    ('C:\\boot.ini', 9484,),
    ("<IMG SRC=javascript:alert('XSS')>", 9485,),
    ('%3CIMG%20SRC%3Djavascript%3Aalert%28%27XSS%27%29%3E', 9486,),
    ("&#60;IMG SRC=javascript:alert('XSS')&#62;", 9487,),
    ('<IMG SRC=javascript:alert(\\u0027XSS\\u0027)>', 9488,),
    ('<svg onload=alert(1)>', 9489,),
    ('%3Csvg%20onload%3Dalert%281%29%3E', 9490,),
    ('&#60;svg onload=alert(1)&#62;', 9491,),
    ('<svg onload=alert(1)>', 9492,),
    ('<iframe src=evil>', 9493,),
    ('%3Ciframe%20src%3Devil%3E', 9494,),
    ('&#60;iframe src=evil&#62;', 9495,),
    ('<iframe src=evil>', 9496,),
    ("SELECT 'a' AS b WHERE 1=1 UNION SELECT NULL", 9497,),
    ('SELECT%20%27a%27%20AS%20b%20WHERE%201%3D1%20UNION%20SELECT%20NULL', 9498,),
    ("SELECT 'a' AS b WHERE 1=1 UNION SELECT NULL", 9499,),
    ('SELECT \\u0027a\\u0027 AS b WHERE 1=1 UNION SELECT NULL', 9500,),
)

class TestEncodedPayload(BaseTest):
    """Encoded payloads never crash the moderator."""

    @pytest.mark.parametrize(('payload', 'uid',), _ENCODED_PAYLOAD_CASES)
    def test_encoded_payload(self, client: Any, payload: str, uid: int) -> None:
        """Encoded payloads never crash the moderator."""
        response = client.post('/moderate', json={'text': payload, 'app_name': 'a'})
        assert response.status_code == 200
        assert response.json()['verdict'] in ('PASS', 'BLOCK', 'REVIEW')
