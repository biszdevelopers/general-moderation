# Unit Test Documentation

## Overview
- **Total Planned:** 4,350,000
- **Phase 1:** 365 (IDs TC-UNIT-001 to TC-UNIT-365)
- **Phase 2:** 5,000 (IDs TC-UNIT-366 to TC-UNIT-5,365)
- **Phase 3:** 50,000 (IDs TC-UNIT-5,366 to TC-UNIT-55,365)
- **Phase 4:** 500,000 (IDs TC-UNIT-55,366 to TC-UNIT-555,365)
- **Phase 5:** 3,794,635 (IDs TC-UNIT-555,366 to TC-UNIT-4,350,000)

## Phase 1 Coverage
| Submodule | Cases | Files |
| :--- | :--- | :--- |
| Detectors | 125 | test_aho_corasick_part_1, test_bk_tree_part_1, test_metaphone_part_1, test_multi_language_part_1, test_multi_language_part_2 |
| Engine | 80 | test_engine_part_1, test_engine_part_2 |
| Semantic | 80 | test_semantic_part_1, test_semantic_part_2 |
| Profiling | 80 | test_profiling_part_1, test_profiling_part_2 |

## Dimension Matrix (Detectors)
| Dimension | Values | Phase 1 | Phase 2 |
| :--- | :--- | :--- | :--- |
| Language | en, zh, ru, ar, ja, ko, multi, any | en, multi | +zh, ru, ar |
| Length | 1, 10, 100, 1000, 8192 | 1-100 | 1-8192 |
| Content type | profanity, violence, hate, sexual, pii, ads, clean | profanity, clean | all |
| Obfuscation | none, leet, fullwidth, phonetic | none, phonetic | all |

## Adding New Tests
Follow `tests/unit/detectors/README.md` step-by-step guide. Use the
`BaseTest` frozen clock for time-sensitive logic and the engine/word bank
fixtures from `conftest.py`.

## Related Documentation
- [Architecture](../../docs/architecture/)
- [Algorithms](../../docs/algorithms/)
