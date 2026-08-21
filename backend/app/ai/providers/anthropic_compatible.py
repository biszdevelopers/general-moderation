"""Anthropic-compatible messages provider.

Works against the official Anthropic API and any gateway speaking the same
``/v1/messages`` schema.
"""

from __future__ import annotations

from typing import Any

from app.ai.providers.remote import RemoteProvider

_ANTHROPIC_VERSION: str = "2023-06-01"


class AnthropicCompatibleProvider(RemoteProvider):
    """Classifies text through an Anthropic-compatible messages API."""

    @property
    def name(self) -> str:
        """Return the provider identifier."""
        return "anthropic_compatible"

    def _headers(self) -> dict[str, str]:
        """Build request headers with the API key and version pin."""
        return {
            "Content-Type": "application/json",
            "x-api-key": self._config("ANTHROPIC_API_KEY"),
            "anthropic-version": _ANTHROPIC_VERSION,
        }

    def _messages_url(self) -> str:
        """Return the messages endpoint URL."""
        base: str = self._config("ANTHROPIC_BASE_URL", "https://api.anthropic.com").rstrip("/")
        return f"{base}/v1/messages"

    def _classify_remote(self, sanitized: str) -> str:
        """Run one classification against the messages endpoint.

        :param sanitized: sanitized user text
        :return: the raw reply text
        """
        from app.ai.prompt import SYSTEM_PROMPT

        body: dict[str, Any] = self._post(
            self._messages_url(),
            {
                "model": self._config("ANTHROPIC_MODEL"),
                "max_tokens": 10,
                "system": SYSTEM_PROMPT,
                "messages": [{"role": "user", "content": sanitized}],
                "temperature": 0,
            },
            self._headers(),
        )
        try:
            return str(body["content"][0]["text"])
        except (KeyError, IndexError, TypeError) as exc:
            raise RuntimeError(f"Unexpected messages response: {body}") from exc

    def _ping(self) -> bool:
        """Probe the models listing endpoint."""
        base: str = self._config("ANTHROPIC_BASE_URL", "https://api.anthropic.com").rstrip("/")
        response = self._session.get(f"{base}/v1/models", headers=self._headers(), timeout=5)
        return response.status_code < 500
