"""Model router tests.

Covers startup wiring, classification pinning, graceful drain, inline and
monitored failover, status reporting, and shutdown.
"""

from __future__ import annotations

import threading
import time
from typing import Any
from unittest.mock import MagicMock

from app.ai.providers.interface import LLMProvider, ProviderResult
from app.ai.providers.router import ModelRouter


class _StubSettingsService:
    """Canned settings values with mutation for refresh scenarios."""

    def __init__(self) -> None:
        self.values: dict[str, Any] = {
            "LLM_PROVIDER": "a",
            "BACKUP_LLM_PROVIDER": "b",
            "MODEL_HEALTH_FAILURE_THRESHOLD": 2,
            "MODEL_HEALTH_INTERVAL_SECONDS": 30,
        }

    def get(self, key: str, default: Any = None) -> Any:
        """Return the stored value or default."""
        return self.values.get(key, default)


class _StubProvider(LLMProvider):
    """Scriptable provider recording lifecycle calls."""

    def __init__(self, name: str, fail: bool = False) -> None:
        self._name: str = name
        self.fail: bool = fail
        self.started: bool = False
        self.shutdown_calls: int = 0
        self.inflight_gate: threading.Event | None = None
        self.release_gate: threading.Event | None = None

    @property
    def name(self) -> str:
        """Return the provider name."""
        return self._name

    def classify(self, text: str) -> ProviderResult:
        """Optionally block until released, then reply or raise."""
        if self.inflight_gate is not None:
            self.inflight_gate.set()
            assert self.release_gate is not None
            self.release_gate.wait(timeout=5)
        if self.fail:
            raise RuntimeError("boom")
        return ProviderResult(blocked=True, confidence=0.9, raw_reply="BLOCK", latency_ms=1.0)

    def health_check(self) -> bool:
        """Healthy unless flagged to fail."""
        return not self.fail

    @property
    def last_prompt(self) -> str | None:
        """Return the prompt."""
        return "p"

    @property
    def last_reply(self) -> str | None:
        """Return the reply."""
        return "BLOCK"

    def start(self) -> None:
        """Mark started."""
        self.started = True

    def shutdown(self) -> None:
        """Count the shutdown."""
        self.shutdown_calls += 1


class _RouterHarness(ModelRouter):
    """Router whose provider factory returns scripted stubs."""

    def __init__(self, providers: dict[str, _StubProvider]) -> None:
        super().__init__(MagicMock(), _StubSettingsService())
        self.providers: dict[str, _StubProvider] = providers

    def _build(self, name: str) -> LLMProvider | None:
        """Return the scripted provider for a name."""
        if name == "fail":
            broken: _StubProvider = _StubProvider(name, fail=True)
            self.providers[name] = broken
            return broken
        return self.providers.get(name)


def _harness() -> tuple[_RouterHarness, _StubProvider, _StubProvider]:
    """Build a harness with active 'a' and backup 'b'."""
    a: _StubProvider = _StubProvider("a")
    b: _StubProvider = _StubProvider("b")
    return _RouterHarness({"a": a, "b": b}), a, b


class TestRouterLifecycle:
    """Start, refresh, switch, and shutdown."""

    def test_start_builds_and_starts_active(self) -> None:
        """start() activates the configured provider and monitor thread."""
        router, a, _ = _harness()
        router.start()
        assert a.started is True
        assert router.active_provider_name == "a"
        assert router.is_available() is True
        router.shutdown()
        assert a.shutdown_calls >= 1

    def test_start_is_idempotent(self) -> None:
        """Repeated start() calls do not rebuild the active provider."""
        router, _a, _ = _harness()
        router.start()
        router.start()
        assert router.active_provider_name == "a"
        router.shutdown()

    def test_switch_replaces_active_and_drains_old(self) -> None:
        """switch() retires the old provider after drain."""
        router, a, _b = _harness()
        router.start()
        assert router.switch("b") is True
        deadline: float = time.monotonic() + 3
        while a.shutdown_calls == 0 and time.monotonic() < deadline:
            time.sleep(0.01)
        assert a.shutdown_calls == 1
        assert router.active_provider_name == "b"
        router.shutdown()

    def test_switch_unknown_name_fails(self) -> None:
        """switch() rejects unknown names without touching the active."""
        router, _, _ = _harness()
        router.start()
        assert router.switch("missing") is False
        assert router.active_provider_name == "a"
        router.shutdown()

    def test_refresh_rebuilds_from_settings(self) -> None:
        """refresh() keeps the settings-named provider active."""
        router, a, b = _harness()
        router.start()
        router.refresh()
        assert router.active_provider_name == "a"
        assert a.shutdown_calls == 0
        assert b.shutdown_calls == 0
        router.shutdown()


