"""Rate limiting facade backed by slowapi.

Only endpoints decorated with ``@RateLimiter.limit()`` (the public moderation
routes) are rate limited. Admin and test routes are intentionally exempt: they
are already guarded by the admin API key and their auto-refreshing dashboards
must not consume a shared per-IP budget.

Set ``RATE_LIMIT_STORAGE_URI`` to a ``redis://`` URI to delegate storage to
the C Redis client (hiredis) for multi-worker enforcement.
"""

from __future__ import annotations

from collections.abc import Callable
from typing import Any

from fastapi import Request
from slowapi import Limiter
from slowapi.util import get_remote_address


class RateLimiter:
    """Wraps slowapi and exposes per-endpoint rate limits.

    :param requests: number of allowed requests
    :param period_seconds: the window in seconds
    :param redis_uri: optional ``redis://`` URI for multi-worker storage
    """

    def __init__(
        self, requests: int = 100, period_seconds: int = 60, redis_uri: str | None = None
    ) -> None:
        storage_uri: str | None = redis_uri or None
        self._limiter: Limiter = Limiter(
            key_func=get_remote_address,
            default_limits=[],
            storage_uri=storage_uri,
        )
        self._requests: int = requests
        self._period_seconds: int = period_seconds

    @property
    def limiter(self) -> Limiter:
        """Return the underlying slowapi limiter.

        :return: the slowapi Limiter instance
        """
        return self._limiter

    def limit(
        self, requests: int | None = None, period_seconds: int | None = None
    ) -> Callable[[Any], Any]:
        """Return a decorator applying a rate limit to an endpoint.

        :param requests: overrides the default request count
        :param period_seconds: overrides the default window
        :return: the slowapi limit decorator
        """
        count: int = requests or self._requests
        period: int = period_seconds or self._period_seconds
        return self._limiter.limit(f"{count}/{period}second")


def rate_limit_key(request: Request) -> str:
    """Compute a stable rate limit key for a request.

    Falls back to the remote address when no client identifier is present.

    :param request: the incoming request
    :return: the rate limit key
    """
    return get_remote_address(request)
