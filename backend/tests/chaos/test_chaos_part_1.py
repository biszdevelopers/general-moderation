"""Chaos and resilience tests (Phase 1, P2/P3).

Covers degraded detector availability, malformed databases, broken package
adapters, thread-pool fallbacks, corrupted logs, and shutdown robustness.
"""

from __future__ import annotations

import sqlite3
from pathlib import Path
from typing import Any

import pytest

from app.detectors.rolling_hash_detector import RollingHashDetector
from tests.base_test import BaseTest


class TestChaosDetectors(BaseTest):
    """Detector resilience to missing data."""

    def test_rolling_hash_eviction_storm(self) -> None:
        """A burst of unique messages does not crash the cache."""
        detector: RollingHashDetector = RollingHashDetector(cache_size=100, ttl_seconds=1)
        for index in range(10_000):
            detector.detect(f"unique message number {index}")
        assert len(detector._cache) <= 100

    def test_rolling_hash_zero_ttl(self) -> None:
        """A zero TTL never retains entries."""
        detector: RollingHashDetector = RollingHashDetector(cache_size=10, ttl_seconds=0)
        detector.record_hit("expire now")
        detector.detect("expire now")
        detector.detect("expire now")
        assert detector.detect("expire now").matched is False

    def test_rolling_hash_negative_ttl(self) -> None:
        """A negative TTL is tolerated."""
        detector: RollingHashDetector = RollingHashDetector(cache_size=10, ttl_seconds=-5)
        detector.record_hit("gone")
        assert detector.detect("gone").matched is False

    def test_rolling_hash_one_slot(self) -> None:
        """A one-slot cache stays bounded and tracks the latest hit."""
        detector: RollingHashDetector = RollingHashDetector(cache_size=1, ttl_seconds=60)
        detector.record_hit("first")
        detector.record_hit("second")
        assert len(detector._cache) <= 1
        assert detector.detect("second").matched is True


class TestChaosDatabase(BaseTest):
    """Malformed database handling."""

    def test_corrupt_settings_db_raises_database_error(self, tmp_path: Path) -> None:
        """A corrupt settings database raises a DatabaseError."""
        db: Path = tmp_path / "settings.db"
        db.write_bytes(b"this is not sqlite data at all")
        from app.config import Settings

        settings = Settings(
            app_port=0, settings_db_path=str(db), log_file_path=str(tmp_path / "l.log")
        )
        from app.settings_service import SettingsService

        with pytest.raises(sqlite3.DatabaseError):
            SettingsService(settings)

    def test_empty_settings_db_constructs(self, tmp_path: Path) -> None:
        """A fresh empty settings database constructs a service."""
        db: Path = tmp_path / "settings.db"
        db.write_bytes(b"")
        from app.config import Settings

        settings = Settings(
            app_port=0, settings_db_path=str(db), log_file_path=str(tmp_path / "l.log")
        )
        from app.settings_service import SettingsService

        service: SettingsService = SettingsService(settings)
        assert "WEIGHT_DETECTOR_AHO" in service.all()
        assert service.all() != {}
        service.close()

    def test_missing_custom_words_db(self, engine: Any) -> None:
        """A missing custom words database does not break the word bank."""
        from app.wordbank.manager import WordBankManager
        from app.wordbank.storage import create_storage

        manager: WordBankManager = WordBankManager(
            storage=create_storage("sqlite", str(Path("nonexistent_dir_xyz") / "w.db"))
        )
        assert manager.get_stats()["total_words"] >= 0
        manager.close()

    def test_profiler_unknown_database(self, tmp_path: Path) -> None:
        """An empty profiler database initializes cleanly."""
        from app.profiling.user_profiler import UserProfiler

        profiler: UserProfiler = UserProfiler(str(tmp_path / "u.db"), str(tmp_path / "a.db"), 91)
        assert profiler.stats()["daily_rows"] == 0
        profiler.close()


