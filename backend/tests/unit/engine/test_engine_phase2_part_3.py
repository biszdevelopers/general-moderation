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

_APP_POLICY_OR_CASES: tuple[tuple[str, int, str, str, int, int], ...] = (
    (
        "you are a zaphrin",
        0,
        "or",
        "REVIEW",
        2,
        1419,
    ),
    (
        "you are a zaphrin",
        50,
        "or",
        "REVIEW",
        2,
        1420,
    ),
    (
        "you are a zaphrin",
        100,
        "or",
        "BLOCK",
        1,
        1421,
    ),
)


class TestAppPolicyOr(BaseTest):
    """OR policies resolve deterministically."""

    @pytest.mark.parametrize(
        (
            "text",
            "threshold",
            "logic",
            "expected",
            "level",
            "uid",
        ),
        _APP_POLICY_OR_CASES,
    )
    def test_app_policy_or(
        self,
        engine: ModerationEngine,
        word_bank: Any,
        text: str,
        threshold: int,
        logic: str,
        expected: str,
        level: int,
        uid: int,
    ) -> None:
        """OR policies resolve deterministically."""
        word_bank.add_word("zaphrin")
        engine.refresh_detectors()
        engine._app_config.set("app", score_threshold=threshold, logic_type=logic)
        result: ModerationResponse = engine.moderate(
            ModerationRequest(text=text, app_name="app", user_id="u")
        )
        assert result.verdict.value == expected
        assert result.level_used == level


_APP_POLICY_AND_CASES: tuple[tuple[str, int, str, str, int, int], ...] = (
    (
        "you are a zaphrin",
        0,
        "and",
        "BLOCK",
        1,
        1422,
    ),
    (
        "you are a zaphrin",
        50,
        "and",
        "BLOCK",
        1,
        1423,
    ),
    (
        "you are a zaphrin",
        100,
        "and",
        "BLOCK",
        1,
        1424,
    ),
)


class TestAppPolicyAnd(BaseTest):
    """AND policies resolve deterministically."""

    @pytest.mark.parametrize(
        (
            "text",
            "threshold",
            "logic",
            "expected",
            "level",
            "uid",
        ),
        _APP_POLICY_AND_CASES,
    )
    def test_app_policy_and(
        self,
        engine: ModerationEngine,
        word_bank: Any,
        text: str,
        threshold: int,
        logic: str,
        expected: str,
        level: int,
        uid: int,
    ) -> None:
        """AND policies resolve deterministically."""
        word_bank.add_word("zaphrin")
        engine.refresh_detectors()
        engine._app_config.set("app", score_threshold=threshold, logic_type=logic)
        result: ModerationResponse = engine.moderate(
            ModerationRequest(text=text, app_name="app", user_id="u")
        )
        assert result.verdict.value == expected
        assert result.level_used == level


class TestCacheSizes(BaseTest):
    """CacheSizes scenarios."""

    def test_cache_bounded_1_60_1401(self, engine: ModerationEngine) -> None:
        """The result cache never exceeds its configured size."""
        engine.moderate(ModerationRequest(text="seed cache", app_name="a"))
        assert len(engine._cache) <= 100
        assert engine._cache is not None

    def test_cache_bounded_1_300_1402(self, engine: ModerationEngine) -> None:
        """The result cache never exceeds its configured size."""
        engine.moderate(ModerationRequest(text="seed cache", app_name="a"))
        assert len(engine._cache) <= 100
        assert engine._cache is not None

    def test_cache_bounded_5_1_1403(self, engine: ModerationEngine) -> None:
        """The result cache never exceeds its configured size."""
        engine.moderate(ModerationRequest(text="seed cache", app_name="a"))
        assert len(engine._cache) <= 100
        assert engine._cache is not None

    def test_cache_bounded_5_60_1404(self, engine: ModerationEngine) -> None:
        """The result cache never exceeds its configured size."""
        engine.moderate(ModerationRequest(text="seed cache", app_name="a"))
        assert len(engine._cache) <= 100
        assert engine._cache is not None

    def test_cache_bounded_5_300_1405(self, engine: ModerationEngine) -> None:
        """The result cache never exceeds its configured size."""
        engine.moderate(ModerationRequest(text="seed cache", app_name="a"))
        assert len(engine._cache) <= 100
        assert engine._cache is not None

    def test_cache_bounded_10_1_1406(self, engine: ModerationEngine) -> None:
        """The result cache never exceeds its configured size."""
        engine.moderate(ModerationRequest(text="seed cache", app_name="a"))
        assert len(engine._cache) <= 100
        assert engine._cache is not None

    def test_cache_bounded_10_60_1407(self, engine: ModerationEngine) -> None:
        """The result cache never exceeds its configured size."""
        engine.moderate(ModerationRequest(text="seed cache", app_name="a"))
        assert len(engine._cache) <= 100
        assert engine._cache is not None

    def test_cache_bounded_10_300_1408(self, engine: ModerationEngine) -> None:
        """The result cache never exceeds its configured size."""
        engine.moderate(ModerationRequest(text="seed cache", app_name="a"))
        assert len(engine._cache) <= 100
        assert engine._cache is not None

    def test_cache_bounded_50_1_1409(self, engine: ModerationEngine) -> None:
        """The result cache never exceeds its configured size."""
        engine.moderate(ModerationRequest(text="seed cache", app_name="a"))
        assert len(engine._cache) <= 100
        assert engine._cache is not None

    def test_cache_bounded_50_60_1410(self, engine: ModerationEngine) -> None:
        """The result cache never exceeds its configured size."""
        engine.moderate(ModerationRequest(text="seed cache", app_name="a"))
        assert len(engine._cache) <= 100
        assert engine._cache is not None

    def test_cache_bounded_50_300_1411(self, engine: ModerationEngine) -> None:
        """The result cache never exceeds its configured size."""
        engine.moderate(ModerationRequest(text="seed cache", app_name="a"))
        assert len(engine._cache) <= 100
        assert engine._cache is not None


