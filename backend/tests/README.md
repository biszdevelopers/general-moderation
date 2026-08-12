# Test Suite

## Overview

General Moderation ships a **Phase 1 core suite of exactly 1,000 test cases**
and a **Phase 2 suite of exactly 9,000 additional cases** (10,000 total)
covering every critical path of the backend moderation service, plus a fully
documented roadmap to a **planned universe of 25,000,000+ test cases** across
all future phases.

- **Phase 1:** 1,000 cases across 13 module directories.
- **Phase 2 (current):** 9,000 cases across 92 generated files — golden-master
  characterization tests emitted by `tests/tools/phase2_generator.py`, with
  zero overlap against Phase 1 (verified by `phase2_uniqueness_report.md`).
- **Speed:** the suite parallelizes across every available CPU core via
  pytest-xdist (`-n auto`; worker count derived from the machine at runtime).
  The session-scoped `db_template` fixture pre-seeds the SQLite files once per
  worker and copies them into each test's sandbox, so per-test setup is file
  copies instead of schema creation and seeding. No hard-coded worker counts
  or wall-clock figures are baked in.
- **Report target:** `test_reports/index.html` (generated with `pytest-html`).

## Phase 2 Allocation (Implemented)

| Module | Phase 1 | Phase 2 | Total |
| :--- | :--- | :--- | :--- |
| Detectors | 125 | 1,200 | 1,325 |
| Engine | 80 | 700 | 780 |
| Semantic | 80 | 700 | 780 |
| User Profiling | 80 | 700 | 780 |
| Archive | 115 | 950 | 1,065 |
| Auto-Tuning | 60 | 550 | 610 |
| Model/LLM | 60 | 550 | 610 |
| Settings | 60 | 550 | 610 |
| Public API | 80 | 700 | 780 |
| Admin API | 50 | 600 | 650 |
| Export | 70 | 600 | 670 |
| Security | 80 | 700 | 780 |
| Chaos/Resilience | 60 | 500 | 560 |
| **Total** | **1,000** | **9,000** | **10,000** |

## Priority Breakdown

| Priority | Count | Meaning |
| :--- | :--- | :--- |
| P0 (Critical) | 200 | Core API, auth, archive, detectors, security — must never break |
| P1 (High) | 300 | Common user flows, main features |
| P2 (Medium) | 300 | Edge cases, error handling, boundary conditions |
| P3 (Low) | 200 | Performance sanity, resilience, rare conditions |

## Directory Layout

```
tests/
├── conftest.py          # Global fixtures (settings, engine, word bank, client)
├── base_test.py         # BaseTest class with frozen-clock and SQLite helpers
├── README.md            # This file
├── unit/
│   ├── README.md        # All planned unit tests
│   ├── detectors/       # 125 Phase-1 cases (aho, bk-tree, metaphone, multi-lang)
│   ├── engine/          # 80 Phase-1 cases (pipeline, cache, metrics, components)
│   ├── semantic/        # 80 Phase-1 cases (service + SuspicionScorer)
│   └── profiling/       # 80 Phase-1 cases (ratios, cycles, isolation)
├── integration/
│   ├── README.md        # All planned integration tests
│   ├── archive/         # 115 Phase-1 cases (91-day cycles)
│   ├── auto_tuning/     # 60 Phase-1 cases (weights, thresholds, decay)
│   ├── model/           # 60 Phase-1 cases (sanitize, download, retry)
│   └── settings/        # 60 Phase-1 cases (validation, types, read-only)
├── e2e/
│   ├── README.md        # All planned end-to-end tests
│   ├── public/          # 80 Phase-1 cases (moderate, batch, health)
│   └── admin/           # 50 Phase-1 cases (word bank, app config, settings)
├── export/              # 70 Phase-1 cases (archives, redaction, pruning)
├── security/            # 80 Phase-1 cases (headers, CORS, injection, auth)
├── chaos/               # 60 Phase-1 cases (resilience, concurrency, recovery)
├── performance/         # README only (planned universe)
├── data_integrity/      # README only (planned universe)
├── longevity/           # README only (planned universe)
├── upgrade/             # README only (planned universe)
├── compatibility/       # README only (planned universe)
├── property/            # README only (planned universe)
├── mutation/            # README only (planned universe)
├── contract/            # README only (planned universe)
└── fuzzing/             # README only (planned universe)
```

## Phase 1 Allocation

