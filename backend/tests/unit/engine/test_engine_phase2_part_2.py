"""Phase 2 engine pipeline tests (generated).

Golden verdict matrices, cache and batch properties, app policies and
component invariants; see tests/tools/phase2_generator.py."""

# multilingual fixtures use non-ASCII on purpose
from __future__ import annotations

from typing import Any

import pytest

from app.engine.moderation_engine import ModerationEngine
from app.models.request import ModerationRequest
from app.models.response import ModerationResponse
from tests.base_test import BaseTest

_VERDICT_EXACT_MATRIX_CASES: tuple[tuple[str, str, int, str, int, int], ...] = (
    ('you are a zaphrin here', 'zaphrin', 0, 'BLOCK', 2, 1301,),
    ('you are a zaphrin here', 'zaphrin', 10, 'BLOCK', 2, 1303,),
    ('you are a zaphrin here', 'zaphrin', 30, 'BLOCK', 2, 1305,),
    ('you are a zaphrin here', 'zaphrin', 50, 'BLOCK', 2, 1307,),
    ('you are a zaphrin here', 'zaphrin', 70, 'BLOCK', 1, 1309,),
    ('you are a zaphrin here', 'zaphrin', 100, 'BLOCK', 1, 1311,),
    ('you are a blorp here', 'blorp', 0, 'BLOCK', 2, 1313,),
    ('you are a blorp here', 'blorp', 10, 'BLOCK', 2, 1315,),
    ('you are a blorp here', 'blorp', 30, 'BLOCK', 2, 1317,),
    ('you are a blorp here', 'blorp', 50, 'BLOCK', 2, 1319,),
    ('you are a blorp here', 'blorp', 70, 'BLOCK', 1, 1321,),
    ('you are a blorp here', 'blorp', 100, 'BLOCK', 1, 1323,),
    ('you are a flubber here', 'flubber', 0, 'BLOCK', 2, 1325,),
    ('you are a flubber here', 'flubber', 10, 'BLOCK', 2, 1327,),
    ('you are a flubber here', 'flubber', 30, 'BLOCK', 2, 1329,),
    ('you are a flubber here', 'flubber', 50, 'BLOCK', 2, 1331,),
    ('you are a flubber here', 'flubber', 70, 'BLOCK', 1, 1333,),
    ('you are a flubber here', 'flubber', 100, 'BLOCK', 1, 1335,),
    ('you are a quxxle here', 'quxxle', 0, 'BLOCK', 2, 1337,),
    ('you are a quxxle here', 'quxxle', 10, 'BLOCK', 2, 1339,),
    ('you are a quxxle here', 'quxxle', 30, 'BLOCK', 2, 1341,),
    ('you are a quxxle here', 'quxxle', 50, 'BLOCK', 2, 1343,),
    ('you are a quxxle here', 'quxxle', 70, 'BLOCK', 1, 1345,),
    ('you are a quxxle here', 'quxxle', 100, 'BLOCK', 1, 1347,),
    ('you are a wombat here', 'wombat', 0, 'BLOCK', 2, 1349,),
    ('you are a wombat here', 'wombat', 10, 'BLOCK', 2, 1351,),
    ('you are a wombat here', 'wombat', 30, 'BLOCK', 2, 1353,),
    ('you are a wombat here', 'wombat', 50, 'BLOCK', 2, 1355,),
    ('you are a wombat here', 'wombat', 70, 'BLOCK', 1, 1357,),
    ('you are a wombat here', 'wombat', 100, 'BLOCK', 1, 1359,),
    ('you are a giblet here', 'giblet', 0, 'BLOCK', 2, 1361,),
    ('you are a giblet here', 'giblet', 10, 'BLOCK', 2, 1363,),
    ('you are a giblet here', 'giblet', 30, 'BLOCK', 2, 1365,),
    ('you are a giblet here', 'giblet', 50, 'BLOCK', 2, 1367,),
    ('you are a giblet here', 'giblet', 70, 'BLOCK', 1, 1369,),
    ('you are a giblet here', 'giblet', 100, 'BLOCK', 1, 1371,),
    ('you are a snarg here', 'snarg', 0, 'BLOCK', 2, 1373,),
    ('you are a snarg here', 'snarg', 10, 'BLOCK', 2, 1375,),
    ('you are a snarg here', 'snarg', 30, 'BLOCK', 2, 1377,),
    ('you are a snarg here', 'snarg', 50, 'BLOCK', 2, 1379,),
    ('you are a snarg here', 'snarg', 70, 'BLOCK', 1, 1381,),
    ('you are a snarg here', 'snarg', 100, 'BLOCK', 1, 1383,),
    ('you are a zorp here', 'zorp', 0, 'BLOCK', 2, 1385,),
    ('you are a zorp here', 'zorp', 10, 'BLOCK', 2, 1387,),
    ('you are a zorp here', 'zorp', 30, 'BLOCK', 2, 1389,),
    ('you are a zorp here', 'zorp', 50, 'BLOCK', 2, 1391,),
    ('you are a zorp here', 'zorp', 70, 'BLOCK', 1, 1393,),
    ('you are a zorp here', 'zorp', 100, 'BLOCK', 1, 1395,),
)

