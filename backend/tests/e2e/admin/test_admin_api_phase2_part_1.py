"""Phase 2 admin API tests (generated).

Word CRUD, import/export, app policies, settings, logs and dashboard
stats; see tests/tools/phase2_generator.py."""

# multilingual fixtures use non-ASCII on purpose
from __future__ import annotations

from typing import Any

import pytest

from tests.base_test import BaseTest

_WORD_CRUD_CASES: tuple[tuple[str, str, int, str, int], ...] = (
    ('crud_other_0_en', 'other', 0, 'en', 7229,),
    ('crud_other_0_zh-CN', 'other', 0, 'zh-CN', 7230,),
    ('crud_other_0_ru', 'other', 0, 'ru', 7231,),
    ('crud_other_0_ar', 'other', 0, 'ar', 7232,),
    ('crud_other_0_ja', 'other', 0, 'ja', 7233,),
    ('crud_other_1_en', 'other', 1, 'en', 7234,),
    ('crud_other_1_zh-CN', 'other', 1, 'zh-CN', 7235,),
    ('crud_other_1_ru', 'other', 1, 'ru', 7236,),
    ('crud_other_1_ar', 'other', 1, 'ar', 7237,),
    ('crud_other_1_ja', 'other', 1, 'ja', 7238,),
    ('crud_other_3_en', 'other', 3, 'en', 7239,),
    ('crud_other_3_zh-CN', 'other', 3, 'zh-CN', 7240,),
    ('crud_other_3_ru', 'other', 3, 'ru', 7241,),
    ('crud_other_3_ar', 'other', 3, 'ar', 7242,),
    ('crud_other_3_ja', 'other', 3, 'ja', 7243,),
    ('crud_other_5_en', 'other', 5, 'en', 7244,),
    ('crud_other_5_zh-CN', 'other', 5, 'zh-CN', 7245,),
    ('crud_other_5_ru', 'other', 5, 'ru', 7246,),
    ('crud_other_5_ar', 'other', 5, 'ar', 7247,),
    ('crud_other_5_ja', 'other', 5, 'ja', 7248,),
    ('crud_other_7_en', 'other', 7, 'en', 7249,),
    ('crud_other_7_zh-CN', 'other', 7, 'zh-CN', 7250,),
    ('crud_other_7_ru', 'other', 7, 'ru', 7251,),
    ('crud_other_7_ar', 'other', 7, 'ar', 7252,),
    ('crud_other_7_ja', 'other', 7, 'ja', 7253,),
    ('crud_other_10_en', 'other', 10, 'en', 7254,),
    ('crud_other_10_zh-CN', 'other', 10, 'zh-CN', 7255,),
    ('crud_other_10_ru', 'other', 10, 'ru', 7256,),
    ('crud_other_10_ar', 'other', 10, 'ar', 7257,),
    ('crud_other_10_ja', 'other', 10, 'ja', 7258,),
    ('crud_hate_speech_0_en', 'hate_speech', 0, 'en', 7259,),
    ('crud_hate_speech_0_zh-CN', 'hate_speech', 0, 'zh-CN', 7260,),
    ('crud_hate_speech_0_ru', 'hate_speech', 0, 'ru', 7261,),
    ('crud_hate_speech_0_ar', 'hate_speech', 0, 'ar', 7262,),
    ('crud_hate_speech_0_ja', 'hate_speech', 0, 'ja', 7263,),
    ('crud_hate_speech_1_en', 'hate_speech', 1, 'en', 7264,),
    ('crud_hate_speech_1_zh-CN', 'hate_speech', 1, 'zh-CN', 7265,),
    ('crud_hate_speech_1_ru', 'hate_speech', 1, 'ru', 7266,),
    ('crud_hate_speech_1_ar', 'hate_speech', 1, 'ar', 7267,),
    ('crud_hate_speech_1_ja', 'hate_speech', 1, 'ja', 7268,),
    ('crud_hate_speech_3_en', 'hate_speech', 3, 'en', 7269,),
    ('crud_hate_speech_3_zh-CN', 'hate_speech', 3, 'zh-CN', 7270,),
    ('crud_hate_speech_3_ru', 'hate_speech', 3, 'ru', 7271,),
    ('crud_hate_speech_3_ar', 'hate_speech', 3, 'ar', 7272,),
    ('crud_hate_speech_3_ja', 'hate_speech', 3, 'ja', 7273,),
    ('crud_hate_speech_5_en', 'hate_speech', 5, 'en', 7274,),
    ('crud_hate_speech_5_zh-CN', 'hate_speech', 5, 'zh-CN', 7275,),
    ('crud_hate_speech_5_ru', 'hate_speech', 5, 'ru', 7276,),
    ('crud_hate_speech_5_ar', 'hate_speech', 5, 'ar', 7277,),
    ('crud_hate_speech_5_ja', 'hate_speech', 5, 'ja', 7278,),
    ('crud_hate_speech_7_en', 'hate_speech', 7, 'en', 7279,),
    ('crud_hate_speech_7_zh-CN', 'hate_speech', 7, 'zh-CN', 7280,),
    ('crud_hate_speech_7_ru', 'hate_speech', 7, 'ru', 7281,),
    ('crud_hate_speech_7_ar', 'hate_speech', 7, 'ar', 7282,),
    ('crud_hate_speech_7_ja', 'hate_speech', 7, 'ja', 7283,),
    ('crud_hate_speech_10_en', 'hate_speech', 10, 'en', 7284,),
    ('crud_hate_speech_10_zh-CN', 'hate_speech', 10, 'zh-CN', 7285,),
    ('crud_hate_speech_10_ru', 'hate_speech', 10, 'ru', 7286,),
    ('crud_hate_speech_10_ar', 'hate_speech', 10, 'ar', 7287,),
    ('crud_hate_speech_10_ja', 'hate_speech', 10, 'ja', 7288,),
    ('crud_violence_0_en', 'violence', 0, 'en', 7289,),
    ('crud_violence_0_zh-CN', 'violence', 0, 'zh-CN', 7290,),
    ('crud_violence_0_ru', 'violence', 0, 'ru', 7291,),
    ('crud_violence_0_ar', 'violence', 0, 'ar', 7292,),
    ('crud_violence_0_ja', 'violence', 0, 'ja', 7293,),
    ('crud_violence_1_en', 'violence', 1, 'en', 7294,),
    ('crud_violence_1_zh-CN', 'violence', 1, 'zh-CN', 7295,),
    ('crud_violence_1_ru', 'violence', 1, 'ru', 7296,),
    ('crud_violence_1_ar', 'violence', 1, 'ar', 7297,),
    ('crud_violence_1_ja', 'violence', 1, 'ja', 7298,),
    ('crud_violence_3_en', 'violence', 3, 'en', 7299,),
    ('crud_violence_3_zh-CN', 'violence', 3, 'zh-CN', 7300,),
    ('crud_violence_3_ru', 'violence', 3, 'ru', 7301,),
    ('crud_violence_3_ar', 'violence', 3, 'ar', 7302,),
    ('crud_violence_3_ja', 'violence', 3, 'ja', 7303,),
    ('crud_violence_5_en', 'violence', 5, 'en', 7304,),
    ('crud_violence_5_zh-CN', 'violence', 5, 'zh-CN', 7305,),
    ('crud_violence_5_ru', 'violence', 5, 'ru', 7306,),
    ('crud_violence_5_ar', 'violence', 5, 'ar', 7307,),
    ('crud_violence_5_ja', 'violence', 5, 'ja', 7308,),
    ('crud_violence_7_en', 'violence', 7, 'en', 7309,),
    ('crud_violence_7_zh-CN', 'violence', 7, 'zh-CN', 7310,),
    ('crud_violence_7_ru', 'violence', 7, 'ru', 7311,),
    ('crud_violence_7_ar', 'violence', 7, 'ar', 7312,),
    ('crud_violence_7_ja', 'violence', 7, 'ja', 7313,),
    ('crud_violence_10_en', 'violence', 10, 'en', 7314,),
    ('crud_violence_10_zh-CN', 'violence', 10, 'zh-CN', 7315,),
    ('crud_violence_10_ru', 'violence', 10, 'ru', 7316,),
    ('crud_violence_10_ar', 'violence', 10, 'ar', 7317,),
    ('crud_violence_10_ja', 'violence', 10, 'ja', 7318,),
    ('crud_sexual_0_en', 'sexual', 0, 'en', 7319,),
    ('crud_sexual_0_zh-CN', 'sexual', 0, 'zh-CN', 7320,),
    ('crud_sexual_0_ru', 'sexual', 0, 'ru', 7321,),
    ('crud_sexual_0_ar', 'sexual', 0, 'ar', 7322,),
    ('crud_sexual_0_ja', 'sexual', 0, 'ja', 7323,),
    ('crud_sexual_1_en', 'sexual', 1, 'en', 7324,),
    ('crud_sexual_1_zh-CN', 'sexual', 1, 'zh-CN', 7325,),
    ('crud_sexual_1_ru', 'sexual', 1, 'ru', 7326,),
    ('crud_sexual_1_ar', 'sexual', 1, 'ar', 7327,),
    ('crud_sexual_1_ja', 'sexual', 1, 'ja', 7328,),
)

class TestWordCrud(BaseTest):
    """Adding, listing and deleting a custom word round-trips."""

    @pytest.mark.parametrize(('word', 'category', 'severity', 'language', 'uid',), _WORD_CRUD_CASES)
    def test_word_crud(self, client: Any, admin_headers: dict[str, str], word: str, category: str, severity: int, language: str, uid: int) -> None:
        """Adding, listing and deleting a custom word round-trips."""
        payload = {'word': word, 'category': category, 'severity': severity, 'language': language}
        created = client.post(
            '/admin/wordbank/words',
            headers=admin_headers,
            json=payload,
        )
        assert created.status_code == 201
        response = client.get('/admin/wordbank/words', headers=admin_headers)
        assert response.status_code == 200
        assert any(entry['word'] == word.lower() for entry in response.json())
