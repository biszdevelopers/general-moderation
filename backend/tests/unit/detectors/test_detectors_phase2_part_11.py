"""Phase 2 detector tests (golden master, generated).

Computed from the locked test environment; see tests/tools/phase2_generator.py."""

# multilingual fixtures use non-ASCII on purpose
from __future__ import annotations

from typing import Any

from app.config import Settings
from app.detectors.multi_language_detector import MultiLanguageDetector
from tests.base_test import BaseTest


class TestCnGuard(BaseTest):
    """CnGuard scenarios."""

    def test_cn_guard_30_1001(self, engine: Any) -> None:
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

    def test_cn_guard_31_1002(self, engine: Any) -> None:
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

    def test_cn_guard_32_1003(self, engine: Any) -> None:
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

    def test_cn_guard_33_1004(self, engine: Any) -> None:
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

    def test_cn_guard_34_1005(self, engine: Any) -> None:
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

    def test_cn_guard_35_1006(self, engine: Any) -> None:
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

    def test_cn_guard_36_1007(self, engine: Any) -> None:
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

    def test_cn_guard_37_1008(self, engine: Any) -> None:
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

    def test_cn_guard_38_1009(self, engine: Any) -> None:
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

    def test_cn_guard_39_1010(self, engine: Any) -> None:
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

    def test_cn_guard_40_1011(self, engine: Any) -> None:
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

    def test_cn_guard_41_1012(self, engine: Any) -> None:
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

    def test_cn_guard_42_1013(self, engine: Any) -> None:
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

    def test_cn_guard_43_1014(self, engine: Any) -> None:
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

    def test_cn_guard_44_1015(self, engine: Any) -> None:
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

    def test_cn_guard_45_1016(self, engine: Any) -> None:
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

    def test_cn_guard_46_1017(self, engine: Any) -> None:
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

    def test_cn_guard_47_1018(self, engine: Any) -> None:
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

    def test_cn_guard_48_1019(self, engine: Any) -> None:
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

    def test_cn_guard_49_1020(self, engine: Any) -> None:
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

    def test_cn_guard_50_1021(self, engine: Any) -> None:
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

    def test_cn_guard_51_1022(self, engine: Any) -> None:
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

    def test_cn_guard_52_1023(self, engine: Any) -> None:
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

    def test_cn_guard_53_1024(self, engine: Any) -> None:
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

    def test_cn_guard_54_1025(self, engine: Any) -> None:
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

    def test_cn_guard_55_1026(self, engine: Any) -> None:
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

    def test_cn_guard_56_1027(self, engine: Any) -> None:
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

    def test_cn_guard_57_1028(self, engine: Any) -> None:
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

    def test_cn_guard_58_1029(self, engine: Any) -> None:
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

    def test_cn_guard_59_1030(self, engine: Any) -> None:
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

    def test_cn_guard_60_1031(self, engine: Any) -> None:
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

    def test_cn_guard_61_1032(self, engine: Any) -> None:
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

    def test_cn_guard_62_1033(self, engine: Any) -> None:
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

    def test_cn_guard_63_1034(self, engine: Any) -> None:
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

    def test_cn_guard_64_1035(self, engine: Any) -> None:
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

    def test_cn_guard_65_1036(self, engine: Any) -> None:
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

    def test_cn_guard_66_1037(self, engine: Any) -> None:
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

    def test_cn_guard_67_1038(self, engine: Any) -> None:
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

    def test_cn_guard_68_1039(self, engine: Any) -> None:
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

    def test_cn_guard_69_1040(self, engine: Any) -> None:
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

    def test_cn_guard_70_1041(self, engine: Any) -> None:
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

    def test_cn_guard_71_1042(self, engine: Any) -> None:
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

    def test_cn_guard_72_1043(self, engine: Any) -> None:
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

    def test_cn_guard_73_1044(self, engine: Any) -> None:
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

    def test_cn_guard_74_1045(self, engine: Any) -> None:
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

    def test_cn_guard_75_1046(self, engine: Any) -> None:
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

    def test_cn_guard_76_1047(self, engine: Any) -> None:
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

    def test_cn_guard_77_1048(self, engine: Any) -> None:
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

    def test_cn_guard_78_1049(self, engine: Any) -> None:
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

    def test_cn_guard_79_1050(self, engine: Any) -> None:
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