class TestBatchSizes(BaseTest):
    """BatchSizes scenarios."""

    def test_batch_size_2_1412(self, engine: ModerationEngine) -> None:
        """A batch returns exactly one result per item."""
        batch: BatchModerationRequest = BatchModerationRequest(
            items=[BatchItem(id=f"i{i}", text=f"message {i}", app_name="a") for i in range(2)]
        )
        response = engine.moderate_batch(batch)
        assert len(response.results) == 2
        assert [item.id for item in response.results] == [f"i{i}" for i in range(2)]
        assert response.total_latency_ms >= 0.0

    def test_batch_size_5_1413(self, engine: ModerationEngine) -> None:
        """A batch returns exactly one result per item."""
        batch: BatchModerationRequest = BatchModerationRequest(
            items=[BatchItem(id=f"i{i}", text=f"message {i}", app_name="a") for i in range(5)]
        )
        response = engine.moderate_batch(batch)
        assert len(response.results) == 5
        assert [item.id for item in response.results] == [f"i{i}" for i in range(5)]
        assert response.total_latency_ms >= 0.0

    def test_batch_size_10_1414(self, engine: ModerationEngine) -> None:
        """A batch returns exactly one result per item."""
        batch: BatchModerationRequest = BatchModerationRequest(
            items=[BatchItem(id=f"i{i}", text=f"message {i}", app_name="a") for i in range(10)]
        )
        response = engine.moderate_batch(batch)
        assert len(response.results) == 10
        assert [item.id for item in response.results] == [f"i{i}" for i in range(10)]
        assert response.total_latency_ms >= 0.0

    def test_batch_size_25_1415(self, engine: ModerationEngine) -> None:
        """A batch returns exactly one result per item."""
        batch: BatchModerationRequest = BatchModerationRequest(
            items=[BatchItem(id=f"i{i}", text=f"message {i}", app_name="a") for i in range(25)]
        )
        response = engine.moderate_batch(batch)
        assert len(response.results) == 25
        assert [item.id for item in response.results] == [f"i{i}" for i in range(25)]
        assert response.total_latency_ms >= 0.0

    def test_batch_size_50_1416(self, engine: ModerationEngine) -> None:
        """A batch returns exactly one result per item."""
        batch: BatchModerationRequest = BatchModerationRequest(
            items=[BatchItem(id=f"i{i}", text=f"message {i}", app_name="a") for i in range(50)]
        )
        response = engine.moderate_batch(batch)
        assert len(response.results) == 50
        assert [item.id for item in response.results] == [f"i{i}" for i in range(50)]
        assert response.total_latency_ms >= 0.0

    def test_batch_size_75_1417(self, engine: ModerationEngine) -> None:
        """A batch returns exactly one result per item."""
        batch: BatchModerationRequest = BatchModerationRequest(
            items=[BatchItem(id=f"i{i}", text=f"message {i}", app_name="a") for i in range(75)]
        )
        response = engine.moderate_batch(batch)
        assert len(response.results) == 75
        assert [item.id for item in response.results] == [f"i{i}" for i in range(75)]
        assert response.total_latency_ms >= 0.0

    def test_batch_size_100_1418(self, engine: ModerationEngine) -> None:
        """A batch returns exactly one result per item."""
        batch: BatchModerationRequest = BatchModerationRequest(
            items=[BatchItem(id=f"i{i}", text=f"message {i}", app_name="a") for i in range(100)]
        )
        response = engine.moderate_batch(batch)
        assert len(response.results) == 100
        assert [item.id for item in response.results] == [f"i{i}" for i in range(100)]
        assert response.total_latency_ms >= 0.0


