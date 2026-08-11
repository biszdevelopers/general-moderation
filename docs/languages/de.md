# German

## Coverage

German is covered by `glin-profanity`, `profanite`, and `PyProfane` German
dictionaries.

## Specifics

German compounds long words by concatenation, which can hide a profane root
inside a longer compound. The Aho-Corasick automaton is a substring matcher,
so profane roots embedded in compounds are still found in a single pass.

## Common Attacks

- Umlaut substitution (`ä` → `ae`, `ß` → `ss`).
- Compound word obfuscation.
- Leetspeak.

## Example

```bash
curl -X POST http://127.0.0.1:8080/moderate \
    -d '{"text":"Hallo Welt"}'
```
