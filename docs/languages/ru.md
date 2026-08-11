# Russian

## Coverage

Russian is covered by `glin-profanity`, `profanite`, and `PyProfane`,
all of which ship Russian profanity dictionaries.

## Specifics

Russian is highly inflected, so exact dictionary matching misses many word
forms. The BK-tree layer (edit distance 2) helps recover morphological
variants and near-duplicates.

## Common Attacks

- Mat (мат) vocabulary with suffix variation.
- Transliteration into Latin script (obscene terms written phonetically).
- Character substitution (`@`, `*`, digits).

Transliterated forms are partially caught by the phonetic (Double Metaphone)
layer.

## Example

```bash
curl -X POST http://127.0.0.1:8080/moderate \
    -d '{"text":"привет мир"}'
```
