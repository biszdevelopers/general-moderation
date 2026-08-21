"""Provider adapter tests.

Covers the shared verdict parser, every remote adapter's request shape and
reply extraction, the local provider wrapper, the runtime settings view,
and the provider factory.
"""

from __future__ import annotations

from typing import Any
from unittest.mock import MagicMock

import pytest

from app.ai.providers.anthropic_compatible import AnthropicCompatibleProvider
from app.ai.providers.external_llama_cpp import ExternalLlamaCppProvider
from app.ai.providers.factory import create_provider
from app.ai.providers.interface import LLMProvider, ProviderResult
from app.ai.providers.local import LocalLlamaCppProvider, RuntimeModelSettings
from app.ai.providers.ollama import OllamaProvider
from app.ai.providers.openai_compatible import OpenAICompatibleProvider
from app.ai.providers.remote import parse_verdict


class _StubSettingsService:
    """Returns canned values for any settings key."""

    def __init__(self, values: dict[str, Any] | None = None) -> None:
        self.values: dict[str, Any] = values or {}

    def get(self, key: str, default: Any = None) -> Any:
        """Return the canned value or the default."""
        return self.values.get(key, default)


def _remote(service_values: dict[str, Any] | None = None) -> OpenAICompatibleProvider:
    """Build an OpenAI-compatible provider with stubbed settings."""
    return OpenAICompatibleProvider(_StubSettingsService(service_values))


class TestParseVerdict:
    """Shared reply parsing."""

    def test_plain_block(self) -> None:
        """A plain BLOCK reply parses as blocked."""
        blocked, cleaned = parse_verdict("BLOCK")
        assert blocked is True
        assert cleaned == "BLOCK"

    def test_plain_allow(self) -> None:
        """A plain ALLOW reply parses as allowed."""
        blocked, _cleaned = parse_verdict("ALLOW")
        assert blocked is False

    def test_reasoning_block_stripped(self) -> None:
        """A think block containing ALLOW does not mask a BLOCK verdict."""
        blocked, cleaned = parse_verdict("<think>ALLOW</think>BLOCK")
        assert blocked is True
        assert "THINK" not in cleaned

    def test_trailing_think_tag(self) -> None:
        """Content after an unclosed think tag still parses."""
        blocked, _ = parse_verdict("junk</think>BLOCK")
        assert blocked is True


class TestOpenAICompatibleProvider:
    """Request shape and reply extraction for the OpenAI adapter."""

    def test_classify_sends_expected_body(self) -> None:
        """The chat completions body carries system+user messages at temp 0."""
        provider = _remote({"OPENAI_BASE_URL": "http://x/v1", "OPENAI_MODEL": "m"})
        response = MagicMock()
        response.status_code = 200
        response.json.return_value = {"choices": [{"message": {"content": " BLOCK "}}]}
        provider._session.post = MagicMock(return_value=response)
        result = provider.classify("hello")
        url = provider._session.post.call_args.args[0]
        payload = provider._session.post.call_args.kwargs["json"]
        assert url == "http://x/v1/chat/completions"
        assert payload["model"] == "m"
        assert payload["temperature"] == 0
        assert payload["messages"][0]["role"] == "system"
        assert payload["messages"][1]["content"] == "hello"
        assert result.blocked is True
        assert result.confidence == 0.9
        assert result.raw_reply == "BLOCK"

    def test_api_key_header_only_when_set(self) -> None:
        """The bearer header appears only with a configured key."""
        keyed = _remote({"OPENAI_API_KEY": "sk-1"})
        assert keyed._headers()["Authorization"] == "Bearer sk-1"
        assert "Authorization" not in _remote()._headers()

    def test_error_status_raises(self) -> None:
        """HTTP failures surface as RuntimeError."""
        provider = _remote()
        response = MagicMock()
        response.status_code = 500
        response.text = "boom"
        provider._session.post = MagicMock(return_value=response)
        with pytest.raises(RuntimeError):
            provider.classify("hello")

    def test_unexpected_shape_raises(self) -> None:
        """A malformed body raises instead of returning garbage."""
        provider = _remote()
        with pytest.raises(RuntimeError):
            provider._extract_reply({"nope": []})

    def test_ping_uses_models_route(self) -> None:
        """Health probing hits GET /models below 500."""
        provider = _remote({"OPENAI_BASE_URL": "http://x/v1"})
        response = MagicMock()
        response.status_code = 200
        provider._session.get = MagicMock(return_value=response)
        assert provider.health_check() is True
        assert provider._session.get.call_args.args[0] == "http://x/v1/models"

    def test_ping_failure_is_false(self) -> None:
        """Connection errors map to unhealthy."""
        provider = _remote()
        provider._session.get = MagicMock(side_effect=OSError("down"))
        assert provider.health_check() is False


