# Property Test Documentation

## Overview
- **Total Planned:** 900,000
- **Phase 1:** 0 (README only; small property checks inside module suites)
- **Phase 2:** 900 (IDs TC-PROP-201 to TC-PROP-1,100)
- **Phase 3:** 9,000 (IDs TC-PROP-1,101 to TC-PROP-10,100)
- **Phase 4:** 90,000 (IDs TC-PROP-10,101 to TC-PROP-100,100)
- **Phase 5:** 799,900 (IDs TC-PROP-100,101 to TC-PROP-900,000)

## Dimension Matrix
| Dimension | Values | Phase 2 | Phase 3 |
| :--- | :--- | :--- | :--- |
| Generator | hypothesis strategies | standard | custom |
| Invariant | score in 0-100, verdict valid | all | all |
| Input space | unicode, lengths, unicode | unicode | all |
| Runs per case | 1-1000 | 100 | 1000 |

## Planned Invariants
- `0 <= suspicion_score <= 100` for any input.
- Verdict is always one of PASS/BLOCK/REVIEW.
- `allowed == (verdict != BLOCK)`.
- Ratio is always in `[0.0, 1.0]`.
- Archive totals equal the sum of live+archived rows.

## Adding New Tests
Use `hypothesis` (`@given`) in `test_property_part_1.py`. Commit tag:
`TEST-PROP`.

## Related Documentation
- [Suspicion Scoring](../../docs/algorithms/)
