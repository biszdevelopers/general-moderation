# Traditional Chinese

## Coverage

Traditional Chinese is matched by the same packages as Simplified Chinese,
with `glin-profanity`, `profanite`, and `PyProfane` providing the core
dictionaries.

## Normalization

NFKC normalization maps many compatibility characters used in Traditional
Chinese documents to their canonical forms, improving recall against
Simplified-dictionary entries while preserving the original text for
auditing.

## Obfuscation Handling

- Full-width and compatibility characters are folded.
- Whitespace tricks are collapsed.
- Politically sensitive terminology is covered by the dedicated C matcher.

## Example

```bash
curl -X POST http://127.0.0.1:8080/moderate \
    -d '{"text":"這是一則測試訊息"}'
```
