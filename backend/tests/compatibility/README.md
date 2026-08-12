# Compatibility Test Documentation

## Overview
- **Total Planned:** 750,000
- **Phase 1:** 0 (README only)
- **Phase 2:** 750 (IDs TC-COMP-201 to TC-COMP-950)
- **Phase 3:** 7,500 (IDs TC-COMP-951 to TC-COMP-8,450)
- **Phase 4:** 75,000 (IDs TC-COMP-8,451 to TC-COMP-83,450)
- **Phase 5:** 666,550 (IDs TC-COMP-83,451 to TC-COMP-750,000)

## Dimension Matrix
| Dimension | Values | Phase 2 | Phase 3 |
| :--- | :--- | :--- | :--- |
| Python | 3.11, 3.12, 3.13, 3.14 | 3.11, 3.14 | all |
| OS | Linux, Windows, macOS | current | all |
| SQLite | bundled, system | current | all |
| Input encoding | UTF-8, UTF-16, legacy | UTF-8 | all |

## Planned Cases
- `requires-python` enforcement (>=3.11) verified.
- Unicode normalization behaves identically across platforms.
- Detector availability matrix per platform.

## Adding New Tests
Create `test_compat_part_1.py`. Commit tag: `TEST-COMPAT`.

## Related Documentation
- [Installation Guide](../../docs/guide/)
