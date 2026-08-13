"""Phase 2 detector tests (golden master, generated).

Computed from the locked test environment; see tests/tools/phase2_generator.py."""

# ruff: noqa: RUF001  # multilingual fixtures use non-ASCII on purpose
from __future__ import annotations

from typing import Any

import pytest

from app.config import Settings
from app.detectors.multi_language_detector import MultiLanguageDetector
from tests.base_test import BaseTest

_BADWORDS_MATRIX_CASES: tuple[tuple[str, str, bool, int], ...] = (
    ('he', 'this is זין here', False, 501,),
    ('th', 'this is เหี้ย here', True, 503,),
)

class TestBadwordsMatrix(BaseTest):
    """badwords-py reproduces the golden match flag over he."""

    @pytest.mark.parametrize(('language', 'text', 'expected', 'uid',), _BADWORDS_MATRIX_CASES)
    def test_badwords_matrix(self, engine: Any, language: str, text: str, expected: bool, uid: int) -> None:
        """badwords-py reproduces the golden match flag over he."""
        settings: Settings = engine._settings
        settings.enable_badwords_py = True
        for key in ("enable_badwords_py", "enable_profanite", "enable_glin_profanity",
                    "enable_gangajal"):
            if key != "enable_badwords_py":
                setattr(settings, key, False)
        detector: MultiLanguageDetector = MultiLanguageDetector(settings, None)
        assert detector.detect(text).matched is expected


_BADWORDS_CLEAN_CASES: tuple[tuple[str, str, bool, int], ...] = (
    ('he', 'מזג האוויר נחמד היום', False, 502,),
    ('th', 'วันนี้อากาศดี', False, 504,),
)

class TestBadwordsClean(BaseTest):
    """badwords-py reproduces the golden match flag over he."""

    @pytest.mark.parametrize(('language', 'text', 'expected', 'uid',), _BADWORDS_CLEAN_CASES)
    def test_badwords_clean(self, engine: Any, language: str, text: str, expected: bool, uid: int) -> None:
        """badwords-py reproduces the golden match flag over he."""
        settings: Settings = engine._settings
        settings.enable_badwords_py = True
        for key in ("enable_badwords_py", "enable_profanite", "enable_glin_profanity",
                    "enable_gangajal"):
            if key != "enable_badwords_py":
                setattr(settings, key, False)
        detector: MultiLanguageDetector = MultiLanguageDetector(settings, None)
        assert detector.detect(text).matched is expected


_BADWORDS_MASKED_CASES: tuple[tuple[str, str, bool, int], ...] = (
    ('en', 'word f*ck', True, 505,),
    ('zh-CN', 'word 妈的', False, 506,),
    ('ja', 'word くそ', True, 507,),
    ('ko', 'word 씨발', True, 508,),
    ('ru', 'word б*ядь', False, 509,),
    ('es', 'word j*der', False, 510,),
    ('fr', 'word m*rde', False, 511,),
    ('de', 'word s*heiße', False, 512,),
    ('it', 'word c*zzo', False, 513,),
    ('ar', 'word س*قا', False, 514,),
    ('hi', 'word ग*ंड', False, 515,),
    ('tr', 'word s*ktir', True, 516,),
    ('pt', 'word c*ralho', False, 517,),
    ('nl', 'word k*t', False, 518,),
    ('pl', 'word k*rwa', False, 519,),
    ('uk', 'word б*яха', False, 520,),
    ('cs', 'word k*rva', False, 521,),
    ('el', 'word γ*μώ', False, 522,),
    ('sv', 'word f*n', False, 523,),
    ('no', 'word f*en', False, 524,),
    ('da', 'word f*nd', False, 525,),
    ('fi', 'word v*ttu', False, 526,),
    ('hu', 'word b*szd', False, 527,),
    ('ro', 'word p*la', False, 528,),
    ('bg', 'word м*йната', False, 529,),
    ('he', 'word ז*ן', False, 530,),
    ('th', 'word เ*ี้ย', False, 531,),
)

