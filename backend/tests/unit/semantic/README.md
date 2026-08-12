# Semantic Module Test Documentation

## Overview
- **Total Planned:** 1,200,000
- **Phase 1:** 80 (IDs TC-SEM-001 to TC-SEM-080)
- **Phase 2:** 1,500 (IDs TC-SEM-101 to TC-SEM-1,600)
- **Phase 3:** 15,000 (IDs TC-SEM-1,601 to TC-SEM-16,600)
- **Phase 4:** 150,000 (IDs TC-SEM-16,601 to TC-SEM-166,600)
- **Phase 5:** 1,033,400 (IDs TC-SEM-166,601 to TC-SEM-1,200,000)

## Dimension Matrix
| Dimension | Values | Phase 1 | Phase 2 |
| :--- | :--- | :--- | :--- |
| Category | political, violence, sexual, hate, pii, ads, other | all | all |
| Threshold | 0.1-1.0 step 0.05 | 0.85, 0.90 | all |
| Index type | FlatIP, FlatL2, IVF | FlatIP | +FlatL2 |
| Dimensionality | 384, 768, 1024 | 384 | +768 |
| Availability | installed, missing | both | installed |
| Top-k | 1-100 | 5 | all |

## Phase 1 Case List (80 cases)
| ID | Description | File |
| :--- | :--- | :--- |
| TC-SEM-001..040 | Unavailable path, category metadata, SuspicionScorer weights | test_semantic_part_1.py |
| TC-SEM-041..080 | Fake-module available path: query, add, delete, persist | test_semantic_part_2.py |

## Adding New Tests
Semantic cases use the `fake_semantic_modules` fixture from `conftest.py`
when exercising the available path. New Phase 2 cases (threshold sweeps,
index-type parity) go in `test_semantic_part_3.py`, IDs starting TC-SEM-101.

## Related Documentation
- [Semantic Similarity](../../docs/algorithms/)
- [Configuration](../../docs/guide/configuration.md)
