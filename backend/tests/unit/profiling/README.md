# User Profiling Module Test Documentation

## Overview
- **Total Planned:** 1,050,000
- **Phase 1:** 80 (IDs TC-PRF-001 to TC-PRF-080)
- **Phase 2:** 1,200 (IDs TC-PRF-101 to TC-PRF-1,300)
- **Phase 3:** 12,000 (IDs TC-PRF-1,301 to TC-PRF-13,300)
- **Phase 4:** 120,000 (IDs TC-PRF-13,301 to TC-PRF-133,300)
- **Phase 5:** 916,700 (IDs TC-PRF-133,301 to TC-PRF-1,050,000)

## Dimension Matrix
| Dimension | Values | Phase 1 | Phase 2 |
| :--- | :--- | :--- | :--- |
| Window | 7, 30, 91, 365 | 91 (+short) | all |
| Users | 1-100 | 1-25 | all |
| Apps | 1-20 | 1-10 | all |
| Flagged % | 0-100 | matrix | all |
| Cycles | 1-10 | 1-3 | all |
| Day offset | 1-91 | 1-91 | all |

## Phase 1 Case List (80 cases)
| ID | Description | File |
| :--- | :--- | :--- |
| TC-PRF-001..040 | Ratios, daily aggregation, gaps, isolation, archive summaries | test_profiling_part_1.py |
| TC-PRF-041..080 | Cycle boundaries, linked summaries, ratio matrix, windows | test_profiling_part_2.py |

## Adding New Tests
Profiling tests freeze time with `BaseTest.advance_days(n)`. New Phase 2
cases (ratio thresholds, multi-cycle churn) go in `test_profiling_part_3.py`,
IDs starting TC-PRF-101.

## Related Documentation
- [User Profiling](../../docs/architecture/)
- [Archive Strategy](../../docs/architecture/)
