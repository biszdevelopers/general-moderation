"""Phase 2 detector tests (golden master, generated).

Computed from the locked test environment; see tests/tools/phase2_generator.py."""

# ruff: noqa: RUF001  # multilingual fixtures use non-ASCII on purpose
from __future__ import annotations

import pytest

from app.detectors.aho_detector import AhoCorasickDetector
from app.wordbank.manager import WordBankManager
from tests.base_test import BaseTest

_AHO_LANGUAGE_MATRIX_CASES: tuple[tuple[str, str, bool, int], ...] = (
    ('fuck', 'they used fuck in the message', True, 1,),
    ('妈的', 'they used 妈的 in the message', True, 3,),
    ('くそ', 'they used くそ in the message', True, 5,),
    ('씨발', 'they used 씨발 in the message', True, 7,),
    ('блядь', 'they used блядь in the message', True, 9,),
    ('joder', 'they used joder in the message', True, 11,),
    ('merde', 'they used merde in the message', True, 13,),
    ('scheiße', 'they used scheiße in the message', True, 15,),
    ('cazzo', 'they used cazzo in the message', True, 17,),
    ('سحقا', 'they used سحقا in the message', True, 19,),
    ('गांड', 'they used गांड in the message', True, 21,),
    ('siktir', 'they used siktir in the message', True, 23,),
    ('caralho', 'they used caralho in the message', True, 25,),
    ('kut', 'they used kut in the message', True, 27,),
    ('kurwa', 'they used kurwa in the message', True, 29,),
    ('бляха', 'they used бляха in the message', True, 31,),
    ('kurva', 'they used kurva in the message', True, 33,),
    ('γαμώ', 'they used γαμώ in the message', True, 35,),
    ('fan', 'they used fan in the message', True, 37,),
    ('faen', 'they used faen in the message', True, 39,),
    ('fand', 'they used fand in the message', True, 41,),
    ('vittu', 'they used vittu in the message', True, 43,),
    ('baszd', 'they used baszd in the message', True, 45,),
    ('pula', 'they used pula in the message', True, 47,),
    ('майната', 'they used майната in the message', True, 49,),
    ('זין', 'they used זין in the message', True, 51,),
    ('เหี้ย', 'they used เหี้ย in the message', True, 53,),
)

class TestAhoLanguageMatrix(BaseTest):
    """A non-ASCII dictionary word is caught."""

    @pytest.mark.parametrize(('word', 'text', 'expected', 'uid',), _AHO_LANGUAGE_MATRIX_CASES)
    def test_aho_language_matrix(self, word_bank: WordBankManager, word: str, text: str, expected: bool, uid: int) -> None:
        """A non-ASCII dictionary word is caught."""
        word_bank.add_word(word)
        detector: AhoCorasickDetector = AhoCorasickDetector(word_bank)
        assert detector.detect(text).matched is expected


_AHO_LANGUAGE_CLEAN_CASES: tuple[tuple[str, str, bool, int], ...] = (
    ('fuck', 'the weather is pleasant today', False, 2,),
    ('妈的', '今天天气不错', False, 4,),
    ('くそ', '今日は天気が良いです', False, 6,),
    ('씨발', '오늘 날씨가 좋아요', False, 8,),
    ('блядь', 'сегодня хорошая погода', False, 10,),
    ('joder', 'hoy hace buen tiempo', False, 12,),
    ('merde', "il fait beau aujourd'hui", False, 14,),
    ('scheiße', 'das wetter ist schön heute', False, 16,),
    ('cazzo', 'oggi il tempo è bello', False, 18,),
    ('سحقا', 'الطقس جميل اليوم', False, 20,),
    ('गांड', 'आज मौसम अच्छा है', False, 22,),
    ('siktir', 'bugün hava güzel', False, 24,),
    ('caralho', 'o tempo está bom hoje', False, 26,),
    ('kut', 'het weer is mooi vandaag', False, 28,),
    ('kurwa', 'dzisiaj jest ładna pogoda', False, 30,),
    ('бляха', 'сьогодні гарна погода', False, 32,),
    ('kurva', 'dnes je hezké počasí', False, 34,),
    ('γαμώ', 'σήμερα έχει καλό καιρό', False, 36,),
    ('fan', 'vädret är fint idag', False, 38,),
    ('faen', 'været er fint i dag', False, 40,),
    ('fand', 'vejret er dejligt i dag', False, 42,),
    ('vittu', 'tänään on kaunis sää', False, 44,),
    ('baszd', 'ma szép az idő', False, 46,),
    ('pula', 'astăzi este vreme frumoasă', False, 48,),
    ('майната', 'днес е хубаво време', False, 50,),
    ('זין', 'מזג האוויר נחמד היום', False, 52,),
    ('เหี้ย', 'วันนี้อากาศดี', False, 54,),
)

