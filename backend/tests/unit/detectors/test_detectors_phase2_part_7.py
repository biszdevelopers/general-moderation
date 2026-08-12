"""Phase 2 detector tests (golden master, generated).

Computed from the locked test environment; see tests/tools/phase2_generator.py."""

# ruff: noqa: RUF001  # multilingual fixtures use non-ASCII on purpose
from __future__ import annotations

from typing import Any

import pytest

from app.config import Settings
from app.detectors.multi_language_detector import MultiLanguageDetector
from tests.base_test import BaseTest

_PROFANITE_MATRIX_CASES: tuple[tuple[str, str, bool, int], ...] = (
    (
        "en",
        "message with fuck",
        True,
        601,
    ),
    (
        "zh-CN",
        "message with 妈的",
        False,
        603,
    ),
    (
        "ja",
        "message with くそ",
        False,
        605,
    ),
    (
        "ko",
        "message with 씨발",
        False,
        607,
    ),
    (
        "ru",
        "message with блядь",
        False,
        609,
    ),
    (
        "es",
        "message with joder",
        False,
        611,
    ),
    (
        "fr",
        "message with merde",
        False,
        613,
    ),
    (
        "de",
        "message with scheiße",
        False,
        615,
    ),
    (
        "it",
        "message with cazzo",
        False,
        617,
    ),
    (
        "ar",
        "message with سحقا",
        False,
        619,
    ),
    (
        "hi",
        "message with गांड",
        False,
        621,
    ),
    (
        "tr",
        "message with siktir",
        False,
        623,
    ),
    (
        "pt",
        "message with caralho",
        False,
        625,
    ),
    (
        "nl",
        "message with kut",
        False,
        627,
    ),
    (
        "pl",
        "message with kurwa",
        False,
        629,
    ),
    (
        "uk",
        "message with бляха",
        False,
        631,
    ),
    (
        "cs",
        "message with kurva",
        False,
        633,
    ),
    (
        "el",
        "message with γαμώ",
        False,
        635,
    ),
    (
        "sv",
        "message with fan",
        False,
        637,
    ),
    (
        "no",
        "message with faen",
        False,
        639,
    ),
    (
        "da",
        "message with fand",
        False,
        641,
    ),
    (
        "fi",
        "message with vittu",
        False,
        643,
    ),
    (
        "hu",
        "message with baszd",
        False,
        645,
    ),
    (
        "ro",
        "message with pula",
        False,
        647,
    ),
    (
        "bg",
        "message with майната",
        False,
        649,
    ),
    (
        "he",
        "message with זין",
        False,
        651,
    ),
    (
        "th",
        "message with เหี้ย",
        False,
        653,
    ),
)


class TestProfaniteMatrix(BaseTest):
    """profanite reproduces the golden match flag over en."""

    @pytest.mark.parametrize(
        (
            "language",
            "text",
            "expected",
            "uid",
        ),
        _PROFANITE_MATRIX_CASES,
    )
    def test_profanite_matrix(
        self, engine: Any, language: str, text: str, expected: bool, uid: int
    ) -> None:
        """profanite reproduces the golden match flag over en."""
        settings: Settings = engine._settings
        settings.enable_profanite = True
        for key in (
            "enable_badwords_py",
            "enable_profanite",
            "enable_glin_profanity",
            "enable_gangajal",
        ):
            if key != "enable_profanite":
                setattr(settings, key, False)
        detector: MultiLanguageDetector = MultiLanguageDetector(settings, None)
        assert detector.detect(text).matched is expected


