# French

## Coverage

French is covered by `badwords-py`, `glin-profanity`, `profanite`, and
`safetext` French dictionaries.

## Specifics

French elision and apostrophes (`l'`, `d'`, `qu'`) split words in ways that
can defeat token-based matchers. The Aho-Corasick automaton operates over
the full normalized text and therefore still finds elided profane roots.

## Common Attacks

- Apostrophe and accent substitution.
- Elided-word splitting.
- Verlan (reversed-syllable slang).

## Example

```bash
curl -X POST http://127.0.0.1:8080/moderate \
    -d '{"text":"bonjour le monde"}'
```
