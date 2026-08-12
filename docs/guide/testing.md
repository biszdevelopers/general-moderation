# Testing Pipeline

General Moderation ships a **10,000-test suite** — 1,000 Phase 1 core cases
and 9,000 Phase 2 golden-master cases — that is designed to run as fast as a
modern JS test runner such as Vitest. This page documents the exact pipeline:
how tests are discovered, how the machine's full core count is used, how
fixtures are shared and isolated, and how the Phase 2 suite is generated and
verified.

## Suite Shape

| Property | Value |
| :--- | :--- |
| Total tests | 10,000 |
| Phase 1 | 1,000 hand-written core cases |
| Phase 2 | 9,000 generated golden-master cases |
| Test files | 92 Phase 2 files + 24 Phase 1 files |
| Per-file cap | 100 test cases |
| Runner | pytest + pytest-xdist |
| Isolation | per-test sandbox directory |

```mermaid
flowchart LR
    subgraph Source["Test Sources"]
        A["Phase 1<br/>1,000 hand-written cases"]
        B["Phase 2<br/>9,000 generated cases"]
    end
    A --> C["pytest collection<br/>tests/"]
    B --> C
    C --> D["pytest-xdist<br/>-n auto"]
    D --> E["Worker 1"]
    D --> F["Worker 2"]
    D --> G["Worker N"]
    E --> H["conftest fixtures<br/>db_template + engine + client"]
    F --> H
    G --> H
    H --> I["PASS / FAIL summary"]
```

## Execution Model: Every Core, No Hard-Coded Worker Count

The suite is invoked with `-n auto`, which asks pytest-xdist to pick the
worker count from the machine's logical CPU count at runtime. There is no
hard-coded `-n 8` or `-n 16` anywhere: on a 4-core laptop it uses 4 workers,
on a 128-core server it uses 128. `test:serial` exists for deterministic
CI debugging but is not the default.

```mermaid
flowchart TD
    R["npm run test<br/>(pytest tests -n auto)"] --> A{"os.cpu_count()"}
    A --> W1["Worker process 1"]
    A --> W2["Worker process 2"]
    A --> W3["Worker process ..."]
    A --> W4["Worker process N"]
    W1 --> C["Each worker owns a slice of test files"]
    W2 --> C
    W3 --> C
    W4 --> C
    C --> D["Shared session fixtures built once per worker"]
    D --> E["Per-test sandbox copies"]
    E --> F["100% green or red verdict"]
```

Each worker is a full Python process with its own interpreter, so the
C/C++/Rust detector packages and SQLite engines run truly in parallel across
all cores. Test files are distributed, never duplicated, so there is no
re-execution between workers.

## Fixture Lifecycle: One Seed, Many Sandboxes

The single most expensive operation used to be fixture construction: every
test created and seeded five SQLite databases (settings, app-config, profiler
live, profiler archive, feedback) plus the custom-words store — roughly
100+ ms of schema creation and seeding per test, serialized across the suite.

The `conftest.py` `db_template` fixture fixes this. It is **session-scoped**
per worker: it builds and seeds every database exactly once, then each test's
`settings` fixture **copies** the files into that test's sandbox. Opening an
existing, schema-complete SQLite file costs a fraction of a millisecond versus
creating and seeding it from scratch.

```mermaid
sequenceDiagram
    autonumber
    participant W as Worker process
    participant T as db_template (session)
    participant S as settings (per test)
    participant E as engine / client
    participant DB as SQLite sandbox

    W->>T: build once: create + seed settings.db, config.db,<br/>users.db, archive.db, feedback.db, custom_words.db
    T-->>W: template data/ directory
    Note over W: for every test
    W->>S: copy template data/* -> tmp_path/data (file copies)
    S-->>E: settings point at sandbox paths
    E->>DB: open existing schema-complete files
    E-->>W: engine / TestClient ready
    W->>E: run test body
    W-->>S: teardown (sandbox discarded)
```

Isolation is unchanged: every test still gets its own physical database
copies, so no test can observe another test's writes. The optimization only
moves schema creation and seeding out of the per-test critical path.

## Per-Test Path

```mermaid
flowchart LR
    subgraph Setup["Per-test setup (fast)"]
        C["copy DB template files"]
        S["build Settings object"]
        L["open JSONL logger"]
        WB["open custom-words store"]
        E["build ModerationEngine<br/>(detectors, profiler, scorer)"]
    end
    subgraph Body["Test body"]
        M["run the real code paths"]
        A["assert golden / property outcome"]
    end
    subgraph Teardown["Teardown"]
        T["close engine + logger"]
        D["discard sandbox"]
    end
    C --> S --> L --> WB --> E --> M --> A --> T --> D
```