class TestPf2Guard(BaseTest):
    """Pf2Guard scenarios."""

    def test_pf2_guard_0_1051(self, engine: Any) -> None:
        """The profanity-filter2 guard stays inert when missing."""
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
        assert detector.detect("plain english sentence").matched is False

    def test_pf2_guard_1_1052(self, engine: Any) -> None:
        """The profanity-filter2 guard stays inert when missing."""
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
        assert detector.detect("plain english sentence").matched is False

    def test_pf2_guard_2_1053(self, engine: Any) -> None:
        """The profanity-filter2 guard stays inert when missing."""
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
        assert detector.detect("plain english sentence").matched is False

    def test_pf2_guard_3_1054(self, engine: Any) -> None:
        """The profanity-filter2 guard stays inert when missing."""
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
        assert detector.detect("plain english sentence").matched is False

    def test_pf2_guard_4_1055(self, engine: Any) -> None:
        """The profanity-filter2 guard stays inert when missing."""
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
        assert detector.detect("plain english sentence").matched is False

    def test_pf2_guard_5_1056(self, engine: Any) -> None:
        """The profanity-filter2 guard stays inert when missing."""
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
        assert detector.detect("plain english sentence").matched is False

    def test_pf2_guard_6_1057(self, engine: Any) -> None:
        """The profanity-filter2 guard stays inert when missing."""
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
        assert detector.detect("plain english sentence").matched is False

    def test_pf2_guard_7_1058(self, engine: Any) -> None:
        """The profanity-filter2 guard stays inert when missing."""
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
        assert detector.detect("plain english sentence").matched is False

    def test_pf2_guard_8_1059(self, engine: Any) -> None:
        """The profanity-filter2 guard stays inert when missing."""
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
        assert detector.detect("plain english sentence").matched is False

    def test_pf2_guard_9_1060(self, engine: Any) -> None:
        """The profanity-filter2 guard stays inert when missing."""
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
        assert detector.detect("plain english sentence").matched is False

    def test_pf2_guard_10_1061(self, engine: Any) -> None:
        """The profanity-filter2 guard stays inert when missing."""
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
        assert detector.detect("plain english sentence").matched is False

    def test_pf2_guard_11_1062(self, engine: Any) -> None:
        """The profanity-filter2 guard stays inert when missing."""
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
        assert detector.detect("plain english sentence").matched is False

    def test_pf2_guard_12_1063(self, engine: Any) -> None:
        """The profanity-filter2 guard stays inert when missing."""
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
        assert detector.detect("plain english sentence").matched is False

    def test_pf2_guard_13_1064(self, engine: Any) -> None:
        """The profanity-filter2 guard stays inert when missing."""
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
        assert detector.detect("plain english sentence").matched is False

    def test_pf2_guard_14_1065(self, engine: Any) -> None:
        """The profanity-filter2 guard stays inert when missing."""
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
        assert detector.detect("plain english sentence").matched is False

    def test_pf2_guard_15_1066(self, engine: Any) -> None:
        """The profanity-filter2 guard stays inert when missing."""
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
        assert detector.detect("plain english sentence").matched is False

    def test_pf2_guard_16_1067(self, engine: Any) -> None:
        """The profanity-filter2 guard stays inert when missing."""
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
        assert detector.detect("plain english sentence").matched is False

    def test_pf2_guard_17_1068(self, engine: Any) -> None:
        """The profanity-filter2 guard stays inert when missing."""
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
        assert detector.detect("plain english sentence").matched is False

    def test_pf2_guard_18_1069(self, engine: Any) -> None:
        """The profanity-filter2 guard stays inert when missing."""
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
        assert detector.detect("plain english sentence").matched is False

    def test_pf2_guard_19_1070(self, engine: Any) -> None:
        """The profanity-filter2 guard stays inert when missing."""
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
        assert detector.detect("plain english sentence").matched is False

    def test_pf2_guard_20_1071(self, engine: Any) -> None:
        """The profanity-filter2 guard stays inert when missing."""
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
        assert detector.detect("plain english sentence").matched is False

    def test_pf2_guard_21_1072(self, engine: Any) -> None:
        """The profanity-filter2 guard stays inert when missing."""
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
        assert detector.detect("plain english sentence").matched is False

    def test_pf2_guard_22_1073(self, engine: Any) -> None:
        """The profanity-filter2 guard stays inert when missing."""
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
        assert detector.detect("plain english sentence").matched is False

    def test_pf2_guard_23_1074(self, engine: Any) -> None:
        """The profanity-filter2 guard stays inert when missing."""
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
        assert detector.detect("plain english sentence").matched is False

    def test_pf2_guard_24_1075(self, engine: Any) -> None:
        """The profanity-filter2 guard stays inert when missing."""
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
        assert detector.detect("plain english sentence").matched is False

    def test_pf2_guard_25_1076(self, engine: Any) -> None:
        """The profanity-filter2 guard stays inert when missing."""
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
        assert detector.detect("plain english sentence").matched is False

    def test_pf2_guard_26_1077(self, engine: Any) -> None:
        """The profanity-filter2 guard stays inert when missing."""
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
        assert detector.detect("plain english sentence").matched is False

    def test_pf2_guard_27_1078(self, engine: Any) -> None:
        """The profanity-filter2 guard stays inert when missing."""
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
        assert detector.detect("plain english sentence").matched is False

    def test_pf2_guard_28_1079(self, engine: Any) -> None:
        """The profanity-filter2 guard stays inert when missing."""
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
        assert detector.detect("plain english sentence").matched is False

    def test_pf2_guard_29_1080(self, engine: Any) -> None:
        """The profanity-filter2 guard stays inert when missing."""
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
        assert detector.detect("plain english sentence").matched is False

    def test_pf2_guard_30_1081(self, engine: Any) -> None:
        """The profanity-filter2 guard stays inert when missing."""
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
        assert detector.detect("plain english sentence").matched is False

    def test_pf2_guard_31_1082(self, engine: Any) -> None:
        """The profanity-filter2 guard stays inert when missing."""
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
        assert detector.detect("plain english sentence").matched is False

    def test_pf2_guard_32_1083(self, engine: Any) -> None:
        """The profanity-filter2 guard stays inert when missing."""
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
        assert detector.detect("plain english sentence").matched is False

    def test_pf2_guard_33_1084(self, engine: Any) -> None:
        """The profanity-filter2 guard stays inert when missing."""
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
        assert detector.detect("plain english sentence").matched is False

    def test_pf2_guard_34_1085(self, engine: Any) -> None:
        """The profanity-filter2 guard stays inert when missing."""
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
        assert detector.detect("plain english sentence").matched is False

    def test_pf2_guard_35_1086(self, engine: Any) -> None:
        """The profanity-filter2 guard stays inert when missing."""
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
        assert detector.detect("plain english sentence").matched is False

    def test_pf2_guard_36_1087(self, engine: Any) -> None:
        """The profanity-filter2 guard stays inert when missing."""
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
        assert detector.detect("plain english sentence").matched is False

    def test_pf2_guard_37_1088(self, engine: Any) -> None:
        """The profanity-filter2 guard stays inert when missing."""
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
        assert detector.detect("plain english sentence").matched is False

    def test_pf2_guard_38_1089(self, engine: Any) -> None:
        """The profanity-filter2 guard stays inert when missing."""
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
        assert detector.detect("plain english sentence").matched is False

    def test_pf2_guard_39_1090(self, engine: Any) -> None:
        """The profanity-filter2 guard stays inert when missing."""
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
        assert detector.detect("plain english sentence").matched is False

    def test_pf2_guard_40_1091(self, engine: Any) -> None:
        """The profanity-filter2 guard stays inert when missing."""
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
        assert detector.detect("plain english sentence").matched is False

    def test_pf2_guard_41_1092(self, engine: Any) -> None:
        """The profanity-filter2 guard stays inert when missing."""
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
        assert detector.detect("plain english sentence").matched is False

    def test_pf2_guard_42_1093(self, engine: Any) -> None:
        """The profanity-filter2 guard stays inert when missing."""
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
        assert detector.detect("plain english sentence").matched is False

    def test_pf2_guard_43_1094(self, engine: Any) -> None:
        """The profanity-filter2 guard stays inert when missing."""
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
        assert detector.detect("plain english sentence").matched is False

    def test_pf2_guard_44_1095(self, engine: Any) -> None:
        """The profanity-filter2 guard stays inert when missing."""
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
        assert detector.detect("plain english sentence").matched is False

    def test_pf2_guard_45_1096(self, engine: Any) -> None:
        """The profanity-filter2 guard stays inert when missing."""
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
        assert detector.detect("plain english sentence").matched is False

    def test_pf2_guard_46_1097(self, engine: Any) -> None:
        """The profanity-filter2 guard stays inert when missing."""
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
        assert detector.detect("plain english sentence").matched is False

    def test_pf2_guard_47_1098(self, engine: Any) -> None:
        """The profanity-filter2 guard stays inert when missing."""
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
        assert detector.detect("plain english sentence").matched is False

    def test_pf2_guard_48_1099(self, engine: Any) -> None:
        """The profanity-filter2 guard stays inert when missing."""
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
        assert detector.detect("plain english sentence").matched is False

    def test_pf2_guard_49_1100(self, engine: Any) -> None:
        """The profanity-filter2 guard stays inert when missing."""
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
        assert detector.detect("plain english sentence").matched is False