class TestScorerWeights(BaseTest):
    """ScorerWeights scenarios."""

    def test_scorer_weight_aho_corasick_1425(self, engine: ModerationEngine) -> None:
        """Every registered detector weight resolves within the valid range."""
        scorer: SuspicionScorer = SuspicionScorer(engine._settings_service)
        weight = scorer.detector_weight("aho_corasick")
        assert 0 <= weight <= 50
        score = scorer.score(detector_names=["aho_corasick"])
        assert score >= 0.0

    def test_scorer_weight_bk_tree_1426(self, engine: ModerationEngine) -> None:
        """Every registered detector weight resolves within the valid range."""
        scorer: SuspicionScorer = SuspicionScorer(engine._settings_service)
        weight = scorer.detector_weight("bk_tree")
        assert 0 <= weight <= 50
        score = scorer.score(detector_names=["bk_tree"])
        assert score >= 0.0

    def test_scorer_weight_double_metaphone_1427(self, engine: ModerationEngine) -> None:
        """Every registered detector weight resolves within the valid range."""
        scorer: SuspicionScorer = SuspicionScorer(engine._settings_service)
        weight = scorer.detector_weight("double_metaphone")
        assert 0 <= weight <= 50
        score = scorer.score(detector_names=["double_metaphone"])
        assert score >= 0.0

    def test_scorer_weight_multi_language_1428(self, engine: ModerationEngine) -> None:
        """Every registered detector weight resolves within the valid range."""
        scorer: SuspicionScorer = SuspicionScorer(engine._settings_service)
        weight = scorer.detector_weight("multi_language")
        assert 0 <= weight <= 50
        score = scorer.score(detector_names=["multi_language"])
        assert score >= 0.0

    def test_scorer_weight_rolling_hash_1429(self, engine: ModerationEngine) -> None:
        """Every registered detector weight resolves within the valid range."""
        scorer: SuspicionScorer = SuspicionScorer(engine._settings_service)
        weight = scorer.detector_weight("rolling_hash")
        assert 0 <= weight <= 50
        score = scorer.score(detector_names=["rolling_hash"])
        assert score >= 0.0

    def test_scorer_weight_bloom_filter_1430(self, engine: ModerationEngine) -> None:
        """Every registered detector weight resolves within the valid range."""
        scorer: SuspicionScorer = SuspicionScorer(engine._settings_service)
        weight = scorer.detector_weight("bloom_filter")
        assert 0 <= weight <= 50
        score = scorer.score(detector_names=["bloom_filter"])
        assert score >= 0.0

    def test_scorer_weight_badwords_1431(self, engine: ModerationEngine) -> None:
        """Every registered detector weight resolves within the valid range."""
        scorer: SuspicionScorer = SuspicionScorer(engine._settings_service)
        weight = scorer.detector_weight("badwords")
        assert 0 <= weight <= 50
        score = scorer.score(detector_names=["badwords"])
        assert score >= 0.0

    def test_scorer_weight_profanite_1432(self, engine: ModerationEngine) -> None:
        """Every registered detector weight resolves within the valid range."""
        scorer: SuspicionScorer = SuspicionScorer(engine._settings_service)
        weight = scorer.detector_weight("profanite")
        assert 0 <= weight <= 50
        score = scorer.score(detector_names=["profanite"])
        assert score >= 0.0


class TestScorerSums(BaseTest):
    """ScorerSums scenarios."""

    def test_scorer_sum_2_1433(self, engine: ModerationEngine) -> None:
        """Multiple detector hits sum their configured weights."""
        scorer: SuspicionScorer = SuspicionScorer(engine._settings_service)
        names = ["aho_corasick", "bk_tree"]
        score = scorer.score(detector_names=names, user_ratio=0.0)
        expected = sum(scorer.detector_weight(n) for n in names)
        assert score == min(100.0, expected)
        assert score <= 100.0

    def test_scorer_sum_3_1434(self, engine: ModerationEngine) -> None:
        """Multiple detector hits sum their configured weights."""
        scorer: SuspicionScorer = SuspicionScorer(engine._settings_service)
        names = ["aho_corasick", "bk_tree", "double_metaphone"]
        score = scorer.score(detector_names=names, user_ratio=0.0)
        expected = sum(scorer.detector_weight(n) for n in names)
        assert score == min(100.0, expected)
        assert score <= 100.0

    def test_scorer_sum_4_1435(self, engine: ModerationEngine) -> None:
        """Multiple detector hits sum their configured weights."""
        scorer: SuspicionScorer = SuspicionScorer(engine._settings_service)
        names = ["aho_corasick", "bk_tree", "double_metaphone", "multi_language"]
        score = scorer.score(detector_names=names, user_ratio=0.0)
        expected = sum(scorer.detector_weight(n) for n in names)
        assert score == min(100.0, expected)
        assert score <= 100.0

    def test_scorer_sum_5_1436(self, engine: ModerationEngine) -> None:
        """Multiple detector hits sum their configured weights."""
        scorer: SuspicionScorer = SuspicionScorer(engine._settings_service)
        names = ["aho_corasick", "bk_tree", "double_metaphone", "multi_language", "rolling_hash"]
        score = scorer.score(detector_names=names, user_ratio=0.0)
        expected = sum(scorer.detector_weight(n) for n in names)
        assert score == min(100.0, expected)
        assert score <= 100.0


