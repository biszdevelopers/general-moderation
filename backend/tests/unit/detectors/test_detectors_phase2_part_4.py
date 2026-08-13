"""Phase 2 detector tests (golden master, generated).

Computed from the locked test environment; see tests/tools/phase2_generator.py."""

# multilingual fixtures use non-ASCII on purpose
from __future__ import annotations

import pytest

from app.detectors.bktree_detector import BkTreeDetector
from app.detectors.metaphone_detector import MetaphoneDetector
from app.wordbank.manager import WordBankManager
from tests.base_test import BaseTest

_BK_CLEAN_NONMATCH_CASES: tuple[tuple[str, str, int, bool, int], ...] = (
    ('hate', 'completely unrelated vocabulary here', 2, True, 301,),
    ('hate', 'completely unrelated vocabulary here', 3, True, 302,),
    ('idiot', 'completely unrelated vocabulary here', 1, False, 303,),
    ('idiot', 'completely unrelated vocabulary here', 2, False, 304,),
    ('idiot', 'completely unrelated vocabulary here', 3, False, 305,),
    ('liar', 'completely unrelated vocabulary here', 1, False, 306,),
    ('liar', 'completely unrelated vocabulary here', 2, False, 307,),
    ('liar', 'completely unrelated vocabulary here', 3, False, 308,),
)

class TestBkCleanNonmatch(BaseTest):
    """Unrelated text never fuzz-matches."""

    @pytest.mark.parametrize(('word', 'text', 'distance', 'expected', 'uid',), _BK_CLEAN_NONMATCH_CASES)
    def test_bk_clean_nonmatch(self, word_bank: WordBankManager, word: str, text: str, distance: int, expected: bool, uid: int) -> None:
        """Unrelated text never fuzz-matches."""
        word_bank.add_word(word)
        detector: BkTreeDetector = BkTreeDetector(word_bank, distance)
        assert detector.detect(text).matched is expected


_BK_UNICODE_SWEEP_CASES: tuple[tuple[str, str, int, bool, int], ...] = (
    ('fuck', 'fuc', 1, True, 309,),
    ('fuck', 'fuc', 2, True, 310,),
    ('fuck', 'fuc', 3, True, 311,),
    ('妈的', '妈', 1, True, 312,),
    ('妈的', '妈', 2, True, 313,),
    ('妈的', '妈', 3, True, 314,),
    ('くそ', 'く', 1, True, 315,),
    ('くそ', 'く', 2, True, 316,),
    ('くそ', 'く', 3, True, 317,),
    ('씨발', '씨', 1, True, 318,),
    ('씨발', '씨', 2, True, 319,),
    ('씨발', '씨', 3, True, 320,),
    ('блядь', 'бляд', 1, True, 321,),
    ('блядь', 'бляд', 2, True, 322,),
    ('блядь', 'бляд', 3, True, 323,),
    ('joder', 'jode', 1, True, 324,),
    ('joder', 'jode', 2, True, 325,),
    ('joder', 'jode', 3, True, 326,),
    ('merde', 'merd', 1, True, 327,),
    ('merde', 'merd', 2, True, 328,),
    ('merde', 'merd', 3, True, 329,),
    ('scheiße', 'scheiß', 1, True, 330,),
    ('scheiße', 'scheiß', 2, True, 331,),
    ('scheiße', 'scheiß', 3, True, 332,),
    ('cazzo', 'cazz', 1, True, 333,),
    ('cazzo', 'cazz', 2, True, 334,),
    ('cazzo', 'cazz', 3, True, 335,),
    ('سحقا', 'سحق', 1, True, 336,),
    ('سحقا', 'سحق', 2, True, 337,),
    ('سحقا', 'سحق', 3, True, 338,),
    ('गांड', 'गां', 1, True, 339,),
    ('गांड', 'गां', 2, True, 340,),
    ('गांड', 'गां', 3, True, 341,),
    ('siktir', 'sikti', 1, True, 342,),
    ('siktir', 'sikti', 2, True, 343,),
    ('siktir', 'sikti', 3, True, 344,),
    ('caralho', 'caralh', 1, True, 345,),
    ('caralho', 'caralh', 2, True, 346,),
    ('caralho', 'caralh', 3, True, 347,),
    ('kut', 'ku', 1, True, 348,),
    ('kut', 'ku', 2, True, 349,),
    ('kut', 'ku', 3, True, 350,),
)