| Module | P0 | P1 | P2 | P3 | Phase-1 Total |
| :--- | :--- | :--- | :--- | :--- | :--- |
| Public API | 20 | 40 | 15 | 5 | 80 |
| Admin API | 20 | 20 | 10 | 0 | 50 |
| Detectors | 30 | 40 | 35 | 20 | 125 |
| Engine | 15 | 35 | 25 | 5 | 80 |
| Archive | 30 | 35 | 30 | 20 | 115 |
| Semantic | 15 | 30 | 25 | 10 | 80 |
| User Profiling | 20 | 25 | 25 | 10 | 80 |
| Auto-Tuning | 10 | 20 | 20 | 10 | 60 |
| Model/LLM | 10 | 20 | 20 | 10 | 60 |
| Security | 10 | 20 | 30 | 20 | 80 |
| Export | 5 | 15 | 35 | 15 | 70 |
| Settings | 5 | 15 | 30 | 10 | 60 |
| Chaos/Resilience | 0 | 15 | 30 | 15 | 60 |
| **Total** | **190** | **330** | **330** | **150** | **1,000** |

## Running the Tests

From the backend directory:

```bash
# All tests (serial)
uv run python -m pytest tests

# All tests (parallel, target < 5 min)
uv run python -m pytest tests -n auto

# Phase 2 tests only
uv run python -m pytest tests -k phase2

# Regenerate the Phase 2 suite + READMEs (only when changing the generator)
uv run python tests/tools/phase2_generator.py
```

# A single module
uv run python -m pytest tests/unit/detectors -v

# A single file
uv run python -m pytest tests/integration/archive/test_archive_part_1.py -v

# Coverage
uv run python -m pytest tests --cov=app --cov-report=html
```

From the repository root:

```bash
npm run test          # all backend tests
npm run test:unit     # unit tests only
npm run test:integration  # integration tests only
npm run test:e2e      # e2e tests only
```

## Test Design

- **Isolation:** every test gets a fresh temporary directory; the suite never
  touches real `data/`, `logs/`, `models/`, or `semantic/` directories.
- **Determinism:** `BaseTest` freezes `datetime.now` so archive cycles and
  auto-tuning batches are reproducible. Advance the clock with
  `self.advance_days(n)` / `self.advance_hours(n)`.
- **Speed:** per-test SQLite files, `:memory:` databases for unit tests,
  mock model packages, and fake `faiss`/`sentence_transformers` modules keep
  the suite fast. Run with `-n auto` for parallel execution.
- **Style:** American English, OOP, full type annotations, 4-space indent,
  `ruff` lint/format, no `any` types without justification.

## Adding New Tests

Each module README contains a step-by-step guide (see `tests/unit/detectors/README.md`
for a worked example). The short version:

1. Pick the target phase and priority (P0-P3).
2. Confirm the dimension combination is not already covered in the matrix.
3. Create `test_<module>_part_<N>.py` (max 100 cases per file).
4. Write the test method; use `BaseTest` helpers and existing fixtures.
5. Update the module README (new row in the phase table + status table).
6. Run: `uv run python -m pytest tests/<module>/ -v`
7. Commit one file per commit: `[TEST-<TYPE>] Add <module> tests part <N>`.

## Commit Tags

`TEST-UNIT`, `TEST-INT`, `TEST-E2E`, `TEST-PERF`, `TEST-SEC`, `TEST-CHAOS`,
`TEST-DATA`, `TEST-LONGEVITY`, `TEST-UPGRADE`, `TEST-COMPAT`, `TEST-PROP`,
`TEST-MUTATION`, `TEST-CONTRACT`, `TEST-FUZZ`, `TEST-DOCS`.

## The 25M Universe

The full planned universe of 25,000,000+ test cases is documented per module:

- **Detectors:** multi-language × length × content-type × obfuscation matrix.
- **Archive:** cycle number × volume × flagged/blocked/reviewed percentages ×
  user count × app count.
- **Semantic:** categories × thresholds × index types × dimensionalities.
- **Auto-tuning:** precision × pass-rate × decay × batch timing.
- **Model:** endpoints × retries × mirror fallbacks × idle behavior.
- **Security:** injection vectors × auth bypasses × header combinations.
- **Export:** database counts × redaction patterns × retention windows.
- **Chaos:** failure injection × concurrency × recovery ordering.
- Plus **performance**, **data integrity**, **longevity**, **upgrade**,
  **compatibility**, **property**, **mutation**, **contract**, and **fuzz**
  suites, each with its own README and dimension matrix.

Each module README lists the planned IDs by phase and explains exactly how to
add the next batch of cases.

## Related Documentation

- [Architecture](../../docs/architecture/)
- [API Reference](../../docs/api/)
- [Configuration](../../docs/guide/configuration.md)
- [Testing Guide](../../docs/guide/testing.md)
