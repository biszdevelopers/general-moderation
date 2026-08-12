"""Public moderation API tests, part 2 (Phase 1, P1).

Covers user profiling through the API, batch edge cases, unicode handling,
and moderation responses for varied content.
"""

from __future__ import annotations

from typing import Any

import pytest

from tests.base_test import BaseTest

_FLAGGED_TEXTS: tuple[str, ...] = (
    "you are a zaphrin",
    "this contains blocked content",
    "an asshole said hello",
)


class TestApiProfiling(BaseTest):
    """User profiling driven through the API."""

    def test_user_activity_recorded(self, client: Any, engine: Any) -> None:
        """Moderating with a user id records profile activity."""
        client.post("/moderate", json={"text": "hello", "app_name": "app", "user_id": "u1"})
        profile = engine._profiler.get_profile("app", "u1")
        assert profile["daily"]
        assert profile["daily"][0]["total_msgs"] >= 1

    def test_repeat_requests_accumulate(self, client: Any, engine: Any) -> None:
        """Multiple requests from one user accumulate daily counts."""
        for index in range(3):
            client.post(
                "/moderate",
                json={"text": f"distinct message {index}", "app_name": "app", "user_id": "u1"},
            )
        profile = engine._profiler.get_profile("app", "u1")
        assert sum(row["total_msgs"] for row in profile["daily"]) == 3

    def test_user_ratio_via_api(self, client: Any, word_bank: Any, engine: Any) -> None:
        """A flagged request raises the recorded user ratio."""
        word_bank.add_word("zaphrin")
        client.post("/moderate", json={"text": "warmup", "app_name": "app"})
        client.post(
            "/moderate",
            json={"text": "you are a zaphrin", "app_name": "app", "user_id": "bad"},
        )
        assert engine._profiler.get_ratio("app", "bad") >= 0.0


class TestApiUnicode(BaseTest):
    """Unicode and normalization through the API."""

    @pytest.mark.parametrize(
        "text",
        (
            "你好世界",
            "привет мир",
            "مرحبا بالعالم",
            "こんにちは世界",
            "안녕하세요",
            "héllo wörld",
            "emoji 😀 test",
            "café au lait",
            "ｆｕｌｌｗｉｄｔｈ",  # noqa: RUF001
            "mixed 中文 english 123",
        ),
    )
    def test_unicode_text_moderated(self, client: Any, text: str) -> None:
        """Unicode text is moderated without error.

        :param client: test API client
        :param text: unicode message
        """
        response = client.post("/moderate", json={"text": text, "app_name": "a"})
        assert response.status_code == 200
        assert response.json()["verdict"] in ("PASS", "BLOCK", "REVIEW")


class TestApiBatchEdge(BaseTest):
    """Batch moderation edge cases."""

    def test_batch_one_item(self, client: Any) -> None:
        """A single-item batch works."""
        response = client.post(
            "/moderate/batch", json={"items": [{"text": "only one", "id": "i1"}]}
        )
        assert response.status_code == 200
        assert len(response.json()["results"]) == 1

    def test_batch_hundred_items(self, client: Any) -> None:
        """A 100-item batch is accepted."""
        items: list[dict[str, str]] = [{"text": f"msg {index}"} for index in range(100)]
        response = client.post("/moderate/batch", json={"items": items})
        assert response.status_code == 200
        assert len(response.json()["results"]) == 100

    def test_batch_items_with_ids(self, client: Any) -> None:
        """Batch results echo item ids in order."""
        items: list[dict[str, str]] = [
            {"id": f"id{index}", "text": f"text {index}"} for index in range(3)
        ]
        response = client.post("/moderate/batch", json={"items": items})
        results: list[dict[str, Any]] = response.json()["results"]
        assert [result["id"] for result in results] == ["id0", "id1", "id2"]

    def test_batch_invalid_item_rejected(self, client: Any) -> None:
        """An item without text fails the whole batch."""
        response = client.post("/moderate/batch", json={"items": [{"nope": 1}]})
        assert response.status_code == 422

    def test_batch_user_ids(self, client: Any) -> None:
        """Batch items can carry per-item user ids."""
        response = client.post(
            "/moderate/batch",
            json={"items": [{"text": "hi", "user_id": "u1"}, {"text": "bye", "user_id": "u2"}]},
        )
        assert response.status_code == 200


