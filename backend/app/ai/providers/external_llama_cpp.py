"""External llama.cpp server provider.

The llama.cpp ``llama-server`` binary exposes an OpenAI-compatible chat
completions endpoint, so this adapter reuses the OpenAI-compatible request
shape with no API key and probes the server's native ``/health`` route.
"""

from __future__ import annotations

from app.ai.providers.openai_compatible import OpenAICompatibleProvider


class ExternalLlamaCppProvider(OpenAICompatibleProvider):
    """Classifies text through a llama.cpp server hosted outside the project."""

    @property
    def name(self) -> str:
        """Return the provider identifier."""
        return "external_llama_cpp"

    def _chat_url(self) -> str:
        """Return the external server's chat completions endpoint."""
        base: str = self._config("EXTERNAL_LLAMACPP_BASE_URL", "http://127.0.0.1:8080").rstrip("/")
        return f"{base}/v1/chat/completions"

    def _classify_remote(self, sanitized: str) -> str:
        """Run one classification against the external server.

        The model name is optional: a single-model server ignores it.

        :param sanitized: sanitized user text
        :return: the raw reply text
        """
        from app.ai.prompt import SYSTEM_PROMPT

        payload: dict[str, str] = {"role": "user", "content": sanitized}
        model: str = self._config("EXTERNAL_LLAMACPP_MODEL")
        body_payload: dict[str, object] = {
            "messages": [
                {"role": "system", "content": SYSTEM_PROMPT},
                payload,
            ],
            "temperature": 0,
            "max_tokens": 10,
        }
        if model:
            body_payload["model"] = model
        body = self._post(self._chat_url(), body_payload, {"Content-Type": "application/json"})
        return self._extract_reply(body)

    def _ping(self) -> bool:
        """Probe the native llama.cpp health endpoint."""
        base: str = self._config("EXTERNAL_LLAMACPP_BASE_URL", "http://127.0.0.1:8080").rstrip("/")
        response = self._session.get(f"{base}/health", timeout=5)
        return response.status_code < 500
