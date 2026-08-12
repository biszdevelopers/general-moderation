# Fuzzing Test Documentation

## Overview
- **Total Planned:** 1,050,000
- **Phase 1:** 0 (README only; random-input checks inside chaos suites)
- **Phase 2:** 1,000 (IDs TC-FUZ-201 to TC-FUZ-1,200)
- **Phase 3:** 10,000 (IDs TC-FUZ-1,201 to TC-FUZ-11,200)
- **Phase 4:** 100,000 (IDs TC-FUZ-11,201 to TC-FUZ-111,200)
- **Phase 5:** 938,800 (IDs TC-FUZ-111,201 to TC-FUZ-1,050,000)

## Dimension Matrix
| Dimension | Values | Phase 2 | Phase 3 |
| :--- | :--- | :--- | :--- |
| Corpus | unicode, injection, malformed, random | random | all |
| Endpoint | moderate, batch, admin words | moderate | all |
| Mutation | afl-style, python-based | python | afl |
| Runs | 100-100000 | 1000 | 10000 |

## Planned Cases
- Random unicode strings never crash the moderator.
- Fuzzed admin payloads never corrupt storage.
- Long-running fuzz corpus finds no assertion violations.
- Regression corpus replays every previously-crashing input.

## Adding New Tests
Create `test_fuzz_part_1.py` (uses `python-afl` or `hypothesis` fuzzing).
Commit tag: `TEST-FUZZ`.

## Related Documentation
- [API Reference](../../docs/api/)
