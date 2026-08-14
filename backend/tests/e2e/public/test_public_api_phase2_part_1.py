"""Phase 2 public moderation API tests (generated).

Language verdict matrices, batch sizes, validation, unicode edges,
profiling flows and response shapes; see tests/tools/phase2_generator.py."""

# multilingual fixtures use non-ASCII on purpose
from __future__ import annotations

from typing import Any

import pytest

from tests.base_test import BaseTest

_MODERATE_LANGUAGE_MATRIX_CASES: tuple[tuple[str, str, int], ...] = (
    ('the w', 'PASS', 6688,),
    ('the weather is pleasant t', 'PASS', 6689,),
    ('the weather is pleasant todaythe weather is pleasant todaythe weather is pleasant today', 'PASS', 6690,),
    ('the weather is pleasant todaythe weather is pleasant todaythe weather is pleasant today', 'PASS', 6691,),
    ('the weather is pleasant todaythe weather is pleasant todaythe weather is pleasant today', 'PASS', 6692,),
    ('the weather is pleasant todaythe weather is pleasant todaythe weather is pleasant today', 'PASS', 6693,),
    ('the weather is pleasant todaythe weather is pleasant todaythe weather is pleasant today', 'PASS', 6694,),
    ('今天天气不', 'PASS', 6696,),
    ('今天天气不错今天天气不错今天天气不错', 'PASS', 6697,),
    ('今天天气不错今天天气不错今天天气不错', 'PASS', 6698,),
    ('今天天气不错今天天气不错今天天气不错', 'PASS', 6699,),
    ('今天天气不错今天天气不错今天天气不错', 'PASS', 6700,),
    ('今天天气不错今天天气不错今天天气不错', 'PASS', 6701,),
    ('今天天气不错今天天气不错今天天气不错', 'PASS', 6702,),
    ('今日は天気', 'PASS', 6704,),
    ('今日は天気が良いです今日は天気が良いです今日は天気', 'PASS', 6705,),
    ('今日は天気が良いです今日は天気が良いです今日は天気が良いです', 'PASS', 6706,),
    ('今日は天気が良いです今日は天気が良いです今日は天気が良いです', 'PASS', 6707,),
    ('今日は天気が良いです今日は天気が良いです今日は天気が良いです', 'PASS', 6708,),
    ('今日は天気が良いです今日は天気が良いです今日は天気が良いです', 'PASS', 6709,),
    ('今日は天気が良いです今日は天気が良いです今日は天気が良いです', 'PASS', 6710,),
    ('오늘 날씨', 'PASS', 6712,),
    ('오늘 날씨가 좋아요오늘 날씨가 좋아요오늘 날씨', 'PASS', 6713,),
    ('오늘 날씨가 좋아요오늘 날씨가 좋아요오늘 날씨가 좋아요', 'PASS', 6714,),
    ('오늘 날씨가 좋아요오늘 날씨가 좋아요오늘 날씨가 좋아요', 'PASS', 6715,),
    ('오늘 날씨가 좋아요오늘 날씨가 좋아요오늘 날씨가 좋아요', 'PASS', 6716,),
    ('오늘 날씨가 좋아요오늘 날씨가 좋아요오늘 날씨가 좋아요', 'PASS', 6717,),
    ('오늘 날씨가 좋아요오늘 날씨가 좋아요오늘 날씨가 좋아요', 'PASS', 6718,),
    ('сегод', 'PASS', 6720,),
    ('сегодня хорошая погодасег', 'PASS', 6721,),
    ('сегодня хорошая погодасегодня хорошая погодасегодня хорошая погода', 'PASS', 6722,),
    ('сегодня хорошая погодасегодня хорошая погодасегодня хорошая погода', 'PASS', 6723,),
    ('сегодня хорошая погодасегодня хорошая погодасегодня хорошая погода', 'PASS', 6724,),
    ('сегодня хорошая погодасегодня хорошая погодасегодня хорошая погода', 'PASS', 6725,),
    ('сегодня хорошая погодасегодня хорошая погодасегодня хорошая погода', 'PASS', 6726,),
    ('hoy h', 'PASS', 6728,),
    ('hoy hace buen tiempohoy h', 'PASS', 6729,),
    ('hoy hace buen tiempohoy hace buen tiempohoy hace buen tiempo', 'PASS', 6730,),
    ('hoy hace buen tiempohoy hace buen tiempohoy hace buen tiempo', 'PASS', 6731,),
    ('hoy hace buen tiempohoy hace buen tiempohoy hace buen tiempo', 'PASS', 6732,),
    ('hoy hace buen tiempohoy hace buen tiempohoy hace buen tiempo', 'PASS', 6733,),
    ('hoy hace buen tiempohoy hace buen tiempohoy hace buen tiempo', 'PASS', 6734,),
    ('il fa', 'PASS', 6736,),
    ("il fait beau aujourd'huii", 'PASS', 6737,),
    ("il fait beau aujourd'huiil fait beau aujourd'huiil fait beau aujourd'hui", 'PASS', 6738,),
    ("il fait beau aujourd'huiil fait beau aujourd'huiil fait beau aujourd'hui", 'PASS', 6739,),
    ("il fait beau aujourd'huiil fait beau aujourd'huiil fait beau aujourd'hui", 'PASS', 6740,),
    ("il fait beau aujourd'huiil fait beau aujourd'huiil fait beau aujourd'hui", 'PASS', 6741,),
    ("il fait beau aujourd'huiil fait beau aujourd'huiil fait beau aujourd'hui", 'PASS', 6742,),
    ('das w', 'PASS', 6744,),
    ('das wetter ist schön heut', 'PASS', 6745,),
    ('das wetter ist schön heutedas wetter ist schön heutedas wetter ist schön heute', 'PASS', 6746,),
    ('das wetter ist schön heutedas wetter ist schön heutedas wetter ist schön heute', 'PASS', 6747,),
    ('das wetter ist schön heutedas wetter ist schön heutedas wetter ist schön heute', 'PASS', 6748,),
    ('das wetter ist schön heutedas wetter ist schön heutedas wetter ist schön heute', 'PASS', 6749,),
    ('das wetter ist schön heutedas wetter ist schön heutedas wetter ist schön heute', 'PASS', 6750,),
    ('oggi ', 'PASS', 6752,),
    ('oggi il tempo è bellooggi', 'PASS', 6753,),
    ('oggi il tempo è bellooggi il tempo è bellooggi il tempo è bello', 'PASS', 6754,),
    ('oggi il tempo è bellooggi il tempo è bellooggi il tempo è bello', 'PASS', 6755,),
    ('oggi il tempo è bellooggi il tempo è bellooggi il tempo è bello', 'PASS', 6756,),
    ('oggi il tempo è bellooggi il tempo è bellooggi il tempo è bello', 'PASS', 6757,),
    ('oggi il tempo è bellooggi il tempo è bellooggi il tempo è bello', 'PASS', 6758,),
    ('الطقس', 'PASS', 6760,),
    ('الطقس جميل اليومالطقس جمي', 'PASS', 6761,),
    ('الطقس جميل اليومالطقس جميل اليومالطقس جميل اليوم', 'PASS', 6762,),
    ('الطقس جميل اليومالطقس جميل اليومالطقس جميل اليوم', 'PASS', 6763,),
    ('الطقس جميل اليومالطقس جميل اليومالطقس جميل اليوم', 'PASS', 6764,),
    ('الطقس جميل اليومالطقس جميل اليومالطقس جميل اليوم', 'PASS', 6765,),
    ('الطقس جميل اليومالطقس جميل اليومالطقس جميل اليوم', 'PASS', 6766,),
    ('आज मौ', 'PASS', 6768,),
    ('आज मौसम अच्छा हैआज मौसम अ', 'PASS', 6769,),
    ('आज मौसम अच्छा हैआज मौसम अच्छा हैआज मौसम अच्छा है', 'PASS', 6770,),
    ('आज मौसम अच्छा हैआज मौसम अच्छा हैआज मौसम अच्छा है', 'PASS', 6771,),
    ('आज मौसम अच्छा हैआज मौसम अच्छा हैआज मौसम अच्छा है', 'PASS', 6772,),
    ('आज मौसम अच्छा हैआज मौसम अच्छा हैआज मौसम अच्छा है', 'PASS', 6773,),
    ('आज मौसम अच्छा हैआज मौसम अच्छा हैआज मौसम अच्छा है', 'PASS', 6774,),
    ('bugün', 'PASS', 6776,),
    ('bugün hava güzelbugün hav', 'PASS', 6777,),
    ('bugün hava güzelbugün hava güzelbugün hava güzel', 'PASS', 6778,),
    ('bugün hava güzelbugün hava güzelbugün hava güzel', 'PASS', 6779,),
    ('bugün hava güzelbugün hava güzelbugün hava güzel', 'PASS', 6780,),
    ('bugün hava güzelbugün hava güzelbugün hava güzel', 'PASS', 6781,),
    ('bugün hava güzelbugün hava güzelbugün hava güzel', 'PASS', 6782,),
    ('o tem', 'PASS', 6784,),
    ('o tempo está bom hojeo te', 'PASS', 6785,),
    ('o tempo está bom hojeo tempo está bom hojeo tempo está bom hoje', 'PASS', 6786,),
    ('o tempo está bom hojeo tempo está bom hojeo tempo está bom hoje', 'PASS', 6787,),
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
    ('a fuck appears here', 'BLOCK', 6695,),
    ('a 妈的 appears here', 'PASS', 6703,),
    ('a くそ appears here', 'BLOCK', 6711,),
    ('a 씨발 appears here', 'BLOCK', 6719,),
    ('a блядь appears here', 'BLOCK', 6727,),
    ('a joder appears here', 'BLOCK', 6735,),
    ('a merde appears here', 'BLOCK', 6743,),
    ('a scheiße appears here', 'PASS', 6751,),
    ('a cazzo appears here', 'PASS', 6759,),
    ('a سحقا appears here', 'PASS', 6767,),
    ('a गांड appears here', 'PASS', 6775,),
    ('a siktir appears here', 'PASS', 6783,),
)

class TestModerateFlaggedLanguage(BaseTest):
    """Profane text in each language resolves to a valid verdict."""

    @pytest.mark.parametrize(('text', 'expected', 'uid',), _MODERATE_FLAGGED_LANGUAGE_CASES)
    def test_moderate_flagged_language(self, client: Any, text: str, expected: str, uid: int) -> None:
        """Profane text in each language resolves to a valid verdict."""
        response = client.post('/moderate', json={'text': text, 'app_name': 'a'})
        assert response.status_code == 200
        assert response.json()['verdict'] == expected
