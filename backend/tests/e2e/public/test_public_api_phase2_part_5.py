"""Phase 2 public moderation API tests (generated).

Language verdict matrices, batch sizes, validation, unicode edges,
profiling flows and response shapes; see tests/tools/phase2_generator.py."""

# ruff: noqa: RUF001  # multilingual fixtures use non-ASCII on purpose
from __future__ import annotations

from typing import Any

import pytest

from tests.base_test import BaseTest

_EDGE_CONTENT_CASES: tuple[tuple[str, int], ...] = (
    ('emoji 😀 test', 7076,),
    ('emoji 😀 test emoji 😀 test', 7077,),
    ('emoji 😀 test emoji 😀 test emoji 😀 test', 7078,),
    ('lead emoji 😀 test', 7079,),
    ('emoji 😀 test tail', 7080,),
    ('café au lait', 7081,),
    ('café au lait café au lait', 7082,),
    ('café au lait café au lait café au lait', 7083,),
    ('lead café au lait', 7084,),
    ('café au lait tail', 7085,),
    ('ｆｕｌｌｗｉｄｔｈ', 7086,),
    ('ｆｕｌｌｗｉｄｔｈ ｆｕｌｌｗｉｄｔｈ', 7087,),
    ('ｆｕｌｌｗｉｄｔｈ ｆｕｌｌｗｉｄｔｈ ｆｕｌｌｗｉｄｔｈ', 7088,),
    ('lead ｆｕｌｌｗｉｄｔｈ', 7089,),
    ('ｆｕｌｌｗｉｄｔｈ tail', 7090,),
    ('mixed 中文 english 123', 7091,),
    ('mixed 中文 english 123 mixed 中文 english 123', 7092,),
    ('mixed 中文 english 123 mixed 中文 english 123 mixed 中文 english 123', 7093,),
    ('lead mixed 中文 english 123', 7094,),
    ('mixed 中文 english 123 tail', 7095,),
    ('tab\tseparated', 7096,),
    ('tab\tseparated tab\tseparated', 7097,),
    ('tab\tseparated tab\tseparated tab\tseparated', 7098,),
    ('lead tab\tseparated', 7099,),
    ('tab\tseparated tail', 7100,),
    ('line\nbreak', 7101,),
    ('line\nbreak line\nbreak', 7102,),
    ('line\nbreak line\nbreak line\nbreak', 7103,),
    ('lead line\nbreak', 7104,),
    ('line\nbreak tail', 7105,),
    ('multiple   spaces', 7106,),
    ('multiple   spaces multiple   spaces', 7107,),
    ('multiple   spaces multiple   spaces multiple   spaces', 7108,),
    ('lead multiple   spaces', 7109,),
    ('multiple   spaces tail', 7110,),
    ('!!! ??? ...', 7111,),
    ('!!! ??? ... !!! ??? ...', 7112,),
    ('!!! ??? ... !!! ??? ... !!! ??? ...', 7113,),
    ('lead !!! ??? ...', 7114,),
    ('!!! ??? ... tail', 7115,),
    ('12345 67890', 7116,),
    ('12345 67890 12345 67890', 7117,),
    ('12345 67890 12345 67890 12345 67890', 7118,),
    ('lead 12345 67890', 7119,),
    ('12345 67890 tail', 7120,),
    ('x', 7121,),
    ('x x', 7122,),
    ('x x x', 7123,),
    ('lead x', 7124,),
    ('x tail', 7125,),
    ('ßæøåñ', 7126,),
    ('ßæøåñ ßæøåñ', 7127,),
    ('ßæøåñ ßæøåñ ßæøåñ', 7128,),
    ('lead ßæøåñ', 7129,),
    ('ßæøåñ tail', 7130,),
    ('\u2028hidden', 7131,),
    ('\u2028hidden \u2028hidden', 7132,),
    ('\u2028hidden \u2028hidden \u2028hidden', 7133,),
    ('lead \u2028hidden', 7134,),
    ('\u2028hidden tail', 7135,),
    ('zero width \u200b join', 7136,),
    ('zero width \u200b join zero width \u200b join', 7137,),
    ('zero width \u200b join zero width \u200b join zero width \u200b join', 7138,),
    ('lead zero width \u200b join', 7139,),
    ('zero width \u200b join tail', 7140,),
    ('directional \u202e override', 7141,),
    ('directional \u202e override directional \u202e override', 7142,),
    ('directional \u202e override directional \u202e override directional \u202e override', 7143,),
    ('lead directional \u202e override', 7144,),
    ('directional \u202e override tail', 7145,),
    ('combining é', 7146,),
    ('combining é combining é', 7147,),
    ('combining é combining é combining é', 7148,),
    ('lead combining é', 7149,),
    ('combining é tail', 7150,),
    ('русский текст', 7151,),
    ('русский текст русский текст', 7152,),
    ('русский текст русский текст русский текст', 7153,),
    ('lead русский текст', 7154,),
    ('русский текст tail', 7155,),
    ('日本語の文章', 7156,),
    ('日本語の文章 日本語の文章', 7157,),
    ('日本語の文章 日本語の文章 日本語の文章', 7158,),
    ('lead 日本語の文章', 7159,),
    ('日本語の文章 tail', 7160,),
    ('한국어 문장', 7161,),
    ('한국어 문장 한국어 문장', 7162,),
    ('한국어 문장 한국어 문장 한국어 문장', 7163,),
    ('lead 한국어 문장', 7164,),
    ('한국어 문장 tail', 7165,),
    ('العربية نص', 7166,),
    ('العربية نص العربية نص', 7167,),
    ('العربية نص العربية نص العربية نص', 7168,),
    ('lead العربية نص', 7169,),
    ('العربية نص tail', 7170,),
    ('עברית טקסט', 7171,),
    ('עברית טקסט עברית טקסט', 7172,),
    ('עברית טקסט עברית טקסט עברית טקסט', 7173,),
    ('lead עברית טקסט', 7174,),
    ('עברית טקסט tail', 7175,),
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
