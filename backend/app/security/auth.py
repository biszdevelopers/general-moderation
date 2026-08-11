"""Authentication dependency.

API keys are compared with ``hmac.compare_digest``, a constant-time
comparison backed by C, to prevent timing attacks on the admin endpoints.
"""

from __future__ import annotations

from hmac import compare_digest

from fastapi import Header, HTTPException, status


class RequireAdminApiKey:
    """FastAPI dependency validating the static admin API key.

    :param expected_key: the configured ADMIN_API_KEY
    """

    def __init__(self, expected_key: str) -> None:
        self._expected_key: str = expected_key

    def __call__(self, x_api_key: str = Header(default="")) -> None:
        """Reject the request when the key does not match.

        :param x_api_key: the X-API-Key header value
        :raises HTTPException: 401 when the key is invalid
        """
        if not compare_digest(x_api_key, self._expected_key):
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Invalid or missing API key",
            )


class RequireWebUiApiKey:
    """FastAPI dependency validating the web UI API key.

    :param expected_key: the configured WEBUI_API_KEY
    """

    def __init__(self, expected_key: str) -> None:
        self._expected_key: str = expected_key

    def __call__(self, x_api_key: str = Header(default="")) -> None:
        """Reject the request when the web UI key does not match.

        :param x_api_key: the X-API-Key header value
        :raises HTTPException: 401 when the key is invalid
        """
        if not compare_digest(x_api_key, self._expected_key):
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Invalid or missing web UI API key",
            )
