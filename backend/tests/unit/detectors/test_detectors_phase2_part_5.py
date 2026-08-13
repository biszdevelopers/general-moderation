"""Phase 2 detector tests (golden master, generated).

Computed from the locked test environment; see tests/tools/phase2_generator.py."""

# ruff: noqa: RUF001  # multilingual fixtures use non-ASCII on purpose
from __future__ import annotations

from typing import Any

import pytest

from app.config import Settings
from app.detectors.metaphone_detector import MetaphoneDetector
from app.detectors.multi_language_detector import MultiLanguageDetector
from app.wordbank.manager import WordBankManager
from tests.base_test import BaseTest

_METAPHONE_PAIR_MATRIX_CASES: tuple[tuple[str, str, bool, int], ...] = (
    ('our', 'hour', True, 401,),
    ('ate', 'eight', True, 402,),
    ('eight', 'ate', True, 403,),
    ('weight', 'wait', True, 404,),
    ('wait', 'weight', True, 405,),
    ('plane', 'plain', True, 406,),
    ('plain', 'plane', True, 407,),
    ('brake', 'break', True, 408,),
    ('break', 'brake', True, 409,),
    ('new', 'knew', True, 410,),
    ('knew', 'new', True, 411,),
    ('no', 'know', True, 412,),
    ('know', 'no', True, 413,),
    ('son', 'sun', True, 414,),
    ('sun', 'son', True, 415,),
    ('won', 'one', True, 416,),
    ('one', 'won', True, 417,),
    ('buy', 'by', True, 418,),
    ('by', 'buy', True, 419,),
    ('sigh', 'si', True, 420,),
    ('night', 'nite', True, 421,),
    ('light', 'lite', True, 422,),
    ('fight', 'fite', True, 423,),
    ('might', 'mite', True, 424,),
    ('sight', 'site', True, 425,),
    ('height', 'hite', True, 426,),
    ('weighty', 'watey', True, 427,),
    ('freight', 'frate', True, 428,),
    ('sleigh', 'slay', True, 429,),
    ('neigh', 'nay', True, 430,),
    ('eight', 'ate', True, 431,),
    ('straight', 'strat', True, 432,),
    ('caught', 'cort', True, 433,),
    ('taught', 'tort', True, 434,),
    ('naught', 'nort', True, 435,),
    ('daughter', 'dorter', True, 436,),
    ('laughter', 'lafter', True, 437,),
    ('slaughter', 'slorter', True, 438,),
    ('borough', 'boro', True, 439,),
    ('thorough', 'thuro', True, 440,),
    ('through', 'thru', True, 441,),
    ('though', 'tho', True, 442,),
    ('enough', 'enuf', True, 443,),
    ('rough', 'ruf', True, 444,),
    ('cough', 'cof', True, 445,),
    ('dough', 'doe', True, 446,),
    ('cheque', 'check', True, 447,),
    ('chord', 'cord', True, 448,),
    ('queue', 'cue', True, 449,),
    ('yacht', 'yot', True, 450,),
)

class TestMetaphonePairMatrix(BaseTest):
    """Phonetic pairs reproduce the golden flag."""

    @pytest.mark.parametrize(('word', 'text', 'expected', 'uid',), _METAPHONE_PAIR_MATRIX_CASES)
    def test_metaphone_pair_matrix(self, word_bank: WordBankManager, word: str, text: str, expected: bool, uid: int) -> None:
        """Phonetic pairs reproduce the golden flag."""
        word_bank.add_word(word)
        detector: MetaphoneDetector = MetaphoneDetector(word_bank)
        assert detector.detect(text).matched is expected


