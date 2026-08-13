"""Phase 2 engine pipeline tests (generated).

Golden verdict matrices, cache and batch properties, app policies and
component invariants; see tests/tools/phase2_generator.py."""

# multilingual fixtures use non-ASCII on purpose
from __future__ import annotations

from typing import Any

import pytest

from app.engine.moderation_engine import ModerationEngine
from app.models.request import BatchItem, BatchModerationRequest, ModerationRequest
from app.models.response import ModerationResponse
from tests.base_test import BaseTest

_CACHE_TTL_CLOCK_CASES: tuple[tuple[int, bool, int], ...] = (
    (
        120,
        False,
        1801,
    ),
    (
        300,
        False,
        1802,
    ),
    (
        600,
        False,
        1803,
    ),
    (
        900,
        False,
        1804,
    ),
    (
        1800,
        False,
        1805,
    ),
    (
        3600,
        False,
        1806,
    ),
    (
        7200,
        False,
        1807,
    ),
    (
        86400,
        False,
        1808,
    ),
    (
        172800,
        False,
        1809,
    ),
)


class TestCacheTtlClock(BaseTest):
    """Cached results expire once the timestamp passes the TTL."""

    @pytest.mark.parametrize(
        (
            "offset",
            "expected_cached",
            "uid",
        ),
        _CACHE_TTL_CLOCK_CASES,
    )
    def test_cache_ttl_clock(
        self, engine: ModerationEngine, offset: int, expected_cached: bool, uid: int
    ) -> None:
        """Cached results expire once the timestamp passes the TTL."""
        engine.moderate(ModerationRequest(text="clock cache", app_name="a"))
        key = engine._get_cache_key("clock cache")
        assert engine._get_cached(key) is not None
        engine._cache_timestamps[key] -= engine._cache_ttl + offset
        if expected_cached:
            assert engine._get_cached(key) is not None
        else:
            assert engine._get_cached(key) is None


_BATCH_MIXED_CASES: tuple[tuple[tuple[object, ...], int], ...] = (
    (
        (
            "clean message here",
            "you are a zaphrin",
        ),
        1810,
    ),
    (
        (
            "clean message here",
            "you are a zaphrin",
            "buy cheap pills now",
        ),
        1811,
    ),
    (
        (
            "clean message here",
            "you are a zaphrin",
            "buy cheap pills now",
            "ordinary daily update",
        ),
        1812,
    ),
    (
        (
            "clean message here",
            "you are a zaphrin",
            "buy cheap pills now",
            "ordinary daily update",
            "i will hurt you badly",
        ),
        1813,
    ),
    (
        (
            "clean message here",
            "you are a zaphrin",
            "buy cheap pills now",
            "ordinary daily update",
            "i will hurt you badly",
            "free gift cards",
        ),
        1814,
    ),
    (
        (
            "clean message here",
            "you are a zaphrin",
            "buy cheap pills now",
            "ordinary daily update",
            "i will hurt you badly",
            "free gift cards",
        ),
        1815,
    ),
    (
        (
            "clean message here",
            "you are a zaphrin",
            "buy cheap pills now",
            "ordinary daily update",
            "i will hurt you badly",
            "free gift cards",
        ),
        1816,
    ),
)


class TestBatchMixed(BaseTest):
    """Mixed-content batches return a valid verdict per item."""

    @pytest.mark.parametrize(
        (
            "items",
            "uid",
        ),
        _BATCH_MIXED_CASES,
    )
    def test_batch_mixed(
        self, engine: ModerationEngine, word_bank: Any, items: tuple[object, ...], uid: int
    ) -> None:
        """Mixed-content batches return a valid verdict per item."""
        word_bank.add_word("zaphrin")
        engine.refresh_detectors()
        batch: BatchModerationRequest = BatchModerationRequest(
            items=[BatchItem(text=text, app_name="a") for text in items]
        )
        response = engine.moderate_batch(batch)
        assert len(response.results) == len(items)
        for result in response.results:
            assert result.verdict.value in ("PASS", "BLOCK", "REVIEW")


