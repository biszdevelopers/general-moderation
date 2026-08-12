# Security Module Test Documentation

## Overview
- **Total Planned:** 2,000,000
- **Phase 1:** 80 (IDs TC-SEC-001 to TC-SEC-080)
- **Phase 2:** 2,000 (IDs TC-SEC-201 to TC-SEC-2,200)
- **Phase 3:** 20,000 (IDs TC-SEC-2,201 to TC-SEC-22,200)
- **Phase 4:** 200,000 (IDs TC-SEC-22,201 to TC-SEC-222,200)
- **Phase 5:** 1,777,800 (IDs TC-SEC-222,201 to TC-SEC-2,000,000)

## Dimension Matrix
| Dimension | Values | Phase 1 | Phase 2 |
| :--- | :--- | :--- | :--- |
| Header | 6 security headers | all | all |
| CORS origin | allowed, disallowed, none | all | all |
| Auth key | valid, missing, wrong, empty | all | all |
| Injection | SQL, XSS, template, unicode | all | all |
| Traversal | ../, %2e%2e, absolute | all | all |
| Method | GET, POST, PUT, DELETE | all | all |

## Phase 1 Case List (80 cases)
| ID | Description | File |
| :--- | :--- | :--- |
| TC-SEC-001..080 | Headers, CORS, auth bypass, injection, traversal, rate limit, API keys | test_security_part_1.py |

## Adding New Tests
New Phase 2 cases (rate-limit thresholds, brute-force key sweeps, header
parity across all endpoints) go in `test_security_part_2.py`, IDs starting
TC-SEC-201.

## Related Documentation
- [Security Model](../../docs/architecture/)
- [API Reference](../../docs/api/)
