"""Phase 2 public moderation API tests (generated).

Language verdict matrices, batch sizes, validation, unicode edges,
profiling flows and response shapes; see tests/tools/phase2_generator.py."""

# multilingual fixtures use non-ASCII on purpose
from __future__ import annotations

from typing import Any

import pytest

from tests.base_test import BaseTest

_PROFILING_FLOW_CASES: tuple[tuple[str, str, int], ...] = (
    ('pubuser0', 'profile 0', 7216,),
    ('pubuser1', 'profile 1', 7217,),
    ('pubuser2', 'profile 2', 7218,),
    ('pubuser3', 'profile 3', 7219,),
    ('pubuser4', 'profile 4', 7220,),
    ('pubuser5', 'profile 5', 7221,),
    ('pubuser6', 'profile 6', 7222,),
    ('pubuser7', 'profile 7', 7223,),
    ('pubuser8', 'profile 8', 7224,),
    ('pubuser9', 'profile 9', 7225,),
    ('pubuser10', 'profile 10', 7226,),
    ('pubuser11', 'profile 11', 7227,),
    ('pubuser12', 'profile 12', 7228,),
    ('pubuser13', 'profile 13', 7229,),
    ('pubuser14', 'profile 14', 7230,),
    ('pubuser15', 'profile 15', 7231,),
    ('pubuser16', 'profile 16', 7232,),
    ('pubuser17', 'profile 17', 7233,),
    ('pubuser18', 'profile 18', 7234,),
    ('pubuser19', 'profile 19', 7235,),
    ('pubuser20', 'profile 20', 7236,),
    ('pubuser21', 'profile 21', 7237,),
    ('pubuser22', 'profile 22', 7238,),
    ('pubuser23', 'profile 23', 7239,),
    ('pubuser24', 'profile 24', 7240,),
    ('pubuser25', 'profile 25', 7241,),
    ('pubuser26', 'profile 26', 7242,),
    ('pubuser27', 'profile 27', 7243,),
    ('pubuser28', 'profile 28', 7244,),
    ('pubuser29', 'profile 29', 7245,),
    ('pubuser30', 'profile 30', 7246,),
    ('pubuser31', 'profile 31', 7247,),
    ('pubuser32', 'profile 32', 7248,),
    ('pubuser33', 'profile 33', 7249,),
    ('pubuser34', 'profile 34', 7250,),
    ('pubuser35', 'profile 35', 7251,),
    ('pubuser36', 'profile 36', 7252,),
    ('pubuser37', 'profile 37', 7253,),
    ('pubuser38', 'profile 38', 7254,),
    ('pubuser39', 'profile 39', 7255,),
    ('pubuser40', 'profile 40', 7256,),
    ('pubuser41', 'profile 41', 7257,),
    ('pubuser42', 'profile 42', 7258,),
    ('pubuser43', 'profile 43', 7259,),
    ('pubuser44', 'profile 44', 7260,),
    ('pubuser45', 'profile 45', 7261,),
    ('pubuser46', 'profile 46', 7262,),
    ('pubuser47', 'profile 47', 7263,),
    ('pubuser48', 'profile 48', 7264,),
    ('pubuser49', 'profile 49', 7265,),
    ('pubuser50', 'profile 50', 7266,),
    ('pubuser51', 'profile 51', 7267,),
    ('pubuser52', 'profile 52', 7268,),
    ('pubuser53', 'profile 53', 7269,),
    ('pubuser54', 'profile 54', 7270,),
    ('pubuser55', 'profile 55', 7271,),
    ('pubuser56', 'profile 56', 7272,),
    ('pubuser57', 'profile 57', 7273,),
    ('pubuser58', 'profile 58', 7274,),
    ('pubuser59', 'profile 59', 7275,),
    ('pubuser60', 'profile 60', 7276,),
    ('pubuser61', 'profile 61', 7277,),
    ('pubuser62', 'profile 62', 7278,),
    ('pubuser63', 'profile 63', 7279,),
    ('pubuser64', 'profile 64', 7280,),
    ('pubuser65', 'profile 65', 7281,),
    ('pubuser66', 'profile 66', 7282,),
    ('pubuser67', 'profile 67', 7283,),
    ('pubuser68', 'profile 68', 7284,),
    ('pubuser69', 'profile 69', 7285,),
    ('pubuser70', 'profile 70', 7286,),
    ('pubuser71', 'profile 71', 7287,),
    ('pubuser72', 'profile 72', 7288,),
    ('pubuser73', 'profile 73', 7289,),
    ('pubuser74', 'profile 74', 7290,),
    ('pubuser75', 'profile 75', 7291,),
    ('pubuser76', 'profile 76', 7292,),
    ('pubuser77', 'profile 77', 7293,),
    ('pubuser78', 'profile 78', 7294,),
    ('pubuser79', 'profile 79', 7295,),
    ('pubuser80', 'profile 80', 7296,),
    ('pubuser81', 'profile 81', 7297,),
    ('pubuser82', 'profile 82', 7298,),
    ('pubuser83', 'profile 83', 7299,),
    ('pubuser84', 'profile 84', 7300,),
    ('pubuser85', 'profile 85', 7301,),
    ('pubuser86', 'profile 86', 7302,),
    ('pubuser87', 'profile 87', 7303,),
    ('pubuser88', 'profile 88', 7304,),
    ('pubuser89', 'profile 89', 7305,),
    ('pubuser90', 'profile 90', 7306,),
    ('pubuser91', 'profile 91', 7307,),
    ('pubuser92', 'profile 92', 7308,),
    ('pubuser93', 'profile 93', 7309,),
    ('pubuser94', 'profile 94', 7310,),
    ('pubuser95', 'profile 95', 7311,),
    ('pubuser96', 'profile 96', 7312,),
    ('pubuser97', 'profile 97', 7313,),
    ('pubuser98', 'profile 98', 7314,),
    ('pubuser99', 'profile 99', 7315,),
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
