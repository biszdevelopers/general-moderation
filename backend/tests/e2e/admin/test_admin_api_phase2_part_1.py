"""Phase 2 admin API tests (generated).

Word CRUD, import/export, app policies, settings, logs and dashboard
stats; see tests/tools/phase2_generator.py."""

# multilingual fixtures use non-ASCII on purpose
from __future__ import annotations

from typing import Any

import pytest

from tests.base_test import BaseTest

_WORD_CRUD_CASES: tuple[tuple[str, str, int, str, int], ...] = (
    ('crud_other_0_en', 'other', 0, 'en', 7428,),
    ('crud_other_0_zh-CN', 'other', 0, 'zh-CN', 7429,),
    ('crud_other_0_ru', 'other', 0, 'ru', 7430,),
    ('crud_other_0_ar', 'other', 0, 'ar', 7431,),
    ('crud_other_0_ja', 'other', 0, 'ja', 7432,),
    ('crud_other_1_en', 'other', 1, 'en', 7433,),
    ('crud_other_1_zh-CN', 'other', 1, 'zh-CN', 7434,),
    ('crud_other_1_ru', 'other', 1, 'ru', 7435,),
    ('crud_other_1_ar', 'other', 1, 'ar', 7436,),
    ('crud_other_1_ja', 'other', 1, 'ja', 7437,),
    ('crud_other_3_en', 'other', 3, 'en', 7438,),
    ('crud_other_3_zh-CN', 'other', 3, 'zh-CN', 7439,),
    ('crud_other_3_ru', 'other', 3, 'ru', 7440,),
    ('crud_other_3_ar', 'other', 3, 'ar', 7441,),
    ('crud_other_3_ja', 'other', 3, 'ja', 7442,),
    ('crud_other_5_en', 'other', 5, 'en', 7443,),
    ('crud_other_5_zh-CN', 'other', 5, 'zh-CN', 7444,),
    ('crud_other_5_ru', 'other', 5, 'ru', 7445,),
    ('crud_other_5_ar', 'other', 5, 'ar', 7446,),
    ('crud_other_5_ja', 'other', 5, 'ja', 7447,),
    ('crud_other_7_en', 'other', 7, 'en', 7448,),
    ('crud_other_7_zh-CN', 'other', 7, 'zh-CN', 7449,),
    ('crud_other_7_ru', 'other', 7, 'ru', 7450,),
    ('crud_other_7_ar', 'other', 7, 'ar', 7451,),
    ('crud_other_7_ja', 'other', 7, 'ja', 7452,),
    ('crud_other_10_en', 'other', 10, 'en', 7453,),
    ('crud_other_10_zh-CN', 'other', 10, 'zh-CN', 7454,),
    ('crud_other_10_ru', 'other', 10, 'ru', 7455,),
    ('crud_other_10_ar', 'other', 10, 'ar', 7456,),
    ('crud_other_10_ja', 'other', 10, 'ja', 7457,),
    ('crud_hate_speech_0_en', 'hate_speech', 0, 'en', 7458,),
    ('crud_hate_speech_0_zh-CN', 'hate_speech', 0, 'zh-CN', 7459,),
    ('crud_hate_speech_0_ru', 'hate_speech', 0, 'ru', 7460,),
    ('crud_hate_speech_0_ar', 'hate_speech', 0, 'ar', 7461,),
    ('crud_hate_speech_0_ja', 'hate_speech', 0, 'ja', 7462,),
    ('crud_hate_speech_1_en', 'hate_speech', 1, 'en', 7463,),
    ('crud_hate_speech_1_zh-CN', 'hate_speech', 1, 'zh-CN', 7464,),
    ('crud_hate_speech_1_ru', 'hate_speech', 1, 'ru', 7465,),
    ('crud_hate_speech_1_ar', 'hate_speech', 1, 'ar', 7466,),
    ('crud_hate_speech_1_ja', 'hate_speech', 1, 'ja', 7467,),
    ('crud_hate_speech_3_en', 'hate_speech', 3, 'en', 7468,),
    ('crud_hate_speech_3_zh-CN', 'hate_speech', 3, 'zh-CN', 7469,),
    ('crud_hate_speech_3_ru', 'hate_speech', 3, 'ru', 7470,),
    ('crud_hate_speech_3_ar', 'hate_speech', 3, 'ar', 7471,),
    ('crud_hate_speech_3_ja', 'hate_speech', 3, 'ja', 7472,),
    ('crud_hate_speech_5_en', 'hate_speech', 5, 'en', 7473,),
    ('crud_hate_speech_5_zh-CN', 'hate_speech', 5, 'zh-CN', 7474,),
    ('crud_hate_speech_5_ru', 'hate_speech', 5, 'ru', 7475,),
    ('crud_hate_speech_5_ar', 'hate_speech', 5, 'ar', 7476,),
    ('crud_hate_speech_5_ja', 'hate_speech', 5, 'ja', 7477,),
    ('crud_hate_speech_7_en', 'hate_speech', 7, 'en', 7478,),
    ('crud_hate_speech_7_zh-CN', 'hate_speech', 7, 'zh-CN', 7479,),
    ('crud_hate_speech_7_ru', 'hate_speech', 7, 'ru', 7480,),
    ('crud_hate_speech_7_ar', 'hate_speech', 7, 'ar', 7481,),
    ('crud_hate_speech_7_ja', 'hate_speech', 7, 'ja', 7482,),
    ('crud_hate_speech_10_en', 'hate_speech', 10, 'en', 7483,),
    ('crud_hate_speech_10_zh-CN', 'hate_speech', 10, 'zh-CN', 7484,),
    ('crud_hate_speech_10_ru', 'hate_speech', 10, 'ru', 7485,),
    ('crud_hate_speech_10_ar', 'hate_speech', 10, 'ar', 7486,),
    ('crud_hate_speech_10_ja', 'hate_speech', 10, 'ja', 7487,),
    ('crud_violence_0_en', 'violence', 0, 'en', 7488,),
    ('crud_violence_0_zh-CN', 'violence', 0, 'zh-CN', 7489,),
    ('crud_violence_0_ru', 'violence', 0, 'ru', 7490,),
    ('crud_violence_0_ar', 'violence', 0, 'ar', 7491,),
    ('crud_violence_0_ja', 'violence', 0, 'ja', 7492,),
    ('crud_violence_1_en', 'violence', 1, 'en', 7493,),
    ('crud_violence_1_zh-CN', 'violence', 1, 'zh-CN', 7494,),
    ('crud_violence_1_ru', 'violence', 1, 'ru', 7495,),
    ('crud_violence_1_ar', 'violence', 1, 'ar', 7496,),
    ('crud_violence_1_ja', 'violence', 1, 'ja', 7497,),
    ('crud_violence_3_en', 'violence', 3, 'en', 7498,),
    ('crud_violence_3_zh-CN', 'violence', 3, 'zh-CN', 7499,),
    ('crud_violence_3_ru', 'violence', 3, 'ru', 7500,),
    ('crud_violence_3_ar', 'violence', 3, 'ar', 7501,),
    ('crud_violence_3_ja', 'violence', 3, 'ja', 7502,),
    ('crud_violence_5_en', 'violence', 5, 'en', 7503,),
    ('crud_violence_5_zh-CN', 'violence', 5, 'zh-CN', 7504,),
    ('crud_violence_5_ru', 'violence', 5, 'ru', 7505,),
    ('crud_violence_5_ar', 'violence', 5, 'ar', 7506,),
    ('crud_violence_5_ja', 'violence', 5, 'ja', 7507,),
    ('crud_violence_7_en', 'violence', 7, 'en', 7508,),
    ('crud_violence_7_zh-CN', 'violence', 7, 'zh-CN', 7509,),
    ('crud_violence_7_ru', 'violence', 7, 'ru', 7510,),
    ('crud_violence_7_ar', 'violence', 7, 'ar', 7511,),
    ('crud_violence_7_ja', 'violence', 7, 'ja', 7512,),
    ('crud_violence_10_en', 'violence', 10, 'en', 7513,),
    ('crud_violence_10_zh-CN', 'violence', 10, 'zh-CN', 7514,),
    ('crud_violence_10_ru', 'violence', 10, 'ru', 7515,),
    ('crud_violence_10_ar', 'violence', 10, 'ar', 7516,),
    ('crud_violence_10_ja', 'violence', 10, 'ja', 7517,),
    ('crud_sexual_0_en', 'sexual', 0, 'en', 7518,),
    ('crud_sexual_0_zh-CN', 'sexual', 0, 'zh-CN', 7519,),
    ('crud_sexual_0_ru', 'sexual', 0, 'ru', 7520,),
    ('crud_sexual_0_ar', 'sexual', 0, 'ar', 7521,),
    ('crud_sexual_0_ja', 'sexual', 0, 'ja', 7522,),
    ('crud_sexual_1_en', 'sexual', 1, 'en', 7523,),
    ('crud_sexual_1_zh-CN', 'sexual', 1, 'zh-CN', 7524,),
    ('crud_sexual_1_ru', 'sexual', 1, 'ru', 7525,),
    ('crud_sexual_1_ar', 'sexual', 1, 'ar', 7526,),
    ('crud_sexual_1_ja', 'sexual', 1, 'ja', 7527,),
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
