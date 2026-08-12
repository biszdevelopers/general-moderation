# Export Module Test Documentation

## Overview
- **Total Planned:** 1,500,000
- **Phase 1:** 70 (IDs TC-EXP-001 to TC-EXP-070)
- **Phase 2:** 1,500 (IDs TC-EXP-101 to TC-EXP-1,600)
- **Phase 3:** 15,000 (IDs TC-EXP-1,601 to TC-EXP-16,600)
- **Phase 4:** 150,000 (IDs TC-EXP-16,601 to TC-EXP-166,600)
- **Phase 5:** 1,333,400 (IDs TC-EXP-166,601 to TC-EXP-1,500,000)

## Dimension Matrix
| Dimension | Values | Phase 1 | Phase 2 |
| :--- | :--- | :--- | :--- |
| Database count | 0-5 | 1-3 | all |
| Table count | 1-10 | 1-4 | all |
| Secret suffix | _KEY, _SECRET, PASSWORD, TOKEN | all | all |
| Retention days | 1-365 | 1-90 | all |
| Semantic files | present, missing | all | all |
| Log rotation | 0-10 backups | 0-2 | all |

## Phase 1 Case List (70 cases)
| ID | Description | File |
| :--- | :--- | :--- |
| TC-EXP-001..070 | Archive construction, redaction, manifest, pruning, multi-DB, CSV, locking | test_export_part_1.py |

## Adding New Tests
Export tests chdir into a sandbox root; use the `_Chdir` helper. New Phase 2
cases (many-database archives, rotated-log matrices) go in
`test_export_part_2.py`, IDs starting TC-EXP-101.

## Related Documentation
- [Data Export](../../docs/guide/)
