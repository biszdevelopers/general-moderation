"""Phase 2 engine pipeline tests (generated).

Golden verdict matrices, cache and batch properties, app policies and
component invariants; see tests/tools/phase2_generator.py."""

# ruff: noqa: RUF001  # multilingual fixtures use non-ASCII on purpose
from __future__ import annotations

from typing import Any

import pytest

from app.detectors.rolling_hash_detector import RollingHashDetector
from app.engine.moderation_engine import ModerationEngine
from app.fastpath.safe_word_filter import SafeWordFilter
from app.models.request import BatchItem, BatchModerationRequest, ModerationRequest
from app.models.response import ModerationResponse
from app.scoring.suspicion_scorer import SuspicionScorer
from tests.base_test import BaseTest

_CACHE_BOUNDED_CASES: tuple[tuple[int, int], ...] = (
    (10, 1401,),
    (15, 1402,),
    (20, 1403,),
    (25, 1404,),
    (30, 1405,),
    (40, 1406,),
    (50, 1407,),
    (60, 1408,),
    (75, 1409,),
    (100, 1410,),
    (150, 1411,),
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


_BATCH_SIZE_CASES: tuple[tuple[int, int], ...] = (
    (2, 1412,),
    (5, 1413,),
    (10, 1414,),
    (25, 1415,),
    (50, 1416,),
    (75, 1417,),
    (100, 1418,),
)

class TestBatchSize(BaseTest):
    """A batch returns exactly one result per item."""

    @pytest.mark.parametrize(('size', 'uid',), _BATCH_SIZE_CASES)
    def test_batch_size(self, engine: ModerationEngine, size: int, uid: int) -> None:
        """A batch returns exactly one result per item."""
        batch: BatchModerationRequest = BatchModerationRequest(
            items=[BatchItem(id=f'i{i}', text=f'message {i}', app_name='a') for i in range(size)]
        )
        response = engine.moderate_batch(batch)
        assert len(response.results) == size
        assert [item.id for item in response.results] == [f'i{i}' for i in range(size)]
        assert response.total_latency_ms >= 0.0


_APP_POLICY_OR_CASES: tuple[tuple[str, int, str, str, int, int], ...] = (
    ('you are a zaphrin', 0, 'or', 'REVIEW', 2, 1419,),
    ('you are a zaphrin', 50, 'or', 'REVIEW', 2, 1420,),
    ('you are a zaphrin', 100, 'or', 'BLOCK', 1, 1421,),
)

class TestAppPolicyOr(BaseTest):
    """OR policies resolve deterministically."""

    @pytest.mark.parametrize(('text', 'threshold', 'logic', 'expected', 'level', 'uid',), _APP_POLICY_OR_CASES)
    def test_app_policy_or(self, engine: ModerationEngine, word_bank: Any, text: str, threshold: int, logic: str, expected: str, level: int, uid: int) -> None:
        """OR policies resolve deterministically."""
        word_bank.add_word('zaphrin')
        engine.refresh_detectors()
        engine._app_config.set('app', score_threshold=threshold, logic_type=logic)
        result: ModerationResponse = engine.moderate(
            ModerationRequest(text=text, app_name='app', user_id='u')
        )
        assert result.verdict.value == expected
        assert result.level_used == level


_APP_POLICY_AND_CASES: tuple[tuple[str, int, str, str, int, int], ...] = (
    ('you are a zaphrin', 0, 'and', 'BLOCK', 1, 1422,),
    ('you are a zaphrin', 50, 'and', 'BLOCK', 1, 1423,),
    ('you are a zaphrin', 100, 'and', 'BLOCK', 1, 1424,),
)

class TestAppPolicyAnd(BaseTest):
    """AND policies resolve deterministically."""

    @pytest.mark.parametrize(('text', 'threshold', 'logic', 'expected', 'level', 'uid',), _APP_POLICY_AND_CASES)
    def test_app_policy_and(self, engine: ModerationEngine, word_bank: Any, text: str, threshold: int, logic: str, expected: str, level: int, uid: int) -> None:
        """AND policies resolve deterministically."""
        word_bank.add_word('zaphrin')
        engine.refresh_detectors()
        engine._app_config.set('app', score_threshold=threshold, logic_type=logic)
        result: ModerationResponse = engine.moderate(
            ModerationRequest(text=text, app_name='app', user_id='u')
        )
        assert result.verdict.value == expected
        assert result.level_used == level


_SCORER_WEIGHT_CASES: tuple[tuple[str, int], ...] = (
    ('aho_corasick', 1425,),
    ('bk_tree', 1426,),
    ('double_metaphone', 1427,),
    ('multi_language', 1428,),
    ('rolling_hash', 1429,),
    ('bloom_filter', 1430,),
    ('badwords', 1431,),
    ('profanite', 1432,),
)

class TestScorerWeight(BaseTest):
    """Every registered detector weight resolves within the valid range."""

    @pytest.mark.parametrize(('detector', 'uid',), _SCORER_WEIGHT_CASES)
    def test_scorer_weight(self, engine: ModerationEngine, detector: str, uid: int) -> None:
        """Every registered detector weight resolves within the valid range."""
        scorer: SuspicionScorer = SuspicionScorer(engine._settings_service)
        weight = scorer.detector_weight(detector)
        assert 0 <= weight <= 50
        score = scorer.score(detector_names=[detector])
        assert score >= 0.0


_SCORER_SUM_CASES: tuple[tuple[tuple[object, ...], int], ...] = (
    (('aho_corasick', 'bk_tree',), 1433,),
    (('aho_corasick', 'bk_tree', 'double_metaphone',), 1434,),
    (('aho_corasick', 'bk_tree', 'double_metaphone', 'multi_language',), 1435,),
    (('aho_corasick', 'bk_tree', 'double_metaphone', 'multi_language', 'rolling_hash',), 1436,),
)

class TestScorerSum(BaseTest):
    """Multiple detector hits sum their configured weights."""

    @pytest.mark.parametrize(('names', 'uid',), _SCORER_SUM_CASES)
    def test_scorer_sum(self, engine: ModerationEngine, names: tuple[object, ...], uid: int) -> None:
        """Multiple detector hits sum their configured weights."""
        scorer: SuspicionScorer = SuspicionScorer(engine._settings_service)
        score = scorer.score(detector_names=names, user_ratio=0.0)
        expected = sum(scorer.detector_weight(n) for n in names)
        assert score == min(100.0, expected)
        assert score <= 100.0


_SAFE_LANGUAGE_CASES: tuple[tuple[str, int], ...] = (
    ('the weather is pleasant today', 1437,),
    ('今天天气不错', 1438,),
    ('今日は天気が良いです', 1439,),
    ('오늘 날씨가 좋아요', 1440,),
    ('сегодня хорошая погода', 1441,),
    ('hoy hace buen tiempo', 1442,),
    ("il fait beau aujourd'hui", 1443,),
    ('das wetter ist schön heute', 1444,),
    ('oggi il tempo è bello', 1445,),
    ('الطقس جميل اليوم', 1446,),
    ('आज मौसम अच्छा है', 1447,),
    ('bugün hava güzel', 1448,),
    ('o tempo está bom hoje', 1449,),
    ('het weer is mooi vandaag', 1450,),
    ('dzisiaj jest ładna pogoda', 1451,),
    ('сьогодні гарна погода', 1452,),
    ('dnes je hezké počasí', 1453,),
    ('σήμερα έχει καλό καιρό', 1454,),
    ('vädret är fint idag', 1455,),
    ('været er fint i dag', 1456,),
    ('vejret er dejligt i dag', 1457,),
    ('tänään on kaunis sää', 1458,),
    ('ma szép az idő', 1459,),
    ('astăzi este vreme frumoasă', 1460,),
    ('днес е хубаво време', 1461,),
    ('מזג האוויר נחמד היום', 1462,),
    ('วันนี้อากาศดี', 1463,),
)

class TestSafeLanguage(BaseTest):
    """Stage 1 language detection classifies the script."""

    @pytest.mark.parametrize(('text', 'uid',), _SAFE_LANGUAGE_CASES)
    def test_safe_language(self, engine: ModerationEngine, text: str, uid: int) -> None:
        """Stage 1 language detection classifies the script."""
        detected = SafeWordFilter.detect_language(text)
        import re
        assert re.match(r'^[a-z]{2,3}$', detected) is not None


_SAFE_FILTER_CASES: tuple[tuple[tuple[object, ...], tuple[object, ...], str, bool, str, bool, int], ...] = (
    (('alpha',), (), 'alpha', True, 'alpha gamma', False, 1464,),
    (('alpha',), ('alpha',), 'alpha', False, 'alpha gamma', False, 1465,),
    (('alpha', 'beta',), (), 'alpha beta', True, 'gamma', False, 1466,),
    (('alpha', 'beta',), ('alpha',), 'beta', True, 'alpha beta', False, 1467,),
    (('car', 'dog', 'fish',), (), 'car dog fish', True, 'car cat', False, 1468,),
    (('car', 'dog',), ('car',), 'dog', True, 'car', False, 1469,),
    (('safe', 'word', 'list',), ('word',), 'safe list', True, 'word', False, 1470,),
    (('hello', 'world',), ('hello', 'world',), 'hello world', False, 'hello', False, 1471,),
    (('one',), ('one',), 'one two', False, 'one', False, 1472,),
    (('two', 'three',), (), 'two three', True, 'three four', False, 1473,),
    (('alpha',), (), 'ALPHA', True, 'beta', False, 1474,),
    (('alpha',), (), 'alpha!', True, '!alpha', True, 1475,),
    (('multi', 'token',), (), 'multi token', True, 'single', False, 1476,),
    (('a', 'b', 'c',), ('b',), 'a c', True, 'a b', False, 1477,),
    (('x', 'y',), ('x',), 'y', True, 'x y', False, 1478,),
    (('kitten', 'puppy',), (), 'kitten puppy', True, 'kitten dog', False, 1479,),
    (('alpha',), ('beta',), 'alpha', True, 'beta', False, 1480,),
    (('red', 'green',), ('red', 'green',), 'red', False, 'red green', False, 1481,),
    (('blue', 'yellow',), ('blue',), 'yellow', True, 'blue yellow', False, 1482,),
    (('eins', 'zwei',), (), 'eins zwei', True, 'drei', False, 1483,),
    (('uno', 'dos',), ('uno',), 'dos', True, 'uno', False, 1484,),
    (('ichi', 'ni', 'san',), ('ni',), 'ichi san', True, 'ichi ni', False, 1485,),
    (('alpha', 'beta', 'gamma',), ('beta', 'gamma',), 'alpha', True, 'beta gamma', False, 1486,),
    (('only',), ('only',), 'only', False, 'not', False, 1487,),
)

class TestSafeFilter(BaseTest):
    """Safe word add/remove/is_safe stays consistent."""

    @pytest.mark.parametrize(('add_words', 'remove_words', 'present', 'present_expected', 'absent', 'absent_expected', 'uid',), _SAFE_FILTER_CASES)
    def test_safe_filter(self, engine: ModerationEngine, add_words: tuple[object, ...], remove_words: tuple[object, ...], present: str, present_expected: bool, absent: str, absent_expected: bool, uid: int) -> None:
        """Safe word add/remove/is_safe stays consistent."""
        safe_word: SafeWordFilter = engine._safe_word
        for word in add_words:
            safe_word.add_word(word)
        for word in remove_words:
            safe_word.remove_word(word)
        assert safe_word.is_safe(present) is present_expected
        assert safe_word.is_safe(absent) is absent_expected


_ROLLING_HASH_CASES: tuple[tuple[int, int, int], ...] = (
    (1, 0, 1488,),
    (1, 1, 1489,),
    (1, 60, 1490,),
    (3, 0, 1491,),
    (3, 1, 1492,),
    (3, 60, 1493,),
    (10, 0, 1494,),
    (10, 1, 1495,),
    (10, 60, 1496,),
    (100, 0, 1497,),
    (100, 1, 1498,),
    (100, 60, 1499,),
)

class TestRollingHash(BaseTest):
    """Rolling hash caches stay bounded and honor their TTL."""

    @pytest.mark.parametrize(('cache_size', 'ttl', 'uid',), _ROLLING_HASH_CASES)
    def test_rolling_hash(self, cache_size: int, ttl: int, uid: int) -> None:
        """Rolling hash caches stay bounded and honor their TTL."""
        detector: RollingHashDetector = RollingHashDetector(cache_size=cache_size, ttl_seconds=ttl)
        detector.record_hit('spam phrase')
        for index in range(50):
            detector.detect(f'unique {index}')
        assert len(detector._cache) <= cache_size
        assert isinstance(detector.detect('spam phrase').matched, bool)
        assert detector.detect('unrelated text').matched is False


_ROLLING_HASH_REPEAT_CASES: tuple[tuple[str, int], ...] = (
    ('repeat spam 0', 1500,),
)

class TestRollingHashRepeat(BaseTest):
    """Repeated flagged messages are caught deterministically."""

    @pytest.mark.parametrize(('text', 'uid',), _ROLLING_HASH_REPEAT_CASES)
    def test_rolling_hash_repeat(self, text: str, uid: int) -> None:
        """Repeated flagged messages are caught deterministically."""
        detector: RollingHashDetector = RollingHashDetector(cache_size=10, ttl_seconds=60)
        detector.record_hit(text)
        assert detector.detect(text).matched is True
        assert detector.detect('clean text here').matched is False
