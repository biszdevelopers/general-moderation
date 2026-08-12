# Contract Test Documentation

## Overview
- **Total Planned:** 600,000
- **Phase 1:** 0 (README only; response-shape checks inside e2e suites)
- **Phase 2:** 600 (IDs TC-CTR-201 to TC-CTR-800)
- **Phase 3:** 6,000 (IDs TC-CTR-801 to TC-CTR-6,800)
- **Phase 4:** 60,000 (IDs TC-CTR-6,801 to TC-CTR-66,800)
- **Phase 5:** 533,200 (IDs TC-CTR-66,801 to TC-CTR-600,000)

## Dimension Matrix
| Dimension | Values | Phase 2 | Phase 3 |
| :--- | :--- | :--- | :--- |
| Contract | OpenAPI schema | current | all |
| Field naming | camelCase responses, snake_case requests | all | all |
| Response model | moderate, batch, admin, health | all | all |
| Versioning | v1 | v1 | all |

## Planned Cases
- Every response field matches the declared Pydantic schema.
- OpenAPI schema is generated without errors and is self-consistent.
- Admin models serialize with camelCase aliases.
- Request models accept snake_case field names.

## Adding New Tests
Create `test_contract_part_1.py`. Commit tag: `TEST-CONTRACT`.

## Related Documentation
- [API Reference](../../docs/api/)
