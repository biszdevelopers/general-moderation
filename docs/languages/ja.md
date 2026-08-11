# Japanese

## Coverage

Japanese is covered by the universal packages (`glin-profanity`,
`profanite`, `gangajal`, `PyProfane`) which include Japanese profanity
dictionaries.

## Specifics

Japanese text mixes kanji, hiragana, katakana, and Latin characters with no
spaces. The pipeline relies on:

- The Aho-Corasick automaton for exact phrase matches.
- The BK-tree for edit-distance variants.
- MinHash for near-duplicate short phrases.

## Common Attacks

- Katakana substitution of loanword profanity.
- Repetition characters (ー) inside sensitive words.
- Mixed-script obfuscation.

NFKC normalization folds half-width katakana and full-width Latin forms.

## Example

```bash
curl -X POST http://127.0.0.1:8080/moderate \
    -d '{"text":"こんにちは世界"}'
```
