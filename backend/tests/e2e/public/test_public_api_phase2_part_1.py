"""Phase 2 public moderation API tests (generated).

Language verdict matrices, batch sizes, validation, unicode edges,
profiling flows and response shapes; see tests/tools/phase2_generator.py."""

# multilingual fixtures use non-ASCII on purpose
from __future__ import annotations

from typing import Any

import pytest

from tests.base_test import BaseTest

_MODERATE_LANGUAGE_MATRIX_CASES: tuple[tuple[str, str, int], ...] = (
    ('the w', 'PASS', 6648,),
    ('the weather is pleasant t', 'PASS', 6649,),
    ('the weather is pleasant todaythe weather is pleasant todaythe weather is pleasant today', 'PASS', 6650,),
    ('the weather is pleasant todaythe weather is pleasant todaythe weather is pleasant today', 'PASS', 6651,),
    ('the weather is pleasant todaythe weather is pleasant todaythe weather is pleasant today', 'PASS', 6652,),
    ('the weather is pleasant todaythe weather is pleasant todaythe weather is pleasant today', 'PASS', 6653,),
    ('the weather is pleasant todaythe weather is pleasant todaythe weather is pleasant today', 'PASS', 6654,),
    ('今天天气不', 'PASS', 6656,),
    ('今天天气不错今天天气不错今天天气不错', 'PASS', 6657,),
    ('今天天气不错今天天气不错今天天气不错', 'PASS', 6658,),
    ('今天天气不错今天天气不错今天天气不错', 'PASS', 6659,),
    ('今天天气不错今天天气不错今天天气不错', 'PASS', 6660,),
    ('今天天气不错今天天气不错今天天气不错', 'PASS', 6661,),
    ('今天天气不错今天天气不错今天天气不错', 'PASS', 6662,),
    ('今日は天気', 'PASS', 6664,),
    ('今日は天気が良いです今日は天気が良いです今日は天気', 'PASS', 6665,),
    ('今日は天気が良いです今日は天気が良いです今日は天気が良いです', 'PASS', 6666,),
    ('今日は天気が良いです今日は天気が良いです今日は天気が良いです', 'PASS', 6667,),
    ('今日は天気が良いです今日は天気が良いです今日は天気が良いです', 'PASS', 6668,),
    ('今日は天気が良いです今日は天気が良いです今日は天気が良いです', 'PASS', 6669,),
    ('今日は天気が良いです今日は天気が良いです今日は天気が良いです', 'PASS', 6670,),
    ('오늘 날씨', 'PASS', 6672,),
    ('오늘 날씨가 좋아요오늘 날씨가 좋아요오늘 날씨', 'PASS', 6673,),
    ('오늘 날씨가 좋아요오늘 날씨가 좋아요오늘 날씨가 좋아요', 'PASS', 6674,),
    ('오늘 날씨가 좋아요오늘 날씨가 좋아요오늘 날씨가 좋아요', 'PASS', 6675,),
    ('오늘 날씨가 좋아요오늘 날씨가 좋아요오늘 날씨가 좋아요', 'PASS', 6676,),
    ('오늘 날씨가 좋아요오늘 날씨가 좋아요오늘 날씨가 좋아요', 'PASS', 6677,),
    ('오늘 날씨가 좋아요오늘 날씨가 좋아요오늘 날씨가 좋아요', 'PASS', 6678,),
    ('сегод', 'PASS', 6680,),
    ('сегодня хорошая погодасег', 'PASS', 6681,),
    ('сегодня хорошая погодасегодня хорошая погодасегодня хорошая погода', 'PASS', 6682,),
    ('сегодня хорошая погодасегодня хорошая погодасегодня хорошая погода', 'PASS', 6683,),
    ('сегодня хорошая погодасегодня хорошая погодасегодня хорошая погода', 'PASS', 6684,),
    ('сегодня хорошая погодасегодня хорошая погодасегодня хорошая погода', 'PASS', 6685,),
    ('сегодня хорошая погодасегодня хорошая погодасегодня хорошая погода', 'PASS', 6686,),
    ('hoy h', 'PASS', 6688,),
    ('hoy hace buen tiempohoy h', 'PASS', 6689,),
    ('hoy hace buen tiempohoy hace buen tiempohoy hace buen tiempo', 'PASS', 6690,),
    ('hoy hace buen tiempohoy hace buen tiempohoy hace buen tiempo', 'PASS', 6691,),
    ('hoy hace buen tiempohoy hace buen tiempohoy hace buen tiempo', 'PASS', 6692,),
    ('hoy hace buen tiempohoy hace buen tiempohoy hace buen tiempo', 'PASS', 6693,),
    ('hoy hace buen tiempohoy hace buen tiempohoy hace buen tiempo', 'PASS', 6694,),
    ('il fa', 'PASS', 6696,),
    ("il fait beau aujourd'huii", 'PASS', 6697,),
    ("il fait beau aujourd'huiil fait beau aujourd'huiil fait beau aujourd'hui", 'BLOCK', 6698,),
    ("il fait beau aujourd'huiil fait beau aujourd'huiil fait beau aujourd'hui", 'BLOCK', 6699,),
    ("il fait beau aujourd'huiil fait beau aujourd'huiil fait beau aujourd'hui", 'BLOCK', 6700,),
    ("il fait beau aujourd'huiil fait beau aujourd'huiil fait beau aujourd'hui", 'BLOCK', 6701,),
    ("il fait beau aujourd'huiil fait beau aujourd'huiil fait beau aujourd'hui", 'BLOCK', 6702,),
    ('das w', 'PASS', 6704,),
    ('das wetter ist schön heut', 'PASS', 6705,),
    ('das wetter ist schön heutedas wetter ist schön heutedas wetter ist schön heute', 'PASS', 6706,),
    ('das wetter ist schön heutedas wetter ist schön heutedas wetter ist schön heute', 'PASS', 6707,),
    ('das wetter ist schön heutedas wetter ist schön heutedas wetter ist schön heute', 'PASS', 6708,),
    ('das wetter ist schön heutedas wetter ist schön heutedas wetter ist schön heute', 'PASS', 6709,),
    ('das wetter ist schön heutedas wetter ist schön heutedas wetter ist schön heute', 'PASS', 6710,),
    ('oggi ', 'PASS', 6712,),
    ('oggi il tempo è bellooggi', 'PASS', 6713,),
    ('oggi il tempo è bellooggi il tempo è bellooggi il tempo è bello', 'PASS', 6714,),
    ('oggi il tempo è bellooggi il tempo è bellooggi il tempo è bello', 'PASS', 6715,),
    ('oggi il tempo è bellooggi il tempo è bellooggi il tempo è bello', 'PASS', 6716,),
    ('oggi il tempo è bellooggi il tempo è bellooggi il tempo è bello', 'PASS', 6717,),
    ('oggi il tempo è bellooggi il tempo è bellooggi il tempo è bello', 'PASS', 6718,),
    ('الطقس', 'PASS', 6720,),
    ('الطقس جميل اليومالطقس جمي', 'PASS', 6721,),
    ('الطقس جميل اليومالطقس جميل اليومالطقس جميل اليوم', 'PASS', 6722,),
    ('الطقس جميل اليومالطقس جميل اليومالطقس جميل اليوم', 'PASS', 6723,),
    ('الطقس جميل اليومالطقس جميل اليومالطقس جميل اليوم', 'PASS', 6724,),
    ('الطقس جميل اليومالطقس جميل اليومالطقس جميل اليوم', 'PASS', 6725,),
    ('الطقس جميل اليومالطقس جميل اليومالطقس جميل اليوم', 'PASS', 6726,),
    ('आज मौ', 'PASS', 6728,),
    ('आज मौसम अच्छा हैआज मौसम अ', 'PASS', 6729,),
    ('आज मौसम अच्छा हैआज मौसम अच्छा हैआज मौसम अच्छा है', 'PASS', 6730,),
    ('आज मौसम अच्छा हैआज मौसम अच्छा हैआज मौसम अच्छा है', 'PASS', 6731,),
    ('आज मौसम अच्छा हैआज मौसम अच्छा हैआज मौसम अच्छा है', 'PASS', 6732,),
    ('आज मौसम अच्छा हैआज मौसम अच्छा हैआज मौसम अच्छा है', 'PASS', 6733,),
    ('आज मौसम अच्छा हैआज मौसम अच्छा हैआज मौसम अच्छा है', 'PASS', 6734,),
    ('bugün', 'PASS', 6736,),
    ('bugün hava güzelbugün hav', 'PASS', 6737,),
    ('bugün hava güzelbugün hava güzelbugün hava güzel', 'PASS', 6738,),
    ('bugün hava güzelbugün hava güzelbugün hava güzel', 'PASS', 6739,),
    ('bugün hava güzelbugün hava güzelbugün hava güzel', 'PASS', 6740,),
    ('bugün hava güzelbugün hava güzelbugün hava güzel', 'PASS', 6741,),
    ('bugün hava güzelbugün hava güzelbugün hava güzel', 'PASS', 6742,),
    ('o tem', 'PASS', 6744,),
    ('o tempo está bom hojeo te', 'PASS', 6745,),
    ('o tempo está bom hojeo tempo está bom hojeo tempo está bom hoje', 'PASS', 6746,),
    ('o tempo está bom hojeo tempo está bom hojeo tempo está bom hoje', 'PASS', 6747,),
)