class TestBadwordsMasked(BaseTest):
    """badwords-py reproduces the golden match flag over en."""

    @pytest.mark.parametrize(('language', 'text', 'expected', 'uid',), _BADWORDS_MASKED_CASES)
    def test_badwords_masked(self, engine: Any, language: str, text: str, expected: bool, uid: int) -> None:
        """badwords-py reproduces the golden match flag over en."""
        settings: Settings = engine._settings
        settings.enable_badwords_py = True
        for key in ("enable_badwords_py", "enable_profanite", "enable_glin_profanity",
                    "enable_gangajal"):
            if key != "enable_badwords_py":
                setattr(settings, key, False)
        detector: MultiLanguageDetector = MultiLanguageDetector(settings, None)
        assert detector.detect(text).matched is expected


_BADWORDS_LONG_CASES: tuple[tuple[str, str, bool, int], ...] = (
    ('en', 'fuck fuck fuck fuck fuck fuck fuck fuck fuck fuck fuck fuck fuck fuck fuck fuck fuck fuck fuck fuck fuck fuck fuck fuck fuck fuck fuck fuck fuck fuck fuck fuck fuck fuck fuck fuck fuck fuck fuck fuck', True, 532,),
    ('zh-CN', '妈的 妈的 妈的 妈的 妈的 妈的 妈的 妈的 妈的 妈的 妈的 妈的 妈的 妈的 妈的 妈的 妈的 妈的 妈的 妈的 妈的 妈的 妈的 妈的 妈的 妈的 妈的 妈的 妈的 妈的 妈的 妈的 妈的 妈的 妈的 妈的 妈的 妈的 妈的 妈的', False, 533,),
    ('ja', 'くそ くそ くそ くそ くそ くそ くそ くそ くそ くそ くそ くそ くそ くそ くそ くそ くそ くそ くそ くそ くそ くそ くそ くそ くそ くそ くそ くそ くそ くそ くそ くそ くそ くそ くそ くそ くそ くそ くそ くそ', True, 534,),
    ('ko', '씨발 씨발 씨발 씨발 씨발 씨발 씨발 씨발 씨발 씨발 씨발 씨발 씨발 씨발 씨발 씨발 씨발 씨발 씨발 씨발 씨발 씨발 씨발 씨발 씨발 씨발 씨발 씨발 씨발 씨발 씨발 씨발 씨발 씨발 씨발 씨발 씨발 씨발 씨발 씨발', True, 535,),
    ('ru', 'блядь блядь блядь блядь блядь блядь блядь блядь блядь блядь блядь блядь блядь блядь блядь блядь блядь блядь блядь блядь блядь блядь блядь блядь блядь блядь блядь блядь блядь блядь блядь блядь блядь блядь блядь блядь блядь блядь блядь блядь', True, 536,),
    ('es', 'joder joder joder joder joder joder joder joder joder joder joder joder joder joder joder joder joder joder joder joder joder joder joder joder joder joder joder joder joder joder joder joder joder joder joder joder joder joder joder joder', True, 537,),
    ('fr', 'merde merde merde merde merde merde merde merde merde merde merde merde merde merde merde merde merde merde merde merde merde merde merde merde merde merde merde merde merde merde merde merde merde merde merde merde merde merde merde merde', True, 538,),
    ('de', 'scheiße scheiße scheiße scheiße scheiße scheiße scheiße scheiße scheiße scheiße scheiße scheiße scheiße scheiße scheiße scheiße scheiße scheiße scheiße scheiße scheiße scheiße scheiße scheiße scheiße scheiße scheiße scheiße scheiße scheiße scheiße scheiße scheiße scheiße scheiße scheiße scheiße scheiße scheiße scheiße', False, 539,),
    ('it', 'cazzo cazzo cazzo cazzo cazzo cazzo cazzo cazzo cazzo cazzo cazzo cazzo cazzo cazzo cazzo cazzo cazzo cazzo cazzo cazzo cazzo cazzo cazzo cazzo cazzo cazzo cazzo cazzo cazzo cazzo cazzo cazzo cazzo cazzo cazzo cazzo cazzo cazzo cazzo cazzo', False, 540,),
    ('ar', 'سحقا سحقا سحقا سحقا سحقا سحقا سحقا سحقا سحقا سحقا سحقا سحقا سحقا سحقا سحقا سحقا سحقا سحقا سحقا سحقا سحقا سحقا سحقا سحقا سحقا سحقا سحقا سحقا سحقا سحقا سحقا سحقا سحقا سحقا سحقا سحقا سحقا سحقا سحقا سحقا', False, 541,),
)

