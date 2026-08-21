# Model Management

The **Models** page of the admin console turns Stage 3 into a pluggable
layer: choose which LLM provider classifies borderline content, manage
multiple GGUF model versions, monitor provider health, and edit the system
prompt — all without restarting the service.

## Providers

Five providers are supported. The active one is selected by the
`LLM_PROVIDER` runtime setting; a backup can be registered with
`BACKUP_LLM_PROVIDER`.

| Provider | Reaches | Configuration keys |
| :--- | :--- | :--- |
| `local_llama_cpp` | A GGUF model loaded in-process via llama.cpp | `ACTIVE_GGUF_PATH`, `MODEL_*` tuning keys |
| `external_llama_cpp` | Any external `llama-server` (OpenAI-compatible endpoint, native `/health`) | `EXTERNAL_LLAMACPP_BASE_URL`, `EXTERNAL_LLAMACPP_MODEL` |
| `ollama` | An Ollama server (`/api/chat`, `/api/tags`) | `OLLAMA_BASE_URL`, `OLLAMA_MODEL` |
| `openai_compatible` | The OpenAI API or any compatible gateway (vLLM, LM Studio, OpenRouter) | `OPENAI_BASE_URL`, `OPENAI_MODEL`, `OPENAI_API_KEY` |
| `anthropic_compatible` | The Anthropic API or any `/v1/messages`-compatible gateway | `ANTHROPIC_BASE_URL`, `ANTHROPIC_MODEL`, `ANTHROPIC_API_KEY` |

Provider credentials entered through the admin UI are encrypted with AES-GCM
using the service `ENCRYPTION_KEY` before they are written to the settings
database, and are always redacted (`********`) in API responses.

## Switching and Health

Switching is manual: pick a provider (or an active GGUF) on the Models page
and save; the change is audited like every other setting.

- **Graceful drain** — classifications already running finish on the old
  provider; it is unloaded only after its last in-flight request completes.
  New requests immediately use the new provider.
- **Health monitoring** — a background probe runs every
  `MODEL_HEALTH_INTERVAL_SECONDS`. After `MODEL_HEALTH_FAILURE_THRESHOLD`
  consecutive failures the router fails over to the backup provider.
  Recovery does not auto-revert; activate the preferred provider again when
  ready.
- **Total failure** — when no provider is healthy, `LLM_FAILURE_POLICY`
  decides: `rule_based` keeps rule verdicts (ambiguous content becomes
  REVIEW for human moderation), while `block` fails closed.

## GGUF Registry

Multiple GGUF files can coexist under `MODEL_DIR`; one is active at a time.
Three ways to add a version:

1. **Register path** — point at a file already on the server disk.
2. **Upload** — stream a `.gguf` through the browser (large files take a
   while).
3. **Download** — queue a Hugging Face download with repository id and
   filename; mirror fallback applies automatically.

Activating a model updates the `ACTIVE_GGUF_PATH` setting, so the local
provider loads that file at the next lazy load (or immediately after an
idle unload). Removing a registration never deletes the file from disk.

## System Prompt

The classification system prompt is editable and versioned. Saving creates
a new version and activates it immediately across both routed providers;
any older version can be reactivated to roll back. When no custom version
is active, the built-in default prompt is used.

## REST API

```text
GET    /admin/models                      list models + provider health
GET    /admin/models/health               probe active/backup providers
POST   /admin/models/register             {name, path}
POST   /admin/models/download             {name, repo, filename}
POST   /admin/models/upload?name=<name>   multipart .gguf upload
POST   /admin/models/{id}/activate        switch ACTIVE_GGUF_PATH
DELETE /admin/models/{id}                 remove registration only
GET    /admin/prompt                      active template
PUT    /admin/prompt                      {template} — saves new version
GET    /admin/prompt/versions             version history
POST   /admin/prompt/versions/{id}/activate
```