class TestAnthropicCompatibleProvider:
    """Request shape for the Anthropic adapter."""

    def test_classify_sends_messages_shape(self) -> None:
        """The messages body carries system text and the API key header."""
        provider = AnthropicCompatibleProvider(
            _StubSettingsService(
                {
                    "ANTHROPIC_BASE_URL": "http://a",
                    "ANTHROPIC_MODEL": "claude",
                    "ANTHROPIC_API_KEY": "k",
                }
            )
        )
        response = MagicMock()
        response.status_code = 200
        response.json.return_value = {"content": [{"text": "ALLOW"}]}
        provider._session.post = MagicMock(return_value=response)
        result = provider.classify("hi")
        headers = provider._session.post.call_args.kwargs["headers"]
        payload = provider._session.post.call_args.kwargs["json"]
        assert headers["x-api-key"] == "k"
        assert headers["anthropic-version"] == "2023-06-01"
        assert payload["system"]
        assert result.blocked is False

    def test_bad_shape_raises(self) -> None:
        """A malformed content list raises RuntimeError."""
        provider = AnthropicCompatibleProvider(_StubSettingsService())
        with pytest.raises(RuntimeError):
            provider._classify_remote("x")


class TestOllamaProvider:
    """Request shape for the Ollama adapter."""

    def test_classify_sends_chat_options(self) -> None:
        """The chat body disables streaming and pins temperature zero."""
        provider = OllamaProvider(
            _StubSettingsService({"OLLAMA_BASE_URL": "http://o", "OLLAMA_MODEL": "q"})
        )
        response = MagicMock()
        response.status_code = 200
        response.json.return_value = {"message": {"content": "BLOCK"}}
        provider._session.post = MagicMock(return_value=response)
        result = provider.classify("hi")
        payload = provider._session.post.call_args.kwargs["json"]
        assert payload["stream"] is False
        assert payload["options"]["temperature"] == 0
        assert result.blocked is True

    def test_missing_message_raises(self) -> None:
        """A body without message content raises RuntimeError."""
        provider = OllamaProvider(_StubSettingsService())
        provider._post = MagicMock(return_value={})
        with pytest.raises(RuntimeError):
            provider._classify_remote("x")


class TestExternalLlamaCppProvider:
    """The external llama.cpp adapter reuses the OpenAI shape."""

    def test_model_optional_and_health_native(self) -> None:
        """Without EXTERNAL_LLAMACPP_MODEL no model field is sent; /health probes."""
        provider = ExternalLlamaCppProvider(
            _StubSettingsService({"EXTERNAL_LLAMACPP_BASE_URL": "http://l:8080"})
        )
        response = MagicMock()
        response.status_code = 200
        response.json.return_value = {"choices": [{"message": {"content": "BLOCK"}}]}
        provider._session.post = MagicMock(return_value=response)
        result = provider.classify("hi")
        payload = provider._session.post.call_args.kwargs["json"]
        assert "model" not in payload
        assert result.blocked is True
        health = MagicMock()
        health.status_code = 200
        provider._session.get = MagicMock(return_value=health)
        assert provider.health_check() is True
        assert provider._session.get.call_args.args[0] == "http://l:8080/health"