_REFRESH_SCENARIO_CASES: tuple[tuple[int, int], ...] = (
    (
        1,
        1817,
    ),
    (
        2,
        1818,
    ),
    (
        3,
        1819,
    ),
    (
        4,
        1820,
    ),
    (
        5,
        1821,
    ),
    (
        6,
        1822,
    ),
    (
        7,
        1823,
    ),
    (
        8,
        1824,
    ),
    (
        9,
        1825,
    ),
    (
        10,
        1826,
    ),
    (
        11,
        1827,
    ),
    (
        12,
        1828,
    ),
    (
        13,
        1829,
    ),
    (
        14,
        1830,
    ),
    (
        15,
        1831,
    ),
    (
        16,
        1832,
    ),
    (
        17,
        1833,
    ),
    (
        18,
        1834,
    ),
    (
        19,
        1835,
    ),
    (
        20,
        1836,
    ),
    (
        21,
        1837,
    ),
    (
        22,
        1838,
    ),
    (
        23,
        1839,
    ),
    (
        24,
        1840,
    ),
    (
        25,
        1841,
    ),
    (
        26,
        1842,
    ),
    (
        27,
        1843,
    ),
    (
        28,
        1844,
    ),
    (
        29,
        1845,
    ),
    (
        30,
        1846,
    ),
)


class TestRefreshScenario(BaseTest):
    """refresh_detectors clears the cache and keeps the roster."""

    @pytest.mark.parametrize(
        (
            "n_texts",
            "uid",
        ),
        _REFRESH_SCENARIO_CASES,
    )
    def test_refresh_scenario(
        self, engine: ModerationEngine, word_bank: Any, n_texts: int, uid: int
    ) -> None:
        """refresh_detectors clears the cache and keeps the roster."""
        for index in range(n_texts):
            engine.moderate(ModerationRequest(text=f"pre refresh {index}", app_name="a"))
        assert len(engine._cache) == min(n_texts, engine._cache_max_size)
        word_bank.add_word("refreshword")
        engine.refresh_detectors()
        assert len(engine._cache) == 0
        assert len(engine._detectors) >= 4


_PROFILER_INTEGRATION_CASES: tuple[tuple[str, str, int], ...] = (
    (
        "p2user0",
        "profile 0",
        1847,
    ),
    (
        "p2user1",
        "profile 1",
        1848,
    ),
    (
        "p2user2",
        "profile 2",
        1849,
    ),
    (
        "p2user3",
        "profile 3",
        1850,
    ),
    (
        "p2user4",
        "profile 4",
        1851,
    ),
    (
        "p2user5",
        "profile 5",
        1852,
    ),
    (
        "p2user6",
        "profile 6",
        1853,
    ),
    (
        "p2user7",
        "profile 7",
        1854,
    ),
    (
        "p2user8",
        "profile 8",
        1855,
    ),
    (
        "p2user9",
        "profile 9",
        1856,
    ),
    (
        "p2user10",
        "profile 10",
        1857,
    ),
    (
        "p2user11",
        "profile 11",
        1858,
    ),
    (
        "p2user12",
        "profile 12",
        1859,
    ),
    (
        "p2user13",
        "profile 13",
        1860,
    ),
    (
        "p2user14",
        "profile 14",
        1861,
    ),
    (
        "p2user15",
        "profile 15",
        1862,
    ),
    (
        "p2user16",
        "profile 16",
        1863,
    ),
    (
        "p2user17",
        "profile 17",
        1864,
    ),
    (
        "p2user18",
        "profile 18",
        1865,
    ),
    (
        "p2user19",
        "profile 19",
        1866,
    ),
    (
        "p2user20",
        "profile 20",
        1867,
    ),
    (
        "p2user21",
        "profile 21",
        1868,
    ),
    (
        "p2user22",
        "profile 22",
        1869,
    ),
    (
        "p2user23",
        "profile 23",
        1870,
    ),
    (
        "p2user24",
        "profile 24",
        1871,
    ),
    (
        "p2user25",
        "profile 25",
        1872,
    ),
    (
        "p2user26",
        "profile 26",
        1873,
    ),
    (
        "p2user27",
        "profile 27",
        1874,
    ),
    (
        "p2user28",
        "profile 28",
        1875,
    ),
    (
        "p2user29",
        "profile 29",
        1876,
    ),
    (
        "p2user30",
        "profile 30",
        1877,
    ),
    (
        "p2user31",
        "profile 31",
        1878,
    ),
    (
        "p2user32",
        "profile 32",
        1879,
    ),
    (
        "p2user33",
        "profile 33",
        1880,
    ),
    (
        "p2user34",
        "profile 34",
        1881,
    ),
    (
        "p2user35",
        "profile 35",
        1882,
    ),
    (
        "p2user36",
        "profile 36",
        1883,
    ),
    (
        "p2user37",
        "profile 37",
        1884,
    ),
    (
        "p2user38",
        "profile 38",
        1885,
    ),
    (
        "p2user39",
        "profile 39",
        1886,
    ),
)


