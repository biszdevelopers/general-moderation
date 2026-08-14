"""Phase 2 public moderation API tests (generated).

Language verdict matrices, batch sizes, validation, unicode edges,
profiling flows and response shapes; see tests/tools/phase2_generator.py."""

# ruff: noqa: RUF001  # multilingual fixtures use non-ASCII on purpose
from __future__ import annotations

from typing import Any

import pytest

from tests.base_test import BaseTest

_MODERATE_LANGUAGE_MATRIX_CASES: tuple[tuple[str, str, int], ...] = (
    ('o tempo está bom hojeo tempo está bom hojeo tempo está bom hoje', 'PASS', 6788,),
    ('o tempo está bom hojeo tempo está bom hojeo tempo está bom hoje', 'PASS', 6789,),
    ('o tempo está bom hojeo tempo está bom hojeo tempo está bom hoje', 'PASS', 6790,),
    ('het w', 'PASS', 6792,),
    ('het weer is mooi vandaagh', 'PASS', 6793,),
    ('het weer is mooi vandaaghet weer is mooi vandaaghet weer is mooi vandaag', 'PASS', 6794,),
    ('het weer is mooi vandaaghet weer is mooi vandaaghet weer is mooi vandaag', 'PASS', 6795,),
    ('het weer is mooi vandaaghet weer is mooi vandaaghet weer is mooi vandaag', 'PASS', 6796,),
    ('het weer is mooi vandaaghet weer is mooi vandaaghet weer is mooi vandaag', 'PASS', 6797,),
    ('het weer is mooi vandaaghet weer is mooi vandaaghet weer is mooi vandaag', 'PASS', 6798,),
    ('dzisi', 'PASS', 6800,),
    ('dzisiaj jest ładna pogoda', 'PASS', 6801,),
    ('dzisiaj jest ładna pogodadzisiaj jest ładna pogodadzisiaj jest ładna pogoda', 'PASS', 6802,),
    ('dzisiaj jest ładna pogodadzisiaj jest ładna pogodadzisiaj jest ładna pogoda', 'PASS', 6803,),
    ('dzisiaj jest ładna pogodadzisiaj jest ładna pogodadzisiaj jest ładna pogoda', 'PASS', 6804,),
    ('dzisiaj jest ładna pogodadzisiaj jest ładna pogodadzisiaj jest ładna pogoda', 'PASS', 6805,),
    ('dzisiaj jest ładna pogodadzisiaj jest ładna pogodadzisiaj jest ładna pogoda', 'PASS', 6806,),
    ('сього', 'PASS', 6808,),
    ('сьогодні гарна погодасьог', 'PASS', 6809,),
    ('сьогодні гарна погодасьогодні гарна погодасьогодні гарна погода', 'PASS', 6810,),
    ('сьогодні гарна погодасьогодні гарна погодасьогодні гарна погода', 'PASS', 6811,),
    ('сьогодні гарна погодасьогодні гарна погодасьогодні гарна погода', 'PASS', 6812,),
    ('сьогодні гарна погодасьогодні гарна погодасьогодні гарна погода', 'PASS', 6813,),
    ('сьогодні гарна погодасьогодні гарна погодасьогодні гарна погода', 'PASS', 6814,),
    ('dnes ', 'PASS', 6816,),
    ('dnes je hezké počasídnes ', 'PASS', 6817,),
    ('dnes je hezké počasídnes je hezké počasídnes je hezké počasí', 'PASS', 6818,),
    ('dnes je hezké počasídnes je hezké počasídnes je hezké počasí', 'PASS', 6819,),
    ('dnes je hezké počasídnes je hezké počasídnes je hezké počasí', 'PASS', 6820,),
    ('dnes je hezké počasídnes je hezké počasídnes je hezké počasí', 'PASS', 6821,),
    ('dnes je hezké počasídnes je hezké počasídnes je hezké počasí', 'PASS', 6822,),
    ('σήμερ', 'PASS', 6824,),
    ('σήμερα έχει καλό καιρόσήμ', 'PASS', 6825,),
    ('σήμερα έχει καλό καιρόσήμερα έχει καλό καιρόσήμερα έχει καλό καιρό', 'PASS', 6826,),
    ('σήμερα έχει καλό καιρόσήμερα έχει καλό καιρόσήμερα έχει καλό καιρό', 'PASS', 6827,),
    ('σήμερα έχει καλό καιρόσήμερα έχει καλό καιρόσήμερα έχει καλό καιρό', 'PASS', 6828,),
    ('σήμερα έχει καλό καιρόσήμερα έχει καλό καιρόσήμερα έχει καλό καιρό', 'PASS', 6829,),
    ('σήμερα έχει καλό καιρόσήμερα έχει καλό καιρόσήμερα έχει καλό καιρό', 'PASS', 6830,),
    ('vädre', 'PASS', 6832,),
    ('vädret är fint idagvädret', 'PASS', 6833,),
    ('vädret är fint idagvädret är fint idagvädret är fint idag', 'PASS', 6834,),
    ('vädret är fint idagvädret är fint idagvädret är fint idag', 'PASS', 6835,),
    ('vädret är fint idagvädret är fint idagvädret är fint idag', 'PASS', 6836,),
    ('vädret är fint idagvädret är fint idagvädret är fint idag', 'PASS', 6837,),
    ('vädret är fint idagvädret är fint idagvädret är fint idag', 'PASS', 6838,),
    ('været', 'PASS', 6840,),
    ('været er fint i dagværet ', 'PASS', 6841,),
    ('været er fint i dagværet er fint i dagværet er fint i dag', 'PASS', 6842,),
    ('været er fint i dagværet er fint i dagværet er fint i dag', 'PASS', 6843,),
    ('været er fint i dagværet er fint i dagværet er fint i dag', 'PASS', 6844,),
    ('været er fint i dagværet er fint i dagværet er fint i dag', 'PASS', 6845,),
    ('været er fint i dagværet er fint i dagværet er fint i dag', 'PASS', 6846,),
    ('vejre', 'PASS', 6848,),
    ('vejret er dejligt i dagve', 'PASS', 6849,),
    ('vejret er dejligt i dagvejret er dejligt i dagvejret er dejligt i dag', 'PASS', 6850,),
    ('vejret er dejligt i dagvejret er dejligt i dagvejret er dejligt i dag', 'PASS', 6851,),
    ('vejret er dejligt i dagvejret er dejligt i dagvejret er dejligt i dag', 'PASS', 6852,),
    ('vejret er dejligt i dagvejret er dejligt i dagvejret er dejligt i dag', 'PASS', 6853,),
    ('vejret er dejligt i dagvejret er dejligt i dagvejret er dejligt i dag', 'PASS', 6854,),
    ('tänää', 'PASS', 6856,),
    ('tänään on kaunis säätänää', 'PASS', 6857,),
    ('tänään on kaunis säätänään on kaunis säätänään on kaunis sää', 'PASS', 6858,),
    ('tänään on kaunis säätänään on kaunis säätänään on kaunis sää', 'PASS', 6859,),
    ('tänään on kaunis säätänään on kaunis säätänään on kaunis sää', 'PASS', 6860,),
    ('tänään on kaunis säätänään on kaunis säätänään on kaunis sää', 'PASS', 6861,),
    ('tänään on kaunis säätänään on kaunis säätänään on kaunis sää', 'PASS', 6862,),
    ('ma sz', 'PASS', 6864,),
    ('ma szép az időma szép az ', 'PASS', 6865,),
    ('ma szép az időma szép az időma szép az idő', 'PASS', 6866,),
    ('ma szép az időma szép az időma szép az idő', 'PASS', 6867,),
    ('ma szép az időma szép az időma szép az idő', 'PASS', 6868,),
    ('ma szép az időma szép az időma szép az idő', 'PASS', 6869,),
    ('ma szép az időma szép az időma szép az idő', 'PASS', 6870,),
    ('astăz', 'PASS', 6872,),
    ('astăzi este vreme frumoas', 'PASS', 6873,),
    ('astăzi este vreme frumoasăastăzi este vreme frumoasăastăzi este vreme frumoasă', 'PASS', 6874,),
    ('astăzi este vreme frumoasăastăzi este vreme frumoasăastăzi este vreme frumoasă', 'PASS', 6875,),
    ('astăzi este vreme frumoasăastăzi este vreme frumoasăastăzi este vreme frumoasă', 'PASS', 6876,),
    ('astăzi este vreme frumoasăastăzi este vreme frumoasăastăzi este vreme frumoasă', 'PASS', 6877,),
    ('astăzi este vreme frumoasăastăzi este vreme frumoasăastăzi este vreme frumoasă', 'PASS', 6878,),
    ('днес ', 'PASS', 6880,),
    ('днес е хубаво времеднес е', 'PASS', 6881,),
    ('днес е хубаво времеднес е хубаво времеднес е хубаво време', 'PASS', 6882,),
    ('днес е хубаво времеднес е хубаво времеднес е хубаво време', 'PASS', 6883,),
    ('днес е хубаво времеднес е хубаво времеднес е хубаво време', 'PASS', 6884,),
    ('днес е хубаво времеднес е хубаво времеднес е хубаво време', 'PASS', 6885,),
    ('днес е хубаво времеднес е хубаво времеднес е хубаво време', 'PASS', 6886,),
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
    ('a caralho appears here', 'PASS', 6791,),
    ('a kut appears here', 'BLOCK', 6799,),
    ('a kurwa appears here', 'BLOCK', 6807,),
    ('a бляха appears here', 'PASS', 6815,),
    ('a kurva appears here', 'BLOCK', 6823,),
    ('a γαμώ appears here', 'BLOCK', 6831,),
    ('a fan appears here', 'PASS', 6839,),
    ('a faen appears here', 'BLOCK', 6847,),
    ('a fand appears here', 'PASS', 6855,),
    ('a vittu appears here', 'PASS', 6863,),
    ('a baszd appears here', 'PASS', 6871,),
    ('a pula appears here', 'BLOCK', 6879,),
    ('a майната appears here', 'PASS', 6887,),
)

class TestModerateFlaggedLanguage(BaseTest):
    """Profane text in each language resolves to a valid verdict."""

    @pytest.mark.parametrize(('text', 'expected', 'uid',), _MODERATE_FLAGGED_LANGUAGE_CASES)
    def test_moderate_flagged_language(self, client: Any, text: str, expected: str, uid: int) -> None:
        """Profane text in each language resolves to a valid verdict."""
        response = client.post('/moderate', json={'text': text, 'app_name': 'a'})
        assert response.status_code == 200
        assert response.json()['verdict'] == expected