class TestBadwordsLong(BaseTest):
    """badwords-py reproduces the golden match flag over en."""

    @pytest.mark.parametrize(('language', 'text', 'expected', 'uid',), _BADWORDS_LONG_CASES)
    def test_badwords_long(self, engine: Any, language: str, text: str, expected: bool, uid: int) -> None:
        """badwords-py reproduces the golden match flag over en."""
        settings: Settings = engine._settings
        settings.enable_badwords_py = True
        for key in ("enable_badwords_py", "enable_profanite", "enable_glin_profanity",
                    "enable_gangajal"):
            if key != "enable_badwords_py":
                setattr(settings, key, False)
        detector: MultiLanguageDetector = MultiLanguageDetector(settings, None)
        assert detector.detect(text).matched is expected


_BADWORDS_UPPER_CASES: tuple[tuple[str, str, bool, int], ...] = (
    ('en', 'FUCK', True, 542,),
    ('zh-CN', '妈的', False, 543,),
    ('ja', 'くそ', True, 544,),
    ('ko', '씨발', True, 545,),
    ('ru', 'БЛЯДЬ', True, 546,),
    ('es', 'JODER', True, 547,),
    ('fr', 'MERDE', True, 548,),
    ('de', 'SCHEISSE', False, 549,),
    ('it', 'CAZZO', False, 550,),
    ('ar', 'سحقا', False, 551,),
    ('hi', 'गांड', False, 552,),
    ('tr', 'SIKTIR', False, 553,),
    ('pt', 'CARALHO', False, 554,),
    ('nl', 'KUT', True, 555,),
    ('pl', 'KURWA', True, 556,),
    ('uk', 'БЛЯХА', False, 557,),
    ('cs', 'KURVA', True, 558,),
    ('el', 'ΓΑΜΏ', True, 559,),
    ('sv', 'FAN', False, 560,),
    ('no', 'FAEN', True, 561,),
    ('da', 'FAND', False, 562,),
    ('fi', 'VITTU', False, 563,),
    ('hu', 'BASZD', False, 564,),
    ('ro', 'PULA', True, 565,),
    ('bg', 'МАЙНАТА', False, 566,),
    ('he', 'זין', False, 567,),
    ('th', 'เหี้ย', True, 568,),
)

class TestBadwordsUpper(BaseTest):
    """badwords-py reproduces the golden match flag over en."""

    @pytest.mark.parametrize(('language', 'text', 'expected', 'uid',), _BADWORDS_UPPER_CASES)
    def test_badwords_upper(self, engine: Any, language: str, text: str, expected: bool, uid: int) -> None:
        """badwords-py reproduces the golden match flag over en."""
        settings: Settings = engine._settings
        settings.enable_badwords_py = True
        for key in ("enable_badwords_py", "enable_profanite", "enable_glin_profanity",
                    "enable_gangajal"):
            if key != "enable_badwords_py":
                setattr(settings, key, False)
        detector: MultiLanguageDetector = MultiLanguageDetector(settings, None)
        assert detector.detect(text).matched is expected


_BADWORDS_REPEAT_CASES: tuple[tuple[str, str, bool, int], ...] = (
    ('en', 'fuck and fuck again', True, 569,),
    ('zh-CN', '妈的 and 妈的 again', False, 570,),
    ('ja', 'くそ and くそ again', True, 571,),
    ('ko', '씨발 and 씨발 again', True, 572,),
    ('ru', 'блядь and блядь again', True, 573,),
    ('es', 'joder and joder again', True, 574,),
    ('fr', 'merde and merde again', True, 575,),
    ('de', 'scheiße and scheiße again', False, 576,),
    ('it', 'cazzo and cazzo again', False, 577,),
    ('ar', 'سحقا and سحقا again', False, 578,),
    ('hi', 'गांड and गांड again', False, 579,),
    ('tr', 'siktir and siktir again', False, 580,),
    ('pt', 'caralho and caralho again', False, 581,),
    ('nl', 'kut and kut again', True, 582,),
    ('pl', 'kurwa and kurwa again', True, 583,),
    ('uk', 'бляха and бляха again', False, 584,),
    ('cs', 'kurva and kurva again', True, 585,),
    ('el', 'γαμώ and γαμώ again', True, 586,),
    ('sv', 'fan and fan again', False, 587,),
    ('no', 'faen and faen again', True, 588,),
    ('da', 'fand and fand again', False, 589,),
    ('fi', 'vittu and vittu again', False, 590,),
    ('hu', 'baszd and baszd again', False, 591,),
    ('ro', 'pula and pula again', True, 592,),
    ('bg', 'майната and майната again', False, 593,),
    ('he', 'זין and זין again', False, 594,),
    ('th', 'เหี้ย and เหี้ย again', True, 595,),
)

