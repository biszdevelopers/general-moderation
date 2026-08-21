"""Provider abstraction for Stage 3 LLM classification.

Every provider — local llama.cpp, an external llama.cpp server, Ollama,
OpenAI-compatible chat completions, or Anthropic-compatible messages —
implements the same small surface so the model router can switch between
them without the pipeline knowing which engine answered.
"""

from __future__ import annotations

from abc import ABC, abstractmethod
from dataclasses import dataclass
from typing import Any


@dataclass(frozen=True, slots=True)
class ProviderResult:
    """One classification verdict from a provider.

    :param blocked: whether the provider replied BLOCK
    :param confidence: raw confidence in the verdict, 0.0 to 1.0
    :param raw_reply: the unmodified provider reply text
    :param latency_ms: wall-clock time of the classification
    """

    blocked: bool
    confidence: float
    raw_reply: str
    latency_ms: float


class LLMProvider(ABC):
    """Common interface implemented by every Stage 3 model provider."""

    @property
    @abstractmethod
    def name(self) -> str:
        """Return the provider identifier used in settings and metrics."""

    @abstractmethod
    def classify(self, text: str) -> ProviderResult:
        """Classify one sanitized text payload.

        :param text: raw user text; providers sanitize before inference
        :return: the classification result
        """

    @abstractmethod
    def health_check(self) -> bool:
        """Return whether the provider can serve a classification right now."""

    @property
    @abstractmethod
    def last_prompt(self) -> str | None:
        """Return the most recent prompt sent to the model, if any."""

    @property
    @abstractmethod
    def last_reply(self) -> str | None:
        """Return the most recent raw reply, if any."""

    @abstractmethod
    def start(self) -> None:
        """Begin any background work (downloads, loads) without blocking."""

    @abstractmethod
    def shutdown(self) -> None:
        """Release every resource held by the provider."""

    def describe_status(self) -> dict[str, Any]:
        """Return a JSON-serializable health summary for the admin API.

        :return: provider name and availability
        """
        return {"name": self.name, "available": self.health_check()}
