# Severe-Content Unit Tests

Phase 1 suite for the severity-aware detection pipeline introduced by the
moderation rework.

## Coverage

| Area | Cases |
| :--- | :--- |
| `CriticalPhraseManager` | add/reload/detect, remove, duplicate rejection |
| Severity hard-block | high-severity blocks, low-severity passes, per-app threshold |
| Severity scoring | suspicion-score floor lifts, ordinary words unaffected |
| False positives | benign everyday text passes (glin resolver fix) |
| Cache invalidation | config changes drop stale cached verdicts |

## Dimension Matrix

- Phrase severity: below / at / above the hard-block threshold.
- Per-app policy overrides: global default vs. app-specific severity threshold.
- Content classes: benign sentences, high-severity phrases, severity-1 custom words.

## Running

```bash
cd backend && uv run python -m pytest tests/unit/severe -v
```

New cases follow the `BaseTest` pattern from `tests/base_test.py` and use the
shared fixtures from `tests/conftest.py`.
