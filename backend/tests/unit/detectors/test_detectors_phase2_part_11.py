"""Phase 2 detector tests (golden master, generated).

Computed from the locked test environment; see tests/tools/phase2_generator.py."""

# multilingual fixtures use non-ASCII on purpose
from __future__ import annotations

from typing import Any

import pytest

from app.config import Settings
from app.detectors.multi_language_detector import MultiLanguageDetector
from tests.base_test import BaseTest

_CN_GUARD_CASES: tuple[tuple[str, str, bool, int], ...] = (
    ('zh', '普通消息30', False, 1001,),
    ('zh', '普通消息31', False, 1002,),
    ('zh', '普通消息32', False, 1003,),
    ('zh', '普通消息33', False, 1004,),
    ('zh', '普通消息34', False, 1005,),
    ('zh', '普通消息35', False, 1006,),
    ('zh', '普通消息36', False, 1007,),
    ('zh', '普通消息37', False, 1008,),
    ('zh', '普通消息38', False, 1009,),
    ('zh', '普通消息39', False, 1010,),
    ('zh', '普通消息40', False, 1011,),
    ('zh', '普通消息41', False, 1012,),
    ('zh', '普通消息42', False, 1013,),
    ('zh', '普通消息43', False, 1014,),
    ('zh', '普通消息44', False, 1015,),
    ('zh', '普通消息45', False, 1016,),
    ('zh', '普通消息46', False, 1017,),
    ('zh', '普通消息47', False, 1018,),
    ('zh', '普通消息48', False, 1019,),
    ('zh', '普通消息49', False, 1020,),
    ('zh', '普通消息50', False, 1021,),
    ('zh', '普通消息51', False, 1022,),
    ('zh', '普通消息52', False, 1023,),
    ('zh', '普通消息53', False, 1024,),
    ('zh', '普通消息54', False, 1025,),
    ('zh', '普通消息55', False, 1026,),
    ('zh', '普通消息56', False, 1027,),
    ('zh', '普通消息57', False, 1028,),
    ('zh', '普通消息58', False, 1029,),
    ('zh', '普通消息59', False, 1030,),
    ('zh', '普通消息60', False, 1031,),
    ('zh', '普通消息61', False, 1032,),
    ('zh', '普通消息62', False, 1033,),
    ('zh', '普通消息63', False, 1034,),
    ('zh', '普通消息64', False, 1035,),
    ('zh', '普通消息65', False, 1036,),
    ('zh', '普通消息66', False, 1037,),
    ('zh', '普通消息67', False, 1038,),
    ('zh', '普通消息68', False, 1039,),
    ('zh', '普通消息69', False, 1040,),
    ('zh', '普通消息70', False, 1041,),
    ('zh', '普通消息71', False, 1042,),
    ('zh', '普通消息72', False, 1043,),
    ('zh', '普通消息73', False, 1044,),
    ('zh', '普通消息74', False, 1045,),
    ('zh', '普通消息75', False, 1046,),
    ('zh', '普通消息76', False, 1047,),
    ('zh', '普通消息77', False, 1048,),
    ('zh', '普通消息78', False, 1049,),
    ('zh', '普通消息79', False, 1050,),
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


_PF2_GUARD_CASES: tuple[tuple[str, str, bool, int], ...] = (
    ('en', 'plain english sentence 0', False, 1051,),
    ('en', 'plain english sentence 1', False, 1052,),
    ('en', 'plain english sentence 2', False, 1053,),
    ('en', 'plain english sentence 3', False, 1054,),
    ('en', 'plain english sentence 4', False, 1055,),
    ('en', 'plain english sentence 5', False, 1056,),
    ('en', 'plain english sentence 6', False, 1057,),
    ('en', 'plain english sentence 7', False, 1058,),
    ('en', 'plain english sentence 8', False, 1059,),
    ('en', 'plain english sentence 9', False, 1060,),
    ('en', 'plain english sentence 10', False, 1061,),
    ('en', 'plain english sentence 11', False, 1062,),
    ('en', 'plain english sentence 12', False, 1063,),
    ('en', 'plain english sentence 13', False, 1064,),
    ('en', 'plain english sentence 14', False, 1065,),
    ('en', 'plain english sentence 15', False, 1066,),
    ('en', 'plain english sentence 16', False, 1067,),
    ('en', 'plain english sentence 17', False, 1068,),
    ('en', 'plain english sentence 18', False, 1069,),
    ('en', 'plain english sentence 19', False, 1070,),
    ('en', 'plain english sentence 20', False, 1071,),
    ('en', 'plain english sentence 21', False, 1072,),
    ('en', 'plain english sentence 22', False, 1073,),
    ('en', 'plain english sentence 23', False, 1074,),
    ('en', 'plain english sentence 24', False, 1075,),
    ('en', 'plain english sentence 25', False, 1076,),
    ('en', 'plain english sentence 26', False, 1077,),
    ('en', 'plain english sentence 27', False, 1078,),
    ('en', 'plain english sentence 28', False, 1079,),
    ('en', 'plain english sentence 29', False, 1080,),
    ('en', 'plain english sentence 30', False, 1081,),
    ('en', 'plain english sentence 31', False, 1082,),
    ('en', 'plain english sentence 32', False, 1083,),
    ('en', 'plain english sentence 33', False, 1084,),
    ('en', 'plain english sentence 34', False, 1085,),
    ('en', 'plain english sentence 35', False, 1086,),
    ('en', 'plain english sentence 36', False, 1087,),
    ('en', 'plain english sentence 37', False, 1088,),
    ('en', 'plain english sentence 38', False, 1089,),
    ('en', 'plain english sentence 39', False, 1090,),
    ('en', 'plain english sentence 40', False, 1091,),
    ('en', 'plain english sentence 41', False, 1092,),
    ('en', 'plain english sentence 42', False, 1093,),
    ('en', 'plain english sentence 43', False, 1094,),
    ('en', 'plain english sentence 44', False, 1095,),
    ('en', 'plain english sentence 45', False, 1096,),
    ('en', 'plain english sentence 46', False, 1097,),
    ('en', 'plain english sentence 47', False, 1098,),
    ('en', 'plain english sentence 48', False, 1099,),
    ('en', 'plain english sentence 49', False, 1100,),
)

class TestPf2Guard(BaseTest):
    """The profanity-filter2 guard stays inert when the package is missing."""

    @pytest.mark.parametrize(('language', 'text', 'expected', 'uid',), _PF2_GUARD_CASES)
    def test_pf2_guard(self, engine: Any, language: str, text: str, expected: bool, uid: int) -> None:
        """The profanity-filter2 guard stays inert when the package is missing."""
        settings: Settings = engine._settings
        settings.enable_profanity_filter = True
        for key in ("enable_badwords_py", "enable_profanite", "enable_glin_profanity",
                    "enable_gangajal"):
            setattr(settings, key, False)
        detector: MultiLanguageDetector = MultiLanguageDetector(settings, None)
        assert detector.detect(text).matched is expected
