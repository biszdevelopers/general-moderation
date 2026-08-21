"""Test workbench endpoints (Phase 1).

Covers the ``/test`` router: detailed moderation traces (JSON and SSE),
the configuration playground, user profile seeding/lookup, the live
dashboard, and the load test runner.
"""

from __future__ import annotations

import asyncio
import json
from typing import Any

import pytest

from app.engine.moderation_engine import ModerationEngine
from app.models.request import ModerationRequest
from app.test.load_test import LoadTestConfig, run_load_test
from app.test.pipeline_trace import PipelineTrace
from tests.base_test import BaseTest


def _parse_sse(text: str) -> list[tuple[str, dict[str, Any]]]:
    """Parse a Server-Sent Events payload into (event, data) pairs."""
    frames: list[tuple[str, dict[str, Any]]] = []
    name: str | None = None
    data_lines: list[str] = []
    for line in text.splitlines():
        if line.startswith("event: "):
            name = line[len("event: ") :]
        elif line.startswith("data: "):
            data_lines.append(line[len("data: ") :])
        elif line == "" and name is not None:
            frames.append((name, json.loads("\n".join(data_lines))))
            name = None
            data_lines = []
    return frames


class TestModerateDetail(BaseTest):
    """The detailed moderation endpoint."""

    def test_trace_structure(self, client: Any, admin_headers: dict[str, str]) -> None:
        """A non-streaming detail call returns a complete trace."""
        response = client.post(
            "/test/moderate-detail",
            headers=admin_headers,
            json={"text": "hello world", "user_id": "u1", "app_name": "test"},
        )
        assert response.status_code == 200
        body: dict[str, Any] = response.json()
        assert "response" in body
        assert "trace" in body
        trace: dict[str, Any] = body["trace"]
        assert trace["verdict"] in ("PASS", "BLOCK", "REVIEW")
        assert set(trace) >= {
            "stage_1",
            "stage_2",
            "stage_3",
            "suspicion_score",
            "total_latency_ms",
        }
        assert isinstance(trace["stage_2"]["detector_results"], list)
        assert trace["stage_2"]["detector_results"]

    def test_requires_admin_key(self, client: Any) -> None:
        """The endpoint rejects requests without a valid admin key."""
        response = client.post("/test/moderate-detail", json={"text": "hello"})
        assert response.status_code == 401

    def test_stream_emits_stage_events(self, client: Any, admin_headers: dict[str, str]) -> None:
        """The streaming variant emits stage events then a complete event."""
        response = client.post(
            "/test/moderate-detail?stream=true",
            headers=admin_headers,
            json={"text": "hello world", "user_id": "u2"},
        )
        assert response.status_code == 200
        assert response.headers["content-type"].startswith("text/event-stream")
        frames: list[tuple[str, dict[str, Any]]] = _parse_sse(response.text)
        names: list[str] = [name for name, _ in frames]
        assert "stage1_complete" in names
        assert "stage2_complete" in names
        assert names[-1] == "complete"
        assert "trace" in dict(frames)["complete"]

    def test_engine_moderate_detailed_returns_trace(self, engine: ModerationEngine) -> None:
        """The engine method returns both a response and a PipelineTrace."""
        response, trace = engine.moderate_detailed(
            ModerationRequest(text="hello world", user_id="u3")
        )
        assert isinstance(trace, PipelineTrace)
        assert response.verdict.value == trace.verdict


