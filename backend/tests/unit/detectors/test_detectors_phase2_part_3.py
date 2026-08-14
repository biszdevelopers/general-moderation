"""Phase 2 detector tests (golden master, generated).

Computed from the locked test environment; see tests/tools/phase2_generator.py."""

# multilingual fixtures use non-ASCII on purpose
from __future__ import annotations

import pytest

from app.detectors.bktree_detector import BkTreeDetector
from app.wordbank.manager import WordBankManager
from tests.base_test import BaseTest

_BK_MUTATION_SWEEP_CASES: tuple[tuple[str, str, int, bool, int], ...] = (
    ('asshole', 'asshole', 1, False, 201,),
    ('asshole', 'assho', 2, True, 202,),
    ('asshole', 'assh', 3, True, 203,),
    ('blocked', 'blocked', 1, False, 204,),
    ('blocked', 'block', 2, True, 205,),
    ('blocked', 'bloc', 3, True, 206,),
    ('kill', 'kill', 1, False, 207,),
    ('kill', 'ki', 2, True, 208,),
    ('kill', 'k', 3, True, 209,),
    ('murder', 'murder', 1, False, 210,),
    ('murder', 'murd', 2, True, 211,),
    ('murder', 'mur', 3, True, 212,),
    ('scam', 'scam', 1, False, 213,),
    ('scam', 'sc', 2, True, 214,),
    ('scam', 's', 3, True, 215,),
    ('poison', 'poison', 1, False, 216,),
    ('poison', 'pois', 2, True, 217,),
    ('poison', 'poi', 3, True, 218,),
    ('knife', 'knife', 1, False, 219,),
    ('knife', 'kni', 2, True, 220,),
    ('knife', 'kn', 3, True, 221,),
    ('terror', 'terror', 1, False, 222,),
    ('terror', 'terr', 2, True, 223,),
    ('terror', 'ter', 3, True, 224,),
    ('weapon', 'weapon', 1, False, 225,),
    ('weapon', 'weap', 2, True, 226,),
    ('weapon', 'wea', 3, True, 227,),
    ('bomb', 'bomb', 1, False, 228,),
    ('bomb', 'bo', 2, True, 229,),
    ('bomb', 'b', 3, True, 230,),
    ('steal', 'steal', 1, False, 231,),
    ('steal', 'ste', 2, True, 232,),
    ('steal', 'st', 3, True, 233,),
    ('threat', 'threat', 1, False, 234,),
    ('threat', 'thre', 2, True, 235,),
    ('threat', 'thr', 3, True, 236,),
    ('fraud', 'fraud', 1, False, 237,),
    ('fraud', 'fra', 2, True, 238,),
    ('fraud', 'fr', 3, True, 239,),
    ('gun', 'gun', 1, False, 240,),
    ('gun', 'g', 2, True, 241,),
    ('gun', 'g', 3, True, 242,),
    ('rape', 'rape', 1, False, 243,),
    ('rape', 'ra', 2, True, 244,),
    ('rape', 'r', 3, True, 245,),
    ('hate', 'hate', 1, False, 246,),
    ('hate', 'ha', 2, True, 247,),
    ('hate', 'h', 3, True, 248,),
    ('idiot', 'idiot', 1, False, 249,),
    ('idiot', 'idi', 2, True, 250,),
    ('idiot', 'id', 3, True, 251,),
    ('liar', 'liar', 1, False, 252,),
    ('liar', 'li', 2, True, 253,),
    ('liar', 'l', 3, True, 254,),
)

class TestBkMutationSweep(BaseTest):
    """Edit-distance mutations are caught."""

    @pytest.mark.parametrize(('word', 'text', 'distance', 'expected', 'uid',), _BK_MUTATION_SWEEP_CASES)
    def test_bk_mutation_sweep(self, word_bank: WordBankManager, word: str, text: str, distance: int, expected: bool, uid: int) -> None:
        """Edit-distance mutations are caught."""
        word_bank.add_word(word)
        detector: BkTreeDetector = BkTreeDetector(word_bank, distance)
        assert detector.detect(text).matched is expected


