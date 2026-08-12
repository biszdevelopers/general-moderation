"""Public moderation API tests, part 1 (Phase 1, P0).

Covers the health endpoint, single-message moderation, validation errors,
and response shape through the wired FastAPI app.
"""

from __future__ import annotations

from typing import Any

import pytest

from tests.base_test import BaseTest

_CLEAN_TEXTS: tuple[str, ...] = (
    "the weather is nice today",
    "coffee is ready",
    "let us begin the meeting",
    "welcome to the team",
    "the report is on the desk",
    "thanks for your help",
    "good night everyone",
    "hello world",
    "total ordinary content",
    "this text contains no flagged terms",
)


class TestHealth(BaseTest):
    """Health endpoint."""

    def test_health_ok(self, client: Any) -> None:
        """GET /health returns 200."""
        response = client.get("/health")
        assert response.status_code == 200

    def test_health_status(self, client: Any) -> None:
        """The health payload reports healthy."""
        response = client.get("/health")
        assert response.json()["status"] == "healthy"

    def test_health_method_only(self, client: Any) -> None:
        """POST /health is not allowed."""
        response = client.post("/health")
        assert response.status_code == 405


class TestModerate(BaseTest):
    """Single message moderation."""

    @pytest.mark.parametrize("text", _CLEAN_TEXTS)
    def test_clean_text_passes(self, client: Any, text: str) -> None:
        """Clean text returns a PASS verdict.

        :param client: test API client
        :param text: clean message
        """
        response = client.post("/moderate", json={"text": text})
        assert response.status_code == 200
        assert response.json()["verdict"] == "PASS"

    @pytest.mark.parametrize(
        "text",
        (
            "you are a zaphrin",
            "blocked content here",
            "this is an asshole statement",
        ),
    )
    def test_flagged_text_response(self, client: Any, word_bank: Any, text: str) -> None:
        """Flagged text returns a structured response.

        :param client: test API client
        :param word_bank: isolated word bank
        :param text: message under test
        """
        word_bank.add_word("zaphrin")
        word_bank.add_word("blocked")
        word_bank.add_word("asshole")
        response = client.post("/moderate", json={"text": text, "app_name": "a"})
        assert response.status_code == 200
        body: dict[str, Any] = response.json()
        assert body["verdict"] in ("PASS", "BLOCK", "REVIEW")
        assert isinstance(body["suspicionScore"], (int, float))
        assert isinstance(body["latencyMs"], (int, float))
        assert isinstance(body["detectorChain"], list)

    def test_response_shape(self, client: Any) -> None:
        """The response exposes the documented fields."""
        response = client.post("/moderate", json={"text": "hello", "app_name": "a"})
        body: dict[str, Any] = response.json()
        for field in (
            "id",
            "verdict",
            "allowed",
            "levelUsed",
            "aiTriggered",
            "suspicionScore",
            "reasons",
            "reason",
            "matchedWords",
            "matchedWord",
            "matchedLanguage",
            "confidenceScore",
            "latencyMs",
            "detectorChain",
        ):
            assert field in body

    def test_id_echoed(self, client: Any) -> None:
        """The caller id is echoed back."""
        response = client.post("/moderate", json={"id": "abc123", "text": "hello"})
        assert response.json()["id"] == "abc123"

    def test_user_id_accepted(self, client: Any) -> None:
        """A user id is accepted without error."""
        response = client.post(
            "/moderate", json={"text": "hello", "app_name": "a", "user_id": "u1"}
        )
        assert response.status_code == 200

    def test_app_name_defaulted(self, client: Any) -> None:
        """An absent app name is handled."""
        response = client.post("/moderate", json={"text": "hello"})
        assert response.status_code == 200


class TestModerateValidation(BaseTest):
    """Input validation."""

    @pytest.mark.parametrize("payload", ({"text": ""}, {"text": None}, {}, {"nope": 1}))
    def test_invalid_payload_rejected(self, client: Any, payload: dict[str, object]) -> None:
        """Missing or empty text is rejected with 422.

        :param client: test API client
        :param payload: invalid request body
        """
        response = client.post("/moderate", json=payload)
        assert response.status_code == 422

    def test_too_long_text_rejected(self, client: Any) -> None:
        """Text over the 8192 limit is rejected."""
        long_text: str = "x" * 9000
        response = client.post("/moderate", json={"text": long_text})
        assert response.status_code == 422

    def test_max_length_accepted(self, client: Any) -> None:
        """Text at exactly the limit is accepted."""
        response = client.post("/moderate", json={"text": "x" * 8192})
        assert response.status_code == 200

    def test_non_string_text_rejected(self, client: Any) -> None:
        """Non-string text is rejected."""
        response = client.post("/moderate", json={"text": 12345})
        assert response.status_code == 422


