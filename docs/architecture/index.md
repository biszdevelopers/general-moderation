# Architecture

General Moderation is a high-performance, multi-tenant content moderation
service that pre-filters content before human review. It combines fast-path
rule detection with semantic similarity, user behavior profiling, and an
optional locally hosted LLM.

## Native-Core Design

The service is **maximally optimized by layering Python over compiled
engines**: Python is the surface glue that orchestrates state, policy, and
routing, while every hot path is delegated to C, C++, Rust, or WebAssembly
underneath — exact matching runs in C, fuzzy distance in C, hashing in C,
profanity lists in Rust, sandboxed evaluation in WebAssembly, validation and
serialization in Rust, persistence in C (SQLite), and inference in C++
(llama.cpp). The full inventory of native engines and the per-request
execution path are documented in [Performance
Engineering](/architecture/performance).

```mermaid
flowchart TB
    subgraph Glue["Python glue layer (policy + orchestration)"]
        API["FastAPI · engine · profiler · admin"]
    end
    subgraph Native["Compiled engines (C / C++ / Rust / WASM)"]
        C1["Aho-Corasick (C)"]
        C2["Levenshtein (C)"]
        C3["Bloom · MurmurHash (C)"]
        R1["badwords · stop-words (Rust)"]
        W1["gangajal (WASM)"]
        RS["pydantic-core · orjson · cryptography (Rust)"]
        SQ["SQLite (C)"]
        LLM["llama.cpp (C++)"]
    end
    Glue --> Native
```

## Components

```mermaid
flowchart TD
    Apps[External Applications<br/>unique API key per app] -->|HTTPS + API key| API[FastAPI + Gunicorn<br/>single port 18427]
    API --> SPA[React admin SPA<br/>built frontend/dist]
    API --> PIPE[3-Stage Detection Pipeline]

    subgraph PIPE[3-Stage Pipeline]
        S1[Stage 1: Fast Path<br/>safe word list, C regex]
        S2[Stage 2: Detectors + Semantic + Profiling<br/>suspicion score 0-100]
        S3[Stage 3: LLM Qwen3.5-9B<br/>BLOCK / PASS]
        S1 --> S2 --> S3
    end

    S2 --> DET[Parallel detectors<br/>Aho-Corasick, BK-tree, Metaphone,<br/>5+ multi-language packages]
    S2 --> SEM[Semantic similarity<br/>SentenceTransformer + Faiss per category]
    S2 --> PRO[User profiling<br/>91-day rolling window + summaries]

    API --> ADM[Admin & feedback]
    ADM --> TUNE[Auto weight tuning<br/>daily batch]
    ADM --> EXP[Data export<br/>ZIP archive]
    ADM --> SET[Runtime settings<br/>settings.db]

    PIPE --> DATA[(SQLite layer<br/>users.db, archive.db,<br/>feedback.db, config.db,<br/>settings.db)]
```

## Directory Layout

```
backend/
├── app/
│   ├── ai/            # llama.cpp model, download, prompts
│   ├── detectors/     # rule-based detectors (C/C++/Rust backed)
│   ├── fastpath/      # Stage 1 safe word list + language detection
│   ├── semantic/      # SentenceTransformer + Faiss per category
│   ├── profiling/     # 91-day user stats + cycle summaries
│   ├── scoring/       # suspicion score
│   ├── feedback/      # corrections + auto-tuning
│   ├── export/        # full system ZIP export
│   ├── settings_service.py
│   ├── engine/        # 3-stage pipeline orchestration
│   └── admin/         # admin REST endpoints
frontend/              # React + Ant Design admin console
docs/                  # VitePress documentation
deployment/            # Docker, systemd, nginx, frp
scripts/               # build, deploy, secret generation
```

## Performance Targets

| Target | Value |
| :--- | :--- |
| Content handled without the LLM | 95%+, under 200 ms latency |
| LLM invocation | under 5% of traffic |
| Rule-based checks | sub-millisecond |
| Semantic query | under 50 ms |
