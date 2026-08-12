"""Phase 2 detector tests (golden master, generated).

Computed from the locked test environment; see tests/tools/phase2_generator.py."""

# ruff: noqa: RUF001  # multilingual fixtures use non-ASCII on purpose
from __future__ import annotations

from typing import Any

import pytest

from app.config import Settings
from app.detectors.multi_language_detector import MultiLanguageDetector
from tests.base_test import BaseTest

_GLIN_MATRIX_CASES: tuple[tuple[str, str, bool, int], ...] = (
    (
        "en",
        "stop saying fuck",
        True,
        701,
    ),
    (
        "zh-CN",
        "stop saying 妈的",
        False,
        703,
    ),
    (
        "ja",
        "stop saying くそ",
        False,
        705,
    ),
    (
        "ko",
        "stop saying 씨발",
        False,
        707,
    ),
    (
        "ru",
        "stop saying блядь",
        False,
        709,
    ),
    (
        "es",
        "stop saying joder",
        False,
        711,
    ),
    (
        "fr",
        "stop saying merde",
        False,
        713,
    ),
    (
        "de",
        "stop saying scheiße",
        False,
        715,
    ),
    (
        "it",
        "stop saying cazzo",
        False,
        717,
    ),
    (
        "ar",
        "stop saying سحقا",
        False,
        719,
    ),
    (
        "hi",
        "stop saying गांड",
        False,
        721,
    ),
    (
        "tr",
        "stop saying siktir",
        False,
        723,
    ),
    (
        "pt",
        "stop saying caralho",
        False,
        725,
    ),
    (
        "nl",
        "stop saying kut",
        False,
        727,
    ),
    (
        "pl",
        "stop saying kurwa",
        False,
        729,
    ),
    (
        "uk",
        "stop saying бляха",
        False,
        731,
    ),
    (
        "cs",
        "stop saying kurva",
        False,
        733,
    ),
    (
        "el",
        "stop saying γαμώ",
        False,
        735,
    ),
    (
        "sv",
        "stop saying fan",
        False,
        737,
    ),
    (
        "no",
        "stop saying faen",
        False,
        739,
    ),
    (
        "da",
        "stop saying fand",
        False,
        741,
    ),
    (
        "fi",
        "stop saying vittu",
        False,
        743,
    ),
    (
        "hu",
        "stop saying baszd",
        False,
        745,
    ),
    (
        "ro",
        "stop saying pula",
        False,
        747,
    ),
    (
        "bg",
        "stop saying майната",
        False,
        749,
    ),
    (
        "he",
        "stop saying זין",
        False,
        751,
    ),
    (
        "th",
        "stop saying เหี้ย",
        False,
        753,
    ),
)


class TestGlinMatrix(BaseTest):
    """glin-profanity reproduces the golden match flag over en."""

    @pytest.mark.parametrize(
        (
            "language",
            "text",
            "expected",
            "uid",
        ),
        _GLIN_MATRIX_CASES,
    )
    def test_glin_matrix(
        self, engine: Any, language: str, text: str, expected: bool, uid: int
    ) -> None:
        """glin-profanity reproduces the golden match flag over en."""
        settings: Settings = engine._settings
        settings.enable_glin_profanity = True
        for key in (
            "enable_badwords_py",
            "enable_profanite",
            "enable_glin_profanity",
            "enable_gangajal",
        ):
            if key != "enable_glin_profanity":
                setattr(settings, key, False)
        detector: MultiLanguageDetector = MultiLanguageDetector(settings, None)
        assert detector.detect(text).matched is expected


