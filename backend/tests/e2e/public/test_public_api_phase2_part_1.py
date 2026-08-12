"""Phase 2 public moderation API tests (generated).

Language verdict matrices, batch sizes, validation, unicode edges,
profiling flows and response shapes; see tests/tools/phase2_generator.py."""

# multilingual fixtures use non-ASCII on purpose
from __future__ import annotations

from typing import Any

import pytest

from tests.base_test import BaseTest

_MODERATE_LANGUAGE_MATRIX_CASES: tuple[tuple[str, str, int], ...] = (
    (
        "the w",
        "PASS",
        6489,
    ),
    (
        "the weather is pleasant t",
        "PASS",
        6490,
    ),
    (
        "the weather is pleasant todaythe weather is pleasant todaythe weather is pleasant today",
        "PASS",
        6491,
    ),
    (
        "the weather is pleasant todaythe weather is pleasant todaythe weather is pleasant today",
        "PASS",
        6492,
    ),
    (
        "the weather is pleasant todaythe weather is pleasant todaythe weather is pleasant today",
        "PASS",
        6493,
    ),
    (
        "the weather is pleasant todaythe weather is pleasant todaythe weather is pleasant today",
        "PASS",
        6494,
    ),
    (
        "the weather is pleasant todaythe weather is pleasant todaythe weather is pleasant today",
        "PASS",
        6495,
    ),
    (
        "今天天气不",
        "PASS",
        6497,
    ),
    (
        "今天天气不错今天天气不错今天天气不错",
        "PASS",
        6498,
    ),
    (
        "今天天气不错今天天气不错今天天气不错",
        "PASS",
        6499,
    ),
    (
        "今天天气不错今天天气不错今天天气不错",
        "PASS",
        6500,
    ),
    (
        "今天天气不错今天天气不错今天天气不错",
        "PASS",
        6501,
    ),
    (
        "今天天气不错今天天气不错今天天气不错",
        "PASS",
        6502,
    ),
    (
        "今天天气不错今天天气不错今天天气不错",
        "PASS",
        6503,
    ),
    (
        "今日は天気",
        "PASS",
        6505,
    ),
    (
        "今日は天気が良いです今日は天気が良いです今日は天気",
        "PASS",
        6506,
    ),
    (
        "今日は天気が良いです今日は天気が良いです今日は天気が良いです",
        "PASS",
        6507,
    ),
    (
        "今日は天気が良いです今日は天気が良いです今日は天気が良いです",
        "PASS",
        6508,
    ),
    (
        "今日は天気が良いです今日は天気が良いです今日は天気が良いです",
        "PASS",
        6509,
    ),
    (
        "今日は天気が良いです今日は天気が良いです今日は天気が良いです",
        "PASS",
        6510,
    ),
    (
        "今日は天気が良いです今日は天気が良いです今日は天気が良いです",
        "PASS",
        6511,
    ),
    (
        "오늘 날씨",
        "PASS",
        6513,
    ),
    (
        "오늘 날씨가 좋아요오늘 날씨가 좋아요오늘 날씨",
        "PASS",
        6514,
    ),
    (
        "오늘 날씨가 좋아요오늘 날씨가 좋아요오늘 날씨가 좋아요",
        "PASS",
        6515,
    ),
    (
        "오늘 날씨가 좋아요오늘 날씨가 좋아요오늘 날씨가 좋아요",
        "PASS",
        6516,
    ),
    (
        "오늘 날씨가 좋아요오늘 날씨가 좋아요오늘 날씨가 좋아요",
        "PASS",
        6517,
    ),
    (
        "오늘 날씨가 좋아요오늘 날씨가 좋아요오늘 날씨가 좋아요",
        "PASS",
        6518,
    ),
    (
        "오늘 날씨가 좋아요오늘 날씨가 좋아요오늘 날씨가 좋아요",
        "PASS",
        6519,
    ),
    (
        "сегод",
        "PASS",
        6521,
    ),
    (
        "сегодня хорошая погодасег",
        "PASS",
        6522,
    ),
    (
        "сегодня хорошая погодасегодня хорошая погодасегодня хорошая погода",
        "PASS",
        6523,
    ),
    (
        "сегодня хорошая погодасегодня хорошая погодасегодня хорошая погода",
        "PASS",
        6524,
    ),
    (
        "сегодня хорошая погодасегодня хорошая погодасегодня хорошая погода",
        "PASS",
        6525,
    ),
    (
        "сегодня хорошая погодасегодня хорошая погодасегодня хорошая погода",
        "PASS",
        6526,
    ),
    (
        "сегодня хорошая погодасегодня хорошая погодасегодня хорошая погода",
        "PASS",
        6527,
    ),
    (
        "hoy h",
        "PASS",
        6529,
    ),
    (
        "hoy hace buen tiempohoy h",
        "PASS",
        6530,
    ),
    (
        "hoy hace buen tiempohoy hace buen tiempohoy hace buen tiempo",
        "PASS",
        6531,
    ),
    (
        "hoy hace buen tiempohoy hace buen tiempohoy hace buen tiempo",
        "PASS",
        6532,
    ),
    (
        "hoy hace buen tiempohoy hace buen tiempohoy hace buen tiempo",
        "PASS",
        6533,
    ),
    (
        "hoy hace buen tiempohoy hace buen tiempohoy hace buen tiempo",
        "PASS",
        6534,
    ),
    (
        "hoy hace buen tiempohoy hace buen tiempohoy hace buen tiempo",
        "PASS",
        6535,
    ),
    (
        "il fa",
        "PASS",
        6537,
    ),
    (
        "il fait beau aujourd'huii",
        "PASS",
        6538,
    ),
    (
        "il fait beau aujourd'huiil fait beau aujourd'huiil fait beau aujourd'hui",
        "BLOCK",
        6539,
    ),
    (
        "il fait beau aujourd'huiil fait beau aujourd'huiil fait beau aujourd'hui",
        "BLOCK",
        6540,
    ),
    (
        "il fait beau aujourd'huiil fait beau aujourd'huiil fait beau aujourd'hui",
        "BLOCK",
        6541,
    ),
    (
        "il fait beau aujourd'huiil fait beau aujourd'huiil fait beau aujourd'hui",
        "BLOCK",
        6542,
    ),
    (
        "il fait beau aujourd'huiil fait beau aujourd'huiil fait beau aujourd'hui",
        "BLOCK",
        6543,
    ),
    (
        "das w",
        "PASS",
        6545,
    ),
    (
        "das wetter ist schön heut",
        "PASS",
        6546,
    ),
    (
        "das wetter ist schön heutedas wetter ist schön heutedas wetter ist schön heute",
        "PASS",
        6547,
    ),
    (
        "das wetter ist schön heutedas wetter ist schön heutedas wetter ist schön heute",
        "PASS",
        6548,
    ),
    (
        "das wetter ist schön heutedas wetter ist schön heutedas wetter ist schön heute",
        "PASS",
        6549,
    ),
    (
        "das wetter ist schön heutedas wetter ist schön heutedas wetter ist schön heute",
        "PASS",
        6550,
    ),
    (
        "das wetter ist schön heutedas wetter ist schön heutedas wetter ist schön heute",
        "PASS",
        6551,
    ),
    (
        "oggi ",
        "PASS",
        6553,
    ),
    (
        "oggi il tempo è bellooggi",
        "PASS",
        6554,
    ),
    (
        "oggi il tempo è bellooggi il tempo è bellooggi il tempo è bello",
        "PASS",
        6555,
    ),
    (
        "oggi il tempo è bellooggi il tempo è bellooggi il tempo è bello",
        "PASS",
        6556,
    ),
    (
        "oggi il tempo è bellooggi il tempo è bellooggi il tempo è bello",
        "PASS",
        6557,
    ),
    (
        "oggi il tempo è bellooggi il tempo è bellooggi il tempo è bello",
        "PASS",
        6558,
    ),
    (
        "oggi il tempo è bellooggi il tempo è bellooggi il tempo è bello",
        "PASS",
        6559,
    ),
    (
        "الطقس",
        "PASS",
        6561,
    ),
    (
        "الطقس جميل اليومالطقس جمي",
        "PASS",
        6562,
    ),
    (
        "الطقس جميل اليومالطقس جميل اليومالطقس جميل اليوم",
        "PASS",
        6563,
    ),
    (
        "الطقس جميل اليومالطقس جميل اليومالطقس جميل اليوم",
        "PASS",
        6564,
    ),
    (
        "الطقس جميل اليومالطقس جميل اليومالطقس جميل اليوم",
        "PASS",
        6565,
    ),
    (
        "الطقس جميل اليومالطقس جميل اليومالطقس جميل اليوم",
        "PASS",
        6566,
    ),
    (
        "الطقس جميل اليومالطقس جميل اليومالطقس جميل اليوم",
        "PASS",
        6567,
    ),
    (
        "आज मौ",
        "PASS",
        6569,
    ),
    (
        "आज मौसम अच्छा हैआज मौसम अ",
        "PASS",
        6570,
    ),
    (
        "आज मौसम अच्छा हैआज मौसम अच्छा हैआज मौसम अच्छा है",
        "PASS",
        6571,
    ),
    (
        "आज मौसम अच्छा हैआज मौसम अच्छा हैआज मौसम अच्छा है",
        "PASS",
        6572,
    ),
    (
        "आज मौसम अच्छा हैआज मौसम अच्छा हैआज मौसम अच्छा है",
        "PASS",
        6573,
    ),
    (
        "आज मौसम अच्छा हैआज मौसम अच्छा हैआज मौसम अच्छा है",
        "PASS",
        6574,
    ),
    (
        "आज मौसम अच्छा हैआज मौसम अच्छा हैआज मौसम अच्छा है",
        "PASS",
        6575,
    ),
    (
        "bugün",
        "PASS",
        6577,
    ),
    (
        "bugün hava güzelbugün hav",
        "PASS",
        6578,
    ),
    (
        "bugün hava güzelbugün hava güzelbugün hava güzel",
        "PASS",
        6579,
    ),
    (
        "bugün hava güzelbugün hava güzelbugün hava güzel",
        "PASS",
        6580,
    ),
    (
        "bugün hava güzelbugün hava güzelbugün hava güzel",
        "PASS",
        6581,
    ),
    (
        "bugün hava güzelbugün hava güzelbugün hava güzel",
        "PASS",
        6582,
    ),
    (
        "bugün hava güzelbugün hava güzelbugün hava güzel",
        "PASS",
        6583,
    ),
    (
        "o tem",
        "PASS",
        6585,
    ),
    (
        "o tempo está bom hojeo te",
        "PASS",
        6586,
    ),
    (
        "o tempo está bom hojeo tempo está bom hojeo tempo está bom hoje",
        "BLOCK",
        6587,
    ),
    (
        "o tempo está bom hojeo tempo está bom hojeo tempo está bom hoje",
        "BLOCK",
        6588,
    ),
)


