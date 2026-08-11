# Data Flow

## Request Flow

```mermaid
sequenceDiagram
    participant Client
    participant API as FastAPI
    participant S1 as Stage 1
    participant S2 as Stage 2
    participant S3 as Stage 3
    participant DB

    Client->>API: POST /moderate (text, user_id, app_name)
    API->>S1: Check safe word list
    alt All tokens safe
        S1-->>API: PASS (score 0, ai_triggered false)
    else Not safe
        API->>S2: Run detectors + semantic + user profile
        S2->>DB: Read 91-day window + cycle summaries
        DB-->>S2: user ratio
        S2->>S2: Compute suspicion score
        alt Trigger policy fires
            API->>S3: Run LLM (BLOCK/PASS)
            S3-->>API: final verdict
        else Score below threshold
            API-->>API: PASS without LLM
        end
    end
    API->>DB: Record daily user stats (archive on day 91)
    API->>DB: Record decision (auto-tuning)
    API-->>Client: { allowed, verdict, suspicionScore, aiTriggered }
```

## Export Flow

```mermaid
sequenceDiagram
    participant Admin
    participant UI
    participant API
    participant EXP as ExportService
    participant DB
    participant FS

    Admin->>UI: Click "Export All Data"
    UI->>API: GET /admin/export
    API->>EXP: Build archive
    EXP->>DB: Copy SQLite databases
    EXP->>DB: Dump tables to CSV
    EXP->>FS: Copy log files
    EXP->>FS: Copy redacted .env and settings snapshot
    EXP->>FS: Copy semantic indexes
    EXP->>EXP: Write export_metadata.json and zip
    EXP-->>API: ZIP stream
    API-->>UI: application/zip download
```

## Feedback Flow

```mermaid
sequenceDiagram
    participant Admin
    participant API
    participant FB as FeedbackService
    participant Tune as Auto-Tuning

    Admin->>API: POST /admin/feedback (correction)
    API->>FB: Store feedback row
    Note over FB: daily batch at AUTO_TUNING_BATCH_HOUR
    FB->>Tune: Aggregate last 24h precision
    Tune->>Tune: Adjust weights (5-50), decay with half-life
    Tune->>Tune: Re-tune threshold toward AI_TARGET_PERCENTAGE
    Tune-->>FB: tuning report
```
