# Word Banks

The service combines three word sources:

- **Base dictionaries** pulled from the C/C++/Rust pip packages at runtime
  (~13,835 words, cached per process).
- **Custom words** stored in SQLite (C implementation) or a JSON document
  written atomically.
- **Chinese sensitive-word lists** from the `backend/data/` subrepos, matched
  by the dedicated top-priority sensitive-stop-words detector (see
  [Configuration](/guide/configuration) and [Credits](/guide/credits)).

## How Words Are Combined

At startup and on every reload, the `WordBankManager`:

1. Collects base words from the installed pip packages via `WordListLoader`.
2. Loads every custom word from storage.
3. Compiles the union into an Aho-Corasick automaton and seeds a Bloom filter.
4. Swaps the new immutable snapshot into place with a single reference
   assignment — no locks, no partial states.

The fuzzy layers (BK-tree, Double Metaphone, Bloom) operate **only** on
administrator-curated custom words. Base words are covered exactly by the
Aho-Corasick automaton (with an ASCII word-boundary guard) and the
multi-language packages; matching them fuzzily would flag nearly every token.
The Chinese subrepos are matched by the separate sensitive-stop-words detector,
so they never pollute the custom-word fuzzy index.

## Custom Words

Custom words carry four fields:

| Field | Description |
| :--- | :--- |
| `word` | The term, NFKC-normalized and lowercased. |
| `language` | ISO 639-1 code, or `any`. |
| `category` | `profanity`, `violence`, `political`, `hate_speech`, `sexual`, `other`. |
| `severity` | Integer from 0 to 10. |

## Managing Words

The REST API is documented in [Admin API](/api/admin). Quick examples:

```bash
# Add a word
curl -X POST http://127.0.0.1:18427/admin/wordbank/words \
    -H "X-API-Key: $KEY" -H "Content-Type: application/json" \
    -d '{"word":"badword","language":"en","category":"profanity","severity":5}'

# List words
curl http://127.0.0.1:18427/admin/wordbank/words -H "X-API-Key: $KEY"

# Bulk import
curl -X POST http://127.0.0.1:18427/admin/wordbank/import \
    -H "X-API-Key: $KEY" -H "Content-Type: application/json" \
    -d '{"items":[{"word":"w1","language":"de"},{"word":"w2","language":"fr"}]}'
```

## Hot Reload

After editing the word bank, reload the compiled structures atomically:

```bash
curl -X POST http://127.0.0.1:18427/admin/reload -H "X-API-Key: $KEY"
```

New detectors read the current snapshot on every request, so the swap is
instantly visible to concurrent traffic.

## Storage Backends

### SQLite (default)

```bash
CUSTOM_WORDS_STORAGE=sqlite
CUSTOM_WORDS_PATH=./data/custom_words.db
```

Uses the C sqlite3 module with parameterized queries and WAL journaling.

### JSON

```bash
CUSTOM_WORDS_STORAGE=json
CUSTOM_WORDS_PATH=./data/custom_words.json
```

A single JSON document serialized with Rust `orjson` and written atomically
via `atomicwrites`.

## Unicode Handling

Every word and every incoming message passes through NFKC normalization and
whitespace collapsing before matching. This defeats full-width characters,
ligatures, and Unicode obfuscation.

## Statistics

`GET /admin/wordbank/stats` returns total, custom, and base word counts plus
the number of distinct languages and categories.

## Severity and Category on Custom Words

A custom word's `severity` (0–10) and `category` ride along on a match and
feed Stage 2: the strongest matched severity promotes the suspicion score via
the severity floor, and a phrase or word at or above
`SEVERITY_HARD_BLOCK_THRESHOLD` (default 5) hard-blocks. See [Suspicion
Score](/algorithms/suspicion-score) for how severity is consumed.
