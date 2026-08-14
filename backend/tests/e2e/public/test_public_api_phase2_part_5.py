"""Phase 2 public moderation API tests (generated).

Language verdict matrices, batch sizes, validation, unicode edges,
profiling flows and response shapes; see tests/tools/phase2_generator.py."""

# ruff: noqa: RUF001  # multilingual fixtures use non-ASCII on purpose
from __future__ import annotations

from typing import Any

import pytest

from tests.base_test import BaseTest

_EDGE_CONTENT_CASES: tuple[tuple[str, int], ...] = (
    ('emoji 😀 test', 7116,),
    ('emoji 😀 test emoji 😀 test', 7117,),
    ('emoji 😀 test emoji 😀 test emoji 😀 test', 7118,),
    ('lead emoji 😀 test', 7119,),
    ('emoji 😀 test tail', 7120,),
    ('café au lait', 7121,),
    ('café au lait café au lait', 7122,),
    ('café au lait café au lait café au lait', 7123,),
    ('lead café au lait', 7124,),
    ('café au lait tail', 7125,),
    ('ｆｕｌｌｗｉｄｔｈ', 7126,),
    ('ｆｕｌｌｗｉｄｔｈ ｆｕｌｌｗｉｄｔｈ', 7127,),
    ('ｆｕｌｌｗｉｄｔｈ ｆｕｌｌｗｉｄｔｈ ｆｕｌｌｗｉｄｔｈ', 7128,),
    ('lead ｆｕｌｌｗｉｄｔｈ', 7129,),
    ('ｆｕｌｌｗｉｄｔｈ tail', 7130,),
    ('mixed 中文 english 123', 7131,),
    ('mixed 中文 english 123 mixed 中文 english 123', 7132,),
    ('mixed 中文 english 123 mixed 中文 english 123 mixed 中文 english 123', 7133,),
    ('lead mixed 中文 english 123', 7134,),
    ('mixed 中文 english 123 tail', 7135,),
    ('tab\tseparated', 7136,),
    ('tab\tseparated tab\tseparated', 7137,),
    ('tab\tseparated tab\tseparated tab\tseparated', 7138,),
    ('lead tab\tseparated', 7139,),
    ('tab\tseparated tail', 7140,),
    ('line\nbreak', 7141,),
    ('line\nbreak line\nbreak', 7142,),
    ('line\nbreak line\nbreak line\nbreak', 7143,),
    ('lead line\nbreak', 7144,),
    ('line\nbreak tail', 7145,),
    ('multiple   spaces', 7146,),
    ('multiple   spaces multiple   spaces', 7147,),
    ('multiple   spaces multiple   spaces multiple   spaces', 7148,),
    ('lead multiple   spaces', 7149,),
    ('multiple   spaces tail', 7150,),
    ('!!! ??? ...', 7151,),
    ('!!! ??? ... !!! ??? ...', 7152,),
    ('!!! ??? ... !!! ??? ... !!! ??? ...', 7153,),
    ('lead !!! ??? ...', 7154,),
    ('!!! ??? ... tail', 7155,),
    ('12345 67890', 7156,),
    ('12345 67890 12345 67890', 7157,),
    ('12345 67890 12345 67890 12345 67890', 7158,),
    ('lead 12345 67890', 7159,),
    ('12345 67890 tail', 7160,),
    ('x', 7161,),
    ('x x', 7162,),
    ('x x x', 7163,),
    ('lead x', 7164,),
    ('x tail', 7165,),
    ('ßæøåñ', 7166,),
    ('ßæøåñ ßæøåñ', 7167,),
    ('ßæøåñ ßæøåñ ßæøåñ', 7168,),
    ('lead ßæøåñ', 7169,),
    ('ßæøåñ tail', 7170,),
    ('\u2028hidden', 7171,),
    ('\u2028hidden \u2028hidden', 7172,),
    ('\u2028hidden \u2028hidden \u2028hidden', 7173,),
    ('lead \u2028hidden', 7174,),
    ('\u2028hidden tail', 7175,),
    ('zero width \u200b join', 7176,),
    ('zero width \u200b join zero width \u200b join', 7177,),
    ('zero width \u200b join zero width \u200b join zero width \u200b join', 7178,),
    ('lead zero width \u200b join', 7179,),
    ('zero width \u200b join tail', 7180,),
    ('directional \u202e override', 7181,),
    ('directional \u202e override directional \u202e override', 7182,),
    ('directional \u202e override directional \u202e override directional \u202e override', 7183,),
    ('lead directional \u202e override', 7184,),
    ('directional \u202e override tail', 7185,),
    ('combining é', 7186,),
    ('combining é combining é', 7187,),
    ('combining é combining é combining é', 7188,),
    ('lead combining é', 7189,),
    ('combining é tail', 7190,),
    ('русский текст', 7191,),
    ('русский текст русский текст', 7192,),
    ('русский текст русский текст русский текст', 7193,),
    ('lead русский текст', 7194,),
    ('русский текст tail', 7195,),
    ('日本語の文章', 7196,),
    ('日本語の文章 日本語の文章', 7197,),
    ('日本語の文章 日本語の文章 日本語の文章', 7198,),
    ('lead 日本語の文章', 7199,),
    ('日本語の文章 tail', 7200,),
    ('한국어 문장', 7201,),
    ('한국어 문장 한국어 문장', 7202,),
    ('한국어 문장 한국어 문장 한국어 문장', 7203,),
    ('lead 한국어 문장', 7204,),
    ('한국어 문장 tail', 7205,),
    ('العربية نص', 7206,),
    ('العربية نص العربية نص', 7207,),
    ('العربية نص العربية نص العربية نص', 7208,),
    ('lead العربية نص', 7209,),
    ('العربية نص tail', 7210,),
    ('עברית טקסט', 7211,),
    ('עברית טקסט עברית טקסט', 7212,),
    ('עברית טקסט עברית טקסט עברית טקסט', 7213,),
    ('lead עברית טקסט', 7214,),
    ('עברית טקסט tail', 7215,),
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