_GLIN_CLEAN_CASES: tuple[tuple[str, str, bool, int], ...] = (
    (
        "en",
        "the weather is pleasant today",
        False,
        702,
    ),
    (
        "zh-CN",
        "今天天气不错",
        False,
        704,
    ),
    (
        "ja",
        "今日は天気が良いです",
        False,
        706,
    ),
    (
        "ko",
        "오늘 날씨가 좋아요",
        False,
        708,
    ),
    (
        "ru",
        "сегодня хорошая погода",
        False,
        710,
    ),
    (
        "es",
        "hoy hace buen tiempo",
        False,
        712,
    ),
    (
        "fr",
        "il fait beau aujourd'hui",
        False,
        714,
    ),
    (
        "de",
        "das wetter ist schön heute",
        False,
        716,
    ),
    (
        "it",
        "oggi il tempo è bello",
        False,
        718,
    ),
    (
        "ar",
        "الطقس جميل اليوم",
        False,
        720,
    ),
    (
        "hi",
        "आज मौसम अच्छा है",
        False,
        722,
    ),
    (
        "tr",
        "bugün hava güzel",
        False,
        724,
    ),
    (
        "pt",
        "o tempo está bom hoje",
        True,
        726,
    ),
    (
        "nl",
        "het weer is mooi vandaag",
        False,
        728,
    ),
    (
        "pl",
        "dzisiaj jest ładna pogoda",
        False,
        730,
    ),
    (
        "uk",
        "сьогодні гарна погода",
        False,
        732,
    ),
    (
        "cs",
        "dnes je hezké počasí",
        False,
        734,
    ),
    (
        "el",
        "σήμερα έχει καλό καιρό",
        False,
        736,
    ),
    (
        "sv",
        "vädret är fint idag",
        False,
        738,
    ),
    (
        "no",
        "været er fint i dag",
        False,
        740,
    ),
    (
        "da",
        "vejret er dejligt i dag",
        False,
        742,
    ),
    (
        "fi",
        "tänään on kaunis sää",
        False,
        744,
    ),
    (
        "hu",
        "ma szép az idő",
        False,
        746,
    ),
    (
        "ro",
        "astăzi este vreme frumoasă",
        False,
        748,
    ),
    (
        "bg",
        "днес е хубаво време",
        False,
        750,
    ),
    (
        "he",
        "מזג האוויר נחמד היום",
        False,
        752,
    ),
    (
        "th",
        "วันนี้อากาศดี",
        False,
        754,
    ),
)


class TestGlinClean(BaseTest):
    """glin-profanity reproduces the golden match flag over en."""

    @pytest.mark.parametrize(
        (
            "language",
            "text",
            "expected",
            "uid",
        ),
        _GLIN_CLEAN_CASES,
    )
    def test_glin_clean(
        self, engine: Any, language: str, text: str, expected: bool, uid: int
    ) -> None:
        """glin-profanity reproduces the golden match flag over en."""
        settings: Settings = engine._settings
        settings.enable_glin_profanity = True
        for key in (
            "enable_badwords_py",
            "enable_profanite",
            "enable_glin_profanity",
            "enable_gangajal",
        ):
            if key != "enable_glin_profanity":
                setattr(settings, key, False)
        detector: MultiLanguageDetector = MultiLanguageDetector(settings, None)
        assert detector.detect(text).matched is expected


_GLIN_MASKED_CASES: tuple[tuple[str, str, bool, int], ...] = (
    (
        "en",
        "a f*ck day",
        True,
        755,
    ),
    (
        "zh-CN",
        "a 妈的 day",
        False,
        756,
    ),
    (
        "ja",
        "a くそ day",
        False,
        757,
    ),
    (
        "ko",
        "a 씨발 day",
        False,
        758,
    ),
    (
        "ru",
        "a б*ядь day",
        False,
        759,
    ),
    (
        "es",
        "a j*der day",
        False,
        760,
    ),
    (
        "fr",
        "a m*rde day",
        False,
        761,
    ),
    (
        "de",
        "a s*heiße day",
        False,
        762,
    ),
    (
        "it",
        "a c*zzo day",
        False,
        763,
    ),
    (
        "ar",
        "a س*قا day",
        False,
        764,
    ),
    (
        "hi",
        "a ग*ंड day",
        False,
        765,
    ),
    (
        "tr",
        "a s*ktir day",
        False,
        766,
    ),
    (
        "pt",
        "a c*ralho day",
        False,
        767,
    ),
    (
        "nl",
        "a k*t day",
        False,
        768,
    ),
    (
        "pl",
        "a k*rwa day",
        False,
        769,
    ),
    (
        "uk",
        "a б*яха day",
        False,
        770,
    ),
    (
        "cs",
        "a k*rva day",
        False,
        771,
    ),
    (
        "el",
        "a γ*μώ day",
        False,
        772,
    ),
    (
        "sv",
        "a f*n day",
        False,
        773,
    ),
    (
        "no",
        "a f*en day",
        False,
        774,
    ),
    (
        "da",
        "a f*nd day",
        False,
        775,
    ),
    (
        "fi",
        "a v*ttu day",
        False,
        776,
    ),
    (
        "hu",
        "a b*szd day",
        False,
        777,
    ),
    (
        "ro",
        "a p*la day",
        False,
        778,
    ),
    (
        "bg",
        "a м*йната day",
        False,
        779,
    ),
    (
        "he",
        "a ז*ן day",
        False,
        780,
    ),
    (
        "th",
        "a เ*ี้ย day",
        False,
        781,
    ),
)


