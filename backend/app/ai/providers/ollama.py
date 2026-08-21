"""Ollama HTTP API provider."""

from __future__ import annotations

from typing import Any

from app.ai.providers.remote import RemoteProvider


class OllamaProvider(RemoteProvider):
    """Classifies text through a local or remote Ollama server."""

    @property
    def name(self) -> str:
        """Return the provider identifier."""
        return "ollama"

    def _chat_url(self) -> str:
        """Return the Ollama chat endpoint URL."""
        base: str = self._config("OLLAMA_BASE_URL", "http://127.0.0.1:11434").rstrip("/")
        return f"{base}/api/chat"

    def _classify_remote(self, sanitized: str) -> str:
        """Run one classification against the Ollama chat endpoint.

        :param sanitized: sanitized user text
        :return: the raw reply text
        """
        body: dict[str, Any] = self._post(
            self._chat_url(),
            {
                "model": self._config("OLLAMA_MODEL"),
                "messages": [
                    {"role": "system", "content": self._system_prompt()},
                    {"role": "user", "content": sanitized},
                ],
                "stream": False,
                "options": {"temperature": 0, "num_predict": 10},
            },
            {"Content-Type": "application/json"},
        )
        try:
            return str(body["message"]["content"])
        except (KeyError, TypeError) as exc:
            raise RuntimeError(f"Unexpected Ollama response: {body}") from exc

    def _ping(self) -> bool:
        """Probe the tags endpoint that lists installed models."""
        base: str = self._config("OLLAMA_BASE_URL", "http://127.0.0.1:11434").rstrip("/")
        response = self._session.get(f"{base}/api/tags", timeout=5)
        return response.status_code < 500