class TestModerateLanguageMatrix(BaseTest):
    """Clean text in each language reproduces the golden verdict."""

    @pytest.mark.parametrize(('text', 'expected', 'uid',), _MODERATE_LANGUAGE_MATRIX_CASES)
    def test_moderate_language_matrix(self, client: Any, text: str, expected: str, uid: int) -> None:
        """Clean text in each language reproduces the golden verdict."""
        response = client.post('/moderate', json={'text': text, 'app_name': 'a'})
        assert response.status_code == 200
        assert response.json()['verdict'] == expected


_MODERATE_FLAGGED_LANGUAGE_CASES: tuple[tuple[str, str, int], ...] = (
    ('a fuck appears here', 'BLOCK', 6655,),
    ('a 妈的 appears here', 'BLOCK', 6663,),
    ('a くそ appears here', 'BLOCK', 6671,),
    ('a 씨발 appears here', 'BLOCK', 6679,),
    ('a блядь appears here', 'BLOCK', 6687,),
    ('a joder appears here', 'BLOCK', 6695,),
    ('a merde appears here', 'BLOCK', 6703,),
    ('a scheiße appears here', 'BLOCK', 6711,),
    ('a cazzo appears here', 'BLOCK', 6719,),
    ('a سحقا appears here', 'PASS', 6727,),
    ('a गांड appears here', 'BLOCK', 6735,),
    ('a siktir appears here', 'BLOCK', 6743,),
)

class TestModerateFlaggedLanguage(BaseTest):
    """Profane text in each language resolves to a valid verdict."""

    @pytest.mark.parametrize(('text', 'expected', 'uid',), _MODERATE_FLAGGED_LANGUAGE_CASES)
    def test_moderate_flagged_language(self, client: Any, text: str, expected: str, uid: int) -> None:
        """Profane text in each language resolves to a valid verdict."""
        response = client.post('/moderate', json={'text': text, 'app_name': 'a'})
        assert response.status_code == 200
        assert response.json()['verdict'] == expected
