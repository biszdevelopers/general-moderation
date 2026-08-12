"""Admin API tests (Phase 1, P0/P1).

Covers word bank CRUD, authentication, app config policies, settings,
logs, health, and stats through the wired admin router.
"""

from __future__ import annotations

from typing import Any

import pytest

from tests.base_test import BaseTest


class TestAdminAuth(BaseTest):
    """Admin authentication."""

    def test_missing_key_rejected(self, client: Any) -> None:
        """Admin endpoints reject requests without a key."""
        response = client.get("/admin/wordbank/stats")
        assert response.status_code == 401

    def test_wrong_key_rejected(self, client: Any) -> None:
        """A wrong API key is rejected."""
        response = client.get("/admin/wordbank/stats", headers={"X-API-Key": "wrong"})
        assert response.status_code == 401

    def test_valid_key_accepted(self, client: Any, admin_headers: dict[str, str]) -> None:
        """The configured key grants access."""
        response = client.get("/admin/wordbank/stats", headers=admin_headers)
        assert response.status_code == 200

    def test_public_endpoint_no_auth(self, client: Any) -> None:
        """Public endpoints do not require the admin key."""
        response = client.get("/health")
        assert response.status_code == 200


class TestWordBankAdmin(BaseTest):
    """Custom word CRUD."""

    @pytest.mark.parametrize(
        ("word", "severity", "category"),
        (
            ("blockme", 5, "other"),
            ("hatespeech", 8, "hate_speech"),
            ("violenceword", 9, "violence"),
            ("politicalword", 3, "political"),
            ("sexualword", 7, "sexual"),
        ),
    )
    def test_add_word(
        self,
        client: Any,
        admin_headers: dict[str, str],
        word: str,
        severity: int,
        category: str,
    ) -> None:
        """Adding a word returns 201 with the stored record.

        :param client: test API client
        :param admin_headers: admin auth headers
        :param word: the term to add
        :param severity: severity score
        :param category: semantic bucket
        """
        response = client.post(
            "/admin/wordbank/words",
            headers=admin_headers,
            json={"word": word, "severity": severity, "category": category},
        )
        assert response.status_code == 201
        body: dict[str, Any] = response.json()
        assert body["word"] == word
        assert body["severity"] == severity

    def test_add_duplicate_rejected(self, client: Any, admin_headers: dict[str, str]) -> None:
        """Adding an existing word returns 409."""
        client.post("/admin/wordbank/words", headers=admin_headers, json={"word": "dupword"})
        response = client.post(
            "/admin/wordbank/words", headers=admin_headers, json={"word": "dupword"}
        )
        assert response.status_code == 409

    def test_list_words(self, client: Any, admin_headers: dict[str, str]) -> None:
        """Listing returns the stored words."""
        client.post("/admin/wordbank/words", headers=admin_headers, json={"word": "listme"})
        response = client.get("/admin/wordbank/words", headers=admin_headers)
        assert response.status_code == 200
        assert any(entry["word"] == "listme" for entry in response.json())

    def test_list_search_filter(self, client: Any, admin_headers: dict[str, str]) -> None:
        """Search filters the word list."""
        client.post("/admin/wordbank/words", headers=admin_headers, json={"word": "needleword"})
        response = client.get(
            "/admin/wordbank/words", headers=admin_headers, params={"search": "needle"}
        )
        words: list[dict[str, Any]] = response.json()
        assert words and all("needle" in entry["word"] for entry in words)

    def test_update_word(self, client: Any, admin_headers: dict[str, str]) -> None:
        """Updating a word changes its severity."""
        created: dict[str, Any] = client.post(
            "/admin/wordbank/words", headers=admin_headers, json={"word": "updateme"}
        ).json()
        response = client.put(
            f"/admin/wordbank/words/{created['id']}",
            headers=admin_headers,
            json={"severity": 9},
        )
        assert response.status_code == 200
        assert response.json()["severity"] == 9

    def test_update_missing_rejected(self, client: Any, admin_headers: dict[str, str]) -> None:
        """Updating a missing word returns 404."""
        response = client.put(
            "/admin/wordbank/words/99999", headers=admin_headers, json={"severity": 9}
        )
        assert response.status_code == 404

    def test_delete_word(self, client: Any, admin_headers: dict[str, str]) -> None:
        """Deleting a word returns removed true."""
        created: dict[str, Any] = client.post(
            "/admin/wordbank/words", headers=admin_headers, json={"word": "deleteme"}
        ).json()
        response = client.delete(
            f"/admin/wordbank/words?word_id={created['id']}", headers=admin_headers
        )
        assert response.status_code == 200
        assert response.json()["removed"] is True

    def test_delete_missing_returns_false(self, client: Any, admin_headers: dict[str, str]) -> None:
        """Deleting a missing word returns removed false."""
        response = client.delete("/admin/wordbank/words?word_id=99999", headers=admin_headers)
        assert response.json()["removed"] is False

    def test_bulk_import(self, client: Any, admin_headers: dict[str, str]) -> None:
        """Bulk import reports the imported count."""
        response = client.post(
            "/admin/wordbank/import",
            headers=admin_headers,
            json={"items": [{"word": "imp1"}, {"word": "imp2"}, {"word": "imp3"}]},
        )
        assert response.status_code == 200
        assert response.json()["imported"] == 3

    def test_import_skips_duplicates(self, client: Any, admin_headers: dict[str, str]) -> None:
        """Duplicate words in an import are skipped."""
        client.post("/admin/wordbank/words", headers=admin_headers, json={"word": "exists"})
        response = client.post(
            "/admin/wordbank/import",
            headers=admin_headers,
            json={"items": [{"word": "exists"}, {"word": "fresh"}]},
        )
        assert response.json()["imported"] == 1

    def test_wordbank_export(self, client: Any, admin_headers: dict[str, str]) -> None:
        """Exporting the word bank returns every word."""
        client.post("/admin/wordbank/words", headers=admin_headers, json={"word": "exportme"})
        response = client.get("/admin/wordbank/export", headers=admin_headers)
        assert response.status_code == 200
        assert any(entry["word"] == "exportme" for entry in response.json())


