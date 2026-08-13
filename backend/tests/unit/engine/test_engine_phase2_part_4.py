"""Phase 2 engine pipeline tests (generated).

Golden verdict matrices, cache and batch properties, app policies and
component invariants; see tests/tools/phase2_generator.py."""

# multilingual fixtures use non-ASCII on purpose
from __future__ import annotations

import pytest

from app.detectors.rolling_hash_detector import RollingHashDetector
from app.engine.moderation_engine import ModerationEngine
from app.models.request import ModerationRequest
from app.models.response import ModerationResponse
from tests.base_test import BaseTest

_ROLLING_HASH_REPEAT_CASES: tuple[tuple[str, int], ...] = (
    (
        "repeat spam 1",
        1501,
    ),
    (
        "repeat spam 2",
        1502,
    ),
    (
        "repeat spam 3",
        1503,
    ),
    (
        "repeat spam 4",
        1504,
    ),
    (
        "repeat spam 5",
        1505,
    ),
    (
        "repeat spam 6",
        1506,
    ),
    (
        "repeat spam 7",
        1507,
    ),
    (
        "repeat spam 8",
        1508,
    ),
    (
        "repeat spam 9",
        1509,
    ),
)


class TestRollingHashRepeat(BaseTest):
    """Repeated flagged messages are caught deterministically."""

    @pytest.mark.parametrize(
        (
            "text",
            "uid",
        ),
        _ROLLING_HASH_REPEAT_CASES,
    )
    def test_rolling_hash_repeat(self, text: str, uid: int) -> None:
        """Repeated flagged messages are caught deterministically."""
        detector: RollingHashDetector = RollingHashDetector(cache_size=10, ttl_seconds=60)
        detector.record_hit(text)
        assert detector.detect(text).matched is True
        assert detector.detect("clean text here").matched is False


_METRICS_COUNTER_CASES: tuple[tuple[int, int], ...] = (
    (
        1,
        1510,
    ),
    (
        2,
        1511,
    ),
    (
        3,
        1512,
    ),
    (
        4,
        1513,
    ),
    (
        5,
        1514,
    ),
    (
        6,
        1515,
    ),
    (
        7,
        1516,
    ),
    (
        8,
        1517,
    ),
    (
        9,
        1518,
    ),
    (
        10,
        1519,
    ),
    (
        11,
        1520,
    ),
    (
        12,
        1521,
    ),
    (
        13,
        1522,
    ),
    (
        14,
        1523,
    ),
    (
        15,
        1524,
    ),
    (
        16,
        1525,
    ),
    (
        17,
        1526,
    ),
    (
        18,
        1527,
    ),
    (
        19,
        1528,
    ),
    (
        20,
        1529,
    ),
    (
        21,
        1530,
    ),
    (
        22,
        1531,
    ),
    (
        23,
        1532,
    ),
    (
        24,
        1533,
    ),
    (
        25,
        1534,
    ),
    (
        26,
        1535,
    ),
    (
        27,
        1536,
    ),
    (
        28,
        1537,
    ),
    (
        29,
        1538,
    ),
    (
        30,
        1539,
    ),
    (
        31,
        1540,
    ),
    (
        32,
        1541,
    ),
    (
        33,
        1542,
    ),
    (
        34,
        1543,
    ),
    (
        35,
        1544,
    ),
    (
        36,
        1545,
    ),
    (
        37,
        1546,
    ),
    (
        38,
        1547,
    ),
    (
        39,
        1548,
    ),
    (
        40,
        1549,
    ),
    (
        41,
        1550,
    ),
    (
        42,
        1551,
    ),
    (
        43,
        1552,
    ),
    (
        44,
        1553,
    ),
    (
        45,
        1554,
    ),
    (
        46,
        1555,
    ),
    (
        47,
        1556,
    ),
    (
        48,
        1557,
    ),
    (
        49,
        1558,
    ),
    (
        50,
        1559,
    ),
)


class TestMetricsCounter(BaseTest):
    """Request counters match the number of moderations exactly."""

    @pytest.mark.parametrize(
        (
            "n_moderations",
            "uid",
        ),
        _METRICS_COUNTER_CASES,
    )
    def test_metrics_counter(self, engine: ModerationEngine, n_moderations: int, uid: int) -> None:
        """Request counters match the number of moderations exactly."""
        for index in range(n_moderations):
            engine.moderate(ModerationRequest(text=f"metric message {index}", app_name="a"))
        metrics = engine.metrics()
        assert metrics["requests_total"] == n_moderations
        assert metrics["requests_pass_total"] == n_moderations
        assert "detector_rolling_hash_seconds_total" in metrics


