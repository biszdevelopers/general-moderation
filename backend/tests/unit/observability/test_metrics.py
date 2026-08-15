"""Unit tests for the Prometheus text-format metrics renderer."""

from __future__ import annotations

import pytest

from app.observability.metrics import Histogram, render_prometheus


def test_histogram_percentiles_over_window() -> None:
    """p50/p95/p99 are computed over the retained samples."""
    histogram: Histogram = Histogram(max_samples=100)
    for value in (1, 2, 3, 4, 5, 6, 7, 8, 9, 10):
        histogram.observe(value / 1000.0)
    percentiles: dict[str, float] = histogram._percentiles()
    assert percentiles["p50"] == pytest.approx(0.0055, abs=0.001)
    assert percentiles["p95"] == pytest.approx(0.0095, abs=0.001)
    assert percentiles["p99"] == pytest.approx(0.0099, abs=0.001)


def test_histogram_window_is_bounded() -> None:
    """Old samples are evicted once the window fills."""
    histogram: Histogram = Histogram(max_samples=10)
    for index in range(50):
        histogram.observe(index / 1000.0)
    assert len(histogram._samples) == 10
    assert histogram._samples[0] == pytest.approx(40 / 1000.0)


def test_histogram_empty_window() -> None:
    """An empty histogram renders zero values and no crash."""
    lines: list[str] = Histogram().render("request_latency", "help")
    text: str = "\n".join(lines)
    assert 'request_latency_seconds_bucket{le="+Inf"} 0' in text
    assert "request_latency_seconds_sum 0" in text


def test_render_prometheus_exposition_format() -> None:
    """Counters, histograms, and gauges serialize in exposition format."""
    histogram: Histogram = Histogram()
    histogram.observe(0.001)
    text: str = render_prometheus(
        counters={"requests_total": 1.0, "cache_hits_total": 2.0},
        histograms={"request_latency": histogram},
        gauges={"cache_hit_rate": 0.75},
        help_text={"request_latency": "total moderation request latency"},
    )
    assert "# TYPE requests_total counter" in text
    assert "# TYPE request_latency_seconds histogram" in text
    assert "# TYPE cache_hit_rate gauge" in text
    assert "# HELP request_latency_seconds total moderation request latency" in text
    assert text.endswith("\n")


def test_render_prometheus_sorted_output() -> None:
    """Names are emitted in sorted order for stable diffs."""
    text: str = render_prometheus(
        counters={"zebra": 1.0, "alpha": 1.0}, histograms={}, gauges={}
    )
    assert text.index("# HELP alpha") < text.index("# HELP zebra")