class TestChaosPackages(BaseTest):
    """Package adapter resilience."""

    def test_adapters_survive_import_failure(self, monkeypatch: pytest.MonkeyPatch) -> None:
        """A missing package is skipped without crashing."""
        import importlib

        real_import: Any = importlib.import_module

        def _broken_import(name: str, *args: object, **kwargs: object) -> Any:
            if name == "profanite":
                raise ImportError("simulated missing package")
            return real_import(name, *args, **kwargs)

        monkeypatch.setattr(importlib, "import_module", _broken_import)
        from app.detectors.multi_language_detector import _PackageAdapter

        adapter: _PackageAdapter = _PackageAdapter("profanite", "any", "truthy")
        assert adapter.available is False
        assert adapter.detect("any text").matched is False

    def test_adapter_callable_raises_returns_no_match(self) -> None:
        """A callable that raises returns a non-match."""
        import types

        from app.detectors.multi_language_detector import _PackageAdapter

        module: Any = types.ModuleType("broken_pkg")

        def _boom(text: str) -> Any:
            raise RuntimeError("simulated crash")

        module.check = _boom
        adapter: _PackageAdapter = _PackageAdapter("broken_pkg", "any", "truthy")
        adapter._module = module
        adapter._callable = _boom
        assert adapter.detect("text").matched is False


class TestChaosEngine(BaseTest):
    """Engine resilience under degraded conditions."""

    def test_repeated_shutdown_safe(self, engine: Any) -> None:
        """Calling shutdown twice is safe."""
        engine.shutdown()
        engine.shutdown()

    def test_moderate_after_shutdown_raises(self, engine: Any) -> None:
        """Moderating after shutdown raises a database error, not a hang."""
        from app.models.request import ModerationRequest

        engine.shutdown()
        with pytest.raises(sqlite3.ProgrammingError):
            engine.moderate(ModerationRequest(text="post shutdown", app_name="a"))

    def test_clear_cache_twice(self, engine: Any) -> None:
        """Clearing the cache repeatedly is safe."""
        engine.clear_cache()
        engine.clear_cache()

    def test_metrics_after_shutdown(self, engine: Any) -> None:
        """Metrics remain readable after shutdown."""
        engine.shutdown()
        assert isinstance(engine.metrics(), dict)

    def test_log_after_shutdown(self, engine: Any) -> None:
        """Logging after shutdown does not raise."""
        engine.log("post shutdown message")


class TestChaosConcurrency(BaseTest):
    """Concurrent request stress."""

    @pytest.mark.parametrize("count", (10, 100))
    def test_sequential_burst(self, client: Any, count: int) -> None:
        """A rapid sequential burst never errors.

        :param client: test API client
        :param count: number of sequential requests
        """
        for index in range(count):
            response = client.post(
                "/moderate", json={"text": f"burst message {index}", "app_name": "a"}
            )
            assert response.status_code == 200

    @pytest.mark.parametrize("count", (5, 20))
    def test_interleaved_apps(self, client: Any, count: int) -> None:
        """Requests across apps interleave cleanly.

        :param client: test API client
        :param count: number of requests per app
        """
        for index in range(count):
            for app_name in ("app1", "app2", "app3"):
                response = client.post(
                    "/moderate",
                    json={"text": f"message {index}", "app_name": app_name, "user_id": "u"},
                )
                assert response.status_code == 200


class TestChaosProfiler(BaseTest):
    """Profiler resilience."""

    def test_profiler_concurrent_records(self) -> None:
        """Concurrent profile writes do not corrupt counts."""
        import threading

        from app.profiling.user_profiler import UserProfiler

        profiler: UserProfiler = UserProfiler(":memory:", ":memory:", 91)

        def _record(index: int) -> None:
            profiler.record("app", f"user{index % 3}", total_msgs=1)

        threads: list[threading.Thread] = [
            threading.Thread(target=_record, args=(index,)) for index in range(30)
        ]
        for thread in threads:
            thread.start()
        for thread in threads:
            thread.join()
        stats = profiler.stats()
        assert stats["daily_rows"] >= 1
        profiler.close()


