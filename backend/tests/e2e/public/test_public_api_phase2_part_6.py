"""Phase 2 public moderation API tests (generated).

Language verdict matrices, batch sizes, validation, unicode edges,
profiling flows and response shapes; see tests/tools/phase2_generator.py."""

# multilingual fixtures use non-ASCII on purpose
from __future__ import annotations

from typing import Any

import pytest

from tests.base_test import BaseTest

_PROFILING_FLOW_CASES: tuple[tuple[str, str, int], ...] = (
    ('pubuser0', 'profile 0', 7017,),
    ('pubuser1', 'profile 1', 7018,),
    ('pubuser2', 'profile 2', 7019,),
    ('pubuser3', 'profile 3', 7020,),
    ('pubuser4', 'profile 4', 7021,),
    ('pubuser5', 'profile 5', 7022,),
    ('pubuser6', 'profile 6', 7023,),
    ('pubuser7', 'profile 7', 7024,),
    ('pubuser8', 'profile 8', 7025,),
    ('pubuser9', 'profile 9', 7026,),
    ('pubuser10', 'profile 10', 7027,),
    ('pubuser11', 'profile 11', 7028,),
    ('pubuser12', 'profile 12', 7029,),
    ('pubuser13', 'profile 13', 7030,),
    ('pubuser14', 'profile 14', 7031,),
    ('pubuser15', 'profile 15', 7032,),
    ('pubuser16', 'profile 16', 7033,),
    ('pubuser17', 'profile 17', 7034,),
    ('pubuser18', 'profile 18', 7035,),
    ('pubuser19', 'profile 19', 7036,),
    ('pubuser20', 'profile 20', 7037,),
    ('pubuser21', 'profile 21', 7038,),
    ('pubuser22', 'profile 22', 7039,),
    ('pubuser23', 'profile 23', 7040,),
    ('pubuser24', 'profile 24', 7041,),
    ('pubuser25', 'profile 25', 7042,),
    ('pubuser26', 'profile 26', 7043,),
    ('pubuser27', 'profile 27', 7044,),
    ('pubuser28', 'profile 28', 7045,),
    ('pubuser29', 'profile 29', 7046,),
    ('pubuser30', 'profile 30', 7047,),
    ('pubuser31', 'profile 31', 7048,),
    ('pubuser32', 'profile 32', 7049,),
    ('pubuser33', 'profile 33', 7050,),
    ('pubuser34', 'profile 34', 7051,),
    ('pubuser35', 'profile 35', 7052,),
    ('pubuser36', 'profile 36', 7053,),
    ('pubuser37', 'profile 37', 7054,),
    ('pubuser38', 'profile 38', 7055,),
    ('pubuser39', 'profile 39', 7056,),
    ('pubuser40', 'profile 40', 7057,),
    ('pubuser41', 'profile 41', 7058,),
    ('pubuser42', 'profile 42', 7059,),
    ('pubuser43', 'profile 43', 7060,),
    ('pubuser44', 'profile 44', 7061,),
    ('pubuser45', 'profile 45', 7062,),
    ('pubuser46', 'profile 46', 7063,),
    ('pubuser47', 'profile 47', 7064,),
    ('pubuser48', 'profile 48', 7065,),
    ('pubuser49', 'profile 49', 7066,),
    ('pubuser50', 'profile 50', 7067,),
    ('pubuser51', 'profile 51', 7068,),
    ('pubuser52', 'profile 52', 7069,),
    ('pubuser53', 'profile 53', 7070,),
    ('pubuser54', 'profile 54', 7071,),
    ('pubuser55', 'profile 55', 7072,),
    ('pubuser56', 'profile 56', 7073,),
    ('pubuser57', 'profile 57', 7074,),
    ('pubuser58', 'profile 58', 7075,),
    ('pubuser59', 'profile 59', 7076,),
    ('pubuser60', 'profile 60', 7077,),
    ('pubuser61', 'profile 61', 7078,),
    ('pubuser62', 'profile 62', 7079,),
    ('pubuser63', 'profile 63', 7080,),
    ('pubuser64', 'profile 64', 7081,),
    ('pubuser65', 'profile 65', 7082,),
    ('pubuser66', 'profile 66', 7083,),
    ('pubuser67', 'profile 67', 7084,),
    ('pubuser68', 'profile 68', 7085,),
    ('pubuser69', 'profile 69', 7086,),
    ('pubuser70', 'profile 70', 7087,),
    ('pubuser71', 'profile 71', 7088,),
    ('pubuser72', 'profile 72', 7089,),
    ('pubuser73', 'profile 73', 7090,),
    ('pubuser74', 'profile 74', 7091,),
    ('pubuser75', 'profile 75', 7092,),
    ('pubuser76', 'profile 76', 7093,),
    ('pubuser77', 'profile 77', 7094,),
    ('pubuser78', 'profile 78', 7095,),
    ('pubuser79', 'profile 79', 7096,),
    ('pubuser80', 'profile 80', 7097,),
    ('pubuser81', 'profile 81', 7098,),
    ('pubuser82', 'profile 82', 7099,),
    ('pubuser83', 'profile 83', 7100,),
    ('pubuser84', 'profile 84', 7101,),
    ('pubuser85', 'profile 85', 7102,),
    ('pubuser86', 'profile 86', 7103,),
    ('pubuser87', 'profile 87', 7104,),
    ('pubuser88', 'profile 88', 7105,),
    ('pubuser89', 'profile 89', 7106,),
    ('pubuser90', 'profile 90', 7107,),
    ('pubuser91', 'profile 91', 7108,),
    ('pubuser92', 'profile 92', 7109,),
    ('pubuser93', 'profile 93', 7110,),
    ('pubuser94', 'profile 94', 7111,),
    ('pubuser95', 'profile 95', 7112,),
    ('pubuser96', 'profile 96', 7113,),
    ('pubuser97', 'profile 97', 7114,),
    ('pubuser98', 'profile 98', 7115,),
    ('pubuser99', 'profile 99', 7116,),
)

class TestProfilingFlow(BaseTest):
    """API moderation records user profiling rows."""

    @pytest.mark.parametrize(('user_id', 'text', 'uid',), _PROFILING_FLOW_CASES)
    def test_profiling_flow(self, client: Any, engine: Any, user_id: str, text: str, uid: int) -> None:
        """API moderation records user profiling rows."""
        client.post('/moderate', json={'text': text, 'app_name': 'app', 'user_id': user_id})
        profile = engine._profiler.get_profile('app', user_id)
        assert profile['daily']
        assert profile['daily'][0]['total_msgs'] >= 1
