# Longevity Test Documentation

## Overview
- **Total Planned:** 900,000
- **Phase 1:** 0 (README only; 1-year simulation planned)
- **Phase 2:** 900 (IDs TC-LONG-201 to TC-LONG-1,100)
- **Phase 3:** 9,000 (IDs TC-LONG-1,101 to TC-LONG-10,100)
- **Phase 4:** 90,000 (IDs TC-LONG-10,101 to TC-LONG-100,100)
- **Phase 5:** 799,900 (IDs TC-LONG-100,101 to TC-LONG-900,000)

## Dimension Matrix
| Dimension | Values | Phase 2 | Phase 3 |
| :--- | :--- | :--- | :--- |
| Years simulated | 1, 2, 5, 10 | 1 | 5 |
| Cycles | 4-40 per year | 4 | 20 |
| Users | 1-1000 | 10 | 100 |
| Daily volume | 1-1000 | 10 | 100 |

## Planned Cases
- 1-year simulation: ~365 daily records, 4 archived cycles per user.
- Longevity 5-year: linked chain of 20 summaries.
- Storage stays bounded: live table ≤ window, summaries grow linearly.
- Ratio accuracy preserved across all archived years.

## Adding New Tests
Create `test_longevity_part_1.py` using `BaseTest.advance_days` to fast-forward
without wall-clock waits. Commit tag: `TEST-LONGEVITY`.

## Related Documentation
- [Archive Strategy](../../docs/architecture/)