class TestModerateLanguageMatrix(BaseTest):
    """Clean text in each language reproduces the golden verdict."""

    @pytest.mark.parametrize(
        (
            "text",
            "expected",
            "uid",
        ),
        _MODERATE_LANGUAGE_MATRIX_CASES,
    )
    def test_moderate_language_matrix(
        self, client: Any, text: str, expected: str, uid: int
    ) -> None:
        """Clean text in each language reproduces the golden verdict."""
        response = client.post("/moderate", json={"text": text, "app_name": "a"})
        assert response.status_code == 200
        assert response.json()["verdict"] == expected


_MODERATE_FLAGGED_LANGUAGE_CASES: tuple[tuple[str, str, int], ...] = (
    (
        "a fuck appears here",
        "BLOCK",
        6496,
    ),
    (
        "a 妈的 appears here",
        "BLOCK",
        6504,
    ),
    (
        "a くそ appears here",
        "BLOCK",
        6512,
    ),
    (
        "a 씨발 appears here",
        "BLOCK",
        6520,
    ),
    (
        "a блядь appears here",
        "BLOCK",
        6528,
    ),
    (
        "a joder appears here",
        "BLOCK",
        6536,
    ),
    (
        "a merde appears here",
        "BLOCK",
        6544,
    ),
    (
        "a scheiße appears here",
        "BLOCK",
        6552,
    ),
    (
        "a cazzo appears here",
        "BLOCK",
        6560,
    ),
    (
        "a سحقا appears here",
        "PASS",
        6568,
    ),
    (
        "a गांड appears here",
        "BLOCK",
        6576,
    ),
    (
        "a siktir appears here",
        "BLOCK",
        6584,
    ),
)


class TestModerateFlaggedLanguage(BaseTest):
    """Profane text in each language resolves to a valid verdict."""

    @pytest.mark.parametrize(
        (
            "text",
            "expected",
            "uid",
        ),
        _MODERATE_FLAGGED_LANGUAGE_CASES,
    )
    def test_moderate_flagged_language(
        self, client: Any, text: str, expected: str, uid: int
    ) -> None:
        """Profane text in each language resolves to a valid verdict."""
        response = client.post("/moderate", json={"text": text, "app_name": "a"})
        assert response.status_code == 200
        assert response.json()["verdict"] == expected
