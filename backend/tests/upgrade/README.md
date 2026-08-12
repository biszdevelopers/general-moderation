# Upgrade/Migration Test Documentation

## Overview
- **Total Planned:** 600,000
- **Phase 1:** 0 (README only)
- **Phase 2:** 600 (IDs TC-UPG-201 to TC-UPG-800)
- **Phase 3:** 6,000 (IDs TC-UPG-801 to TC-UPG-6,800)
- **Phase 4:** 60,000 (IDs TC-UPG-6,801 to TC-UPG-66,800)
- **Phase 5:** 533,200 (IDs TC-UPG-66,801 to TC-UPG-600,000)

## Dimension Matrix
| Dimension | Values | Phase 2 | Phase 3 |
| :--- | :--- | :--- | :--- |
| Schema version | v0 -> v1 | v0 -> v1 | all |
| Data present | empty, small, large | small | all |
| Migration | create, add column, index | create | all |
| Downgrade | forward only | forward | both |

## Planned Cases
- Reopening existing databases keeps data intact.
- New tables are created idempotently on every service start.
- Old archive rows survive a schema migration.
- Fresh databases initialize without migration errors.

## Adding New Tests
Create `test_upgrade_part_1.py`. Commit tag: `TEST-UPGRADE`.

## Related Documentation
- [Configuration](../../docs/guide/configuration.md)
