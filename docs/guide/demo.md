# Demo Excellence

One command boots the whole system, proves the accuracy numbers, pre-warms the
model and semantic layer, and opens the admin console and workbench — so the
audience never watches a cold start.

## One-command demo

```bash
npm run demo
```

What it does:

1. **Builds the frontend** once if `frontend/dist/index.html` is missing.
2. **Runs the accuracy gate** (`npm run eval`) so the raw numbers
   (accuracy/precision/recall/F1 = 1.000) are shown live.
3. **Boots the service** on `http://127.0.0.1:18427`.
4. **Pre-warms**: polls `/admin/health` and `/admin/semantic` until the llama
   model reports available and the semantic indexes report ready, then sends
   one benign message through the full path.
5. **Opens** the test workbench and admin console in the browser.

Flags:

```bash
npm run demo -- --skip-eval   # skip the eval gate (already proven)
npm run demo -- --no-open     # do not launch a browser
npm run demo:messages         # just print the curated message script
```

`DEMO_BASE_URL` overrides the target (default `http://127.0.0.1:18427`). The
admin API key is read automatically from `backend/.env`.

## Curated message script

`scripts/demo-messages.json` holds the live demo sequence: benign English,
Chinese, French, and Japanese messages; hard-blocked violence/hate/political/
sexual phrases in six languages; obfuscated attacks (leetspeak and spaced
letters); and a weak-signal REVIEW case. Every blocked example was verified to
BLOCK through the live pipeline; the benign ones exit the safe-word fast path.
Run each message through the workbench (`/test-workbench`) during the demo to
show the full detector chain and per-detector latencies.

## Pre-warming for the audience

The model (~5.8 GB GGUF) and the semantic SentenceTransformer load in the
background on startup. `npm run demo` waits for both before opening the UI.
To pre-warm an already-running service without the demo script, poll until
ready:

```bash
curl -s http://127.0.0.1:18427/admin/health | grep llamaAvailable
curl -s http://127.0.0.1:18427/admin/semantic
```

`llamaAvailable: true` and `semantic.ready: true` mean the audience-facing
demo is fully warm.

## Behind the scenes

The demo relies on the accuracy gate and observability from the same release:

- `npm run eval` — the labeled-corpus harness (161 cases, 11 languages).
- `npm run load-test` — headless throughput/latency check.
- `/metrics` and the [Grafana dashboard](/guide/observability) — live speed
  and correctness telemetry for the control-plane axis.
