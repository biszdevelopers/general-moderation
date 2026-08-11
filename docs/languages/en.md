# English

## Coverage

English profanity, hate speech, and abuse are covered by the verified
packages (`badwords`, `profanite`, `glin-profanity`, `gangajal`, `PyProfane`)
plus the C-backed Aho-Corasick exact matcher.

## Detection Layers

- **Aho-Corasick (C)**: exact matches, decisive BLOCK.
- **BK-tree (C)**: edit distance 2 catches typos and leetspeak (`@sshole`,
  `fck`).
- **Double Metaphone**: phonetically equivalent obfuscations (`phuq` → `fuck`).
- **MinHash**: paraphrased near-duplicates of known phrases.
- **Rolling hash**: repeated messages are caught from the spam cache.

## Obfuscation Handling

- NFKC normalization folds full-width and compatibility characters.
- Whitespace collapsing defeats spacing tricks.
- Casing is neutralized before all matching.

## Example

```bash
curl -X POST http://127.0.0.1:8080/moderate \
    -d '{"text":"you are a phuq1ng idiot"}'
```

The BK-tree and metaphone layers typically flag this for review.