class TestAdminWordbankStats(BaseTest):
    """Word bank statistics endpoints."""

    def test_stats_shape(self, client: Any, admin_headers: dict[str, str]) -> None:
        """Stats expose the documented fields."""
        response = client.get("/admin/wordbank/stats", headers=admin_headers)
        body: dict[str, Any] = response.json()
        for field in ("totalWords", "customWords", "baseWords", "languages", "categories"):
            assert field in body

    def test_stats_after_add(self, client: Any, admin_headers: dict[str, str]) -> None:
        """Adding a word increases the custom count."""
        client.post("/admin/wordbank/words", headers=admin_headers, json={"word": "statword"})
        body: dict[str, Any] = client.get("/admin/wordbank/stats", headers=admin_headers).json()
        assert body["customWords"] >= 1

    def test_languages_endpoint(self, client: Any, admin_headers: dict[str, str]) -> None:
        """The languages endpoint returns a list."""
        response = client.get("/admin/wordbank/languages", headers=admin_headers)
        assert response.status_code == 200
        assert isinstance(response.json(), list)

    def test_categories_endpoint(self, client: Any, admin_headers: dict[str, str]) -> None:
        """The categories endpoint returns a list."""
        response = client.get("/admin/wordbank/categories", headers=admin_headers)
        assert response.status_code == 200
        assert isinstance(response.json(), list)


