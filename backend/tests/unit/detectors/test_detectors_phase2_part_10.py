"""Phase 2 detector tests (golden master, generated).

Computed from the locked test environment; see tests/tools/phase2_generator.py."""

# ruff: noqa: RUF001  # multilingual fixtures use non-ASCII on purpose
from __future__ import annotations

from typing import Any

from app.config import Settings
from app.detectors.multi_language_detector import MultiLanguageDetector
from tests.base_test import BaseTest


class TestSafetextGuard(BaseTest):
    """SafetextGuard scenarios."""

    def test_guard_safetext_3_en_901(self, engine: Any) -> None:
        """The safetext guard stays inert when the package is missing."""
        settings: Settings = engine._settings
        settings.enable_safetext = True
        for key in (
            "enable_badwords_py",
            "enable_profanite",
            "enable_glin_profanity",
            "enable_gangajal",
        ):
            setattr(settings, key, False)
        detector: MultiLanguageDetector = MultiLanguageDetector(settings, None)
        assert detector.detect("some harmless sentence here").matched is False

    def test_guard_safetext_3_ja_902(self, engine: Any) -> None:
        """The safetext guard stays inert when the package is missing."""
        settings: Settings = engine._settings
        settings.enable_safetext = True
        for key in (
            "enable_badwords_py",
            "enable_profanite",
            "enable_glin_profanity",
            "enable_gangajal",
        ):
            setattr(settings, key, False)
        detector: MultiLanguageDetector = MultiLanguageDetector(settings, None)
        assert detector.detect("これは普通の文章です").matched is False

    def test_guard_safetext_3_ar_903(self, engine: Any) -> None:
        """The safetext guard stays inert when the package is missing."""
        settings: Settings = engine._settings
        settings.enable_safetext = True
        for key in (
            "enable_badwords_py",
            "enable_profanite",
            "enable_glin_profanity",
            "enable_gangajal",
        ):
            setattr(settings, key, False)
        detector: MultiLanguageDetector = MultiLanguageDetector(settings, None)
        assert detector.detect("هذه جملة عادية").matched is False

    def test_guard_safetext_3_ru_904(self, engine: Any) -> None:
        """The safetext guard stays inert when the package is missing."""
        settings: Settings = engine._settings
        settings.enable_safetext = True
        for key in (
            "enable_badwords_py",
            "enable_profanite",
            "enable_glin_profanity",
            "enable_gangajal",
        ):
            setattr(settings, key, False)
        detector: MultiLanguageDetector = MultiLanguageDetector(settings, None)
        assert detector.detect("обычное безобидное предложение").matched is False

    def test_guard_safetext_3_ko_905(self, engine: Any) -> None:
        """The safetext guard stays inert when the package is missing."""
        settings: Settings = engine._settings
        settings.enable_safetext = True
        for key in (
            "enable_badwords_py",
            "enable_profanite",
            "enable_glin_profanity",
            "enable_gangajal",
        ):
            setattr(settings, key, False)
        detector: MultiLanguageDetector = MultiLanguageDetector(settings, None)
        assert detector.detect("이건 평범한 문장입니다").matched is False

    def test_guard_safetext_3_de_906(self, engine: Any) -> None:
        """The safetext guard stays inert when the package is missing."""
        settings: Settings = engine._settings
        settings.enable_safetext = True
        for key in (
            "enable_badwords_py",
            "enable_profanite",
            "enable_glin_profanity",
            "enable_gangajal",
        ):
            setattr(settings, key, False)
        detector: MultiLanguageDetector = MultiLanguageDetector(settings, None)
        assert detector.detect("ein völlig harmloser satz").matched is False

    def test_guard_safetext_3_fr_907(self, engine: Any) -> None:
        """The safetext guard stays inert when the package is missing."""
        settings: Settings = engine._settings
        settings.enable_safetext = True
        for key in (
            "enable_badwords_py",
            "enable_profanite",
            "enable_glin_profanity",
            "enable_gangajal",
        ):
            setattr(settings, key, False)
        detector: MultiLanguageDetector = MultiLanguageDetector(settings, None)
        assert detector.detect("une phrase tout à fait banale").matched is False

    def test_guard_safetext_3_it_908(self, engine: Any) -> None:
        """The safetext guard stays inert when the package is missing."""
        settings: Settings = engine._settings
        settings.enable_safetext = True
        for key in (
            "enable_badwords_py",
            "enable_profanite",
            "enable_glin_profanity",
            "enable_gangajal",
        ):
            setattr(settings, key, False)
        detector: MultiLanguageDetector = MultiLanguageDetector(settings, None)
        assert detector.detect("una frase assolutamente innocua").matched is False

    def test_guard_safetext_3_hi_909(self, engine: Any) -> None:
        """The safetext guard stays inert when the package is missing."""
        settings: Settings = engine._settings
        settings.enable_safetext = True
        for key in (
            "enable_badwords_py",
            "enable_profanite",
            "enable_glin_profanity",
            "enable_gangajal",
        ):
            setattr(settings, key, False)
        detector: MultiLanguageDetector = MultiLanguageDetector(settings, None)
        assert detector.detect("यह एक साधारण वाक्य है").matched is False

    def test_guard_safetext_3_tr_910(self, engine: Any) -> None:
        """The safetext guard stays inert when the package is missing."""
        settings: Settings = engine._settings
        settings.enable_safetext = True
        for key in (
            "enable_badwords_py",
            "enable_profanite",
            "enable_glin_profanity",
            "enable_gangajal",
        ):
            setattr(settings, key, False)
        detector: MultiLanguageDetector = MultiLanguageDetector(settings, None)
        assert detector.detect("bu zararsız bir cümle").matched is False

    def test_guard_safetext_4_en_911(self, engine: Any) -> None:
        """The safetext guard stays inert when the package is missing."""
        settings: Settings = engine._settings
        settings.enable_safetext = True
        for key in (
            "enable_badwords_py",
            "enable_profanite",
            "enable_glin_profanity",
            "enable_gangajal",
        ):
            setattr(settings, key, False)
        detector: MultiLanguageDetector = MultiLanguageDetector(settings, None)
        assert detector.detect("some harmless sentence here").matched is False

    def test_guard_safetext_4_ja_912(self, engine: Any) -> None:
        """The safetext guard stays inert when the package is missing."""
        settings: Settings = engine._settings
        settings.enable_safetext = True
        for key in (
            "enable_badwords_py",
            "enable_profanite",
            "enable_glin_profanity",
            "enable_gangajal",
        ):
            setattr(settings, key, False)
        detector: MultiLanguageDetector = MultiLanguageDetector(settings, None)
        assert detector.detect("これは普通の文章です").matched is False

    def test_guard_safetext_4_ar_913(self, engine: Any) -> None:
        """The safetext guard stays inert when the package is missing."""
        settings: Settings = engine._settings
        settings.enable_safetext = True
        for key in (
            "enable_badwords_py",
            "enable_profanite",
            "enable_glin_profanity",
            "enable_gangajal",
        ):
            setattr(settings, key, False)
        detector: MultiLanguageDetector = MultiLanguageDetector(settings, None)
        assert detector.detect("هذه جملة عادية").matched is False

    def test_guard_safetext_4_ru_914(self, engine: Any) -> None:
        """The safetext guard stays inert when the package is missing."""
        settings: Settings = engine._settings
        settings.enable_safetext = True
        for key in (
            "enable_badwords_py",
            "enable_profanite",
            "enable_glin_profanity",
            "enable_gangajal",
        ):
            setattr(settings, key, False)
        detector: MultiLanguageDetector = MultiLanguageDetector(settings, None)
        assert detector.detect("обычное безобидное предложение").matched is False

    def test_guard_safetext_4_ko_915(self, engine: Any) -> None:
        """The safetext guard stays inert when the package is missing."""
        settings: Settings = engine._settings
        settings.enable_safetext = True
        for key in (
            "enable_badwords_py",
            "enable_profanite",
            "enable_glin_profanity",
            "enable_gangajal",
        ):
            setattr(settings, key, False)
        detector: MultiLanguageDetector = MultiLanguageDetector(settings, None)
        assert detector.detect("이건 평범한 문장입니다").matched is False

    def test_guard_safetext_4_de_916(self, engine: Any) -> None:
        """The safetext guard stays inert when the package is missing."""
        settings: Settings = engine._settings
        settings.enable_safetext = True
        for key in (
            "enable_badwords_py",
            "enable_profanite",
            "enable_glin_profanity",
            "enable_gangajal",
        ):
            setattr(settings, key, False)
        detector: MultiLanguageDetector = MultiLanguageDetector(settings, None)
        assert detector.detect("ein völlig harmloser satz").matched is False

    def test_guard_safetext_4_fr_917(self, engine: Any) -> None:
        """The safetext guard stays inert when the package is missing."""
        settings: Settings = engine._settings
        settings.enable_safetext = True
        for key in (
            "enable_badwords_py",
            "enable_profanite",
            "enable_glin_profanity",
            "enable_gangajal",
        ):
            setattr(settings, key, False)
        detector: MultiLanguageDetector = MultiLanguageDetector(settings, None)
        assert detector.detect("une phrase tout à fait banale").matched is False

    def test_guard_safetext_4_it_918(self, engine: Any) -> None:
        """The safetext guard stays inert when the package is missing."""
        settings: Settings = engine._settings
        settings.enable_safetext = True
        for key in (
            "enable_badwords_py",
            "enable_profanite",
            "enable_glin_profanity",
            "enable_gangajal",
        ):
            setattr(settings, key, False)
        detector: MultiLanguageDetector = MultiLanguageDetector(settings, None)
        assert detector.detect("una frase assolutamente innocua").matched is False

    def test_guard_safetext_4_hi_919(self, engine: Any) -> None:
        """The safetext guard stays inert when the package is missing."""
        settings: Settings = engine._settings
        settings.enable_safetext = True
        for key in (
            "enable_badwords_py",
            "enable_profanite",
            "enable_glin_profanity",
            "enable_gangajal",
        ):
            setattr(settings, key, False)
        detector: MultiLanguageDetector = MultiLanguageDetector(settings, None)
        assert detector.detect("यह एक साधारण वाक्य है").matched is False

    def test_guard_safetext_4_tr_920(self, engine: Any) -> None:
        """The safetext guard stays inert when the package is missing."""
        settings: Settings = engine._settings
        settings.enable_safetext = True
        for key in (
            "enable_badwords_py",
            "enable_profanite",
            "enable_glin_profanity",
            "enable_gangajal",
        ):
            setattr(settings, key, False)
        detector: MultiLanguageDetector = MultiLanguageDetector(settings, None)
        assert detector.detect("bu zararsız bir cümle").matched is False

    def test_guard_safetext_5_en_921(self, engine: Any) -> None:
        """The safetext guard stays inert when the package is missing."""
        settings: Settings = engine._settings
        settings.enable_safetext = True
        for key in (
            "enable_badwords_py",
            "enable_profanite",
            "enable_glin_profanity",
            "enable_gangajal",
        ):
            setattr(settings, key, False)
        detector: MultiLanguageDetector = MultiLanguageDetector(settings, None)
        assert detector.detect("some harmless sentence here").matched is False

    def test_guard_safetext_5_ja_922(self, engine: Any) -> None:
        """The safetext guard stays inert when the package is missing."""
        settings: Settings = engine._settings
        settings.enable_safetext = True
        for key in (
            "enable_badwords_py",
            "enable_profanite",
            "enable_glin_profanity",
            "enable_gangajal",
        ):
            setattr(settings, key, False)
        detector: MultiLanguageDetector = MultiLanguageDetector(settings, None)
        assert detector.detect("これは普通の文章です").matched is False

    def test_guard_safetext_5_ar_923(self, engine: Any) -> None:
        """The safetext guard stays inert when the package is missing."""
        settings: Settings = engine._settings
        settings.enable_safetext = True
        for key in (
            "enable_badwords_py",
            "enable_profanite",
            "enable_glin_profanity",
            "enable_gangajal",
        ):
            setattr(settings, key, False)
        detector: MultiLanguageDetector = MultiLanguageDetector(settings, None)
        assert detector.detect("هذه جملة عادية").matched is False

    def test_guard_safetext_5_ru_924(self, engine: Any) -> None:
        """The safetext guard stays inert when the package is missing."""
        settings: Settings = engine._settings
        settings.enable_safetext = True
        for key in (
            "enable_badwords_py",
            "enable_profanite",
            "enable_glin_profanity",
            "enable_gangajal",
        ):
            setattr(settings, key, False)
        detector: MultiLanguageDetector = MultiLanguageDetector(settings, None)
        assert detector.detect("обычное безобидное предложение").matched is False

    def test_guard_safetext_5_ko_925(self, engine: Any) -> None:
        """The safetext guard stays inert when the package is missing."""
        settings: Settings = engine._settings
        settings.enable_safetext = True
        for key in (
            "enable_badwords_py",
            "enable_profanite",
            "enable_glin_profanity",
            "enable_gangajal",
        ):
            setattr(settings, key, False)
        detector: MultiLanguageDetector = MultiLanguageDetector(settings, None)
        assert detector.detect("이건 평범한 문장입니다").matched is False

    def test_guard_safetext_5_de_926(self, engine: Any) -> None:
        """The safetext guard stays inert when the package is missing."""
        settings: Settings = engine._settings
        settings.enable_safetext = True
        for key in (
            "enable_badwords_py",
            "enable_profanite",
            "enable_glin_profanity",
            "enable_gangajal",
        ):
            setattr(settings, key, False)
        detector: MultiLanguageDetector = MultiLanguageDetector(settings, None)
        assert detector.detect("ein völlig harmloser satz").matched is False

    def test_guard_safetext_5_fr_927(self, engine: Any) -> None:
        """The safetext guard stays inert when the package is missing."""
        settings: Settings = engine._settings
        settings.enable_safetext = True
        for key in (
            "enable_badwords_py",
            "enable_profanite",
            "enable_glin_profanity",
            "enable_gangajal",
        ):
            setattr(settings, key, False)
        detector: MultiLanguageDetector = MultiLanguageDetector(settings, None)
        assert detector.detect("une phrase tout à fait banale").matched is False

    def test_guard_safetext_5_it_928(self, engine: Any) -> None:
        """The safetext guard stays inert when the package is missing."""
        settings: Settings = engine._settings
        settings.enable_safetext = True
        for key in (
            "enable_badwords_py",
            "enable_profanite",
            "enable_glin_profanity",
            "enable_gangajal",
        ):
            setattr(settings, key, False)
        detector: MultiLanguageDetector = MultiLanguageDetector(settings, None)
        assert detector.detect("una frase assolutamente innocua").matched is False

    def test_guard_safetext_5_hi_929(self, engine: Any) -> None:
        """The safetext guard stays inert when the package is missing."""
        settings: Settings = engine._settings
        settings.enable_safetext = True
        for key in (
            "enable_badwords_py",
            "enable_profanite",
            "enable_glin_profanity",
            "enable_gangajal",
        ):
            setattr(settings, key, False)
        detector: MultiLanguageDetector = MultiLanguageDetector(settings, None)
        assert detector.detect("यह एक साधारण वाक्य है").matched is False

    def test_guard_safetext_5_tr_930(self, engine: Any) -> None:
        """The safetext guard stays inert when the package is missing."""
        settings: Settings = engine._settings
        settings.enable_safetext = True
        for key in (
            "enable_badwords_py",
            "enable_profanite",
            "enable_glin_profanity",
            "enable_gangajal",
        ):
            setattr(settings, key, False)
        detector: MultiLanguageDetector = MultiLanguageDetector(settings, None)
        assert detector.detect("bu zararsız bir cümle").matched is False

    def test_guard_safetext_6_en_931(self, engine: Any) -> None:
        """The safetext guard stays inert when the package is missing."""
        settings: Settings = engine._settings
        settings.enable_safetext = True
        for key in (
            "enable_badwords_py",
            "enable_profanite",
            "enable_glin_profanity",
            "enable_gangajal",
        ):
            setattr(settings, key, False)
        detector: MultiLanguageDetector = MultiLanguageDetector(settings, None)
        assert detector.detect("some harmless sentence here").matched is False

    def test_guard_safetext_6_ja_932(self, engine: Any) -> None:
        """The safetext guard stays inert when the package is missing."""
        settings: Settings = engine._settings
        settings.enable_safetext = True
        for key in (
            "enable_badwords_py",
            "enable_profanite",
            "enable_glin_profanity",
            "enable_gangajal",
        ):
            setattr(settings, key, False)
        detector: MultiLanguageDetector = MultiLanguageDetector(settings, None)
        assert detector.detect("これは普通の文章です").matched is False

    def test_guard_safetext_6_ar_933(self, engine: Any) -> None:
        """The safetext guard stays inert when the package is missing."""
        settings: Settings = engine._settings
        settings.enable_safetext = True
        for key in (
            "enable_badwords_py",
            "enable_profanite",
            "enable_glin_profanity",
            "enable_gangajal",
        ):
            setattr(settings, key, False)
        detector: MultiLanguageDetector = MultiLanguageDetector(settings, None)
        assert detector.detect("هذه جملة عادية").matched is False

    def test_guard_safetext_6_ru_934(self, engine: Any) -> None:
        """The safetext guard stays inert when the package is missing."""
        settings: Settings = engine._settings
        settings.enable_safetext = True
        for key in (
            "enable_badwords_py",
            "enable_profanite",
            "enable_glin_profanity",
            "enable_gangajal",
        ):
            setattr(settings, key, False)
        detector: MultiLanguageDetector = MultiLanguageDetector(settings, None)
        assert detector.detect("обычное безобидное предложение").matched is False

    def test_guard_safetext_6_ko_935(self, engine: Any) -> None:
        """The safetext guard stays inert when the package is missing."""
        settings: Settings = engine._settings
        settings.enable_safetext = True
        for key in (
            "enable_badwords_py",
            "enable_profanite",
            "enable_glin_profanity",
            "enable_gangajal",
        ):
            setattr(settings, key, False)
        detector: MultiLanguageDetector = MultiLanguageDetector(settings, None)
        assert detector.detect("이건 평범한 문장입니다").matched is False

    def test_guard_safetext_6_de_936(self, engine: Any) -> None:
        """The safetext guard stays inert when the package is missing."""
        settings: Settings = engine._settings
        settings.enable_safetext = True
        for key in (
            "enable_badwords_py",
            "enable_profanite",
            "enable_glin_profanity",
            "enable_gangajal",
        ):
            setattr(settings, key, False)
        detector: MultiLanguageDetector = MultiLanguageDetector(settings, None)
        assert detector.detect("ein völlig harmloser satz").matched is False

    def test_guard_safetext_6_fr_937(self, engine: Any) -> None:
        """The safetext guard stays inert when the package is missing."""
        settings: Settings = engine._settings
        settings.enable_safetext = True
        for key in (
            "enable_badwords_py",
            "enable_profanite",
            "enable_glin_profanity",
            "enable_gangajal",
        ):
            setattr(settings, key, False)
        detector: MultiLanguageDetector = MultiLanguageDetector(settings, None)
        assert detector.detect("une phrase tout à fait banale").matched is False

    def test_guard_safetext_6_it_938(self, engine: Any) -> None:
        """The safetext guard stays inert when the package is missing."""
        settings: Settings = engine._settings
        settings.enable_safetext = True
        for key in (
            "enable_badwords_py",
            "enable_profanite",
            "enable_glin_profanity",
            "enable_gangajal",
        ):
            setattr(settings, key, False)
        detector: MultiLanguageDetector = MultiLanguageDetector(settings, None)
        assert detector.detect("una frase assolutamente innocua").matched is False

    def test_guard_safetext_6_hi_939(self, engine: Any) -> None:
        """The safetext guard stays inert when the package is missing."""
        settings: Settings = engine._settings
        settings.enable_safetext = True
        for key in (
            "enable_badwords_py",
            "enable_profanite",
            "enable_glin_profanity",
            "enable_gangajal",
        ):
            setattr(settings, key, False)
        detector: MultiLanguageDetector = MultiLanguageDetector(settings, None)
        assert detector.detect("यह एक साधारण वाक्य है").matched is False

    def test_guard_safetext_6_tr_940(self, engine: Any) -> None:
        """The safetext guard stays inert when the package is missing."""
        settings: Settings = engine._settings
        settings.enable_safetext = True
        for key in (
            "enable_badwords_py",
            "enable_profanite",
            "enable_glin_profanity",
            "enable_gangajal",
        ):
            setattr(settings, key, False)
        detector: MultiLanguageDetector = MultiLanguageDetector(settings, None)
        assert detector.detect("bu zararsız bir cümle").matched is False

    def test_guard_safetext_7_en_941(self, engine: Any) -> None:
        """The safetext guard stays inert when the package is missing."""
        settings: Settings = engine._settings
        settings.enable_safetext = True
        for key in (
            "enable_badwords_py",
            "enable_profanite",
            "enable_glin_profanity",
            "enable_gangajal",
        ):
            setattr(settings, key, False)
        detector: MultiLanguageDetector = MultiLanguageDetector(settings, None)
        assert detector.detect("some harmless sentence here").matched is False

    def test_guard_safetext_7_ja_942(self, engine: Any) -> None:
        """The safetext guard stays inert when the package is missing."""
        settings: Settings = engine._settings
        settings.enable_safetext = True
        for key in (
            "enable_badwords_py",
            "enable_profanite",
            "enable_glin_profanity",
            "enable_gangajal",
        ):
            setattr(settings, key, False)
        detector: MultiLanguageDetector = MultiLanguageDetector(settings, None)
        assert detector.detect("これは普通の文章です").matched is False

    def test_guard_safetext_7_ar_943(self, engine: Any) -> None:
        """The safetext guard stays inert when the package is missing."""
        settings: Settings = engine._settings
        settings.enable_safetext = True
        for key in (
            "enable_badwords_py",
            "enable_profanite",
            "enable_glin_profanity",
            "enable_gangajal",
        ):
            setattr(settings, key, False)
        detector: MultiLanguageDetector = MultiLanguageDetector(settings, None)
        assert detector.detect("هذه جملة عادية").matched is False

    def test_guard_safetext_7_ru_944(self, engine: Any) -> None:
        """The safetext guard stays inert when the package is missing."""
        settings: Settings = engine._settings
        settings.enable_safetext = True
        for key in (
            "enable_badwords_py",
            "enable_profanite",
            "enable_glin_profanity",
            "enable_gangajal",
        ):
            setattr(settings, key, False)
        detector: MultiLanguageDetector = MultiLanguageDetector(settings, None)
        assert detector.detect("обычное безобидное предложение").matched is False

    def test_guard_safetext_7_ko_945(self, engine: Any) -> None:
        """The safetext guard stays inert when the package is missing."""
        settings: Settings = engine._settings
        settings.enable_safetext = True
        for key in (
            "enable_badwords_py",
            "enable_profanite",
            "enable_glin_profanity",
            "enable_gangajal",
        ):
            setattr(settings, key, False)
        detector: MultiLanguageDetector = MultiLanguageDetector(settings, None)
        assert detector.detect("이건 평범한 문장입니다").matched is False

    def test_guard_safetext_7_de_946(self, engine: Any) -> None:
        """The safetext guard stays inert when the package is missing."""
        settings: Settings = engine._settings
        settings.enable_safetext = True
        for key in (
            "enable_badwords_py",
            "enable_profanite",
            "enable_glin_profanity",
            "enable_gangajal",
        ):
            setattr(settings, key, False)
        detector: MultiLanguageDetector = MultiLanguageDetector(settings, None)
        assert detector.detect("ein völlig harmloser satz").matched is False

    def test_guard_safetext_7_fr_947(self, engine: Any) -> None:
        """The safetext guard stays inert when the package is missing."""
        settings: Settings = engine._settings
        settings.enable_safetext = True
        for key in (
            "enable_badwords_py",
            "enable_profanite",
            "enable_glin_profanity",
            "enable_gangajal",
        ):
            setattr(settings, key, False)
        detector: MultiLanguageDetector = MultiLanguageDetector(settings, None)
        assert detector.detect("une phrase tout à fait banale").matched is False

    def test_guard_safetext_7_it_948(self, engine: Any) -> None:
        """The safetext guard stays inert when the package is missing."""
        settings: Settings = engine._settings
        settings.enable_safetext = True
        for key in (
            "enable_badwords_py",
            "enable_profanite",
            "enable_glin_profanity",
            "enable_gangajal",
        ):
            setattr(settings, key, False)
        detector: MultiLanguageDetector = MultiLanguageDetector(settings, None)
        assert detector.detect("una frase assolutamente innocua").matched is False

    def test_guard_safetext_7_hi_949(self, engine: Any) -> None:
        """The safetext guard stays inert when the package is missing."""
        settings: Settings = engine._settings
        settings.enable_safetext = True
        for key in (
            "enable_badwords_py",
            "enable_profanite",
            "enable_glin_profanity",
            "enable_gangajal",
        ):
            setattr(settings, key, False)
        detector: MultiLanguageDetector = MultiLanguageDetector(settings, None)
        assert detector.detect("यह एक साधारण वाक्य है").matched is False

    def test_guard_safetext_7_tr_950(self, engine: Any) -> None:
        """The safetext guard stays inert when the package is missing."""
        settings: Settings = engine._settings
        settings.enable_safetext = True
        for key in (
            "enable_badwords_py",
            "enable_profanite",
            "enable_glin_profanity",
            "enable_gangajal",
        ):
            setattr(settings, key, False)
        detector: MultiLanguageDetector = MultiLanguageDetector(settings, None)
        assert detector.detect("bu zararsız bir cümle").matched is False

    def test_guard_safetext_8_en_951(self, engine: Any) -> None:
        """The safetext guard stays inert when the package is missing."""
        settings: Settings = engine._settings
        settings.enable_safetext = True
        for key in (
            "enable_badwords_py",
            "enable_profanite",
            "enable_glin_profanity",
            "enable_gangajal",
        ):
            setattr(settings, key, False)
        detector: MultiLanguageDetector = MultiLanguageDetector(settings, None)
        assert detector.detect("some harmless sentence here").matched is False

    def test_guard_safetext_8_ja_952(self, engine: Any) -> None:
        """The safetext guard stays inert when the package is missing."""
        settings: Settings = engine._settings
        settings.enable_safetext = True
        for key in (
            "enable_badwords_py",
            "enable_profanite",
            "enable_glin_profanity",
            "enable_gangajal",
        ):
            setattr(settings, key, False)
        detector: MultiLanguageDetector = MultiLanguageDetector(settings, None)
        assert detector.detect("これは普通の文章です").matched is False

    def test_guard_safetext_8_ar_953(self, engine: Any) -> None:
        """The safetext guard stays inert when the package is missing."""
        settings: Settings = engine._settings
        settings.enable_safetext = True
        for key in (
            "enable_badwords_py",
            "enable_profanite",
            "enable_glin_profanity",
            "enable_gangajal",
        ):
            setattr(settings, key, False)
        detector: MultiLanguageDetector = MultiLanguageDetector(settings, None)
        assert detector.detect("هذه جملة عادية").matched is False

    def test_guard_safetext_8_ru_954(self, engine: Any) -> None:
        """The safetext guard stays inert when the package is missing."""
        settings: Settings = engine._settings
        settings.enable_safetext = True
        for key in (
            "enable_badwords_py",
            "enable_profanite",
            "enable_glin_profanity",
            "enable_gangajal",
        ):
            setattr(settings, key, False)
        detector: MultiLanguageDetector = MultiLanguageDetector(settings, None)
        assert detector.detect("обычное безобидное предложение").matched is False

    def test_guard_safetext_8_ko_955(self, engine: Any) -> None:
        """The safetext guard stays inert when the package is missing."""
        settings: Settings = engine._settings
        settings.enable_safetext = True
        for key in (
            "enable_badwords_py",
            "enable_profanite",
            "enable_glin_profanity",
            "enable_gangajal",
        ):
            setattr(settings, key, False)
        detector: MultiLanguageDetector = MultiLanguageDetector(settings, None)
        assert detector.detect("이건 평범한 문장입니다").matched is False

    def test_guard_safetext_8_de_956(self, engine: Any) -> None:
        """The safetext guard stays inert when the package is missing."""
        settings: Settings = engine._settings
        settings.enable_safetext = True
        for key in (
            "enable_badwords_py",
            "enable_profanite",
            "enable_glin_profanity",
            "enable_gangajal",
        ):
            setattr(settings, key, False)
        detector: MultiLanguageDetector = MultiLanguageDetector(settings, None)
        assert detector.detect("ein völlig harmloser satz").matched is False

    def test_guard_safetext_8_fr_957(self, engine: Any) -> None:
        """The safetext guard stays inert when the package is missing."""
        settings: Settings = engine._settings
        settings.enable_safetext = True
        for key in (
            "enable_badwords_py",
            "enable_profanite",
            "enable_glin_profanity",
            "enable_gangajal",
        ):
            setattr(settings, key, False)
        detector: MultiLanguageDetector = MultiLanguageDetector(settings, None)
        assert detector.detect("une phrase tout à fait banale").matched is False

    def test_guard_safetext_8_it_958(self, engine: Any) -> None:
        """The safetext guard stays inert when the package is missing."""
        settings: Settings = engine._settings
        settings.enable_safetext = True
        for key in (
            "enable_badwords_py",
            "enable_profanite",
            "enable_glin_profanity",
            "enable_gangajal",
        ):
            setattr(settings, key, False)
        detector: MultiLanguageDetector = MultiLanguageDetector(settings, None)
        assert detector.detect("una frase assolutamente innocua").matched is False

    def test_guard_safetext_8_hi_959(self, engine: Any) -> None:
        """The safetext guard stays inert when the package is missing."""
        settings: Settings = engine._settings
        settings.enable_safetext = True
        for key in (
            "enable_badwords_py",
            "enable_profanite",
            "enable_glin_profanity",
            "enable_gangajal",
        ):
            setattr(settings, key, False)
        detector: MultiLanguageDetector = MultiLanguageDetector(settings, None)
        assert detector.detect("यह एक साधारण वाक्य है").matched is False

    def test_guard_safetext_8_tr_960(self, engine: Any) -> None:
        """The safetext guard stays inert when the package is missing."""
        settings: Settings = engine._settings
        settings.enable_safetext = True
        for key in (
            "enable_badwords_py",
            "enable_profanite",
            "enable_glin_profanity",
            "enable_gangajal",
        ):
            setattr(settings, key, False)
        detector: MultiLanguageDetector = MultiLanguageDetector(settings, None)
        assert detector.detect("bu zararsız bir cümle").matched is False

    def test_guard_safetext_9_en_961(self, engine: Any) -> None:
        """The safetext guard stays inert when the package is missing."""
        settings: Settings = engine._settings
        settings.enable_safetext = True
        for key in (
            "enable_badwords_py",
            "enable_profanite",
            "enable_glin_profanity",
            "enable_gangajal",
        ):
            setattr(settings, key, False)
        detector: MultiLanguageDetector = MultiLanguageDetector(settings, None)
        assert detector.detect("some harmless sentence here").matched is False

    def test_guard_safetext_9_ja_962(self, engine: Any) -> None:
        """The safetext guard stays inert when the package is missing."""
        settings: Settings = engine._settings
        settings.enable_safetext = True
        for key in (
            "enable_badwords_py",
            "enable_profanite",
            "enable_glin_profanity",
            "enable_gangajal",
        ):
            setattr(settings, key, False)
        detector: MultiLanguageDetector = MultiLanguageDetector(settings, None)
        assert detector.detect("これは普通の文章です").matched is False

    def test_guard_safetext_9_ar_963(self, engine: Any) -> None:
        """The safetext guard stays inert when the package is missing."""
        settings: Settings = engine._settings
        settings.enable_safetext = True
        for key in (
            "enable_badwords_py",
            "enable_profanite",
            "enable_glin_profanity",
            "enable_gangajal",
        ):
            setattr(settings, key, False)
        detector: MultiLanguageDetector = MultiLanguageDetector(settings, None)
        assert detector.detect("هذه جملة عادية").matched is False

    def test_guard_safetext_9_ru_964(self, engine: Any) -> None:
        """The safetext guard stays inert when the package is missing."""
        settings: Settings = engine._settings
        settings.enable_safetext = True
        for key in (
            "enable_badwords_py",
            "enable_profanite",
            "enable_glin_profanity",
            "enable_gangajal",
        ):
            setattr(settings, key, False)
        detector: MultiLanguageDetector = MultiLanguageDetector(settings, None)
        assert detector.detect("обычное безобидное предложение").matched is False

    def test_guard_safetext_9_ko_965(self, engine: Any) -> None:
        """The safetext guard stays inert when the package is missing."""
        settings: Settings = engine._settings
        settings.enable_safetext = True
        for key in (
            "enable_badwords_py",
            "enable_profanite",
            "enable_glin_profanity",
            "enable_gangajal",
        ):
            setattr(settings, key, False)
        detector: MultiLanguageDetector = MultiLanguageDetector(settings, None)
        assert detector.detect("이건 평범한 문장입니다").matched is False

    def test_guard_safetext_9_de_966(self, engine: Any) -> None:
        """The safetext guard stays inert when the package is missing."""
        settings: Settings = engine._settings
        settings.enable_safetext = True
        for key in (
            "enable_badwords_py",
            "enable_profanite",
            "enable_glin_profanity",
            "enable_gangajal",
        ):
            setattr(settings, key, False)
        detector: MultiLanguageDetector = MultiLanguageDetector(settings, None)
        assert detector.detect("ein völlig harmloser satz").matched is False

    def test_guard_safetext_9_fr_967(self, engine: Any) -> None:
        """The safetext guard stays inert when the package is missing."""
        settings: Settings = engine._settings
        settings.enable_safetext = True
        for key in (
            "enable_badwords_py",
            "enable_profanite",
            "enable_glin_profanity",
            "enable_gangajal",
        ):
            setattr(settings, key, False)
        detector: MultiLanguageDetector = MultiLanguageDetector(settings, None)
        assert detector.detect("une phrase tout à fait banale").matched is False

    def test_guard_safetext_9_it_968(self, engine: Any) -> None:
        """The safetext guard stays inert when the package is missing."""
        settings: Settings = engine._settings
        settings.enable_safetext = True
        for key in (
            "enable_badwords_py",
            "enable_profanite",
            "enable_glin_profanity",
            "enable_gangajal",
        ):
            setattr(settings, key, False)
        detector: MultiLanguageDetector = MultiLanguageDetector(settings, None)
        assert detector.detect("una frase assolutamente innocua").matched is False

    def test_guard_safetext_9_hi_969(self, engine: Any) -> None:
        """The safetext guard stays inert when the package is missing."""
        settings: Settings = engine._settings
        settings.enable_safetext = True
        for key in (
            "enable_badwords_py",
            "enable_profanite",
            "enable_glin_profanity",
            "enable_gangajal",
        ):
            setattr(settings, key, False)
        detector: MultiLanguageDetector = MultiLanguageDetector(settings, None)
        assert detector.detect("यह एक साधारण वाक्य है").matched is False

    def test_guard_safetext_9_tr_970(self, engine: Any) -> None:
        """The safetext guard stays inert when the package is missing."""
        settings: Settings = engine._settings
        settings.enable_safetext = True
        for key in (
            "enable_badwords_py",
            "enable_profanite",
            "enable_glin_profanity",
            "enable_gangajal",
        ):
            setattr(settings, key, False)
        detector: MultiLanguageDetector = MultiLanguageDetector(settings, None)
        assert detector.detect("bu zararsız bir cümle").matched is False