class TestBadwordsRepeat(BaseTest):
    """badwords-py reproduces the golden match flag over en."""

    @pytest.mark.parametrize(('language', 'text', 'expected', 'uid',), _BADWORDS_REPEAT_CASES)
    def test_badwords_repeat(self, engine: Any, language: str, text: str, expected: bool, uid: int) -> None:
        """badwords-py reproduces the golden match flag over en."""
        settings: Settings = engine._settings
        settings.enable_badwords_py = True
        for key in ("enable_badwords_py", "enable_profanite", "enable_glin_profanity",
                    "enable_gangajal"):
            if key != "enable_badwords_py":
                setattr(settings, key, False)
        detector: MultiLanguageDetector = MultiLanguageDetector(settings, None)
        assert detector.detect(text).matched is expected


_BADWORDS_LONGEST_CASES: tuple[tuple[str, str, bool, int], ...] = (
    ('en', 'fuck fuck fuck fuck fuck fuck fuck fuck fuck fuck fuck fuck fuck fuck fuck fuck fuck fuck fuck fuck fuck fuck fuck fuck fuck fuck fuck fuck fuck fuck fuck fuck fuck fuck fuck fuck fuck fuck fuck fuck fuck fuck fuck fuck fuck fuck fuck fuck fuck fuck fuck fuck fuck fuck fuck fuck fuck fuck fuck fuck fuck fuck fuck fuck fuck fuck fuck fuck fuck fuck fuck fuck fuck fuck fuck fuck fuck fuck fuck fuck fuck fuck fuck fuck fuck fuck fuck fuck fuck fuck fuck fuck fuck fuck fuck fuck fuck fuck fuck fuck fuck fuck fuck fuck fuck fuck fuck fuck fuck fuck fuck fuck fuck fuck fuck fuck fuck fuck fuck fuck fuck fuck fuck fuck fuck fuck fuck fuck fuck fuck fuck fuck fuck fuck fuck fuck fuck fuck fuck fuck fuck fuck fuck fuck fuck fuck fuck fuck fuck fuck', True, 596,),
    ('zh-CN', '妈的 妈的 妈的 妈的 妈的 妈的 妈的 妈的 妈的 妈的 妈的 妈的 妈的 妈的 妈的 妈的 妈的 妈的 妈的 妈的 妈的 妈的 妈的 妈的 妈的 妈的 妈的 妈的 妈的 妈的 妈的 妈的 妈的 妈的 妈的 妈的 妈的 妈的 妈的 妈的 妈的 妈的 妈的 妈的 妈的 妈的 妈的 妈的 妈的 妈的 妈的 妈的 妈的 妈的 妈的 妈的 妈的 妈的 妈的 妈的 妈的 妈的 妈的 妈的 妈的 妈的 妈的 妈的 妈的 妈的 妈的 妈的 妈的 妈的 妈的 妈的 妈的 妈的 妈的 妈的 妈的 妈的 妈的 妈的 妈的 妈的 妈的 妈的 妈的 妈的 妈的 妈的 妈的 妈的 妈的 妈的 妈的 妈的 妈的 妈的 妈的 妈的 妈的 妈的 妈的 妈的 妈的 妈的 妈的 妈的 妈的 妈的 妈的 妈的 妈的 妈的 妈的 妈的 妈的 妈的 妈的 妈的 妈的 妈的 妈的 妈的 妈的 妈的 妈的 妈的 妈的 妈的 妈的 妈的 妈的 妈的 妈的 妈的 妈的 妈的 妈的 妈的 妈的 妈的 妈的 妈的 妈的 妈的 妈的 妈的', False, 597,),
    ('ja', 'くそ くそ くそ くそ くそ くそ くそ くそ くそ くそ くそ くそ くそ くそ くそ くそ くそ くそ くそ くそ くそ くそ くそ くそ くそ くそ くそ くそ くそ くそ くそ くそ くそ くそ くそ くそ くそ くそ くそ くそ くそ くそ くそ くそ くそ くそ くそ くそ くそ くそ くそ くそ くそ くそ くそ くそ くそ くそ くそ くそ くそ くそ くそ くそ くそ くそ くそ くそ くそ くそ くそ くそ くそ くそ くそ くそ くそ くそ くそ くそ くそ くそ くそ くそ くそ くそ くそ くそ くそ くそ くそ くそ くそ くそ くそ くそ くそ くそ くそ くそ くそ くそ くそ くそ くそ くそ くそ くそ くそ くそ くそ くそ くそ くそ くそ くそ くそ くそ くそ くそ くそ くそ くそ くそ くそ くそ くそ くそ くそ くそ くそ くそ くそ くそ くそ くそ くそ くそ くそ くそ くそ くそ くそ くそ くそ くそ くそ くそ くそ くそ', True, 598,),
    ('ko', '씨발 씨발 씨발 씨발 씨발 씨발 씨발 씨발 씨발 씨발 씨발 씨발 씨발 씨발 씨발 씨발 씨발 씨발 씨발 씨발 씨발 씨발 씨발 씨발 씨발 씨발 씨발 씨발 씨발 씨발 씨발 씨발 씨발 씨발 씨발 씨발 씨발 씨발 씨발 씨발 씨발 씨발 씨발 씨발 씨발 씨발 씨발 씨발 씨발 씨발 씨발 씨발 씨발 씨발 씨발 씨발 씨발 씨발 씨발 씨발 씨발 씨발 씨발 씨발 씨발 씨발 씨발 씨발 씨발 씨발 씨발 씨발 씨발 씨발 씨발 씨발 씨발 씨발 씨발 씨발 씨발 씨발 씨발 씨발 씨발 씨발 씨발 씨발 씨발 씨발 씨발 씨발 씨발 씨발 씨발 씨발 씨발 씨발 씨발 씨발 씨발 씨발 씨발 씨발 씨발 씨발 씨발 씨발 씨발 씨발 씨발 씨발 씨발 씨발 씨발 씨발 씨발 씨발 씨발 씨발 씨발 씨발 씨발 씨발 씨발 씨발 씨발 씨발 씨발 씨발 씨발 씨발 씨발 씨발 씨발 씨발 씨발 씨발 씨발 씨발 씨발 씨발 씨발 씨발 씨발 씨발 씨발 씨발 씨발 씨발', True, 599,),
    ('ru', 'блядь блядь блядь блядь блядь блядь блядь блядь блядь блядь блядь блядь блядь блядь блядь блядь блядь блядь блядь блядь блядь блядь блядь блядь блядь блядь блядь блядь блядь блядь блядь блядь блядь блядь блядь блядь блядь блядь блядь блядь блядь блядь блядь блядь блядь блядь блядь блядь блядь блядь блядь блядь блядь блядь блядь блядь блядь блядь блядь блядь блядь блядь блядь блядь блядь блядь блядь блядь блядь блядь блядь блядь блядь блядь блядь блядь блядь блядь блядь блядь блядь блядь блядь блядь блядь блядь блядь блядь блядь блядь блядь блядь блядь блядь блядь блядь блядь блядь блядь блядь блядь блядь блядь блядь блядь блядь блядь блядь блядь блядь блядь блядь блядь блядь блядь блядь блядь блядь блядь блядь блядь блядь блядь блядь блядь блядь блядь блядь блядь блядь блядь блядь блядь блядь блядь блядь блядь блядь блядь блядь блядь блядь блядь блядь блядь блядь блядь блядь блядь блядь', True, 600,),
)

class TestBadwordsLongest(BaseTest):
    """badwords-py reproduces the golden match flag over en."""

    @pytest.mark.parametrize(('language', 'text', 'expected', 'uid',), _BADWORDS_LONGEST_CASES)
    def test_badwords_longest(self, engine: Any, language: str, text: str, expected: bool, uid: int) -> None:
        """badwords-py reproduces the golden match flag over en."""
        settings: Settings = engine._settings
        settings.enable_badwords_py = True
        for key in ("enable_badwords_py", "enable_profanite", "enable_glin_profanity",
                    "enable_gangajal"):
            if key != "enable_badwords_py":
                setattr(settings, key, False)
        detector: MultiLanguageDetector = MultiLanguageDetector(settings, None)
        assert detector.detect(text).matched is expected
