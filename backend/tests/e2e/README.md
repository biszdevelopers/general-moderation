# End-to-End Test Documentation

## Overview
- **Total Planned:** 3,150,000
- **Phase 1:** 130 (IDs TC-E2E-001 to TC-E2E-130)
- **Phase 2:** 3,000 (IDs TC-E2E-201 to TC-E2E-3,200)
- **Phase 3:** 30,000 (IDs TC-E2E-3,201 to TC-E2E-33,200)
- **Phase 4:** 300,000 (IDs TC-E2E-33,201 to TC-E2E-333,200)
- **Phase 5:** 2,816,800 (IDs TC-E2E-333,201 to TC-E2E-3,150,000)

## Phase 1 Coverage
| Submodule | Cases | Files |
| :--- | :--- | :--- |
| Public API | 80 | test_public_api_part_1, test_public_api_part_2 |
| Admin API | 50 | test_admin_part_1 |

## Adding New Tests
E2E tests use the `client` fixture (a wired FastAPI `TestClient`). Public
requests use snake_case field names (`user_id`, `app_name`). New Phase 2
cases (multi-app scenarios, SPA fallback) go in `test_public_api_part_3.py`
and `test_admin_part_2.py`.

## Related Documentation
- [API Reference](../../docs/api/)
- [Architecture](../../docs/architecture/)
