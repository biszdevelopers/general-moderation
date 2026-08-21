"""Shared HTTP plumbing for remote LLM providers.

Every remote backend (Ollama, OpenAI-compatible, Anthropic-compatible,
external llama.cpp) reads its endpoint configuration from the runtime
settings service on each call so admin edits apply without a restart, and
shares one reply parser that strips reasoning blocks before verdict lookup.
"""

from __future__ import annotations

import re
import time
from abc import abstractmethod
from typing import Any

import requests

from app.ai.llama_detector import LlamaCppDetector
from app.ai.providers.interface import LLMProvider, ProviderResult

_THINK_PATTERN: re.Pattern[str] = re.compile(r"<think>.*?</think>", re.DOTALL)


def parse_verdict(reply: str) -> tuple[bool, str]:
    """Extract a BLOCK/ALLOW verdict from a raw model reply.

    Reasoning blocks are removed and the remaining text is uppercased; a
    reply containing BLOCK anywhere is treated as a block decision.

    :param reply: the raw provider reply text
    :return: (blocked, cleaned reply) tuple
    """
    cleaned: str = _THINK_PATTERN.sub("", reply).strip().upper()
    if "</think>" in cleaned:
        cleaned = cleaned.split("</think>")[-1].strip()
    return "BLOCK" in cleaned, cleaned


class RemoteProvider(LLMProvider):
    """Base class for providers reached over HTTP.

    :param settings_service: runtime settings used for endpoints and keys
    :param timeout_key: settings key holding the per-call timeout in seconds
    """

    def __init__(
        self, settings_service: Any, timeout_key: str = "LLM_RESPONSE_TIMEOUT_SECONDS"
    ) -> None:
        self._settings_service: Any = settings_service
        self._timeout_key: str = timeout_key
        self._session: requests.Session = requests.Session()
        self._last_prompt_value: str | None = None
        self._last_reply_value: str | None = None

    def _timeout(self) -> float:
        """Return the configured request timeout in seconds."""
        return float(self._settings_service.get(self._timeout_key, 30))

    def _config(self, key: str, default: str = "") -> str:
        """Return one string setting used by this provider.

        :param key: the settings key
        :param default: value returned when unset
        """
        value = self._settings_service.get(key, default)
        return default if value is None else str(value)

    def _post(self, url: str, payload: dict[str, Any], headers: dict[str, str]) -> dict[str, Any]:
        """POST a JSON body and decode the JSON response.

        :param url: the absolute endpoint URL
        :param payload: the JSON-serializable request body
        :param headers: request headers
        :return: the decoded response body
        :raises RuntimeError: when the endpoint returns an error status
        """
        response = self._session.post(url, json=payload, headers=headers, timeout=self._timeout())
        if response.status_code >= 400:
            raise RuntimeError(f"{url} returned {response.status_code}: {response.text[:200]}")
        return response.json()

    @abstractmethod
    def _ping(self) -> bool:
        """Probe the remote endpoint cheaply without running inference."""

    @abstractmethod
    def _classify_remote(self, sanitized: str) -> str:
        """Run one remote classification and return the raw reply text.

        :param sanitized: sanitized user text
        :return: the raw reply text
        """

    def classify(self, text: str) -> ProviderResult:
        """Classify the text through the remote endpoint.

        :param text: raw user text; sanitized before it leaves the process
        :return: the classification result
        :raises RuntimeError: when the endpoint fails or returns garbage
        """
        from app.ai.prompt import SYSTEM_PROMPT

        sanitized: str = LlamaCppDetector.sanitize(text)
        self._last_prompt_value = SYSTEM_PROMPT
        start: float = time.monotonic()
        reply: str = self._classify_remote(sanitized)
        latency_ms: float = round((time.monotonic() - start) * 1000, 2)
        self._last_reply_value = reply
        blocked, cleaned = parse_verdict(reply)
        confidence: float = 0.9 if blocked else 0.5
        return ProviderResult(
            blocked=blocked, confidence=confidence, raw_reply=cleaned, latency_ms=latency_ms
        )

    def health_check(self) -> bool:
        """Return whether the remote endpoint answers its ping probe."""
        try:
            return self._ping()
        except Exception:
            return False

    @property
    def last_prompt(self) -> str | None:
        """Return the system prompt of the most recent classification."""
        return self._last_prompt_value

    @property
    def last_reply(self) -> str | None:
        """Return the most recent raw reply."""
        return self._last_reply_value

    def start(self) -> None:
        """No-op: remote providers hold no background resources."""

    def shutdown(self) -> None:
        """Close the underlying HTTP session."""
        self._session.close()
