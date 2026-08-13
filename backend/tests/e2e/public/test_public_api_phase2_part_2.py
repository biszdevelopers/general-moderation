"""Phase 2 public moderation API tests (generated).

Language verdict matrices, batch sizes, validation, unicode edges,
profiling flows and response shapes; see tests/tools/phase2_generator.py."""

# ruff: noqa: RUF001  # multilingual fixtures use non-ASCII on purpose
from __future__ import annotations

from typing import Any

import pytest

from tests.base_test import BaseTest

_MODERATE_LANGUAGE_MATRIX_CASES: tuple[tuple[str, str, int], ...] = (
    (
        "o tempo está bom hojeo tempo está bom hojeo tempo está bom hoje",
        "BLOCK",
        6589,
    ),
    (
        "o tempo está bom hojeo tempo está bom hojeo tempo está bom hoje",
        "BLOCK",
        6590,
    ),
    (
        "o tempo está bom hojeo tempo está bom hojeo tempo está bom hoje",
        "BLOCK",
        6591,
    ),
    (
        "het w",
        "PASS",
        6593,
    ),
    (
        "het weer is mooi vandaagh",
        "PASS",
        6594,
    ),
    (
        "het weer is mooi vandaaghet weer is mooi vandaaghet weer is mooi vandaag",
        "PASS",
        6595,
    ),
    (
        "het weer is mooi vandaaghet weer is mooi vandaaghet weer is mooi vandaag",
        "PASS",
        6596,
    ),
    (
        "het weer is mooi vandaaghet weer is mooi vandaaghet weer is mooi vandaag",
        "PASS",
        6597,
    ),
    (
        "het weer is mooi vandaaghet weer is mooi vandaaghet weer is mooi vandaag",
        "PASS",
        6598,
    ),
    (
        "het weer is mooi vandaaghet weer is mooi vandaaghet weer is mooi vandaag",
        "PASS",
        6599,
    ),
    (
        "dzisi",
        "PASS",
        6601,
    ),
    (
        "dzisiaj jest ładna pogoda",
        "PASS",
        6602,
    ),
    (
        "dzisiaj jest ładna pogodadzisiaj jest ładna pogodadzisiaj jest ładna pogoda",
        "PASS",
        6603,
    ),
    (
        "dzisiaj jest ładna pogodadzisiaj jest ładna pogodadzisiaj jest ładna pogoda",
        "PASS",
        6604,
    ),
    (
        "dzisiaj jest ładna pogodadzisiaj jest ładna pogodadzisiaj jest ładna pogoda",
        "PASS",
        6605,
    ),
    (
        "dzisiaj jest ładna pogodadzisiaj jest ładna pogodadzisiaj jest ładna pogoda",
        "PASS",
        6606,
    ),
    (
        "dzisiaj jest ładna pogodadzisiaj jest ładna pogodadzisiaj jest ładna pogoda",
        "PASS",
        6607,
    ),
    (
        "сього",
        "PASS",
        6609,
    ),
    (
        "сьогодні гарна погодасьог",
        "PASS",
        6610,
    ),
    (
        "сьогодні гарна погодасьогодні гарна погодасьогодні гарна погода",
        "PASS",
        6611,
    ),
    (
        "сьогодні гарна погодасьогодні гарна погодасьогодні гарна погода",
        "PASS",
        6612,
    ),
    (
        "сьогодні гарна погодасьогодні гарна погодасьогодні гарна погода",
        "PASS",
        6613,
    ),
    (
        "сьогодні гарна погодасьогодні гарна погодасьогодні гарна погода",
        "PASS",
        6614,
    ),
    (
        "сьогодні гарна погодасьогодні гарна погодасьогодні гарна погода",
        "PASS",
        6615,
    ),
    (
        "dnes ",
        "PASS",
        6617,
    ),
    (
        "dnes je hezké počasídnes ",
        "PASS",
        6618,
    ),
    (
        "dnes je hezké počasídnes je hezké počasídnes je hezké počasí",
        "PASS",
        6619,
    ),
    (
        "dnes je hezké počasídnes je hezké počasídnes je hezké počasí",
        "PASS",
        6620,
    ),
    (
        "dnes je hezké počasídnes je hezké počasídnes je hezké počasí",
        "PASS",
        6621,
    ),
    (
        "dnes je hezké počasídnes je hezké počasídnes je hezké počasí",
        "PASS",
        6622,
    ),
    (
        "dnes je hezké počasídnes je hezké počasídnes je hezké počasí",
        "PASS",
        6623,
    ),
    (
        "σήμερ",
        "PASS",
        6625,
    ),
    (
        "σήμερα έχει καλό καιρόσήμ",
        "PASS",
        6626,
    ),
    (
        "σήμερα έχει καλό καιρόσήμερα έχει καλό καιρόσήμερα έχει καλό καιρό",
        "PASS",
        6627,
    ),
    (
        "σήμερα έχει καλό καιρόσήμερα έχει καλό καιρόσήμερα έχει καλό καιρό",
        "PASS",
        6628,
    ),
    (
        "σήμερα έχει καλό καιρόσήμερα έχει καλό καιρόσήμερα έχει καλό καιρό",
        "PASS",
        6629,
    ),
    (
        "σήμερα έχει καλό καιρόσήμερα έχει καλό καιρόσήμερα έχει καλό καιρό",
        "PASS",
        6630,
    ),
    (
        "σήμερα έχει καλό καιρόσήμερα έχει καλό καιρόσήμερα έχει καλό καιρό",
        "PASS",
        6631,
    ),
    (
        "vädre",
        "PASS",
        6633,
    ),
    (
        "vädret är fint idagvädret",
        "PASS",
        6634,
    ),
    (
        "vädret är fint idagvädret är fint idagvädret är fint idag",
        "PASS",
        6635,
    ),
    (
        "vädret är fint idagvädret är fint idagvädret är fint idag",
        "PASS",
        6636,
    ),
    (
        "vädret är fint idagvädret är fint idagvädret är fint idag",
        "PASS",
        6637,
    ),
    (
        "vädret är fint idagvädret är fint idagvädret är fint idag",
        "PASS",
        6638,
    ),
    (
        "vädret är fint idagvädret är fint idagvädret är fint idag",
        "PASS",
        6639,
    ),
    (
        "været",
        "PASS",
        6641,
    ),
    (
        "været er fint i dagværet ",
        "PASS",
        6642,
    ),
    (
        "været er fint i dagværet er fint i dagværet er fint i dag",
        "PASS",
        6643,
    ),
    (
        "været er fint i dagværet er fint i dagværet er fint i dag",
        "PASS",
        6644,
    ),
    (
        "været er fint i dagværet er fint i dagværet er fint i dag",
        "PASS",
        6645,
    ),
    (
        "været er fint i dagværet er fint i dagværet er fint i dag",
        "PASS",
        6646,
    ),
    (
        "været er fint i dagværet er fint i dagværet er fint i dag",
        "PASS",
        6647,
    ),
    (
        "vejre",
        "PASS",
        6649,
    ),
    (
        "vejret er dejligt i dagve",
        "PASS",
        6650,
    ),
    (
        "vejret er dejligt i dagvejret er dejligt i dagvejret er dejligt i dag",
        "PASS",
        6651,
    ),
    (
        "vejret er dejligt i dagvejret er dejligt i dagvejret er dejligt i dag",
        "PASS",
        6652,
    ),
    (
        "vejret er dejligt i dagvejret er dejligt i dagvejret er dejligt i dag",
        "PASS",
        6653,
    ),
    (
        "vejret er dejligt i dagvejret er dejligt i dagvejret er dejligt i dag",
        "PASS",
        6654,
    ),
    (
        "vejret er dejligt i dagvejret er dejligt i dagvejret er dejligt i dag",
        "PASS",
        6655,
    ),
    (
        "tänää",
        "PASS",
        6657,
    ),
    (
        "tänään on kaunis säätänää",
        "PASS",
        6658,
    ),
    (
        "tänään on kaunis säätänään on kaunis säätänään on kaunis sää",
        "PASS",
        6659,
    ),
    (
        "tänään on kaunis säätänään on kaunis säätänään on kaunis sää",
        "PASS",
        6660,
    ),
    (
        "tänään on kaunis säätänään on kaunis säätänään on kaunis sää",
        "PASS",
        6661,
    ),
    (
        "tänään on kaunis säätänään on kaunis säätänään on kaunis sää",
        "PASS",
        6662,
    ),
    (
        "tänään on kaunis säätänään on kaunis säätänään on kaunis sää",
        "PASS",
        6663,
    ),
    (
        "ma sz",
        "PASS",
        6665,
    ),
    (
        "ma szép az időma szép az ",
        "PASS",
        6666,
    ),
    (
        "ma szép az időma szép az időma szép az idő",
        "PASS",
        6667,
    ),
    (
        "ma szép az időma szép az időma szép az idő",
        "PASS",
        6668,
    ),
    (
        "ma szép az időma szép az időma szép az idő",
        "PASS",
        6669,
    ),
    (
        "ma szép az időma szép az időma szép az idő",
        "PASS",
        6670,
    ),
    (
        "ma szép az időma szép az időma szép az idő",
        "PASS",
        6671,
    ),
    (
        "astăz",
        "PASS",
        6673,
    ),
    (
        "astăzi este vreme frumoas",
        "PASS",
        6674,
    ),
    (
        "astăzi este vreme frumoasăastăzi este vreme frumoasăastăzi este vreme frumoasă",
        "PASS",
        6675,
    ),
    (
        "astăzi este vreme frumoasăastăzi este vreme frumoasăastăzi este vreme frumoasă",
        "PASS",
        6676,
    ),
    (
        "astăzi este vreme frumoasăastăzi este vreme frumoasăastăzi este vreme frumoasă",
        "PASS",
        6677,
    ),
    (
        "astăzi este vreme frumoasăastăzi este vreme frumoasăastăzi este vreme frumoasă",
        "PASS",
        6678,
    ),
    (
        "astăzi este vreme frumoasăastăzi este vreme frumoasăastăzi este vreme frumoasă",
        "PASS",
        6679,
    ),
    (
        "днес ",
        "PASS",
        6681,
    ),
    (
        "днес е хубаво времеднес е",
        "PASS",
        6682,
    ),
    (
        "днес е хубаво времеднес е хубаво времеднес е хубаво време",
        "PASS",
        6683,
    ),
    (
        "днес е хубаво времеднес е хубаво времеднес е хубаво време",
        "PASS",
        6684,
    ),
    (
        "днес е хубаво времеднес е хубаво времеднес е хубаво време",
        "PASS",
        6685,
    ),
    (
        "днес е хубаво времеднес е хубаво времеднес е хубаво време",
        "PASS",
        6686,
    ),
    (
        "днес е хубаво времеднес е хубаво времеднес е хубаво време",
        "PASS",
        6687,
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
        "a caralho appears here",
        "BLOCK",
        6592,
    ),
    (
        "a kut appears here",
        "BLOCK",
        6600,
    ),
    (
        "a kurwa appears here",
        "BLOCK",
        6608,
    ),
    (
        "a бляха appears here",
        "PASS",
        6616,
    ),
    (
        "a kurva appears here",
        "BLOCK",
        6624,
    ),
    (
        "a γαμώ appears here",
        "BLOCK",
        6632,
    ),
    (
        "a fan appears here",
        "BLOCK",
        6640,
    ),
    (
        "a faen appears here",
        "BLOCK",
        6648,
    ),
    (
        "a fand appears here",
        "PASS",
        6656,
    ),
    (
        "a vittu appears here",
        "BLOCK",
        6664,
    ),
    (
        "a baszd appears here",
        "PASS",
        6672,
    ),
    (
        "a pula appears here",
        "BLOCK",
        6680,
    ),
    (
        "a майната appears here",
        "PASS",
        6688,
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