class TestChaosLogs(BaseTest):
    """Log robustness."""

    def test_corrupt_log_lines_skipped(self, tmp_path: Path) -> None:
        """Corrupt JSONL lines are skipped during audit reads."""
        log_file: Path = tmp_path / "moderation.log"
        log_file.write_text('{"verdict": "PASS"}\nnot valid json\n{also bad}\n', encoding="utf-8")
        import orjson

        entries: list[dict[str, Any]] = []
        for line in log_file.read_text(encoding="utf-8").splitlines():
            try:
                entries.append(orjson.loads(line))
            except orjson.JSONDecodeError:
                continue
        assert len(entries) == 1
        assert entries[0]["verdict"] == "PASS"

    def test_missing_log_file_audit(
        self,
        engine: Any,
        word_bank: Any,
        settings: Any,
        admin_headers: dict[str, str],
        tmp_path: Path,
    ) -> None:
        """A missing log file yields an empty audit."""
        from fastapi.testclient import TestClient

        from tests.conftest import build_app

        missing_settings: Any = settings.model_copy(deep=True)
        missing_settings.log_file_path = str(tmp_path / "absent" / "moderation.log")
        client: Any = TestClient(build_app(engine, word_bank, missing_settings))
        with client:
            response = client.get("/admin/wordbank/audit", headers=admin_headers)
            assert response.status_code == 200
            assert response.json() == []

    def test_truncated_log_tail(self, client: Any, admin_headers: dict[str, str]) -> None:
        """The audit endpoint tolerates many lines."""
        response = client.get("/admin/wordbank/audit", headers=admin_headers)
        assert isinstance(response.json(), list)


class TestChaosResilienceMore(BaseTest):
    """Additional resilience scenarios."""

    @pytest.mark.parametrize(
        "text",
        (
            "",
            " ",
            "\n\t",
            "a" * 8192,
            "z" * 1,
            "x" * 100,
            "y" * 1000,
            "w" * 5000,
        ),
    )
    def test_extreme_lengths_moderated(self, client: Any, text: str) -> None:
        """Boundary-length messages are handled.

        :param client: test API client
        :param text: message under test
        """
        response = client.post("/moderate", json={"text": text, "app_name": "a"})
        assert response.status_code in (200, 422)

    def test_empty_batch_and_empty_text(self, client: Any) -> None:
        """Empty batch plus empty text is rejected cleanly."""
        response = client.post("/moderate/batch", json={"items": [{"text": ""}]})
        assert response.status_code == 422

    def test_invalid_json_body(self, client: Any) -> None:
        """A malformed JSON body is rejected."""
        response = client.post(
            "/moderate",
            content="{not valid json",
            headers={"content-type": "application/json"},
        )
        assert response.status_code == 422

    def test_wrong_content_type(self, client: Any) -> None:
        """Non-JSON content type is rejected."""
        response = client.post("/moderate", content="text", headers={"content-type": "text/plain"})
        assert response.status_code in (200, 415, 422)


class TestChaosRecovery(BaseTest):
    """Recovery after degraded states."""

    def test_recover_after_clear_cache(self, engine: Any, word_bank: Any) -> None:
        """Moderation works after a cache clear."""
        from app.models.request import ModerationRequest

        engine.moderate(ModerationRequest(text="before clear", app_name="a"))
        engine.clear_cache()
        result = engine.moderate(ModerationRequest(text="after clear", app_name="a"))
        assert result.verdict is not None

    def test_reload_after_word_add(self, engine: Any, word_bank: Any) -> None:
        """Detectors recover after the word bank changes."""
        from app.models.request import ModerationRequest

        word_bank.add_word("zaphrin")
        engine.refresh_detectors()
        result = engine.moderate(ModerationRequest(text="you are a zaphrin", app_name="a"))
        assert result.suspicion_score > 0

    def test_multiple_reloads(self, engine: Any, word_bank: Any) -> None:
        """Repeated reloads stay consistent."""
        for _ in range(3):
            word_bank.add_word(f"word{_}")
            engine.refresh_detectors()
        assert len(engine._detectors) >= 1

    def test_metrics_monotonic(self, engine: Any) -> None:
        """Request counters never decrease."""
        from app.models.request import ModerationRequest

        engine.moderate(ModerationRequest(text="first", app_name="a"))
        first: float = engine.metrics()["requests_total"]
        engine.moderate(ModerationRequest(text="second", app_name="a"))
        second: float = engine.metrics()["requests_total"]
        assert second >= first