_BK_CLEAN_NONMATCH_CASES: tuple[tuple[str, str, int, bool, int], ...] = (
    ('asshole', 'completely unrelated vocabulary here', 1, False, 255,),
    ('asshole', 'completely unrelated vocabulary here', 2, False, 256,),
    ('asshole', 'completely unrelated vocabulary here', 3, False, 257,),
    ('blocked', 'completely unrelated vocabulary here', 1, False, 258,),
    ('blocked', 'completely unrelated vocabulary here', 2, False, 259,),
    ('blocked', 'completely unrelated vocabulary here', 3, False, 260,),
    ('kill', 'completely unrelated vocabulary here', 1, False, 261,),
    ('kill', 'completely unrelated vocabulary here', 2, False, 262,),
    ('kill', 'completely unrelated vocabulary here', 3, False, 263,),
    ('murder', 'completely unrelated vocabulary here', 1, False, 264,),
    ('murder', 'completely unrelated vocabulary here', 2, False, 265,),
    ('murder', 'completely unrelated vocabulary here', 3, False, 266,),
    ('scam', 'completely unrelated vocabulary here', 1, False, 267,),
    ('scam', 'completely unrelated vocabulary here', 2, False, 268,),
    ('scam', 'completely unrelated vocabulary here', 3, False, 269,),
    ('poison', 'completely unrelated vocabulary here', 1, False, 270,),
    ('poison', 'completely unrelated vocabulary here', 2, False, 271,),
    ('poison', 'completely unrelated vocabulary here', 3, False, 272,),
    ('knife', 'completely unrelated vocabulary here', 1, False, 273,),
    ('knife', 'completely unrelated vocabulary here', 2, False, 274,),
    ('knife', 'completely unrelated vocabulary here', 3, False, 275,),
    ('terror', 'completely unrelated vocabulary here', 1, False, 276,),
    ('terror', 'completely unrelated vocabulary here', 2, False, 277,),
    ('terror', 'completely unrelated vocabulary here', 3, False, 278,),
    ('weapon', 'completely unrelated vocabulary here', 1, False, 279,),
    ('weapon', 'completely unrelated vocabulary here', 2, False, 280,),
    ('weapon', 'completely unrelated vocabulary here', 3, False, 281,),
    ('bomb', 'completely unrelated vocabulary here', 1, False, 282,),
    ('bomb', 'completely unrelated vocabulary here', 2, False, 283,),
    ('bomb', 'completely unrelated vocabulary here', 3, False, 284,),
    ('steal', 'completely unrelated vocabulary here', 1, False, 285,),
    ('steal', 'completely unrelated vocabulary here', 2, False, 286,),
    ('steal', 'completely unrelated vocabulary here', 3, False, 287,),
    ('threat', 'completely unrelated vocabulary here', 1, False, 288,),
    ('threat', 'completely unrelated vocabulary here', 2, False, 289,),
    ('threat', 'completely unrelated vocabulary here', 3, False, 290,),
    ('fraud', 'completely unrelated vocabulary here', 1, False, 291,),
    ('fraud', 'completely unrelated vocabulary here', 2, False, 292,),
    ('fraud', 'completely unrelated vocabulary here', 3, False, 293,),
    ('gun', 'completely unrelated vocabulary here', 1, False, 294,),
    ('gun', 'completely unrelated vocabulary here', 2, False, 295,),
    ('gun', 'completely unrelated vocabulary here', 3, False, 296,),
    ('rape', 'completely unrelated vocabulary here', 1, False, 297,),
    ('rape', 'completely unrelated vocabulary here', 2, False, 298,),
    ('rape', 'completely unrelated vocabulary here', 3, True, 299,),
    ('hate', 'completely unrelated vocabulary here', 1, False, 300,),
)

class TestBkCleanNonmatch(BaseTest):
    """Unrelated text never fuzz-matches."""

    @pytest.mark.parametrize(('word', 'text', 'distance', 'expected', 'uid',), _BK_CLEAN_NONMATCH_CASES)
    def test_bk_clean_nonmatch(self, word_bank: WordBankManager, word: str, text: str, distance: int, expected: bool, uid: int) -> None:
        """Unrelated text never fuzz-matches."""
        word_bank.add_word(word)
        detector: BkTreeDetector = BkTreeDetector(word_bank, distance)
        assert detector.detect(text).matched is expected