class TestCnGuard(BaseTest):
    """CnGuard scenarios."""

    def test_cn_guard_0_971(self, engine: Any) -> None:
        """The sensitive-word-filter-cn guard stays inert when missing."""
        settings: Settings = engine._settings
        settings.enable_sensitive_word_filter_cn = True
        for key in (
            "enable_badwords_py",
            "enable_profanite",
            "enable_glin_profanity",
            "enable_gangajal",
        ):
            setattr(settings, key, False)
        detector: MultiLanguageDetector = MultiLanguageDetector(settings, None)
        assert detector.detect("一些普通的中文内容").matched is False

    def test_cn_guard_1_972(self, engine: Any) -> None:
        """The sensitive-word-filter-cn guard stays inert when missing."""
        settings: Settings = engine._settings
        settings.enable_sensitive_word_filter_cn = True
        for key in (
            "enable_badwords_py",
            "enable_profanite",
            "enable_glin_profanity",
            "enable_gangajal",
        ):
            setattr(settings, key, False)
        detector: MultiLanguageDetector = MultiLanguageDetector(settings, None)
        assert detector.detect("一些普通的中文内容").matched is False

    def test_cn_guard_2_973(self, engine: Any) -> None:
        """The sensitive-word-filter-cn guard stays inert when missing."""
        settings: Settings = engine._settings
        settings.enable_sensitive_word_filter_cn = True
        for key in (
            "enable_badwords_py",
            "enable_profanite",
            "enable_glin_profanity",
            "enable_gangajal",
        ):
            setattr(settings, key, False)
        detector: MultiLanguageDetector = MultiLanguageDetector(settings, None)
        assert detector.detect("一些普通的中文内容").matched is False

    def test_cn_guard_3_974(self, engine: Any) -> None:
        """The sensitive-word-filter-cn guard stays inert when missing."""
        settings: Settings = engine._settings
        settings.enable_sensitive_word_filter_cn = True
        for key in (
            "enable_badwords_py",
            "enable_profanite",
            "enable_glin_profanity",
            "enable_gangajal",
        ):
            setattr(settings, key, False)
        detector: MultiLanguageDetector = MultiLanguageDetector(settings, None)
        assert detector.detect("一些普通的中文内容").matched is False

    def test_cn_guard_4_975(self, engine: Any) -> None:
        """The sensitive-word-filter-cn guard stays inert when missing."""
        settings: Settings = engine._settings
        settings.enable_sensitive_word_filter_cn = True
        for key in (
            "enable_badwords_py",
            "enable_profanite",
            "enable_glin_profanity",
            "enable_gangajal",
        ):
            setattr(settings, key, False)
        detector: MultiLanguageDetector = MultiLanguageDetector(settings, None)
        assert detector.detect("一些普通的中文内容").matched is False

    def test_cn_guard_5_976(self, engine: Any) -> None:
        """The sensitive-word-filter-cn guard stays inert when missing."""
        settings: Settings = engine._settings
        settings.enable_sensitive_word_filter_cn = True
        for key in (
            "enable_badwords_py",
            "enable_profanite",
            "enable_glin_profanity",
            "enable_gangajal",
        ):
            setattr(settings, key, False)
        detector: MultiLanguageDetector = MultiLanguageDetector(settings, None)
        assert detector.detect("一些普通的中文内容").matched is False

    def test_cn_guard_6_977(self, engine: Any) -> None:
        """The sensitive-word-filter-cn guard stays inert when missing."""
        settings: Settings = engine._settings
        settings.enable_sensitive_word_filter_cn = True
        for key in (
            "enable_badwords_py",
            "enable_profanite",
            "enable_glin_profanity",
            "enable_gangajal",
        ):
            setattr(settings, key, False)
        detector: MultiLanguageDetector = MultiLanguageDetector(settings, None)
        assert detector.detect("一些普通的中文内容").matched is False

    def test_cn_guard_7_978(self, engine: Any) -> None:
        """The sensitive-word-filter-cn guard stays inert when missing."""
        settings: Settings = engine._settings
        settings.enable_sensitive_word_filter_cn = True
        for key in (
            "enable_badwords_py",
            "enable_profanite",
            "enable_glin_profanity",
            "enable_gangajal",
        ):
            setattr(settings, key, False)
        detector: MultiLanguageDetector = MultiLanguageDetector(settings, None)
        assert detector.detect("一些普通的中文内容").matched is False

    def test_cn_guard_8_979(self, engine: Any) -> None:
        """The sensitive-word-filter-cn guard stays inert when missing."""
        settings: Settings = engine._settings
        settings.enable_sensitive_word_filter_cn = True
        for key in (
            "enable_badwords_py",
            "enable_profanite",
            "enable_glin_profanity",
            "enable_gangajal",
        ):
            setattr(settings, key, False)
        detector: MultiLanguageDetector = MultiLanguageDetector(settings, None)
        assert detector.detect("一些普通的中文内容").matched is False

    def test_cn_guard_9_980(self, engine: Any) -> None:
        """The sensitive-word-filter-cn guard stays inert when missing."""
        settings: Settings = engine._settings
        settings.enable_sensitive_word_filter_cn = True
        for key in (
            "enable_badwords_py",
            "enable_profanite",
            "enable_glin_profanity",
            "enable_gangajal",
        ):
            setattr(settings, key, False)
        detector: MultiLanguageDetector = MultiLanguageDetector(settings, None)
        assert detector.detect("一些普通的中文内容").matched is False

    def test_cn_guard_10_981(self, engine: Any) -> None:
        """The sensitive-word-filter-cn guard stays inert when missing."""
        settings: Settings = engine._settings
        settings.enable_sensitive_word_filter_cn = True
        for key in (
            "enable_badwords_py",
            "enable_profanite",
            "enable_glin_profanity",
            "enable_gangajal",
        ):
            setattr(settings, key, False)
        detector: MultiLanguageDetector = MultiLanguageDetector(settings, None)
        assert detector.detect("一些普通的中文内容").matched is False

    def test_cn_guard_11_982(self, engine: Any) -> None:
        """The sensitive-word-filter-cn guard stays inert when missing."""
        settings: Settings = engine._settings
        settings.enable_sensitive_word_filter_cn = True
        for key in (
            "enable_badwords_py",
            "enable_profanite",
            "enable_glin_profanity",
            "enable_gangajal",
        ):
            setattr(settings, key, False)
        detector: MultiLanguageDetector = MultiLanguageDetector(settings, None)
        assert detector.detect("一些普通的中文内容").matched is False

    def test_cn_guard_12_983(self, engine: Any) -> None:
        """The sensitive-word-filter-cn guard stays inert when missing."""
        settings: Settings = engine._settings
        settings.enable_sensitive_word_filter_cn = True
        for key in (
            "enable_badwords_py",
            "enable_profanite",
            "enable_glin_profanity",
            "enable_gangajal",
        ):
            setattr(settings, key, False)
        detector: MultiLanguageDetector = MultiLanguageDetector(settings, None)
        assert detector.detect("一些普通的中文内容").matched is False

    def test_cn_guard_13_984(self, engine: Any) -> None:
        """The sensitive-word-filter-cn guard stays inert when missing."""
        settings: Settings = engine._settings
        settings.enable_sensitive_word_filter_cn = True
        for key in (
            "enable_badwords_py",
            "enable_profanite",
            "enable_glin_profanity",
            "enable_gangajal",
        ):
            setattr(settings, key, False)
        detector: MultiLanguageDetector = MultiLanguageDetector(settings, None)
        assert detector.detect("一些普通的中文内容").matched is False

    def test_cn_guard_14_985(self, engine: Any) -> None:
        """The sensitive-word-filter-cn guard stays inert when missing."""
        settings: Settings = engine._settings
        settings.enable_sensitive_word_filter_cn = True
        for key in (
            "enable_badwords_py",
            "enable_profanite",
            "enable_glin_profanity",
            "enable_gangajal",
        ):
            setattr(settings, key, False)
        detector: MultiLanguageDetector = MultiLanguageDetector(settings, None)
        assert detector.detect("一些普通的中文内容").matched is False

    def test_cn_guard_15_986(self, engine: Any) -> None:
        """The sensitive-word-filter-cn guard stays inert when missing."""
        settings: Settings = engine._settings
        settings.enable_sensitive_word_filter_cn = True
        for key in (
            "enable_badwords_py",
            "enable_profanite",
            "enable_glin_profanity",
            "enable_gangajal",
        ):
            setattr(settings, key, False)
        detector: MultiLanguageDetector = MultiLanguageDetector(settings, None)
        assert detector.detect("一些普通的中文内容").matched is False

    def test_cn_guard_16_987(self, engine: Any) -> None:
        """The sensitive-word-filter-cn guard stays inert when missing."""
        settings: Settings = engine._settings
        settings.enable_sensitive_word_filter_cn = True
        for key in (
            "enable_badwords_py",
            "enable_profanite",
            "enable_glin_profanity",
            "enable_gangajal",
        ):
            setattr(settings, key, False)
        detector: MultiLanguageDetector = MultiLanguageDetector(settings, None)
        assert detector.detect("一些普通的中文内容").matched is False

    def test_cn_guard_17_988(self, engine: Any) -> None:
        """The sensitive-word-filter-cn guard stays inert when missing."""
        settings: Settings = engine._settings
        settings.enable_sensitive_word_filter_cn = True
        for key in (
            "enable_badwords_py",
            "enable_profanite",
            "enable_glin_profanity",
            "enable_gangajal",
        ):
            setattr(settings, key, False)
        detector: MultiLanguageDetector = MultiLanguageDetector(settings, None)
        assert detector.detect("一些普通的中文内容").matched is False

    def test_cn_guard_18_989(self, engine: Any) -> None:
        """The sensitive-word-filter-cn guard stays inert when missing."""
        settings: Settings = engine._settings
        settings.enable_sensitive_word_filter_cn = True
        for key in (
            "enable_badwords_py",
            "enable_profanite",
            "enable_glin_profanity",
            "enable_gangajal",
        ):
            setattr(settings, key, False)
        detector: MultiLanguageDetector = MultiLanguageDetector(settings, None)
        assert detector.detect("一些普通的中文内容").matched is False

    def test_cn_guard_19_990(self, engine: Any) -> None:
        """The sensitive-word-filter-cn guard stays inert when missing."""
        settings: Settings = engine._settings
        settings.enable_sensitive_word_filter_cn = True
        for key in (
            "enable_badwords_py",
            "enable_profanite",
            "enable_glin_profanity",
            "enable_gangajal",
        ):
            setattr(settings, key, False)
        detector: MultiLanguageDetector = MultiLanguageDetector(settings, None)
        assert detector.detect("一些普通的中文内容").matched is False

    def test_cn_guard_20_991(self, engine: Any) -> None:
        """The sensitive-word-filter-cn guard stays inert when missing."""
        settings: Settings = engine._settings
        settings.enable_sensitive_word_filter_cn = True
        for key in (
            "enable_badwords_py",
            "enable_profanite",
            "enable_glin_profanity",
            "enable_gangajal",
        ):
            setattr(settings, key, False)
        detector: MultiLanguageDetector = MultiLanguageDetector(settings, None)
        assert detector.detect("一些普通的中文内容").matched is False

    def test_cn_guard_21_992(self, engine: Any) -> None:
        """The sensitive-word-filter-cn guard stays inert when missing."""
        settings: Settings = engine._settings
        settings.enable_sensitive_word_filter_cn = True
        for key in (
            "enable_badwords_py",
            "enable_profanite",
            "enable_glin_profanity",
            "enable_gangajal",
        ):
            setattr(settings, key, False)
        detector: MultiLanguageDetector = MultiLanguageDetector(settings, None)
        assert detector.detect("一些普通的中文内容").matched is False

    def test_cn_guard_22_993(self, engine: Any) -> None:
        """The sensitive-word-filter-cn guard stays inert when missing."""
        settings: Settings = engine._settings
        settings.enable_sensitive_word_filter_cn = True
        for key in (
            "enable_badwords_py",
            "enable_profanite",
            "enable_glin_profanity",
            "enable_gangajal",
        ):
            setattr(settings, key, False)
        detector: MultiLanguageDetector = MultiLanguageDetector(settings, None)
        assert detector.detect("一些普通的中文内容").matched is False

    def test_cn_guard_23_994(self, engine: Any) -> None:
        """The sensitive-word-filter-cn guard stays inert when missing."""
        settings: Settings = engine._settings
        settings.enable_sensitive_word_filter_cn = True
        for key in (
            "enable_badwords_py",
            "enable_profanite",
            "enable_glin_profanity",
            "enable_gangajal",
        ):
            setattr(settings, key, False)
        detector: MultiLanguageDetector = MultiLanguageDetector(settings, None)
        assert detector.detect("一些普通的中文内容").matched is False

    def test_cn_guard_24_995(self, engine: Any) -> None:
        """The sensitive-word-filter-cn guard stays inert when missing."""
        settings: Settings = engine._settings
        settings.enable_sensitive_word_filter_cn = True
        for key in (
            "enable_badwords_py",
            "enable_profanite",
            "enable_glin_profanity",
            "enable_gangajal",
        ):
            setattr(settings, key, False)
        detector: MultiLanguageDetector = MultiLanguageDetector(settings, None)
        assert detector.detect("一些普通的中文内容").matched is False

    def test_cn_guard_25_996(self, engine: Any) -> None:
        """The sensitive-word-filter-cn guard stays inert when missing."""
        settings: Settings = engine._settings
        settings.enable_sensitive_word_filter_cn = True
        for key in (
            "enable_badwords_py",
            "enable_profanite",
            "enable_glin_profanity",
            "enable_gangajal",
        ):
            setattr(settings, key, False)
        detector: MultiLanguageDetector = MultiLanguageDetector(settings, None)
        assert detector.detect("一些普通的中文内容").matched is False

    def test_cn_guard_26_997(self, engine: Any) -> None:
        """The sensitive-word-filter-cn guard stays inert when missing."""
        settings: Settings = engine._settings
        settings.enable_sensitive_word_filter_cn = True
        for key in (
            "enable_badwords_py",
            "enable_profanite",
            "enable_glin_profanity",
            "enable_gangajal",
        ):
            setattr(settings, key, False)
        detector: MultiLanguageDetector = MultiLanguageDetector(settings, None)
        assert detector.detect("一些普通的中文内容").matched is False

    def test_cn_guard_27_998(self, engine: Any) -> None:
        """The sensitive-word-filter-cn guard stays inert when missing."""
        settings: Settings = engine._settings
        settings.enable_sensitive_word_filter_cn = True
        for key in (
            "enable_badwords_py",
            "enable_profanite",
            "enable_glin_profanity",
            "enable_gangajal",
        ):
            setattr(settings, key, False)
        detector: MultiLanguageDetector = MultiLanguageDetector(settings, None)
        assert detector.detect("一些普通的中文内容").matched is False

    def test_cn_guard_28_999(self, engine: Any) -> None:
        """The sensitive-word-filter-cn guard stays inert when missing."""
        settings: Settings = engine._settings
        settings.enable_sensitive_word_filter_cn = True
        for key in (
            "enable_badwords_py",
            "enable_profanite",
            "enable_glin_profanity",
            "enable_gangajal",
        ):
            setattr(settings, key, False)
        detector: MultiLanguageDetector = MultiLanguageDetector(settings, None)
        assert detector.detect("一些普通的中文内容").matched is False

    def test_cn_guard_29_1000(self, engine: Any) -> None:
        """The sensitive-word-filter-cn guard stays inert when missing."""
        settings: Settings = engine._settings
        settings.enable_sensitive_word_filter_cn = True
        for key in (
            "enable_badwords_py",
            "enable_profanite",
            "enable_glin_profanity",
            "enable_gangajal",
        ):
            setattr(settings, key, False)
        detector: MultiLanguageDetector = MultiLanguageDetector(settings, None)
        assert detector.detect("一些普通的中文内容").matched is False
