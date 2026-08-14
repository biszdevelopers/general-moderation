"""Phase 2 security tests (generated).

Header parity, CORS, auth bypass, injection, traversal, method
restrictions and encoded payloads; see tests/tools/phase2_generator.py."""

# multilingual fixtures use non-ASCII on purpose
from __future__ import annotations

from typing import Any

import pytest

from tests.base_test import BaseTest

_INJECTION_SAFE_CASES: tuple[tuple[str, int], ...] = (
    ("'; DROP TABLE users; --", 9041,),
    ('%27%3B%20DROP%20TABLE%20users%3B%20--', 9042,),
    ("'; DROP TABLE users; --", 9043,),
    ('\\u0027; DROP TABLE users; --', 9044,),
    ("' OR 1=1 --", 9045,),
    ('%27%20OR%201%3D1%20--', 9046,),
    ("' OR 1=1 --", 9047,),
    ('\\u0027 OR 1=1 --', 9048,),
    ('<script>alert(1)</script>', 9049,),
    ('%3Cscript%3Ealert%281%29%3C/script%3E', 9050,),
    ('&#60;script&#62;alert(1)&#60;/script&#62;', 9051,),
    ('<script>alert(1)</script>', 9052,),
    ('{{ 7 * 7 }}', 9053,),
    ('%7B%7B%207%20%2A%207%20%7D%7D', 9054,),
    ('{{ 7 * 7 }}', 9055,),
    ('{{ 7 * 7 }}', 9056,),
    ('${7*7}', 9057,),
    ('%24%7B7%2A7%7D', 9058,),
    ('${7*7}', 9059,),
    ('${7*7}', 9060,),
    ('javascript:alert(1)', 9061,),
    ('javascript%3Aalert%281%29', 9062,),
    ('javascript:alert(1)', 9063,),
    ('javascript:alert(1)', 9064,),
    ('SELECT * FROM users WHERE 1=1', 9065,),
    ('SELECT%20%2A%20FROM%20users%20WHERE%201%3D1', 9066,),
    ('SELECT * FROM users WHERE 1=1', 9067,),
    ('SELECT * FROM users WHERE 1=1', 9068,),
    ('UNION SELECT password FROM admin --', 9069,),
    ('UNION%20SELECT%20password%20FROM%20admin%20--', 9070,),
    ('UNION SELECT password FROM admin --', 9071,),
    ('UNION SELECT password FROM admin --', 9072,),
    ("x' OR '1'='1", 9073,),
    ('x%27%20OR%20%271%27%3D%271', 9074,),
    ("x' OR '1'='1", 9075,),
    ('x\\u0027 OR \\u00271\\u0027=\\u00271', 9076,),
    ("'; EXEC xp_cmdshell('dir'); --", 9077,),
    ('%27%3B%20EXEC%20xp_cmdshell%28%27dir%27%29%3B%20--', 9078,),
    ("'; EXEC xp_cmdshell('dir'); --", 9079,),
    ('\\u0027; EXEC xp_cmdshell(\\u0027dir\\u0027); --', 9080,),
    ("<!--#exec cmd='ls' -->", 9081,),
    ('%3C%21--%23exec%20cmd%3D%27ls%27%20--%3E', 9082,),
    ("&#60;!--#exec cmd='ls' --&#62;", 9083,),
    ('<!--#exec cmd=\\u0027ls\\u0027 -->', 9084,),
    ('cmd | sh -i', 9085,),
    ('cmd%20%7C%20sh%20-i', 9086,),
    ('cmd | sh -i', 9087,),
    ('cmd | sh -i', 9088,),
    ('`whoami`', 9089,),
    ('%60whoami%60', 9090,),
    ('`whoami`', 9091,),
    ('`whoami`', 9092,),
    ('$(cat /etc/passwd)', 9093,),
    ('%24%28cat%20/etc/passwd%29', 9094,),
    ('$(cat /etc/passwd)', 9095,),
    ('$(cat /etc/passwd)', 9096,),
    ('%3Cscript%3Ealert(1)%3C/script%3E', 9097,),
    ('%253Cscript%253Ealert%281%29%253C/script%253E', 9098,),
    ('%3Cscript%3Ealert(1)%3C/script%3E', 9099,),
    ('%3Cscript%3Ealert(1)%3C/script%3E', 9100,),
    ('\\u003cscript\\u003e', 9101,),
    ('%5Cu003cscript%5Cu003e', 9102,),
    ('\\u003cscript\\u003e', 9103,),
    ('\\u003cscript\\u003e', 9104,),
    ('&#60;script&#62;', 9105,),
    ('%26%2360%3Bscript%26%2362%3B', 9106,),
    ('&#60;script&#62;', 9107,),
    ('&#60;script&#62;', 9108,),
    ("'''''''''''", 9109,),
    ('%27%27%27%27%27%27%27%27%27%27%27', 9110,),
    ("'''''''''''", 9111,),
    ('\\u0027\\u0027\\u0027\\u0027\\u0027\\u0027\\u0027\\u0027\\u0027\\u0027\\u0027', 9112,),
    ('1; DROP TABLE', 9113,),
    ('1%3B%20DROP%20TABLE', 9114,),
    ('1; DROP TABLE', 9115,),
    ('1; DROP TABLE', 9116,),
    ('../../../etc/passwd', 9117,),
    ('../../../etc/passwd', 9118,),
    ('../../../etc/passwd', 9119,),
    ('../../../etc/passwd', 9120,),
    ('C:\\boot.ini', 9121,),
    ('C%3A%5Cboot.ini', 9122,),
    ('C:\\boot.ini', 9123,),
    ('C:\\boot.ini', 9124,),
    ("<IMG SRC=javascript:alert('XSS')>", 9125,),
    ('%3CIMG%20SRC%3Djavascript%3Aalert%28%27XSS%27%29%3E', 9126,),
    ("&#60;IMG SRC=javascript:alert('XSS')&#62;", 9127,),
    ('<IMG SRC=javascript:alert(\\u0027XSS\\u0027)>', 9128,),
    ('<svg onload=alert(1)>', 9129,),
    ('%3Csvg%20onload%3Dalert%281%29%3E', 9130,),
    ('&#60;svg onload=alert(1)&#62;', 9131,),
    ('<svg onload=alert(1)>', 9132,),
    ('<iframe src=evil>', 9133,),
    ('%3Ciframe%20src%3Devil%3E', 9134,),
    ('&#60;iframe src=evil&#62;', 9135,),
    ('<iframe src=evil>', 9136,),
    ("SELECT 'a' AS b WHERE 1=1 UNION SELECT NULL", 9137,),
    ('SELECT%20%27a%27%20AS%20b%20WHERE%201%3D1%20UNION%20SELECT%20NULL', 9138,),
    ("SELECT 'a' AS b WHERE 1=1 UNION SELECT NULL", 9139,),
    ('SELECT \\u0027a\\u0027 AS b WHERE 1=1 UNION SELECT NULL', 9140,),
)

class TestInjectionSafe(BaseTest):
    """Injection payloads never crash the moderator."""

    @pytest.mark.parametrize(('payload', 'uid',), _INJECTION_SAFE_CASES)
    def test_injection_safe(self, client: Any, payload: str, uid: int) -> None:
        """Injection payloads never crash the moderator."""
        response = client.post('/moderate', json={'text': payload, 'app_name': 'a'})
        assert response.status_code == 200
        assert response.json()['verdict'] in ('PASS', 'BLOCK', 'REVIEW')