_PROFANITE_CLEAN_CASES: tuple[tuple[str, str, bool, int], ...] = (
    (
        "en",
        "the weather is pleasant today",
        False,
        602,
    ),
    (
        "zh-CN",
        "今天天气不错",
        False,
        604,
    ),
    (
        "ja",
        "今日は天気が良いです",
        False,
        606,
    ),
    (
        "ko",
        "오늘 날씨가 좋아요",
        False,
        608,
    ),
    (
        "ru",
        "сегодня хорошая погода",
        False,
        610,
    ),
    (
        "es",
        "hoy hace buen tiempo",
        False,
        612,
    ),
    (
        "fr",
        "il fait beau aujourd'hui",
        False,
        614,
    ),
    (
        "de",
        "das wetter ist schön heute",
        False,
        616,
    ),
    (
        "it",
        "oggi il tempo è bello",
        False,
        618,
    ),
    (
        "ar",
        "الطقس جميل اليوم",
        False,
        620,
    ),
    (
        "hi",
        "आज मौसम अच्छा है",
        False,
        622,
    ),
    (
        "tr",
        "bugün hava güzel",
        False,
        624,
    ),
    (
        "pt",
        "o tempo está bom hoje",
        False,
        626,
    ),
    (
        "nl",
        "het weer is mooi vandaag",
        False,
        628,
    ),
    (
        "pl",
        "dzisiaj jest ładna pogoda",
        False,
        630,
    ),
    (
        "uk",
        "сьогодні гарна погода",
        False,
        632,
    ),
    (
        "cs",
        "dnes je hezké počasí",
        False,
        634,
    ),
    (
        "el",
        "σήμερα έχει καλό καιρό",
        False,
        636,
    ),
    (
        "sv",
        "vädret är fint idag",
        False,
        638,
    ),
    (
        "no",
        "været er fint i dag",
        False,
        640,
    ),
    (
        "da",
        "vejret er dejligt i dag",
        False,
        642,
    ),
    (
        "fi",
        "tänään on kaunis sää",
        False,
        644,
    ),
    (
        "hu",
        "ma szép az idő",
        False,
        646,
    ),
    (
        "ro",
        "astăzi este vreme frumoasă",
        False,
        648,
    ),
    (
        "bg",
        "днес е хубаво време",
        False,
        650,
    ),
    (
        "he",
        "מזג האוויר נחמד היום",
        False,
        652,
    ),
    (
        "th",
        "วันนี้อากาศดี",
        False,
        654,
    ),
)


class TestProfaniteClean(BaseTest):
    """profanite reproduces the golden match flag over en."""

    @pytest.mark.parametrize(
        (
            "language",
            "text",
            "expected",
            "uid",
        ),
        _PROFANITE_CLEAN_CASES,
    )
    def test_profanite_clean(
        self, engine: Any, language: str, text: str, expected: bool, uid: int
    ) -> None:
        """profanite reproduces the golden match flag over en."""
        settings: Settings = engine._settings
        settings.enable_profanite = True
        for key in (
            "enable_badwords_py",
            "enable_profanite",
            "enable_glin_profanity",
            "enable_gangajal",
        ):
            if key != "enable_profanite":
                setattr(settings, key, False)
        detector: MultiLanguageDetector = MultiLanguageDetector(settings, None)
        assert detector.detect(text).matched is expected


_PROFANITE_LEET_CASES: tuple[tuple[str, str, bool, int], ...] = (
    (
        "en",
        "check fuck",
        True,
        655,
    ),
    (
        "zh-CN",
        "check 妈的",
        False,
        656,
    ),
    (
        "ja",
        "check くそ",
        False,
        657,
    ),
    (
        "ko",
        "check 씨발",
        False,
        658,
    ),
    (
        "ru",
        "check блядь",
        False,
        659,
    ),
    (
        "es",
        "check j0d3r",
        False,
        660,
    ),
    (
        "fr",
        "check m3rd3",
        False,
        661,
    ),
    (
        "de",
        "check $ch31ß3",
        False,
        662,
    ),
    (
        "it",
        "check c@zz0",
        False,
        663,
    ),
    (
        "ar",
        "check سحقا",
        False,
        664,
    ),
    (
        "hi",
        "check गांड",
        False,
        665,
    ),
    (
        "tr",
        "check $1kt1r",
        False,
        666,
    ),
    (
        "pt",
        "check c@r@lh0",
        False,
        667,
    ),
    (
        "nl",
        "check kut",
        False,
        668,
    ),
    (
        "pl",
        "check kurw@",
        False,
        669,
    ),
    (
        "uk",
        "check бляха",
        False,
        670,
    ),
    (
        "cs",
        "check kurv@",
        False,
        671,
    ),
    (
        "el",
        "check γαμώ",
        False,
        672,
    ),
    (
        "sv",
        "check f@n",
        False,
        673,
    ),
    (
        "no",
        "check f@3n",
        False,
        674,
    ),
    (
        "da",
        "check f@nd",
        False,
        675,
    ),
    (
        "fi",
        "check v1ttu",
        False,
        676,
    ),
    (
        "hu",
        "check b@$zd",
        False,
        677,
    ),
    (
        "ro",
        "check pul@",
        False,
        678,
    ),
    (
        "bg",
        "check майната",
        False,
        679,
    ),
    (
        "he",
        "check זין",
        False,
        680,
    ),
    (
        "th",
        "check เหี้ย",
        False,
        681,
    ),
)


