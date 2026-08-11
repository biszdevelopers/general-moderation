# Admin Settings

Every runtime parameter of the service can be viewed and edited from the
**Settings** page of the admin console. Changes are persisted to
`settings.db` and applied immediately — no `.env` edit or service restart is
required. The `.env` file remains the fallback used to seed values on first
run.

## How It Works

The backend reads every editable value through the `SettingsService`, which
caches the database contents with a short TTL. Saving a value validates it
first (type and range checks), then persists it and refreshes the cache so
the next request sees the new value.

## Editable Groups

| Group | Example settings |
| :--- | :--- |
| Model | `MODEL_CONTEXT_SIZE`, `MODEL_THREADS`, `MODEL_BATCH_SIZE`, `MODEL_MAX_TOKENS`, `MODEL_CACHE_TYPE_K`, `MODEL_CACHE_TYPE_V`, `MODEL_FLASH_ATTN`, `MODEL_MLOCK`, `MODEL_IDLE_TIMEOUT_SECONDS` |
| Stage 1 Fast Path | `SAFE_WORD_ENABLED`, `SAFE_WORD_LIST_PATH` |
| Detectors | All `ENABLE_*` toggles for the multi-language packages |
| Detector Weights | `WEIGHT_DETECTOR_*` values (5–50) |
| Semantic Similarity | `SEMANTIC_ENABLED`, `SEMANTIC_MODEL`, `SEMANTIC_SIMILARITY_THRESHOLD`, `SEMANTIC_FORCE_LLM_THRESHOLD`, `SEMANTIC_TOP_K` |
| Semantic Weights | `WEIGHT_SEMANTIC_*` values (5–50) |
| User Profiling | `USER_PROFILING_ENABLED`, `USER_RATIO_THRESHOLD`, `USER_SCORE_MODIFIER`, `USER_WINDOW_DAYS` |
| Suspicion Scoring | `WEIGHT_USER`, `SCORE_WEIGHTS_CACHE_TTL_SECONDS` |
| LLM | `AI_TARGET_PERCENTAGE`, `FORCE_LLM_ON_SEMANTIC_HIGH`, `FORCE_LLM_ON_USER_RATIO_HIGH`, `LLM_RESPONSE_TIMEOUT_SECONDS` |
| Feedback & Auto-Tuning | `AUTO_TUNING_ENABLED`, `WEIGHT_DECAY_HALF_LIFE_DAYS`, `AUTO_TUNING_BATCH_HOUR` |
| Performance | `CACHE_MAX_SIZE`, `CACHE_TTL_SECONDS`, `DETECTOR_THREAD_POOL_SIZE`, `REQUEST_TIMEOUT_SECONDS`, `MAX_BATCH_SIZE` |
| Security | `RATE_LIMIT_REQUESTS`, `RATE_LIMIT_PERIOD`, `ALLOWED_ORIGINS` |
| Logging | `LOG_LEVEL`, `LOG_MAX_BYTES`, `LOG_BACKUP_COUNT`, `LOG_RETENTION_DAYS` |
| Export | `EXPORT_RETENTION_DAYS` |

## Read-Only Settings

The following require a restart and cannot be changed at runtime:

- `APP_PORT`
- `WORKERS`
- `MODEL_PATH`
- `FEEDBACK_DB_PATH`
- `EXPORT_TEMP_DIR`
- Every `*_KEY` and `*_SECRET` value

## Validation Rules

- Boolean settings are rendered as switches.
- Integer settings are rendered as number inputs with documented ranges
  (for example, detector weights are clamped to 5–50).
- Fractional settings such as `SEMANTIC_SIMILARITY_THRESHOLD` accept values
  in the 0–1 range.
- Invalid values are rejected with an HTTP 400 and the save is aborted.

## REST API

```text
GET  /admin/settings
POST /admin/settings
```

`POST` accepts a JSON body:

```json
{
    "settings": {
        "MODEL_CONTEXT_SIZE": 16384,
        "CACHE_MAX_SIZE": 600
    }
}
```

The response lists the keys that were updated.
