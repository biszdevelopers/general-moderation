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

_MULTIWORD_VERDICT_CASES: tuple[tuple[str, str, str, int, str, int, int], ...] = (
    (
        "watch out for krazor and tundel today",
        "krazor",
        "tundel",
        100,
        "BLOCK",
        1,
        1701,
    ),
    (
        "watch out for pluvious and barvex today",
        "pluvious",
        "barvex",
        10,
        "REVIEW",
        2,
        1702,
    ),
    (
        "watch out for pluvious and barvex today",
        "pluvious",
        "barvex",
        30,
        "REVIEW",
        2,
        1703,
    ),
    (
        "watch out for pluvious and barvex today",
        "pluvious",
        "barvex",
        50,
        "REVIEW",
        2,
        1704,
    ),
    (
        "watch out for pluvious and barvex today",
        "pluvious",
        "barvex",
        70,
        "BLOCK",
        1,
        1705,
    ),
    (
        "watch out for pluvious and barvex today",
        "pluvious",
        "barvex",
        90,
        "BLOCK",
        1,
        1706,
    ),
    (
        "watch out for pluvious and barvex today",
        "pluvious",
        "barvex",
        100,
        "BLOCK",
        1,
        1707,
    ),
    (
        "watch out for snicker and doodle today",
        "snicker",
        "doodle",
        10,
        "REVIEW",
        2,
        1708,
    ),
    (
        "watch out for snicker and doodle today",
        "snicker",
        "doodle",
        30,
        "REVIEW",
        2,
        1709,
    ),
    (
        "watch out for snicker and doodle today",
        "snicker",
        "doodle",
        50,
        "REVIEW",
        2,
        1710,
    ),
    (
        "watch out for snicker and doodle today",
        "snicker",
        "doodle",
        70,
        "BLOCK",
        1,
        1711,
    ),
    (
        "watch out for snicker and doodle today",
        "snicker",
        "doodle",
        90,
        "BLOCK",
        1,
        1712,
    ),
    (
        "watch out for snicker and doodle today",
        "snicker",
        "doodle",
        100,
        "BLOCK",
        1,
        1713,
    ),
    (
        "watch out for grimble and wuzzle today",
        "grimble",
        "wuzzle",
        10,
        "REVIEW",
        2,
        1714,
    ),
    (
        "watch out for grimble and wuzzle today",
        "grimble",
        "wuzzle",
        30,
        "REVIEW",
        2,
        1715,
    ),
    (
        "watch out for grimble and wuzzle today",
        "grimble",
        "wuzzle",
        50,
        "REVIEW",
        2,
        1716,
    ),
    (
        "watch out for grimble and wuzzle today",
        "grimble",
        "wuzzle",
        70,
        "BLOCK",
        1,
        1717,
    ),
    (
        "watch out for grimble and wuzzle today",
        "grimble",
        "wuzzle",
        90,
        "BLOCK",
        1,
        1718,
    ),
    (
        "watch out for grimble and wuzzle today",
        "grimble",
        "wuzzle",
        100,
        "BLOCK",
        1,
        1719,
    ),
)


class TestMultiwordVerdict(BaseTest):
    """Multi-word seeds resolve deterministically at each threshold."""

    @pytest.mark.parametrize(
        (
            "text",
            "word1",
            "word2",
            "threshold",
            "expected",
            "level",
            "uid",
        ),
        _MULTIWORD_VERDICT_CASES,
    )
    def test_multiword_verdict(
        self,
        engine: ModerationEngine,
        word_bank: Any,
        text: str,
        word1: str,
        word2: str,
        threshold: int,
        expected: str,
        level: int,
        uid: int,
    ) -> None:
        """Multi-word seeds resolve deterministically at each threshold."""
        word_bank.add_word(word1)
        word_bank.add_word(word2)
        engine.refresh_detectors()
        engine._app_config.update_default_threshold(threshold)
        result: ModerationResponse = engine.moderate(
            ModerationRequest(text=text, app_name="a", user_id="u")
        )
        assert result.verdict.value == expected
        assert result.level_used == level


