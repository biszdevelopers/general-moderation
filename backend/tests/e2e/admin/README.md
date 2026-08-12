# Admin API Test Documentation

## Overview
- **Total Planned:** 1,050,000
- **Phase 1:** 50 (IDs TC-ADM-001 to TC-ADM-050)
- **Phase 2:** 1,000 (IDs TC-ADM-101 to TC-ADM-1,100)
- **Phase 3:** 10,000 (IDs TC-ADM-1,101 to TC-ADM-11,100)
- **Phase 4:** 100,000 (IDs TC-ADM-11,101 to TC-ADM-111,100)
- **Phase 5:** 938,900 (IDs TC-ADM-111,101 to TC-ADM-1,050,000)

## Dimension Matrix
| Dimension | Values | Phase 1 | Phase 2 |
| :--- | :--- | :--- | :--- |
| Endpoint | words, import, export, stats, health, logs, settings, app-config | all | all |
| Auth | valid, missing, wrong | all | all |
| Word payload | valid, empty, long, unicode, injection | all | all |
| App config | or, and, thresholds | all | all |
| Settings | valid, invalid, secret | all | all |

## Phase 1 Case List (50 cases)
| ID | Description | File |
| :--- | :--- | :--- |
| TC-ADM-001..050 | Auth, word CRUD, stats, health, app config, settings, logs, validation | test_admin_part_1.py |

## Adding New Tests
Admin tests use `admin_headers` fixture. New Phase 2 cases (bulk import
edges, settings catalog parity) go in `test_admin_part_2.py`, IDs starting
TC-ADM-101.

## Related Documentation
- [Admin Console](../../docs/guide/)
- [API Reference](../../docs/api/)
