"""Load test simulation for the moderation pipeline.

Simulates ``concurrent_users`` users, each sending ``requests_per_user``
messages. Users run in parallel and each user sends its requests sequentially,
mirroring realistic mixed traffic. The runner is an async generator so progress
can be streamed over SSE while the test is still executing.

The engine's ``moderate_detailed`` path is used (cache bypassed) so every
request exercises the detectors against the current runtime settings.
"""

from __future__ import annotations

import asyncio
import random
import time
from collections import Counter
from collections.abc import AsyncIterator
from typing import Any, Literal

from pydantic import BaseModel, Field
from starlette.concurrency import run_in_threadpool

from app.models.request import ModerationRequest

_SAFE_TEXTS: tuple[str, ...] = (
    "hello world",
    "nice to meet you",
    "the weather is great today",
    "thanks for the update",
    "sounds good to me",
    "see you tomorrow",
    "can we meet at three",
    "please review my application",
    "looking forward to the event",
    "that is a great question",
    "i agree with the proposal",
    "have a nice weekend",
)

_RISKY_TEXTS: tuple[str, ...] = (
    "I will kill you tonight",
    "The government is corrupt",
    "Send nudes now",
    "Buy this product now limited time offer",
    "You are a stupid idiot",
    "Bomb the building",
    "Explicit sexual content here",
    "Here is my credit card number 4111111111111111",
    "Racial slurs against them",
    "Election fraud everywhere",
)


class LoadTestConfig(BaseModel):
    """Configuration for one load test run.

    :param concurrent_users: number of parallel simulated users
    :param requests_per_user: messages each user sends
    :param text_source: where the messages come from
    :param corpus: messages used when text_source is "corpus"
    :param custom_texts: messages used when text_source is "custom"
    :param app_name: application name used for every request
    :param user_prefix: generated user IDs start with this
    """

    concurrent_users: int = Field(default=10, ge=1, le=1000)
    requests_per_user: int = Field(default=10, ge=1, le=100)
    text_source: Literal["random", "corpus", "custom"] = "random"
    corpus: list[str] = Field(default_factory=list)
    custom_texts: list[str] = Field(default_factory=list)
    app_name: str = "default"
    user_prefix: str = "loadtest"


class LoadTestResult(BaseModel):
    """Aggregated result of one load test run.

    :param total_requests: requests issued
    :param successful_requests: requests that returned a verdict
    :param failed_requests: requests that raised
    :param total_duration_ms: wall time of the whole run
    :param requests_per_second: completed requests per second
    :param latency_percentiles: p50/p95/p99 latency in milliseconds
    :param max_concurrency_reached: peak in-flight requests
    :param llm_invocation_count: requests that consulted the LLM
    :param error_distribution: exception type to count
    :param verdicts: PASS/BLOCK/REVIEW counts
    """

    total_requests: int
    successful_requests: int
    failed_requests: int
    total_duration_ms: float
    requests_per_second: float
    latency_percentiles: dict[str, float]
    max_concurrency_reached: int
    llm_invocation_count: int
    error_distribution: dict[str, int]
    verdicts: dict[str, int]


def _percentile(sorted_values: list[float], percentile: float) -> float:
    """Return the value at a percentile of an ascending list.

    :param sorted_values: sorted latency samples
    :param percentile: percentile in 0-100
    :return: the value at that percentile, or 0.0 when empty
    """
    if not sorted_values:
        return 0.0
    index: int = min(len(sorted_values) - 1, round((percentile / 100.0) * (len(sorted_values) - 1)))
    return round(sorted_values[index], 3)


def _pick_text(config: LoadTestConfig, pool: list[str], index: int) -> str:
    """Select the message for one request.

    :param config: the load test configuration
    :param pool: the resolved message pool
    :param index: request sequence number for corpus/custom cycling
    :return: the message text
    """
    if config.text_source in ("corpus", "custom"):
        if not pool:
            return "hello world"
        return pool[index % len(pool)]
    if random.random() < 0.65:
        return random.choice(_SAFE_TEXTS)
    return random.choice(_RISKY_TEXTS)