_PER_APP_POLICY_CASES: tuple[tuple[str, str, int, str, int, int], ...] = (
    (
        "you are a zaphrin here",
        "alpha",
        0,
        "REVIEW",
        2,
        1720,
    ),
    (
        "you are a zaphrin here",
        "alpha",
        20,
        "REVIEW",
        2,
        1721,
    ),
    (
        "you are a zaphrin here",
        "alpha",
        40,
        "REVIEW",
        2,
        1722,
    ),
    (
        "you are a zaphrin here",
        "alpha",
        60,
        "BLOCK",
        1,
        1723,
    ),
    (
        "you are a zaphrin here",
        "alpha",
        80,
        "BLOCK",
        1,
        1724,
    ),
    (
        "you are a zaphrin here",
        "alpha",
        100,
        "BLOCK",
        1,
        1725,
    ),
    (
        "you are a zaphrin here",
        "beta",
        0,
        "REVIEW",
        2,
        1726,
    ),
    (
        "you are a zaphrin here",
        "beta",
        20,
        "REVIEW",
        2,
        1727,
    ),
    (
        "you are a zaphrin here",
        "beta",
        40,
        "REVIEW",
        2,
        1728,
    ),
    (
        "you are a zaphrin here",
        "beta",
        60,
        "BLOCK",
        1,
        1729,
    ),
    (
        "you are a zaphrin here",
        "beta",
        80,
        "BLOCK",
        1,
        1730,
    ),
    (
        "you are a zaphrin here",
        "beta",
        100,
        "BLOCK",
        1,
        1731,
    ),
    (
        "you are a zaphrin here",
        "gamma",
        0,
        "REVIEW",
        2,
        1732,
    ),
    (
        "you are a zaphrin here",
        "gamma",
        20,
        "REVIEW",
        2,
        1733,
    ),
    (
        "you are a zaphrin here",
        "gamma",
        40,
        "REVIEW",
        2,
        1734,
    ),
    (
        "you are a zaphrin here",
        "gamma",
        60,
        "BLOCK",
        1,
        1735,
    ),
    (
        "you are a zaphrin here",
        "gamma",
        80,
        "BLOCK",
        1,
        1736,
    ),
    (
        "you are a zaphrin here",
        "gamma",
        100,
        "BLOCK",
        1,
        1737,
    ),
    (
        "you are a zaphrin here",
        "delta",
        0,
        "REVIEW",
        2,
        1738,
    ),
    (
        "you are a zaphrin here",
        "delta",
        20,
        "REVIEW",
        2,
        1739,
    ),
    (
        "you are a zaphrin here",
        "delta",
        40,
        "REVIEW",
        2,
        1740,
    ),
    (
        "you are a zaphrin here",
        "delta",
        60,
        "BLOCK",
        1,
        1741,
    ),
    (
        "you are a zaphrin here",
        "delta",
        80,
        "BLOCK",
        1,
        1742,
    ),
    (
        "you are a zaphrin here",
        "delta",
        100,
        "BLOCK",
        1,
        1743,
    ),
    (
        "you are a zaphrin here",
        "epsilon",
        0,
        "REVIEW",
        2,
        1744,
    ),
    (
        "you are a zaphrin here",
        "epsilon",
        20,
        "REVIEW",
        2,
        1745,
    ),
    (
        "you are a zaphrin here",
        "epsilon",
        40,
        "REVIEW",
        2,
        1746,
    ),
    (
        "you are a zaphrin here",
        "epsilon",
        60,
        "BLOCK",
        1,
        1747,
    ),
    (
        "you are a zaphrin here",
        "epsilon",
        80,
        "BLOCK",
        1,
        1748,
    ),
    (
        "you are a zaphrin here",
        "epsilon",
        100,
        "BLOCK",
        1,
        1749,
    ),
    (
        "you are a zaphrin here",
        "zeta",
        0,
        "REVIEW",
        2,
        1750,
    ),
    (
        "you are a zaphrin here",
        "zeta",
        20,
        "REVIEW",
        2,
        1751,
    ),
    (
        "you are a zaphrin here",
        "zeta",
        40,
        "REVIEW",
        2,
        1752,
    ),
    (
        "you are a zaphrin here",
        "zeta",
        60,
        "BLOCK",
        1,
        1753,
    ),
    (
        "you are a zaphrin here",
        "zeta",
        80,
        "BLOCK",
        1,
        1754,
    ),
    (
        "you are a zaphrin here",
        "zeta",
        100,
        "BLOCK",
        1,
        1755,
    ),
    (
        "you are a zaphrin here",
        "eta",
        0,
        "REVIEW",
        2,
        1756,
    ),
    (
        "you are a zaphrin here",
        "eta",
        20,
        "REVIEW",
        2,
        1757,
    ),
    (
        "you are a zaphrin here",
        "eta",
        40,
        "REVIEW",
        2,
        1758,
    ),
    (
        "you are a zaphrin here",
        "eta",
        60,
        "BLOCK",
        1,
        1759,
    ),
    (
        "you are a zaphrin here",
        "eta",
        80,
        "BLOCK",
        1,
        1760,
    ),
    (
        "you are a zaphrin here",
        "eta",
        100,
        "BLOCK",
        1,
        1761,
    ),
    (
        "you are a zaphrin here",
        "theta",
        0,
        "REVIEW",
        2,
        1762,
    ),
    (
        "you are a zaphrin here",
        "theta",
        20,
        "REVIEW",
        2,
        1763,
    ),
    (
        "you are a zaphrin here",
        "theta",
        40,
        "REVIEW",
        2,
        1764,
    ),
    (
        "you are a zaphrin here",
        "theta",
        60,
        "BLOCK",
        1,
        1765,
    ),
    (
        "you are a zaphrin here",
        "theta",
        80,
        "BLOCK",
        1,
        1766,
    ),
    (
        "you are a zaphrin here",
        "theta",
        100,
        "BLOCK",
        1,
        1767,
    ),
    (
        "you are a zaphrin here",
        "iota",
        0,
        "REVIEW",
        2,
        1768,
    ),
    (
        "you are a zaphrin here",
        "iota",
        20,
        "REVIEW",
        2,
        1769,
    ),
    (
        "you are a zaphrin here",
        "iota",
        40,
        "REVIEW",
        2,
        1770,
    ),
    (
        "you are a zaphrin here",
        "iota",
        60,
        "BLOCK",
        1,
        1771,
    ),
    (
        "you are a zaphrin here",
        "iota",
        80,
        "BLOCK",
        1,
        1772,
    ),
    (
        "you are a zaphrin here",
        "iota",
        100,
        "BLOCK",
        1,
        1773,
    ),
    (
        "you are a zaphrin here",
        "kappa",
        0,
        "REVIEW",
        2,
        1774,
    ),
    (
        "you are a zaphrin here",
        "kappa",
        20,
        "REVIEW",
        2,
        1775,
    ),
    (
        "you are a zaphrin here",
        "kappa",
        40,
        "REVIEW",
        2,
        1776,
    ),
    (
        "you are a zaphrin here",
        "kappa",
        60,
        "BLOCK",
        1,
        1777,
    ),
    (
        "you are a zaphrin here",
        "kappa",
        80,
        "BLOCK",
        1,
        1778,
    ),
    (
        "you are a zaphrin here",
        "kappa",
        100,
        "BLOCK",
        1,
        1779,
    ),
)