class TestRouterClassify:
    """Classification paths."""

    def test_classify_success_resets_failures(self) -> None:
        """A successful classify clears the failure counter."""
        router, _, _ = _harness()
        router.start()
        result = router.classify("hi")
        assert result is not None and result.blocked is True
        assert router.status()["consecutive_failures"] == 0
        router.shutdown()

    def test_classify_without_provider_returns_none(self) -> None:
        """No active provider yields None."""
        router, _, _ = _harness()
        assert router.classify("hi") is None

    def test_classify_error_counts_toward_failover(self) -> None:
        """Threshold failures swap to the backup."""
        broken: _StubProvider = _StubProvider("a", fail=True)
        backup: _StubProvider = _StubProvider("b")
        router = _RouterHarness({"a": broken, "b": backup})
        router.start()
        first = router.classify("hi")
        second = router.classify("hi")
        assert first is None and second is None
        assert router.active_provider_name == "b"
        router.shutdown()

    def test_failover_without_backup_stays(self) -> None:
        """Without a backup the failed provider stays active."""
        broken: _StubProvider = _StubProvider("a", fail=True)
        router = _RouterHarness({"a": broken})
        router.start()
        router.classify("hi")
        router.classify("hi")
        router.classify("hi")
        assert router.active_provider_name == "a"
        router.shutdown()

    def test_graceful_drain_completes_before_shutdown(self) -> None:
        """An in-flight classify finishes on the retired provider."""
        router, a, _b = _harness()
        a.inflight_gate = threading.Event()
        a.release_gate = threading.Event()
        results: list[ProviderResult | None] = []

        def worker() -> None:
            """Classify on the background thread."""
            results.append(router.classify("hi"))

        thread = threading.Thread(target=worker)
        router.start()
        thread.start()
        assert a.inflight_gate.wait(timeout=5)
        assert router.switch("b") is True
        a.release_gate.set()
        thread.join(timeout=5)
        assert results and results[0] is not None
        deadline: float = time.monotonic() + 3
        while a.shutdown_calls == 0 and time.monotonic() < deadline:
            time.sleep(0.01)
        assert a.shutdown_calls == 1
        router.shutdown()

    def test_trace_passthrough(self) -> None:
        """last_prompt/last_reply delegate to the active provider."""
        router, _, _ = _harness()
        router.start()
        assert router.last_prompt == "p"
        assert router.last_reply == "BLOCK"
        router.shutdown()

    def test_set_system_prompt_reaches_both(self) -> None:
        """Prompt updates propagate to active and backup providers."""
        prompts: dict[str, str] = {}

        class PromptRecorder(_StubProvider):
            """Records the last system prompt."""

            def set_system_prompt(self, template: str) -> None:
                """Record the template."""
                prompts[self.name] = template

        recorder_a: PromptRecorder = PromptRecorder("a")
        recorder_b: PromptRecorder = PromptRecorder("b")
        router = _RouterHarness({"a": recorder_a, "b": recorder_b})
        router.start()
        router.set_system_prompt("custom rules")
        assert prompts == {"a": "custom rules", "b": "custom rules"}
        router.shutdown()


class TestRouterHealthMonitor:
    """Monitor-driven failover."""

    def test_monitor_failover_after_threshold(self, monkeypatch: Any) -> None:
        """A failing health probe triggers failover within one interval."""
        broken: _StubProvider = _StubProvider("a", fail=True)
        backup: _StubProvider = _StubProvider("b")
        router = _RouterHarness({"a": broken, "b": backup})
        router._settings_service.values["MODEL_HEALTH_INTERVAL_SECONDS"] = 1
        router.start()
        deadline: float = time.monotonic() + 6
        while router.active_provider_name != "b" and time.monotonic() < deadline:
            time.sleep(0.05)
        assert router.active_provider_name == "b"
        router.shutdown()

    def test_status_reports_unavailable_providers(self) -> None:
        """status() tolerates probing errors."""
        router, a, _ = _harness()
        router.start()
        a.health_check = lambda: (_ for _ in ()).throw(RuntimeError("x"))
        summary: dict[str, Any] = router.status()
        assert summary["active"]["available"] is False
        assert summary["backup"]["available"] is True
        router.shutdown()

    def test_shutdown_without_start_is_safe(self) -> None:
        """Shutting down an unused router does not raise."""
        router, _, _ = _harness()
        router.shutdown()
        assert router.active_provider_name is None
