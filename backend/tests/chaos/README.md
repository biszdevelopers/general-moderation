# Chaos/Resilience Module Test Documentation

## Overview
- **Total Planned:** 1,200,000
- **Phase 1:** 60 (IDs TC-CHAOS-001 to TC-CHAOS-060)
- **Phase 2:** 1,200 (IDs TC-CHAOS-101 to TC-CHAOS-1,300)
- **Phase 3:** 12,000 (IDs TC-CHAOS-1,301 to TC-CHAOS-13,300)
- **Phase 4:** 120,000 (IDs TC-CHAOS-13,301 to TC-CHAOS-133,300)
- **Phase 5:** 1,066,700 (IDs TC-CHAOS-133,301 to TC-CHAOS-1,200,000)

## Dimension Matrix
| Dimension | Values | Phase 1 | Phase 2 |
| :--- | :--- | :--- | :--- |
| Fault | import fail, DB corrupt, callable crash | all | all |
| Load | burst, interleaved apps | all | all |
| Recovery | clear cache, reload, shutdown | all | all |
| Length | 0-8192 | 0-8192 | all |
| Concurrency | sequential burst | 10-100 | all |

## Phase 1 Case List (60 cases)
| ID | Description | File |
| :--- | :--- | :--- |
| TC-CHAOS-001..060 | Degraded detectors, malformed DBs, package failures, bursts, recovery, schemas | test_chaos_part_1.py |

## Adding New Tests
New Phase 2 cases (fault injection with monkeypatch, crash recovery ordering,
disk-full simulation) go in `test_chaos_part_2.py`, IDs starting TC-CHAOS-101.

## Related Documentation
- [Deployment Guide](../../docs/guide/)
- [Operations](../../docs/guide/)
