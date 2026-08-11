# Simplified Chinese

## Coverage

Simplified Chinese is handled by the verified packages:

- `glin-profanity` — C matcher with Chinese dictionary.
- `profanite` — Rust matcher with universal coverage.
- `PyProfane` — C matcher with a compact profanity dictionary.

The dedicated `sensitive-word-filter-cn` and `sensitive-word-filter`
packages were removed because they do not exist on PyPI.

## Specifics

Chinese text has no word boundaries, so detection relies on substring DFA
matching over the normalized text rather than tokenization. NFKC
normalization converts full-width characters and traditional-compatible
variants.

## Common Attacks

- Full-width characters (`ｆｕｃｋ`).
- Homophone substitutions (谐音).
- Character insertion between syllables.

These are partially mitigated by the fuzzy BK-tree layer.

## Example

```bash
curl -X POST http://127.0.0.1:18427/moderate \
    -d '{"text":"这是一个测试消息"}'
```
