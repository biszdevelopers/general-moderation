"""Phase 2 detector tests (golden master, generated).

Computed from the locked test environment; see tests/tools/phase2_generator.py."""

# multilingual fixtures use non-ASCII on purpose
from __future__ import annotations

from typing import Any

import pytest

from app.config import Settings
from app.detectors.multi_language_detector import MultiLanguageDetector
from tests.base_test import BaseTest

_PF2_GUARD_CASES: tuple[tuple[str, str, bool, int], ...] = (
    (
        "en",
        "plain english sentence 50",
        False,
        1101,
    ),
    (
        "en",
        "plain english sentence 51",
        False,
        1102,
    ),
    (
        "en",
        "plain english sentence 52",
        False,
        1103,
    ),
    (
        "en",
        "plain english sentence 53",
        False,
        1104,
    ),
    (
        "en",
        "plain english sentence 54",
        False,
        1105,
    ),
    (
        "en",
        "plain english sentence 55",
        False,
        1106,
    ),
    (
        "en",
        "plain english sentence 56",
        False,
        1107,
    ),
    (
        "en",
        "plain english sentence 57",
        False,
        1108,
    ),
    (
        "en",
        "plain english sentence 58",
        False,
        1109,
    ),
    (
        "en",
        "plain english sentence 59",
        False,
        1110,
    ),
    (
        "en",
        "plain english sentence 60",
        False,
        1111,
    ),
    (
        "en",
        "plain english sentence 61",
        False,
        1112,
    ),
    (
        "en",
        "plain english sentence 62",
        False,
        1113,
    ),
    (
        "en",
        "plain english sentence 63",
        False,
        1114,
    ),
    (
        "en",
        "plain english sentence 64",
        False,
        1115,
    ),
    (
        "en",
        "plain english sentence 65",
        False,
        1116,
    ),
    (
        "en",
        "plain english sentence 66",
        False,
        1117,
    ),
    (
        "en",
        "plain english sentence 67",
        False,
        1118,
    ),
    (
        "en",
        "plain english sentence 68",
        False,
        1119,
    ),
    (
        "en",
        "plain english sentence 69",
        False,
        1120,
    ),
    (
        "en",
        "plain english sentence 70",
        False,
        1121,
    ),
    (
        "en",
        "plain english sentence 71",
        False,
        1122,
    ),
    (
        "en",
        "plain english sentence 72",
        False,
        1123,
    ),
    (
        "en",
        "plain english sentence 73",
        False,
        1124,
    ),
    (
        "en",
        "plain english sentence 74",
        False,
        1125,
    ),
    (
        "en",
        "plain english sentence 75",
        False,
        1126,
    ),
    (
        "en",
        "plain english sentence 76",
        False,
        1127,
    ),
    (
        "en",
        "plain english sentence 77",
        False,
        1128,
    ),
    (
        "en",
        "plain english sentence 78",
        False,
        1129,
    ),
    (
        "en",
        "plain english sentence 79",
        False,
        1130,
    ),
)


class TestPf2Guard(BaseTest):
    """The profanity-filter2 guard stays inert when the package is missing."""

    @pytest.mark.parametrize(
        (
            "language",
            "text",
            "expected",
            "uid",
        ),
        _PF2_GUARD_CASES,
    )
    def test_pf2_guard(
        self, engine: Any, language: str, text: str, expected: bool, uid: int
    ) -> None:
        """The profanity-filter2 guard stays inert when the package is missing."""
        settings: Settings = engine._settings
        settings.enable_profanity_filter = True
        for key in (
            "enable_badwords_py",
            "enable_profanite",
            "enable_glin_profanity",
            "enable_gangajal",
        ):
            setattr(settings, key, False)
        detector: MultiLanguageDetector = MultiLanguageDetector(settings, None)
        assert detector.detect(text).matched is expected


