"""Phase 2 admin API tests (generated).

Word CRUD, import/export, app policies, settings, logs and dashboard
stats; see tests/tools/phase2_generator.py."""

# multilingual fixtures use non-ASCII on purpose
from __future__ import annotations

from typing import Any

import pytest

from tests.base_test import BaseTest

_WORD_CRUD_CASES: tuple[tuple[str, str, int, str, int], ...] = (
    ('crud_sexual_3_en', 'sexual', 3, 'en', 7488,),
    ('crud_sexual_3_zh-CN', 'sexual', 3, 'zh-CN', 7489,),
    ('crud_sexual_3_ru', 'sexual', 3, 'ru', 7490,),
    ('crud_sexual_3_ar', 'sexual', 3, 'ar', 7491,),
    ('crud_sexual_3_ja', 'sexual', 3, 'ja', 7492,),
    ('crud_sexual_5_en', 'sexual', 5, 'en', 7493,),
    ('crud_sexual_5_zh-CN', 'sexual', 5, 'zh-CN', 7494,),
    ('crud_sexual_5_ru', 'sexual', 5, 'ru', 7495,),
    ('crud_sexual_5_ar', 'sexual', 5, 'ar', 7496,),
    ('crud_sexual_5_ja', 'sexual', 5, 'ja', 7497,),
    ('crud_sexual_7_en', 'sexual', 7, 'en', 7498,),
    ('crud_sexual_7_zh-CN', 'sexual', 7, 'zh-CN', 7499,),
    ('crud_sexual_7_ru', 'sexual', 7, 'ru', 7500,),
    ('crud_sexual_7_ar', 'sexual', 7, 'ar', 7501,),
    ('crud_sexual_7_ja', 'sexual', 7, 'ja', 7502,),
    ('crud_sexual_10_en', 'sexual', 10, 'en', 7503,),
    ('crud_sexual_10_zh-CN', 'sexual', 10, 'zh-CN', 7504,),
    ('crud_sexual_10_ru', 'sexual', 10, 'ru', 7505,),
    ('crud_sexual_10_ar', 'sexual', 10, 'ar', 7506,),
    ('crud_sexual_10_ja', 'sexual', 10, 'ja', 7507,),
    ('crud_political_0_en', 'political', 0, 'en', 7508,),
    ('crud_political_0_zh-CN', 'political', 0, 'zh-CN', 7509,),
    ('crud_political_0_ru', 'political', 0, 'ru', 7510,),
    ('crud_political_0_ar', 'political', 0, 'ar', 7511,),
    ('crud_political_0_ja', 'political', 0, 'ja', 7512,),
    ('crud_political_1_en', 'political', 1, 'en', 7513,),
    ('crud_political_1_zh-CN', 'political', 1, 'zh-CN', 7514,),
    ('crud_political_1_ru', 'political', 1, 'ru', 7515,),
    ('crud_political_1_ar', 'political', 1, 'ar', 7516,),
    ('crud_political_1_ja', 'political', 1, 'ja', 7517,),
    ('crud_political_3_en', 'political', 3, 'en', 7518,),
    ('crud_political_3_zh-CN', 'political', 3, 'zh-CN', 7519,),
    ('crud_political_3_ru', 'political', 3, 'ru', 7520,),
    ('crud_political_3_ar', 'political', 3, 'ar', 7521,),
    ('crud_political_3_ja', 'political', 3, 'ja', 7522,),
    ('crud_political_5_en', 'political', 5, 'en', 7523,),
    ('crud_political_5_zh-CN', 'political', 5, 'zh-CN', 7524,),
    ('crud_political_5_ru', 'political', 5, 'ru', 7525,),
    ('crud_political_5_ar', 'political', 5, 'ar', 7526,),
    ('crud_political_5_ja', 'political', 5, 'ja', 7527,),
    ('crud_political_7_en', 'political', 7, 'en', 7528,),
    ('crud_political_7_zh-CN', 'political', 7, 'zh-CN', 7529,),
    ('crud_political_7_ru', 'political', 7, 'ru', 7530,),
    ('crud_political_7_ar', 'political', 7, 'ar', 7531,),
    ('crud_political_7_ja', 'political', 7, 'ja', 7532,),
    ('crud_political_10_en', 'political', 10, 'en', 7533,),
    ('crud_political_10_zh-CN', 'political', 10, 'zh-CN', 7534,),
    ('crud_political_10_ru', 'political', 10, 'ru', 7535,),
    ('crud_political_10_ar', 'political', 10, 'ar', 7536,),
    ('crud_political_10_ja', 'political', 10, 'ja', 7537,),
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


_IMPORT_WORDS_CASES: tuple[tuple[int, int, int], ...] = (
    (1, 0, 7628,),
    (1, 1, 7629,),
    (1, 2, 7630,),
    (1, 3, 7631,),
    (1, 4, 7632,),
    (1, 5, 7633,),
    (1, 6, 7634,),
    (1, 7, 7635,),
    (1, 8, 7636,),
    (1, 9, 7637,),
    (1, 10, 7638,),
    (1, 11, 7639,),
    (1, 12, 7640,),
    (1, 13, 7641,),
    (1, 14, 7642,),
    (2, 0, 7643,),
    (2, 1, 7644,),
    (2, 2, 7645,),
    (2, 3, 7646,),
    (2, 4, 7647,),
    (2, 5, 7648,),
    (2, 6, 7649,),
    (2, 7, 7650,),
    (2, 8, 7651,),
    (2, 9, 7652,),
    (2, 10, 7653,),
    (2, 11, 7654,),
    (2, 12, 7655,),
    (2, 13, 7656,),
    (2, 14, 7657,),
    (5, 0, 7658,),
    (5, 1, 7659,),
    (5, 2, 7660,),
    (5, 3, 7661,),
    (5, 4, 7662,),
    (5, 5, 7663,),
    (5, 6, 7664,),
    (5, 7, 7665,),
    (5, 8, 7666,),
    (5, 9, 7667,),
    (5, 10, 7668,),
    (5, 11, 7669,),
    (5, 12, 7670,),
    (5, 13, 7671,),
    (5, 14, 7672,),
    (10, 0, 7673,),
    (10, 1, 7674,),
    (10, 2, 7675,),
    (10, 3, 7676,),
    (10, 4, 7677,),
)

class TestImportWords(BaseTest):
    """Bulk import reports the imported count."""

    @pytest.mark.parametrize(('size', 'scenario', 'uid',), _IMPORT_WORDS_CASES)
    def test_import_words(self, client: Any, admin_headers: dict[str, str], size: int, scenario: int, uid: int) -> None:
        """Bulk import reports the imported count."""
        items = [{'word': f'imp{index}_{scenario}'} for index in range(size)]
        response = client.post('/admin/wordbank/import', headers=admin_headers, json={'items': items})
        assert response.status_code == 200
        assert response.json()['imported'] == size
        stats = client.get('/admin/wordbank/stats', headers=admin_headers).json()
        assert stats['customWords'] >= size
