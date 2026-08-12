"""Phase 2 admin API tests (generated).

Word CRUD, import/export, app policies, settings, logs and dashboard
stats; see tests/tools/phase2_generator.py."""

# multilingual fixtures use non-ASCII on purpose
from __future__ import annotations

from typing import Any

from tests.base_test import BaseTest


class TestWordCrud(BaseTest):
    """WordCrud scenarios."""

    def test_word_crud_other_0_en_7229(self, client: Any, admin_headers: dict[str, str]) -> None:
        """Adding, listing and deleting a custom word round-trips."""
        payload = {"word": "crud_other_0_en", "category": "other", "severity": 0, "language": "en"}
        created = client.post(
            "/admin/wordbank/words",
            headers=admin_headers,
            json=payload,
        )
        assert created.status_code in (201, 409)
        response = client.get("/admin/wordbank/words", headers=admin_headers)
        assert response.status_code == 200
        assert any(entry["word"] == "crud_other_0_en" for entry in response.json())

    def test_word_crud_other_0_zh_CN_7230(self, client: Any, admin_headers: dict[str, str]) -> None:
        """Adding, listing and deleting a custom word round-trips."""
        payload = {
            "word": "crud_other_0_zh-CN",
            "category": "other",
            "severity": 0,
            "language": "zh-CN",
        }
        created = client.post(
            "/admin/wordbank/words",
            headers=admin_headers,
            json=payload,
        )
        assert created.status_code in (201, 409)
        response = client.get("/admin/wordbank/words", headers=admin_headers)
        assert response.status_code == 200
        assert any(entry["word"] == "crud_other_0_zh-cn" for entry in response.json())

    def test_word_crud_other_0_ru_7231(self, client: Any, admin_headers: dict[str, str]) -> None:
        """Adding, listing and deleting a custom word round-trips."""
        payload = {"word": "crud_other_0_ru", "category": "other", "severity": 0, "language": "ru"}
        created = client.post(
            "/admin/wordbank/words",
            headers=admin_headers,
            json=payload,
        )
        assert created.status_code in (201, 409)
        response = client.get("/admin/wordbank/words", headers=admin_headers)
        assert response.status_code == 200
        assert any(entry["word"] == "crud_other_0_ru" for entry in response.json())

    def test_word_crud_other_0_ar_7232(self, client: Any, admin_headers: dict[str, str]) -> None:
        """Adding, listing and deleting a custom word round-trips."""
        payload = {"word": "crud_other_0_ar", "category": "other", "severity": 0, "language": "ar"}
        created = client.post(
            "/admin/wordbank/words",
            headers=admin_headers,
            json=payload,
        )
        assert created.status_code in (201, 409)
        response = client.get("/admin/wordbank/words", headers=admin_headers)
        assert response.status_code == 200
        assert any(entry["word"] == "crud_other_0_ar" for entry in response.json())

    def test_word_crud_other_0_ja_7233(self, client: Any, admin_headers: dict[str, str]) -> None:
        """Adding, listing and deleting a custom word round-trips."""
        payload = {"word": "crud_other_0_ja", "category": "other", "severity": 0, "language": "ja"}
        created = client.post(
            "/admin/wordbank/words",
            headers=admin_headers,
            json=payload,
        )
        assert created.status_code in (201, 409)
        response = client.get("/admin/wordbank/words", headers=admin_headers)
        assert response.status_code == 200
        assert any(entry["word"] == "crud_other_0_ja" for entry in response.json())

    def test_word_crud_other_1_en_7234(self, client: Any, admin_headers: dict[str, str]) -> None:
        """Adding, listing and deleting a custom word round-trips."""
        payload = {"word": "crud_other_1_en", "category": "other", "severity": 1, "language": "en"}
        created = client.post(
            "/admin/wordbank/words",
            headers=admin_headers,
            json=payload,
        )
        assert created.status_code in (201, 409)
        response = client.get("/admin/wordbank/words", headers=admin_headers)
        assert response.status_code == 200
        assert any(entry["word"] == "crud_other_1_en" for entry in response.json())

    def test_word_crud_other_1_zh_CN_7235(self, client: Any, admin_headers: dict[str, str]) -> None:
        """Adding, listing and deleting a custom word round-trips."""
        payload = {
            "word": "crud_other_1_zh-CN",
            "category": "other",
            "severity": 1,
            "language": "zh-CN",
        }
        created = client.post(
            "/admin/wordbank/words",
            headers=admin_headers,
            json=payload,
        )
        assert created.status_code in (201, 409)
        response = client.get("/admin/wordbank/words", headers=admin_headers)
        assert response.status_code == 200
        assert any(entry["word"] == "crud_other_1_zh-cn" for entry in response.json())

    def test_word_crud_other_1_ru_7236(self, client: Any, admin_headers: dict[str, str]) -> None:
        """Adding, listing and deleting a custom word round-trips."""
        payload = {"word": "crud_other_1_ru", "category": "other", "severity": 1, "language": "ru"}
        created = client.post(
            "/admin/wordbank/words",
            headers=admin_headers,
            json=payload,
        )
        assert created.status_code in (201, 409)
        response = client.get("/admin/wordbank/words", headers=admin_headers)
        assert response.status_code == 200
        assert any(entry["word"] == "crud_other_1_ru" for entry in response.json())

    def test_word_crud_other_1_ar_7237(self, client: Any, admin_headers: dict[str, str]) -> None:
        """Adding, listing and deleting a custom word round-trips."""
        payload = {"word": "crud_other_1_ar", "category": "other", "severity": 1, "language": "ar"}
        created = client.post(
            "/admin/wordbank/words",
            headers=admin_headers,
            json=payload,
        )
        assert created.status_code in (201, 409)
        response = client.get("/admin/wordbank/words", headers=admin_headers)
        assert response.status_code == 200
        assert any(entry["word"] == "crud_other_1_ar" for entry in response.json())

    def test_word_crud_other_1_ja_7238(self, client: Any, admin_headers: dict[str, str]) -> None:
        """Adding, listing and deleting a custom word round-trips."""
        payload = {"word": "crud_other_1_ja", "category": "other", "severity": 1, "language": "ja"}
        created = client.post(
            "/admin/wordbank/words",
            headers=admin_headers,
            json=payload,
        )
        assert created.status_code in (201, 409)
        response = client.get("/admin/wordbank/words", headers=admin_headers)
        assert response.status_code == 200
        assert any(entry["word"] == "crud_other_1_ja" for entry in response.json())

    def test_word_crud_other_3_en_7239(self, client: Any, admin_headers: dict[str, str]) -> None:
        """Adding, listing and deleting a custom word round-trips."""
        payload = {"word": "crud_other_3_en", "category": "other", "severity": 3, "language": "en"}
        created = client.post(
            "/admin/wordbank/words",
            headers=admin_headers,
            json=payload,
        )
        assert created.status_code in (201, 409)
        response = client.get("/admin/wordbank/words", headers=admin_headers)
        assert response.status_code == 200
        assert any(entry["word"] == "crud_other_3_en" for entry in response.json())

    def test_word_crud_other_3_zh_CN_7240(self, client: Any, admin_headers: dict[str, str]) -> None:
        """Adding, listing and deleting a custom word round-trips."""
        payload = {
            "word": "crud_other_3_zh-CN",
            "category": "other",
            "severity": 3,
            "language": "zh-CN",
        }
        created = client.post(
            "/admin/wordbank/words",
            headers=admin_headers,
            json=payload,
        )
        assert created.status_code in (201, 409)
        response = client.get("/admin/wordbank/words", headers=admin_headers)
        assert response.status_code == 200
        assert any(entry["word"] == "crud_other_3_zh-cn" for entry in response.json())

    def test_word_crud_other_3_ru_7241(self, client: Any, admin_headers: dict[str, str]) -> None:
        """Adding, listing and deleting a custom word round-trips."""
        payload = {"word": "crud_other_3_ru", "category": "other", "severity": 3, "language": "ru"}
        created = client.post(
            "/admin/wordbank/words",
            headers=admin_headers,
            json=payload,
        )
        assert created.status_code in (201, 409)
        response = client.get("/admin/wordbank/words", headers=admin_headers)
        assert response.status_code == 200
        assert any(entry["word"] == "crud_other_3_ru" for entry in response.json())

    def test_word_crud_other_3_ar_7242(self, client: Any, admin_headers: dict[str, str]) -> None:
        """Adding, listing and deleting a custom word round-trips."""
        payload = {"word": "crud_other_3_ar", "category": "other", "severity": 3, "language": "ar"}
        created = client.post(
            "/admin/wordbank/words",
            headers=admin_headers,
            json=payload,
        )
        assert created.status_code in (201, 409)
        response = client.get("/admin/wordbank/words", headers=admin_headers)
        assert response.status_code == 200
        assert any(entry["word"] == "crud_other_3_ar" for entry in response.json())

    def test_word_crud_other_3_ja_7243(self, client: Any, admin_headers: dict[str, str]) -> None:
        """Adding, listing and deleting a custom word round-trips."""
        payload = {"word": "crud_other_3_ja", "category": "other", "severity": 3, "language": "ja"}
        created = client.post(
            "/admin/wordbank/words",
            headers=admin_headers,
            json=payload,
        )
        assert created.status_code in (201, 409)
        response = client.get("/admin/wordbank/words", headers=admin_headers)
        assert response.status_code == 200
        assert any(entry["word"] == "crud_other_3_ja" for entry in response.json())

    def test_word_crud_other_5_en_7244(self, client: Any, admin_headers: dict[str, str]) -> None:
        """Adding, listing and deleting a custom word round-trips."""
        payload = {"word": "crud_other_5_en", "category": "other", "severity": 5, "language": "en"}
        created = client.post(
            "/admin/wordbank/words",
            headers=admin_headers,
            json=payload,
        )
        assert created.status_code in (201, 409)
        response = client.get("/admin/wordbank/words", headers=admin_headers)
        assert response.status_code == 200
        assert any(entry["word"] == "crud_other_5_en" for entry in response.json())

    def test_word_crud_other_5_zh_CN_7245(self, client: Any, admin_headers: dict[str, str]) -> None:
        """Adding, listing and deleting a custom word round-trips."""
        payload = {
            "word": "crud_other_5_zh-CN",
            "category": "other",
            "severity": 5,
            "language": "zh-CN",
        }
        created = client.post(
            "/admin/wordbank/words",
            headers=admin_headers,
            json=payload,
        )
        assert created.status_code in (201, 409)
        response = client.get("/admin/wordbank/words", headers=admin_headers)
        assert response.status_code == 200
        assert any(entry["word"] == "crud_other_5_zh-cn" for entry in response.json())

    def test_word_crud_other_5_ru_7246(self, client: Any, admin_headers: dict[str, str]) -> None:
        """Adding, listing and deleting a custom word round-trips."""
        payload = {"word": "crud_other_5_ru", "category": "other", "severity": 5, "language": "ru"}
        created = client.post(
            "/admin/wordbank/words",
            headers=admin_headers,
            json=payload,
        )
        assert created.status_code in (201, 409)
        response = client.get("/admin/wordbank/words", headers=admin_headers)
        assert response.status_code == 200
        assert any(entry["word"] == "crud_other_5_ru" for entry in response.json())

    def test_word_crud_other_5_ar_7247(self, client: Any, admin_headers: dict[str, str]) -> None:
        """Adding, listing and deleting a custom word round-trips."""
        payload = {"word": "crud_other_5_ar", "category": "other", "severity": 5, "language": "ar"}
        created = client.post(
            "/admin/wordbank/words",
            headers=admin_headers,
            json=payload,
        )
        assert created.status_code in (201, 409)
        response = client.get("/admin/wordbank/words", headers=admin_headers)
        assert response.status_code == 200
        assert any(entry["word"] == "crud_other_5_ar" for entry in response.json())

    def test_word_crud_other_5_ja_7248(self, client: Any, admin_headers: dict[str, str]) -> None:
        """Adding, listing and deleting a custom word round-trips."""
        payload = {"word": "crud_other_5_ja", "category": "other", "severity": 5, "language": "ja"}
        created = client.post(
            "/admin/wordbank/words",
            headers=admin_headers,
            json=payload,
        )
        assert created.status_code in (201, 409)
        response = client.get("/admin/wordbank/words", headers=admin_headers)
        assert response.status_code == 200
        assert any(entry["word"] == "crud_other_5_ja" for entry in response.json())

    def test_word_crud_other_7_en_7249(self, client: Any, admin_headers: dict[str, str]) -> None:
        """Adding, listing and deleting a custom word round-trips."""
        payload = {"word": "crud_other_7_en", "category": "other", "severity": 7, "language": "en"}
        created = client.post(
            "/admin/wordbank/words",
            headers=admin_headers,
            json=payload,
        )
        assert created.status_code in (201, 409)
        response = client.get("/admin/wordbank/words", headers=admin_headers)
        assert response.status_code == 200
        assert any(entry["word"] == "crud_other_7_en" for entry in response.json())

    def test_word_crud_other_7_zh_CN_7250(self, client: Any, admin_headers: dict[str, str]) -> None:
        """Adding, listing and deleting a custom word round-trips."""
        payload = {
            "word": "crud_other_7_zh-CN",
            "category": "other",
            "severity": 7,
            "language": "zh-CN",
        }
        created = client.post(
            "/admin/wordbank/words",
            headers=admin_headers,
            json=payload,
        )
        assert created.status_code in (201, 409)
        response = client.get("/admin/wordbank/words", headers=admin_headers)
        assert response.status_code == 200
        assert any(entry["word"] == "crud_other_7_zh-cn" for entry in response.json())

    def test_word_crud_other_7_ru_7251(self, client: Any, admin_headers: dict[str, str]) -> None:
        """Adding, listing and deleting a custom word round-trips."""
        payload = {"word": "crud_other_7_ru", "category": "other", "severity": 7, "language": "ru"}
        created = client.post(
            "/admin/wordbank/words",
            headers=admin_headers,
            json=payload,
        )
        assert created.status_code in (201, 409)
        response = client.get("/admin/wordbank/words", headers=admin_headers)
        assert response.status_code == 200
        assert any(entry["word"] == "crud_other_7_ru" for entry in response.json())

    def test_word_crud_other_7_ar_7252(self, client: Any, admin_headers: dict[str, str]) -> None:
        """Adding, listing and deleting a custom word round-trips."""
        payload = {"word": "crud_other_7_ar", "category": "other", "severity": 7, "language": "ar"}
        created = client.post(
            "/admin/wordbank/words",
            headers=admin_headers,
            json=payload,
        )
        assert created.status_code in (201, 409)
        response = client.get("/admin/wordbank/words", headers=admin_headers)
        assert response.status_code == 200
        assert any(entry["word"] == "crud_other_7_ar" for entry in response.json())

    def test_word_crud_other_7_ja_7253(self, client: Any, admin_headers: dict[str, str]) -> None:
        """Adding, listing and deleting a custom word round-trips."""
        payload = {"word": "crud_other_7_ja", "category": "other", "severity": 7, "language": "ja"}
        created = client.post(
            "/admin/wordbank/words",
            headers=admin_headers,
            json=payload,
        )
        assert created.status_code in (201, 409)
        response = client.get("/admin/wordbank/words", headers=admin_headers)
        assert response.status_code == 200
        assert any(entry["word"] == "crud_other_7_ja" for entry in response.json())

    def test_word_crud_other_10_en_7254(self, client: Any, admin_headers: dict[str, str]) -> None:
        """Adding, listing and deleting a custom word round-trips."""
        payload = {
            "word": "crud_other_10_en",
            "category": "other",
            "severity": 10,
            "language": "en",
        }
        created = client.post(
            "/admin/wordbank/words",
            headers=admin_headers,
            json=payload,
        )
        assert created.status_code in (201, 409)
        response = client.get("/admin/wordbank/words", headers=admin_headers)
        assert response.status_code == 200
        assert any(entry["word"] == "crud_other_10_en" for entry in response.json())

    def test_word_crud_other_10_zh_CN_7255(
        self, client: Any, admin_headers: dict[str, str]
    ) -> None:
        """Adding, listing and deleting a custom word round-trips."""
        payload = {
            "word": "crud_other_10_zh-CN",
            "category": "other",
            "severity": 10,
            "language": "zh-CN",
        }
        created = client.post(
            "/admin/wordbank/words",
            headers=admin_headers,
            json=payload,
        )
        assert created.status_code in (201, 409)
        response = client.get("/admin/wordbank/words", headers=admin_headers)
        assert response.status_code == 200
        assert any(entry["word"] == "crud_other_10_zh-cn" for entry in response.json())

    def test_word_crud_other_10_ru_7256(self, client: Any, admin_headers: dict[str, str]) -> None:
        """Adding, listing and deleting a custom word round-trips."""
        payload = {
            "word": "crud_other_10_ru",
            "category": "other",
            "severity": 10,
            "language": "ru",
        }
        created = client.post(
            "/admin/wordbank/words",
            headers=admin_headers,
            json=payload,
        )
        assert created.status_code in (201, 409)
        response = client.get("/admin/wordbank/words", headers=admin_headers)
        assert response.status_code == 200
        assert any(entry["word"] == "crud_other_10_ru" for entry in response.json())

    def test_word_crud_other_10_ar_7257(self, client: Any, admin_headers: dict[str, str]) -> None:
        """Adding, listing and deleting a custom word round-trips."""
        payload = {
            "word": "crud_other_10_ar",
            "category": "other",
            "severity": 10,
            "language": "ar",
        }
        created = client.post(
            "/admin/wordbank/words",
            headers=admin_headers,
            json=payload,
        )
        assert created.status_code in (201, 409)
        response = client.get("/admin/wordbank/words", headers=admin_headers)
        assert response.status_code == 200
        assert any(entry["word"] == "crud_other_10_ar" for entry in response.json())

    def test_word_crud_other_10_ja_7258(self, client: Any, admin_headers: dict[str, str]) -> None:
        """Adding, listing and deleting a custom word round-trips."""
        payload = {
            "word": "crud_other_10_ja",
            "category": "other",
            "severity": 10,
            "language": "ja",
        }
        created = client.post(
            "/admin/wordbank/words",
            headers=admin_headers,
            json=payload,
        )
        assert created.status_code in (201, 409)
        response = client.get("/admin/wordbank/words", headers=admin_headers)
        assert response.status_code == 200
        assert any(entry["word"] == "crud_other_10_ja" for entry in response.json())

    def test_word_crud_hate_speech_0_en_7259(
        self, client: Any, admin_headers: dict[str, str]
    ) -> None:
        """Adding, listing and deleting a custom word round-trips."""
        payload = {
            "word": "crud_hate_speech_0_en",
            "category": "hate_speech",
            "severity": 0,
            "language": "en",
        }
        created = client.post(
            "/admin/wordbank/words",
            headers=admin_headers,
            json=payload,
        )
        assert created.status_code in (201, 409)
        response = client.get("/admin/wordbank/words", headers=admin_headers)
        assert response.status_code == 200
        assert any(entry["word"] == "crud_hate_speech_0_en" for entry in response.json())

    def test_word_crud_hate_speech_0_zh_CN_7260(
        self, client: Any, admin_headers: dict[str, str]
    ) -> None:
        """Adding, listing and deleting a custom word round-trips."""
        payload = {
            "word": "crud_hate_speech_0_zh-CN",
            "category": "hate_speech",
            "severity": 0,
            "language": "zh-CN",
        }
        created = client.post(
            "/admin/wordbank/words",
            headers=admin_headers,
            json=payload,
        )
        assert created.status_code in (201, 409)
        response = client.get("/admin/wordbank/words", headers=admin_headers)
        assert response.status_code == 200
        assert any(entry["word"] == "crud_hate_speech_0_zh-cn" for entry in response.json())

    def test_word_crud_hate_speech_0_ru_7261(
        self, client: Any, admin_headers: dict[str, str]
    ) -> None:
        """Adding, listing and deleting a custom word round-trips."""
        payload = {
            "word": "crud_hate_speech_0_ru",
            "category": "hate_speech",
            "severity": 0,
            "language": "ru",
        }
        created = client.post(
            "/admin/wordbank/words",
            headers=admin_headers,
            json=payload,
        )
        assert created.status_code in (201, 409)
        response = client.get("/admin/wordbank/words", headers=admin_headers)
        assert response.status_code == 200
        assert any(entry["word"] == "crud_hate_speech_0_ru" for entry in response.json())

    def test_word_crud_hate_speech_0_ar_7262(
        self, client: Any, admin_headers: dict[str, str]
    ) -> None:
        """Adding, listing and deleting a custom word round-trips."""
        payload = {
            "word": "crud_hate_speech_0_ar",
            "category": "hate_speech",
            "severity": 0,
            "language": "ar",
        }
        created = client.post(
            "/admin/wordbank/words",
            headers=admin_headers,
            json=payload,
        )
        assert created.status_code in (201, 409)
        response = client.get("/admin/wordbank/words", headers=admin_headers)
        assert response.status_code == 200
        assert any(entry["word"] == "crud_hate_speech_0_ar" for entry in response.json())

    def test_word_crud_hate_speech_0_ja_7263(
        self, client: Any, admin_headers: dict[str, str]
    ) -> None:
        """Adding, listing and deleting a custom word round-trips."""
        payload = {
            "word": "crud_hate_speech_0_ja",
            "category": "hate_speech",
            "severity": 0,
            "language": "ja",
        }
        created = client.post(
            "/admin/wordbank/words",
            headers=admin_headers,
            json=payload,
        )
        assert created.status_code in (201, 409)
        response = client.get("/admin/wordbank/words", headers=admin_headers)
        assert response.status_code == 200
        assert any(entry["word"] == "crud_hate_speech_0_ja" for entry in response.json())

    def test_word_crud_hate_speech_1_en_7264(
        self, client: Any, admin_headers: dict[str, str]
    ) -> None:
        """Adding, listing and deleting a custom word round-trips."""
        payload = {
            "word": "crud_hate_speech_1_en",
            "category": "hate_speech",
            "severity": 1,
            "language": "en",
        }
        created = client.post(
            "/admin/wordbank/words",
            headers=admin_headers,
            json=payload,
        )
        assert created.status_code in (201, 409)
        response = client.get("/admin/wordbank/words", headers=admin_headers)
        assert response.status_code == 200
        assert any(entry["word"] == "crud_hate_speech_1_en" for entry in response.json())

    def test_word_crud_hate_speech_1_zh_CN_7265(
        self, client: Any, admin_headers: dict[str, str]
    ) -> None:
        """Adding, listing and deleting a custom word round-trips."""
        payload = {
            "word": "crud_hate_speech_1_zh-CN",
            "category": "hate_speech",
            "severity": 1,
            "language": "zh-CN",
        }
        created = client.post(
            "/admin/wordbank/words",
            headers=admin_headers,
            json=payload,
        )
        assert created.status_code in (201, 409)
        response = client.get("/admin/wordbank/words", headers=admin_headers)
        assert response.status_code == 200
        assert any(entry["word"] == "crud_hate_speech_1_zh-cn" for entry in response.json())

    def test_word_crud_hate_speech_1_ru_7266(
        self, client: Any, admin_headers: dict[str, str]
    ) -> None:
        """Adding, listing and deleting a custom word round-trips."""
        payload = {
            "word": "crud_hate_speech_1_ru",
            "category": "hate_speech",
            "severity": 1,
            "language": "ru",
        }
        created = client.post(
            "/admin/wordbank/words",
            headers=admin_headers,
            json=payload,
        )
        assert created.status_code in (201, 409)
        response = client.get("/admin/wordbank/words", headers=admin_headers)
        assert response.status_code == 200
        assert any(entry["word"] == "crud_hate_speech_1_ru" for entry in response.json())

    def test_word_crud_hate_speech_1_ar_7267(
        self, client: Any, admin_headers: dict[str, str]
    ) -> None:
        """Adding, listing and deleting a custom word round-trips."""
        payload = {
            "word": "crud_hate_speech_1_ar",
            "category": "hate_speech",
            "severity": 1,
            "language": "ar",
        }
        created = client.post(
            "/admin/wordbank/words",
            headers=admin_headers,
            json=payload,
        )
        assert created.status_code in (201, 409)
        response = client.get("/admin/wordbank/words", headers=admin_headers)
        assert response.status_code == 200
        assert any(entry["word"] == "crud_hate_speech_1_ar" for entry in response.json())

    def test_word_crud_hate_speech_1_ja_7268(
        self, client: Any, admin_headers: dict[str, str]
    ) -> None:
        """Adding, listing and deleting a custom word round-trips."""
        payload = {
            "word": "crud_hate_speech_1_ja",
            "category": "hate_speech",
            "severity": 1,
            "language": "ja",
        }
        created = client.post(
            "/admin/wordbank/words",
            headers=admin_headers,
            json=payload,
        )
        assert created.status_code in (201, 409)
        response = client.get("/admin/wordbank/words", headers=admin_headers)
        assert response.status_code == 200
        assert any(entry["word"] == "crud_hate_speech_1_ja" for entry in response.json())

    def test_word_crud_hate_speech_3_en_7269(
        self, client: Any, admin_headers: dict[str, str]
    ) -> None:
        """Adding, listing and deleting a custom word round-trips."""
        payload = {
            "word": "crud_hate_speech_3_en",
            "category": "hate_speech",
            "severity": 3,
            "language": "en",
        }
        created = client.post(
            "/admin/wordbank/words",
            headers=admin_headers,
            json=payload,
        )
        assert created.status_code in (201, 409)
        response = client.get("/admin/wordbank/words", headers=admin_headers)
        assert response.status_code == 200
        assert any(entry["word"] == "crud_hate_speech_3_en" for entry in response.json())

    def test_word_crud_hate_speech_3_zh_CN_7270(
        self, client: Any, admin_headers: dict[str, str]
    ) -> None:
        """Adding, listing and deleting a custom word round-trips."""
        payload = {
            "word": "crud_hate_speech_3_zh-CN",
            "category": "hate_speech",
            "severity": 3,
            "language": "zh-CN",
        }
        created = client.post(
            "/admin/wordbank/words",
            headers=admin_headers,
            json=payload,
        )
        assert created.status_code in (201, 409)
        response = client.get("/admin/wordbank/words", headers=admin_headers)
        assert response.status_code == 200
        assert any(entry["word"] == "crud_hate_speech_3_zh-cn" for entry in response.json())

    def test_word_crud_hate_speech_3_ru_7271(
        self, client: Any, admin_headers: dict[str, str]
    ) -> None:
        """Adding, listing and deleting a custom word round-trips."""
        payload = {
            "word": "crud_hate_speech_3_ru",
            "category": "hate_speech",
            "severity": 3,
            "language": "ru",
        }
        created = client.post(
            "/admin/wordbank/words",
            headers=admin_headers,
            json=payload,
        )
        assert created.status_code in (201, 409)
        response = client.get("/admin/wordbank/words", headers=admin_headers)
        assert response.status_code == 200
        assert any(entry["word"] == "crud_hate_speech_3_ru" for entry in response.json())

    def test_word_crud_hate_speech_3_ar_7272(
        self, client: Any, admin_headers: dict[str, str]
    ) -> None:
        """Adding, listing and deleting a custom word round-trips."""
        payload = {
            "word": "crud_hate_speech_3_ar",
            "category": "hate_speech",
            "severity": 3,
            "language": "ar",
        }
        created = client.post(
            "/admin/wordbank/words",
            headers=admin_headers,
            json=payload,
        )
        assert created.status_code in (201, 409)
        response = client.get("/admin/wordbank/words", headers=admin_headers)
        assert response.status_code == 200
        assert any(entry["word"] == "crud_hate_speech_3_ar" for entry in response.json())

    def test_word_crud_hate_speech_3_ja_7273(
        self, client: Any, admin_headers: dict[str, str]
    ) -> None:
        """Adding, listing and deleting a custom word round-trips."""
        payload = {
            "word": "crud_hate_speech_3_ja",
            "category": "hate_speech",
            "severity": 3,
            "language": "ja",
        }
        created = client.post(
            "/admin/wordbank/words",
            headers=admin_headers,
            json=payload,
        )
        assert created.status_code in (201, 409)
        response = client.get("/admin/wordbank/words", headers=admin_headers)
        assert response.status_code == 200
        assert any(entry["word"] == "crud_hate_speech_3_ja" for entry in response.json())

    def test_word_crud_hate_speech_5_en_7274(
        self, client: Any, admin_headers: dict[str, str]
    ) -> None:
        """Adding, listing and deleting a custom word round-trips."""
        payload = {
            "word": "crud_hate_speech_5_en",
            "category": "hate_speech",
            "severity": 5,
            "language": "en",
        }
        created = client.post(
            "/admin/wordbank/words",
            headers=admin_headers,
            json=payload,
        )
        assert created.status_code in (201, 409)
        response = client.get("/admin/wordbank/words", headers=admin_headers)
        assert response.status_code == 200
        assert any(entry["word"] == "crud_hate_speech_5_en" for entry in response.json())

    def test_word_crud_hate_speech_5_zh_CN_7275(
        self, client: Any, admin_headers: dict[str, str]
    ) -> None:
        """Adding, listing and deleting a custom word round-trips."""
        payload = {
            "word": "crud_hate_speech_5_zh-CN",
            "category": "hate_speech",
            "severity": 5,
            "language": "zh-CN",
        }
        created = client.post(
            "/admin/wordbank/words",
            headers=admin_headers,
            json=payload,
        )
        assert created.status_code in (201, 409)
        response = client.get("/admin/wordbank/words", headers=admin_headers)
        assert response.status_code == 200
        assert any(entry["word"] == "crud_hate_speech_5_zh-cn" for entry in response.json())

    def test_word_crud_hate_speech_5_ru_7276(
        self, client: Any, admin_headers: dict[str, str]
    ) -> None:
        """Adding, listing and deleting a custom word round-trips."""
        payload = {
            "word": "crud_hate_speech_5_ru",
            "category": "hate_speech",
            "severity": 5,
            "language": "ru",
        }
        created = client.post(
            "/admin/wordbank/words",
            headers=admin_headers,
            json=payload,
        )
        assert created.status_code in (201, 409)
        response = client.get("/admin/wordbank/words", headers=admin_headers)
        assert response.status_code == 200
        assert any(entry["word"] == "crud_hate_speech_5_ru" for entry in response.json())

    def test_word_crud_hate_speech_5_ar_7277(
        self, client: Any, admin_headers: dict[str, str]
    ) -> None:
        """Adding, listing and deleting a custom word round-trips."""
        payload = {
            "word": "crud_hate_speech_5_ar",
            "category": "hate_speech",
            "severity": 5,
            "language": "ar",
        }
        created = client.post(
            "/admin/wordbank/words",
            headers=admin_headers,
            json=payload,
        )
        assert created.status_code in (201, 409)
        response = client.get("/admin/wordbank/words", headers=admin_headers)
        assert response.status_code == 200
        assert any(entry["word"] == "crud_hate_speech_5_ar" for entry in response.json())

    def test_word_crud_hate_speech_5_ja_7278(
        self, client: Any, admin_headers: dict[str, str]
    ) -> None:
        """Adding, listing and deleting a custom word round-trips."""
        payload = {
            "word": "crud_hate_speech_5_ja",
            "category": "hate_speech",
            "severity": 5,
            "language": "ja",
        }
        created = client.post(
            "/admin/wordbank/words",
            headers=admin_headers,
            json=payload,
        )
        assert created.status_code in (201, 409)
        response = client.get("/admin/wordbank/words", headers=admin_headers)
        assert response.status_code == 200
        assert any(entry["word"] == "crud_hate_speech_5_ja" for entry in response.json())

    def test_word_crud_hate_speech_7_en_7279(
        self, client: Any, admin_headers: dict[str, str]
    ) -> None:
        """Adding, listing and deleting a custom word round-trips."""
        payload = {
            "word": "crud_hate_speech_7_en",
            "category": "hate_speech",
            "severity": 7,
            "language": "en",
        }
        created = client.post(
            "/admin/wordbank/words",
            headers=admin_headers,
            json=payload,
        )
        assert created.status_code in (201, 409)
        response = client.get("/admin/wordbank/words", headers=admin_headers)
        assert response.status_code == 200
        assert any(entry["word"] == "crud_hate_speech_7_en" for entry in response.json())

    def test_word_crud_hate_speech_7_zh_CN_7280(
        self, client: Any, admin_headers: dict[str, str]
    ) -> None:
        """Adding, listing and deleting a custom word round-trips."""
        payload = {
            "word": "crud_hate_speech_7_zh-CN",
            "category": "hate_speech",
            "severity": 7,
            "language": "zh-CN",
        }
        created = client.post(
            "/admin/wordbank/words",
            headers=admin_headers,
            json=payload,
        )
        assert created.status_code in (201, 409)
        response = client.get("/admin/wordbank/words", headers=admin_headers)
        assert response.status_code == 200
        assert any(entry["word"] == "crud_hate_speech_7_zh-cn" for entry in response.json())

    def test_word_crud_hate_speech_7_ru_7281(
        self, client: Any, admin_headers: dict[str, str]
    ) -> None:
        """Adding, listing and deleting a custom word round-trips."""
        payload = {
            "word": "crud_hate_speech_7_ru",
            "category": "hate_speech",
            "severity": 7,
            "language": "ru",
        }
        created = client.post(
            "/admin/wordbank/words",
            headers=admin_headers,
            json=payload,
        )
        assert created.status_code in (201, 409)
        response = client.get("/admin/wordbank/words", headers=admin_headers)
        assert response.status_code == 200
        assert any(entry["word"] == "crud_hate_speech_7_ru" for entry in response.json())

    def test_word_crud_hate_speech_7_ar_7282(
        self, client: Any, admin_headers: dict[str, str]
    ) -> None:
        """Adding, listing and deleting a custom word round-trips."""
        payload = {
            "word": "crud_hate_speech_7_ar",
            "category": "hate_speech",
            "severity": 7,
            "language": "ar",
        }
        created = client.post(
            "/admin/wordbank/words",
            headers=admin_headers,
            json=payload,
        )
        assert created.status_code in (201, 409)
        response = client.get("/admin/wordbank/words", headers=admin_headers)
        assert response.status_code == 200
        assert any(entry["word"] == "crud_hate_speech_7_ar" for entry in response.json())

    def test_word_crud_hate_speech_7_ja_7283(
        self, client: Any, admin_headers: dict[str, str]
    ) -> None:
        """Adding, listing and deleting a custom word round-trips."""
        payload = {
            "word": "crud_hate_speech_7_ja",
            "category": "hate_speech",
            "severity": 7,
            "language": "ja",
        }
        created = client.post(
            "/admin/wordbank/words",
            headers=admin_headers,
            json=payload,
        )
        assert created.status_code in (201, 409)
        response = client.get("/admin/wordbank/words", headers=admin_headers)
        assert response.status_code == 200
        assert any(entry["word"] == "crud_hate_speech_7_ja" for entry in response.json())

    def test_word_crud_hate_speech_10_en_7284(
        self, client: Any, admin_headers: dict[str, str]
    ) -> None:
        """Adding, listing and deleting a custom word round-trips."""
        payload = {
            "word": "crud_hate_speech_10_en",
            "category": "hate_speech",
            "severity": 10,
            "language": "en",
        }
        created = client.post(
            "/admin/wordbank/words",
            headers=admin_headers,
            json=payload,
        )
        assert created.status_code in (201, 409)
        response = client.get("/admin/wordbank/words", headers=admin_headers)
        assert response.status_code == 200
        assert any(entry["word"] == "crud_hate_speech_10_en" for entry in response.json())

    def test_word_crud_hate_speech_10_zh_CN_7285(
        self, client: Any, admin_headers: dict[str, str]
    ) -> None:
        """Adding, listing and deleting a custom word round-trips."""
        payload = {
            "word": "crud_hate_speech_10_zh-CN",
            "category": "hate_speech",
            "severity": 10,
            "language": "zh-CN",
        }
        created = client.post(
            "/admin/wordbank/words",
            headers=admin_headers,
            json=payload,
        )
        assert created.status_code in (201, 409)
        response = client.get("/admin/wordbank/words", headers=admin_headers)
        assert response.status_code == 200
        assert any(entry["word"] == "crud_hate_speech_10_zh-cn" for entry in response.json())

    def test_word_crud_hate_speech_10_ru_7286(
        self, client: Any, admin_headers: dict[str, str]
    ) -> None:
        """Adding, listing and deleting a custom word round-trips."""
        payload = {
            "word": "crud_hate_speech_10_ru",
            "category": "hate_speech",
            "severity": 10,
            "language": "ru",
        }
        created = client.post(
            "/admin/wordbank/words",
            headers=admin_headers,
            json=payload,
        )
        assert created.status_code in (201, 409)
        response = client.get("/admin/wordbank/words", headers=admin_headers)
        assert response.status_code == 200
        assert any(entry["word"] == "crud_hate_speech_10_ru" for entry in response.json())

    def test_word_crud_hate_speech_10_ar_7287(
        self, client: Any, admin_headers: dict[str, str]
    ) -> None:
        """Adding, listing and deleting a custom word round-trips."""
        payload = {
            "word": "crud_hate_speech_10_ar",
            "category": "hate_speech",
            "severity": 10,
            "language": "ar",
        }
        created = client.post(
            "/admin/wordbank/words",
            headers=admin_headers,
            json=payload,
        )
        assert created.status_code in (201, 409)
        response = client.get("/admin/wordbank/words", headers=admin_headers)
        assert response.status_code == 200
        assert any(entry["word"] == "crud_hate_speech_10_ar" for entry in response.json())

    def test_word_crud_hate_speech_10_ja_7288(
        self, client: Any, admin_headers: dict[str, str]
    ) -> None:
        """Adding, listing and deleting a custom word round-trips."""
        payload = {
            "word": "crud_hate_speech_10_ja",
            "category": "hate_speech",
            "severity": 10,
            "language": "ja",
        }
        created = client.post(
            "/admin/wordbank/words",
            headers=admin_headers,
            json=payload,
        )
        assert created.status_code in (201, 409)
        response = client.get("/admin/wordbank/words", headers=admin_headers)
        assert response.status_code == 200
        assert any(entry["word"] == "crud_hate_speech_10_ja" for entry in response.json())

    def test_word_crud_violence_0_en_7289(self, client: Any, admin_headers: dict[str, str]) -> None:
        """Adding, listing and deleting a custom word round-trips."""
        payload = {
            "word": "crud_violence_0_en",
            "category": "violence",
            "severity": 0,
            "language": "en",
        }
        created = client.post(
            "/admin/wordbank/words",
            headers=admin_headers,
            json=payload,
        )
        assert created.status_code in (201, 409)
        response = client.get("/admin/wordbank/words", headers=admin_headers)
        assert response.status_code == 200
        assert any(entry["word"] == "crud_violence_0_en" for entry in response.json())

    def test_word_crud_violence_0_zh_CN_7290(
        self, client: Any, admin_headers: dict[str, str]
    ) -> None:
        """Adding, listing and deleting a custom word round-trips."""
        payload = {
            "word": "crud_violence_0_zh-CN",
            "category": "violence",
            "severity": 0,
            "language": "zh-CN",
        }
        created = client.post(
            "/admin/wordbank/words",
            headers=admin_headers,
            json=payload,
        )
        assert created.status_code in (201, 409)
        response = client.get("/admin/wordbank/words", headers=admin_headers)
        assert response.status_code == 200
        assert any(entry["word"] == "crud_violence_0_zh-cn" for entry in response.json())

    def test_word_crud_violence_0_ru_7291(self, client: Any, admin_headers: dict[str, str]) -> None:
        """Adding, listing and deleting a custom word round-trips."""
        payload = {
            "word": "crud_violence_0_ru",
            "category": "violence",
            "severity": 0,
            "language": "ru",
        }
        created = client.post(
            "/admin/wordbank/words",
            headers=admin_headers,
            json=payload,
        )
        assert created.status_code in (201, 409)
        response = client.get("/admin/wordbank/words", headers=admin_headers)
        assert response.status_code == 200
        assert any(entry["word"] == "crud_violence_0_ru" for entry in response.json())

    def test_word_crud_violence_0_ar_7292(self, client: Any, admin_headers: dict[str, str]) -> None:
        """Adding, listing and deleting a custom word round-trips."""
        payload = {
            "word": "crud_violence_0_ar",
            "category": "violence",
            "severity": 0,
            "language": "ar",
        }
        created = client.post(
            "/admin/wordbank/words",
            headers=admin_headers,
            json=payload,
        )
        assert created.status_code in (201, 409)
        response = client.get("/admin/wordbank/words", headers=admin_headers)
        assert response.status_code == 200
        assert any(entry["word"] == "crud_violence_0_ar" for entry in response.json())

    def test_word_crud_violence_0_ja_7293(self, client: Any, admin_headers: dict[str, str]) -> None:
        """Adding, listing and deleting a custom word round-trips."""
        payload = {
            "word": "crud_violence_0_ja",
            "category": "violence",
            "severity": 0,
            "language": "ja",
        }
        created = client.post(
            "/admin/wordbank/words",
            headers=admin_headers,
            json=payload,
        )
        assert created.status_code in (201, 409)
        response = client.get("/admin/wordbank/words", headers=admin_headers)
        assert response.status_code == 200
        assert any(entry["word"] == "crud_violence_0_ja" for entry in response.json())

    def test_word_crud_violence_1_en_7294(self, client: Any, admin_headers: dict[str, str]) -> None:
        """Adding, listing and deleting a custom word round-trips."""
        payload = {
            "word": "crud_violence_1_en",
            "category": "violence",
            "severity": 1,
            "language": "en",
        }
        created = client.post(
            "/admin/wordbank/words",
            headers=admin_headers,
            json=payload,
        )
        assert created.status_code in (201, 409)
        response = client.get("/admin/wordbank/words", headers=admin_headers)
        assert response.status_code == 200
        assert any(entry["word"] == "crud_violence_1_en" for entry in response.json())

    def test_word_crud_violence_1_zh_CN_7295(
        self, client: Any, admin_headers: dict[str, str]
    ) -> None:
        """Adding, listing and deleting a custom word round-trips."""
        payload = {
            "word": "crud_violence_1_zh-CN",
            "category": "violence",
            "severity": 1,
            "language": "zh-CN",
        }
        created = client.post(
            "/admin/wordbank/words",
            headers=admin_headers,
            json=payload,
        )
        assert created.status_code in (201, 409)
        response = client.get("/admin/wordbank/words", headers=admin_headers)
        assert response.status_code == 200
        assert any(entry["word"] == "crud_violence_1_zh-cn" for entry in response.json())

    def test_word_crud_violence_1_ru_7296(self, client: Any, admin_headers: dict[str, str]) -> None:
        """Adding, listing and deleting a custom word round-trips."""
        payload = {
            "word": "crud_violence_1_ru",
            "category": "violence",
            "severity": 1,
            "language": "ru",
        }
        created = client.post(
            "/admin/wordbank/words",
            headers=admin_headers,
            json=payload,
        )
        assert created.status_code in (201, 409)
        response = client.get("/admin/wordbank/words", headers=admin_headers)
        assert response.status_code == 200
        assert any(entry["word"] == "crud_violence_1_ru" for entry in response.json())

    def test_word_crud_violence_1_ar_7297(self, client: Any, admin_headers: dict[str, str]) -> None:
        """Adding, listing and deleting a custom word round-trips."""
        payload = {
            "word": "crud_violence_1_ar",
            "category": "violence",
            "severity": 1,
            "language": "ar",
        }
        created = client.post(
            "/admin/wordbank/words",
            headers=admin_headers,
            json=payload,
        )
        assert created.status_code in (201, 409)
        response = client.get("/admin/wordbank/words", headers=admin_headers)
        assert response.status_code == 200
        assert any(entry["word"] == "crud_violence_1_ar" for entry in response.json())

    def test_word_crud_violence_1_ja_7298(self, client: Any, admin_headers: dict[str, str]) -> None:
        """Adding, listing and deleting a custom word round-trips."""
        payload = {
            "word": "crud_violence_1_ja",
            "category": "violence",
            "severity": 1,
            "language": "ja",
        }
        created = client.post(
            "/admin/wordbank/words",
            headers=admin_headers,
            json=payload,
        )
        assert created.status_code in (201, 409)
        response = client.get("/admin/wordbank/words", headers=admin_headers)
        assert response.status_code == 200
        assert any(entry["word"] == "crud_violence_1_ja" for entry in response.json())

    def test_word_crud_violence_3_en_7299(self, client: Any, admin_headers: dict[str, str]) -> None:
        """Adding, listing and deleting a custom word round-trips."""
        payload = {
            "word": "crud_violence_3_en",
            "category": "violence",
            "severity": 3,
            "language": "en",
        }
        created = client.post(
            "/admin/wordbank/words",
            headers=admin_headers,
            json=payload,
        )
        assert created.status_code in (201, 409)
        response = client.get("/admin/wordbank/words", headers=admin_headers)
        assert response.status_code == 200
        assert any(entry["word"] == "crud_violence_3_en" for entry in response.json())

    def test_word_crud_violence_3_zh_CN_7300(
        self, client: Any, admin_headers: dict[str, str]
    ) -> None:
        """Adding, listing and deleting a custom word round-trips."""
        payload = {
            "word": "crud_violence_3_zh-CN",
            "category": "violence",
            "severity": 3,
            "language": "zh-CN",
        }
        created = client.post(
            "/admin/wordbank/words",
            headers=admin_headers,
            json=payload,
        )
        assert created.status_code in (201, 409)
        response = client.get("/admin/wordbank/words", headers=admin_headers)
        assert response.status_code == 200
        assert any(entry["word"] == "crud_violence_3_zh-cn" for entry in response.json())

    def test_word_crud_violence_3_ru_7301(self, client: Any, admin_headers: dict[str, str]) -> None:
        """Adding, listing and deleting a custom word round-trips."""
        payload = {
            "word": "crud_violence_3_ru",
            "category": "violence",
            "severity": 3,
            "language": "ru",
        }
        created = client.post(
            "/admin/wordbank/words",
            headers=admin_headers,
            json=payload,
        )
        assert created.status_code in (201, 409)
        response = client.get("/admin/wordbank/words", headers=admin_headers)
        assert response.status_code == 200
        assert any(entry["word"] == "crud_violence_3_ru" for entry in response.json())

    def test_word_crud_violence_3_ar_7302(self, client: Any, admin_headers: dict[str, str]) -> None:
        """Adding, listing and deleting a custom word round-trips."""
        payload = {
            "word": "crud_violence_3_ar",
            "category": "violence",
            "severity": 3,
            "language": "ar",
        }
        created = client.post(
            "/admin/wordbank/words",
            headers=admin_headers,
            json=payload,
        )
        assert created.status_code in (201, 409)
        response = client.get("/admin/wordbank/words", headers=admin_headers)
        assert response.status_code == 200
        assert any(entry["word"] == "crud_violence_3_ar" for entry in response.json())

    def test_word_crud_violence_3_ja_7303(self, client: Any, admin_headers: dict[str, str]) -> None:
        """Adding, listing and deleting a custom word round-trips."""
        payload = {
            "word": "crud_violence_3_ja",
            "category": "violence",
            "severity": 3,
            "language": "ja",
        }
        created = client.post(
            "/admin/wordbank/words",
            headers=admin_headers,
            json=payload,
        )
        assert created.status_code in (201, 409)
        response = client.get("/admin/wordbank/words", headers=admin_headers)
        assert response.status_code == 200
        assert any(entry["word"] == "crud_violence_3_ja" for entry in response.json())

    def test_word_crud_violence_5_en_7304(self, client: Any, admin_headers: dict[str, str]) -> None:
        """Adding, listing and deleting a custom word round-trips."""
        payload = {
            "word": "crud_violence_5_en",
            "category": "violence",
            "severity": 5,
            "language": "en",
        }
        created = client.post(
            "/admin/wordbank/words",
            headers=admin_headers,
            json=payload,
        )
        assert created.status_code in (201, 409)
        response = client.get("/admin/wordbank/words", headers=admin_headers)
        assert response.status_code == 200
        assert any(entry["word"] == "crud_violence_5_en" for entry in response.json())

    def test_word_crud_violence_5_zh_CN_7305(
        self, client: Any, admin_headers: dict[str, str]
    ) -> None:
        """Adding, listing and deleting a custom word round-trips."""
        payload = {
            "word": "crud_violence_5_zh-CN",
            "category": "violence",
            "severity": 5,
            "language": "zh-CN",
        }
        created = client.post(
            "/admin/wordbank/words",
            headers=admin_headers,
            json=payload,
        )
        assert created.status_code in (201, 409)
        response = client.get("/admin/wordbank/words", headers=admin_headers)
        assert response.status_code == 200
        assert any(entry["word"] == "crud_violence_5_zh-cn" for entry in response.json())

    def test_word_crud_violence_5_ru_7306(self, client: Any, admin_headers: dict[str, str]) -> None:
        """Adding, listing and deleting a custom word round-trips."""
        payload = {
            "word": "crud_violence_5_ru",
            "category": "violence",
            "severity": 5,
            "language": "ru",
        }
        created = client.post(
            "/admin/wordbank/words",
            headers=admin_headers,
            json=payload,
        )
        assert created.status_code in (201, 409)
        response = client.get("/admin/wordbank/words", headers=admin_headers)
        assert response.status_code == 200
        assert any(entry["word"] == "crud_violence_5_ru" for entry in response.json())

    def test_word_crud_violence_5_ar_7307(self, client: Any, admin_headers: dict[str, str]) -> None:
        """Adding, listing and deleting a custom word round-trips."""
        payload = {
            "word": "crud_violence_5_ar",
            "category": "violence",
            "severity": 5,
            "language": "ar",
        }
        created = client.post(
            "/admin/wordbank/words",
            headers=admin_headers,
            json=payload,
        )
        assert created.status_code in (201, 409)
        response = client.get("/admin/wordbank/words", headers=admin_headers)
        assert response.status_code == 200
        assert any(entry["word"] == "crud_violence_5_ar" for entry in response.json())

    def test_word_crud_violence_5_ja_7308(self, client: Any, admin_headers: dict[str, str]) -> None:
        """Adding, listing and deleting a custom word round-trips."""
        payload = {
            "word": "crud_violence_5_ja",
            "category": "violence",
            "severity": 5,
            "language": "ja",
        }
        created = client.post(
            "/admin/wordbank/words",
            headers=admin_headers,
            json=payload,
        )
        assert created.status_code in (201, 409)
        response = client.get("/admin/wordbank/words", headers=admin_headers)
        assert response.status_code == 200
        assert any(entry["word"] == "crud_violence_5_ja" for entry in response.json())

    def test_word_crud_violence_7_en_7309(self, client: Any, admin_headers: dict[str, str]) -> None:
        """Adding, listing and deleting a custom word round-trips."""
        payload = {
            "word": "crud_violence_7_en",
            "category": "violence",
            "severity": 7,
            "language": "en",
        }
        created = client.post(
            "/admin/wordbank/words",
            headers=admin_headers,
            json=payload,
        )
        assert created.status_code in (201, 409)
        response = client.get("/admin/wordbank/words", headers=admin_headers)
        assert response.status_code == 200
        assert any(entry["word"] == "crud_violence_7_en" for entry in response.json())

    def test_word_crud_violence_7_zh_CN_7310(
        self, client: Any, admin_headers: dict[str, str]
    ) -> None:
        """Adding, listing and deleting a custom word round-trips."""
        payload = {
            "word": "crud_violence_7_zh-CN",
            "category": "violence",
            "severity": 7,
            "language": "zh-CN",
        }
        created = client.post(
            "/admin/wordbank/words",
            headers=admin_headers,
            json=payload,
        )
        assert created.status_code in (201, 409)
        response = client.get("/admin/wordbank/words", headers=admin_headers)
        assert response.status_code == 200
        assert any(entry["word"] == "crud_violence_7_zh-cn" for entry in response.json())

    def test_word_crud_violence_7_ru_7311(self, client: Any, admin_headers: dict[str, str]) -> None:
        """Adding, listing and deleting a custom word round-trips."""
        payload = {
            "word": "crud_violence_7_ru",
            "category": "violence",
            "severity": 7,
            "language": "ru",
        }
        created = client.post(
            "/admin/wordbank/words",
            headers=admin_headers,
            json=payload,
        )
        assert created.status_code in (201, 409)
        response = client.get("/admin/wordbank/words", headers=admin_headers)
        assert response.status_code == 200
        assert any(entry["word"] == "crud_violence_7_ru" for entry in response.json())

    def test_word_crud_violence_7_ar_7312(self, client: Any, admin_headers: dict[str, str]) -> None:
        """Adding, listing and deleting a custom word round-trips."""
        payload = {
            "word": "crud_violence_7_ar",
            "category": "violence",
            "severity": 7,
            "language": "ar",
        }
        created = client.post(
            "/admin/wordbank/words",
            headers=admin_headers,
            json=payload,
        )
        assert created.status_code in (201, 409)
        response = client.get("/admin/wordbank/words", headers=admin_headers)
        assert response.status_code == 200
        assert any(entry["word"] == "crud_violence_7_ar" for entry in response.json())

    def test_word_crud_violence_7_ja_7313(self, client: Any, admin_headers: dict[str, str]) -> None:
        """Adding, listing and deleting a custom word round-trips."""
        payload = {
            "word": "crud_violence_7_ja",
            "category": "violence",
            "severity": 7,
            "language": "ja",
        }
        created = client.post(
            "/admin/wordbank/words",
            headers=admin_headers,
            json=payload,
        )
        assert created.status_code in (201, 409)
        response = client.get("/admin/wordbank/words", headers=admin_headers)
        assert response.status_code == 200
        assert any(entry["word"] == "crud_violence_7_ja" for entry in response.json())

    def test_word_crud_violence_10_en_7314(
        self, client: Any, admin_headers: dict[str, str]
    ) -> None:
        """Adding, listing and deleting a custom word round-trips."""
        payload = {
            "word": "crud_violence_10_en",
            "category": "violence",
            "severity": 10,
            "language": "en",
        }
        created = client.post(
            "/admin/wordbank/words",
            headers=admin_headers,
            json=payload,
        )
        assert created.status_code in (201, 409)
        response = client.get("/admin/wordbank/words", headers=admin_headers)
        assert response.status_code == 200
        assert any(entry["word"] == "crud_violence_10_en" for entry in response.json())

    def test_word_crud_violence_10_zh_CN_7315(
        self, client: Any, admin_headers: dict[str, str]
    ) -> None:
        """Adding, listing and deleting a custom word round-trips."""
        payload = {
            "word": "crud_violence_10_zh-CN",
            "category": "violence",
            "severity": 10,
            "language": "zh-CN",
        }
        created = client.post(
            "/admin/wordbank/words",
            headers=admin_headers,
            json=payload,
        )
        assert created.status_code in (201, 409)
        response = client.get("/admin/wordbank/words", headers=admin_headers)
        assert response.status_code == 200
        assert any(entry["word"] == "crud_violence_10_zh-cn" for entry in response.json())

    def test_word_crud_violence_10_ru_7316(
        self, client: Any, admin_headers: dict[str, str]
    ) -> None:
        """Adding, listing and deleting a custom word round-trips."""
        payload = {
            "word": "crud_violence_10_ru",
            "category": "violence",
            "severity": 10,
            "language": "ru",
        }
        created = client.post(
            "/admin/wordbank/words",
            headers=admin_headers,
            json=payload,
        )
        assert created.status_code in (201, 409)
        response = client.get("/admin/wordbank/words", headers=admin_headers)
        assert response.status_code == 200
        assert any(entry["word"] == "crud_violence_10_ru" for entry in response.json())

    def test_word_crud_violence_10_ar_7317(
        self, client: Any, admin_headers: dict[str, str]
    ) -> None:
        """Adding, listing and deleting a custom word round-trips."""
        payload = {
            "word": "crud_violence_10_ar",
            "category": "violence",
            "severity": 10,
            "language": "ar",
        }
        created = client.post(
            "/admin/wordbank/words",
            headers=admin_headers,
            json=payload,
        )
        assert created.status_code in (201, 409)
        response = client.get("/admin/wordbank/words", headers=admin_headers)
        assert response.status_code == 200
        assert any(entry["word"] == "crud_violence_10_ar" for entry in response.json())

    def test_word_crud_violence_10_ja_7318(
        self, client: Any, admin_headers: dict[str, str]
    ) -> None:
        """Adding, listing and deleting a custom word round-trips."""
        payload = {
            "word": "crud_violence_10_ja",
            "category": "violence",
            "severity": 10,
            "language": "ja",
        }
        created = client.post(
            "/admin/wordbank/words",
            headers=admin_headers,
            json=payload,
        )
        assert created.status_code in (201, 409)
        response = client.get("/admin/wordbank/words", headers=admin_headers)
        assert response.status_code == 200
        assert any(entry["word"] == "crud_violence_10_ja" for entry in response.json())

    def test_word_crud_sexual_0_en_7319(self, client: Any, admin_headers: dict[str, str]) -> None:
        """Adding, listing and deleting a custom word round-trips."""
        payload = {
            "word": "crud_sexual_0_en",
            "category": "sexual",
            "severity": 0,
            "language": "en",
        }
        created = client.post(
            "/admin/wordbank/words",
            headers=admin_headers,
            json=payload,
        )
        assert created.status_code in (201, 409)
        response = client.get("/admin/wordbank/words", headers=admin_headers)
        assert response.status_code == 200
        assert any(entry["word"] == "crud_sexual_0_en" for entry in response.json())

    def test_word_crud_sexual_0_zh_CN_7320(
        self, client: Any, admin_headers: dict[str, str]
    ) -> None:
        """Adding, listing and deleting a custom word round-trips."""
        payload = {
            "word": "crud_sexual_0_zh-CN",
            "category": "sexual",
            "severity": 0,
            "language": "zh-CN",
        }
        created = client.post(
            "/admin/wordbank/words",
            headers=admin_headers,
            json=payload,
        )
        assert created.status_code in (201, 409)
        response = client.get("/admin/wordbank/words", headers=admin_headers)
        assert response.status_code == 200
        assert any(entry["word"] == "crud_sexual_0_zh-cn" for entry in response.json())

    def test_word_crud_sexual_0_ru_7321(self, client: Any, admin_headers: dict[str, str]) -> None:
        """Adding, listing and deleting a custom word round-trips."""
        payload = {
            "word": "crud_sexual_0_ru",
            "category": "sexual",
            "severity": 0,
            "language": "ru",
        }
        created = client.post(
            "/admin/wordbank/words",
            headers=admin_headers,
            json=payload,
        )
        assert created.status_code in (201, 409)
        response = client.get("/admin/wordbank/words", headers=admin_headers)
        assert response.status_code == 200
        assert any(entry["word"] == "crud_sexual_0_ru" for entry in response.json())

    def test_word_crud_sexual_0_ar_7322(self, client: Any, admin_headers: dict[str, str]) -> None:
        """Adding, listing and deleting a custom word round-trips."""
        payload = {
            "word": "crud_sexual_0_ar",
            "category": "sexual",
            "severity": 0,
            "language": "ar",
        }
        created = client.post(
            "/admin/wordbank/words",
            headers=admin_headers,
            json=payload,
        )
        assert created.status_code in (201, 409)
        response = client.get("/admin/wordbank/words", headers=admin_headers)
        assert response.status_code == 200
        assert any(entry["word"] == "crud_sexual_0_ar" for entry in response.json())

    def test_word_crud_sexual_0_ja_7323(self, client: Any, admin_headers: dict[str, str]) -> None:
        """Adding, listing and deleting a custom word round-trips."""
        payload = {
            "word": "crud_sexual_0_ja",
            "category": "sexual",
            "severity": 0,
            "language": "ja",
        }
        created = client.post(
            "/admin/wordbank/words",
            headers=admin_headers,
            json=payload,
        )
        assert created.status_code in (201, 409)
        response = client.get("/admin/wordbank/words", headers=admin_headers)
        assert response.status_code == 200
        assert any(entry["word"] == "crud_sexual_0_ja" for entry in response.json())

    def test_word_crud_sexual_1_en_7324(self, client: Any, admin_headers: dict[str, str]) -> None:
        """Adding, listing and deleting a custom word round-trips."""
        payload = {
            "word": "crud_sexual_1_en",
            "category": "sexual",
            "severity": 1,
            "language": "en",
        }
        created = client.post(
            "/admin/wordbank/words",
            headers=admin_headers,
            json=payload,
        )
        assert created.status_code in (201, 409)
        response = client.get("/admin/wordbank/words", headers=admin_headers)
        assert response.status_code == 200
        assert any(entry["word"] == "crud_sexual_1_en" for entry in response.json())

    def test_word_crud_sexual_1_zh_CN_7325(
        self, client: Any, admin_headers: dict[str, str]
    ) -> None:
        """Adding, listing and deleting a custom word round-trips."""
        payload = {
            "word": "crud_sexual_1_zh-CN",
            "category": "sexual",
            "severity": 1,
            "language": "zh-CN",
        }
        created = client.post(
            "/admin/wordbank/words",
            headers=admin_headers,
            json=payload,
        )
        assert created.status_code in (201, 409)
        response = client.get("/admin/wordbank/words", headers=admin_headers)
        assert response.status_code == 200
        assert any(entry["word"] == "crud_sexual_1_zh-cn" for entry in response.json())

    def test_word_crud_sexual_1_ru_7326(self, client: Any, admin_headers: dict[str, str]) -> None:
        """Adding, listing and deleting a custom word round-trips."""
        payload = {
            "word": "crud_sexual_1_ru",
            "category": "sexual",
            "severity": 1,
            "language": "ru",
        }
        created = client.post(
            "/admin/wordbank/words",
            headers=admin_headers,
            json=payload,
        )
        assert created.status_code in (201, 409)
        response = client.get("/admin/wordbank/words", headers=admin_headers)
        assert response.status_code == 200
        assert any(entry["word"] == "crud_sexual_1_ru" for entry in response.json())

    def test_word_crud_sexual_1_ar_7327(self, client: Any, admin_headers: dict[str, str]) -> None:
        """Adding, listing and deleting a custom word round-trips."""
        payload = {
            "word": "crud_sexual_1_ar",
            "category": "sexual",
            "severity": 1,
            "language": "ar",
        }
        created = client.post(
            "/admin/wordbank/words",
            headers=admin_headers,
            json=payload,
        )
        assert created.status_code in (201, 409)
        response = client.get("/admin/wordbank/words", headers=admin_headers)
        assert response.status_code == 200
        assert any(entry["word"] == "crud_sexual_1_ar" for entry in response.json())

    def test_word_crud_sexual_1_ja_7328(self, client: Any, admin_headers: dict[str, str]) -> None:
        """Adding, listing and deleting a custom word round-trips."""
        payload = {
            "word": "crud_sexual_1_ja",
            "category": "sexual",
            "severity": 1,
            "language": "ja",
        }
        created = client.post(
            "/admin/wordbank/words",
            headers=admin_headers,
            json=payload,
        )
        assert created.status_code in (201, 409)
        response = client.get("/admin/wordbank/words", headers=admin_headers)
        assert response.status_code == 200
        assert any(entry["word"] == "crud_sexual_1_ja" for entry in response.json())
