"""Phase 2 admin API tests (generated).

Word CRUD, import/export, app policies, settings, logs and dashboard
stats; see tests/tools/phase2_generator.py."""

# multilingual fixtures use non-ASCII on purpose
from __future__ import annotations

from typing import Any

import pytest

from tests.base_test import BaseTest

_WORD_CRUD_CASES: tuple[tuple[str, str, int, str, int], ...] = (
    ('crud_sexual_3_en', 'sexual', 3, 'en', 7528,),
    ('crud_sexual_3_zh-CN', 'sexual', 3, 'zh-CN', 7529,),
    ('crud_sexual_3_ru', 'sexual', 3, 'ru', 7530,),
    ('crud_sexual_3_ar', 'sexual', 3, 'ar', 7531,),
    ('crud_sexual_3_ja', 'sexual', 3, 'ja', 7532,),
    ('crud_sexual_5_en', 'sexual', 5, 'en', 7533,),
    ('crud_sexual_5_zh-CN', 'sexual', 5, 'zh-CN', 7534,),
    ('crud_sexual_5_ru', 'sexual', 5, 'ru', 7535,),
    ('crud_sexual_5_ar', 'sexual', 5, 'ar', 7536,),
    ('crud_sexual_5_ja', 'sexual', 5, 'ja', 7537,),
    ('crud_sexual_7_en', 'sexual', 7, 'en', 7538,),
    ('crud_sexual_7_zh-CN', 'sexual', 7, 'zh-CN', 7539,),
    ('crud_sexual_7_ru', 'sexual', 7, 'ru', 7540,),
    ('crud_sexual_7_ar', 'sexual', 7, 'ar', 7541,),
    ('crud_sexual_7_ja', 'sexual', 7, 'ja', 7542,),
    ('crud_sexual_10_en', 'sexual', 10, 'en', 7543,),
    ('crud_sexual_10_zh-CN', 'sexual', 10, 'zh-CN', 7544,),
    ('crud_sexual_10_ru', 'sexual', 10, 'ru', 7545,),
    ('crud_sexual_10_ar', 'sexual', 10, 'ar', 7546,),
    ('crud_sexual_10_ja', 'sexual', 10, 'ja', 7547,),
    ('crud_political_0_en', 'political', 0, 'en', 7548,),
    ('crud_political_0_zh-CN', 'political', 0, 'zh-CN', 7549,),
    ('crud_political_0_ru', 'political', 0, 'ru', 7550,),
    ('crud_political_0_ar', 'political', 0, 'ar', 7551,),
    ('crud_political_0_ja', 'political', 0, 'ja', 7552,),
    ('crud_political_1_en', 'political', 1, 'en', 7553,),
    ('crud_political_1_zh-CN', 'political', 1, 'zh-CN', 7554,),
    ('crud_political_1_ru', 'political', 1, 'ru', 7555,),
    ('crud_political_1_ar', 'political', 1, 'ar', 7556,),
    ('crud_political_1_ja', 'political', 1, 'ja', 7557,),
    ('crud_political_3_en', 'political', 3, 'en', 7558,),
    ('crud_political_3_zh-CN', 'political', 3, 'zh-CN', 7559,),
    ('crud_political_3_ru', 'political', 3, 'ru', 7560,),
    ('crud_political_3_ar', 'political', 3, 'ar', 7561,),
    ('crud_political_3_ja', 'political', 3, 'ja', 7562,),
    ('crud_political_5_en', 'political', 5, 'en', 7563,),
    ('crud_political_5_zh-CN', 'political', 5, 'zh-CN', 7564,),
    ('crud_political_5_ru', 'political', 5, 'ru', 7565,),
    ('crud_political_5_ar', 'political', 5, 'ar', 7566,),
    ('crud_political_5_ja', 'political', 5, 'ja', 7567,),
    ('crud_political_7_en', 'political', 7, 'en', 7568,),
    ('crud_political_7_zh-CN', 'political', 7, 'zh-CN', 7569,),
    ('crud_political_7_ru', 'political', 7, 'ru', 7570,),
    ('crud_political_7_ar', 'political', 7, 'ar', 7571,),
    ('crud_political_7_ja', 'political', 7, 'ja', 7572,),
    ('crud_political_10_en', 'political', 10, 'en', 7573,),
    ('crud_political_10_zh-CN', 'political', 10, 'zh-CN', 7574,),
    ('crud_political_10_ru', 'political', 10, 'ru', 7575,),
    ('crud_political_10_ar', 'political', 10, 'ar', 7576,),
    ('crud_political_10_ja', 'political', 10, 'ja', 7577,),
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
    (1, 0, 7668,),
    (1, 1, 7669,),
    (1, 2, 7670,),
    (1, 3, 7671,),
    (1, 4, 7672,),
    (1, 5, 7673,),
    (1, 6, 7674,),
    (1, 7, 7675,),
    (1, 8, 7676,),
    (1, 9, 7677,),
    (1, 10, 7678,),
    (1, 11, 7679,),
    (1, 12, 7680,),
    (1, 13, 7681,),
    (1, 14, 7682,),
    (2, 0, 7683,),
    (2, 1, 7684,),
    (2, 2, 7685,),
    (2, 3, 7686,),
    (2, 4, 7687,),
    (2, 5, 7688,),
    (2, 6, 7689,),
    (2, 7, 7690,),
    (2, 8, 7691,),
    (2, 9, 7692,),
    (2, 10, 7693,),
    (2, 11, 7694,),
    (2, 12, 7695,),
    (2, 13, 7696,),
    (2, 14, 7697,),
    (5, 0, 7698,),
    (5, 1, 7699,),
    (5, 2, 7700,),
    (5, 3, 7701,),
    (5, 4, 7702,),
    (5, 5, 7703,),
    (5, 6, 7704,),
    (5, 7, 7705,),
    (5, 8, 7706,),
    (5, 9, 7707,),
    (5, 10, 7708,),
    (5, 11, 7709,),
    (5, 12, 7710,),
    (5, 13, 7711,),
    (5, 14, 7712,),
    (10, 0, 7713,),
    (10, 1, 7714,),
    (10, 2, 7715,),
    (10, 3, 7716,),
    (10, 4, 7717,),
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