class TestPipelineStatus(BaseTest):
    """The pipeline-status streaming endpoint."""

    def test_requires_admin_key(self, client: Any) -> None:
        """The endpoint rejects requests without a valid admin key."""
        response = client.get("/test/pipeline-status", params={"text": "hello"})
        assert response.status_code == 401

    def test_streams_events_in_order(self, client: Any, admin_headers: dict[str, str]) -> None:
        """The endpoint streams every stage event and finishes with a trace."""
        response = client.get(
            "/test/pipeline-status",
            headers=admin_headers,
            params={"text": "hello world", "user_id": "u6", "app_name": "default"},
        )
        assert response.status_code == 200
        assert response.headers["content-type"].startswith("text/event-stream")
        frames: list[tuple[str, dict[str, Any]]] = _parse_sse(response.text)
        names: list[str] = [name for name, _ in frames]
        assert names[0] == "stage1_complete"
        assert "detector_result" in names
        assert (
            names.index("stage1_complete")
            < names.index("stage2_complete")
            < names.index("stage3_complete")
            < names.index("complete")
        )
        assert names[-1] == "complete"
        complete: dict[str, Any] = dict(frames)["complete"]
        assert set(complete["trace"]) >= {
            "stage_1",
            "stage_2",
            "stage_3",
            "verdict",
            "suspicion_score",
        }
        assert complete["trace"]["stage_2"]["detector_results"]

    def test_matches_moderate_detail_verdict(
        self, client: Any, admin_headers: dict[str, str]
    ) -> None:
        """The streamed trace agrees with the non-streaming detail response."""
        detail = client.post(
            "/test/moderate-detail",
            headers=admin_headers,
            json={"text": "hello world", "user_id": "u7"},
        ).json()
        stream = client.get(
            "/test/pipeline-status",
            headers=admin_headers,
            params={"text": "hello world", "user_id": "u7"},
        )
        frames: list[tuple[str, dict[str, Any]]] = _parse_sse(stream.text)
        trace: dict[str, Any] = dict(frames)["complete"]["trace"]
        assert trace["verdict"] == detail["trace"]["verdict"]
        assert trace["suspicion_score"] == detail["trace"]["suspicion_score"]
        assert [run["name"] for run in trace["stage_2"]["detector_results"]] == [
            run["name"] for run in detail["trace"]["stage_2"]["detector_results"]
        ]

    def test_validates_text(self, client: Any, admin_headers: dict[str, str]) -> None:
        """A missing or overlong text is rejected with 422."""
        missing = client.get("/test/pipeline-status", headers=admin_headers)
        assert missing.status_code == 422
        overlong = client.get(
            "/test/pipeline-status",
            headers=admin_headers,
            params={"text": "x" * 8193},
        )
        assert overlong.status_code == 422


class TestDetectorToggles(BaseTest):
    """Runtime detector toggles affect the detailed pipeline."""

    def test_disabled_detector_is_recorded(self, engine: ModerationEngine) -> None:
        """Disabling a detector is reflected in the trace."""
        engine._settings_service.update({"ENABLE_DETECTOR_ROLLING_HASH": False})
        _response, trace = engine.moderate_detailed(
            ModerationRequest(text="hello world", user_id="u4")
        )
        names: dict[str, bool] = {run.name: run.enabled for run in trace.stage_2.detector_results}
        assert names["rolling_hash"] is False
        assert names["bloom_filter"] is True

    def test_reenable_restores_detector(self, engine: ModerationEngine) -> None:
        """Re-enabling a detector restores it for the next run."""
        engine._settings_service.update({"ENABLE_DETECTOR_ROLLING_HASH": True})
        _response, trace = engine.moderate_detailed(
            ModerationRequest(text="hello world", user_id="u5")
        )
        names: dict[str, bool] = {run.name: run.enabled for run in trace.stage_2.detector_results}
        assert names["rolling_hash"] is True


