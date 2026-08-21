"""Provider factory mapping setting names to adapter instances."""

from __future__ import annotations

from typing import Any

from app.ai.providers.anthropic_compatible import AnthropicCompatibleProvider
from app.ai.providers.external_llama_cpp import ExternalLlamaCppProvider
from app.ai.providers.interface import LLMProvider
from app.ai.providers.local import LocalLlamaCppProvider
from app.ai.providers.ollama import OllamaProvider
from app.ai.providers.openai_compatible import OpenAICompatibleProvider


def create_provider(
    name: str, settings: Any, settings_service: Any, logger: Any | None = None
) -> LLMProvider | None:
    """Build the provider registered under a settings name.

    :param name: provider identifier from ``LLM_PROVIDER``/``BACKUP_LLM_PROVIDER``
    :param settings: static application settings (MODEL_* fields)
    :param settings_service: runtime settings for endpoints and keys
    :param logger: optional structured logger
    :return: the provider, or None for an empty or unknown name
    """
    if not name:
        return None
    provider: LLMProvider
    if name == "local_llama_cpp":
        provider = LocalLlamaCppProvider(settings, settings_service, logger)
    elif name == "external_llama_cpp":
        provider = ExternalLlamaCppProvider(settings_service)
    elif name == "ollama":
        provider = OllamaProvider(settings_service)
    elif name == "openai_compatible":
        provider = OpenAICompatibleProvider(settings_service)
    elif name == "anthropic_compatible":
        provider = AnthropicCompatibleProvider(settings_service)
    else:
        return None
    return provider
