"""Phase 2 public moderation API tests (generated).

Language verdict matrices, batch sizes, validation, unicode edges,
profiling flows and response shapes; see tests/tools/phase2_generator.py."""

# ruff: noqa: RUF001  # multilingual fixtures use non-ASCII on purpose
from __future__ import annotations

from typing import Any

import pytest

from tests.base_test import BaseTest

_EDGE_CONTENT_CASES: tuple[tuple[str, int], ...] = (
    ('emoji 😀 test', 6917,),
    ('emoji 😀 test emoji 😀 test', 6918,),
    ('emoji 😀 test emoji 😀 test emoji 😀 test', 6919,),
    ('lead emoji 😀 test', 6920,),
    ('emoji 😀 test tail', 6921,),
    ('café au lait', 6922,),
    ('café au lait café au lait', 6923,),
    ('café au lait café au lait café au lait', 6924,),
    ('lead café au lait', 6925,),
    ('café au lait tail', 6926,),
    ('ｆｕｌｌｗｉｄｔｈ', 6927,),
    ('ｆｕｌｌｗｉｄｔｈ ｆｕｌｌｗｉｄｔｈ', 6928,),
    ('ｆｕｌｌｗｉｄｔｈ ｆｕｌｌｗｉｄｔｈ ｆｕｌｌｗｉｄｔｈ', 6929,),
    ('lead ｆｕｌｌｗｉｄｔｈ', 6930,),
    ('ｆｕｌｌｗｉｄｔｈ tail', 6931,),
    ('mixed 中文 english 123', 6932,),
    ('mixed 中文 english 123 mixed 中文 english 123', 6933,),
    ('mixed 中文 english 123 mixed 中文 english 123 mixed 中文 english 123', 6934,),
    ('lead mixed 中文 english 123', 6935,),
    ('mixed 中文 english 123 tail', 6936,),
    ('tab\tseparated', 6937,),
    ('tab\tseparated tab\tseparated', 6938,),
    ('tab\tseparated tab\tseparated tab\tseparated', 6939,),
    ('lead tab\tseparated', 6940,),
    ('tab\tseparated tail', 6941,),
    ('line\nbreak', 6942,),
    ('line\nbreak line\nbreak', 6943,),
    ('line\nbreak line\nbreak line\nbreak', 6944,),
    ('lead line\nbreak', 6945,),
    ('line\nbreak tail', 6946,),
    ('multiple   spaces', 6947,),
    ('multiple   spaces multiple   spaces', 6948,),
    ('multiple   spaces multiple   spaces multiple   spaces', 6949,),
    ('lead multiple   spaces', 6950,),
    ('multiple   spaces tail', 6951,),
    ('!!! ??? ...', 6952,),
    ('!!! ??? ... !!! ??? ...', 6953,),
    ('!!! ??? ... !!! ??? ... !!! ??? ...', 6954,),
    ('lead !!! ??? ...', 6955,),
    ('!!! ??? ... tail', 6956,),
    ('12345 67890', 6957,),
    ('12345 67890 12345 67890', 6958,),
    ('12345 67890 12345 67890 12345 67890', 6959,),
    ('lead 12345 67890', 6960,),
    ('12345 67890 tail', 6961,),
    ('x', 6962,),
    ('x x', 6963,),
    ('x x x', 6964,),
    ('lead x', 6965,),
    ('x tail', 6966,),
    ('ßæøåñ', 6967,),
    ('ßæøåñ ßæøåñ', 6968,),
    ('ßæøåñ ßæøåñ ßæøåñ', 6969,),
    ('lead ßæøåñ', 6970,),
    ('ßæøåñ tail', 6971,),
    ('\u2028hidden', 6972,),
    ('\u2028hidden \u2028hidden', 6973,),
    ('\u2028hidden \u2028hidden \u2028hidden', 6974,),
    ('lead \u2028hidden', 6975,),
    ('\u2028hidden tail', 6976,),
    ('zero width \u200b join', 6977,),
    ('zero width \u200b join zero width \u200b join', 6978,),
    ('zero width \u200b join zero width \u200b join zero width \u200b join', 6979,),
    ('lead zero width \u200b join', 6980,),
    ('zero width \u200b join tail', 6981,),
    ('directional \u202e override', 6982,),
    ('directional \u202e override directional \u202e override', 6983,),
    ('directional \u202e override directional \u202e override directional \u202e override', 6984,),
    ('lead directional \u202e override', 6985,),
    ('directional \u202e override tail', 6986,),
    ('combining é', 6987,),
    ('combining é combining é', 6988,),
    ('combining é combining é combining é', 6989,),
    ('lead combining é', 6990,),
    ('combining é tail', 6991,),
    ('русский текст', 6992,),
    ('русский текст русский текст', 6993,),
    ('русский текст русский текст русский текст', 6994,),
    ('lead русский текст', 6995,),
    ('русский текст tail', 6996,),
    ('日本語の文章', 6997,),
    ('日本語の文章 日本語の文章', 6998,),
    ('日本語の文章 日本語の文章 日本語の文章', 6999,),
    ('lead 日本語の文章', 7000,),
    ('日本語の文章 tail', 7001,),
    ('한국어 문장', 7002,),
    ('한국어 문장 한국어 문장', 7003,),
    ('한국어 문장 한국어 문장 한국어 문장', 7004,),
    ('lead 한국어 문장', 7005,),
    ('한국어 문장 tail', 7006,),
    ('العربية نص', 7007,),
    ('العربية نص العربية نص', 7008,),
    ('العربية نص العربية نص العربية نص', 7009,),
    ('lead العربية نص', 7010,),
    ('العربية نص tail', 7011,),
    ('עברית טקסט', 7012,),
    ('עברית טקסט עברית טקסט', 7013,),
    ('עברית טקסט עברית טקסט עברית טקסט', 7014,),
    ('lead עברית טקסט', 7015,),
    ('עברית טקסט tail', 7016,),
)

class TestEdgeContent(BaseTest):
    """Unicode and special-character content moderates cleanly."""

    @pytest.mark.parametrize(('text', 'uid',), _EDGE_CONTENT_CASES)
    def test_edge_content(self, client: Any, text: str, uid: int) -> None:
        """Unicode and special-character content moderates cleanly."""
        response = client.post('/moderate', json={'text': text, 'app_name': 'a'})
        assert response.status_code == 200
        assert response.json()['verdict'] in ('PASS', 'BLOCK', 'REVIEW')
        assert response.json()['allowed'] == (response.json()['verdict'] != 'BLOCK')