class TestAhoLanguageClean(BaseTest):
    """Clean text over a non-ASCII dictionary word."""

    @pytest.mark.parametrize(('word', 'text', 'expected', 'uid',), _AHO_LANGUAGE_CLEAN_CASES)
    def test_aho_language_clean(self, word_bank: WordBankManager, word: str, text: str, expected: bool, uid: int) -> None:
        """Clean text over a non-ASCII dictionary word."""
        word_bank.add_word(word)
        detector: AhoCorasickDetector = AhoCorasickDetector(word_bank)
        assert detector.detect(text).matched is expected


_AHO_FULLWIDTH_CASES: tuple[tuple[str, str, bool, int], ...] = (
    ('fuck', 'fullwidth ｆｕｃｋ here', True, 55,),
    ('妈的', 'fullwidth 妈的 here', True, 56,),
    ('くそ', 'fullwidth くそ here', True, 57,),
    ('씨발', 'fullwidth 씨발 here', True, 58,),
    ('блядь', 'fullwidth блядь here', True, 59,),
    ('joder', 'fullwidth ｊｏｄｅｒ here', True, 60,),
    ('merde', 'fullwidth ｍｅｒｄｅ here', True, 61,),
    ('scheiße', 'fullwidth ｓｃｈｅｉßｅ here', True, 62,),
    ('cazzo', 'fullwidth ｃａｚｚｏ here', True, 63,),
    ('سحقا', 'fullwidth سحقا here', True, 64,),
    ('गांड', 'fullwidth गांड here', True, 65,),
    ('siktir', 'fullwidth ｓｉｋｔｉｒ here', True, 66,),
    ('caralho', 'fullwidth ｃａｒａｌｈｏ here', True, 67,),
    ('kut', 'fullwidth ｋｕｔ here', True, 68,),
    ('kurwa', 'fullwidth ｋｕｒｗａ here', True, 69,),
    ('бляха', 'fullwidth бляха here', True, 70,),
    ('kurva', 'fullwidth ｋｕｒｖａ here', True, 71,),
    ('γαμώ', 'fullwidth γαμώ here', True, 72,),
    ('fan', 'fullwidth ｆａｎ here', True, 73,),
    ('faen', 'fullwidth ｆａｅｎ here', True, 74,),
    ('fand', 'fullwidth ｆａｎｄ here', True, 75,),
    ('vittu', 'fullwidth ｖｉｔｔｕ here', True, 76,),
    ('baszd', 'fullwidth ｂａｓｚｄ here', True, 77,),
    ('pula', 'fullwidth ｐｕｌａ here', True, 78,),
    ('майната', 'fullwidth майната here', True, 79,),
    ('זין', 'fullwidth זין here', True, 80,),
    ('เหี้ย', 'fullwidth เหี้ย here', True, 81,),
)

class TestAhoFullwidth(BaseTest):
    """NFKC folding catches full-width input."""

    @pytest.mark.parametrize(('word', 'text', 'expected', 'uid',), _AHO_FULLWIDTH_CASES)
    def test_aho_fullwidth(self, word_bank: WordBankManager, word: str, text: str, expected: bool, uid: int) -> None:
        """NFKC folding catches full-width input."""
        word_bank.add_word(word)
        detector: AhoCorasickDetector = AhoCorasickDetector(word_bank)
        assert detector.detect(text).matched is expected


_AHO_SEPARATOR_MATRIX_CASES: tuple[tuple[str, str, bool, int], ...] = (
    ('blocked', 'b l o c k e d', False, 82,),
    ('blocked', 'b*l*o*c*k*e*d', False, 83,),
    ('blocked', 'b.l.o.c.k.e.d', False, 84,),
    ('blocked', 'b_l_o_c_k_e_d', False, 85,),
    ('blocked', 'b-l-o-c-k-e-d', False, 86,),
    ('blocked', 'b+l+o+c+k+e+d', False, 87,),
    ('blocked', 'b~l~o~c~k~e~d', False, 88,),
    ('kill', 'k i l l', False, 89,),
    ('kill', 'k*i*l*l', False, 90,),
    ('kill', 'k.i.l.l', False, 91,),
    ('kill', 'k_i_l_l', False, 92,),
    ('kill', 'k-i-l-l', False, 93,),
    ('kill', 'k+i+l+l', False, 94,),
    ('kill', 'k~i~l~l', False, 95,),
    ('hate', 'h a t e', False, 96,),
    ('hate', 'h*a*t*e', False, 97,),
    ('hate', 'h.a.t.e', False, 98,),
    ('hate', 'h_a_t_e', False, 99,),
    ('hate', 'h-a-t-e', False, 100,),
)

class TestAhoSeparatorMatrix(BaseTest):
    """Symbol-separated tokens never match."""

    @pytest.mark.parametrize(('word', 'text', 'expected', 'uid',), _AHO_SEPARATOR_MATRIX_CASES)
    def test_aho_separator_matrix(self, word_bank: WordBankManager, word: str, text: str, expected: bool, uid: int) -> None:
        """Symbol-separated tokens never match."""
        word_bank.add_word(word)
        detector: AhoCorasickDetector = AhoCorasickDetector(word_bank)
        assert detector.detect(text).matched is expected