class TestProfaniteLeet(BaseTest):
    """profanite reproduces the golden match flag over en."""

    @pytest.mark.parametrize(
        (
            "language",
            "text",
            "expected",
            "uid",
        ),
        _PROFANITE_LEET_CASES,
    )
    def test_profanite_leet(
        self, engine: Any, language: str, text: str, expected: bool, uid: int
    ) -> None:
        """profanite reproduces the golden match flag over en."""
        settings: Settings = engine._settings
        settings.enable_profanite = True
        for key in (
            "enable_badwords_py",
            "enable_profanite",
            "enable_glin_profanity",
            "enable_gangajal",
        ):
            if key != "enable_profanite":
                setattr(settings, key, False)
        detector: MultiLanguageDetector = MultiLanguageDetector(settings, None)
        assert detector.detect(text).matched is expected


_PROFANITE_LEETSPEAK_CASES: tuple[tuple[str, str, bool, int], ...] = (
    (
        "en",
        "fuck fuck",
        True,
        682,
    ),
    (
        "zh-CN",
        "妈的 妈的",
        False,
        683,
    ),
    (
        "ja",
        "くそ くそ",
        False,
        684,
    ),
    (
        "ko",
        "씨발 씨발",
        False,
        685,
    ),
    (
        "ru",
        "блядь блядь",
        False,
        686,
    ),
    (
        "es",
        "j0d3r j0d3r",
        False,
        687,
    ),
    (
        "fr",
        "m3rd3 m3rd3",
        False,
        688,
    ),
    (
        "de",
        "$ch31ß3 $ch31ß3",
        False,
        689,
    ),
    (
        "it",
        "c@zz0 c@zz0",
        False,
        690,
    ),
    (
        "ar",
        "سحقا سحقا",
        False,
        691,
    ),
    (
        "hi",
        "गांड गांड",
        False,
        692,
    ),
    (
        "tr",
        "$1kt1r $1kt1r",
        False,
        693,
    ),
    (
        "pt",
        "c@r@lh0 c@r@lh0",
        False,
        694,
    ),
    (
        "nl",
        "kut kut",
        False,
        695,
    ),
    (
        "pl",
        "kurw@ kurw@",
        False,
        696,
    ),
    (
        "uk",
        "бляха бляха",
        False,
        697,
    ),
    (
        "cs",
        "kurv@ kurv@",
        False,
        698,
    ),
    (
        "el",
        "γαμώ γαμώ",
        False,
        699,
    ),
    (
        "sv",
        "f@n f@n",
        False,
        700,
    ),
)


class TestProfaniteLeetspeak(BaseTest):
    """profanite reproduces the golden match flag over en."""

    @pytest.mark.parametrize(
        (
            "language",
            "text",
            "expected",
            "uid",
        ),
        _PROFANITE_LEETSPEAK_CASES,
    )
    def test_profanite_leetspeak(
        self, engine: Any, language: str, text: str, expected: bool, uid: int
    ) -> None:
        """profanite reproduces the golden match flag over en."""
        settings: Settings = engine._settings
        settings.enable_profanite = True
        for key in (
            "enable_badwords_py",
            "enable_profanite",
            "enable_glin_profanity",
            "enable_gangajal",
        ):
            if key != "enable_profanite":
                setattr(settings, key, False)
        detector: MultiLanguageDetector = MultiLanguageDetector(settings, None)
        assert detector.detect(text).matched is expected
