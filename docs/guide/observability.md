# Observability

The service ships production observability out of the box: a Prometheus
scrape endpoint, structured JSONL decision logs with per-stage and
per-detector latency, and ready-to-import alert rules and a Grafana
dashboard. All metrics are rendered by the service itself — no external
agent is required to collect them.

## Metrics endpoint

`GET /metrics` exposes the full Prometheus exposition
(`text/plain; version=0.0.4`) without authentication. It is gated by the
`METRICS_ENABLED` setting (default on).

The payload includes:

- **Counters** — `requests_total` (plus `requests_pass_total` /
  `requests_block_total` / `requests_review_total`), `ai_requests_total`,
  `rate_limit_hits_total`, `stage1_fast_path_total`, `semantic_queries_total`,
  `model_unavailable_total`, `review_escalations_total`,
  `requests_errors_total`, `cache_hits_total`, `cache_misses_total`, and
  `detector_<name>_seconds_total` per detector.
- **Latency histograms** — `request_latency_seconds`,
  `stage1_latency_seconds`, `stage2_latency_seconds`, and
  `detector_<name>_latency_seconds`, each with Prometheus bucket series plus
  `_p50` / `_p95` / `_p99` gauges computed over a bounded recent window.
- **Gauges** — `model_available`, `semantic_available`, `semantic_ready`,
  `cache_size`, `cache_max_size`, and `cache_hit_rate`.

## Alert rules

`observability/prometheus-alerts.yml` contains alert rules for the failure
modes that matter:

- **Moderation5xxHigh** — 5xx responses above 5% of traffic for 5 minutes.
- **ModelUnavailable** — the local LLM is not loaded; Stage 3 runs fail-open.
- **ReviewEscalationSpike** — an abnormal rate of REVIEW escalations (possible
  threshold drift or abuse).
- **RateLimitHitsHigh** — clients are being throttled frequently.
- **SemanticStageDown** — semantic deps installed but the model has not
  finished loading.

Load the file in Prometheus (e.g. via `rule_files` in `prometheus.yml`).

## Grafana dashboard

`observability/grafana-dashboard.json` is a ready-to-import dashboard covering
request rate by verdict, request/stage latency percentiles, cache hit rate,
model and semantic availability, error rate, and semantic/LLM activity.
Import it from Grafana → Dashboards → Import, choosing your Prometheus data
source when prompted.

## Structured decision logs

Every moderation decision is written to the JSONL audit log
(`MODERATION_LOG_FILE_PATH`, default `./logs/moderation.log`) with the message
`moderation_decision`. Beyond the long-standing fields (`verdict`,
`suspicionScore`, `latencyMs`, `detectorChain`, `severity`, `category`), each
record now carries:

- `stage1Ms` / `stage2Ms` — wall time per pipeline stage.
- `detectorLatenciesMs` — a map of detector name to wall time for the
  detectors that ran on that request.

Text is never logged raw; only a SHA-256 hash and a 50-character preview are
stored. Query the log with any JSONL tool, for example:

```bash
# Last 20 decisions with their stage breakdown
Get-Content backend/logs/moderation.log | Where-Object { $_ -match '"message":"moderation_decision"' } | Select-Object -Last 20
```
