"""Phase 2 detector tests (golden master, generated).

Computed from the locked test environment; see tests/tools/phase2_generator.py."""

# ruff: noqa: RUF001  # multilingual fixtures use non-ASCII on purpose
from __future__ import annotations

from typing import Any

import pytest

from app.config import Settings
from app.detectors.multi_language_detector import MultiLanguageDetector
from tests.base_test import BaseTest

_GANGAJAL_MATRIX_CASES: tuple[tuple[str, str, bool, int], ...] = (
    ('en', 'the word fuck appears', True, 801,),
    ('zh-CN', 'the word 妈的 appears', True, 803,),
    ('ja', 'the word くそ appears', False, 805,),
    ('ko', 'the word 씨발 appears', True, 807,),
    ('ru', 'the word блядь appears', True, 809,),
    ('es', 'the word joder appears', True, 811,),
    ('fr', 'the word merde appears', True, 813,),
    ('de', 'the word scheiße appears', True, 815,),
    ('it', 'the word cazzo appears', True, 817,),
    ('ar', 'the word سحقا appears', False, 819,),
    ('hi', 'the word गांड appears', True, 821,),
    ('tr', 'the word siktir appears', True, 823,),
    ('pt', 'the word caralho appears', True, 825,),
    ('nl', 'the word kut appears', True, 827,),
    ('pl', 'the word kurwa appears', True, 829,),
    ('uk', 'the word бляха appears', False, 831,),
    ('cs', 'the word kurva appears', True, 833,),
    ('el', 'the word γαμώ appears', True, 835,),
    ('sv', 'the word fan appears', True, 837,),
    ('no', 'the word faen appears', True, 839,),
    ('da', 'the word fand appears', False, 841,),
    ('fi', 'the word vittu appears', True, 843,),
    ('hu', 'the word baszd appears', False, 845,),
    ('ro', 'the word pula appears', True, 847,),
    ('bg', 'the word майната appears', False, 849,),
    ('he', 'the word זין appears', True, 851,),
    ('th', 'the word เหี้ย appears', True, 853,),
)

class TestGangajalMatrix(BaseTest):
    """gangajal reproduces the golden match flag over en."""

    @pytest.mark.parametrize(('language', 'text', 'expected', 'uid',), _GANGAJAL_MATRIX_CASES)
    def test_gangajal_matrix(self, engine: Any, language: str, text: str, expected: bool, uid: int) -> None:
        """gangajal reproduces the golden match flag over en."""
        settings: Settings = engine._settings
        settings.enable_gangajal = True
        for key in ("enable_badwords_py", "enable_profanite", "enable_glin_profanity",
                    "enable_gangajal"):
            if key != "enable_gangajal":
                setattr(settings, key, False)
        detector: MultiLanguageDetector = MultiLanguageDetector(settings, None)
        assert detector.detect(text).matched is expected


_GANGAJAL_CLEAN_CASES: tuple[tuple[str, str, bool, int], ...] = (
    ('en', 'the weather is pleasant today', False, 802,),
    ('zh-CN', '今天天气不错', False, 804,),
    ('ja', '今日は天気が良いです', False, 806,),
    ('ko', '오늘 날씨가 좋아요', False, 808,),
    ('ru', 'сегодня хорошая погода', False, 810,),
    ('es', 'hoy hace buen tiempo', False, 812,),
    ('fr', "il fait beau aujourd'hui", True, 814,),
    ('de', 'das wetter ist schön heute', False, 816,),
    ('it', 'oggi il tempo è bello', False, 818,),
    ('ar', 'الطقس جميل اليوم', False, 820,),
    ('hi', 'आज मौसम अच्छा है', False, 822,),
    ('tr', 'bugün hava güzel', False, 824,),
    ('pt', 'o tempo está bom hoje', False, 826,),
    ('nl', 'het weer is mooi vandaag', False, 828,),
    ('pl', 'dzisiaj jest ładna pogoda', False, 830,),
    ('uk', 'сьогодні гарна погода', False, 832,),
    ('cs', 'dnes je hezké počasí', False, 834,),
    ('el', 'σήμερα έχει καλό καιρό', False, 836,),
    ('sv', 'vädret är fint idag', False, 838,),
    ('no', 'været er fint i dag', False, 840,),
    ('da', 'vejret er dejligt i dag', False, 842,),
    ('fi', 'tänään on kaunis sää', False, 844,),
    ('hu', 'ma szép az idő', False, 846,),
    ('ro', 'astăzi este vreme frumoasă', False, 848,),
    ('bg', 'днес е хубаво време', False, 850,),
    ('he', 'מזג האוויר נחמד היום', False, 852,),
    ('th', 'วันนี้อากาศดี', False, 854,),
)

class TestGangajalClean(BaseTest):
    """gangajal reproduces the golden match flag over en."""

    @pytest.mark.parametrize(('language', 'text', 'expected', 'uid',), _GANGAJAL_CLEAN_CASES)
    def test_gangajal_clean(self, engine: Any, language: str, text: str, expected: bool, uid: int) -> None:
        """gangajal reproduces the golden match flag over en."""
        settings: Settings = engine._settings
        settings.enable_gangajal = True
        for key in ("enable_badwords_py", "enable_profanite", "enable_glin_profanity",
                    "enable_gangajal"):
            if key != "enable_gangajal":
                setattr(settings, key, False)
        detector: MultiLanguageDetector = MultiLanguageDetector(settings, None)
        assert detector.detect(text).matched is expected


