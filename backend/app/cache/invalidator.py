"""Cross-worker cache invalidation over Redis pub/sub.

Each Gunicorn worker keeps its own in-memory result cache. A settings,
app-config, or phrase edit clears the cache in the worker that made the
change, but the other workers keep serving stale verdicts until their TTL
expires. This module publishes an invalidation event whenever a worker
clears its cache; every worker subscribes and drops its own cache too.

Fail-open by design: without ``REDIS_URI`` set or the ``redis`` package
installed the bus is a no-op, matching the service's stance that optional
infrastructure never breaks moderation.
"""

from __future__ import annotations

import logging
import threading
from collections.abc import Callable
from typing import Any

_LOGGER: logging.Logger = logging.getLogger(__name__)

_DEFAULT_CHANNEL: str = "moderation:cache:invalidate"


class CacheInvalidator:
    """Optional Redis pub/sub bus that broadcasts cache clears.

    :param redis_uri: ``redis://`` connection string, or empty to disable
    :param channel: pub/sub channel name
    :param on_invalidate: callback invoked when another worker clears its cache
    """

    def __init__(
        self,
        redis_uri: str = "",
        channel: str = _DEFAULT_CHANNEL,
        on_invalidate: Callable[[], None] | None = None,
    ) -> None:
        self._redis_uri: str = redis_uri or ""
        self._channel: str = channel
        self._on_invalidate: Callable[[], None] | None = on_invalidate
        self._client: Any = None
        self._pubsub: Any = None
        self._thread: threading.Thread | None = None
        self._stop: threading.Event = threading.Event()
        self._lock: threading.Lock = threading.Lock()
        if self._redis_uri:
            self._connect()

    def _connect(self) -> None:
        """Create the Redis client, if the package is available."""
        try:
            import redis  # type: ignore[import-not-found]

            self._client = redis.Redis.from_url(self._redis_uri)
            self._client.ping()
        except Exception as exc:
            self._client = None
            _LOGGER.warning("Cache invalidation bus disabled: %s", exc)

    def enabled(self) -> bool:
        """Return whether the bus is actively connected."""
        return self._client is not None

    def start(self) -> None:
        """Begin listening for invalidation events from other workers.

        Runs a daemon subscriber thread; the bus is a no-op when Redis is
        unavailable or no callback was supplied.
        """
        if not self.enabled() or self._on_invalidate is None or self._thread is not None:
            return
        self._stop.clear()
        self._thread = threading.Thread(target=self._listen, name="cache-invalidator", daemon=True)
        self._thread.start()

    def _listen(self) -> None:
        """Subscribe and clear the local cache on every published event."""
        try:
            self._pubsub = self._client.pubsub()
            self._pubsub.subscribe(self._channel)
            for message in self._pubsub.listen():
                if self._stop.is_set():
                    break
                if message.get("type") == "message":
                    self._on_invalidate()
        except Exception as exc:
            _LOGGER.warning("Cache invalidation listener stopped: %s", exc)

    def publish(self) -> None:
        """Broadcast a cache clear to every other worker."""
        if not self.enabled():
            return
        with self._lock:
            try:
                self._client.publish(self._channel, "clear")
            except Exception as exc:
                _LOGGER.warning("Cache invalidation publish failed: %s", exc)

    def stop(self) -> None:
        """Stop the listener thread and close the connection."""
        self._stop.set()
        if self._pubsub is not None:
            try:
                self._pubsub.unsubscribe(self._channel)
                self._pubsub.close()
            except Exception:
                pass
        if self._thread is not None:
            self._thread.join(timeout=2.0)
            self._thread = None
        if self._client is not None:
            try:
                self._client.close()
            except Exception:
                pass