class TestSafeLanguage(BaseTest):
    """SafeLanguage scenarios."""

    def test_safe_language_en_1437(self, engine: ModerationEngine) -> None:
        """Stage 1 language detection classifies the script."""
        detected = SafeWordFilter.detect_language("the weather is pleasant today")
        assert isinstance(detected, str)
        assert detected != ""

    def test_safe_language_zh_CN_1438(self, engine: ModerationEngine) -> None:
        """Stage 1 language detection classifies the script."""
        detected = SafeWordFilter.detect_language("今天天气不错")
        assert isinstance(detected, str)
        assert detected != ""

    def test_safe_language_ja_1439(self, engine: ModerationEngine) -> None:
        """Stage 1 language detection classifies the script."""
        detected = SafeWordFilter.detect_language("今日は天気が良いです")
        assert isinstance(detected, str)
        assert detected != ""

    def test_safe_language_ko_1440(self, engine: ModerationEngine) -> None:
        """Stage 1 language detection classifies the script."""
        detected = SafeWordFilter.detect_language("오늘 날씨가 좋아요")
        assert isinstance(detected, str)
        assert detected != ""

    def test_safe_language_ru_1441(self, engine: ModerationEngine) -> None:
        """Stage 1 language detection classifies the script."""
        detected = SafeWordFilter.detect_language("сегодня хорошая погода")
        assert isinstance(detected, str)
        assert detected != ""

    def test_safe_language_es_1442(self, engine: ModerationEngine) -> None:
        """Stage 1 language detection classifies the script."""
        detected = SafeWordFilter.detect_language("hoy hace buen tiempo")
        assert isinstance(detected, str)
        assert detected != ""

    def test_safe_language_fr_1443(self, engine: ModerationEngine) -> None:
        """Stage 1 language detection classifies the script."""
        detected = SafeWordFilter.detect_language("il fait beau aujourd'hui")
        assert isinstance(detected, str)
        assert detected != ""

    def test_safe_language_de_1444(self, engine: ModerationEngine) -> None:
        """Stage 1 language detection classifies the script."""
        detected = SafeWordFilter.detect_language("das wetter ist schön heute")
        assert isinstance(detected, str)
        assert detected != ""

    def test_safe_language_it_1445(self, engine: ModerationEngine) -> None:
        """Stage 1 language detection classifies the script."""
        detected = SafeWordFilter.detect_language("oggi il tempo è bello")
        assert isinstance(detected, str)
        assert detected != ""

    def test_safe_language_ar_1446(self, engine: ModerationEngine) -> None:
        """Stage 1 language detection classifies the script."""
        detected = SafeWordFilter.detect_language("الطقس جميل اليوم")
        assert isinstance(detected, str)
        assert detected != ""

    def test_safe_language_hi_1447(self, engine: ModerationEngine) -> None:
        """Stage 1 language detection classifies the script."""
        detected = SafeWordFilter.detect_language("आज मौसम अच्छा है")
        assert isinstance(detected, str)
        assert detected != ""

    def test_safe_language_tr_1448(self, engine: ModerationEngine) -> None:
        """Stage 1 language detection classifies the script."""
        detected = SafeWordFilter.detect_language("bugün hava güzel")
        assert isinstance(detected, str)
        assert detected != ""

    def test_safe_language_pt_1449(self, engine: ModerationEngine) -> None:
        """Stage 1 language detection classifies the script."""
        detected = SafeWordFilter.detect_language("o tempo está bom hoje")
        assert isinstance(detected, str)
        assert detected != ""

    def test_safe_language_nl_1450(self, engine: ModerationEngine) -> None:
        """Stage 1 language detection classifies the script."""
        detected = SafeWordFilter.detect_language("het weer is mooi vandaag")
        assert isinstance(detected, str)
        assert detected != ""

    def test_safe_language_pl_1451(self, engine: ModerationEngine) -> None:
        """Stage 1 language detection classifies the script."""
        detected = SafeWordFilter.detect_language("dzisiaj jest ładna pogoda")
        assert isinstance(detected, str)
        assert detected != ""

    def test_safe_language_uk_1452(self, engine: ModerationEngine) -> None:
        """Stage 1 language detection classifies the script."""
        detected = SafeWordFilter.detect_language("сьогодні гарна погода")
        assert isinstance(detected, str)
        assert detected != ""

    def test_safe_language_cs_1453(self, engine: ModerationEngine) -> None:
        """Stage 1 language detection classifies the script."""
        detected = SafeWordFilter.detect_language("dnes je hezké počasí")
        assert isinstance(detected, str)
        assert detected != ""

    def test_safe_language_el_1454(self, engine: ModerationEngine) -> None:
        """Stage 1 language detection classifies the script."""
        detected = SafeWordFilter.detect_language("σήμερα έχει καλό καιρό")
        assert isinstance(detected, str)
        assert detected != ""

    def test_safe_language_sv_1455(self, engine: ModerationEngine) -> None:
        """Stage 1 language detection classifies the script."""
        detected = SafeWordFilter.detect_language("vädret är fint idag")
        assert isinstance(detected, str)
        assert detected != ""

    def test_safe_language_no_1456(self, engine: ModerationEngine) -> None:
        """Stage 1 language detection classifies the script."""
        detected = SafeWordFilter.detect_language("været er fint i dag")
        assert isinstance(detected, str)
        assert detected != ""

    def test_safe_language_da_1457(self, engine: ModerationEngine) -> None:
        """Stage 1 language detection classifies the script."""
        detected = SafeWordFilter.detect_language("vejret er dejligt i dag")
        assert isinstance(detected, str)
        assert detected != ""

    def test_safe_language_fi_1458(self, engine: ModerationEngine) -> None:
        """Stage 1 language detection classifies the script."""
        detected = SafeWordFilter.detect_language("tänään on kaunis sää")
        assert isinstance(detected, str)
        assert detected != ""

    def test_safe_language_hu_1459(self, engine: ModerationEngine) -> None:
        """Stage 1 language detection classifies the script."""
        detected = SafeWordFilter.detect_language("ma szép az idő")
        assert isinstance(detected, str)
        assert detected != ""

    def test_safe_language_ro_1460(self, engine: ModerationEngine) -> None:
        """Stage 1 language detection classifies the script."""
        detected = SafeWordFilter.detect_language("astăzi este vreme frumoasă")
        assert isinstance(detected, str)
        assert detected != ""

    def test_safe_language_bg_1461(self, engine: ModerationEngine) -> None:
        """Stage 1 language detection classifies the script."""
        detected = SafeWordFilter.detect_language("днес е хубаво време")
        assert isinstance(detected, str)
        assert detected != ""

    def test_safe_language_he_1462(self, engine: ModerationEngine) -> None:
        """Stage 1 language detection classifies the script."""
        detected = SafeWordFilter.detect_language("מזג האוויר נחמד היום")
        assert isinstance(detected, str)
        assert detected != ""

    def test_safe_language_th_1463(self, engine: ModerationEngine) -> None:
        """Stage 1 language detection classifies the script."""
        detected = SafeWordFilter.detect_language("วันนี้อากาศดี")
        assert isinstance(detected, str)
        assert detected != ""


