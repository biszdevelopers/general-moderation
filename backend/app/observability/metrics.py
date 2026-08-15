"""Small Prometheus text-format renderer.

Serializes counters, gauges, and windowed latency histograms into the
Prometheus exposition format (``text/plain; version=0.0.4``) without pulling
in the ``prometheus-client`` dependency. Histograms are built from a bounded
sample window so p50/p95/p99 are computed over recent requests instead of
retaining every sample forever.
"""

from __future__ import annotations

import statistics

_LATENCY_BUCKETS: tuple[float, ...] = (
    0.0005, 0.001, 0.0025, 0.005, 0.01, 0.025, 0.05, 0.1, 0.25, 0.5, 1.0, 2.5, 5.0, 10.0, 30.0
)


class Histogram:
    """A bounded-window latency histogram.

    :param buckets: ascending upper bounds (seconds); +Inf is implied
    :param max_samples: how many recent samples to retain
    """

    def __init__(
        self, buckets: tuple[float, ...] = _LATENCY_BUCKETS, max_samples: int = 10_000
    ) -> None:
        self._buckets: tuple[float, ...] = buckets
        self._max: int = max_samples
        self._samples: list[float] = []

    def observe(self, seconds: float) -> None:
        """Record one latency sample, evicting the oldest when full."""
        self._samples.append(seconds)
        if len(self._samples) > self._max:
            self._samples.pop(0)

    def render(self, name: str, help_text: str, unit: str = "seconds") -> list[str]:
        """Emit the histogram and its percentile gauges as text lines.

        :param name: metric name prefix (e.g. ``request_latency``)
        :param help_text: one-line HELP text
        :param unit: metric suffix, "seconds" or "ms"
        :return: the Prometheus exposition lines
        """
        lines: list[str] = [
            f"# HELP {name}_{unit} {help_text}",
            f"# TYPE {name}_{unit} histogram",
        ]
        count: int = len(self._samples)
        cumulative: int = 0
        for bound in self._buckets:
            cumulative += sum(1 for sample in self._samples if sample <= bound)
            lines.append(f'{name}_{unit}_bucket{{le="{bound}"}} {cumulative}')
        lines.append(f'{name}_{unit}_bucket{{le="+Inf"}} {count}')
        lines.append(f"{name}_{unit}_sum {sum(self._samples):g}")
        lines.append(f"{name}_{unit}_count {count}")
        for quantile, value in self._percentiles().items():
            lines.append(f"# TYPE {name}_{unit}_{quantile} gauge")
            lines.append(f"{name}_{unit}_{quantile} {value:g}")
        return lines

    def _percentiles(self) -> dict[str, float]:
        """Return p50/p95/p99 over the retained window."""
        if not self._samples:
            return {"p50": 0.0, "p95": 0.0, "p99": 0.0}
        ordered: list[float] = sorted(self._samples)
        return {
            "p50": statistics.quantiles(ordered, n=100)[49],
            "p95": statistics.quantiles(ordered, n=100)[94],
            "p99": statistics.quantiles(ordered, n=100)[98],
        }


def render_prometheus(
    counters: dict[str, float],
    histograms: dict[str, Histogram],
    gauges: dict[str, float],
    help_text: dict[str, str] | None = None,
) -> str:
    """Render counters, histograms, and gauges to the Prometheus text format.

    :param counters: name to value mapping for monotonic counters
    :param histograms: name to latency histogram mapping
    :param gauges: name to value mapping for gauges
    :param help_text: optional HELP strings keyed by metric name
    :return: the full exposition payload
    """
    helps: dict[str, str] = help_text or {}
    lines: list[str] = []
    for name in sorted(counters):
        lines.append(f"# HELP {name} {helps.get(name, name.replace('_', ' '))}")
        lines.append(f"# TYPE {name} counter")
        lines.append(f"{name} {counters[name]:g}")
    for name in sorted(histograms):
        lines.extend(histograms[name].render(name, helps.get(name, name.replace("_", " "))))
    for name in sorted(gauges):
        lines.append(f"# HELP {name} {helps.get(name, name.replace('_', ' '))}")
        lines.append(f"# TYPE {name} gauge")
        lines.append(f"{name} {gauges[name]:g}")
    return "\n".join(lines) + "\n"
