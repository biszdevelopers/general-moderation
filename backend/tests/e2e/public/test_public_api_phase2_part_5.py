"""Phase 2 public moderation API tests (generated).

Language verdict matrices, batch sizes, validation, unicode edges,
profiling flows and response shapes; see tests/tools/phase2_generator.py."""

# ruff: noqa: RUF001  # multilingual fixtures use non-ASCII on purpose
from __future__ import annotations

from typing import Any

import pytest

from tests.base_test import BaseTest

_EDGE_CONTENT_CASES: tuple[tuple[str, int], ...] = (
    (
        "emoji 😀 test",
        6917,
    ),
    (
        "emoji 😀 test",
        6918,
    ),
    (
        "emoji 😀 test",
        6919,
    ),
    (
        "emoji 😀 test",
        6920,
    ),
    (
        "emoji 😀 test",
        6921,
    ),
    (
        "café au lait",
        6922,
    ),
    (
        "café au lait",
        6923,
    ),
    (
        "café au lait",
        6924,
    ),
    (
        "café au lait",
        6925,
    ),
    (
        "café au lait",
        6926,
    ),
    (
        "ｆｕｌｌｗｉｄｔｈ",
        6927,
    ),
    (
        "ｆｕｌｌｗｉｄｔｈ",
        6928,
    ),
    (
        "ｆｕｌｌｗｉｄｔｈ",
        6929,
    ),
    (
        "ｆｕｌｌｗｉｄｔｈ",
        6930,
    ),
    (
        "ｆｕｌｌｗｉｄｔｈ",
        6931,
    ),
    (
        "mixed 中文 english 123",
        6932,
    ),
    (
        "mixed 中文 english 123",
        6933,
    ),
    (
        "mixed 中文 english 123",
        6934,
    ),
    (
        "mixed 中文 english 123",
        6935,
    ),
    (
        "mixed 中文 english 123",
        6936,
    ),
    (
        "tab\tseparated",
        6937,
    ),
    (
        "tab\tseparated",
        6938,
    ),
    (
        "tab\tseparated",
        6939,
    ),
    (
        "tab\tseparated",
        6940,
    ),
    (
        "tab\tseparated",
        6941,
    ),
    (
        "line\nbreak",
        6942,
    ),
    (
        "line\nbreak",
        6943,
    ),
    (
        "line\nbreak",
        6944,
    ),
    (
        "line\nbreak",
        6945,
    ),
    (
        "line\nbreak",
        6946,
    ),
    (
        "multiple   spaces",
        6947,
    ),
    (
        "multiple   spaces",
        6948,
    ),
    (
        "multiple   spaces",
        6949,
    ),
    (
        "multiple   spaces",
        6950,
    ),
    (
        "multiple   spaces",
        6951,
    ),
    (
        "!!! ??? ...",
        6952,
    ),
    (
        "!!! ??? ...",
        6953,
    ),
    (
        "!!! ??? ...",
        6954,
    ),
    (
        "!!! ??? ...",
        6955,
    ),
    (
        "!!! ??? ...",
        6956,
    ),
    (
        "12345 67890",
        6957,
    ),
    (
        "12345 67890",
        6958,
    ),
    (
        "12345 67890",
        6959,
    ),
    (
        "12345 67890",
        6960,
    ),
    (
        "12345 67890",
        6961,
    ),
    (
        "x",
        6962,
    ),
    (
        "x",
        6963,
    ),
    (
        "x",
        6964,
    ),
    (
        "x",
        6965,
    ),
    (
        "x",
        6966,
    ),
    (
        "ßæøåñ",
        6967,
    ),
    (
        "ßæøåñ",
        6968,
    ),
    (
        "ßæøåñ",
        6969,
    ),
    (
        "ßæøåñ",
        6970,
    ),
    (
        "ßæøåñ",
        6971,
    ),
    (
        "\u2028hidden",
        6972,
    ),
    (
        "\u2028hidden",
        6973,
    ),
    (
        "\u2028hidden",
        6974,
    ),
    (
        "\u2028hidden",
        6975,
    ),
    (
        "\u2028hidden",
        6976,
    ),
    (
        "zero width \u200b join",
        6977,
    ),
    (
        "zero width \u200b join",
        6978,
    ),
    (
        "zero width \u200b join",
        6979,
    ),
    (
        "zero width \u200b join",
        6980,
    ),
    (
        "zero width \u200b join",
        6981,
    ),
    (
        "directional \u202e override",
        6982,
    ),
    (
        "directional \u202e override",
        6983,
    ),
    (
        "directional \u202e override",
        6984,
    ),
    (
        "directional \u202e override",
        6985,
    ),
    (
        "directional \u202e override",
        6986,
    ),
    (
        "combining é",
        6987,
    ),
    (
        "combining é",
        6988,
    ),
    (
        "combining é",
        6989,
    ),
    (
        "combining é",
        6990,
    ),
    (
        "combining é",
        6991,
    ),
    (
        "русский текст",
        6992,
    ),
    (
        "русский текст",
        6993,
    ),
    (
        "русский текст",
        6994,
    ),
    (
        "русский текст",
        6995,
    ),
    (
        "русский текст",
        6996,
    ),
    (
        "日本語の文章",
        6997,
    ),
    (
        "日本語の文章",
        6998,
    ),
    (
        "日本語の文章",
        6999,
    ),
    (
        "日本語の文章",
        7000,
    ),
    (
        "日本語の文章",
        7001,
    ),
    (
        "한국어 문장",
        7002,
    ),
    (
        "한국어 문장",
        7003,
    ),
    (
        "한국어 문장",
        7004,
    ),
    (
        "한국어 문장",
        7005,
    ),
    (
        "한국어 문장",
        7006,
    ),
    (
        "العربية نص",
        7007,
    ),
    (
        "العربية نص",
        7008,
    ),
    (
        "العربية نص",
        7009,
    ),
    (
        "العربية نص",
        7010,
    ),
    (
        "العربية نص",
        7011,
    ),
    (
        "עברית טקסט",
        7012,
    ),
    (
        "עברית טקסט",
        7013,
    ),
    (
        "עברית טקסט",
        7014,
    ),
    (
        "עברית טקסט",
        7015,
    ),
    (
        "עברית טקסט",
        7016,
    ),
)


class TestEdgeContent(BaseTest):
    """Unicode and special-character content moderates cleanly."""

    @pytest.mark.parametrize(
        (
            "text",
            "uid",
        ),
        _EDGE_CONTENT_CASES,
    )
    def test_edge_content(self, client: Any, text: str, uid: int) -> None:
        """Unicode and special-character content moderates cleanly."""
        response = client.post("/moderate", json={"text": text, "app_name": "a"})
        assert response.status_code == 200
        assert response.json()["verdict"] in ("PASS", "BLOCK", "REVIEW")
        assert response.json()["allowed"] == (response.json()["verdict"] != "BLOCK")
