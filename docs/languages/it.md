# Italian

## Coverage

Italian is covered by `glin-profanity`, `profanite`, and `PyProfane`
Italian dictionaries.

## Specifics

Italian profanity is highly inflected (verbs, plurals, gender agreement).
The BK-tree fuzzy matcher tolerates small spelling variations, and the
Aho-Corasick automaton covers the base vocabulary.

## Common Attacks

- Accent and apostrophe substitution (`e` → `è`, dropped apostrophes).
- Dialectal variants of common insults.
- Leetspeak.

## Example

```bash
curl -X POST http://127.0.0.1:8080/moderate \
    -d '{"text":"ciao mondo"}'
```