_PYPROFANE_GUARD_CASES: tuple[tuple[str, str, bool, int], ...] = (
    (
        "en",
        "soundex prose here 0",
        False,
        1131,
    ),
    (
        "en",
        "soundex prose here 1",
        False,
        1132,
    ),
    (
        "en",
        "soundex prose here 2",
        False,
        1133,
    ),
    (
        "en",
        "soundex prose here 3",
        False,
        1134,
    ),
    (
        "en",
        "soundex prose here 4",
        False,
        1135,
    ),
    (
        "en",
        "soundex prose here 5",
        False,
        1136,
    ),
    (
        "en",
        "soundex prose here 6",
        False,
        1137,
    ),
    (
        "en",
        "soundex prose here 7",
        False,
        1138,
    ),
    (
        "en",
        "soundex prose here 8",
        False,
        1139,
    ),
    (
        "en",
        "soundex prose here 9",
        False,
        1140,
    ),
    (
        "en",
        "soundex prose here 10",
        False,
        1141,
    ),
    (
        "en",
        "soundex prose here 11",
        False,
        1142,
    ),
    (
        "en",
        "soundex prose here 12",
        False,
        1143,
    ),
    (
        "en",
        "soundex prose here 13",
        False,
        1144,
    ),
    (
        "en",
        "soundex prose here 14",
        False,
        1145,
    ),
    (
        "en",
        "soundex prose here 15",
        False,
        1146,
    ),
    (
        "en",
        "soundex prose here 16",
        False,
        1147,
    ),
    (
        "en",
        "soundex prose here 17",
        False,
        1148,
    ),
    (
        "en",
        "soundex prose here 18",
        False,
        1149,
    ),
    (
        "en",
        "soundex prose here 19",
        False,
        1150,
    ),
    (
        "en",
        "soundex prose here 20",
        False,
        1151,
    ),
    (
        "en",
        "soundex prose here 21",
        False,
        1152,
    ),
    (
        "en",
        "soundex prose here 22",
        False,
        1153,
    ),
    (
        "en",
        "soundex prose here 23",
        False,
        1154,
    ),
    (
        "en",
        "soundex prose here 24",
        False,
        1155,
    ),
    (
        "en",
        "soundex prose here 25",
        False,
        1156,
    ),
    (
        "en",
        "soundex prose here 26",
        False,
        1157,
    ),
    (
        "en",
        "soundex prose here 27",
        False,
        1158,
    ),
    (
        "en",
        "soundex prose here 28",
        False,
        1159,
    ),
    (
        "en",
        "soundex prose here 29",
        False,
        1160,
    ),
    (
        "en",
        "soundex prose here 30",
        False,
        1161,
    ),
    (
        "en",
        "soundex prose here 31",
        False,
        1162,
    ),
    (
        "en",
        "soundex prose here 32",
        False,
        1163,
    ),
    (
        "en",
        "soundex prose here 33",
        False,
        1164,
    ),
    (
        "en",
        "soundex prose here 34",
        False,
        1165,
    ),
    (
        "en",
        "soundex prose here 35",
        False,
        1166,
    ),
    (
        "en",
        "soundex prose here 36",
        False,
        1167,
    ),
    (
        "en",
        "soundex prose here 37",
        False,
        1168,
    ),
    (
        "en",
        "soundex prose here 38",
        False,
        1169,
    ),
    (
        "en",
        "soundex prose here 39",
        False,
        1170,
    ),
    (
        "en",
        "soundex prose here 40",
        False,
        1171,
    ),
    (
        "en",
        "soundex prose here 41",
        False,
        1172,
    ),
    (
        "en",
        "soundex prose here 42",
        False,
        1173,
    ),
    (
        "en",
        "soundex prose here 43",
        False,
        1174,
    ),
    (
        "en",
        "soundex prose here 44",
        False,
        1175,
    ),
    (
        "en",
        "soundex prose here 45",
        False,
        1176,
    ),
    (
        "en",
        "soundex prose here 46",
        False,
        1177,
    ),
    (
        "en",
        "soundex prose here 47",
        False,
        1178,
    ),
    (
        "en",
        "soundex prose here 48",
        False,
        1179,
    ),
    (
        "en",
        "soundex prose here 49",
        False,
        1180,
    ),
    (
        "en",
        "soundex prose here 50",
        False,
        1181,
    ),
    (
        "en",
        "soundex prose here 51",
        False,
        1182,
    ),
    (
        "en",
        "soundex prose here 52",
        False,
        1183,
    ),
    (
        "en",
        "soundex prose here 53",
        False,
        1184,
    ),
    (
        "en",
        "soundex prose here 54",
        False,
        1185,
    ),
    (
        "en",
        "soundex prose here 55",
        False,
        1186,
    ),
    (
        "en",
        "soundex prose here 56",
        False,
        1187,
    ),
    (
        "en",
        "soundex prose here 57",
        False,
        1188,
    ),
    (
        "en",
        "soundex prose here 58",
        False,
        1189,
    ),
    (
        "en",
        "soundex prose here 59",
        False,
        1190,
    ),
    (
        "en",
        "soundex prose here 60",
        False,
        1191,
    ),
    (
        "en",
        "soundex prose here 61",
        False,
        1192,
    ),
    (
        "en",
        "soundex prose here 62",
        False,
        1193,
    ),
    (
        "en",
        "soundex prose here 63",
        False,
        1194,
    ),
    (
        "en",
        "soundex prose here 64",
        False,
        1195,
    ),
    (
        "en",
        "soundex prose here 65",
        False,
        1196,
    ),
    (
        "en",
        "soundex prose here 66",
        False,
        1197,
    ),
    (
        "en",
        "soundex prose here 67",
        False,
        1198,
    ),
    (
        "en",
        "soundex prose here 68",
        False,
        1199,
    ),
    (
        "en",
        "soundex prose here 69",
        False,
        1200,
    ),
)


class TestPyprofaneGuard(BaseTest):
    """The pyprofane guard stays inert when the package is missing."""

    @pytest.mark.parametrize(
        (
            "language",
            "text",
            "expected",
            "uid",
        ),
        _PYPROFANE_GUARD_CASES,
    )
    def test_pyprofane_guard(
        self, engine: Any, language: str, text: str, expected: bool, uid: int
    ) -> None:
        """The pyprofane guard stays inert when the package is missing."""
        settings: Settings = engine._settings
        settings.enable_pyprofane = True
        for key in (
            "enable_badwords_py",
            "enable_profanite",
            "enable_glin_profanity",
            "enable_gangajal",
        ):
            setattr(settings, key, False)
        detector: MultiLanguageDetector = MultiLanguageDetector(settings, None)
        assert detector.detect(text).matched is expected