class TestAdminHealth(BaseTest):
    """Admin health report."""

    def test_health_status(self, client: Any, admin_headers: dict[str, str]) -> None:
        """The admin health report reports ok."""
        response = client.get("/admin/health", headers=admin_headers)
        assert response.json()["status"] == "ok"

    def test_health_detectors(self, client: Any, admin_headers: dict[str, str]) -> None:
        """The health report lists detectors."""
        response = client.get("/admin/health", headers=admin_headers)
        assert isinstance(response.json()["detectors"], list)

    def test_health_word_count(self, client: Any, admin_headers: dict[str, str]) -> None:
        """The health report includes word bank stats."""
        response = client.get("/admin/health", headers=admin_headers)
        assert "wordCount" in response.json()

    def test_health_uptime(self, client: Any, admin_headers: dict[str, str]) -> None:
        """The health report includes uptime."""
        response = client.get("/admin/health", headers=admin_headers)
        assert response.json()["uptimeSeconds"] >= 0.0


class TestAdminAppConfig(BaseTest):
    """Per-app trigger policies."""

    def test_list_app_configs(self, client: Any, admin_headers: dict[str, str]) -> None:
        """Listing app configs returns a list."""
        response = client.get("/admin/app-config", headers=admin_headers)
        assert response.status_code == 200
        assert isinstance(response.json()["apps"], list)

    def test_set_app_config(self, client: Any, admin_headers: dict[str, str]) -> None:
        """Setting an app config stores the policy."""
        response = client.post(
            "/admin/app-config",
            headers=admin_headers,
            json={"app_name": "game", "score_threshold": 60},
        )
        assert response.status_code == 200
        assert response.json()["score_threshold"] == 60

    def test_get_app_config(self, client: Any, admin_headers: dict[str, str]) -> None:
        """Getting an app config returns its policy."""
        client.post(
            "/admin/app-config",
            headers=admin_headers,
            json={"app_name": "chat", "score_threshold": 40},
        )
        response = client.get("/admin/app-config/chat", headers=admin_headers)
        assert response.json()["score_threshold"] == 40

    def test_get_unknown_app_defaults(self, client: Any, admin_headers: dict[str, str]) -> None:
        """Unknown apps fall back to defaults."""
        response = client.get("/admin/app-config/ghost", headers=admin_headers)
        assert response.json()["score_threshold"] == 50

    def test_empty_app_name_rejected(self, client: Any, admin_headers: dict[str, str]) -> None:
        """An empty app name in the path is rejected."""
        response = client.get("/admin/app-config/%20", headers=admin_headers)
        assert response.status_code == 400

    def test_and_logic_stored(self, client: Any, admin_headers: dict[str, str]) -> None:
        """AND logic is stored and returned."""
        response = client.post(
            "/admin/app-config",
            headers=admin_headers,
            json={"app_name": "strict", "logic_type": "and"},
        )
        assert response.json()["logic_type"] == "and"


class TestAdminSettings(BaseTest):
    """Settings endpoints."""

    def test_get_settings(self, client: Any, admin_headers: dict[str, str]) -> None:
        """GET /admin/settings returns the catalog."""
        response = client.get("/admin/settings", headers=admin_headers)
        assert response.status_code == 200
        assert isinstance(response.json()["settings"], list)

    def test_post_settings(self, client: Any, admin_headers: dict[str, str]) -> None:
        """POST /admin/settings updates a weight."""
        response = client.post(
            "/admin/settings",
            headers=admin_headers,
            json={"settings": {"WEIGHT_DETECTOR_AHO": 35}},
        )
        assert response.status_code == 200
        assert "WEIGHT_DETECTOR_AHO" in response.json()["updated"]

    def test_post_invalid_settings_rejected(
        self, client: Any, admin_headers: dict[str, str]
    ) -> None:
        """Invalid settings values return 400."""
        response = client.post(
            "/admin/settings",
            headers=admin_headers,
            json={"settings": {"WEIGHT_DETECTOR_AHO": "bogus"}},
        )
        assert response.status_code == 400

    def test_post_secret_rejected(self, client: Any, admin_headers: dict[str, str]) -> None:
        """Read-only secrets cannot be updated."""
        response = client.post(
            "/admin/settings",
            headers=admin_headers,
            json={"settings": {"ADMIN_API_KEY": "new"}},
        )
        assert response.status_code == 400


