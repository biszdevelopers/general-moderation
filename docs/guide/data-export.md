# Data Export

Administrators can download a single ZIP archive containing every piece of
data produced by the service, for backup, migration, or audit purposes.

## What the Archive Contains

| Entry | Contents |
| :--- | :--- |
| `databases/` | Every SQLite database (`users.db`, `archive.db`, `feedback.db`, `config.db`, `settings.db`, `custom_words.db`, `critical_phrases.db`) |
| `csv/` | A CSV dump of every table in every database |
| `logs/` | `moderation.log` and every rotated backup |
| `config/` | `.env` (secrets redacted) and `.env.example` |
| `config/settings_snapshot.json` | The current runtime settings |
| `semantic/` | The Faiss index files and their source texts |
| `export_metadata.json` | Export timestamp, schema version, detector count, model availability, database sizes, and semantic category sizes |

## Security

- The endpoint requires the `ADMIN_API_KEY`.
- Secret values in `.env` are replaced with `[REDACTED]`.
- The endpoint is rate-limited to one request per ten minutes per client.
- The archive is built in the export directory and removed shortly after the
  response is streamed; stale archives are pruned after
  `EXPORT_RETENTION_DAYS`.

## Using the Admin UI

1. Open the **Export** page in the admin console.
2. Click **Export All Data**.
3. The archive downloads as `general_moderation_export_<timestamp>.zip`.
4. The page shows the timestamp of the last export.

## REST API

```text
GET /admin/export
```

Headers: `X-API-Key: <ADMIN_API_KEY>`

The response is `application/zip` with a
`Content-Disposition: attachment` header.
