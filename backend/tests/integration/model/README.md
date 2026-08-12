# Model/LLM Module Test Documentation

## Overview
- **Total Planned:** 900,000
- **Phase 1:** 60 (IDs TC-MODEL-001 to TC-MODEL-060)
- **Phase 2:** 1,000 (IDs TC-MODEL-101 to TC-MODEL-1,100)
- **Phase 3:** 10,000 (IDs TC-MODEL-1,101 to TC-MODEL-11,100)
- **Phase 4:** 100,000 (IDs TC-MODEL-11,101 to TC-MODEL-111,100)
- **Phase 5:** 788,900 (IDs TC-MODEL-111,101 to TC-MODEL-900,000)

## Dimension Matrix
| Dimension | Values | Phase 1 | Phase 2 |
| :--- | :--- | :--- | :--- |
| Model state | missing, local, downloading | missing | all |
| Endpoint | primary, mirror, modelscope, none | all | all |
| Retry count | 0-3 | 1-3 | all |
| Prompt injection | control tokens, XML, prefixes | all | all |
| Cache type | q8_0, f16, unknown | q8_0, f16 | all |
| Threads | auto, numeric | auto, numeric | all |

## Phase 1 Case List (60 cases)
| ID | Description | File |
| :--- | :--- | :--- |
| TC-MODEL-001..060 | Sanitize matrix, threads, KV cache, download retry/fallback, prompt building, detect replies | test_model_part_1.py |

## Adding New Tests
Model tests mock `hf_hub_download`, `requests`, and the inference model. New
Phase 2 cases (idle unload, warm-up, resume) go in `test_model_part_2.py`,
IDs starting TC-MODEL-101.

## Related Documentation
- [Model Auto-Download](../../docs/guide/)
- [LLM Integration](../../docs/architecture/)
