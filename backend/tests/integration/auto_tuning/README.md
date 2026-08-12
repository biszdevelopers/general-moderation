# Auto-Tuning Module Test Documentation

## Overview
- **Total Planned:** 1,050,000
- **Phase 1:** 60 (IDs TC-TUNE-001 to TC-TUNE-060)
- **Phase 2:** 1,000 (IDs TC-TUNE-101 to TC-TUNE-1,100)
- **Phase 3:** 10,000 (IDs TC-TUNE-1,101 to TC-TUNE-11,100)
- **Phase 4:** 100,000 (IDs TC-TUNE-11,101 to TC-TUNE-111,100)
- **Phase 5:** 938,900 (IDs TC-TUNE-111,101 to TC-TUNE-1,050,000)

## Dimension Matrix
| Dimension | Values | Phase 1 | Phase 2 |
| :--- | :--- | :--- | :--- |
| Precision | 0.0-1.0 | 0.3-1.0 | all |
| Feedback rows | 0-1000 | 0-500 | all |
| LLM pass rate | 0.0-1.0 | matrix | all |
| Half-life days | 1-365 | 30 | all |
| Batch timing | first, repeat | first | all |

## Phase 1 Case List (60 cases)
| ID | Description | File |
| :--- | :--- | :--- |
| TC-TUNE-001..060 | Feedback storage, precision deltas, threshold tuning, decay, reports, edge cases | test_auto_tuning_part_1.py |

## Adding New Tests
Auto-tuning uses the frozen clock via `BaseTest.advance_days`. New Phase 2
cases (half-life sweeps, repeated-batch convergence) go in
`test_auto_tuning_part_2.py`, IDs starting TC-TUNE-101.

## Related Documentation
- [Active Learning](../../docs/architecture/)
- [Algorithm Formulations](../../docs/algorithms/)
