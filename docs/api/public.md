# Public Moderation API

The public API moderates single messages and batches. Responses use camelCase
aliases.

## Moderate a Message

`POST /moderate`

```json
{
    "text": "string",
    "user_id": "string",
    "app_name": "string",
    "id": "string"
}
```

`app_name` is optional and defaults to `"default"`; it isolates user
profiling per application.

### Response

```json
{
    "id": null,
    "verdict": "PASS",
    "allowed": true,
    "levelUsed": 1,
    "aiTriggered": false,
    "suspicionScore": 0.0,
    "reasons": [],
    "reason": null,
    "matchedWords": [],
    "matchedWord": null,
    "matchedLanguage": null,
    "confidenceScore": null,
    "latencyMs": 12.4,
    "detectorChain": ["rolling_hash", "bk_tree", "double_metaphone", "multi_language"]
}
```

| Field | Type | Description |
| :--- | :--- | :--- |
| `verdict` | `PASS` \| `BLOCK` \| `REVIEW` | the final decision |
| `allowed` | boolean | whether the message may be published |
| `levelUsed` | integer | detection level that decided (1 or 2) |
| `aiTriggered` | boolean | whether the LLM was invoked |
| `suspicionScore` | number | the 0-100 suspicion score |
| `reason` | string \| null | the primary reason |
| `matchedWord` | string \| null | the primary matched word |
| `matchedLanguage` | string \| null | ISO code of the detected language |
| `confidenceScore` | number \| null | overall confidence |

## Moderate a Batch

`POST /moderate/batch`

```json
{
    "items": [
        { "text": "clean message", "user_id": "u1" },
        { "text": "another message", "user_id": "u2" }
    ]
}
```

Returns `{"results": [...], "totalLatencyMs": 42.1}`.

## Error Responses

| Status | Meaning |
| :--- | :--- |
| 400 | Invalid request body |
| 429 | Rate limit exceeded |
| 500 | Internal error |