class TestModerateBatch(BaseTest):
    """Batch moderation."""

    def test_batch_ok(self, client: Any) -> None:
        """A batch returns 200 with per-item results."""
        response = client.post("/moderate/batch", json={"items": [{"text": "hi"}, {"text": "bye"}]})
        assert response.status_code == 200
        assert len(response.json()["results"]) == 2

    def test_batch_total_latency(self, client: Any) -> None:
        """The batch reports total latency."""
        response = client.post("/moderate/batch", json={"items": [{"text": "hi"}]})
        assert response.json()["totalLatencyMs"] >= 0.0

    def test_batch_empty_rejected(self, client: Any) -> None:
        """An empty items list is rejected."""
        response = client.post("/moderate/batch", json={"items": []})
        assert response.status_code == 422

    def test_batch_over_limit_rejected(self, client: Any) -> None:
        """More than 100 items is rejected."""
        items: list[dict[str, str]] = [{"text": "hi"} for _ in range(101)]
        response = client.post("/moderate/batch", json={"items": items})
        assert response.status_code == 422

    def test_batch_missing_items_rejected(self, client: Any) -> None:
        """A missing items key is rejected."""
        response = client.post("/moderate/batch", json={})
        assert response.status_code == 422

    def test_batch_result_shape(self, client: Any) -> None:
        """Every batch result carries the response fields."""
        response = client.post("/moderate/batch", json={"items": [{"text": "hello", "id": "b1"}]})
        result: dict[str, Any] = response.json()["results"][0]
        assert result["id"] == "b1"
        assert result["verdict"] in ("PASS", "BLOCK", "REVIEW")


class TestModerateIntegration(BaseTest):
    """Engine behaviors surfaced through the API."""

    def test_blocked_word_returns_block(self, client: Any, word_bank: Any) -> None:
        """A custom-word match yields a BLOCK verdict."""
        word_bank.add_word("zaphrin")
        client.post("/moderate", json={"text": "warmup", "app_name": "a"})
        response = client.post("/moderate", json={"text": "you are a zaphrin", "app_name": "a"})
        body: dict[str, Any] = response.json()
        assert body["verdict"] in ("BLOCK", "REVIEW")
        assert body["allowed"] == (body["verdict"] != "BLOCK")

    def test_repeated_request_cached(self, client: Any) -> None:
        """Repeated identical requests return the same verdict."""
        payload: dict[str, str] = {"text": "cache me please", "app_name": "a"}
        first: dict[str, Any] = client.post("/moderate", json=payload).json()
        second: dict[str, Any] = client.post("/moderate", json=payload).json()
        assert first["verdict"] == second["verdict"]

    def test_latency_reported_positive(self, client: Any) -> None:
        """Latency is a non-negative number."""
        body: dict[str, Any] = client.post("/moderate", json={"text": "hi"}).json()
        assert body["latencyMs"] >= 0.0

    def test_ai_never_triggered_without_model(self, client: Any) -> None:
        """Without a loaded model aiTriggered stays false."""
        body: dict[str, Any] = client.post(
            "/moderate", json={"text": "the weather is nice", "app_name": "a"}
        ).json()
        assert body["aiTriggered"] is False

    def test_level_used_one_for_clean(self, client: Any) -> None:
        """Clean text resolves at level one."""
        body: dict[str, Any] = client.post(
            "/moderate", json={"text": "ordinary message", "app_name": "a"}
        ).json()
        assert body["levelUsed"] == 1

    def test_content_type_application_json(self, client: Any) -> None:
        """The moderate endpoint responds as JSON."""
        response = client.post("/moderate", json={"text": "hi"})
        assert response.headers["content-type"].startswith("application/json")

    def test_root_returns_service_status(self, client: Any) -> None:
        """The root endpoint reports service status without a build."""
        response = client.get("/")
        assert response.status_code == 200
        body: dict[str, Any] = response.json()
        assert "service" in body
        assert body["status"] == "ok"
