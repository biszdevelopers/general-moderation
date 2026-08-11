# Turkish

## Coverage

Turkish is covered by `glin-profanity` and `profanite`
Turkish dictionaries.

## Specifics

Turkish agglutination appends many suffixes to a root, and the language
contains the dotless `ı` and dotted `i` which are case-sensitive even in
ASCII. NFKC normalization preserves these distinctions while the BK-tree
layer tolerates small spelling variation.

## Common Attacks

- Dotted/dotless vowel confusion (`i` vs `ı`).
- Suffix variation on profane roots.
- Leetspeak.

## Example

```bash
curl -X POST http://127.0.0.1:8080/moderate \
    -d '{"text":"merhaba dünya"}'
```
