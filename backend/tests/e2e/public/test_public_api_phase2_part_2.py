"""Phase 2 public moderation API tests (generated).

Language verdict matrices, batch sizes, validation, unicode edges,
profiling flows and response shapes; see tests/tools/phase2_generator.py."""

# ruff: noqa: RUF001  # multilingual fixtures use non-ASCII on purpose
from __future__ import annotations

from typing import Any

import pytest

from tests.base_test import BaseTest

_MODERATE_LANGUAGE_MATRIX_CASES: tuple[tuple[str, str, int], ...] = (
    ('o tempo está bom hojeo tempo está bom hojeo tempo está bom hoje', 'PASS', 6748,),
    ('o tempo está bom hojeo tempo está bom hojeo tempo está bom hoje', 'PASS', 6749,),
    ('o tempo está bom hojeo tempo está bom hojeo tempo está bom hoje', 'PASS', 6750,),
    ('het w', 'PASS', 6752,),
    ('het weer is mooi vandaagh', 'PASS', 6753,),
    ('het weer is mooi vandaaghet weer is mooi vandaaghet weer is mooi vandaag', 'PASS', 6754,),
    ('het weer is mooi vandaaghet weer is mooi vandaaghet weer is mooi vandaag', 'PASS', 6755,),
    ('het weer is mooi vandaaghet weer is mooi vandaaghet weer is mooi vandaag', 'PASS', 6756,),
    ('het weer is mooi vandaaghet weer is mooi vandaaghet weer is mooi vandaag', 'PASS', 6757,),
    ('het weer is mooi vandaaghet weer is mooi vandaaghet weer is mooi vandaag', 'PASS', 6758,),
    ('dzisi', 'PASS', 6760,),
    ('dzisiaj jest ładna pogoda', 'PASS', 6761,),
    ('dzisiaj jest ładna pogodadzisiaj jest ładna pogodadzisiaj jest ładna pogoda', 'PASS', 6762,),
    ('dzisiaj jest ładna pogodadzisiaj jest ładna pogodadzisiaj jest ładna pogoda', 'PASS', 6763,),
    ('dzisiaj jest ładna pogodadzisiaj jest ładna pogodadzisiaj jest ładna pogoda', 'PASS', 6764,),
    ('dzisiaj jest ładna pogodadzisiaj jest ładna pogodadzisiaj jest ładna pogoda', 'PASS', 6765,),
    ('dzisiaj jest ładna pogodadzisiaj jest ładna pogodadzisiaj jest ładna pogoda', 'PASS', 6766,),
    ('сього', 'PASS', 6768,),
    ('сьогодні гарна погодасьог', 'PASS', 6769,),
    ('сьогодні гарна погодасьогодні гарна погодасьогодні гарна погода', 'PASS', 6770,),
    ('сьогодні гарна погодасьогодні гарна погодасьогодні гарна погода', 'PASS', 6771,),
    ('сьогодні гарна погодасьогодні гарна погодасьогодні гарна погода', 'PASS', 6772,),
    ('сьогодні гарна погодасьогодні гарна погодасьогодні гарна погода', 'PASS', 6773,),
    ('сьогодні гарна погодасьогодні гарна погодасьогодні гарна погода', 'PASS', 6774,),
    ('dnes ', 'PASS', 6776,),
    ('dnes je hezké počasídnes ', 'PASS', 6777,),
    ('dnes je hezké počasídnes je hezké počasídnes je hezké počasí', 'PASS', 6778,),
    ('dnes je hezké počasídnes je hezké počasídnes je hezké počasí', 'PASS', 6779,),
    ('dnes je hezké počasídnes je hezké počasídnes je hezké počasí', 'PASS', 6780,),
    ('dnes je hezké počasídnes je hezké počasídnes je hezké počasí', 'PASS', 6781,),
    ('dnes je hezké počasídnes je hezké počasídnes je hezké počasí', 'PASS', 6782,),
    ('σήμερ', 'PASS', 6784,),
    ('σήμερα έχει καλό καιρόσήμ', 'PASS', 6785,),
    ('σήμερα έχει καλό καιρόσήμερα έχει καλό καιρόσήμερα έχει καλό καιρό', 'PASS', 6786,),
    ('σήμερα έχει καλό καιρόσήμερα έχει καλό καιρόσήμερα έχει καλό καιρό', 'PASS', 6787,),
    ('σήμερα έχει καλό καιρόσήμερα έχει καλό καιρόσήμερα έχει καλό καιρό', 'PASS', 6788,),
    ('σήμερα έχει καλό καιρόσήμερα έχει καλό καιρόσήμερα έχει καλό καιρό', 'PASS', 6789,),
    ('σήμερα έχει καλό καιρόσήμερα έχει καλό καιρόσήμερα έχει καλό καιρό', 'PASS', 6790,),
    ('vädre', 'PASS', 6792,),
    ('vädret är fint idagvädret', 'PASS', 6793,),
    ('vädret är fint idagvädret är fint idagvädret är fint idag', 'PASS', 6794,),
    ('vädret är fint idagvädret är fint idagvädret är fint idag', 'PASS', 6795,),
    ('vädret är fint idagvädret är fint idagvädret är fint idag', 'PASS', 6796,),
    ('vädret är fint idagvädret är fint idagvädret är fint idag', 'PASS', 6797,),
    ('vädret är fint idagvädret är fint idagvädret är fint idag', 'PASS', 6798,),
    ('været', 'PASS', 6800,),
    ('været er fint i dagværet ', 'PASS', 6801,),
    ('været er fint i dagværet er fint i dagværet er fint i dag', 'PASS', 6802,),
    ('været er fint i dagværet er fint i dagværet er fint i dag', 'PASS', 6803,),
    ('været er fint i dagværet er fint i dagværet er fint i dag', 'PASS', 6804,),
    ('været er fint i dagværet er fint i dagværet er fint i dag', 'PASS', 6805,),
    ('været er fint i dagværet er fint i dagværet er fint i dag', 'PASS', 6806,),
    ('vejre', 'PASS', 6808,),
    ('vejret er dejligt i dagve', 'PASS', 6809,),
    ('vejret er dejligt i dagvejret er dejligt i dagvejret er dejligt i dag', 'PASS', 6810,),
    ('vejret er dejligt i dagvejret er dejligt i dagvejret er dejligt i dag', 'PASS', 6811,),
    ('vejret er dejligt i dagvejret er dejligt i dagvejret er dejligt i dag', 'PASS', 6812,),
    ('vejret er dejligt i dagvejret er dejligt i dagvejret er dejligt i dag', 'PASS', 6813,),
    ('vejret er dejligt i dagvejret er dejligt i dagvejret er dejligt i dag', 'PASS', 6814,),
    ('tänää', 'PASS', 6816,),
    ('tänään on kaunis säätänää', 'PASS', 6817,),
    ('tänään on kaunis säätänään on kaunis säätänään on kaunis sää', 'PASS', 6818,),
    ('tänään on kaunis säätänään on kaunis säätänään on kaunis sää', 'PASS', 6819,),
    ('tänään on kaunis säätänään on kaunis säätänään on kaunis sää', 'PASS', 6820,),
    ('tänään on kaunis säätänään on kaunis säätänään on kaunis sää', 'PASS', 6821,),
    ('tänään on kaunis säätänään on kaunis säätänään on kaunis sää', 'PASS', 6822,),
    ('ma sz', 'PASS', 6824,),
    ('ma szép az időma szép az ', 'PASS', 6825,),
    ('ma szép az időma szép az időma szép az idő', 'PASS', 6826,),
    ('ma szép az időma szép az időma szép az idő', 'PASS', 6827,),
    ('ma szép az időma szép az időma szép az idő', 'PASS', 6828,),
    ('ma szép az időma szép az időma szép az idő', 'PASS', 6829,),
    ('ma szép az időma szép az időma szép az idő', 'PASS', 6830,),
    ('astăz', 'PASS', 6832,),
    ('astăzi este vreme frumoas', 'PASS', 6833,),
    ('astăzi este vreme frumoasăastăzi este vreme frumoasăastăzi este vreme frumoasă', 'PASS', 6834,),
    ('astăzi este vreme frumoasăastăzi este vreme frumoasăastăzi este vreme frumoasă', 'PASS', 6835,),
    ('astăzi este vreme frumoasăastăzi este vreme frumoasăastăzi este vreme frumoasă', 'PASS', 6836,),
    ('astăzi este vreme frumoasăastăzi este vreme frumoasăastăzi este vreme frumoasă', 'PASS', 6837,),
    ('astăzi este vreme frumoasăastăzi este vreme frumoasăastăzi este vreme frumoasă', 'PASS', 6838,),
    ('днес ', 'PASS', 6840,),
    ('днес е хубаво времеднес е', 'PASS', 6841,),
    ('днес е хубаво времеднес е хубаво времеднес е хубаво време', 'PASS', 6842,),
    ('днес е хубаво времеднес е хубаво времеднес е хубаво време', 'PASS', 6843,),
    ('днес е хубаво времеднес е хубаво времеднес е хубаво време', 'PASS', 6844,),
    ('днес е хубаво времеднес е хубаво времеднес е хубаво време', 'PASS', 6845,),
    ('днес е хубаво времеднес е хубаво времеднес е хубаво време', 'PASS', 6846,),
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
    ('a caralho appears here', 'BLOCK', 6751,),
    ('a kut appears here', 'BLOCK', 6759,),
    ('a kurwa appears here', 'BLOCK', 6767,),
    ('a бляха appears here', 'PASS', 6775,),
    ('a kurva appears here', 'BLOCK', 6783,),
    ('a γαμώ appears here', 'BLOCK', 6791,),
    ('a fan appears here', 'BLOCK', 6799,),
    ('a faen appears here', 'BLOCK', 6807,),
    ('a fand appears here', 'PASS', 6815,),
    ('a vittu appears here', 'BLOCK', 6823,),
    ('a baszd appears here', 'PASS', 6831,),
    ('a pula appears here', 'BLOCK', 6839,),
    ('a майната appears here', 'PASS', 6847,),
)

class TestModerateFlaggedLanguage(BaseTest):
    """Profane text in each language resolves to a valid verdict."""

    @pytest.mark.parametrize(('text', 'expected', 'uid',), _MODERATE_FLAGGED_LANGUAGE_CASES)
    def test_moderate_flagged_language(self, client: Any, text: str, expected: str, uid: int) -> None:
        """Profane text in each language resolves to a valid verdict."""
        response = client.post('/moderate', json={'text': text, 'app_name': 'a'})
        assert response.status_code == 200
        assert response.json()['verdict'] == expected
