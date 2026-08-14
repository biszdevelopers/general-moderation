"""Phase 2 detector tests (golden master, generated).

Computed from the locked test environment; see tests/tools/phase2_generator.py."""

# ruff: noqa: RUF001  # multilingual fixtures use non-ASCII on purpose
from __future__ import annotations

from typing import Any

import pytest

from app.config import Settings
from app.detectors.multi_language_detector import MultiLanguageDetector
from tests.base_test import BaseTest

_SAFETEXT_GUARD_CASES: tuple[tuple[str, str, bool, int], ...] = (
    ('en', 'some harmless sentence here 3', False, 901,),
    ('ja', 'これは普通の文章です 3', False, 902,),
    ('ar', 'هذه جملة عادية 3', False, 903,),
    ('ru', 'обычное безобидное предложение 3', False, 904,),
    ('ko', '이건 평범한 문장입니다 3', False, 905,),
    ('de', 'ein völlig harmloser satz 3', False, 906,),
    ('fr', 'une phrase tout à fait banale 3', False, 907,),
    ('it', 'una frase assolutamente innocua 3', False, 908,),
    ('hi', 'यह एक साधारण वाक्य है 3', False, 909,),
    ('tr', 'bu zararsız bir cümle 3', False, 910,),
    ('en', 'some harmless sentence here 4', False, 911,),
    ('ja', 'これは普通の文章です 4', False, 912,),
    ('ar', 'هذه جملة عادية 4', False, 913,),
    ('ru', 'обычное безобидное предложение 4', False, 914,),
    ('ko', '이건 평범한 문장입니다 4', False, 915,),
    ('de', 'ein völlig harmloser satz 4', False, 916,),
    ('fr', 'une phrase tout à fait banale 4', False, 917,),
    ('it', 'una frase assolutamente innocua 4', False, 918,),
    ('hi', 'यह एक साधारण वाक्य है 4', False, 919,),
    ('tr', 'bu zararsız bir cümle 4', False, 920,),
    ('en', 'some harmless sentence here 5', False, 921,),
    ('ja', 'これは普通の文章です 5', False, 922,),
    ('ar', 'هذه جملة عادية 5', False, 923,),
    ('ru', 'обычное безобидное предложение 5', False, 924,),
    ('ko', '이건 평범한 문장입니다 5', False, 925,),
    ('de', 'ein völlig harmloser satz 5', False, 926,),
    ('fr', 'une phrase tout à fait banale 5', False, 927,),
    ('it', 'una frase assolutamente innocua 5', False, 928,),
    ('hi', 'यह एक साधारण वाक्य है 5', False, 929,),
    ('tr', 'bu zararsız bir cümle 5', False, 930,),
    ('en', 'some harmless sentence here 6', False, 931,),
    ('ja', 'これは普通の文章です 6', False, 932,),
    ('ar', 'هذه جملة عادية 6', False, 933,),
    ('ru', 'обычное безобидное предложение 6', False, 934,),
    ('ko', '이건 평범한 문장입니다 6', False, 935,),
    ('de', 'ein völlig harmloser satz 6', False, 936,),
    ('fr', 'une phrase tout à fait banale 6', False, 937,),
    ('it', 'una frase assolutamente innocua 6', False, 938,),
    ('hi', 'यह एक साधारण वाक्य है 6', False, 939,),
    ('tr', 'bu zararsız bir cümle 6', False, 940,),
    ('en', 'some harmless sentence here 7', False, 941,),
    ('ja', 'これは普通の文章です 7', False, 942,),
    ('ar', 'هذه جملة عادية 7', False, 943,),
    ('ru', 'обычное безобидное предложение 7', False, 944,),
    ('ko', '이건 평범한 문장입니다 7', False, 945,),
    ('de', 'ein völlig harmloser satz 7', False, 946,),
    ('fr', 'une phrase tout à fait banale 7', False, 947,),
    ('it', 'una frase assolutamente innocua 7', False, 948,),
    ('hi', 'यह एक साधारण वाक्य है 7', False, 949,),
    ('tr', 'bu zararsız bir cümle 7', False, 950,),
    ('en', 'some harmless sentence here 8', False, 951,),
    ('ja', 'これは普通の文章です 8', False, 952,),
    ('ar', 'هذه جملة عادية 8', False, 953,),
    ('ru', 'обычное безобидное предложение 8', False, 954,),
    ('ko', '이건 평범한 문장입니다 8', False, 955,),
    ('de', 'ein völlig harmloser satz 8', False, 956,),
    ('fr', 'une phrase tout à fait banale 8', False, 957,),
    ('it', 'una frase assolutamente innocua 8', False, 958,),
    ('hi', 'यह एक साधारण वाक्य है 8', False, 959,),
    ('tr', 'bu zararsız bir cümle 8', False, 960,),
    ('en', 'some harmless sentence here 9', False, 961,),
    ('ja', 'これは普通の文章です 9', False, 962,),
    ('ar', 'هذه جملة عادية 9', False, 963,),
    ('ru', 'обычное безобидное предложение 9', False, 964,),
    ('ko', '이건 평범한 문장입니다 9', False, 965,),
    ('de', 'ein völlig harmloser satz 9', False, 966,),
    ('fr', 'une phrase tout à fait banale 9', False, 967,),
    ('it', 'una frase assolutamente innocua 9', False, 968,),
    ('hi', 'यह एक साधारण वाक्य है 9', False, 969,),
    ('tr', 'bu zararsız bir cümle 9', False, 970,),
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


_CN_GUARD_CASES: tuple[tuple[str, str, bool, int], ...] = (
    ('zh', '普通消息0', False, 971,),
    ('zh', '普通消息1', False, 972,),
    ('zh', '普通消息2', False, 973,),
    ('zh', '普通消息3', False, 974,),
    ('zh', '普通消息4', False, 975,),
    ('zh', '普通消息5', False, 976,),
    ('zh', '普通消息6', False, 977,),
    ('zh', '普通消息7', False, 978,),
    ('zh', '普通消息8', False, 979,),
    ('zh', '普通消息9', False, 980,),
    ('zh', '普通消息10', False, 981,),
    ('zh', '普通消息11', False, 982,),
    ('zh', '普通消息12', False, 983,),
    ('zh', '普通消息13', False, 984,),
    ('zh', '普通消息14', False, 985,),
    ('zh', '普通消息15', False, 986,),
    ('zh', '普通消息16', False, 987,),
    ('zh', '普通消息17', False, 988,),
    ('zh', '普通消息18', False, 989,),
    ('zh', '普通消息19', False, 990,),
    ('zh', '普通消息20', False, 991,),
    ('zh', '普通消息21', False, 992,),
    ('zh', '普通消息22', False, 993,),
    ('zh', '普通消息23', False, 994,),
    ('zh', '普通消息24', False, 995,),
    ('zh', '普通消息25', False, 996,),
    ('zh', '普通消息26', False, 997,),
    ('zh', '普通消息27', False, 998,),
    ('zh', '普通消息28', False, 999,),
    ('zh', '普通消息29', False, 1000,),
)

class TestCnGuard(BaseTest):
    """The sensitive-word-filter-cn guard stays inert when the package is missing."""

    @pytest.mark.parametrize(('language', 'text', 'expected', 'uid',), _CN_GUARD_CASES)
    def test_cn_guard(self, engine: Any, language: str, text: str, expected: bool, uid: int) -> None:
        """The sensitive-word-filter-cn guard stays inert when the package is missing."""
        settings: Settings = engine._settings
        settings.enable_sensitive_word_filter_cn = True
        for key in ("enable_badwords_py", "enable_profanite", "enable_glin_profanity",
                    "enable_gangajal"):
            setattr(settings, key, False)
        detector: MultiLanguageDetector = MultiLanguageDetector(settings, None)
        assert detector.detect(text).matched is expected
