# Hindi

## Coverage

Hindi is covered by `glin-profanity` and `profanite` Hindi dictionaries.

## Specifics

Hindi uses the Devanagari script with vowel signs and conjuncts. NFKC
normalization composes decomposed characters, and the Aho-Corasick matcher
covers base vocabulary.

## Common Attacks

- Roman transliteration (Hinglish) of profanity.
- Diacritic and matra variation.
- Space insertion between syllables.

Romanized forms are partially caught by the phonetic layer.

## Example

```bash
curl -X POST http://127.0.0.1:8080/moderate \
    -d '{"text":"नमस्ते दुनिया"}'
```