class TestBkUnicodeSweep(BaseTest):
    """Non-ASCII tokens fuzz-match within distance."""

    @pytest.mark.parametrize(('word', 'text', 'distance', 'expected', 'uid',), _BK_UNICODE_SWEEP_CASES)
    def test_bk_unicode_sweep(self, word_bank: WordBankManager, word: str, text: str, distance: int, expected: bool, uid: int) -> None:
        """Non-ASCII tokens fuzz-match within distance."""
        word_bank.add_word(word)
        detector: BkTreeDetector = BkTreeDetector(word_bank, distance)
        assert detector.detect(text).matched is expected


_METAPHONE_PAIR_MATRIX_CASES: tuple[tuple[str, str, bool, int], ...] = (
    ('phone', 'fone', True, 351,),
    ('photo', 'foto', True, 352,),
    ('graph', 'graf', True, 353,),
    ('knight', 'nite', True, 354,),
    ('knife', 'nife', True, 355,),
    ('psych', 'sike', True, 356,),
    ('ghost', 'gost', True, 357,),
    ('write', 'rite', True, 358,),
    ('right', 'rite', True, 359,),
    ('through', 'thru', True, 360,),
    ('tough', 'tuf', True, 361,),
    ('laugh', 'laf', True, 362,),
    ('cough', 'coff', True, 363,),
    ('dough', 'doe', True, 364,),
    ('bough', 'bof', True, 365,),
    ('rough', 'ruf', True, 366,),
    ('sign', 'sine', True, 367,),
    ('align', 'aline', True, 368,),
    ('foreign', 'forin', True, 369,),
    ('reign', 'rain', True, 370,),
    ('feign', 'fain', True, 371,),
    ('design', 'desine', True, 372,),
    ('castle', 'cassle', True, 373,),
    ('listen', 'lissen', True, 374,),
    ('often', 'offen', True, 375,),
    ('soften', 'sofen', True, 376,),
    ('whistle', 'wisel', True, 377,),
    ('answer', 'anser', True, 378,),
    ('sword', 'sord', True, 379,),
    ('two', 'too', True, 380,),
    ('to', 'too', True, 381,),
    ('there', 'their', True, 382,),
    ('their', 'there', True, 383,),
    ('bear', 'bare', True, 384,),
    ('bare', 'bear', True, 385,),
    ('fair', 'fare', True, 386,),
    ('fare', 'fair', True, 387,),
    ('meet', 'meat', True, 388,),
    ('meat', 'meet', True, 389,),
    ('hear', 'here', True, 390,),
    ('here', 'hear', True, 391,),
    ('see', 'sea', True, 392,),
    ('sea', 'see', True, 393,),
    ('weak', 'week', True, 394,),
    ('week', 'weak', True, 395,),
    ('would', 'wood', True, 396,),
    ('wood', 'would', True, 397,),
    ('whole', 'hole', True, 398,),
    ('hole', 'whole', True, 399,),
    ('hour', 'our', True, 400,),
)

class TestMetaphonePairMatrix(BaseTest):
    """Phonetic pairs reproduce the golden flag."""

    @pytest.mark.parametrize(('word', 'text', 'expected', 'uid',), _METAPHONE_PAIR_MATRIX_CASES)
    def test_metaphone_pair_matrix(self, word_bank: WordBankManager, word: str, text: str, expected: bool, uid: int) -> None:
        """Phonetic pairs reproduce the golden flag."""
        word_bank.add_word(word)
        detector: MetaphoneDetector = MetaphoneDetector(word_bank)
        assert detector.detect(text).matched is expected
