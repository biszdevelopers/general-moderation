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

_VARIED_CONTENT_MATRIX_CASES: tuple[tuple[str, str, int, int], ...] = (
    ('this message contains zer', 'PASS', 1, 1601,),
    ('this message contains zero special meaning ', 'PASS', 1, 1602,),
    ('this message contains zero special meaning ', 'PASS', 1, 1603,),
    ('we st', 'PASS', 1, 1604,),
    ('we strongly condemn all f', 'PASS', 1, 1605,),
    ('we strongly condemn all forms of violence ', 'PASS', 1, 1606,),
    ('we strongly condemn all forms of violence ', 'PASS', 1, 1607,),
    ('today', 'PASS', 1, 1608,),
    ('today the stock market cl', 'PASS', 1, 1609,),
    ('today the stock market closed slightly higher ', 'PASS', 1, 1610,),
    ('today the stock market closed slightly higher ', 'PASS', 1, 1611,),
    ('share', 'PASS', 1, 1612,),
    ('share your credit card de', 'PASS', 1, 1613,),
    ('share your credit card details with support ', 'PASS', 1, 1614,),
    ('share your credit card details with support ', 'PASS', 1, 1615,),
    ('free ', 'PASS', 1, 1616,),
    ('free gift cards for every', 'PASS', 1, 1617,),
    ('free gift cards for everyone who clicks now ', 'PASS', 1, 1618,),
    ('free gift cards for everyone who clicks now ', 'PASS', 1, 1619,),
    ('moder', 'PASS', 1, 1620,),
    ('moderate your tone when a', 'PASS', 1, 1621,),
    ('moderate your tone when addressing colleagues ', 'PASS', 1, 1622,),
    ('moderate your tone when addressing colleagues ', 'PASS', 1, 1623,),
    ('sprea', 'PASS', 1, 1624,),
    ('spread the rumor about th', 'PASS', 1, 1625,),
    ("spread the rumor about the manager's resignation ", 'PASS', 1, 1626,),
    ("spread the rumor about the manager's resignation ", 'PASS', 1, 1627,),
    ('the d', 'PASS', 1, 1628,),
    ('the deadline has been mov', 'PASS', 1, 1629,),
    ('the deadline has been moved to friday next week ', 'PASS', 1, 1630,),
    ('the deadline has been moved to friday next week ', 'PASS', 1, 1631,),
    ('your ', 'PASS', 1, 1632,),
    ('your location data is bei', 'BLOCK', 1, 1633,),
    ('your location data is being collected quietly ', 'BLOCK', 1, 1634,),
    ('your location data is being collected quietly ', 'BLOCK', 1, 1635,),
    ('unsub', 'PASS', 1, 1636,),
    ('unsubscribe from these ma', 'PASS', 1, 1637,),
    ('unsubscribe from these marketing emails please ', 'PASS', 1, 1638,),
    ('unsubscribe from these marketing emails please ', 'PASS', 1, 1639,),
    ('watch', 'PASS', 1, 1640,),
    ('watch the video of the ho', 'BLOCK', 1, 1641,),
    ('watch the video of the horrible accident here ', 'PASS', 1, 1642,),
    ('watch the video of the horrible accident here ', 'PASS', 1, 1643,),
    ('the c', 'PASS', 1, 1644,),
    ('the community guidelines ', 'PASS', 1, 1645,),
    ('the community guidelines prohibit this content ', 'PASS', 1, 1646,),
    ('the community guidelines prohibit this content ', 'PASS', 1, 1647,),
    ('pleas', 'PASS', 1, 1648,),
    ('please read the attached ', 'PASS', 1, 1649,),
    ('please read the attached document carefully ', 'PASS', 1, 1650,),
    ('please read the attached document carefully ', 'PASS', 1, 1651,),
    ('we ne', 'PASS', 1, 1652,),
    ('we need volunteers for th', 'PASS', 1, 1653,),
    ('we need volunteers for the weekend cleanup ', 'PASS', 1, 1654,),
    ('we need volunteers for the weekend cleanup ', 'PASS', 1, 1655,),
    ('vote ', 'PASS', 1, 1656,),
    ('vote for the candidate in', 'PASS', 1, 1657,),
    ('vote for the candidate in the upcoming election ', 'PASS', 1, 1658,),
    ('vote for the candidate in the upcoming election ', 'PASS', 1, 1659,),
)

class TestVariedContentMatrix(BaseTest):
    """Varied content resolves to a recognized verdict."""

    @pytest.mark.parametrize(('text', 'expected', 'level', 'uid',), _VARIED_CONTENT_MATRIX_CASES)
    def test_varied_content_matrix(self, engine: ModerationEngine, text: str, expected: str, level: int, uid: int) -> None:
        """Varied content resolves to a recognized verdict."""
        result: ModerationResponse = engine.moderate(
            ModerationRequest(text=text, app_name='a', user_id='u')
        )
        assert result.verdict.value == expected
        assert result.level_used == level
        assert 0.0 <= result.suspicion_score <= 100.0