class TestGlinMasked(BaseTest):
    """glin-profanity reproduces the golden match flag over en."""

    @pytest.mark.parametrize(
        (
            "language",
            "text",
            "expected",
            "uid",
        ),
        _GLIN_MASKED_CASES,
    )
    def test_glin_masked(
        self, engine: Any, language: str, text: str, expected: bool, uid: int
    ) -> None:
        """glin-profanity reproduces the golden match flag over en."""
        settings: Settings = engine._settings
        settings.enable_glin_profanity = True
        for key in (
            "enable_badwords_py",
            "enable_profanite",
            "enable_glin_profanity",
            "enable_gangajal",
        ):
            if key != "enable_glin_profanity":
                setattr(settings, key, False)
        detector: MultiLanguageDetector = MultiLanguageDetector(settings, None)
        assert detector.detect(text).matched is expected


_GLIN_SPACED_CASES: tuple[tuple[str, str, bool, int], ...] = (
    (
        "en",
        "a f*ck day f*ck",
        True,
        782,
    ),
    (
        "zh-CN",
        "a 妈的 day 妈的",
        False,
        783,
    ),
    (
        "ja",
        "a くそ day くそ",
        False,
        784,
    ),
    (
        "ko",
        "a 씨발 day 씨발",
        False,
        785,
    ),
    (
        "ru",
        "a б*ядь day б*ядь",
        False,
        786,
    ),
    (
        "es",
        "a j*der day j*der",
        False,
        787,
    ),
    (
        "fr",
        "a m*rde day m*rde",
        False,
        788,
    ),
    (
        "de",
        "a s*heiße day s*heiße",
        False,
        789,
    ),
    (
        "it",
        "a c*zzo day c*zzo",
        False,
        790,
    ),
    (
        "ar",
        "a س*قا day س*قا",
        False,
        791,
    ),
    (
        "hi",
        "a ग*ंड day ग*ंड",
        False,
        792,
    ),
    (
        "tr",
        "a s*ktir day s*ktir",
        False,
        793,
    ),
    (
        "pt",
        "a c*ralho day c*ralho",
        False,
        794,
    ),
    (
        "nl",
        "a k*t day k*t",
        False,
        795,
    ),
    (
        "pl",
        "a k*rwa day k*rwa",
        False,
        796,
    ),
    (
        "uk",
        "a б*яха day б*яха",
        False,
        797,
    ),
    (
        "cs",
        "a k*rva day k*rva",
        False,
        798,
    ),
    (
        "el",
        "a γ*μώ day γ*μώ",
        False,
        799,
    ),
    (
        "sv",
        "a f*n day f*n",
        False,
        800,
    ),
)


class TestGlinSpaced(BaseTest):
    """glin-profanity reproduces the golden match flag over en."""

    @pytest.mark.parametrize(
        (
            "language",
            "text",
            "expected",
            "uid",
        ),
        _GLIN_SPACED_CASES,
    )
    def test_glin_spaced(
        self, engine: Any, language: str, text: str, expected: bool, uid: int
    ) -> None:
        """glin-profanity reproduces the golden match flag over en."""
        settings: Settings = engine._settings
        settings.enable_glin_profanity = True
        for key in (
            "enable_badwords_py",
            "enable_profanite",
            "enable_glin_profanity",
            "enable_gangajal",
        ):
            if key != "enable_glin_profanity":
                setattr(settings, key, False)
        detector: MultiLanguageDetector = MultiLanguageDetector(settings, None)
        assert detector.detect(text).matched is expected
