"""Phase 2 public moderation API tests (generated).

Language verdict matrices, batch sizes, validation, unicode edges,
profiling flows and response shapes; see tests/tools/phase2_generator.py."""

# multilingual fixtures use non-ASCII on purpose
from __future__ import annotations

from typing import Any

import pytest

from tests.base_test import BaseTest

_PROFILING_FLOW_CASES: tuple[tuple[str, str, int], ...] = (
    ('pubuser0', 'profile 0', 7176,),
    ('pubuser1', 'profile 1', 7177,),
    ('pubuser2', 'profile 2', 7178,),
    ('pubuser3', 'profile 3', 7179,),
    ('pubuser4', 'profile 4', 7180,),
    ('pubuser5', 'profile 5', 7181,),
    ('pubuser6', 'profile 6', 7182,),
    ('pubuser7', 'profile 7', 7183,),
    ('pubuser8', 'profile 8', 7184,),
    ('pubuser9', 'profile 9', 7185,),
    ('pubuser10', 'profile 10', 7186,),
    ('pubuser11', 'profile 11', 7187,),
    ('pubuser12', 'profile 12', 7188,),
    ('pubuser13', 'profile 13', 7189,),
    ('pubuser14', 'profile 14', 7190,),
    ('pubuser15', 'profile 15', 7191,),
    ('pubuser16', 'profile 16', 7192,),
    ('pubuser17', 'profile 17', 7193,),
    ('pubuser18', 'profile 18', 7194,),
    ('pubuser19', 'profile 19', 7195,),
    ('pubuser20', 'profile 20', 7196,),
    ('pubuser21', 'profile 21', 7197,),
    ('pubuser22', 'profile 22', 7198,),
    ('pubuser23', 'profile 23', 7199,),
    ('pubuser24', 'profile 24', 7200,),
    ('pubuser25', 'profile 25', 7201,),
    ('pubuser26', 'profile 26', 7202,),
    ('pubuser27', 'profile 27', 7203,),
    ('pubuser28', 'profile 28', 7204,),
    ('pubuser29', 'profile 29', 7205,),
    ('pubuser30', 'profile 30', 7206,),
    ('pubuser31', 'profile 31', 7207,),
    ('pubuser32', 'profile 32', 7208,),
    ('pubuser33', 'profile 33', 7209,),
    ('pubuser34', 'profile 34', 7210,),
    ('pubuser35', 'profile 35', 7211,),
    ('pubuser36', 'profile 36', 7212,),
    ('pubuser37', 'profile 37', 7213,),
    ('pubuser38', 'profile 38', 7214,),
    ('pubuser39', 'profile 39', 7215,),
    ('pubuser40', 'profile 40', 7216,),
    ('pubuser41', 'profile 41', 7217,),
    ('pubuser42', 'profile 42', 7218,),
    ('pubuser43', 'profile 43', 7219,),
    ('pubuser44', 'profile 44', 7220,),
    ('pubuser45', 'profile 45', 7221,),
    ('pubuser46', 'profile 46', 7222,),
    ('pubuser47', 'profile 47', 7223,),
    ('pubuser48', 'profile 48', 7224,),
    ('pubuser49', 'profile 49', 7225,),
    ('pubuser50', 'profile 50', 7226,),
    ('pubuser51', 'profile 51', 7227,),
    ('pubuser52', 'profile 52', 7228,),
    ('pubuser53', 'profile 53', 7229,),
    ('pubuser54', 'profile 54', 7230,),
    ('pubuser55', 'profile 55', 7231,),
    ('pubuser56', 'profile 56', 7232,),
    ('pubuser57', 'profile 57', 7233,),
    ('pubuser58', 'profile 58', 7234,),
    ('pubuser59', 'profile 59', 7235,),
    ('pubuser60', 'profile 60', 7236,),
    ('pubuser61', 'profile 61', 7237,),
    ('pubuser62', 'profile 62', 7238,),
    ('pubuser63', 'profile 63', 7239,),
    ('pubuser64', 'profile 64', 7240,),
    ('pubuser65', 'profile 65', 7241,),
    ('pubuser66', 'profile 66', 7242,),
    ('pubuser67', 'profile 67', 7243,),
    ('pubuser68', 'profile 68', 7244,),
    ('pubuser69', 'profile 69', 7245,),
    ('pubuser70', 'profile 70', 7246,),
    ('pubuser71', 'profile 71', 7247,),
    ('pubuser72', 'profile 72', 7248,),
    ('pubuser73', 'profile 73', 7249,),
    ('pubuser74', 'profile 74', 7250,),
    ('pubuser75', 'profile 75', 7251,),
    ('pubuser76', 'profile 76', 7252,),
    ('pubuser77', 'profile 77', 7253,),
    ('pubuser78', 'profile 78', 7254,),
    ('pubuser79', 'profile 79', 7255,),
    ('pubuser80', 'profile 80', 7256,),
    ('pubuser81', 'profile 81', 7257,),
    ('pubuser82', 'profile 82', 7258,),
    ('pubuser83', 'profile 83', 7259,),
    ('pubuser84', 'profile 84', 7260,),
    ('pubuser85', 'profile 85', 7261,),
    ('pubuser86', 'profile 86', 7262,),
    ('pubuser87', 'profile 87', 7263,),
    ('pubuser88', 'profile 88', 7264,),
    ('pubuser89', 'profile 89', 7265,),
    ('pubuser90', 'profile 90', 7266,),
    ('pubuser91', 'profile 91', 7267,),
    ('pubuser92', 'profile 92', 7268,),
    ('pubuser93', 'profile 93', 7269,),
    ('pubuser94', 'profile 94', 7270,),
    ('pubuser95', 'profile 95', 7271,),
    ('pubuser96', 'profile 96', 7272,),
    ('pubuser97', 'profile 97', 7273,),
    ('pubuser98', 'profile 98', 7274,),
    ('pubuser99', 'profile 99', 7275,),
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