class TestConfigPlayground(BaseTest):
    """The configuration playground endpoints."""

    def test_get_config_returns_catalog(self, client: Any, admin_headers: dict[str, str]) -> None:
        """GET /test/config returns the editable settings catalog."""
        response = client.get("/test/config", headers=admin_headers)
        assert response.status_code == 200
        settings = response.json()["settings"]
        keys: set[str] = {entry["key"] for entry in settings}
        assert "WEIGHT_DETECTOR_AHO" in keys
        assert "ENABLE_DETECTOR_AHO_CORASICK" in keys

    def test_post_config_applies_immediately(
        self, client: Any, admin_headers: dict[str, str]
    ) -> None:
        """POST /test/config persists a weight change."""
        response = client.post(
            "/test/config",
            headers=admin_headers,
            json={"settings": {"WEIGHT_DETECTOR_AHO": 35}},
        )
        assert response.status_code == 200
        assert "WEIGHT_DETECTOR_AHO" in response.json()["updated"]
        get_response = client.get("/test/config", headers=admin_headers)
        settings = get_response.json()["settings"]
        value = next(s["value"] for s in settings if s["key"] == "WEIGHT_DETECTOR_AHO")
        assert value == 35

    def test_post_config_rejects_unknown_key(
        self, client: Any, admin_headers: dict[str, str]
    ) -> None:
        """POST /test/config rejects unknown settings."""
        response = client.post(
            "/test/config",
            headers=admin_headers,
            json={"settings": {"NOT_A_SETTING": 1}},
        )
        assert response.status_code == 400

    def test_config_redacts_secret_values(self, client: Any, admin_headers: dict[str, str]) -> None:
        """The settings catalog never exposes credential values."""
        response = client.get("/test/config", headers=admin_headers)
        settings: list[dict[str, Any]] = response.json()["settings"]
        for entry in settings:
            if entry["key"].endswith(("_KEY", "_SECRET")):
                assert entry["value"] == "********"
                if entry["key"] not in ("OPENAI_API_KEY", "ANTHROPIC_API_KEY"):
                    assert entry["editable"] is False


class TestUserProfile(BaseTest):
    """User profile simulation endpoints."""

    def test_seed_and_lookup(self, client: Any, admin_headers: dict[str, str]) -> None:
        """Seeding history is reflected in the profile lookup."""
        seed = client.post(
            "/test/user-profile/seed",
            headers=admin_headers,
            json={"app_name": "app1", "user_id": "sim-user", "total_msgs": 50, "flagged_msgs": 25},
        )
        assert seed.status_code == 200
        lookup = client.get(
            "/test/user-profile",
            headers=admin_headers,
            params={"app_name": "app1", "user_id": "sim-user"},
        )
        assert lookup.status_code == 200
        profile: dict[str, Any] = lookup.json()
        assert profile["total_msgs"] == 50
        assert profile["flagged_msgs"] == 25
        assert profile["ratio"] == pytest.approx(0.5)

    def test_lookup_requires_user_id(self, client: Any, admin_headers: dict[str, str]) -> None:
        """A missing user id is rejected."""
        response = client.get("/test/user-profile", headers=admin_headers, params={})
        assert response.status_code == 400


class TestDashboard(BaseTest):
    """The live dashboard endpoint."""

    def test_dashboard_shape(self, client: Any, admin_headers: dict[str, str]) -> None:
        """The dashboard returns aggregated metrics for today."""
        post = client.post(
            "/test/moderate-detail", headers=admin_headers, json={"text": "hello world"}
        )
        assert post.status_code == 200, post.text
        response = client.get("/test/dashboard", headers=admin_headers)
        assert response.status_code == 200
        body: dict[str, Any] = response.json()
        assert body["total_requests_today"] >= 1
        assert set(body) >= {
            "block_rate",
            "avg_latency_ms",
            "llm_invocation_rate",
            "top_detectors",
            "requests_over_time",
            "metrics",
        }


class TestLoadTest(BaseTest):
    """The load test runner."""

    def test_run_load_test(self, engine: ModerationEngine) -> None:
        """The runner completes and reports accurate totals."""
        config: LoadTestConfig = LoadTestConfig(
            concurrent_users=4,
            requests_per_user=5,
            text_source="corpus",
            corpus=["hello world", "I will kill you tonight", "thanks for the update"],
            user_prefix="lt",
        )

        async def collect() -> list[tuple[str, dict[str, Any]]]:
            return [(name, data) async for name, data in run_load_test(engine, config)]

        events: list[tuple[str, dict[str, Any]]] = asyncio.run(collect())
        assert events
        assert events[-1][0] == "complete"
        result: dict[str, Any] = events[-1][1]
        assert result["total_requests"] == 20
        assert result["successful_requests"] + result["failed_requests"] == 20
        assert result["max_concurrency_reached"] == 4
        assert set(result["latency_percentiles"]) == {"p50", "p95", "p99"}
        assert "PASS" in result["verdicts"]