class TestRuntimeModelSettings:
    """Runtime overlay onto static model settings."""

    def test_active_path_wins_over_static(self) -> None:
        """ACTIVE_GGUF_PATH replaces model_path when set."""
        static = MagicMock()
        static.model_path = "auto"
        view = RuntimeModelSettings(static, _StubSettingsService({"ACTIVE_GGUF_PATH": "/m.gguf"}))
        assert view.model_path == "/m.gguf"
        view2 = RuntimeModelSettings(static, _StubSettingsService())
        assert view2.model_path == "auto"

    def test_other_fields_pass_through(self) -> None:
        """Unrelated attributes resolve from static settings."""
        static = MagicMock()
        static.model_dir = "./models"
        view = RuntimeModelSettings(static, _StubSettingsService())
        assert view.model_dir == "./models"


class TestLocalProvider:
    """Local adapter delegation."""

    def _provider(self) -> LocalLlamaCppProvider:
        """Build a local provider with a mocked detector."""
        provider = LocalLlamaCppProvider(MagicMock(), _StubSettingsService())
        provider._detector = MagicMock()
        provider._detector.detect.return_value = MagicMock(matched=True, confidence_score=0.9)
        provider._detector.last_reply = "BLOCK"
        return provider

    def test_classify_maps_result(self) -> None:
        """Detector output maps to ProviderResult with latency."""
        provider = self._provider()
        result = provider.classify("hi")
        assert result.blocked is True
        assert result.confidence == 0.9
        assert result.latency_ms >= 0

    def test_delegation_methods(self) -> None:
        """Health, prompt hooks, start, and shutdown delegate to the detector."""
        provider = self._provider()
        provider.set_system_prompt("custom")
        provider.start()
        provider.shutdown()
        assert provider._detector.set_system_prompt.called
        assert provider._detector.start_preload.called
        assert provider._detector.shutdown.called
        assert provider.name == "local_llama_cpp"


class TestFactory:
    """Provider factory mapping."""

    @pytest.mark.parametrize(
        ("name", "expected"),
        [
            ("local_llama_cpp", LocalLlamaCppProvider),
            ("external_llama_cpp", ExternalLlamaCppProvider),
            ("ollama", OllamaProvider),
            ("openai_compatible", OpenAICompatibleProvider),
            ("anthropic_compatible", AnthropicCompatibleProvider),
        ],
    )
    def test_known_names(self, name: str, expected: type) -> None:
        """Every documented provider name builds its adapter."""
        provider = create_provider(name, MagicMock(), _StubSettingsService())
        assert isinstance(provider, expected)

    def test_empty_and_unknown_names_return_none(self) -> None:
        """Empty and unknown names degrade to None."""
        assert create_provider("", MagicMock(), _StubSettingsService()) is None
        assert create_provider("nope", MagicMock(), _StubSettingsService()) is None


class TestInterfaceDefaults:
    """Default implementations on the ABC."""

    def test_set_system_prompt_default_noop(self) -> None:
        """The base set_system_prompt accepts calls without effect."""

        class _Minimal(LLMProvider):
            """Concrete minimal provider."""

            @property
            def name(self) -> str:
                """Return a name."""
                return "minimal"

            def classify(self, text: str) -> ProviderResult:
                """Return a fixed result."""
                return ProviderResult(False, 0.5, "", 0.0)

            def health_check(self) -> bool:
                """Report healthy."""
                return True

            @property
            def last_prompt(self) -> str | None:
                """No prompt."""
                return None

            @property
            def last_reply(self) -> str | None:
                """No reply."""
                return None

            def start(self) -> None:
                """Nothing to start."""

            def shutdown(self) -> None:
                """Nothing to release."""

        provider = _Minimal()
        provider.set_system_prompt("ignored")
        assert provider.describe_status() == {"name": "minimal", "available": True}
