# Admin Settings

Every runtime parameter of the service can be viewed and edited from the
**Settings** page of the admin console. Changes are persisted to
`settings.db` and applied immediately — no `.env` edit or service restart is
required. The `.env` file remains the fallback used to seed values on first
run.

## How It Works

The backend reads every editable value through the `SettingsService`, which
caches the database contents with a short TTL. Saving a value validates it
first (type, range, and choice checks), then persists it, records an audit
row, and refreshes the cache so the next request sees the new value. Each
setting also carries UI metadata: category, minimum/maximum bounds, allowed
choices, a restart-required flag, and a secret flag.

## Editable Groups

Settings are grouped server-side; the console renders one collapsible
section per category.

| Group | Example settings |
| :--- | :--- |
| Models & Providers | `LLM_PROVIDER`, `BACKUP_LLM_PROVIDER`, `LLM_FAILURE_POLICY`, `OLLAMA_*`, `OPENAI_*`, `ANTHROPIC_*`, `EXTERNAL_LLAMACPP_*`, `MODEL_HEALTH_*` |
| Model | `MODEL_CONTEXT_SIZE`, `MODEL_THREADS`, `MODEL_BATCH_SIZE`, `MODEL_MAX_TOKENS`, `MODEL_CACHE_TYPE_K`, `MODEL_CACHE_TYPE_V`, `MODEL_FLASH_ATTN`, `MODEL_MLOCK`, `MODEL_IDLE_TIMEOUT_SECONDS`, `ACTIVE_GGUF_PATH` |
| Stage 1 Fast Path | `SAFE_WORD_ENABLED`, `SAFE_WORD_LIST_PATH` |
| Detectors | All `ENABLE_*` toggles for the multi-language packages, `ENABLE_PHRASE_DETECTOR`, and the per-detector `ENABLE_DETECTOR_*` toggles |
| Sensitive Stop Words | `ENABLE_SENSITIVE_STOP_WORDS`, the per-category `ENABLE_SENSITIVE_STOP_WORDS_POLITICAL/PORN/GUN/AD/URL` toggles, and the `SENSITIVE_STOP_WORDS_DIR`, `SENSITIVE_WORD_DATA_DICT`, `SENSITIVE_LEXICON_DIR`, `SENSITIVE_DICT_PATH` paths |
| Detector Weights | `WEIGHT_DETECTOR_*` values (5–50) |
| Semantic Similarity | `SEMANTIC_ENABLED`, `SEMANTIC_MODEL`, `SEMANTIC_SIMILARITY_THRESHOLD`, `SEMANTIC_FORCE_LLM_THRESHOLD`, `SEMANTIC_TOP_K` |
| Semantic Weights | `WEIGHT_SEMANTIC_*` values (5–50) |
| User Profiling | `USER_PROFILING_ENABLED`, `USER_RATIO_THRESHOLD`, `USER_SCORE_MODIFIER`, `USER_WINDOW_DAYS` |
| Suspicion Scoring | `WEIGHT_USER`, `SCORE_WEIGHTS_CACHE_TTL_SECONDS` |
| Severity & Review | `SEVERITY_HARD_BLOCK_THRESHOLD`, `REVIEW_ESCALATION_THRESHOLD`, `ML_REVIEW_MODE` |
| LLM | `AI_TARGET_PERCENTAGE`, `FORCE_LLM_ON_SEMANTIC_HIGH`, `FORCE_LLM_ON_USER_RATIO_HIGH`, `LLM_RESPONSE_TIMEOUT_SECONDS`, `CALIBRATION_*` |
| Feedback & Auto-Tuning | `AUTO_TUNING_ENABLED`, `WEIGHT_DECAY_HALF_LIFE_DAYS`, `AUTO_TUNING_BATCH_HOUR` |
| Performance | `CACHE_MAX_SIZE`, `CACHE_TTL_SECONDS`, `DETECTOR_THREAD_POOL_SIZE`, `REQUEST_TIMEOUT_SECONDS`, `MAX_BATCH_SIZE` |
| Security | `RATE_LIMIT_REQUESTS`, `RATE_LIMIT_PERIOD`, `ALLOWED_ORIGINS` |
| Logging | `LOG_LEVEL`, `LOG_MAX_BYTES`, `LOG_BACKUP_COUNT`, `LOG_RETENTION_DAYS` |
| Export | `EXPORT_RETENTION_DAYS` |

## Read-Only Settings

The following require a restart and cannot be changed at runtime. The UI
renders them locked with a "requires service restart" tooltip:

- `APP_HOST`, `APP_PORT`, `WORKERS`
- `FRONTEND_DIST_PATH`, `LOG_FILE_PATH`
- `MODEL_DIR`, `HF_ENDPOINT`, `HF_MIRROR`, `MODELSCOPE_ENDPOINT`
- `REDIS_URI`, `MODEL_PATH`, `FEEDBACK_DB_PATH`, `EXPORT_TEMP_DIR`
- `ADMIN_API_KEY`, `WEBUI_API_KEY`, `SECRET_KEY`, `ENCRYPTION_KEY`

Provider API keys (`OPENAI_API_KEY`, `ANTHROPIC_API_KEY`) are the only
secret-suffixed values that stay editable at runtime; they are encrypted at
rest and redacted in every read path.

## Change History

Every update — manual or preset-driven — is recorded in a `config_audit`
table with the old value, new value, actor, and source. The **History**
button on the Settings page opens this trail; secret keys are redacted to
`********`. Changes that affect provider selection additionally rebuild the
model router immediately (see [Model Management](/guide/model-management)).

## Presets

Presets apply several settings in one validated, audited batch. Three are
seeded on first run:

- **High Accuracy** — more traffic reaches the LLM, thresholds favor recall.
- **Low Cost** — rule-based verdicts only; aggressive caching.
- **Strict** — aggressive blocking with fail-closed model failures.

Administrators can create custom presets from the REST API; payloads are
validated with the same rules as manual edits before anything persists.

## Validation Rules

- Boolean settings are rendered as switches.
- Integer settings are rendered as number inputs with documented ranges
  (for example, detector weights are clamped to 5–50).
- Fractional settings such as `SEMANTIC_SIMILARITY_THRESHOLD` accept values
  in the 0–1 range.
- Choice settings (`LLM_PROVIDER`, `BACKUP_LLM_PROVIDER`,
  `LLM_FAILURE_POLICY`) render as dropdowns and reject unknown values.
- Invalid values are rejected with an HTTP 400 and the save is aborted.

## REST API

```text
GET    /admin/settings                     full catalog with metadata
POST   /admin/settings                     validated batch update (audited)
GET    /admin/settings/history?key=&limit= audit trail, secrets redacted
GET    /admin/presets                      list presets
POST   /admin/presets                      create a preset
POST   /admin/presets/{name}/apply         apply a preset as one batch
DELETE /admin/presets/{name}               remove a preset
```

`POST /admin/settings` accepts a JSON body:

```json
{
    "settings": {
        "MODEL_CONTEXT_SIZE": 16384,
        "CACHE_MAX_SIZE": 600,
        "LLM_PROVIDER": "ollama"
    }
}
```

The response lists the keys that were updated.
