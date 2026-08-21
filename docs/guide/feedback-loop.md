# Feedback Loop

The service closes the loop between production decisions and accuracy: live
verdicts (with a severity signal) are recorded, administrators can correct
them, the daily auto-tuning batch adjusts weights and thresholds using those
corrections, and a bootstrap tool turns real audit decisions into labeled
eval-corpus cases.

## Live decision capture

Every moderation decision is appended to the `decisions` table in
`feedback.db` (gated by `AUTO_TUNING_ENABLED`). Each row stores the verdict,
whether the LLM participated, and the **severity** of the strongest match
(0-10) — the severity signal the auto-tuning batch now uses.

## Administrator corrections

Operators record corrections through `POST /admin/feedback`:

```json
{
    "requestId": "msg-1234",
    "verdict": "PASS",
    "isCorrect": false,
    "actualAction": "BLOCK",
    "severity": 7
}
```

The `severity` field is optional (0-10) and feeds the severity-weighted
precision computation in the tuning batch.

## Auto-tuning with the severity signal

`FeedbackService.run_batch()` (daily at `AUTO_TUNING_BATCH_HOUR`, or on demand
via `POST /admin/tune`) computes two precision figures:

- `precision` — plain correct/total over the 24-hour feedback window.
- `severity_precision` — the same correctness weighed by `1 + severity`, so a
  missed high-severity case pulls a detector weight down harder than a missed
  low-severity one.

The weights move toward high-precision values using the **severity-weighted**
signal; the suspicion threshold is tuned from the LLM pass rate toward
`AI_TARGET_PERCENTAGE`. The tuning report includes both precision values.

## Bootstrap eval cases from production

`npm run bootstrap:eval` reads the JSONL audit log, deduplicates decisions by
text hash, and writes a labeled eval-corpus file to
`backend/eval/generated/live_corpus.json`.

```bash
npm run bootstrap:eval                        # default log + output paths
cd backend && uv run python -m tools.bootstrap_eval \
    --log ./logs/moderation.log --limit 500 --min-severity 5
```

Privacy is preserved by construction: the audit log stores only a 50-character
preview plus a SHA-256 hash, so the generated cases inherit that redaction —
the full message text never reaches the corpus. Cases that matched a word or
crossed the severity floor are flagged `redact: true` so operators review them
before committing to `backend/eval/`.

The generated file is gitignored (`backend/eval/generated/`); treat it as a
review-and-copy source for growing the committed corpus in `backend/eval/`.