class TestProfilerIntegration(BaseTest):
    """Engine moderation records daily profiling rows."""

    @pytest.mark.parametrize(
        (
            "user_id",
            "text",
            "uid",
        ),
        _PROFILER_INTEGRATION_CASES,
    )
    def test_profiler_integration(
        self, engine: ModerationEngine, user_id: str, text: str, uid: int
    ) -> None:
        """Engine moderation records daily profiling rows."""
        engine.moderate(ModerationRequest(text=text, app_name="app", user_id=user_id))
        profile = engine._profiler.get_profile("app", user_id)
        assert profile["daily"]
        assert profile["daily"][0]["total_msgs"] >= 1
        assert profile["ratio"] == 0.0


_RESPONSE_INVARIANT_CASES: tuple[tuple[str, str, int], ...] = (
    (
        "resp-0",
        "invariant 0",
        1887,
    ),
    (
        "resp-1",
        "invariant 1",
        1888,
    ),
    (
        "resp-2",
        "invariant 2",
        1889,
    ),
    (
        "resp-3",
        "invariant 3",
        1890,
    ),
    (
        "resp-4",
        "invariant 4",
        1891,
    ),
    (
        "resp-5",
        "invariant 5",
        1892,
    ),
    (
        "resp-6",
        "invariant 6",
        1893,
    ),
    (
        "resp-7",
        "invariant 7",
        1894,
    ),
    (
        "resp-8",
        "invariant 8",
        1895,
    ),
    (
        "resp-9",
        "invariant 9",
        1896,
    ),
    (
        "resp-10",
        "invariant 10",
        1897,
    ),
    (
        "resp-11",
        "invariant 11",
        1898,
    ),
    (
        "resp-12",
        "invariant 12",
        1899,
    ),
    (
        "resp-13",
        "invariant 13",
        1900,
    ),
)


class TestResponseInvariant(BaseTest):
    """Every moderation response honors its structural invariants."""

    @pytest.mark.parametrize(
        (
            "request_id",
            "text",
            "uid",
        ),
        _RESPONSE_INVARIANT_CASES,
    )
    def test_response_invariant(
        self, engine: ModerationEngine, request_id: str, text: str, uid: int
    ) -> None:
        """Every moderation response honors its structural invariants."""
        result: ModerationResponse = engine.moderate(
            ModerationRequest(id=request_id, text=text, app_name="a", user_id="u")
        )
        assert result.id == request_id
        assert result.allowed == (result.verdict.value != "BLOCK")
        assert 0.0 <= result.suspicion_score <= 100.0
        assert result.latency_ms >= 0.0
