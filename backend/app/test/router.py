"""Test workbench endpoints.

All routes live under ``/test`` and are guarded by the admin API key. They
expose the engine's internal pipeline state for the interactive test
workbench: detailed moderation traces with streaming progress, load testing,
the configuration playground, per-user profile views, and a live dashboard.

None of these endpoints modify production detection logic; they read and
exercise the existing engine.
"""

from __future__ import annotations

import json
import queue
import threading
from collections import Counter
from datetime import UTC, datetime
from pathlib import Path
from typing import Annotated, Any

import orjson
from fastapi import APIRouter, HTTPException, Query, status
from pydantic import BaseModel, Field
from starlette.concurrency import run_in_threadpool
from starlette.responses import StreamingResponse

from app.engine.moderation_engine import ModerationEngine
from app.models.request import ModerationRequest
from app.test.load_test import LoadTestConfig, run_load_test

_SSE_HEADERS: dict[str, str] = {
    "Cache-Control": "no-cache",
    "Connection": "keep-alive",
    "X-Accel-Buffering": "no",
}


def _sse(event: str, payload: dict[str, Any]) -> str:
    """Render one Server-Sent Events frame.

    :param event: the event name
    :param payload: the JSON payload
    :return: the SSE frame text
    """
    body: str = json.dumps(payload, ensure_ascii=False, default=str)
    return f"event: {event}\ndata: {body}\n\n"


def _stream_pipeline(engine: ModerationEngine, payload: ModerationRequest) -> StreamingResponse:
    """Run a detailed moderation in a worker thread and stream its events.

    Every stage completion is pushed through a thread-safe queue and emitted
    as an SSE frame in pipeline order: ``stage1_complete``, one
    ``detector_result`` per detector, ``stage2_complete``,
    ``stage3_complete``, then ``complete`` (or ``error`` when the pipeline
    raises). Both ``moderate-detail?stream=true`` and ``pipeline-status``
    share this single ordering path.

    :param engine: the moderation engine
    :param payload: the moderation request to run
    :return: a text/event-stream response
    """
    events: queue.Queue[tuple[str | None, dict[str, Any] | None]] = queue.Queue()

    def worker() -> None:
        """Run the pipeline and publish every stage event to the queue."""
        try:
            engine.moderate_detailed(
                payload,
                event_sink=lambda name, data: events.put((name, data)),
            )
        except Exception as exc:
            events.put(("error", {"detail": str(exc)}))
        finally:
            events.put((None, None))

    threading.Thread(target=worker, daemon=True).start()

    def generate() -> Any:
        """Yield the buffered events as SSE frames as they arrive."""
        while True:
            name, data = events.get()
            if name is None:
                break
            yield _sse(name, data or {})

    return StreamingResponse(generate(), media_type="text/event-stream", headers=_SSE_HEADERS)


class ConfigUpdateRequest(BaseModel):
    """A batch of runtime settings to update.

    :param settings: settings key to value mapping
    """

    settings: dict[str, Any]


class SeedProfileRequest(BaseModel):
    """A request to seed simulated user history.

    :param app_name: application name
    :param user_id: user identifier
    :param total_msgs: messages to record
    :param flagged_msgs: flagged messages within that total
    """

    app_name: str = "default"
    user_id: str = Field(min_length=1, max_length=256)
    total_msgs: int = Field(default=50, ge=1, le=1000)
    flagged_msgs: int = Field(default=0, ge=0, le=1000)


def _dashboard(engine: ModerationEngine, log_file_path: str) -> dict[str, Any]:  # noqa: C901
    """Aggregate today's audit records into dashboard metrics.

    :param engine: the moderation engine
    :param log_file_path: path to the JSONL audit log
    :return: counters, rates, top detectors, and per-bucket request counts
    """
    today_prefix: str = datetime.now(UTC).date().isoformat()
    path: Path = Path(log_file_path)
    total: int = 0
    blocked: int = 0
    llm: int = 0
    latencies: list[float] = []
    detector_counts: Counter[str] = Counter()
    buckets: Counter[str] = Counter()
    if path.is_file():
        for line in reversed(path.read_text(encoding="utf-8").splitlines()):
            try:
                record: dict[str, Any] = orjson.loads(line)
            except (orjson.JSONDecodeError, ValueError):
                continue
            timestamp: str = str(record.get("timestamp", ""))
            if not timestamp.startswith(today_prefix):
                if timestamp and timestamp < today_prefix:
                    break
                continue
            if record.get("message") != "moderation_decision":
                continue
            total += 1
            if record.get("verdict") == "BLOCK":
                blocked += 1
            if record.get("aiTriggered"):
                llm += 1
            latency: Any = record.get("latencyMs")
            if isinstance(latency, (int, float)):
                latencies.append(float(latency))
            for name in record.get("detectorChain") or []:
                detector_counts[str(name)] += 1
            buckets[timestamp[11:16]] += 1
    return {
        "total_requests_today": total,
        "blocked_today": blocked,
        "block_rate": round(blocked / total, 4) if total else 0.0,
        "avg_latency_ms": round(sum(latencies) / len(latencies), 2) if latencies else 0.0,
        "llm_invocations_today": llm,
        "llm_invocation_rate": round(llm / total, 4) if total else 0.0,
        "top_detectors": [
            {"name": name, "count": count} for name, count in detector_counts.most_common(8)
        ],
        "requests_over_time": [
            {"bucket": key, "count": count} for key, count in sorted(buckets.items())
        ],
        "metrics": engine.metrics(),
    }