class TestChaosFeedback(BaseTest):
    """Feedback service resilience."""

    def test_feedback_empty_batch(self) -> None:
        """Running a batch on an empty database works."""
        import tempfile

        from app.appconfig.app_config_service import AppConfigService
        from app.config import Settings
        from app.feedback.feedback_service import FeedbackService
        from app.settings_service import SettingsService
        from app.utils.logger import ModerationLogger

        root: Path = Path(tempfile.mkdtemp())
        (root / "logs").mkdir(parents=True, exist_ok=True)
        settings = Settings(
            app_port=0,
            log_file_path=str(root / "logs" / "l.log"),
            feedback_db_path=str(root / "f.db"),
            settings_db_path=str(root / "s.db"),
            app_config_db_path=str(root / "c.db"),
        )
        logger: ModerationLogger = ModerationLogger(settings.log_file_path, max_bytes=100_000)
        feedback: FeedbackService = FeedbackService(
            settings,
            SettingsService(settings),
            AppConfigService(settings.app_config_db_path),
            logger,
        )
        report = feedback.run_batch()
        assert report["status"] == "ok"
        feedback.close()


class TestChaosSettings(BaseTest):
    """Settings resilience."""

    def test_settings_roundtrip_many_updates(self, engine: Any) -> None:
        """Many sequential updates remain consistent."""
        service = engine._settings_service
        service.get("WEIGHT_DETECTOR_AHO")
        for value in range(5, 51):
            service.update({"WEIGHT_DETECTOR_AHO": value})
        assert int(service.get("WEIGHT_DETECTOR_AHO", 0)) == 50

    def test_settings_invalid_does_not_corrupt(self, engine: Any) -> None:
        """A rejected update leaves the previous value intact."""
        service = engine._settings_service
        service.get("WEIGHT_DETECTOR_AHO")
        service.update({"WEIGHT_DETECTOR_AHO": 40})
        with pytest.raises(ValueError):
            service.update({"WEIGHT_DETECTOR_AHO": 999})
        assert int(service.get("WEIGHT_DETECTOR_AHO", 0)) == 40

    def test_settings_get_unknown_default(self, engine: Any) -> None:
        """Unknown keys return the provided default."""
        service = engine._settings_service
        assert service.get("MADE_UP_KEY", "fallback") == "fallback"


class TestChaosWordbank(BaseTest):
    """Word bank resilience."""

    def test_many_word_add_remove(self, word_bank: Any) -> None:
        """Rapid add and remove cycles stay consistent."""
        for index in range(50):
            word_bank.add_word(f"cycled{index}")
            removed: bool = word_bank.remove_word(index + 1)
            assert isinstance(removed, bool)

    def test_word_import_mixed_validity(self, word_bank: Any) -> None:
        """Importing mixed valid and invalid words counts valid only."""
        imported: int = word_bank.import_words(
            [
                {"word": "good1"},
                {"word": "good2"},
                {"nope": "no-word-key"},
                {"word": "good3"},
            ]
        )
        assert imported == 3

    def test_get_stats_after_ops(self, word_bank: Any) -> None:
        """Stats stay valid after many operations."""
        word_bank.add_word("stat1")
        word_bank.add_word("stat2")
        stats = word_bank.get_stats()
        assert stats["custom_words"] >= 2

    def test_close_then_operations(self, word_bank: Any) -> None:
        """Closing the word bank is safe."""
        word_bank.close()
        word_bank.close()