async def run_load_test(
    engine: Any, config: LoadTestConfig
) -> AsyncIterator[tuple[str, dict[str, Any]]]:
    """Execute a load test, yielding ``(event_name, payload)`` pairs.

    Events: ``progress`` while the test runs, then a final ``complete`` event
    with the aggregated :class:`LoadTestResult`.

    :param engine: the moderation engine
    :param config: the load test configuration
    """
    total: int = config.concurrent_users * config.requests_per_user
    pool: list[str] = [
        text
        for text in (config.corpus if config.text_source == "corpus" else config.custom_texts)
        if text.strip()
    ]
    latencies: list[float] = []
    verdicts: Counter[str] = Counter()
    errors: Counter[str] = Counter()
    completed: int = 0
    failed: int = 0
    llm_invocations: int = 0
    in_flight: int = 0
    peak: int = 0
    start: float = time.monotonic()
    last_progress: int = 0
    last_yield: float = time.monotonic()
    progress_interval: int = max(1, total // 100)
    semaphore: asyncio.Semaphore = asyncio.Semaphore(config.concurrent_users)

    async def run_one(user_id: str, text: str) -> None:
        """Run one request through the engine and record its outcome."""
        nonlocal llm_invocations, completed, failed
        started: float = time.perf_counter()
        try:
            response, _trace = await run_in_threadpool(
                engine.moderate_detailed,
                ModerationRequest(app_name=config.app_name, user_id=user_id, text=text),
                None,
                False,
            )
            latencies.append((time.perf_counter() - started) * 1000.0)
            verdicts[response.verdict.value] += 1
            completed += 1
            if response.ai_triggered:
                llm_invocations += 1
        except Exception as exc:
            errors[type(exc).__name__] += 1
            failed += 1

    async def run_user(user_id: str) -> None:
        """Send one user's requests sequentially under the concurrency cap."""
        nonlocal in_flight, peak
        async with semaphore:
            in_flight += 1
            peak = max(peak, in_flight)
            try:
                for index in range(config.requests_per_user):
                    await run_one(user_id, _pick_text(config, pool, index))
            finally:
                in_flight -= 1

    def progress() -> dict[str, Any]:
        """Snapshot the current running totals for a progress event."""
        done: int = completed + failed
        elapsed: float = time.monotonic() - start
        ordered: list[float] = sorted(latencies)
        return {
            "completed": done,
            "total": total,
            "elapsed_ms": round(elapsed * 1000.0, 1),
            "rps": round(done / elapsed, 2) if elapsed > 0 else 0.0,
            "p50": _percentile(ordered, 50),
            "p95": _percentile(ordered, 95),
            "p99": _percentile(ordered, 99),
            "errors": failed,
            "llm_invocations": llm_invocations,
            "verdicts": dict(verdicts),
        }

    tasks: list[asyncio.Task[None]] = [
        asyncio.create_task(run_user(f"{config.user_prefix}-{index}"))
        for index in range(config.concurrent_users)
    ]
    while any(not task.done() for task in tasks):
        now: float = time.monotonic()
        if completed - last_progress >= progress_interval or now - last_yield >= 0.5:
            yield "progress", progress()
            last_progress = completed
            last_yield = now
        await asyncio.sleep(0.05)
    await asyncio.gather(*tasks)

    elapsed = time.monotonic() - start
    ordered = sorted(latencies)
    result: LoadTestResult = LoadTestResult(
        total_requests=total,
        successful_requests=completed,
        failed_requests=failed,
        total_duration_ms=round(elapsed * 1000.0, 3),
        requests_per_second=round(completed / elapsed, 2) if elapsed > 0 else 0.0,
        latency_percentiles={
            "p50": _percentile(ordered, 50),
            "p95": _percentile(ordered, 95),
            "p99": _percentile(ordered, 99),
        },
        max_concurrency_reached=peak,
        llm_invocation_count=llm_invocations,
        error_distribution=dict(errors),
        verdicts=dict(verdicts),
    )
    yield "complete", result.model_dump()
