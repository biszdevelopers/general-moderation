# Korean

## Coverage

Korean is covered by the universal packages with Korean dictionaries
(`glin-profanity`, `profanite`, `gangajal`, `PyProfane`).

## Specifics

Korean text is written with Hangul syllables composed of jamo. NFKC
normalization is particularly important here because it composes jamo
sequences and folds half-width Hangul into full-width forms, unifying
equivalent spellings.

## Common Attacks

- Hangul jamo decomposition (ㅋㅋㅋ split forms).
- Space insertion inside words.
- Leetspeak substitutions.

The BK-tree and metaphone layers complement the exact matchers for these.

## Example

```bash
curl -X POST http://127.0.0.1:8080/moderate \
    -d '{"text":"안녕하세요 세계"}'
```