def create_test_router(  # noqa: C901 - router factory with many sub-routes
    engine: ModerationEngine,
    log_file_path: str,
    auth_dependency: Any,
) -> APIRouter:
    """Build the test workbench router.

    :param engine: the moderation engine
    :param log_file_path: path to the audit log file
    :param auth_dependency: FastAPI dependency guarding the routes
    :return: the configured APIRouter
    """
    router: APIRouter = APIRouter(prefix="/test", tags=["test"], dependencies=[auth_dependency])

    @router.post("/moderate-detail")
    async def moderate_detail(payload: ModerationRequest, stream: bool = False) -> Any:
        """Run the pipeline with a full trace.

        :param payload: the moderation request
        :param stream: when True, return the trace as an SSE stream
        :return: the response and trace, or a streaming response
        """
        if not stream:
            response, trace = await run_in_threadpool(engine.moderate_detailed, payload)
            return {
                "response": response.model_dump(by_alias=True),
                "trace": trace.to_dict(),
            }

        return _stream_pipeline(engine, payload)

    @router.get("/pipeline-status")
    async def pipeline_status(
        text: Annotated[str, Query(min_length=1, max_length=8192)],
        user_id: Annotated[str | None, Query(min_length=1, max_length=256)] = None,
        app_name: Annotated[str | None, Query(min_length=1, max_length=64)] = None,
    ) -> Any:
        """Stream one moderation pipeline run as Server-Sent Events.

        Accepts the message as a query parameter and emits the identical event
        sequence as ``POST /test/moderate-detail?stream=true``:
        ``stage1_complete``, one ``detector_result`` per detector,
        ``stage2_complete``, ``stage3_complete``, then ``complete`` with the
        full trace.

        :param text: the message to moderate (1-8192 characters)
        :param user_id: optional caller-supplied user identifier
        :param app_name: optional calling application name
        :return: a text/event-stream response ending in a complete trace
        """
        return _stream_pipeline(
            engine,
            ModerationRequest(text=text, user_id=user_id, app_name=app_name),
        )

    @router.post("/load-test")
    async def load_test(payload: LoadTestConfig) -> Any:
        """Run a load test, streaming progress over SSE.

        :param payload: the load test configuration
        :return: an SSE stream ending with the aggregated result
        """

        async def generate() -> Any:
            async for name, data in run_load_test(engine, payload):
                yield _sse(name, data)

        return StreamingResponse(generate(), media_type="text/event-stream", headers=_SSE_HEADERS)

    @router.get("/dashboard")
    def dashboard() -> dict[str, Any]:
        """Return the live dashboard metrics.

        :return: aggregated metrics for today
        """
        return _dashboard(engine, log_file_path)

    @router.get("/config")
    def get_config() -> dict[str, Any]:
        """Return the full settings catalog for the configuration playground.

        :return: the settings with type, description, and editability flags
        """
        return {"settings": engine._settings_service.describe()}

    @router.post("/config")
    def update_config(payload: ConfigUpdateRequest) -> dict[str, Any]:
        """Validate and apply a batch of settings immediately.

        :param payload: the settings to update
        :return: the keys that changed
        :raises HTTPException: 400 for an unknown, read-only, or invalid value
        """
        try:
            updated: dict[str, Any] = engine._settings_service.update(payload.settings)
        except ValueError as exc:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(exc)) from exc
        return {"status": "ok", "updated": list(updated.keys())}

    @router.get("/user-profile")
    def user_profile(app_name: str = "default", user_id: str = "") -> dict[str, Any]:
        """Return one user's profiling history and aggregates.

        :param app_name: application name
        :param user_id: user identifier
        :return: daily rows, summaries, ratio, and totals
        """
        if not user_id:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST, detail="user_id is required"
            )
        profile: dict[str, Any] = engine._profiler.get_profile(app_name, user_id)
        total: int = sum(row["total_msgs"] for row in profile["daily"]) + sum(
            summary["total_msgs"] for summary in profile["summaries"]
        )
        flagged: int = sum(row["flagged_msgs"] for row in profile["daily"]) + sum(
            summary["flagged_msgs"] for summary in profile["summaries"]
        )
        blocked: int = sum(row["blocked_msgs"] for row in profile["daily"]) + sum(
            summary["blocked_msgs"] for summary in profile["summaries"]
        )
        return {
            **profile,
            "total_msgs": total,
            "flagged_msgs": flagged,
            "blocked_msgs": blocked,
        }

    @router.post("/user-profile/seed")
    def seed_profile(payload: SeedProfileRequest) -> dict[str, str]:
        """Record simulated user history for profile experiments.

        :param payload: the profile seed parameters
        :return: a status acknowledgment
        """
        engine._profiler.record(
            app_name=payload.app_name,
            user_id=payload.user_id,
            total_msgs=payload.total_msgs,
            flagged_msgs=payload.flagged_msgs,
            blocked_msgs=0,
        )
        return {"status": "seeded"}

    return router