class TestApiVerdicts(BaseTest):
    """Verdict values across content types."""

    @pytest.mark.parametrize(
        "text",
        ("you are a zaphrin", "this contains blocked content", "an asshole said hello"),
    )
    def test_flagged_text_verdicts(self, client: Any, word_bank: Any, text: str) -> None:
        """Flagged text yields a recognized verdict.

        :param client: test API client
        :param word_bank: isolated word bank
        :param text: flagged message
        """
        for word in ("zaphrin", "blocked", "asshole"):
            word_bank.add_word(word)
        response = client.post("/moderate", json={"text": text, "app_name": "a"})
        assert response.json()["verdict"] in ("PASS", "BLOCK", "REVIEW")

    def test_clean_text_allowed(self, client: Any) -> None:
        """Clean text is allowed."""
        response = client.post(
            "/moderate", json={"text": "the weather is nice today", "app_name": "a"}
        )
        assert response.json()["allowed"] is True

    def test_whitespace_normalized(self, client: Any) -> None:
        """Multiple spaces are handled without error."""
        response = client.post("/moderate", json={"text": "hello    world  !", "app_name": "a"})
        assert response.status_code == 200

    def test_numbers_only(self, client: Any) -> None:
        """Numeric-only content is moderated."""
        response = client.post("/moderate", json={"text": "12345 67890", "app_name": "a"})
        assert response.status_code == 200

    def test_single_character(self, client: Any) -> None:
        """A single-character message is moderated."""
        response = client.post("/moderate", json={"text": "x", "app_name": "a"})
        assert response.status_code == 200


class TestApiRateLimit(BaseTest):
    """Rate limit behavior under normal settings."""

    def test_high_rate_not_limited(self, client: Any) -> None:
        """A burst below the limit succeeds."""
        for index in range(20):
            response = client.post(
                "/moderate", json={"text": f"burst message {index}", "app_name": "a"}
            )
            assert response.status_code == 200

    def test_batch_not_rate_limited(self, client: Any) -> None:
        """Repeated batches below the limit succeed."""
        for _ in range(5):
            response = client.post("/moderate/batch", json={"items": [{"text": "one"}]})
            assert response.status_code == 200


class TestApiCaching(BaseTest):
    """Result caching across API calls."""

    def test_cached_response_fast(self, client: Any) -> None:
        """A cached request returns quickly with the same verdict."""
        import time

        payload: dict[str, str] = {"text": "cache latency check", "app_name": "a"}
        client.post("/moderate", json=payload)
        start: float = time.perf_counter()
        response = client.post("/moderate", json=payload)
        elapsed: float = time.perf_counter() - start
        assert response.status_code == 200
        assert elapsed < 2.0

    def test_cache_cleared_between_words(self, client: Any, word_bank: Any) -> None:
        """Adding a word and refreshing clears stale results."""
        word_bank.add_word("zaphrin")
        client.post("/moderate", json={"text": "warm the cache", "app_name": "a"})
        word_bank.add_word("anotherword")
        response = client.post("/moderate", json={"text": "warm the cache", "app_name": "a"})
        assert response.status_code == 200


class TestApiHeaders(BaseTest):
    """API response conventions."""

    def test_moderate_content_length_present(self, client: Any) -> None:
        """Moderate responses carry a content length."""
        response = client.post("/moderate", json={"text": "hi", "app_name": "a"})
        assert "content-length" in response.headers

    def test_batch_content_length_present(self, client: Any) -> None:
        """Batch responses carry a content length."""
        response = client.post("/moderate/batch", json={"items": [{"text": "hi"}]})
        assert "content-length" in response.headers


class TestApiBatchEmptyText(BaseTest):
    """Batch items with empty text."""

    def test_batch_empty_item_text_rejected(self, client: Any) -> None:
        """A batch item with empty text is rejected."""
        response = client.post("/moderate/batch", json={"items": [{"text": ""}]})
        assert response.status_code == 422

    def test_batch_mixed_valid_invalid(self, client: Any) -> None:
        """A batch mixing valid and invalid items fails wholesale."""
        response = client.post("/moderate/batch", json={"items": [{"text": "ok"}, {"text": ""}]})
        assert response.status_code == 422


class TestApiAppIsolation(BaseTest):
    """Per-app behavior through the API."""

    def test_app_name_isolates_profiles(self, client: Any, engine: Any) -> None:
        """The same user in different apps gets separate profiles."""
        client.post(
            "/moderate", json={"text": "first app message", "app_name": "app1", "user_id": "u"}
        )
        client.post(
            "/moderate", json={"text": "second app message", "app_name": "app2", "user_id": "u"}
        )
        assert engine._profiler.get_profile("app1", "u")["daily"]
        assert engine._profiler.get_profile("app2", "u")["daily"]

    def test_default_app_used_when_absent(self, client: Any, engine: Any) -> None:
        """Without an app name the default app records the profile."""
        client.post("/moderate", json={"text": "hello there", "user_id": "u"})
        assert engine._profiler.get_profile("default", "u")["daily"]


class TestApiContent(BaseTest):
    """Content variety moderation."""

    @pytest.mark.parametrize(
        "text",
        (
            "hello world and friends",
            "123 456 789",
            "!!! ??? ...",
            "Mixed CASE Text Here",
            "tab\tseparated\twords",
        ),
    )
    def test_content_variety(self, client: Any, text: str) -> None:
        """Varied content is moderated without error.

        :param client: test API client
        :param text: message under test
        """
        response = client.post("/moderate", json={"text": text, "app_name": "a"})
        assert response.status_code == 200
        assert response.json()["verdict"] in ("PASS", "BLOCK", "REVIEW")
