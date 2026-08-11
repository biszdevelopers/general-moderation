# Portuguese

## Coverage

Portuguese is covered by `glin-profanity` and `profanite`
Portuguese dictionaries, including both European and Brazilian variants.

## Specifics

Portuguese uses heavy diacritics (à, ã, ç, ê, ó). NFKC normalization keeps
forms canonical; the BK-tree layer tolerates accent omission and the
Aho-Corasick matcher covers base vocabulary.

## Common Attacks

- Accent stripping.
- Brazilian slang differences.
- Leetspeak and character substitution.

## Example

```bash
curl -X POST http://127.0.0.1:18427/moderate \
    -d '{"text":"olá mundo"}'
```