_GANGAJAL_OBFUSCATED_CASES: tuple[tuple[str, str, bool, int], ...] = (
    ('en', 'encoded ｆｕｃｋ', True, 855,),
    ('zh-CN', 'encoded 妈的', True, 856,),
    ('ja', 'encoded くそ', False, 857,),
    ('ko', 'encoded 씨발', True, 858,),
    ('ru', 'encoded блядь', True, 859,),
    ('es', 'encoded ｊｏｄｅｒ', True, 860,),
    ('fr', 'encoded ｍｅｒｄｅ', True, 861,),
    ('de', 'encoded ｓｃｈｅｉßｅ', True, 862,),
    ('it', 'encoded ｃａｚｚｏ', True, 863,),
    ('ar', 'encoded سحقا', False, 864,),
    ('hi', 'encoded गांड', True, 865,),
    ('tr', 'encoded ｓｉｋｔｉｒ', True, 866,),
    ('pt', 'encoded ｃａｒａｌｈｏ', True, 867,),
    ('nl', 'encoded ｋｕｔ', True, 868,),
    ('pl', 'encoded ｋｕｒｗａ', True, 869,),
    ('uk', 'encoded бляха', False, 870,),
)

class TestGangajalObfuscated(BaseTest):
    """gangajal reproduces the golden match flag over en."""

    @pytest.mark.parametrize(('language', 'text', 'expected', 'uid',), _GANGAJAL_OBFUSCATED_CASES)
    def test_gangajal_obfuscated(self, engine: Any, language: str, text: str, expected: bool, uid: int) -> None:
        """gangajal reproduces the golden match flag over en."""
        settings: Settings = engine._settings
        settings.enable_gangajal = True
        for key in ("enable_badwords_py", "enable_profanite", "enable_glin_profanity",
                    "enable_gangajal"):
            if key != "enable_gangajal":
                setattr(settings, key, False)
        detector: MultiLanguageDetector = MultiLanguageDetector(settings, None)
        assert detector.detect(text).matched is expected


_SAFETEXT_GUARD_CASES: tuple[tuple[str, str, bool, int], ...] = (
    ('en', 'some harmless sentence here 0', False, 871,),
    ('ja', 'これは普通の文章です 0', False, 872,),
    ('ar', 'هذه جملة عادية 0', False, 873,),
    ('ru', 'обычное безобидное предложение 0', False, 874,),
    ('ko', '이건 평범한 문장입니다 0', False, 875,),
    ('de', 'ein völlig harmloser satz 0', False, 876,),
    ('fr', 'une phrase tout à fait banale 0', False, 877,),
    ('it', 'una frase assolutamente innocua 0', False, 878,),
    ('hi', 'यह एक साधारण वाक्य है 0', False, 879,),
    ('tr', 'bu zararsız bir cümle 0', False, 880,),
    ('en', 'some harmless sentence here 1', False, 881,),
    ('ja', 'これは普通の文章です 1', False, 882,),
    ('ar', 'هذه جملة عادية 1', False, 883,),
    ('ru', 'обычное безобидное предложение 1', False, 884,),
    ('ko', '이건 평범한 문장입니다 1', False, 885,),
    ('de', 'ein völlig harmloser satz 1', False, 886,),
    ('fr', 'une phrase tout à fait banale 1', False, 887,),
    ('it', 'una frase assolutamente innocua 1', False, 888,),
    ('hi', 'यह एक साधारण वाक्य है 1', False, 889,),
    ('tr', 'bu zararsız bir cümle 1', False, 890,),
    ('en', 'some harmless sentence here 2', False, 891,),
    ('ja', 'これは普通の文章です 2', False, 892,),
    ('ar', 'هذه جملة عادية 2', False, 893,),
    ('ru', 'обычное безобидное предложение 2', False, 894,),
    ('ko', '이건 평범한 문장입니다 2', False, 895,),
    ('de', 'ein völlig harmloser satz 2', False, 896,),
    ('fr', 'une phrase tout à fait banale 2', False, 897,),
    ('it', 'una frase assolutamente innocua 2', False, 898,),
    ('hi', 'यह एक साधारण वाक्य है 2', False, 899,),
    ('tr', 'bu zararsız bir cümle 2', False, 900,),
)

class TestSafetextGuard(BaseTest):
    """The safetext guard stays inert when the package is missing."""

    @pytest.mark.parametrize(('language', 'text', 'expected', 'uid',), _SAFETEXT_GUARD_CASES)
    def test_safetext_guard(self, engine: Any, language: str, text: str, expected: bool, uid: int) -> None:
        """The safetext guard stays inert when the package is missing."""
        settings: Settings = engine._settings
        settings.enable_safetext = True
        for key in ("enable_badwords_py", "enable_profanite", "enable_glin_profanity",
                    "enable_gangajal"):
            setattr(settings, key, False)
        detector: MultiLanguageDetector = MultiLanguageDetector(settings, None)
        assert detector.detect(text).matched is expected
