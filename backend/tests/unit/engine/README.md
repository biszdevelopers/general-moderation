# Engine Module Test Documentation

## Overview
- **Total Planned:** 1,050,000
- **Phase 1:** 80 (IDs TC-ENG-001 to TC-ENG-080)
- **Phase 2:** 1,000 (IDs TC-ENG-101 to TC-ENG-1,100)
- **Phase 3:** 10,000 (IDs TC-ENG-1,101 to TC-ENG-11,100)
- **Phase 4:** 100,000 (IDs TC-ENG-11,101 to TC-ENG-111,100)
- **Phase 5:** 938,900 (IDs TC-ENG-111,101 to TC-ENG-1,050,000)

## Dimension Matrix
| Dimension | Values | Phase 1 | Phase 2 |
| :--- | :--- | :--- | :--- |
| Stage | 1 (fast path), 2 (detectors), 3 (LLM) | all | all |
| Verdict | PASS, BLOCK, REVIEW | all | all |
| Cache state | cold, hit, expired, full | hit, cold | all |
| App policy | or, and, per-app | or | +and, per-app |
| User ratio | 0.0, 0.3, 0.5, 1.0 | 0.0, 0.3 | all |
| Batch size | 1, 5, 100 | 1-10 | all |

## Phase 1 Case List (80 cases)
| ID | Description | File |
| :--- | :--- | :--- |
| TC-ENG-001..050 | Fast path, stage-2 verdicts, stage-3 triggers, cache, metrics, batch, refresh | test_engine_part_1.py |
| TC-ENG-051..080 | SafeWordFilter, RollingHash, SuspicionScorer components | test_engine_part_2.py |

## Adding New Tests
Follow `tests/unit/detectors/README.md` steps. New engine cases (stage-3
LLM triggers, cache TTL boundaries, app-policy matrices) go in
`test_engine_part_3.py` and later, IDs starting at TC-ENG-101.

## Related Documentation
- [Three-Stage Pipeline](../../docs/architecture/)
- [Suspicion Scoring](../../docs/algorithms/)
