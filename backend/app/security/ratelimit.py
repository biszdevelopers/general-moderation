"""Rate limiting facade backed by slowapi.

Uses the ``limits`` library under the hood with in-memory storage by default.
Set ``RATE_LIMIT_STORAGE_URI`` to a ``redis://`` URI to delegate storage to
the C Redis client (hiredis) for multi-worker enforcement.
"""

from __future__ import annotations

import os
from collections.abc import Callable
from typing import Any

from fastapi import Request
from slowapi import Limiter
from slowapi.util import get_remote_address


class RateLimiter:
    """Wraps slowapi and exposes per-endpoint rate limits.

    :param requests: number of allowed requests
    :param period_seconds: the window in seconds
    """

    def __init__(self, requests: int = 100, period_seconds: int = 60) -> None:
        storage_uri: str | None = os.getenv("RATE_LIMIT_STORAGE_URI") or None
        self._limiter: Limiter = Limiter(
            key_func=get_remote_address,
            default_limits=[f"{requests}/{period_seconds}second"],
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