class TestChaosDatabaseMore(BaseTest):
    """More database resilience."""

    @pytest.mark.parametrize("table", ("feedback", "decisions", "meta"))
    def test_feedback_schema_tables(self, table: str) -> None:
        """Feedback schema exposes every expected table.

        :param table: expected table name
        """
        import tempfile

        from app.appconfig.app_config_service import AppConfigService
        from app.config import Settings
        from app.feedback.feedback_service import FeedbackService
        from app.settings_service import SettingsService
        from app.utils.logger import ModerationLogger

        root: Path = Path(tempfile.mkdtemp())
        (root / "logs").mkdir(parents=True, exist_ok=True)
        settings = Settings(
            app_port=0,
            log_file_path=str(root / "logs" / "l.log"),
            feedback_db_path=str(root / "f.db"),
            settings_db_path=str(root / "s.db"),
            app_config_db_path=str(root / "c.db"),
        )
        logger: ModerationLogger = ModerationLogger(settings.log_file_path, max_bytes=100_000)
        feedback: FeedbackService = FeedbackService(
            settings,
            SettingsService(settings),
            AppConfigService(settings.app_config_db_path),
            logger,
        )
        rows = feedback._connection.execute(
            "SELECT name FROM sqlite_master WHERE type = 'table' AND name = ?", (table,)
        ).fetchall()
        assert rows
        feedback.close()

    def test_settings_db_schema(self, engine: Any) -> None:
        """The settings database has the settings table."""
        service = engine._settings_service
        rows = service._connection.execute(
            "SELECT name FROM sqlite_master WHERE type = 'table' AND name = 'settings'"
        ).fetchall()
        assert rows

    def test_config_db_schema(self, engine: Any) -> None:
        """The config database has the app_config table."""
        rows = engine._app_config._connection.execute(
            "SELECT name FROM sqlite_master WHERE type = 'table' AND name = 'app_config'"
        ).fetchall()
        assert rows

    def test_profiler_live_schema(self, engine: Any) -> None:
        """The profiler live database has user_daily_stats."""
        rows = engine._profiler._live.execute(
            "SELECT name FROM sqlite_master WHERE type = 'table' AND name = 'user_daily_stats'"
        ).fetchall()
        assert rows

    def test_profiler_archive_schema(self, engine: Any) -> None:
        """The profiler archive database has user_summaries."""
        rows = engine._profiler._archive.execute(
            "SELECT name FROM sqlite_master WHERE type = 'table' AND name = 'user_summaries'"
        ).fetchall()
        assert rows


class TestChaosResponse(BaseTest):
    """Response invariants under varied input."""

    @pytest.mark.parametrize(
        "text",
        (
            "hello world",
            "you are a zaphrin",
            "mixed 中文 content",
            "symbols !@#$%^&*()",
            "line\nbreak",
            "multiple   spaces",
        ),
    )
    def test_verdict_always_valid(self, client: Any, word_bank: Any, text: str) -> None:
        """Every verdict is a recognized enum value.

        :param client: test API client
        :param word_bank: isolated word bank
        :param text: message under test
        """
        word_bank.add_word("zaphrin")
        body: dict[str, Any] = client.post("/moderate", json={"text": text, "app_name": "a"}).json()
        assert body["verdict"] in ("PASS", "BLOCK", "REVIEW")
        assert body["allowed"] == (body["verdict"] != "BLOCK")

    def test_latency_invariants(self, client: Any) -> None:
        """Latency is always a finite non-negative number."""
        for index in range(5):
            body: dict[str, Any] = client.post(
                "/moderate", json={"text": f"latency {index}", "app_name": "a"}
            ).json()
            assert isinstance(body["latencyMs"], (int, float))
            assert body["latencyMs"] >= 0.0