class TestPerAppPolicy(BaseTest):
    """Per-app trigger policies resolve independently."""

    @pytest.mark.parametrize(
        (
            "text",
            "app_name",
            "threshold",
            "expected",
            "level",
            "uid",
        ),
        _PER_APP_POLICY_CASES,
    )
    def test_per_app_policy(
        self,
        engine: ModerationEngine,
        word_bank: Any,
        text: str,
        app_name: str,
        threshold: int,
        expected: str,
        level: int,
        uid: int,
    ) -> None:
        """Per-app trigger policies resolve independently."""
        word_bank.add_word("zaphrin")
        engine.refresh_detectors()
        engine._app_config.update_default_threshold(threshold)
        result: ModerationResponse = engine.moderate(
            ModerationRequest(text=text, app_name=app_name, user_id="u")
        )
        assert result.verdict.value == expected
        assert result.level_used == level


_CACHE_TTL_CLOCK_CASES: tuple[tuple[int, bool, int], ...] = (
    (
        -172800,
        True,
        1780,
    ),
    (
        -86400,
        True,
        1781,
    ),
    (
        -7200,
        True,
        1782,
    ),
    (
        -3600,
        True,
        1783,
    ),
    (
        -1800,
        True,
        1784,
    ),
    (
        -900,
        True,
        1785,
    ),
    (
        -600,
        True,
        1786,
    ),
    (
        -300,
        True,
        1787,
    ),
    (
        -120,
        True,
        1788,
    ),
    (
        -60,
        True,
        1789,
    ),
    (
        -30,
        True,
        1790,
    ),
    (
        -10,
        True,
        1791,
    ),
    (
        -5,
        True,
        1792,
    ),
    (
        -2,
        True,
        1793,
    ),
    (
        -1,
        True,
        1794,
    ),
    (
        1,
        False,
        1795,
    ),
    (
        2,
        False,
        1796,
    ),
    (
        5,
        False,
        1797,
    ),
    (
        10,
        False,
        1798,
    ),
    (
        30,
        False,
        1799,
    ),
    (
        60,
        False,
        1800,
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