class TestVerdictExactMatrix(BaseTest):
    """Exact matches resolve deterministically at every threshold."""

    @pytest.mark.parametrize(('text', 'word', 'threshold', 'expected', 'level', 'uid',), _VERDICT_EXACT_MATRIX_CASES)
    def test_verdict_exact_matrix(self, engine: ModerationEngine, word_bank: Any, text: str, word: str, threshold: int, expected: str, level: int, uid: int) -> None:
        """Exact matches resolve deterministically at every threshold."""
        word_bank.add_word(word)
        engine.refresh_detectors()
        engine._app_config.update_default_threshold(threshold)
        result: ModerationResponse = engine.moderate(
            ModerationRequest(text=text, app_name='a', user_id='u')
        )
        assert result.verdict.value == expected
        assert result.level_used == level


_VERDICT_TYPO_MATRIX_CASES: tuple[tuple[str, str, int, str, int, int], ...] = (
    ('you are a zaphri here', 'zaphrin', 0, 'REVIEW', 2, 1302,),
    ('you are a zaphri here', 'zaphrin', 10, 'REVIEW', 2, 1304,),
    ('you are a zaphri here', 'zaphrin', 30, 'PASS', 1, 1306,),
    ('you are a zaphri here', 'zaphrin', 50, 'PASS', 1, 1308,),
    ('you are a zaphri here', 'zaphrin', 70, 'PASS', 1, 1310,),
    ('you are a zaphri here', 'zaphrin', 100, 'PASS', 1, 1312,),
    ('you are a blor here', 'blorp', 0, 'REVIEW', 2, 1314,),
    ('you are a blor here', 'blorp', 10, 'REVIEW', 2, 1316,),
    ('you are a blor here', 'blorp', 30, 'PASS', 1, 1318,),
    ('you are a blor here', 'blorp', 50, 'PASS', 1, 1320,),
    ('you are a blor here', 'blorp', 70, 'PASS', 1, 1322,),
    ('you are a blor here', 'blorp', 100, 'PASS', 1, 1324,),
    ('you are a flubbe here', 'flubber', 0, 'REVIEW', 2, 1326,),
    ('you are a flubbe here', 'flubber', 10, 'REVIEW', 2, 1328,),
    ('you are a flubbe here', 'flubber', 30, 'PASS', 1, 1330,),
    ('you are a flubbe here', 'flubber', 50, 'PASS', 1, 1332,),
    ('you are a flubbe here', 'flubber', 70, 'PASS', 1, 1334,),
    ('you are a flubbe here', 'flubber', 100, 'PASS', 1, 1336,),
    ('you are a quxxl here', 'quxxle', 0, 'REVIEW', 2, 1338,),
    ('you are a quxxl here', 'quxxle', 10, 'REVIEW', 2, 1340,),
    ('you are a quxxl here', 'quxxle', 30, 'PASS', 1, 1342,),
    ('you are a quxxl here', 'quxxle', 50, 'PASS', 1, 1344,),
    ('you are a quxxl here', 'quxxle', 70, 'PASS', 1, 1346,),
    ('you are a quxxl here', 'quxxle', 100, 'PASS', 1, 1348,),
    ('you are a womba here', 'wombat', 0, 'REVIEW', 2, 1350,),
    ('you are a womba here', 'wombat', 10, 'REVIEW', 2, 1352,),
    ('you are a womba here', 'wombat', 30, 'PASS', 1, 1354,),
    ('you are a womba here', 'wombat', 50, 'PASS', 1, 1356,),
    ('you are a womba here', 'wombat', 70, 'PASS', 1, 1358,),
    ('you are a womba here', 'wombat', 100, 'PASS', 1, 1360,),
    ('you are a gible here', 'giblet', 0, 'REVIEW', 2, 1362,),
    ('you are a gible here', 'giblet', 10, 'REVIEW', 2, 1364,),
    ('you are a gible here', 'giblet', 30, 'PASS', 1, 1366,),
    ('you are a gible here', 'giblet', 50, 'PASS', 1, 1368,),
    ('you are a gible here', 'giblet', 70, 'PASS', 1, 1370,),
    ('you are a gible here', 'giblet', 100, 'PASS', 1, 1372,),
    ('you are a snar here', 'snarg', 0, 'REVIEW', 2, 1374,),
    ('you are a snar here', 'snarg', 10, 'REVIEW', 2, 1376,),
    ('you are a snar here', 'snarg', 30, 'PASS', 1, 1378,),
    ('you are a snar here', 'snarg', 50, 'PASS', 1, 1380,),
    ('you are a snar here', 'snarg', 70, 'PASS', 1, 1382,),
    ('you are a snar here', 'snarg', 100, 'PASS', 1, 1384,),
    ('you are a zor here', 'zorp', 0, 'REVIEW', 2, 1386,),
    ('you are a zor here', 'zorp', 10, 'REVIEW', 2, 1388,),
    ('you are a zor here', 'zorp', 30, 'PASS', 1, 1390,),
    ('you are a zor here', 'zorp', 50, 'PASS', 1, 1392,),
    ('you are a zor here', 'zorp', 70, 'PASS', 1, 1394,),
    ('you are a zor here', 'zorp', 100, 'PASS', 1, 1396,),
)

