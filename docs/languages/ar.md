# Arabic

## Coverage

Arabic is covered by `glin-profanity` and `profanite` Arabic
dictionaries.

## Specifics

Arabic is written right-to-left with contextual letter forms and short vowel
marks (harakat) that are usually omitted. NFKC normalization unifies
different encoding forms of the same letter, and the matchers tolerate the
absence of diacritics.

## Common Attacks

- Diacritic removal or addition.
- Letter substitution (e.g. `ا`, `أ`, `إ`, `آ` variants).
- Latin transliteration (Arabizi) of profanity.

## Example

```bash
curl -X POST http://127.0.0.1:8080/moderate \
    -d '{"text":"مرحبا بالعالم"}'
```
