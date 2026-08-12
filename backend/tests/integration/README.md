# Integration Test Documentation

## Overview
- **Total Planned:** 5,550,000
- **Phase 1:** 295 (IDs TC-INT-001 to TC-INT-295)
- **Phase 2:** 5,000 (IDs TC-INT-301 to TC-INT-5,300)
- **Phase 3:** 50,000 (IDs TC-INT-5,301 to TC-INT-55,300)
- **Phase 4:** 500,000 (IDs TC-INT-55,301 to TC-INT-555,300)
- **Phase 5:** 4,994,700 (IDs TC-INT-555,301 to TC-INT-5,550,000)

## Phase 1 Coverage
| Submodule | Cases | Files |
| :--- | :--- | :--- |
| Archive | 115 | test_archive_part_1, test_archive_part_2 |
| Auto-Tuning | 60 | test_auto_tuning_part_1 |
| Model/LLM | 60 | test_model_part_1 |
| Settings | 60 | test_settings_part_1 |

## Adding New Tests
Integration tests combine multiple services (engine + profiler + feedback +
settings). Use the `engine` fixture and `BaseTest` frozen clock. Follow the
per-module README step-by-step guides.

## Related Documentation
- [Architecture](../../docs/architecture/)
- [Configuration](../../docs/guide/configuration.md)
