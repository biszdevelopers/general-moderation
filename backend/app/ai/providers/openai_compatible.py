"""OpenAI-compatible chat completions provider.

Works against the official API and any server speaking the same schema
(vLLM, LM Studio, llama.cpp's OpenAI endpoint, OpenRouter, ...).
"""

from __future__ import annotations

from typing import Any

from app.ai.providers.remote import RemoteProvider


class OpenAICompatibleProvider(RemoteProvider):
    """Classifies text through an OpenAI-compatible chat completions API."""

    @property
    def name(self) -> str:
        """Return the provider identifier."""
        return "openai_compatible"

    def _headers(self) -> dict[str, str]:
        """Build request headers including the bearer token when set."""
        headers: dict[str, str] = {"Content-Type": "application/json"}
        api_key: str = self._config("OPENAI_API_KEY")
        if api_key:
            headers["Authorization"] = f"Bearer {api_key}"
        return headers

    def _chat_url(self) -> str:
        """Return the chat completions endpoint URL."""
        base: str = self._config("OPENAI_BASE_URL", "https://api.openai.com/v1").rstrip("/")
        return f"{base}/chat/completions"

    def _extract_reply(self, body: dict[str, Any]) -> str:
        """Pull the assistant text out of a chat completions response.

        :param body: decoded response body
        :return: the reply text
        :raises RuntimeError: when the response shape is unexpected
        """
        try:
            return str(body["choices"][0]["message"]["content"])
        except (KeyError, IndexError, TypeError) as exc:
            raise RuntimeError(f"Unexpected chat completions response: {body}") from exc

    def _classify_remote(self, sanitized: str) -> str:
        """Run one classification against the chat completions endpoint.

        :param sanitized: sanitized user text
        :return: the raw reply text
        """
        from app.ai.prompt import SYSTEM_PROMPT

        body: dict[str, Any] = self._post(
            self._chat_url(),
            {
                "model": self._config("OPENAI_MODEL"),
                "messages": [
                    {"role": "system", "content": SYSTEM_PROMPT},
                    {"role": "user", "content": sanitized},
                ],
                "temperature": 0,
                "max_tokens": 10,
            },
            self._headers(),
        )
        return self._extract_reply(body)

    def _ping(self) -> bool:
        """Probe the models listing endpoint."""
        base: str = self._config("OPENAI_BASE_URL", "https://api.openai.com/v1").rstrip("/")
        response = self._session.get(f"{base}/models", headers=self._headers(), timeout=5)
        return response.status_code < 500