class TestAdminLogs(BaseTest):
    """Log management endpoints."""

    def test_list_logs(self, client: Any, admin_headers: dict[str, str]) -> None:
        """Listing logs returns an array."""
        response = client.get("/admin/logs", headers=admin_headers)
        assert response.status_code == 200
        assert isinstance(response.json(), list)

    def test_invalid_log_name_rejected(self, client: Any, admin_headers: dict[str, str]) -> None:
        """An invalid log filename returns 400."""
        response = client.get("/admin/logs/..%2F..%2Fetc%2Fpasswd", headers=admin_headers)
        assert response.status_code in (400, 404)

    def test_reload_endpoint(self, client: Any, admin_headers: dict[str, str]) -> None:
        """Reloading the word bank returns reloaded."""
        response = client.post("/admin/reload", headers=admin_headers)
        assert response.status_code == 200
        assert response.json()["status"] == "reloaded"


class TestAdminStatsEndpoint(BaseTest):
    """Dashboard stats."""

    def test_stats_endpoint(self, client: Any, admin_headers: dict[str, str]) -> None:
        """GET /admin/stats returns dashboard data."""
        response = client.get("/admin/stats", headers=admin_headers)
        assert response.status_code == 200
        body: dict[str, Any] = response.json()
        assert "metrics" in body
        assert "profiling" in body
        assert "word_bank" in body

    def test_spot_check_empty(self, client: Any, admin_headers: dict[str, str]) -> None:
        """Spot check returns an empty sample with no logs."""
        response = client.get("/admin/spot-check", headers=admin_headers)
        assert response.status_code == 200
        assert "sample" in response.json()


class TestAdminWordValidation(BaseTest):
    """Word payload validation."""

    def test_add_empty_word_rejected(self, client: Any, admin_headers: dict[str, str]) -> None:
        """An empty word is rejected with 422."""
        response = client.post("/admin/wordbank/words", headers=admin_headers, json={"word": ""})
        assert response.status_code == 422

    def test_add_too_long_word_rejected(self, client: Any, admin_headers: dict[str, str]) -> None:
        """An over-long word is rejected."""
        response = client.post(
            "/admin/wordbank/words", headers=admin_headers, json={"word": "x" * 300}
        )
        assert response.status_code == 422

    def test_add_negative_severity_rejected(
        self, client: Any, admin_headers: dict[str, str]
    ) -> None:
        """A negative severity is rejected."""
        response = client.post(
            "/admin/wordbank/words", headers=admin_headers, json={"word": "sev", "severity": -1}
        )
        assert response.status_code == 422

    def test_add_high_severity_rejected(self, client: Any, admin_headers: dict[str, str]) -> None:
        """A severity over ten is rejected."""
        response = client.post(
            "/admin/wordbank/words", headers=admin_headers, json={"word": "sev", "severity": 11}
        )
        assert response.status_code == 422

    def test_import_empty_items_rejected(self, client: Any, admin_headers: dict[str, str]) -> None:
        """An import with no items is rejected."""
        response = client.post("/admin/wordbank/import", headers=admin_headers, json={"items": []})
        assert response.status_code == 422

    def test_unicode_word_accepted(self, client: Any, admin_headers: dict[str, str]) -> None:
        """A unicode word is accepted and normalized."""
        response = client.post(
            "/admin/wordbank/words", headers=admin_headers, json={"word": "敏感词"}
        )
        assert response.status_code == 201
        assert response.json()["word"] == "敏感词"

    def test_import_over_limit_rejected(self, client: Any, admin_headers: dict[str, str]) -> None:
        """An import over 1000 items is rejected."""
        items: list[dict[str, str]] = [{"word": f"w{index}"} for index in range(1001)]
        response = client.post(
            "/admin/wordbank/import", headers=admin_headers, json={"items": items}
        )
        assert response.status_code == 422

    def test_word_id_invalid_rejected(self, client: Any, admin_headers: dict[str, str]) -> None:
        """A non-positive word id is rejected."""
        response = client.delete("/admin/wordbank/words?word_id=0", headers=admin_headers)
        assert response.status_code == 422
