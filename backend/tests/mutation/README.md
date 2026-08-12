# Mutation Test Documentation

## Overview
- **Total Planned:** 600,000
- **Phase 1:** 0 (README only)
- **Phase 2:** 600 (IDs TC-MUT-201 to TC-MUT-800)
- **Phase 3:** 6,000 (IDs TC-MUT-801 to TC-MUT-6,800)
- **Phase 4:** 60,000 (IDs TC-MUT-6,801 to TC-MUT-66,800)
- **Phase 5:** 533,200 (IDs TC-MUT-66,801 to TC-MUT-600,000)

## Dimension Matrix
| Dimension | Values | Phase 2 | Phase 3 |
| :--- | :--- | :--- | :--- |
| Mutation type | statement, boundary, constant | constant | all |
| Operator | swap, negate, delete | negate | all |
| Coverage target | detectors, scorer, profiler | scorer | all |
| Killing ratio | 0-100% | >80% | >90% |

## Planned Baseline
- Mutate the suspicion scorer boundary conditions and verify the test suite
  catches the change (mutation killed).
- Track a mutation score baseline and prevent regressions.

## Adding New Tests
Create `test_mutation_part_1.py` (uses `mutmut` or manual mutations). Commit
tag: `TEST-MUTATION`.

## Related Documentation
- [Algorithm Formulations](../../docs/algorithms/)