_BADWORDS_MATRIX_CASES: tuple[tuple[str, str, bool, int], ...] = (
    ('en', 'this is fuck here', True, 451,),
    ('zh-CN', 'this is 妈的 here', False, 453,),
    ('ja', 'this is くそ here', True, 455,),
    ('ko', 'this is 씨발 here', True, 457,),
    ('ru', 'this is блядь here', True, 459,),
    ('es', 'this is joder here', True, 461,),
    ('fr', 'this is merde here', True, 463,),
    ('de', 'this is scheiße here', False, 465,),
    ('it', 'this is cazzo here', False, 467,),
    ('ar', 'this is سحقا here', False, 469,),
    ('hi', 'this is गांड here', False, 471,),
    ('tr', 'this is siktir here', False, 473,),
    ('pt', 'this is caralho here', False, 475,),
    ('nl', 'this is kut here', True, 477,),
    ('pl', 'this is kurwa here', True, 479,),
    ('uk', 'this is бляха here', False, 481,),
    ('cs', 'this is kurva here', True, 483,),
    ('el', 'this is γαμώ here', True, 485,),
    ('sv', 'this is fan here', False, 487,),
    ('no', 'this is faen here', True, 489,),
    ('da', 'this is fand here', False, 491,),
    ('fi', 'this is vittu here', False, 493,),
    ('hu', 'this is baszd here', False, 495,),
    ('ro', 'this is pula here', True, 497,),
    ('bg', 'this is майната here', False, 499,),
)

class TestBadwordsMatrix(BaseTest):
    """badwords-py reproduces the golden match flag over en."""

    @pytest.mark.parametrize(('language', 'text', 'expected', 'uid',), _BADWORDS_MATRIX_CASES)
    def test_badwords_matrix(self, engine: Any, language: str, text: str, expected: bool, uid: int) -> None:
        """badwords-py reproduces the golden match flag over en."""
        settings: Settings = engine._settings
        settings.enable_badwords_py = True
        for key in ("enable_badwords_py", "enable_profanite", "enable_glin_profanity",
                    "enable_gangajal"):
            if key != "enable_badwords_py":
                setattr(settings, key, False)
        detector: MultiLanguageDetector = MultiLanguageDetector(settings, None)
        assert detector.detect(text).matched is expected


_BADWORDS_CLEAN_CASES: tuple[tuple[str, str, bool, int], ...] = (
    ('en', 'the weather is pleasant today', False, 452,),
    ('zh-CN', '今天天气不错', False, 454,),
    ('ja', '今日は天気が良いです', False, 456,),
    ('ko', '오늘 날씨가 좋아요', False, 458,),
    ('ru', 'сегодня хорошая погода', False, 460,),
    ('es', 'hoy hace buen tiempo', False, 462,),
    ('fr', "il fait beau aujourd'hui", False, 464,),
    ('de', 'das wetter ist schön heute', False, 466,),
    ('it', 'oggi il tempo è bello', False, 468,),
    ('ar', 'الطقس جميل اليوم', False, 470,),
    ('hi', 'आज मौसम अच्छा है', False, 472,),
    ('tr', 'bugün hava güzel', False, 474,),
    ('pt', 'o tempo está bom hoje', False, 476,),
    ('nl', 'het weer is mooi vandaag', False, 478,),
    ('pl', 'dzisiaj jest ładna pogoda', False, 480,),
    ('uk', 'сьогодні гарна погода', False, 482,),
    ('cs', 'dnes je hezké počasí', False, 484,),
    ('el', 'σήμερα έχει καλό καιρό', False, 486,),
    ('sv', 'vädret är fint idag', False, 488,),
    ('no', 'været er fint i dag', False, 490,),
    ('da', 'vejret er dejligt i dag', False, 492,),
    ('fi', 'tänään on kaunis sää', False, 494,),
    ('hu', 'ma szép az idő', False, 496,),
    ('ro', 'astăzi este vreme frumoasă', False, 498,),
    ('bg', 'днес е хубаво време', False, 500,),
)

class TestBadwordsClean(BaseTest):
    """badwords-py reproduces the golden match flag over en."""

    @pytest.mark.parametrize(('language', 'text', 'expected', 'uid',), _BADWORDS_CLEAN_CASES)
    def test_badwords_clean(self, engine: Any, language: str, text: str, expected: bool, uid: int) -> None:
        """badwords-py reproduces the golden match flag over en."""
        settings: Settings = engine._settings
        settings.enable_badwords_py = True
        for key in ("enable_badwords_py", "enable_profanite", "enable_glin_profanity",
                    "enable_gangajal"):
            if key != "enable_badwords_py":
                setattr(settings, key, False)
        detector: MultiLanguageDetector = MultiLanguageDetector(settings, None)
        assert detector.detect(text).matched is expected
