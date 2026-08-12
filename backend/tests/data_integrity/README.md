# Data Integrity Test Documentation

## Overview
- **Total Planned:** 1,200,000
- **Phase 1:** 0 (README only)
- **Phase 2:** 1,200 (IDs TC-DATA-201 to TC-DATA-1,400)
- **Phase 3:** 12,000 (IDs TC-DATA-1,401 to TC-DATA-13,400)
- **Phase 4:** 120,000 (IDs TC-DATA-13,401 to TC-DATA-133,400)
- **Phase 5:** 1,066,600 (IDs TC-DATA-133,401 to TC-DATA-1,200,000)

## Dimension Matrix
| Dimension | Values | Phase 2 | Phase 3 |
| :--- | :--- | :--- | :--- |
| Integrity check | WAL, foreign keys, unique, counts | WAL, counts | all |
| Crash point | during record, archive, export | archive | all |
| Recovery | reopen, vacuum | reopen | all |
| Schema version | 1-10 | 1 | all |

## Planned Cases
- WAL journal mode active on every database.
- Unique constraints enforce no duplicate daily rows.
- Archive totals equal recorded message counts after crash simulation.
- Atomic export never leaves a partial ZIP.

## Adding New Tests
Create `test_integrity_part_1.py`. Commit tag: `TEST-DATA`.

## Related Documentation
- [Archive Strategy](../../docs/architecture/)
