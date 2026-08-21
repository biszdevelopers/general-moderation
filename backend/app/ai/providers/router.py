"""Model router with graceful switching and health failover.

The router owns the active and backup providers named by the runtime
settings. Classifications pin the provider they start on, so an admin
switch never aborts in-flight work: the old provider drains its remaining
classifications and only then releases its memory. A daemon monitor probes
the active provider and fails over to the backup after the configured
number of consecutive failures; failures observed inline count toward the
same threshold.
"""

from __future__ import annotations

import threading
from typing import Any

from app.ai.providers.factory import create_provider
from app.ai.providers.interface import LLMProvider, ProviderResult


class ModelRouter:
    """Routes Stage 3 classifications to the active LLM provider.

    :param settings: static application settings (MODEL_* fields)
    :param settings_service: runtime settings for provider selection
    :param logger: optional structured logger
    """

    def __init__(self, settings: Any, settings_service: Any, logger: Any | None = None) -> None:
        self._settings: Any = settings
        self._settings_service: Any = settings_service
        self._logger: Any = logger
        self._lock: threading.Lock = threading.Lock()
        self._drain_cond: threading.Condition = threading.Condition()
        self._active: LLMProvider | None = None
        self._backup: LLMProvider | None = None
        self._inflight: dict[int, int] = {}
        self._failure_count: int = 0
        self._stop_event: threading.Event = threading.Event()
        self._monitor_thread: threading.Thread | None = None

    def _log(self, level: int, message: str, **fields: Any) -> None:
        """Emit a structured log record when a logger is attached.

        :param level: numeric logging level
        :param message: log message
        :param fields: structured fields
        """
        if self._logger is not None:
            self._logger.log(level, f"router:{message}", **fields)

    def _build(self, name: str) -> LLMProvider | None:
        """Construct one provider from a settings name.

        :param name: the provider identifier
        :return: the provider or None
        """
        return create_provider(name, self._settings, self._settings_service, self._logger)

    def _provider_key(self, provider: LLMProvider | None) -> int:
        """Return the inflight-map key for a provider."""
        return id(provider) if provider is not None else 0

    def start(self) -> None:
        """Build both providers from settings and begin monitoring.

        Safe to call repeatedly; only the first call has an effect.
        """
        with self._lock:
            if self._active is not None:
                return
            active_name: str = str(self._settings_service.get("LLM_PROVIDER", ""))
            backup_name: str = str(self._settings_service.get("BACKUP_LLM_PROVIDER", ""))
            self._active = self._build(active_name)
            self._backup = self._build(backup_name)
            if self._active is not None:
                self._active.start()
            self._log(20, "started", active=active_name, backup=backup_name)
        if self._monitor_thread is None:
            self._monitor_thread = threading.Thread(
                target=self._monitor_loop, name="model-health-monitor", daemon=True
            )
            self._monitor_thread.start()

    def refresh(self) -> None:
        """Rebuild both providers from the current settings.

        Called after admin edits to ``LLM_PROVIDER`` or
        ``BACKUP_LLM_PROVIDER``. The previously active provider drains
        before it is shut down.
        """
        self.start()
        active_name: str = str(self._settings_service.get("LLM_PROVIDER", ""))
        backup_name: str = str(self._settings_service.get("BACKUP_LLM_PROVIDER", ""))
        new_active: LLMProvider | None = self._build(active_name)
        new_backup: LLMProvider | None = self._build(backup_name)
        with self._lock:
            old_active: LLMProvider | None = self._active
            old_backup: LLMProvider | None = self._backup
            self._active = new_active
            self._backup = new_backup
            self._failure_count = 0
            if new_active is not None:
                new_active.start()
        self._log(20, "refreshed", active=active_name, backup=backup_name)
        if old_backup is not None and old_backup is not new_backup:
            self._retire(old_backup)
        if old_active is not None and old_active is not new_active:
            self._retire(old_active)

    def switch(self, name: str) -> bool:
        """Switch the active provider by name with a graceful drain.

        :param name: the provider identifier to activate
        :return: True when a provider was built and activated
        """
        provider: LLMProvider | None = self._build(name)
        if provider is None:
            return False
        provider.start()
        with self._lock:
            old: LLMProvider | None = self._active
            self._active = provider
            self._failure_count = 0
        self._log(20, "switched", active=name)
        if old is not None and old is not provider:
            self._retire(old)
        return True

    def classify(self, text: str) -> ProviderResult | None:
        """Classify text through the active provider, failing over on errors.

        :param text: raw user text
        :return: the result, or None when no provider can serve the request
        """
        with self._lock:
            provider: LLMProvider | None = self._active
        if provider is None:
            return None
        key: int = self._provider_key(provider)
        with self._drain_cond:
            self._inflight[key] = self._inflight.get(key, 0) + 1
        try:
            result: ProviderResult = provider.classify(text)
        except Exception as exc:
            self._log(30, "classify_failed", provider=provider.name, error=str(exc))
            self._record_failure()
            return None
        finally:
            with self._drain_cond:
                self._inflight[key] -= 1
                if self._inflight[key] <= 0:
                    del self._inflight[key]
                    self._drain_cond.notify_all()
        self._failure_count = 0
        return result

    def _record_failure(self) -> None:
        """Count one failure and fail over when the threshold is reached."""
        threshold: int = int(self._settings_service.get("MODEL_HEALTH_FAILURE_THRESHOLD", 3))
        with self._lock:
            self._failure_count += 1
            if self._failure_count < threshold or self._backup is None:
                return
            failed: LLMProvider | None = self._active
            backup: LLMProvider | None = self._backup
            self._active, self._backup = backup, failed
            self._failure_count = 0
        if failed is not None:
            self._log(
                30,
                "failed_over",
                from_provider=failed.name,
                to_provider=backup.name if backup else None,
            )
            self._retire(failed)

    def _monitor_loop(self) -> None:
        """Probe the active provider and fail over after repeated failures."""
        while not self._stop_event.is_set():
            interval: float = float(self._settings_service.get("MODEL_HEALTH_INTERVAL_SECONDS", 30))
            if self._stop_event.wait(timeout=interval):
                return
            with self._lock:
                provider: LLMProvider | None = self._active
            if provider is None:
                continue
            try:
                healthy: bool = provider.health_check()
            except Exception:
                healthy = False
            if not healthy:
                self._log(30, "health_check_failed", provider=provider.name)
                self._record_failure()

    def _retire(self, provider: LLMProvider) -> None:
        """Shut a provider down once its in-flight classifications drain.

        :param provider: the provider being taken out of service
        """
        key: int = self._provider_key(provider)

        def waiter() -> None:
            """Block until the provider's inflight count reaches zero."""
            with self._drain_cond:
                while self._inflight.get(key, 0) > 0:
                    self._drain_cond.wait(timeout=1.0)
            provider.shutdown()
            self._log(20, "retired", provider=provider.name)

        threading.Thread(target=waiter, name="provider-drain", daemon=True).start()

    @property
    def last_prompt(self) -> str | None:
        """Return the most recent prompt from the active provider."""
        with self._lock:
            provider: LLMProvider | None = self._active
        return provider.last_prompt if provider is not None else None

    @property
    def last_reply(self) -> str | None:
        """Return the most recent reply from the active provider."""
        with self._lock:
            provider: LLMProvider | None = self._active
        return provider.last_reply if provider is not None else None

    def is_available(self) -> bool:
        """Return whether an active provider exists and reports healthy."""
        with self._lock:
            provider: LLMProvider | None = self._active
        return provider is not None and provider.health_check()

    def status(self) -> dict[str, Any]:
        """Return a JSON-serializable summary for the admin API.

        :return: active/backup names and availability
        """

        def summarize(provider: LLMProvider | None) -> dict[str, Any] | None:
            """Summarize one provider safely."""
            if provider is None:
                return None
            try:
                available: bool = provider.health_check()
            except Exception:
                available = False
            return {"name": provider.name, "available": available}

        with self._lock:
            active: LLMProvider | None = self._active
            backup: LLMProvider | None = self._backup
            failures: int = self._failure_count
        return {
            "active": summarize(active),
            "backup": summarize(backup),
            "consecutive_failures": failures,
        }

    def shutdown(self) -> None:
        """Stop monitoring and release every provider immediately."""
        self._stop_event.set()
        with self._lock:
            providers: list[LLMProvider] = [
                p for p in (self._active, self._backup) if p is not None
            ]
            self._active = None
            self._backup = None
        for provider in providers:
            try:
                provider.shutdown()
            except Exception:
                pass