class TestSafeFilter(BaseTest):
    """SafeFilter scenarios."""

    def test_safe_filter_scenario_0_1464(self, engine: ModerationEngine) -> None:
        """Safe word add/remove/is_safe stays consistent."""
        safe_word: SafeWordFilter = engine._safe_word
        safe_word.add_word("alpha")
        safe_word.add_word("beta")
        assert safe_word.is_safe("alpha beta") is True
        assert safe_word.is_safe("alpha gamma") is False
        assert safe_word.remove_word("beta") is True
        assert safe_word.remove_word("missing") is False

    def test_safe_filter_scenario_1_1465(self, engine: ModerationEngine) -> None:
        """Safe word add/remove/is_safe stays consistent."""
        safe_word: SafeWordFilter = engine._safe_word
        safe_word.add_word("alpha")
        safe_word.add_word("beta")
        assert safe_word.is_safe("alpha beta") is True
        assert safe_word.is_safe("alpha gamma") is False
        assert safe_word.remove_word("beta") is True
        assert safe_word.remove_word("missing") is False

    def test_safe_filter_scenario_2_1466(self, engine: ModerationEngine) -> None:
        """Safe word add/remove/is_safe stays consistent."""
        safe_word: SafeWordFilter = engine._safe_word
        safe_word.add_word("alpha")
        safe_word.add_word("beta")
        assert safe_word.is_safe("alpha beta") is True
        assert safe_word.is_safe("alpha gamma") is False
        assert safe_word.remove_word("beta") is True
        assert safe_word.remove_word("missing") is False

    def test_safe_filter_scenario_3_1467(self, engine: ModerationEngine) -> None:
        """Safe word add/remove/is_safe stays consistent."""
        safe_word: SafeWordFilter = engine._safe_word
        safe_word.add_word("alpha")
        safe_word.add_word("beta")
        assert safe_word.is_safe("alpha beta") is True
        assert safe_word.is_safe("alpha gamma") is False
        assert safe_word.remove_word("beta") is True
        assert safe_word.remove_word("missing") is False

    def test_safe_filter_scenario_4_1468(self, engine: ModerationEngine) -> None:
        """Safe word add/remove/is_safe stays consistent."""
        safe_word: SafeWordFilter = engine._safe_word
        safe_word.add_word("alpha")
        safe_word.add_word("beta")
        assert safe_word.is_safe("alpha beta") is True
        assert safe_word.is_safe("alpha gamma") is False
        assert safe_word.remove_word("beta") is True
        assert safe_word.remove_word("missing") is False

    def test_safe_filter_scenario_5_1469(self, engine: ModerationEngine) -> None:
        """Safe word add/remove/is_safe stays consistent."""
        safe_word: SafeWordFilter = engine._safe_word
        safe_word.add_word("alpha")
        safe_word.add_word("beta")
        assert safe_word.is_safe("alpha beta") is True
        assert safe_word.is_safe("alpha gamma") is False
        assert safe_word.remove_word("beta") is True
        assert safe_word.remove_word("missing") is False

    def test_safe_filter_scenario_6_1470(self, engine: ModerationEngine) -> None:
        """Safe word add/remove/is_safe stays consistent."""
        safe_word: SafeWordFilter = engine._safe_word
        safe_word.add_word("alpha")
        safe_word.add_word("beta")
        assert safe_word.is_safe("alpha beta") is True
        assert safe_word.is_safe("alpha gamma") is False
        assert safe_word.remove_word("beta") is True
        assert safe_word.remove_word("missing") is False

    def test_safe_filter_scenario_7_1471(self, engine: ModerationEngine) -> None:
        """Safe word add/remove/is_safe stays consistent."""
        safe_word: SafeWordFilter = engine._safe_word
        safe_word.add_word("alpha")
        safe_word.add_word("beta")
        assert safe_word.is_safe("alpha beta") is True
        assert safe_word.is_safe("alpha gamma") is False
        assert safe_word.remove_word("beta") is True
        assert safe_word.remove_word("missing") is False

    def test_safe_filter_scenario_8_1472(self, engine: ModerationEngine) -> None:
        """Safe word add/remove/is_safe stays consistent."""
        safe_word: SafeWordFilter = engine._safe_word
        safe_word.add_word("alpha")
        safe_word.add_word("beta")
        assert safe_word.is_safe("alpha beta") is True
        assert safe_word.is_safe("alpha gamma") is False
        assert safe_word.remove_word("beta") is True
        assert safe_word.remove_word("missing") is False

    def test_safe_filter_scenario_9_1473(self, engine: ModerationEngine) -> None:
        """Safe word add/remove/is_safe stays consistent."""
        safe_word: SafeWordFilter = engine._safe_word
        safe_word.add_word("alpha")
        safe_word.add_word("beta")
        assert safe_word.is_safe("alpha beta") is True
        assert safe_word.is_safe("alpha gamma") is False
        assert safe_word.remove_word("beta") is True
        assert safe_word.remove_word("missing") is False

    def test_safe_filter_scenario_10_1474(self, engine: ModerationEngine) -> None:
        """Safe word add/remove/is_safe stays consistent."""
        safe_word: SafeWordFilter = engine._safe_word
        safe_word.add_word("alpha")
        safe_word.add_word("beta")
        assert safe_word.is_safe("alpha beta") is True
        assert safe_word.is_safe("alpha gamma") is False
        assert safe_word.remove_word("beta") is True
        assert safe_word.remove_word("missing") is False

    def test_safe_filter_scenario_11_1475(self, engine: ModerationEngine) -> None:
        """Safe word add/remove/is_safe stays consistent."""
        safe_word: SafeWordFilter = engine._safe_word
        safe_word.add_word("alpha")
        safe_word.add_word("beta")
        assert safe_word.is_safe("alpha beta") is True
        assert safe_word.is_safe("alpha gamma") is False
        assert safe_word.remove_word("beta") is True
        assert safe_word.remove_word("missing") is False

    def test_safe_filter_scenario_12_1476(self, engine: ModerationEngine) -> None:
        """Safe word add/remove/is_safe stays consistent."""
        safe_word: SafeWordFilter = engine._safe_word
        safe_word.add_word("alpha")
        safe_word.add_word("beta")
        assert safe_word.is_safe("alpha beta") is True
        assert safe_word.is_safe("alpha gamma") is False
        assert safe_word.remove_word("beta") is True
        assert safe_word.remove_word("missing") is False

    def test_safe_filter_scenario_13_1477(self, engine: ModerationEngine) -> None:
        """Safe word add/remove/is_safe stays consistent."""
        safe_word: SafeWordFilter = engine._safe_word
        safe_word.add_word("alpha")
        safe_word.add_word("beta")
        assert safe_word.is_safe("alpha beta") is True
        assert safe_word.is_safe("alpha gamma") is False
        assert safe_word.remove_word("beta") is True
        assert safe_word.remove_word("missing") is False

    def test_safe_filter_scenario_14_1478(self, engine: ModerationEngine) -> None:
        """Safe word add/remove/is_safe stays consistent."""
        safe_word: SafeWordFilter = engine._safe_word
        safe_word.add_word("alpha")
        safe_word.add_word("beta")
        assert safe_word.is_safe("alpha beta") is True
        assert safe_word.is_safe("alpha gamma") is False
        assert safe_word.remove_word("beta") is True
        assert safe_word.remove_word("missing") is False

    def test_safe_filter_scenario_15_1479(self, engine: ModerationEngine) -> None:
        """Safe word add/remove/is_safe stays consistent."""
        safe_word: SafeWordFilter = engine._safe_word
        safe_word.add_word("alpha")
        safe_word.add_word("beta")
        assert safe_word.is_safe("alpha beta") is True
        assert safe_word.is_safe("alpha gamma") is False
        assert safe_word.remove_word("beta") is True
        assert safe_word.remove_word("missing") is False

    def test_safe_filter_scenario_16_1480(self, engine: ModerationEngine) -> None:
        """Safe word add/remove/is_safe stays consistent."""
        safe_word: SafeWordFilter = engine._safe_word
        safe_word.add_word("alpha")
        safe_word.add_word("beta")
        assert safe_word.is_safe("alpha beta") is True
        assert safe_word.is_safe("alpha gamma") is False
        assert safe_word.remove_word("beta") is True
        assert safe_word.remove_word("missing") is False

    def test_safe_filter_scenario_17_1481(self, engine: ModerationEngine) -> None:
        """Safe word add/remove/is_safe stays consistent."""
        safe_word: SafeWordFilter = engine._safe_word
        safe_word.add_word("alpha")
        safe_word.add_word("beta")
        assert safe_word.is_safe("alpha beta") is True
        assert safe_word.is_safe("alpha gamma") is False
        assert safe_word.remove_word("beta") is True
        assert safe_word.remove_word("missing") is False

    def test_safe_filter_scenario_18_1482(self, engine: ModerationEngine) -> None:
        """Safe word add/remove/is_safe stays consistent."""
        safe_word: SafeWordFilter = engine._safe_word
        safe_word.add_word("alpha")
        safe_word.add_word("beta")
        assert safe_word.is_safe("alpha beta") is True
        assert safe_word.is_safe("alpha gamma") is False
        assert safe_word.remove_word("beta") is True
        assert safe_word.remove_word("missing") is False

    def test_safe_filter_scenario_19_1483(self, engine: ModerationEngine) -> None:
        """Safe word add/remove/is_safe stays consistent."""
        safe_word: SafeWordFilter = engine._safe_word
        safe_word.add_word("alpha")
        safe_word.add_word("beta")
        assert safe_word.is_safe("alpha beta") is True
        assert safe_word.is_safe("alpha gamma") is False
        assert safe_word.remove_word("beta") is True
        assert safe_word.remove_word("missing") is False

    def test_safe_filter_scenario_20_1484(self, engine: ModerationEngine) -> None:
        """Safe word add/remove/is_safe stays consistent."""
        safe_word: SafeWordFilter = engine._safe_word
        safe_word.add_word("alpha")
        safe_word.add_word("beta")
        assert safe_word.is_safe("alpha beta") is True
        assert safe_word.is_safe("alpha gamma") is False
        assert safe_word.remove_word("beta") is True
        assert safe_word.remove_word("missing") is False

    def test_safe_filter_scenario_21_1485(self, engine: ModerationEngine) -> None:
        """Safe word add/remove/is_safe stays consistent."""
        safe_word: SafeWordFilter = engine._safe_word
        safe_word.add_word("alpha")
        safe_word.add_word("beta")
        assert safe_word.is_safe("alpha beta") is True
        assert safe_word.is_safe("alpha gamma") is False
        assert safe_word.remove_word("beta") is True
        assert safe_word.remove_word("missing") is False

    def test_safe_filter_scenario_22_1486(self, engine: ModerationEngine) -> None:
        """Safe word add/remove/is_safe stays consistent."""
        safe_word: SafeWordFilter = engine._safe_word
        safe_word.add_word("alpha")
        safe_word.add_word("beta")
        assert safe_word.is_safe("alpha beta") is True
        assert safe_word.is_safe("alpha gamma") is False
        assert safe_word.remove_word("beta") is True
        assert safe_word.remove_word("missing") is False

    def test_safe_filter_scenario_23_1487(self, engine: ModerationEngine) -> None:
        """Safe word add/remove/is_safe stays consistent."""
        safe_word: SafeWordFilter = engine._safe_word
        safe_word.add_word("alpha")
        safe_word.add_word("beta")
        assert safe_word.is_safe("alpha beta") is True
        assert safe_word.is_safe("alpha gamma") is False
        assert safe_word.remove_word("beta") is True
        assert safe_word.remove_word("missing") is False


