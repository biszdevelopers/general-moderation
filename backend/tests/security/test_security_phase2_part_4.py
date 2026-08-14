"""Phase 2 security tests (generated).

Header parity, CORS, auth bypass, injection, traversal, method
restrictions and encoded payloads; see tests/tools/phase2_generator.py."""

# multilingual fixtures use non-ASCII on purpose
from __future__ import annotations

from typing import Any

import pytest

from tests.base_test import BaseTest

_INJECTION_SAFE_CASES: tuple[tuple[str, int], ...] = (
    ("'; DROP TABLE users; --", 9081,),
    ('%27%3B%20DROP%20TABLE%20users%3B%20--', 9082,),
    ("'; DROP TABLE users; --", 9083,),
    ('\\u0027; DROP TABLE users; --', 9084,),
    ("' OR 1=1 --", 9085,),
    ('%27%20OR%201%3D1%20--', 9086,),
    ("' OR 1=1 --", 9087,),
    ('\\u0027 OR 1=1 --', 9088,),
    ('<script>alert(1)</script>', 9089,),
    ('%3Cscript%3Ealert%281%29%3C/script%3E', 9090,),
    ('&#60;script&#62;alert(1)&#60;/script&#62;', 9091,),
    ('<script>alert(1)</script>', 9092,),
    ('{{ 7 * 7 }}', 9093,),
    ('%7B%7B%207%20%2A%207%20%7D%7D', 9094,),
    ('{{ 7 * 7 }}', 9095,),
    ('{{ 7 * 7 }}', 9096,),
    ('${7*7}', 9097,),
    ('%24%7B7%2A7%7D', 9098,),
    ('${7*7}', 9099,),
    ('${7*7}', 9100,),
    ('javascript:alert(1)', 9101,),
    ('javascript%3Aalert%281%29', 9102,),
    ('javascript:alert(1)', 9103,),
    ('javascript:alert(1)', 9104,),
    ('SELECT * FROM users WHERE 1=1', 9105,),
    ('SELECT%20%2A%20FROM%20users%20WHERE%201%3D1', 9106,),
    ('SELECT * FROM users WHERE 1=1', 9107,),
    ('SELECT * FROM users WHERE 1=1', 9108,),
    ('UNION SELECT password FROM admin --', 9109,),
    ('UNION%20SELECT%20password%20FROM%20admin%20--', 9110,),
    ('UNION SELECT password FROM admin --', 9111,),
    ('UNION SELECT password FROM admin --', 9112,),
    ("x' OR '1'='1", 9113,),
    ('x%27%20OR%20%271%27%3D%271', 9114,),
    ("x' OR '1'='1", 9115,),
    ('x\\u0027 OR \\u00271\\u0027=\\u00271', 9116,),
    ("'; EXEC xp_cmdshell('dir'); --", 9117,),
    ('%27%3B%20EXEC%20xp_cmdshell%28%27dir%27%29%3B%20--', 9118,),
    ("'; EXEC xp_cmdshell('dir'); --", 9119,),
    ('\\u0027; EXEC xp_cmdshell(\\u0027dir\\u0027); --', 9120,),
    ("<!--#exec cmd='ls' -->", 9121,),
    ('%3C%21--%23exec%20cmd%3D%27ls%27%20--%3E', 9122,),
    ("&#60;!--#exec cmd='ls' --&#62;", 9123,),
    ('<!--#exec cmd=\\u0027ls\\u0027 -->', 9124,),
    ('cmd | sh -i', 9125,),
    ('cmd%20%7C%20sh%20-i', 9126,),
    ('cmd | sh -i', 9127,),
    ('cmd | sh -i', 9128,),
    ('`whoami`', 9129,),
    ('%60whoami%60', 9130,),
    ('`whoami`', 9131,),
    ('`whoami`', 9132,),
    ('$(cat /etc/passwd)', 9133,),
    ('%24%28cat%20/etc/passwd%29', 9134,),
    ('$(cat /etc/passwd)', 9135,),
    ('$(cat /etc/passwd)', 9136,),
    ('%3Cscript%3Ealert(1)%3C/script%3E', 9137,),
    ('%253Cscript%253Ealert%281%29%253C/script%253E', 9138,),
    ('%3Cscript%3Ealert(1)%3C/script%3E', 9139,),
    ('%3Cscript%3Ealert(1)%3C/script%3E', 9140,),
    ('\\u003cscript\\u003e', 9141,),
    ('%5Cu003cscript%5Cu003e', 9142,),
    ('\\u003cscript\\u003e', 9143,),
    ('\\u003cscript\\u003e', 9144,),
    ('&#60;script&#62;', 9145,),
    ('%26%2360%3Bscript%26%2362%3B', 9146,),
    ('&#60;script&#62;', 9147,),
    ('&#60;script&#62;', 9148,),
    ("'''''''''''", 9149,),
    ('%27%27%27%27%27%27%27%27%27%27%27', 9150,),
    ("'''''''''''", 9151,),
    ('\\u0027\\u0027\\u0027\\u0027\\u0027\\u0027\\u0027\\u0027\\u0027\\u0027\\u0027', 9152,),
    ('1; DROP TABLE', 9153,),
    ('1%3B%20DROP%20TABLE', 9154,),
    ('1; DROP TABLE', 9155,),
    ('1; DROP TABLE', 9156,),
    ('../../../etc/passwd', 9157,),
    ('../../../etc/passwd', 9158,),
    ('../../../etc/passwd', 9159,),
    ('../../../etc/passwd', 9160,),
    ('C:\\boot.ini', 9161,),
    ('C%3A%5Cboot.ini', 9162,),
    ('C:\\boot.ini', 9163,),
    ('C:\\boot.ini', 9164,),
    ("<IMG SRC=javascript:alert('XSS')>", 9165,),
    ('%3CIMG%20SRC%3Djavascript%3Aalert%28%27XSS%27%29%3E', 9166,),
    ("&#60;IMG SRC=javascript:alert('XSS')&#62;", 9167,),
    ('<IMG SRC=javascript:alert(\\u0027XSS\\u0027)>', 9168,),
    ('<svg onload=alert(1)>', 9169,),
    ('%3Csvg%20onload%3Dalert%281%29%3E', 9170,),
    ('&#60;svg onload=alert(1)&#62;', 9171,),
    ('<svg onload=alert(1)>', 9172,),
    ('<iframe src=evil>', 9173,),
    ('%3Ciframe%20src%3Devil%3E', 9174,),
    ('&#60;iframe src=evil&#62;', 9175,),
    ('<iframe src=evil>', 9176,),
    ("SELECT 'a' AS b WHERE 1=1 UNION SELECT NULL", 9177,),
    ('SELECT%20%27a%27%20AS%20b%20WHERE%201%3D1%20UNION%20SELECT%20NULL', 9178,),
    ("SELECT 'a' AS b WHERE 1=1 UNION SELECT NULL", 9179,),
    ('SELECT \\u0027a\\u0027 AS b WHERE 1=1 UNION SELECT NULL', 9180,),
)

class TestInjectionSafe(BaseTest):
    """Injection payloads never crash the moderator."""

    @pytest.mark.parametrize(('payload', 'uid',), _INJECTION_SAFE_CASES)
    def test_injection_safe(self, client: Any, payload: str, uid: int) -> None:
        """Injection payloads never crash the moderator."""
        response = client.post('/moderate', json={'text': payload, 'app_name': 'a'})
        assert response.status_code == 200
        assert response.json()['verdict'] in ('PASS', 'BLOCK', 'REVIEW')