class TestVerdictTypoMatrix(BaseTest):
    """Near-miss tokens resolve deterministically at every threshold."""

    @pytest.mark.parametrize(('text', 'word', 'threshold', 'expected', 'level', 'uid',), _VERDICT_TYPO_MATRIX_CASES)
    def test_verdict_typo_matrix(self, engine: ModerationEngine, word_bank: Any, text: str, word: str, threshold: int, expected: str, level: int, uid: int) -> None:
        """Near-miss tokens resolve deterministically at every threshold."""
        word_bank.add_word(word)
        engine.refresh_detectors()
        engine._app_config.update_default_threshold(threshold)
        result: ModerationResponse = engine.moderate(
            ModerationRequest(text=text, app_name='a', user_id='u')
        )
        assert result.verdict.value == expected
        assert result.level_used == level


_CACHE_BOUNDED_CASES: tuple[tuple[int, int], ...] = (
    (1, 1397,),
    (2, 1398,),
    (3, 1399,),
    (5, 1400,),
)

class TestCacheBounded(BaseTest):
    """The result cache never exceeds its configured size."""

    @pytest.mark.parametrize(('n_texts', 'uid',), _CACHE_BOUNDED_CASES)
    def test_cache_bounded(self, engine: ModerationEngine, n_texts: int, uid: int) -> None:
        """The result cache never exceeds its configured size."""
        for index in range(n_texts):
            engine.moderate(ModerationRequest(text=f'cache seed {index}', app_name='a'))
        assert len(engine._cache) == min(n_texts, engine._cache_max_size)
        assert engine._cache_max_size > 0