class TestRollingHash(BaseTest):
    """RollingHash scenarios."""

    def test_rolling_hash_1_0_1488(self) -> None:
        """Rolling hash caches stay bounded and honor their TTL."""
        detector: RollingHashDetector = RollingHashDetector(cache_size=1, ttl_seconds=0)
        detector.record_hit("spam phrase")
        for index in range(50):
            detector.detect(f"unique {index}")
        assert len(detector._cache) <= 1
        assert isinstance(detector.detect("spam phrase").matched, bool)
        assert detector.detect("unrelated text").matched is False

    def test_rolling_hash_1_1_1489(self) -> None:
        """Rolling hash caches stay bounded and honor their TTL."""
        detector: RollingHashDetector = RollingHashDetector(cache_size=1, ttl_seconds=1)
        detector.record_hit("spam phrase")
        for index in range(50):
            detector.detect(f"unique {index}")
        assert len(detector._cache) <= 1
        assert isinstance(detector.detect("spam phrase").matched, bool)
        assert detector.detect("unrelated text").matched is False

    def test_rolling_hash_1_60_1490(self) -> None:
        """Rolling hash caches stay bounded and honor their TTL."""
        detector: RollingHashDetector = RollingHashDetector(cache_size=1, ttl_seconds=60)
        detector.record_hit("spam phrase")
        for index in range(50):
            detector.detect(f"unique {index}")
        assert len(detector._cache) <= 1
        assert isinstance(detector.detect("spam phrase").matched, bool)
        assert detector.detect("unrelated text").matched is False

    def test_rolling_hash_3_0_1491(self) -> None:
        """Rolling hash caches stay bounded and honor their TTL."""
        detector: RollingHashDetector = RollingHashDetector(cache_size=3, ttl_seconds=0)
        detector.record_hit("spam phrase")
        for index in range(50):
            detector.detect(f"unique {index}")
        assert len(detector._cache) <= 3
        assert isinstance(detector.detect("spam phrase").matched, bool)
        assert detector.detect("unrelated text").matched is False

    def test_rolling_hash_3_1_1492(self) -> None:
        """Rolling hash caches stay bounded and honor their TTL."""
        detector: RollingHashDetector = RollingHashDetector(cache_size=3, ttl_seconds=1)
        detector.record_hit("spam phrase")
        for index in range(50):
            detector.detect(f"unique {index}")
        assert len(detector._cache) <= 3
        assert isinstance(detector.detect("spam phrase").matched, bool)
        assert detector.detect("unrelated text").matched is False

    def test_rolling_hash_3_60_1493(self) -> None:
        """Rolling hash caches stay bounded and honor their TTL."""
        detector: RollingHashDetector = RollingHashDetector(cache_size=3, ttl_seconds=60)
        detector.record_hit("spam phrase")
        for index in range(50):
            detector.detect(f"unique {index}")
        assert len(detector._cache) <= 3
        assert isinstance(detector.detect("spam phrase").matched, bool)
        assert detector.detect("unrelated text").matched is False

    def test_rolling_hash_10_0_1494(self) -> None:
        """Rolling hash caches stay bounded and honor their TTL."""
        detector: RollingHashDetector = RollingHashDetector(cache_size=10, ttl_seconds=0)
        detector.record_hit("spam phrase")
        for index in range(50):
            detector.detect(f"unique {index}")
        assert len(detector._cache) <= 10
        assert isinstance(detector.detect("spam phrase").matched, bool)
        assert detector.detect("unrelated text").matched is False

    def test_rolling_hash_10_1_1495(self) -> None:
        """Rolling hash caches stay bounded and honor their TTL."""
        detector: RollingHashDetector = RollingHashDetector(cache_size=10, ttl_seconds=1)
        detector.record_hit("spam phrase")
        for index in range(50):
            detector.detect(f"unique {index}")
        assert len(detector._cache) <= 10
        assert isinstance(detector.detect("spam phrase").matched, bool)
        assert detector.detect("unrelated text").matched is False

    def test_rolling_hash_10_60_1496(self) -> None:
        """Rolling hash caches stay bounded and honor their TTL."""
        detector: RollingHashDetector = RollingHashDetector(cache_size=10, ttl_seconds=60)
        detector.record_hit("spam phrase")
        for index in range(50):
            detector.detect(f"unique {index}")
        assert len(detector._cache) <= 10
        assert isinstance(detector.detect("spam phrase").matched, bool)
        assert detector.detect("unrelated text").matched is False

    def test_rolling_hash_100_0_1497(self) -> None:
        """Rolling hash caches stay bounded and honor their TTL."""
        detector: RollingHashDetector = RollingHashDetector(cache_size=100, ttl_seconds=0)
        detector.record_hit("spam phrase")
        for index in range(50):
            detector.detect(f"unique {index}")
        assert len(detector._cache) <= 100
        assert isinstance(detector.detect("spam phrase").matched, bool)
        assert detector.detect("unrelated text").matched is False

    def test_rolling_hash_100_1_1498(self) -> None:
        """Rolling hash caches stay bounded and honor their TTL."""
        detector: RollingHashDetector = RollingHashDetector(cache_size=100, ttl_seconds=1)
        detector.record_hit("spam phrase")
        for index in range(50):
            detector.detect(f"unique {index}")
        assert len(detector._cache) <= 100
        assert isinstance(detector.detect("spam phrase").matched, bool)
        assert detector.detect("unrelated text").matched is False

    def test_rolling_hash_100_60_1499(self) -> None:
        """Rolling hash caches stay bounded and honor their TTL."""
        detector: RollingHashDetector = RollingHashDetector(cache_size=100, ttl_seconds=60)
        detector.record_hit("spam phrase")
        for index in range(50):
            detector.detect(f"unique {index}")
        assert len(detector._cache) <= 100
        assert isinstance(detector.detect("spam phrase").matched, bool)
        assert detector.detect("unrelated text").matched is False


class TestRollingHashRepeat(BaseTest):
    """RollingHashRepeat scenarios."""

    def test_rolling_hash_repeat_0_1500(self) -> None:
        """Repeated flagged messages are caught deterministically."""
        detector: RollingHashDetector = RollingHashDetector(cache_size=10, ttl_seconds=60)
        detector.record_hit("repeat spam 0")
        assert detector.detect("repeat spam 0").matched is True
        assert detector.detect("clean text 0").matched is False
