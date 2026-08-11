# Spanish

## Coverage

Spanish is covered by `glin-profanity`, `profanite`, and `PyProfane`
Spanish dictionaries, spanning Latin American and peninsular
variants.

## Specifics

Spanish text uses accents and an inverted punctuation set; NFKC
normalization keeps accented forms canonical while the matcher tolerates
accent omission through the BK-tree layer.

## Common Attacks

- Accent stripping (`cabrón` → `cabron`).
- Regional slang differences.
- Leetspeak and character substitution.

## Example

```bash
curl -X POST http://127.0.0.1:8080/moderate \
    -d '{"text":"hola mundo"}'
```
