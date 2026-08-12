# Public API Test Documentation

## Overview
- **Total Planned:** 2,100,000
- **Phase 1:** 80 (IDs TC-PUB-001 to TC-PUB-080)
- **Phase 2:** 2,000 (IDs TC-PUB-201 to TC-PUB-2,200)
- **Phase 3:** 20,000 (IDs TC-PUB-2,201 to TC-PUB-22,200)
- **Phase 4:** 200,000 (IDs TC-PUB-22,201 to TC-PUB-222,200)
- **Phase 5:** 1,877,800 (IDs TC-PUB-222,201 to TC-PUB-2,100,000)

## Dimension Matrix
| Dimension | Values | Phase 1 | Phase 2 |
| :--- | :--- | :--- | :--- |
| Endpoint | /moderate, /moderate/batch, /health | all | all |
| Verdict | PASS, BLOCK, REVIEW | all | all |
| Text length | 1-8192 | 1-8192 | all |
| Unicode | ascii, CJK, Arabic, emoji | all | all |
| Batch size | 1-100 | 1-100 | all |
| User/app | 0-10 | 0-3 | all |

## Phase 1 Case List (80 cases)
| ID | Description | File |
| :--- | :--- | :--- |
| TC-PUB-001..040 | Health, moderate, validation, batch, response shape | test_public_api_part_1.py |
| TC-PUB-041..080 | Profiling, unicode, batch edges, caching, content variety | test_public_api_part_2.py |

## Adding New Tests
Follow the archive README step-by-step template. New Phase 2 cases go in
`test_public_api_part_3.py`, IDs starting TC-PUB-201.

## Related Documentation
- [API Reference](../../docs/api/)
