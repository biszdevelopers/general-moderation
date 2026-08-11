# Moderation API

Public endpoints for moderating single messages and batches.

## Moderate a Single Message

`POST /moderate`

### Request

```json
{
    "id": "msg-123",
    "user_id": "user-456",
    "text": "your message here"
}
```

| Field | Type | Required | Description |
| :--- | :--- | :--- | :--- |
| `id` | string | no | Caller identifier, echoed back. |
| `user_id` | string | no | Author identifier, used for auditing. |
| `text` | string | yes | Message body, 1-8192 characters. |

### Response 200

```json
{
    "id": "msg-123",
    "verdict": "BLOCK",
    "level_used": 1,
    "reasons": ["Exact sensitive word matched in Aho-Corasick automaton"],
    "matched_words": ["badword"],
    "matched_language": "en",
    "confidence_score": 1.0,
    "latency_ms": 0.42,
    "detector_chain": ["bloom_filter", "rolling_hash", "aho_corasick"]
}
```

### Response 429

Rate limit exceeded.

## Moderate a Batch

`POST /moderate/batch`

### Request

```json
{
    "items": [
        { "id": "a", "user_id": "u1", "text": "message one" },
        { "id": "b", "user_id": "u2", "text": "message two" }
    ]
}
```

| Field | Type | Required | Description |
| :--- | :--- | :--- | :--- |
| `items` | array | yes | 1-100 messages. |

### Response 200

```json
{
    "results": [
        {
            "id": "a",
            "verdict": "PASS",
            "level_used": 1,
            "reasons": [],
            "matched_words": [],
            "matched_language": null,
            "confidence_score": null,
            "latency_ms": 0.31,
            "detector_chain": ["bloom_filter", "rolling_hash"]
        }
    ],
    "total_latency_ms": 0.64
}
```

Results are returned in request order.

## Verdict Semantics

| Verdict | Meaning |
| :--- | :--- |
| `PASS` | No sensitive content detected. |
| `BLOCK` | Decisive exact match (Level 1) or model confirmation (Level 2). |
| `REVIEW` | Probabilistic or fuzzy hit pending human review. |

`REVIEW` becomes `BLOCK` when the llama.cpp model is available and classifies
the text as sensitive; otherwise the verdict stays `REVIEW`.
