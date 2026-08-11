# Simplified Chinese

## Coverage

Simplified Chinese is handled by the dedicated packages:

- `sensitive-word-filter-cn` — C DFA matcher for vulgar content.
- `sensitive-word-filter` — C matcher for politically sensitive content.
- `glin-profanity`, `safetext` — additional vulgar coverage.

## Specifics

Chinese text has no word boundaries, so detection relies on substring DFA
matching over the normalized text rather than tokenization. NFKC
normalization converts full-width characters and traditional-compatible
variants.

## Common Attacks

- Full-width characters (`ｆｕｃｋ`).
- Homophone substitutions (谐音).
- Character insertion between syllables.

These are partially mitigated by the fuzzy BK-tree and MinHash layers.

## Example

```bash
curl -X POST http://127.0.0.1:8080/moderate \
    -d '{"text":"这是一个测试消息"}'
```