_MULTIWORD_VERDICT_CASES: tuple[tuple[str, str, str, int, str, int, int], ...] = (
    ('watch out for zaphrin and blorp today', 'zaphrin', 'blorp', 10, 'REVIEW', 2, 1660,),
    ('watch out for zaphrin and blorp today', 'zaphrin', 'blorp', 30, 'REVIEW', 2, 1661,),
    ('watch out for zaphrin and blorp today', 'zaphrin', 'blorp', 50, 'REVIEW', 2, 1662,),
    ('watch out for zaphrin and blorp today', 'zaphrin', 'blorp', 70, 'BLOCK', 1, 1663,),
    ('watch out for zaphrin and blorp today', 'zaphrin', 'blorp', 90, 'BLOCK', 1, 1664,),
    ('watch out for zaphrin and blorp today', 'zaphrin', 'blorp', 100, 'BLOCK', 1, 1665,),
    ('watch out for flubber and quxxle today', 'flubber', 'quxxle', 10, 'REVIEW', 2, 1666,),
    ('watch out for flubber and quxxle today', 'flubber', 'quxxle', 30, 'REVIEW', 2, 1667,),
    ('watch out for flubber and quxxle today', 'flubber', 'quxxle', 50, 'REVIEW', 2, 1668,),
    ('watch out for flubber and quxxle today', 'flubber', 'quxxle', 70, 'BLOCK', 1, 1669,),
    ('watch out for flubber and quxxle today', 'flubber', 'quxxle', 90, 'BLOCK', 1, 1670,),
    ('watch out for flubber and quxxle today', 'flubber', 'quxxle', 100, 'BLOCK', 1, 1671,),
    ('watch out for wombat and giblet today', 'wombat', 'giblet', 10, 'REVIEW', 2, 1672,),
    ('watch out for wombat and giblet today', 'wombat', 'giblet', 30, 'REVIEW', 2, 1673,),
    ('watch out for wombat and giblet today', 'wombat', 'giblet', 50, 'REVIEW', 2, 1674,),
    ('watch out for wombat and giblet today', 'wombat', 'giblet', 70, 'BLOCK', 1, 1675,),
    ('watch out for wombat and giblet today', 'wombat', 'giblet', 90, 'BLOCK', 1, 1676,),
    ('watch out for wombat and giblet today', 'wombat', 'giblet', 100, 'BLOCK', 1, 1677,),
    ('watch out for snarg and zorp today', 'snarg', 'zorp', 10, 'REVIEW', 2, 1678,),
    ('watch out for snarg and zorp today', 'snarg', 'zorp', 30, 'REVIEW', 2, 1679,),
    ('watch out for snarg and zorp today', 'snarg', 'zorp', 50, 'REVIEW', 2, 1680,),
    ('watch out for snarg and zorp today', 'snarg', 'zorp', 70, 'BLOCK', 1, 1681,),
    ('watch out for snarg and zorp today', 'snarg', 'zorp', 90, 'BLOCK', 1, 1682,),
    ('watch out for snarg and zorp today', 'snarg', 'zorp', 100, 'BLOCK', 1, 1683,),
    ('watch out for meldrup and vexil today', 'meldrup', 'vexil', 10, 'REVIEW', 2, 1684,),
    ('watch out for meldrup and vexil today', 'meldrup', 'vexil', 30, 'REVIEW', 2, 1685,),
    ('watch out for meldrup and vexil today', 'meldrup', 'vexil', 50, 'REVIEW', 2, 1686,),
    ('watch out for meldrup and vexil today', 'meldrup', 'vexil', 70, 'BLOCK', 1, 1687,),
    ('watch out for meldrup and vexil today', 'meldrup', 'vexil', 90, 'BLOCK', 1, 1688,),
    ('watch out for meldrup and vexil today', 'meldrup', 'vexil', 100, 'BLOCK', 1, 1689,),
    ('watch out for gromble and spritz today', 'gromble', 'spritz', 10, 'REVIEW', 2, 1690,),
    ('watch out for gromble and spritz today', 'gromble', 'spritz', 30, 'REVIEW', 2, 1691,),
    ('watch out for gromble and spritz today', 'gromble', 'spritz', 50, 'REVIEW', 2, 1692,),
    ('watch out for gromble and spritz today', 'gromble', 'spritz', 70, 'BLOCK', 1, 1693,),
    ('watch out for gromble and spritz today', 'gromble', 'spritz', 90, 'BLOCK', 1, 1694,),
    ('watch out for gromble and spritz today', 'gromble', 'spritz', 100, 'BLOCK', 1, 1695,),
    ('watch out for krazor and tundel today', 'krazor', 'tundel', 10, 'REVIEW', 2, 1696,),
    ('watch out for krazor and tundel today', 'krazor', 'tundel', 30, 'REVIEW', 2, 1697,),
    ('watch out for krazor and tundel today', 'krazor', 'tundel', 50, 'REVIEW', 2, 1698,),
    ('watch out for krazor and tundel today', 'krazor', 'tundel', 70, 'BLOCK', 1, 1699,),
    ('watch out for krazor and tundel today', 'krazor', 'tundel', 90, 'BLOCK', 1, 1700,),
)

class TestMultiwordVerdict(BaseTest):
    """Multi-word seeds resolve deterministically at each threshold."""

    @pytest.mark.parametrize(('text', 'word1', 'word2', 'threshold', 'expected', 'level', 'uid',), _MULTIWORD_VERDICT_CASES)
    def test_multiword_verdict(self, engine: ModerationEngine, word_bank: Any, text: str, word1: str, word2: str, threshold: int, expected: str, level: int, uid: int) -> None:
        """Multi-word seeds resolve deterministically at each threshold."""
        word_bank.add_word(word1)
        word_bank.add_word(word2)
        engine.refresh_detectors()
        engine._app_config.update_default_threshold(threshold)
        result: ModerationResponse = engine.moderate(
            ModerationRequest(text=text, app_name='a', user_id='u')
        )
        assert result.verdict.value == expected
        assert result.level_used == level
