"""Unit tests for the cross-worker cache invalidator."""

from __future__ import annotations

from unittest.mock import MagicMock, patch

from app.cache.invalidator import CacheInvalidator


def test_disabled_without_redis() -> None:
    """Without a URI the bus is disabled and never connects."""
    invalidator: CacheInvalidator = CacheInvalidator(redis_uri="")
    assert not invalidator.enabled()
    invalidator.start()
    invalidator.publish()
    invalidator.stop()


def test_disabled_when_redis_import_fails() -> None:
    """A missing redis package disables the bus without raising."""
    with patch.dict("sys.modules", {"redis": None}):
        with patch("builtins.__import__", side_effect=ImportError("no redis")):
            invalidator: CacheInvalidator = CacheInvalidator(redis_uri="redis://localhost:6379/0")
    assert not invalidator.enabled()


def test_enabled_publishes_and_invalidates() -> None:
    """A connected bus publishes clears and the callback fires on events."""
    client: MagicMock = MagicMock()
    pubsub: MagicMock = MagicMock()
    client.pubsub.return_value = pubsub
    pubsub.listen.return_value = [
        {"type": "message", "data": b"clear"},
        {"type": "subscribe", "data": 1},
    ]
    calls: list[str] = []

    def invalidate() -> None:
        calls.append("cleared")

    fake_redis = MagicMock()
    fake_redis.Redis.from_url.return_value = client
    with patch.dict("sys.modules", {"redis": fake_redis}):
        invalidator: CacheInvalidator = CacheInvalidator(
            redis_uri="redis://localhost:6379/0", on_invalidate=invalidate
        )
    assert invalidator.enabled()
    invalidator.start()
    invalidator._thread.join(timeout=2.0)
    assert calls == ["cleared"]
    invalidator.publish()
    client.publish.assert_called_once()
    invalidator.stop()


def test_stop_is_idempotent() -> None:
    """Stopping an unstarted or disabled bus is safe."""
    invalidator: CacheInvalidator = CacheInvalidator(redis_uri="")
    invalidator.stop()
    invalidator.stop()