## Phase 2: Golden-Master Generation

The 9,000 Phase 2 cases are emitted by `backend/tests/tools/phase2_generator.py`.
It runs the **real application** at generation time to capture expected values
(a golden master), then writes parametrized pytest files plus every module
README and a uniqueness report. Because generation and execution share the
same locked environment, the emitted assertions reproduce observed behavior
exactly and lock it in as regression coverage.

```mermaid
flowchart LR
    subgraph Gen["phase2_generator.py (one-time)"]
        M["dimension matrices<br/>(26 languages, lengths, volumes, faults)"]
        M --> R["invoke real app"]
        R --> G["golden expected values"]
        G --> F["emit 92 test files (<=100 cases each)"]
        G --> D["emit module README tables"]
        G --> U["emit uniqueness report"]
    end
    F --> PT["pytest runs the emitted cases"]
    PT --> V["10,000 cases collected"]
    U --> V
```

The uniqueness report (`backend/tests/tools/phase2_uniqueness_report.md`)
proves zero overlap: Phase 2 IDs start after each module's Phase 1 ceiling,
and no dimension combination from Phase 1 is reused.

## Module Allocation

| Module | Phase 1 | Phase 2 | Phase 2 files |
| :--- | :--- | :--- | :--- |
| Detectors | 125 | 1,200 | 12 |
| Engine | 80 | 700 | 7 |
| Semantic | 80 | 700 | 7 |
| User Profiling | 80 | 700 | 7 |
| Archive | 115 | 950 | 10 |
| Auto-Tuning | 60 | 550 | 6 |
| Model/LLM | 60 | 550 | 6 |
| Settings | 60 | 550 | 6 |
| Public API | 80 | 700 | 7 |
| Admin API | 50 | 600 | 6 |
| Export | 70 | 600 | 6 |
| Security | 80 | 700 | 7 |
| Chaos/Resilience | 60 | 500 | 5 |
| **Total** | **1,000** | **9,000** | **92** |

```mermaid
pie showData title Phase 2 allocation by module
    "Detectors" : 1200
    "Engine" : 700
    "Semantic" : 700
    "Profiling" : 700
    "Archive" : 950
    "Auto-Tuning" : 550
    "Model/LLM" : 550
    "Settings" : 550
    "Public API" : 700
    "Admin API" : 600
    "Export" : 600
    "Security" : 700
    "Chaos" : 500
```

## The 25M Universe

The per-module READMEs document the full planned universe of 25,000,000+
cases. Each phase extends the dimension matrices; the tooling and fixture
design above are built so later phases only add rows to the generator or the
matrices, never new infrastructure.

```mermaid
flowchart LR
    P1["Phase 1<br/>1,000 cases"] --> P2["Phase 2<br/>9,000 cases"]
    P2 --> P3["Phase 3<br/>100,000 cases"]
    P3 --> P4["Phase 4<br/>1,000,000 cases"]
    P4 --> P5["Phase 5<br/>23,890,000 cases"]
    P5 --> U["25,000,000+ universe"]
```

## Running the Pipeline

```bash
# Everything, using all available cores (worker count = logical CPU count)
npm run test

# Scoped runs (all also use -n auto)
npm run test:unit          # tests/unit
npm run test:integration   # tests/integration
npm run test:e2e           # tests/e2e
npm run test:phase2        # all *_phase2_* files

# Deterministic serial run (CI debugging)
npm run test:serial

# Regenerate the Phase 2 suite, READMEs, and uniqueness report
cd backend && uv run python tests/tools/phase2_generator.py

# Lint and format the suite
cd backend && uv run python -m ruff check tests
cd backend && uv run python -m ruff format --check tests
```

## Adding New Tests

1. Read the module README under `backend/tests/` for the dimension matrix and
   the phase it belongs to.
2. For Phase 2+: add rows to `backend/tests/tools/phase2_generator.py` and
   regenerate (the generator emits files, READMEs, and the uniqueness report).
3. For hand-written cases: follow the Phase 1 pattern (`BaseTest`, frozen
   clock, `conftest` fixtures) and add the case to a file with at most 100
   cases.
4. Update the relevant READMEs.
5. Commit one file per commit with `[TEST-<TYPE>]` tags.

## Related Documentation

- The in-repo test suite docs live under `backend/tests/README.md` and each
  module's `backend/tests/*/README.md`.
- [Architecture Overview](../architecture/)
- [Contributing](../contributing)