_VARIED_CONTENT_MATRIX_CASES: tuple[tuple[str, str, int, int], ...] = (
    (
        "you a",
        "PASS",
        1,
        1560,
    ),
    (
        "you are a piece of garbag",
        "PASS",
        1,
        1561,
    ),
    (
        "you are a piece of garbage and a loser ",
        "BLOCK",
        1,
        1562,
    ),
    (
        "you are a piece of garbage and a loser ",
        "BLOCK",
        1,
        1563,
    ),
    (
        "buy c",
        "PASS",
        1,
        1564,
    ),
    (
        "buy cheap pills online no",
        "PASS",
        1,
        1565,
    ),
    (
        "buy cheap pills online now at low prices ",
        "PASS",
        1,
        1566,
    ),
    (
        "buy cheap pills online now at low prices ",
        "PASS",
        1,
        1567,
    ),
    (
        "i wil",
        "PASS",
        1,
        1568,
    ),
    (
        "i will smash your car and",
        "PASS",
        1,
        1569,
    ),
    (
        "i will smash your car and burn the house ",
        "PASS",
        1,
        1570,
    ),
    (
        "i will smash your car and burn the house ",
        "PASS",
        1,
        1571,
    ),
    (
        "your ",
        "PASS",
        1,
        1572,
    ),
    (
        "your phone number 5551234",
        "PASS",
        1,
        1573,
    ),
    (
        "your phone number 5551234567 is now public ",
        "PASS",
        1,
        1574,
    ),
    (
        "your phone number 5551234567 is now public ",
        "PASS",
        1,
        1575,
    ),
    (
        "fuck ",
        "BLOCK",
        1,
        1576,
    ),
    (
        "fuck this noise and every",
        "BLOCK",
        1,
        1577,
    ),
    (
        "fuck this noise and everything else ",
        "BLOCK",
        1,
        1578,
    ),
    (
        "fuck this noise and everything else ",
        "BLOCK",
        1,
        1579,
    ),
    (
        "the m",
        "PASS",
        1,
        1580,
    ),
    (
        "the meeting is scheduled ",
        "PASS",
        1,
        1581,
    ),
    (
        "the meeting is scheduled for ten in the morning ",
        "PASS",
        1,
        1582,
    ),
    (
        "the meeting is scheduled for ten in the morning ",
        "PASS",
        1,
        1583,
    ),
    (
        "let u",
        "PASS",
        1,
        1584,
    ),
    (
        "let us review the quarter",
        "PASS",
        1,
        1585,
    ),
    (
        "let us review the quarterly numbers together ",
        "PASS",
        1,
        1586,
    ),
    (
        "let us review the quarterly numbers together ",
        "PASS",
        1,
        1587,
    ),
    (
        "pleas",
        "PASS",
        1,
        1588,
    ),
    (
        "please confirm the order ",
        "PASS",
        1,
        1589,
    ),
    (
        "please confirm the order number before shipping ",
        "PASS",
        1,
        1590,
    ),
    (
        "please confirm the order number before shipping ",
        "PASS",
        1,
        1591,
    ),
    (
        "your ",
        "PASS",
        1,
        1592,
    ),
    (
        "your account password was",
        "BLOCK",
        1,
        1593,
    ),
    (
        "your account password was exposed in a breach ",
        "BLOCK",
        1,
        1594,
    ),
    (
        "your account password was exposed in a breach ",
        "BLOCK",
        1,
        1595,
    ),
    (
        "join ",
        "PASS",
        1,
        1596,
    ),
    (
        "join our crypto pyramid s",
        "PASS",
        1,
        1597,
    ),
    (
        "join our crypto pyramid scheme today ",
        "BLOCK",
        1,
        1598,
    ),
    (
        "join our crypto pyramid scheme today ",
        "BLOCK",
        1,
        1599,
    ),
    (
        "this ",
        "PASS",
        1,
        1600,
    ),
)


class TestVariedContentMatrix(BaseTest):
    """Varied content resolves to a recognized verdict."""

    @pytest.mark.parametrize(
        (
            "text",
            "expected",
            "level",
            "uid",
        ),
        _VARIED_CONTENT_MATRIX_CASES,
    )
    def test_varied_content_matrix(
        self, engine: ModerationEngine, text: str, expected: str, level: int, uid: int
    ) -> None:
        """Varied content resolves to a recognized verdict."""
        result: ModerationResponse = engine.moderate(
            ModerationRequest(text=text, app_name="a", user_id="u")
        )
        assert result.verdict.value == expected
        assert result.level_used == level
        assert 0.0 <= result.suspicion_score <= 100.0
