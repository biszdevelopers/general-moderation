# Settings Module Test Documentation

## Overview
- **Total Planned:** 900,000
- **Phase 1:** 60 (IDs TC-SET-001 to TC-SET-0060) :white_check_mark: Implemented
- **Phase 2:** 550 (IDs TC-SET-0061 to TC-SET-0610) :white_check_mark: Implemented
- **Phase 3:** 10,000 (IDs TC-SET-0611 to TC-SET-10610) :hourglass: Planned
- **Phase 4:** 100,000 (IDs TC-SET-10611 to TC-SET-110610) :hourglass: Planned
- **Phase 5:** 789,390 (IDs TC-SET-110611 to TC-SET-900000) :hourglass: Planned

## Dimension Matrix
| Dimension | Values (Phase 2) |
| :--- | :--- |
| Field count | 60+ settings |
| Type | boolean, integer, float, string, list |
| Range bounds | min, max, out-of-range |
| Read-only keys | _KEY, _SECRET, fixed |
| Update batch | single, multi, mixed |

## Test Case List

### Phase 1 - 60 cases
- 60 cases (validation, types, read-only).

### Phase 2 (Current) - 550 cases
| ID | Priority | Description | Dimensions | Expected Outcome | File |
| :--- | :--- | :--- | :--- | :--- | :--- |
| TC-SET-5563 | P1 | Describe field key for ADMIN_API_KEY | key=ADMIN_API_KEY,field=key | present | test_settings_phase2_part_1.py |
| TC-SET-5564 | P1 | Describe field value for ADMIN_API_KEY | key=ADMIN_API_KEY,field=value | present | test_settings_phase2_part_1.py |
| TC-SET-5565 | P1 | Describe field type for ADMIN_API_KEY | key=ADMIN_API_KEY,field=type | present | test_settings_phase2_part_1.py |
| TC-SET-5566 | P1 | Describe field editable for ADMIN_API_KEY | key=ADMIN_API_KEY,field=editable | present | test_settings_phase2_part_1.py |
| TC-SET-5567 | P1 | Describe field key for AI_TARGET_PERCENTAGE | key=AI_TARGET_PERCENTAGE,field=key | present | test_settings_phase2_part_1.py |
| TC-SET-5568 | P1 | Describe field value for AI_TARGET_PERCENTAGE | key=AI_TARGET_PERCENTAGE,field=value | present | test_settings_phase2_part_1.py |
| TC-SET-5569 | P1 | Describe field type for AI_TARGET_PERCENTAGE | key=AI_TARGET_PERCENTAGE,field=type | present | test_settings_phase2_part_1.py |
| TC-SET-5570 | P1 | Describe field editable for AI_TARGET_PERCENTAGE | key=AI_TARGET_PERCENTAGE,field=editable | present | test_settings_phase2_part_1.py |
| TC-SET-5571 | P1 | Describe field key for ALLOWED_ORIGINS | key=ALLOWED_ORIGINS,field=key | present | test_settings_phase2_part_1.py |
| TC-SET-5572 | P1 | Describe field value for ALLOWED_ORIGINS | key=ALLOWED_ORIGINS,field=value | present | test_settings_phase2_part_1.py |
| TC-SET-5573 | P1 | Describe field type for ALLOWED_ORIGINS | key=ALLOWED_ORIGINS,field=type | present | test_settings_phase2_part_1.py |
| TC-SET-5574 | P1 | Describe field editable for ALLOWED_ORIGINS | key=ALLOWED_ORIGINS,field=editable | present | test_settings_phase2_part_1.py |
| TC-SET-5575 | P1 | Describe field key for APP_CONFIG_DB_PATH | key=APP_CONFIG_DB_PATH,field=key | present | test_settings_phase2_part_1.py |
| TC-SET-5576 | P1 | Describe field value for APP_CONFIG_DB_PATH | key=APP_CONFIG_DB_PATH,field=value | present | test_settings_phase2_part_1.py |
| TC-SET-5577 | P1 | Describe field type for APP_CONFIG_DB_PATH | key=APP_CONFIG_DB_PATH,field=type | present | test_settings_phase2_part_1.py |
| TC-SET-5578 | P1 | Describe field editable for APP_CONFIG_DB_PATH | key=APP_CONFIG_DB_PATH,field=editable | present | test_settings_phase2_part_1.py |
| TC-SET-5579 | P1 | Describe field key for APP_HOST | key=APP_HOST,field=key | present | test_settings_phase2_part_1.py |
| TC-SET-5580 | P1 | Describe field value for APP_HOST | key=APP_HOST,field=value | present | test_settings_phase2_part_1.py |
| TC-SET-5581 | P1 | Describe field type for APP_HOST | key=APP_HOST,field=type | present | test_settings_phase2_part_1.py |
| TC-SET-5582 | P1 | Describe field editable for APP_HOST | key=APP_HOST,field=editable | present | test_settings_phase2_part_1.py |
| TC-SET-5583 | P1 | Describe field key for APP_PORT | key=APP_PORT,field=key | present | test_settings_phase2_part_1.py |
| TC-SET-5584 | P1 | Describe field value for APP_PORT | key=APP_PORT,field=value | present | test_settings_phase2_part_1.py |
| TC-SET-5585 | P1 | Describe field type for APP_PORT | key=APP_PORT,field=type | present | test_settings_phase2_part_1.py |
| TC-SET-5586 | P1 | Describe field editable for APP_PORT | key=APP_PORT,field=editable | present | test_settings_phase2_part_1.py |
| TC-SET-5587 | P1 | Describe field key for AUTO_TUNING_BATCH_HOUR | key=AUTO_TUNING_BATCH_HOUR,field=key | present | test_settings_phase2_part_1.py |
| TC-SET-5588 | P1 | Describe field value for AUTO_TUNING_BATCH_HOUR | key=AUTO_TUNING_BATCH_HOUR,field=value | present | test_settings_phase2_part_1.py |
| TC-SET-5589 | P1 | Describe field type for AUTO_TUNING_BATCH_HOUR | key=AUTO_TUNING_BATCH_HOUR,field=type | present | test_settings_phase2_part_1.py |
| TC-SET-5590 | P1 | Describe field editable for AUTO_TUNING_BATCH_HOUR | key=AUTO_TUNING_BATCH_HOUR,field=editable | present | test_settings_phase2_part_1.py |
| TC-SET-5591 | P1 | Describe field key for AUTO_TUNING_ENABLED | key=AUTO_TUNING_ENABLED,field=key | present | test_settings_phase2_part_1.py |
| TC-SET-5592 | P1 | Describe field value for AUTO_TUNING_ENABLED | key=AUTO_TUNING_ENABLED,field=value | present | test_settings_phase2_part_1.py |
| TC-SET-5593 | P1 | Describe field type for AUTO_TUNING_ENABLED | key=AUTO_TUNING_ENABLED,field=type | present | test_settings_phase2_part_1.py |
| TC-SET-5594 | P1 | Describe field editable for AUTO_TUNING_ENABLED | key=AUTO_TUNING_ENABLED,field=editable | present | test_settings_phase2_part_1.py |
| TC-SET-5595 | P1 | Describe field key for BLOOM_FILTER_CAPACITY | key=BLOOM_FILTER_CAPACITY,field=key | present | test_settings_phase2_part_1.py |
| TC-SET-5596 | P1 | Describe field value for BLOOM_FILTER_CAPACITY | key=BLOOM_FILTER_CAPACITY,field=value | present | test_settings_phase2_part_1.py |
| TC-SET-5597 | P1 | Describe field type for BLOOM_FILTER_CAPACITY | key=BLOOM_FILTER_CAPACITY,field=type | present | test_settings_phase2_part_1.py |
| TC-SET-5598 | P1 | Describe field editable for BLOOM_FILTER_CAPACITY | key=BLOOM_FILTER_CAPACITY,field=editable | present | test_settings_phase2_part_1.py |
| TC-SET-5599 | P1 | Describe field key for BLOOM_FILTER_ERROR_RATE | key=BLOOM_FILTER_ERROR_RATE,field=key | present | test_settings_phase2_part_1.py |
| TC-SET-5600 | P1 | Describe field value for BLOOM_FILTER_ERROR_RATE | key=BLOOM_FILTER_ERROR_RATE,field=value | present | test_settings_phase2_part_1.py |
| TC-SET-5601 | P1 | Describe field type for BLOOM_FILTER_ERROR_RATE | key=BLOOM_FILTER_ERROR_RATE,field=type | present | test_settings_phase2_part_1.py |
| TC-SET-5602 | P1 | Describe field editable for BLOOM_FILTER_ERROR_RATE | key=BLOOM_FILTER_ERROR_RATE,field=editable | present | test_settings_phase2_part_1.py |
| TC-SET-5603 | P1 | Describe field key for CACHE_MAX_SIZE | key=CACHE_MAX_SIZE,field=key | present | test_settings_phase2_part_1.py |
| TC-SET-5604 | P1 | Describe field value for CACHE_MAX_SIZE | key=CACHE_MAX_SIZE,field=value | present | test_settings_phase2_part_1.py |
| TC-SET-5605 | P1 | Describe field type for CACHE_MAX_SIZE | key=CACHE_MAX_SIZE,field=type | present | test_settings_phase2_part_1.py |
| TC-SET-5606 | P1 | Describe field editable for CACHE_MAX_SIZE | key=CACHE_MAX_SIZE,field=editable | present | test_settings_phase2_part_1.py |
| TC-SET-5607 | P1 | Describe field key for CACHE_TTL_SECONDS | key=CACHE_TTL_SECONDS,field=key | present | test_settings_phase2_part_1.py |
| TC-SET-5608 | P1 | Describe field value for CACHE_TTL_SECONDS | key=CACHE_TTL_SECONDS,field=value | present | test_settings_phase2_part_1.py |
| TC-SET-5609 | P1 | Describe field type for CACHE_TTL_SECONDS | key=CACHE_TTL_SECONDS,field=type | present | test_settings_phase2_part_1.py |
| TC-SET-5610 | P1 | Describe field editable for CACHE_TTL_SECONDS | key=CACHE_TTL_SECONDS,field=editable | present | test_settings_phase2_part_1.py |
| TC-SET-5611 | P1 | Describe field key for CUSTOM_WORDS_PATH | key=CUSTOM_WORDS_PATH,field=key | present | test_settings_phase2_part_1.py |
| TC-SET-5612 | P1 | Describe field value for CUSTOM_WORDS_PATH | key=CUSTOM_WORDS_PATH,field=value | present | test_settings_phase2_part_1.py |
| TC-SET-5613 | P1 | Describe field type for CUSTOM_WORDS_PATH | key=CUSTOM_WORDS_PATH,field=type | present | test_settings_phase2_part_1.py |
| TC-SET-5614 | P1 | Describe field editable for CUSTOM_WORDS_PATH | key=CUSTOM_WORDS_PATH,field=editable | present | test_settings_phase2_part_1.py |
| TC-SET-5615 | P1 | Describe field key for CUSTOM_WORDS_STORAGE | key=CUSTOM_WORDS_STORAGE,field=key | present | test_settings_phase2_part_1.py |
| TC-SET-5616 | P1 | Describe field value for CUSTOM_WORDS_STORAGE | key=CUSTOM_WORDS_STORAGE,field=value | present | test_settings_phase2_part_1.py |
| TC-SET-5617 | P1 | Describe field type for CUSTOM_WORDS_STORAGE | key=CUSTOM_WORDS_STORAGE,field=type | present | test_settings_phase2_part_1.py |
| TC-SET-5618 | P1 | Describe field editable for CUSTOM_WORDS_STORAGE | key=CUSTOM_WORDS_STORAGE,field=editable | present | test_settings_phase2_part_1.py |
| TC-SET-5619 | P1 | Describe field key for DETECTOR_THREAD_POOL_SIZE | key=DETECTOR_THREAD_POOL_SIZE,field=key | present | test_settings_phase2_part_1.py |
| TC-SET-5620 | P1 | Describe field value for DETECTOR_THREAD_POOL_SIZE | key=DETECTOR_THREAD_POOL_SIZE,field=value | present | test_settings_phase2_part_1.py |
| TC-SET-5621 | P1 | Describe field type for DETECTOR_THREAD_POOL_SIZE | key=DETECTOR_THREAD_POOL_SIZE,field=type | present | test_settings_phase2_part_1.py |
| TC-SET-5622 | P1 | Describe field editable for DETECTOR_THREAD_POOL_SIZE | key=DETECTOR_THREAD_POOL_SIZE,field=editable | present | test_settings_phase2_part_1.py |
| TC-SET-5623 | P1 | Describe field key for ENABLE_BADWORDS_PY | key=ENABLE_BADWORDS_PY,field=key | present | test_settings_phase2_part_1.py |
| TC-SET-5624 | P1 | Describe field value for ENABLE_BADWORDS_PY | key=ENABLE_BADWORDS_PY,field=value | present | test_settings_phase2_part_1.py |
| TC-SET-5625 | P1 | Describe field type for ENABLE_BADWORDS_PY | key=ENABLE_BADWORDS_PY,field=type | present | test_settings_phase2_part_1.py |
| TC-SET-5626 | P1 | Describe field editable for ENABLE_BADWORDS_PY | key=ENABLE_BADWORDS_PY,field=editable | present | test_settings_phase2_part_1.py |
| TC-SET-5627 | P1 | Describe field key for ENABLE_GANGAJAL | key=ENABLE_GANGAJAL,field=key | present | test_settings_phase2_part_1.py |
| TC-SET-5628 | P1 | Describe field value for ENABLE_GANGAJAL | key=ENABLE_GANGAJAL,field=value | present | test_settings_phase2_part_1.py |
| TC-SET-5629 | P1 | Describe field type for ENABLE_GANGAJAL | key=ENABLE_GANGAJAL,field=type | present | test_settings_phase2_part_1.py |
| TC-SET-5630 | P1 | Describe field editable for ENABLE_GANGAJAL | key=ENABLE_GANGAJAL,field=editable | present | test_settings_phase2_part_1.py |
| TC-SET-5631 | P1 | Describe field key for ENABLE_GLIN_PROFANITY | key=ENABLE_GLIN_PROFANITY,field=key | present | test_settings_phase2_part_1.py |
| TC-SET-5632 | P1 | Describe field value for ENABLE_GLIN_PROFANITY | key=ENABLE_GLIN_PROFANITY,field=value | present | test_settings_phase2_part_1.py |
| TC-SET-5633 | P1 | Describe field type for ENABLE_GLIN_PROFANITY | key=ENABLE_GLIN_PROFANITY,field=type | present | test_settings_phase2_part_1.py |
| TC-SET-5634 | P1 | Describe field editable for ENABLE_GLIN_PROFANITY | key=ENABLE_GLIN_PROFANITY,field=editable | present | test_settings_phase2_part_1.py |
| TC-SET-5635 | P1 | Describe field key for ENABLE_PROFANITE | key=ENABLE_PROFANITE,field=key | present | test_settings_phase2_part_1.py |
| TC-SET-5636 | P1 | Describe field value for ENABLE_PROFANITE | key=ENABLE_PROFANITE,field=value | present | test_settings_phase2_part_1.py |
| TC-SET-5637 | P1 | Describe field type for ENABLE_PROFANITE | key=ENABLE_PROFANITE,field=type | present | test_settings_phase2_part_1.py |
| TC-SET-5638 | P1 | Describe field editable for ENABLE_PROFANITE | key=ENABLE_PROFANITE,field=editable | present | test_settings_phase2_part_1.py |
| TC-SET-5639 | P1 | Describe field key for ENABLE_PROFANITY_FILTER | key=ENABLE_PROFANITY_FILTER,field=key | present | test_settings_phase2_part_1.py |
| TC-SET-5640 | P1 | Describe field value for ENABLE_PROFANITY_FILTER | key=ENABLE_PROFANITY_FILTER,field=value | present | test_settings_phase2_part_1.py |
| TC-SET-5641 | P1 | Describe field type for ENABLE_PROFANITY_FILTER | key=ENABLE_PROFANITY_FILTER,field=type | present | test_settings_phase2_part_1.py |
| TC-SET-5642 | P1 | Describe field editable for ENABLE_PROFANITY_FILTER | key=ENABLE_PROFANITY_FILTER,field=editable | present | test_settings_phase2_part_1.py |
| TC-SET-5643 | P1 | Describe field key for ENABLE_PYPROFANE | key=ENABLE_PYPROFANE,field=key | present | test_settings_phase2_part_1.py |
| TC-SET-5644 | P1 | Describe field value for ENABLE_PYPROFANE | key=ENABLE_PYPROFANE,field=value | present | test_settings_phase2_part_1.py |
| TC-SET-5645 | P1 | Describe field type for ENABLE_PYPROFANE | key=ENABLE_PYPROFANE,field=type | present | test_settings_phase2_part_1.py |
| TC-SET-5646 | P1 | Describe field editable for ENABLE_PYPROFANE | key=ENABLE_PYPROFANE,field=editable | present | test_settings_phase2_part_1.py |
| TC-SET-5647 | P1 | Describe field key for ENABLE_SAFETEXT | key=ENABLE_SAFETEXT,field=key | present | test_settings_phase2_part_1.py |
| TC-SET-5648 | P1 | Describe field value for ENABLE_SAFETEXT | key=ENABLE_SAFETEXT,field=value | present | test_settings_phase2_part_1.py |
| TC-SET-5649 | P1 | Describe field type for ENABLE_SAFETEXT | key=ENABLE_SAFETEXT,field=type | present | test_settings_phase2_part_1.py |
| TC-SET-5650 | P1 | Describe field editable for ENABLE_SAFETEXT | key=ENABLE_SAFETEXT,field=editable | present | test_settings_phase2_part_1.py |
| TC-SET-5651 | P1 | Describe field key for ENABLE_SENSITIVE_STOP_WORDS | key=ENABLE_SENSITIVE_STOP_WORDS,field=key | present | test_settings_phase2_part_1.py |
| TC-SET-5652 | P1 | Describe field value for ENABLE_SENSITIVE_STOP_WORDS | key=ENABLE_SENSITIVE_STOP_WORDS,field=value | present | test_settings_phase2_part_1.py |
| TC-SET-5653 | P1 | Describe field type for ENABLE_SENSITIVE_STOP_WORDS | key=ENABLE_SENSITIVE_STOP_WORDS,field=type | present | test_settings_phase2_part_1.py |
| TC-SET-5654 | P1 | Describe field editable for ENABLE_SENSITIVE_STOP_WORDS | key=ENABLE_SENSITIVE_STOP_WORDS,field=editable | present | test_settings_phase2_part_1.py |
| TC-SET-5655 | P1 | Describe field key for ENABLE_SENSITIVE_WORD_FILTER_CN | key=ENABLE_SENSITIVE_WORD_FILTER_CN,field=key | present | test_settings_phase2_part_1.py |
| TC-SET-5656 | P1 | Describe field value for ENABLE_SENSITIVE_WORD_FILTER_CN | key=ENABLE_SENSITIVE_WORD_FILTER_CN,field=value | present | test_settings_phase2_part_1.py |
| TC-SET-5657 | P1 | Describe field type for ENABLE_SENSITIVE_WORD_FILTER_CN | key=ENABLE_SENSITIVE_WORD_FILTER_CN,field=type | present | test_settings_phase2_part_1.py |
| TC-SET-5658 | P1 | Describe field editable for ENABLE_SENSITIVE_WORD_FILTER_CN | key=ENABLE_SENSITIVE_WORD_FILTER_CN,field=editable | present | test_settings_phase2_part_1.py |
| TC-SET-5659 | P1 | Describe field key for ENCRYPTION_KEY | key=ENCRYPTION_KEY,field=key | present | test_settings_phase2_part_1.py |
| TC-SET-5660 | P1 | Describe field value for ENCRYPTION_KEY | key=ENCRYPTION_KEY,field=value | present | test_settings_phase2_part_1.py |
| TC-SET-5661 | P1 | Describe field type for ENCRYPTION_KEY | key=ENCRYPTION_KEY,field=type | present | test_settings_phase2_part_1.py |
| TC-SET-5662 | P1 | Describe field editable for ENCRYPTION_KEY | key=ENCRYPTION_KEY,field=editable | present | test_settings_phase2_part_1.py |
| TC-SET-5663 | P1 | Describe field key for EXPORT_RETENTION_DAYS | key=EXPORT_RETENTION_DAYS,field=key | present | test_settings_phase2_part_2.py |
| TC-SET-5664 | P1 | Describe field value for EXPORT_RETENTION_DAYS | key=EXPORT_RETENTION_DAYS,field=value | present | test_settings_phase2_part_2.py |
| TC-SET-5665 | P1 | Describe field type for EXPORT_RETENTION_DAYS | key=EXPORT_RETENTION_DAYS,field=type | present | test_settings_phase2_part_2.py |
| TC-SET-5666 | P1 | Describe field editable for EXPORT_RETENTION_DAYS | key=EXPORT_RETENTION_DAYS,field=editable | present | test_settings_phase2_part_2.py |
| TC-SET-5667 | P1 | Describe field key for EXPORT_TEMP_DIR | key=EXPORT_TEMP_DIR,field=key | present | test_settings_phase2_part_2.py |
| TC-SET-5668 | P1 | Describe field value for EXPORT_TEMP_DIR | key=EXPORT_TEMP_DIR,field=value | present | test_settings_phase2_part_2.py |
| TC-SET-5669 | P1 | Describe field type for EXPORT_TEMP_DIR | key=EXPORT_TEMP_DIR,field=type | present | test_settings_phase2_part_2.py |
| TC-SET-5670 | P1 | Describe field editable for EXPORT_TEMP_DIR | key=EXPORT_TEMP_DIR,field=editable | present | test_settings_phase2_part_2.py |
| TC-SET-5671 | P1 | Describe field key for FEEDBACK_DB_PATH | key=FEEDBACK_DB_PATH,field=key | present | test_settings_phase2_part_2.py |
| TC-SET-5672 | P1 | Describe field value for FEEDBACK_DB_PATH | key=FEEDBACK_DB_PATH,field=value | present | test_settings_phase2_part_2.py |
| TC-SET-5673 | P1 | Describe field type for FEEDBACK_DB_PATH | key=FEEDBACK_DB_PATH,field=type | present | test_settings_phase2_part_2.py |
| TC-SET-5674 | P1 | Describe field editable for FEEDBACK_DB_PATH | key=FEEDBACK_DB_PATH,field=editable | present | test_settings_phase2_part_2.py |
| TC-SET-5675 | P1 | Describe field key for FORCE_LLM_ON_SEMANTIC_HIGH | key=FORCE_LLM_ON_SEMANTIC_HIGH,field=key | present | test_settings_phase2_part_2.py |
| TC-SET-5676 | P1 | Describe field value for FORCE_LLM_ON_SEMANTIC_HIGH | key=FORCE_LLM_ON_SEMANTIC_HIGH,field=value | present | test_settings_phase2_part_2.py |
| TC-SET-5677 | P1 | Describe field type for FORCE_LLM_ON_SEMANTIC_HIGH | key=FORCE_LLM_ON_SEMANTIC_HIGH,field=type | present | test_settings_phase2_part_2.py |
| TC-SET-5678 | P1 | Describe field editable for FORCE_LLM_ON_SEMANTIC_HIGH | key=FORCE_LLM_ON_SEMANTIC_HIGH,field=editable | present | test_settings_phase2_part_2.py |
| TC-SET-5679 | P1 | Describe field key for FORCE_LLM_ON_USER_RATIO_HIGH | key=FORCE_LLM_ON_USER_RATIO_HIGH,field=key | present | test_settings_phase2_part_2.py |
| TC-SET-5680 | P1 | Describe field value for FORCE_LLM_ON_USER_RATIO_HIGH | key=FORCE_LLM_ON_USER_RATIO_HIGH,field=value | present | test_settings_phase2_part_2.py |
| TC-SET-5681 | P1 | Describe field type for FORCE_LLM_ON_USER_RATIO_HIGH | key=FORCE_LLM_ON_USER_RATIO_HIGH,field=type | present | test_settings_phase2_part_2.py |
| TC-SET-5682 | P1 | Describe field editable for FORCE_LLM_ON_USER_RATIO_HIGH | key=FORCE_LLM_ON_USER_RATIO_HIGH,field=editable | present | test_settings_phase2_part_2.py |
| TC-SET-5683 | P1 | Describe field key for FRONTEND_DIST_PATH | key=FRONTEND_DIST_PATH,field=key | present | test_settings_phase2_part_2.py |
| TC-SET-5684 | P1 | Describe field value for FRONTEND_DIST_PATH | key=FRONTEND_DIST_PATH,field=value | present | test_settings_phase2_part_2.py |
| TC-SET-5685 | P1 | Describe field type for FRONTEND_DIST_PATH | key=FRONTEND_DIST_PATH,field=type | present | test_settings_phase2_part_2.py |
| TC-SET-5686 | P1 | Describe field editable for FRONTEND_DIST_PATH | key=FRONTEND_DIST_PATH,field=editable | present | test_settings_phase2_part_2.py |
| TC-SET-5687 | P1 | Describe field key for FUZZY_MAX_DISTANCE | key=FUZZY_MAX_DISTANCE,field=key | present | test_settings_phase2_part_2.py |
| TC-SET-5688 | P1 | Describe field value for FUZZY_MAX_DISTANCE | key=FUZZY_MAX_DISTANCE,field=value | present | test_settings_phase2_part_2.py |
| TC-SET-5689 | P1 | Describe field type for FUZZY_MAX_DISTANCE | key=FUZZY_MAX_DISTANCE,field=type | present | test_settings_phase2_part_2.py |
| TC-SET-5690 | P1 | Describe field editable for FUZZY_MAX_DISTANCE | key=FUZZY_MAX_DISTANCE,field=editable | present | test_settings_phase2_part_2.py |
| TC-SET-5691 | P1 | Describe field key for HF_ENDPOINT | key=HF_ENDPOINT,field=key | present | test_settings_phase2_part_2.py |
| TC-SET-5692 | P1 | Describe field value for HF_ENDPOINT | key=HF_ENDPOINT,field=value | present | test_settings_phase2_part_2.py |
| TC-SET-5693 | P1 | Describe field type for HF_ENDPOINT | key=HF_ENDPOINT,field=type | present | test_settings_phase2_part_2.py |
| TC-SET-5694 | P1 | Describe field editable for HF_ENDPOINT | key=HF_ENDPOINT,field=editable | present | test_settings_phase2_part_2.py |
| TC-SET-5695 | P1 | Describe field key for HF_MIRROR | key=HF_MIRROR,field=key | present | test_settings_phase2_part_2.py |
| TC-SET-5696 | P1 | Describe field value for HF_MIRROR | key=HF_MIRROR,field=value | present | test_settings_phase2_part_2.py |
| TC-SET-5697 | P1 | Describe field type for HF_MIRROR | key=HF_MIRROR,field=type | present | test_settings_phase2_part_2.py |
| TC-SET-5698 | P1 | Describe field editable for HF_MIRROR | key=HF_MIRROR,field=editable | present | test_settings_phase2_part_2.py |
| TC-SET-5699 | P1 | Describe field key for LLM_RESPONSE_TIMEOUT_SECONDS | key=LLM_RESPONSE_TIMEOUT_SECONDS,field=key | present | test_settings_phase2_part_2.py |
| TC-SET-5700 | P1 | Describe field value for LLM_RESPONSE_TIMEOUT_SECONDS | key=LLM_RESPONSE_TIMEOUT_SECONDS,field=value | present | test_settings_phase2_part_2.py |
| TC-SET-5701 | P1 | Describe field type for LLM_RESPONSE_TIMEOUT_SECONDS | key=LLM_RESPONSE_TIMEOUT_SECONDS,field=type | present | test_settings_phase2_part_2.py |
| TC-SET-5702 | P1 | Describe field editable for LLM_RESPONSE_TIMEOUT_SECONDS | key=LLM_RESPONSE_TIMEOUT_SECONDS,field=editable | present | test_settings_phase2_part_2.py |
| TC-SET-5703 | P1 | Describe field key for LOG_BACKUP_COUNT | key=LOG_BACKUP_COUNT,field=key | present | test_settings_phase2_part_2.py |
| TC-SET-5704 | P1 | Describe field value for LOG_BACKUP_COUNT | key=LOG_BACKUP_COUNT,field=value | present | test_settings_phase2_part_2.py |
| TC-SET-5705 | P1 | Describe field type for LOG_BACKUP_COUNT | key=LOG_BACKUP_COUNT,field=type | present | test_settings_phase2_part_2.py |
| TC-SET-5706 | P1 | Describe field editable for LOG_BACKUP_COUNT | key=LOG_BACKUP_COUNT,field=editable | present | test_settings_phase2_part_2.py |
| TC-SET-5707 | P1 | Describe field key for LOG_FILE_PATH | key=LOG_FILE_PATH,field=key | present | test_settings_phase2_part_2.py |
| TC-SET-5708 | P1 | Describe field value for LOG_FILE_PATH | key=LOG_FILE_PATH,field=value | present | test_settings_phase2_part_2.py |
| TC-SET-5709 | P1 | Describe field type for LOG_FILE_PATH | key=LOG_FILE_PATH,field=type | present | test_settings_phase2_part_2.py |
| TC-SET-5710 | P1 | Describe field editable for LOG_FILE_PATH | key=LOG_FILE_PATH,field=editable | present | test_settings_phase2_part_2.py |
| TC-SET-5711 | P1 | Describe field key for LOG_LEVEL | key=LOG_LEVEL,field=key | present | test_settings_phase2_part_2.py |
| TC-SET-5712 | P1 | Describe field value for LOG_LEVEL | key=LOG_LEVEL,field=value | present | test_settings_phase2_part_2.py |
| TC-SET-5967 | P1 | Read-only ADMIN_API_KEY attempt 0 | key=ADMIN_API_KEY,attempt=0 | rejected | test_settings_phase2_part_2.py |
| TC-SET-5968 | P1 | Read-only ADMIN_API_KEY attempt 1 | key=ADMIN_API_KEY,attempt=1 | rejected | test_settings_phase2_part_2.py |
| TC-SET-5969 | P1 | Read-only ADMIN_API_KEY attempt 2 | key=ADMIN_API_KEY,attempt=2 | rejected | test_settings_phase2_part_2.py |
| TC-SET-5970 | P1 | Read-only ADMIN_API_KEY attempt 3 | key=ADMIN_API_KEY,attempt=3 | rejected | test_settings_phase2_part_2.py |
| TC-SET-5971 | P1 | Read-only ADMIN_API_KEY attempt 4 | key=ADMIN_API_KEY,attempt=4 | rejected | test_settings_phase2_part_2.py |
| TC-SET-5972 | P1 | Read-only ADMIN_API_KEY attempt 5 | key=ADMIN_API_KEY,attempt=5 | rejected | test_settings_phase2_part_2.py |
| TC-SET-5973 | P1 | Read-only APP_PORT attempt 0 | key=APP_PORT,attempt=0 | rejected | test_settings_phase2_part_2.py |
| TC-SET-5974 | P1 | Read-only APP_PORT attempt 1 | key=APP_PORT,attempt=1 | rejected | test_settings_phase2_part_2.py |
| TC-SET-5975 | P1 | Read-only APP_PORT attempt 2 | key=APP_PORT,attempt=2 | rejected | test_settings_phase2_part_2.py |
| TC-SET-5976 | P1 | Read-only APP_PORT attempt 3 | key=APP_PORT,attempt=3 | rejected | test_settings_phase2_part_2.py |
| TC-SET-5977 | P1 | Read-only APP_PORT attempt 4 | key=APP_PORT,attempt=4 | rejected | test_settings_phase2_part_2.py |
| TC-SET-5978 | P1 | Read-only APP_PORT attempt 5 | key=APP_PORT,attempt=5 | rejected | test_settings_phase2_part_2.py |
| TC-SET-5979 | P1 | Read-only ENCRYPTION_KEY attempt 0 | key=ENCRYPTION_KEY,attempt=0 | rejected | test_settings_phase2_part_2.py |
| TC-SET-5980 | P1 | Read-only ENCRYPTION_KEY attempt 1 | key=ENCRYPTION_KEY,attempt=1 | rejected | test_settings_phase2_part_2.py |
| TC-SET-5981 | P1 | Read-only ENCRYPTION_KEY attempt 2 | key=ENCRYPTION_KEY,attempt=2 | rejected | test_settings_phase2_part_2.py |
| TC-SET-5982 | P1 | Read-only ENCRYPTION_KEY attempt 3 | key=ENCRYPTION_KEY,attempt=3 | rejected | test_settings_phase2_part_2.py |
| TC-SET-5983 | P1 | Read-only ENCRYPTION_KEY attempt 4 | key=ENCRYPTION_KEY,attempt=4 | rejected | test_settings_phase2_part_2.py |
| TC-SET-5984 | P1 | Read-only ENCRYPTION_KEY attempt 5 | key=ENCRYPTION_KEY,attempt=5 | rejected | test_settings_phase2_part_2.py |
| TC-SET-5985 | P1 | Read-only EXPORT_TEMP_DIR attempt 0 | key=EXPORT_TEMP_DIR,attempt=0 | rejected | test_settings_phase2_part_2.py |
| TC-SET-5986 | P1 | Read-only EXPORT_TEMP_DIR attempt 1 | key=EXPORT_TEMP_DIR,attempt=1 | rejected | test_settings_phase2_part_2.py |
| TC-SET-5987 | P1 | Read-only EXPORT_TEMP_DIR attempt 2 | key=EXPORT_TEMP_DIR,attempt=2 | rejected | test_settings_phase2_part_2.py |
| TC-SET-5988 | P1 | Read-only EXPORT_TEMP_DIR attempt 3 | key=EXPORT_TEMP_DIR,attempt=3 | rejected | test_settings_phase2_part_2.py |
| TC-SET-5989 | P1 | Read-only EXPORT_TEMP_DIR attempt 4 | key=EXPORT_TEMP_DIR,attempt=4 | rejected | test_settings_phase2_part_2.py |
| TC-SET-5990 | P1 | Read-only EXPORT_TEMP_DIR attempt 5 | key=EXPORT_TEMP_DIR,attempt=5 | rejected | test_settings_phase2_part_2.py |
| TC-SET-5991 | P1 | Read-only FEEDBACK_DB_PATH attempt 0 | key=FEEDBACK_DB_PATH,attempt=0 | rejected | test_settings_phase2_part_2.py |
| TC-SET-5992 | P1 | Read-only FEEDBACK_DB_PATH attempt 1 | key=FEEDBACK_DB_PATH,attempt=1 | rejected | test_settings_phase2_part_2.py |
| TC-SET-5993 | P1 | Read-only FEEDBACK_DB_PATH attempt 2 | key=FEEDBACK_DB_PATH,attempt=2 | rejected | test_settings_phase2_part_2.py |
| TC-SET-5994 | P1 | Read-only FEEDBACK_DB_PATH attempt 3 | key=FEEDBACK_DB_PATH,attempt=3 | rejected | test_settings_phase2_part_2.py |
| TC-SET-5995 | P1 | Read-only FEEDBACK_DB_PATH attempt 4 | key=FEEDBACK_DB_PATH,attempt=4 | rejected | test_settings_phase2_part_2.py |
| TC-SET-5996 | P1 | Read-only FEEDBACK_DB_PATH attempt 5 | key=FEEDBACK_DB_PATH,attempt=5 | rejected | test_settings_phase2_part_2.py |
| TC-SET-5997 | P1 | Read-only MODEL_PATH attempt 0 | key=MODEL_PATH,attempt=0 | rejected | test_settings_phase2_part_2.py |
| TC-SET-5998 | P1 | Read-only MODEL_PATH attempt 1 | key=MODEL_PATH,attempt=1 | rejected | test_settings_phase2_part_2.py |
| TC-SET-5999 | P1 | Read-only MODEL_PATH attempt 2 | key=MODEL_PATH,attempt=2 | rejected | test_settings_phase2_part_2.py |
| TC-SET-6000 | P1 | Read-only MODEL_PATH attempt 3 | key=MODEL_PATH,attempt=3 | rejected | test_settings_phase2_part_2.py |
| TC-SET-6001 | P1 | Read-only MODEL_PATH attempt 4 | key=MODEL_PATH,attempt=4 | rejected | test_settings_phase2_part_2.py |
| TC-SET-6002 | P1 | Read-only MODEL_PATH attempt 5 | key=MODEL_PATH,attempt=5 | rejected | test_settings_phase2_part_2.py |
| TC-SET-6003 | P1 | Read-only SECRET_KEY attempt 0 | key=SECRET_KEY,attempt=0 | rejected | test_settings_phase2_part_2.py |
| TC-SET-6004 | P1 | Read-only SECRET_KEY attempt 1 | key=SECRET_KEY,attempt=1 | rejected | test_settings_phase2_part_2.py |
| TC-SET-6005 | P1 | Read-only SECRET_KEY attempt 2 | key=SECRET_KEY,attempt=2 | rejected | test_settings_phase2_part_2.py |
| TC-SET-6006 | P1 | Read-only SECRET_KEY attempt 3 | key=SECRET_KEY,attempt=3 | rejected | test_settings_phase2_part_2.py |
| TC-SET-6007 | P1 | Read-only SECRET_KEY attempt 4 | key=SECRET_KEY,attempt=4 | rejected | test_settings_phase2_part_2.py |
| TC-SET-6008 | P1 | Read-only SECRET_KEY attempt 5 | key=SECRET_KEY,attempt=5 | rejected | test_settings_phase2_part_2.py |
| TC-SET-6009 | P1 | Read-only WEBUI_API_KEY attempt 0 | key=WEBUI_API_KEY,attempt=0 | rejected | test_settings_phase2_part_2.py |
| TC-SET-6010 | P1 | Read-only WEBUI_API_KEY attempt 1 | key=WEBUI_API_KEY,attempt=1 | rejected | test_settings_phase2_part_2.py |
| TC-SET-6011 | P1 | Read-only WEBUI_API_KEY attempt 2 | key=WEBUI_API_KEY,attempt=2 | rejected | test_settings_phase2_part_2.py |
| TC-SET-6012 | P1 | Read-only WEBUI_API_KEY attempt 3 | key=WEBUI_API_KEY,attempt=3 | rejected | test_settings_phase2_part_2.py |
| TC-SET-6013 | P1 | Read-only WEBUI_API_KEY attempt 4 | key=WEBUI_API_KEY,attempt=4 | rejected | test_settings_phase2_part_2.py |
| TC-SET-6014 | P1 | Read-only WEBUI_API_KEY attempt 5 | key=WEBUI_API_KEY,attempt=5 | rejected | test_settings_phase2_part_2.py |
| TC-SET-6015 | P1 | Read-only WORKERS attempt 0 | key=WORKERS,attempt=0 | rejected | test_settings_phase2_part_2.py |
| TC-SET-6016 | P1 | Read-only WORKERS attempt 1 | key=WORKERS,attempt=1 | rejected | test_settings_phase2_part_2.py |
| TC-SET-6017 | P2 | Valid update AI_TARGET_PERCENTAGE = 25 | key=AI_TARGET_PERCENTAGE,value=25 | accepted | test_settings_phase2_part_3.py |
| TC-SET-6018 | P2 | Valid update AI_TARGET_PERCENTAGE = 50 | key=AI_TARGET_PERCENTAGE,value=50 | accepted | test_settings_phase2_part_3.py |
| TC-SET-6019 | P2 | Valid update AI_TARGET_PERCENTAGE = 100 | key=AI_TARGET_PERCENTAGE,value=100 | accepted | test_settings_phase2_part_3.py |
| TC-SET-6020 | P2 | Valid update ALLOWED_ORIGINS = sample-value | key=ALLOWED_ORIGINS,value='sample-value' | accepted | test_settings_phase2_part_3.py |
| TC-SET-6021 | P2 | Valid update ALLOWED_ORIGINS = config-value | key=ALLOWED_ORIGINS,value='config-value' | accepted | test_settings_phase2_part_3.py |
| TC-SET-6022 | P2 | Valid update ALLOWED_ORIGINS = 192.168.0.1 | key=ALLOWED_ORIGINS,value='192.168.0.1' | accepted | test_settings_phase2_part_3.py |
| TC-SET-6023 | P2 | Valid update APP_CONFIG_DB_PATH = sample-value | key=APP_CONFIG_DB_PATH,value='sample-value' | accepted | test_settings_phase2_part_3.py |
| TC-SET-6024 | P2 | Valid update APP_CONFIG_DB_PATH = config-value | key=APP_CONFIG_DB_PATH,value='config-value' | accepted | test_settings_phase2_part_3.py |
| TC-SET-6025 | P2 | Valid update APP_CONFIG_DB_PATH = 192.168.0.1 | key=APP_CONFIG_DB_PATH,value='192.168.0.1' | accepted | test_settings_phase2_part_3.py |
| TC-SET-6026 | P2 | Valid update APP_HOST = sample-value | key=APP_HOST,value='sample-value' | accepted | test_settings_phase2_part_3.py |
| TC-SET-6027 | P2 | Valid update APP_HOST = config-value | key=APP_HOST,value='config-value' | accepted | test_settings_phase2_part_3.py |
| TC-SET-6028 | P2 | Valid update APP_HOST = 192.168.0.1 | key=APP_HOST,value='192.168.0.1' | accepted | test_settings_phase2_part_3.py |
| TC-SET-6029 | P2 | Valid update AUTO_TUNING_ENABLED = True | key=AUTO_TUNING_ENABLED,value=True | accepted | test_settings_phase2_part_3.py |
| TC-SET-6030 | P2 | Valid update AUTO_TUNING_ENABLED = False | key=AUTO_TUNING_ENABLED,value=False | accepted | test_settings_phase2_part_3.py |
| TC-SET-6031 | P2 | Valid update BLOOM_FILTER_CAPACITY = sample-value | key=BLOOM_FILTER_CAPACITY,value='sample-value' | accepted | test_settings_phase2_part_3.py |
| TC-SET-6032 | P2 | Valid update BLOOM_FILTER_CAPACITY = config-value | key=BLOOM_FILTER_CAPACITY,value='config-value' | accepted | test_settings_phase2_part_3.py |
| TC-SET-6033 | P2 | Valid update BLOOM_FILTER_CAPACITY = 192.168.0.1 | key=BLOOM_FILTER_CAPACITY,value='192.168.0.1' | accepted | test_settings_phase2_part_3.py |
| TC-SET-6034 | P2 | Valid update BLOOM_FILTER_ERROR_RATE = sample-value | key=BLOOM_FILTER_ERROR_RATE,value='sample-value' | accepted | test_settings_phase2_part_3.py |
| TC-SET-6035 | P2 | Valid update BLOOM_FILTER_ERROR_RATE = config-value | key=BLOOM_FILTER_ERROR_RATE,value='config-value' | accepted | test_settings_phase2_part_3.py |
| TC-SET-6036 | P2 | Valid update BLOOM_FILTER_ERROR_RATE = 192.168.0.1 | key=BLOOM_FILTER_ERROR_RATE,value='192.168.0.1' | accepted | test_settings_phase2_part_3.py |
| TC-SET-6037 | P2 | Valid update CACHE_MAX_SIZE = 25 | key=CACHE_MAX_SIZE,value=25 | accepted | test_settings_phase2_part_3.py |
| TC-SET-6038 | P2 | Valid update CACHE_MAX_SIZE = 50 | key=CACHE_MAX_SIZE,value=50 | accepted | test_settings_phase2_part_3.py |
| TC-SET-6039 | P2 | Valid update CACHE_MAX_SIZE = 100 | key=CACHE_MAX_SIZE,value=100 | accepted | test_settings_phase2_part_3.py |
| TC-SET-6040 | P2 | Valid update CACHE_MAX_SIZE = 250 | key=CACHE_MAX_SIZE,value=250 | accepted | test_settings_phase2_part_3.py |
| TC-SET-6041 | P2 | Valid update CACHE_MAX_SIZE = 500 | key=CACHE_MAX_SIZE,value=500 | accepted | test_settings_phase2_part_3.py |
| TC-SET-6042 | P2 | Valid update CACHE_TTL_SECONDS = 25 | key=CACHE_TTL_SECONDS,value=25 | accepted | test_settings_phase2_part_3.py |
| TC-SET-6043 | P2 | Valid update CACHE_TTL_SECONDS = 50 | key=CACHE_TTL_SECONDS,value=50 | accepted | test_settings_phase2_part_3.py |
| TC-SET-6044 | P2 | Valid update CACHE_TTL_SECONDS = 100 | key=CACHE_TTL_SECONDS,value=100 | accepted | test_settings_phase2_part_3.py |
| TC-SET-6045 | P2 | Valid update CACHE_TTL_SECONDS = 250 | key=CACHE_TTL_SECONDS,value=250 | accepted | test_settings_phase2_part_3.py |
| TC-SET-6046 | P2 | Valid update CACHE_TTL_SECONDS = 500 | key=CACHE_TTL_SECONDS,value=500 | accepted | test_settings_phase2_part_3.py |
| TC-SET-6047 | P2 | Valid update CUSTOM_WORDS_PATH = sample-value | key=CUSTOM_WORDS_PATH,value='sample-value' | accepted | test_settings_phase2_part_3.py |
| TC-SET-6048 | P2 | Valid update CUSTOM_WORDS_PATH = config-value | key=CUSTOM_WORDS_PATH,value='config-value' | accepted | test_settings_phase2_part_3.py |
| TC-SET-6049 | P2 | Valid update CUSTOM_WORDS_PATH = 192.168.0.1 | key=CUSTOM_WORDS_PATH,value='192.168.0.1' | accepted | test_settings_phase2_part_3.py |
| TC-SET-6050 | P2 | Valid update CUSTOM_WORDS_STORAGE = sample-value | key=CUSTOM_WORDS_STORAGE,value='sample-value' | accepted | test_settings_phase2_part_3.py |
| TC-SET-6051 | P2 | Valid update CUSTOM_WORDS_STORAGE = config-value | key=CUSTOM_WORDS_STORAGE,value='config-value' | accepted | test_settings_phase2_part_3.py |
| TC-SET-6052 | P2 | Valid update CUSTOM_WORDS_STORAGE = 192.168.0.1 | key=CUSTOM_WORDS_STORAGE,value='192.168.0.1' | accepted | test_settings_phase2_part_3.py |
| TC-SET-6053 | P2 | Valid update DETECTOR_THREAD_POOL_SIZE = 25 | key=DETECTOR_THREAD_POOL_SIZE,value=25 | accepted | test_settings_phase2_part_3.py |
| TC-SET-6054 | P2 | Valid update DETECTOR_THREAD_POOL_SIZE = 50 | key=DETECTOR_THREAD_POOL_SIZE,value=50 | accepted | test_settings_phase2_part_3.py |
| TC-SET-6055 | P2 | Valid update ENABLE_BADWORDS_PY = True | key=ENABLE_BADWORDS_PY,value=True | accepted | test_settings_phase2_part_3.py |
| TC-SET-6056 | P2 | Valid update ENABLE_BADWORDS_PY = False | key=ENABLE_BADWORDS_PY,value=False | accepted | test_settings_phase2_part_3.py |
| TC-SET-6057 | P2 | Valid update ENABLE_GANGAJAL = True | key=ENABLE_GANGAJAL,value=True | accepted | test_settings_phase2_part_3.py |
| TC-SET-6058 | P2 | Valid update ENABLE_GANGAJAL = False | key=ENABLE_GANGAJAL,value=False | accepted | test_settings_phase2_part_3.py |
| TC-SET-6059 | P2 | Valid update ENABLE_GLIN_PROFANITY = True | key=ENABLE_GLIN_PROFANITY,value=True | accepted | test_settings_phase2_part_3.py |
| TC-SET-6060 | P2 | Valid update ENABLE_GLIN_PROFANITY = False | key=ENABLE_GLIN_PROFANITY,value=False | accepted | test_settings_phase2_part_3.py |
| TC-SET-6061 | P2 | Valid update ENABLE_PROFANITE = True | key=ENABLE_PROFANITE,value=True | accepted | test_settings_phase2_part_3.py |
| TC-SET-6062 | P2 | Valid update ENABLE_PROFANITE = False | key=ENABLE_PROFANITE,value=False | accepted | test_settings_phase2_part_3.py |
| TC-SET-6063 | P2 | Valid update ENABLE_PROFANITY_FILTER = True | key=ENABLE_PROFANITY_FILTER,value=True | accepted | test_settings_phase2_part_3.py |
| TC-SET-6064 | P2 | Valid update ENABLE_PROFANITY_FILTER = False | key=ENABLE_PROFANITY_FILTER,value=False | accepted | test_settings_phase2_part_3.py |
| TC-SET-6065 | P2 | Valid update ENABLE_PYPROFANE = True | key=ENABLE_PYPROFANE,value=True | accepted | test_settings_phase2_part_3.py |
| TC-SET-6066 | P2 | Valid update ENABLE_PYPROFANE = False | key=ENABLE_PYPROFANE,value=False | accepted | test_settings_phase2_part_3.py |
| TC-SET-6067 | P2 | Valid update ENABLE_SAFETEXT = True | key=ENABLE_SAFETEXT,value=True | accepted | test_settings_phase2_part_3.py |
| TC-SET-6068 | P2 | Valid update ENABLE_SAFETEXT = False | key=ENABLE_SAFETEXT,value=False | accepted | test_settings_phase2_part_3.py |
| TC-SET-6069 | P2 | Valid update ENABLE_SENSITIVE_STOP_WORDS = True | key=ENABLE_SENSITIVE_STOP_WORDS,value=True | accepted | test_settings_phase2_part_3.py |
| TC-SET-6070 | P2 | Valid update ENABLE_SENSITIVE_STOP_WORDS = False | key=ENABLE_SENSITIVE_STOP_WORDS,value=False | accepted | test_settings_phase2_part_3.py |
| TC-SET-6071 | P2 | Valid update ENABLE_SENSITIVE_WORD_FILTER_CN = True | key=ENABLE_SENSITIVE_WORD_FILTER_CN,value=True | accepted | test_settings_phase2_part_3.py |
| TC-SET-6072 | P2 | Valid update ENABLE_SENSITIVE_WORD_FILTER_CN = False | key=ENABLE_SENSITIVE_WORD_FILTER_CN,value=False | accepted | test_settings_phase2_part_3.py |
| TC-SET-6073 | P2 | Valid update EXPORT_RETENTION_DAYS = 25 | key=EXPORT_RETENTION_DAYS,value=25 | accepted | test_settings_phase2_part_3.py |
| TC-SET-6074 | P2 | Valid update EXPORT_RETENTION_DAYS = 50 | key=EXPORT_RETENTION_DAYS,value=50 | accepted | test_settings_phase2_part_3.py |
| TC-SET-6075 | P2 | Valid update EXPORT_RETENTION_DAYS = 100 | key=EXPORT_RETENTION_DAYS,value=100 | accepted | test_settings_phase2_part_3.py |
| TC-SET-6076 | P2 | Valid update EXPORT_RETENTION_DAYS = 250 | key=EXPORT_RETENTION_DAYS,value=250 | accepted | test_settings_phase2_part_3.py |
| TC-SET-6077 | P2 | Valid update FORCE_LLM_ON_SEMANTIC_HIGH = True | key=FORCE_LLM_ON_SEMANTIC_HIGH,value=True | accepted | test_settings_phase2_part_3.py |
| TC-SET-6078 | P2 | Valid update FORCE_LLM_ON_SEMANTIC_HIGH = False | key=FORCE_LLM_ON_SEMANTIC_HIGH,value=False | accepted | test_settings_phase2_part_3.py |
| TC-SET-6079 | P2 | Valid update FORCE_LLM_ON_USER_RATIO_HIGH = True | key=FORCE_LLM_ON_USER_RATIO_HIGH,value=True | accepted | test_settings_phase2_part_3.py |
| TC-SET-6080 | P2 | Valid update FORCE_LLM_ON_USER_RATIO_HIGH = False | key=FORCE_LLM_ON_USER_RATIO_HIGH,value=False | accepted | test_settings_phase2_part_3.py |
| TC-SET-6081 | P2 | Valid update FRONTEND_DIST_PATH = sample-value | key=FRONTEND_DIST_PATH,value='sample-value' | accepted | test_settings_phase2_part_3.py |
| TC-SET-6082 | P2 | Valid update FRONTEND_DIST_PATH = config-value | key=FRONTEND_DIST_PATH,value='config-value' | accepted | test_settings_phase2_part_3.py |
| TC-SET-6083 | P2 | Valid update FRONTEND_DIST_PATH = 192.168.0.1 | key=FRONTEND_DIST_PATH,value='192.168.0.1' | accepted | test_settings_phase2_part_3.py |
| TC-SET-6084 | P2 | Valid update FUZZY_MAX_DISTANCE = sample-value | key=FUZZY_MAX_DISTANCE,value='sample-value' | accepted | test_settings_phase2_part_3.py |
| TC-SET-6085 | P2 | Valid update FUZZY_MAX_DISTANCE = config-value | key=FUZZY_MAX_DISTANCE,value='config-value' | accepted | test_settings_phase2_part_3.py |
| TC-SET-6086 | P2 | Valid update FUZZY_MAX_DISTANCE = 192.168.0.1 | key=FUZZY_MAX_DISTANCE,value='192.168.0.1' | accepted | test_settings_phase2_part_3.py |
| TC-SET-6087 | P2 | Valid update HF_ENDPOINT = sample-value | key=HF_ENDPOINT,value='sample-value' | accepted | test_settings_phase2_part_3.py |
| TC-SET-6088 | P2 | Valid update HF_ENDPOINT = config-value | key=HF_ENDPOINT,value='config-value' | accepted | test_settings_phase2_part_3.py |
| TC-SET-6089 | P2 | Valid update HF_ENDPOINT = 192.168.0.1 | key=HF_ENDPOINT,value='192.168.0.1' | accepted | test_settings_phase2_part_3.py |
| TC-SET-6090 | P2 | Valid update HF_MIRROR = sample-value | key=HF_MIRROR,value='sample-value' | accepted | test_settings_phase2_part_3.py |
| TC-SET-6091 | P2 | Valid update HF_MIRROR = config-value | key=HF_MIRROR,value='config-value' | accepted | test_settings_phase2_part_3.py |
| TC-SET-6092 | P2 | Valid update HF_MIRROR = 192.168.0.1 | key=HF_MIRROR,value='192.168.0.1' | accepted | test_settings_phase2_part_3.py |
| TC-SET-6093 | P2 | Valid update LLM_RESPONSE_TIMEOUT_SECONDS = 25 | key=LLM_RESPONSE_TIMEOUT_SECONDS,value=25 | accepted | test_settings_phase2_part_3.py |
| TC-SET-6094 | P2 | Valid update LLM_RESPONSE_TIMEOUT_SECONDS = 50 | key=LLM_RESPONSE_TIMEOUT_SECONDS,value=50 | accepted | test_settings_phase2_part_3.py |
| TC-SET-6095 | P2 | Valid update LLM_RESPONSE_TIMEOUT_SECONDS = 100 | key=LLM_RESPONSE_TIMEOUT_SECONDS,value=100 | accepted | test_settings_phase2_part_3.py |
| TC-SET-6096 | P2 | Valid update LLM_RESPONSE_TIMEOUT_SECONDS = 250 | key=LLM_RESPONSE_TIMEOUT_SECONDS,value=250 | accepted | test_settings_phase2_part_3.py |
| TC-SET-6097 | P2 | Valid update LOG_BACKUP_COUNT = 25 | key=LOG_BACKUP_COUNT,value=25 | accepted | test_settings_phase2_part_3.py |
| TC-SET-6098 | P2 | Valid update LOG_BACKUP_COUNT = 50 | key=LOG_BACKUP_COUNT,value=50 | accepted | test_settings_phase2_part_3.py |
| TC-SET-6099 | P2 | Valid update LOG_BACKUP_COUNT = 100 | key=LOG_BACKUP_COUNT,value=100 | accepted | test_settings_phase2_part_3.py |
| TC-SET-6100 | P2 | Valid update LOG_FILE_PATH = sample-value | key=LOG_FILE_PATH,value='sample-value' | accepted | test_settings_phase2_part_3.py |
| TC-SET-6101 | P2 | Valid update LOG_FILE_PATH = config-value | key=LOG_FILE_PATH,value='config-value' | accepted | test_settings_phase2_part_3.py |
| TC-SET-6102 | P2 | Valid update LOG_FILE_PATH = 192.168.0.1 | key=LOG_FILE_PATH,value='192.168.0.1' | accepted | test_settings_phase2_part_3.py |
| TC-SET-6103 | P2 | Valid update LOG_LEVEL = sample-value | key=LOG_LEVEL,value='sample-value' | accepted | test_settings_phase2_part_3.py |
| TC-SET-6104 | P2 | Valid update LOG_LEVEL = config-value | key=LOG_LEVEL,value='config-value' | accepted | test_settings_phase2_part_3.py |
| TC-SET-6105 | P2 | Valid update LOG_LEVEL = 192.168.0.1 | key=LOG_LEVEL,value='192.168.0.1' | accepted | test_settings_phase2_part_3.py |
| TC-SET-6106 | P2 | Valid update LOG_RETENTION_DAYS = 25 | key=LOG_RETENTION_DAYS,value=25 | accepted | test_settings_phase2_part_3.py |
| TC-SET-6107 | P2 | Valid update LOG_RETENTION_DAYS = 50 | key=LOG_RETENTION_DAYS,value=50 | accepted | test_settings_phase2_part_3.py |
| TC-SET-6108 | P2 | Valid update LOG_RETENTION_DAYS = 100 | key=LOG_RETENTION_DAYS,value=100 | accepted | test_settings_phase2_part_3.py |
| TC-SET-6109 | P2 | Valid update LOG_RETENTION_DAYS = 250 | key=LOG_RETENTION_DAYS,value=250 | accepted | test_settings_phase2_part_3.py |
| TC-SET-6110 | P2 | Valid update MAX_BATCH_SIZE = 25 | key=MAX_BATCH_SIZE,value=25 | accepted | test_settings_phase2_part_3.py |
| TC-SET-6111 | P2 | Valid update MAX_BATCH_SIZE = 50 | key=MAX_BATCH_SIZE,value=50 | accepted | test_settings_phase2_part_3.py |
| TC-SET-6112 | P2 | Valid update MAX_BATCH_SIZE = 100 | key=MAX_BATCH_SIZE,value=100 | accepted | test_settings_phase2_part_3.py |
| TC-SET-6113 | P2 | Valid update MAX_BATCH_SIZE = 250 | key=MAX_BATCH_SIZE,value=250 | accepted | test_settings_phase2_part_3.py |
| TC-SET-6114 | P2 | Valid update MAX_BATCH_SIZE = 500 | key=MAX_BATCH_SIZE,value=500 | accepted | test_settings_phase2_part_3.py |
| TC-SET-6115 | P2 | Valid update METRICS_ENABLED = sample-value | key=METRICS_ENABLED,value='sample-value' | accepted | test_settings_phase2_part_3.py |
| TC-SET-6116 | P2 | Valid update METRICS_ENABLED = config-value | key=METRICS_ENABLED,value='config-value' | accepted | test_settings_phase2_part_3.py |
| TC-SET-6280 | P2 | Invalid update AI_TARGET_PERCENTAGE = -5 | key=AI_TARGET_PERCENTAGE,value=-5 | rejected | test_settings_phase2_part_4.py |
| TC-SET-6281 | P2 | Invalid update AI_TARGET_PERCENTAGE = -1 | key=AI_TARGET_PERCENTAGE,value=-1 | rejected | test_settings_phase2_part_4.py |
| TC-SET-6282 | P2 | Invalid update AI_TARGET_PERCENTAGE = 1000000000 | key=AI_TARGET_PERCENTAGE,value=1000000000 | rejected | test_settings_phase2_part_4.py |
| TC-SET-6283 | P2 | Invalid update AI_TARGET_PERCENTAGE = 'not-a-number' | key=AI_TARGET_PERCENTAGE,value='not-a-number' | rejected | test_settings_phase2_part_4.py |
| TC-SET-6284 | P2 | Invalid update ALLOWED_ORIGINS = '' | key=ALLOWED_ORIGINS,value='' | rejected | test_settings_phase2_part_4.py |
| TC-SET-6285 | P2 | Invalid update APP_CONFIG_DB_PATH = '' | key=APP_CONFIG_DB_PATH,value='' | rejected | test_settings_phase2_part_4.py |
| TC-SET-6286 | P2 | Invalid update APP_HOST = '' | key=APP_HOST,value='' | rejected | test_settings_phase2_part_4.py |
| TC-SET-6287 | P2 | Invalid update AUTO_TUNING_BATCH_HOUR = -5 | key=AUTO_TUNING_BATCH_HOUR,value=-5 | rejected | test_settings_phase2_part_4.py |
| TC-SET-6288 | P2 | Invalid update AUTO_TUNING_BATCH_HOUR = -1 | key=AUTO_TUNING_BATCH_HOUR,value=-1 | rejected | test_settings_phase2_part_4.py |
| TC-SET-6289 | P2 | Invalid update AUTO_TUNING_BATCH_HOUR = 1000000000 | key=AUTO_TUNING_BATCH_HOUR,value=1000000000 | rejected | test_settings_phase2_part_4.py |
| TC-SET-6290 | P2 | Invalid update AUTO_TUNING_BATCH_HOUR = 'not-a-number' | key=AUTO_TUNING_BATCH_HOUR,value='not-a-number' | rejected | test_settings_phase2_part_4.py |
| TC-SET-6291 | P2 | Invalid update AUTO_TUNING_ENABLED = 'maybe' | key=AUTO_TUNING_ENABLED,value='maybe' | rejected | test_settings_phase2_part_4.py |
| TC-SET-6292 | P2 | Invalid update AUTO_TUNING_ENABLED = 'bogus' | key=AUTO_TUNING_ENABLED,value='bogus' | rejected | test_settings_phase2_part_4.py |
| TC-SET-6293 | P2 | Invalid update AUTO_TUNING_ENABLED = 5 | key=AUTO_TUNING_ENABLED,value=5 | rejected | test_settings_phase2_part_4.py |
| TC-SET-6294 | P2 | Invalid update AUTO_TUNING_ENABLED = 'not-bool' | key=AUTO_TUNING_ENABLED,value='not-bool' | rejected | test_settings_phase2_part_4.py |
| TC-SET-6295 | P2 | Invalid update BLOOM_FILTER_CAPACITY = '' | key=BLOOM_FILTER_CAPACITY,value='' | rejected | test_settings_phase2_part_4.py |
| TC-SET-6296 | P2 | Invalid update BLOOM_FILTER_ERROR_RATE = '' | key=BLOOM_FILTER_ERROR_RATE,value='' | rejected | test_settings_phase2_part_4.py |
| TC-SET-6297 | P2 | Invalid update CACHE_MAX_SIZE = -5 | key=CACHE_MAX_SIZE,value=-5 | rejected | test_settings_phase2_part_4.py |
| TC-SET-6298 | P2 | Invalid update CACHE_MAX_SIZE = -1 | key=CACHE_MAX_SIZE,value=-1 | rejected | test_settings_phase2_part_4.py |
| TC-SET-6299 | P2 | Invalid update CACHE_MAX_SIZE = 0 | key=CACHE_MAX_SIZE,value=0 | rejected | test_settings_phase2_part_4.py |
| TC-SET-6300 | P2 | Invalid update CACHE_MAX_SIZE = 1000000000 | key=CACHE_MAX_SIZE,value=1000000000 | rejected | test_settings_phase2_part_4.py |
| TC-SET-6301 | P2 | Invalid update CACHE_MAX_SIZE = 'not-a-number' | key=CACHE_MAX_SIZE,value='not-a-number' | rejected | test_settings_phase2_part_4.py |
| TC-SET-6302 | P2 | Invalid update CACHE_TTL_SECONDS = -5 | key=CACHE_TTL_SECONDS,value=-5 | rejected | test_settings_phase2_part_4.py |
| TC-SET-6303 | P2 | Invalid update CACHE_TTL_SECONDS = -1 | key=CACHE_TTL_SECONDS,value=-1 | rejected | test_settings_phase2_part_4.py |
| TC-SET-6304 | P2 | Invalid update CACHE_TTL_SECONDS = 0 | key=CACHE_TTL_SECONDS,value=0 | rejected | test_settings_phase2_part_4.py |
| TC-SET-6305 | P2 | Invalid update CACHE_TTL_SECONDS = 1000000000 | key=CACHE_TTL_SECONDS,value=1000000000 | rejected | test_settings_phase2_part_4.py |
| TC-SET-6306 | P2 | Invalid update CACHE_TTL_SECONDS = 'not-a-number' | key=CACHE_TTL_SECONDS,value='not-a-number' | rejected | test_settings_phase2_part_4.py |
| TC-SET-6307 | P2 | Invalid update CUSTOM_WORDS_PATH = '' | key=CUSTOM_WORDS_PATH,value='' | rejected | test_settings_phase2_part_4.py |
| TC-SET-6308 | P2 | Invalid update CUSTOM_WORDS_STORAGE = '' | key=CUSTOM_WORDS_STORAGE,value='' | rejected | test_settings_phase2_part_4.py |
| TC-SET-6309 | P2 | Invalid update DETECTOR_THREAD_POOL_SIZE = -5 | key=DETECTOR_THREAD_POOL_SIZE,value=-5 | rejected | test_settings_phase2_part_4.py |
| TC-SET-6310 | P2 | Invalid update DETECTOR_THREAD_POOL_SIZE = -1 | key=DETECTOR_THREAD_POOL_SIZE,value=-1 | rejected | test_settings_phase2_part_4.py |
| TC-SET-6311 | P2 | Invalid update DETECTOR_THREAD_POOL_SIZE = 0 | key=DETECTOR_THREAD_POOL_SIZE,value=0 | rejected | test_settings_phase2_part_4.py |
| TC-SET-6312 | P2 | Invalid update DETECTOR_THREAD_POOL_SIZE = 1000000000 | key=DETECTOR_THREAD_POOL_SIZE,value=1000000000 | rejected | test_settings_phase2_part_4.py |
| TC-SET-6313 | P2 | Invalid update DETECTOR_THREAD_POOL_SIZE = 'not-a-number' | key=DETECTOR_THREAD_POOL_SIZE,value='not-a-number' | rejected | test_settings_phase2_part_4.py |
| TC-SET-6314 | P2 | Invalid update ENABLE_BADWORDS_PY = 'maybe' | key=ENABLE_BADWORDS_PY,value='maybe' | rejected | test_settings_phase2_part_4.py |
| TC-SET-6315 | P2 | Invalid update ENABLE_BADWORDS_PY = 'bogus' | key=ENABLE_BADWORDS_PY,value='bogus' | rejected | test_settings_phase2_part_4.py |
| TC-SET-6316 | P2 | Invalid update ENABLE_BADWORDS_PY = 5 | key=ENABLE_BADWORDS_PY,value=5 | rejected | test_settings_phase2_part_4.py |
| TC-SET-6317 | P2 | Invalid update ENABLE_BADWORDS_PY = 'not-bool' | key=ENABLE_BADWORDS_PY,value='not-bool' | rejected | test_settings_phase2_part_4.py |
| TC-SET-6318 | P2 | Invalid update ENABLE_GANGAJAL = 'maybe' | key=ENABLE_GANGAJAL,value='maybe' | rejected | test_settings_phase2_part_4.py |
| TC-SET-6319 | P2 | Invalid update ENABLE_GANGAJAL = 'bogus' | key=ENABLE_GANGAJAL,value='bogus' | rejected | test_settings_phase2_part_4.py |
| TC-SET-6320 | P2 | Invalid update ENABLE_GANGAJAL = 5 | key=ENABLE_GANGAJAL,value=5 | rejected | test_settings_phase2_part_4.py |
| TC-SET-6321 | P2 | Invalid update ENABLE_GANGAJAL = 'not-bool' | key=ENABLE_GANGAJAL,value='not-bool' | rejected | test_settings_phase2_part_4.py |
| TC-SET-6322 | P2 | Invalid update ENABLE_GLIN_PROFANITY = 'maybe' | key=ENABLE_GLIN_PROFANITY,value='maybe' | rejected | test_settings_phase2_part_4.py |
| TC-SET-6323 | P2 | Invalid update ENABLE_GLIN_PROFANITY = 'bogus' | key=ENABLE_GLIN_PROFANITY,value='bogus' | rejected | test_settings_phase2_part_4.py |
| TC-SET-6324 | P2 | Invalid update ENABLE_GLIN_PROFANITY = 5 | key=ENABLE_GLIN_PROFANITY,value=5 | rejected | test_settings_phase2_part_4.py |
| TC-SET-6325 | P2 | Invalid update ENABLE_GLIN_PROFANITY = 'not-bool' | key=ENABLE_GLIN_PROFANITY,value='not-bool' | rejected | test_settings_phase2_part_4.py |
| TC-SET-6326 | P2 | Invalid update ENABLE_PROFANITE = 'maybe' | key=ENABLE_PROFANITE,value='maybe' | rejected | test_settings_phase2_part_4.py |
| TC-SET-6327 | P2 | Invalid update ENABLE_PROFANITE = 'bogus' | key=ENABLE_PROFANITE,value='bogus' | rejected | test_settings_phase2_part_4.py |
| TC-SET-6328 | P2 | Invalid update ENABLE_PROFANITE = 5 | key=ENABLE_PROFANITE,value=5 | rejected | test_settings_phase2_part_4.py |
| TC-SET-6329 | P2 | Invalid update ENABLE_PROFANITE = 'not-bool' | key=ENABLE_PROFANITE,value='not-bool' | rejected | test_settings_phase2_part_4.py |
| TC-SET-6330 | P2 | Invalid update ENABLE_PROFANITY_FILTER = 'maybe' | key=ENABLE_PROFANITY_FILTER,value='maybe' | rejected | test_settings_phase2_part_4.py |
| TC-SET-6331 | P2 | Invalid update ENABLE_PROFANITY_FILTER = 'bogus' | key=ENABLE_PROFANITY_FILTER,value='bogus' | rejected | test_settings_phase2_part_4.py |
| TC-SET-6332 | P2 | Invalid update ENABLE_PROFANITY_FILTER = 5 | key=ENABLE_PROFANITY_FILTER,value=5 | rejected | test_settings_phase2_part_4.py |
| TC-SET-6333 | P2 | Invalid update ENABLE_PROFANITY_FILTER = 'not-bool' | key=ENABLE_PROFANITY_FILTER,value='not-bool' | rejected | test_settings_phase2_part_4.py |
| TC-SET-6334 | P2 | Invalid update ENABLE_PYPROFANE = 'maybe' | key=ENABLE_PYPROFANE,value='maybe' | rejected | test_settings_phase2_part_4.py |
| TC-SET-6335 | P2 | Invalid update ENABLE_PYPROFANE = 'bogus' | key=ENABLE_PYPROFANE,value='bogus' | rejected | test_settings_phase2_part_4.py |
| TC-SET-6336 | P2 | Invalid update ENABLE_PYPROFANE = 5 | key=ENABLE_PYPROFANE,value=5 | rejected | test_settings_phase2_part_4.py |
| TC-SET-6337 | P2 | Invalid update ENABLE_PYPROFANE = 'not-bool' | key=ENABLE_PYPROFANE,value='not-bool' | rejected | test_settings_phase2_part_4.py |
| TC-SET-6338 | P2 | Invalid update ENABLE_SAFETEXT = 'maybe' | key=ENABLE_SAFETEXT,value='maybe' | rejected | test_settings_phase2_part_4.py |
| TC-SET-6339 | P2 | Invalid update ENABLE_SAFETEXT = 'bogus' | key=ENABLE_SAFETEXT,value='bogus' | rejected | test_settings_phase2_part_4.py |
| TC-SET-6340 | P2 | Invalid update ENABLE_SAFETEXT = 5 | key=ENABLE_SAFETEXT,value=5 | rejected | test_settings_phase2_part_4.py |
| TC-SET-6341 | P2 | Invalid update ENABLE_SAFETEXT = 'not-bool' | key=ENABLE_SAFETEXT,value='not-bool' | rejected | test_settings_phase2_part_4.py |
| TC-SET-6342 | P2 | Invalid update ENABLE_SENSITIVE_STOP_WORDS = 'maybe' | key=ENABLE_SENSITIVE_STOP_WORDS,value='maybe' | rejected | test_settings_phase2_part_4.py |
| TC-SET-6343 | P2 | Invalid update ENABLE_SENSITIVE_STOP_WORDS = 'bogus' | key=ENABLE_SENSITIVE_STOP_WORDS,value='bogus' | rejected | test_settings_phase2_part_4.py |
| TC-SET-6344 | P2 | Invalid update ENABLE_SENSITIVE_STOP_WORDS = 5 | key=ENABLE_SENSITIVE_STOP_WORDS,value=5 | rejected | test_settings_phase2_part_4.py |
| TC-SET-6345 | P2 | Invalid update ENABLE_SENSITIVE_STOP_WORDS = 'not-bool' | key=ENABLE_SENSITIVE_STOP_WORDS,value='not-bool' | rejected | test_settings_phase2_part_4.py |
| TC-SET-6346 | P2 | Invalid update ENABLE_SENSITIVE_WORD_FILTER_CN = 'maybe' | key=ENABLE_SENSITIVE_WORD_FILTER_CN,value='maybe' | rejected | test_settings_phase2_part_4.py |
| TC-SET-6347 | P2 | Invalid update ENABLE_SENSITIVE_WORD_FILTER_CN = 'bogus' | key=ENABLE_SENSITIVE_WORD_FILTER_CN,value='bogus' | rejected | test_settings_phase2_part_4.py |
| TC-SET-6348 | P2 | Invalid update ENABLE_SENSITIVE_WORD_FILTER_CN = 5 | key=ENABLE_SENSITIVE_WORD_FILTER_CN,value=5 | rejected | test_settings_phase2_part_4.py |
| TC-SET-6349 | P2 | Invalid update ENABLE_SENSITIVE_WORD_FILTER_CN = 'not-bool' | key=ENABLE_SENSITIVE_WORD_FILTER_CN,value='not-bool' | rejected | test_settings_phase2_part_4.py |
| TC-SET-6350 | P2 | Invalid update EXPORT_RETENTION_DAYS = -5 | key=EXPORT_RETENTION_DAYS,value=-5 | rejected | test_settings_phase2_part_4.py |
| TC-SET-6351 | P2 | Invalid update EXPORT_RETENTION_DAYS = -1 | key=EXPORT_RETENTION_DAYS,value=-1 | rejected | test_settings_phase2_part_4.py |
| TC-SET-6352 | P2 | Invalid update EXPORT_RETENTION_DAYS = 0 | key=EXPORT_RETENTION_DAYS,value=0 | rejected | test_settings_phase2_part_4.py |
| TC-SET-6353 | P2 | Invalid update EXPORT_RETENTION_DAYS = 1000000000 | key=EXPORT_RETENTION_DAYS,value=1000000000 | rejected | test_settings_phase2_part_4.py |
| TC-SET-6354 | P2 | Invalid update EXPORT_RETENTION_DAYS = 'not-a-number' | key=EXPORT_RETENTION_DAYS,value='not-a-number' | rejected | test_settings_phase2_part_4.py |
| TC-SET-6355 | P2 | Invalid update FORCE_LLM_ON_SEMANTIC_HIGH = 'maybe' | key=FORCE_LLM_ON_SEMANTIC_HIGH,value='maybe' | rejected | test_settings_phase2_part_4.py |
| TC-SET-6356 | P2 | Invalid update FORCE_LLM_ON_SEMANTIC_HIGH = 'bogus' | key=FORCE_LLM_ON_SEMANTIC_HIGH,value='bogus' | rejected | test_settings_phase2_part_4.py |
| TC-SET-6357 | P2 | Invalid update FORCE_LLM_ON_SEMANTIC_HIGH = 5 | key=FORCE_LLM_ON_SEMANTIC_HIGH,value=5 | rejected | test_settings_phase2_part_4.py |
| TC-SET-6358 | P2 | Invalid update FORCE_LLM_ON_SEMANTIC_HIGH = 'not-bool' | key=FORCE_LLM_ON_SEMANTIC_HIGH,value='not-bool' | rejected | test_settings_phase2_part_4.py |
| TC-SET-6359 | P2 | Invalid update FORCE_LLM_ON_USER_RATIO_HIGH = 'maybe' | key=FORCE_LLM_ON_USER_RATIO_HIGH,value='maybe' | rejected | test_settings_phase2_part_4.py |
| TC-SET-6360 | P2 | Invalid update FORCE_LLM_ON_USER_RATIO_HIGH = 'bogus' | key=FORCE_LLM_ON_USER_RATIO_HIGH,value='bogus' | rejected | test_settings_phase2_part_4.py |
| TC-SET-6361 | P2 | Invalid update FORCE_LLM_ON_USER_RATIO_HIGH = 5 | key=FORCE_LLM_ON_USER_RATIO_HIGH,value=5 | rejected | test_settings_phase2_part_4.py |
| TC-SET-6362 | P2 | Invalid update FORCE_LLM_ON_USER_RATIO_HIGH = 'not-bool' | key=FORCE_LLM_ON_USER_RATIO_HIGH,value='not-bool' | rejected | test_settings_phase2_part_4.py |
| TC-SET-6363 | P2 | Invalid update FRONTEND_DIST_PATH = '' | key=FRONTEND_DIST_PATH,value='' | rejected | test_settings_phase2_part_4.py |
| TC-SET-6364 | P2 | Invalid update FUZZY_MAX_DISTANCE = '' | key=FUZZY_MAX_DISTANCE,value='' | rejected | test_settings_phase2_part_4.py |
| TC-SET-6365 | P2 | Invalid update HF_ENDPOINT = '' | key=HF_ENDPOINT,value='' | rejected | test_settings_phase2_part_4.py |
| TC-SET-6366 | P2 | Invalid update HF_MIRROR = '' | key=HF_MIRROR,value='' | rejected | test_settings_phase2_part_4.py |
| TC-SET-6367 | P2 | Invalid update LLM_RESPONSE_TIMEOUT_SECONDS = -5 | key=LLM_RESPONSE_TIMEOUT_SECONDS,value=-5 | rejected | test_settings_phase2_part_4.py |
| TC-SET-6368 | P2 | Invalid update LLM_RESPONSE_TIMEOUT_SECONDS = -1 | key=LLM_RESPONSE_TIMEOUT_SECONDS,value=-1 | rejected | test_settings_phase2_part_4.py |
| TC-SET-6369 | P2 | Invalid update LLM_RESPONSE_TIMEOUT_SECONDS = 0 | key=LLM_RESPONSE_TIMEOUT_SECONDS,value=0 | rejected | test_settings_phase2_part_4.py |
| TC-SET-6370 | P2 | Invalid update LLM_RESPONSE_TIMEOUT_SECONDS = 1000000000 | key=LLM_RESPONSE_TIMEOUT_SECONDS,value=1000000000 | rejected | test_settings_phase2_part_4.py |
| TC-SET-6371 | P2 | Invalid update LLM_RESPONSE_TIMEOUT_SECONDS = 'not-a-number' | key=LLM_RESPONSE_TIMEOUT_SECONDS,value='not-a-number' | rejected | test_settings_phase2_part_4.py |
| TC-SET-6372 | P2 | Invalid update LOG_BACKUP_COUNT = -5 | key=LOG_BACKUP_COUNT,value=-5 | rejected | test_settings_phase2_part_4.py |
| TC-SET-6373 | P2 | Invalid update LOG_BACKUP_COUNT = -1 | key=LOG_BACKUP_COUNT,value=-1 | rejected | test_settings_phase2_part_4.py |
| TC-SET-6374 | P2 | Invalid update LOG_BACKUP_COUNT = 1000000000 | key=LOG_BACKUP_COUNT,value=1000000000 | rejected | test_settings_phase2_part_4.py |
| TC-SET-6375 | P2 | Invalid update LOG_BACKUP_COUNT = 'not-a-number' | key=LOG_BACKUP_COUNT,value='not-a-number' | rejected | test_settings_phase2_part_4.py |
| TC-SET-6376 | P2 | Invalid update LOG_FILE_PATH = '' | key=LOG_FILE_PATH,value='' | rejected | test_settings_phase2_part_4.py |
| TC-SET-6377 | P2 | Invalid update LOG_LEVEL = '' | key=LOG_LEVEL,value='' | rejected | test_settings_phase2_part_4.py |
| TC-SET-6378 | P2 | Invalid update LOG_MAX_BYTES = -5 | key=LOG_MAX_BYTES,value=-5 | rejected | test_settings_phase2_part_4.py |
| TC-SET-6379 | P2 | Invalid update LOG_MAX_BYTES = -1 | key=LOG_MAX_BYTES,value=-1 | rejected | test_settings_phase2_part_4.py |
| TC-SET-6380 | P2 | Invalid update LOG_MAX_BYTES = 0 | key=LOG_MAX_BYTES,value=0 | rejected | test_settings_phase2_part_5.py |
| TC-SET-6381 | P2 | Invalid update LOG_MAX_BYTES = 'not-a-number' | key=LOG_MAX_BYTES,value='not-a-number' | rejected | test_settings_phase2_part_5.py |
| TC-SET-6382 | P2 | Invalid update LOG_MAX_BYTES = 2.5 | key=LOG_MAX_BYTES,value=2.5 | rejected | test_settings_phase2_part_5.py |
| TC-SET-6383 | P2 | Invalid update LOG_RETENTION_DAYS = -5 | key=LOG_RETENTION_DAYS,value=-5 | rejected | test_settings_phase2_part_5.py |
| TC-SET-6384 | P2 | Invalid update LOG_RETENTION_DAYS = -1 | key=LOG_RETENTION_DAYS,value=-1 | rejected | test_settings_phase2_part_5.py |
| TC-SET-6385 | P2 | Invalid update LOG_RETENTION_DAYS = 0 | key=LOG_RETENTION_DAYS,value=0 | rejected | test_settings_phase2_part_5.py |
| TC-SET-6386 | P2 | Invalid update LOG_RETENTION_DAYS = 1000000000 | key=LOG_RETENTION_DAYS,value=1000000000 | rejected | test_settings_phase2_part_5.py |
| TC-SET-6387 | P2 | Invalid update LOG_RETENTION_DAYS = 'not-a-number' | key=LOG_RETENTION_DAYS,value='not-a-number' | rejected | test_settings_phase2_part_5.py |
| TC-SET-6388 | P2 | Invalid update MAX_BATCH_SIZE = -5 | key=MAX_BATCH_SIZE,value=-5 | rejected | test_settings_phase2_part_5.py |
| TC-SET-6389 | P2 | Invalid update MAX_BATCH_SIZE = -1 | key=MAX_BATCH_SIZE,value=-1 | rejected | test_settings_phase2_part_5.py |
| TC-SET-6390 | P2 | Invalid update MAX_BATCH_SIZE = 0 | key=MAX_BATCH_SIZE,value=0 | rejected | test_settings_phase2_part_5.py |
| TC-SET-6391 | P2 | Invalid update MAX_BATCH_SIZE = 1000000000 | key=MAX_BATCH_SIZE,value=1000000000 | rejected | test_settings_phase2_part_5.py |
| TC-SET-6392 | P2 | Invalid update MAX_BATCH_SIZE = 'not-a-number' | key=MAX_BATCH_SIZE,value='not-a-number' | rejected | test_settings_phase2_part_5.py |
| TC-SET-6393 | P2 | Invalid update METRICS_ENABLED = '' | key=METRICS_ENABLED,value='' | rejected | test_settings_phase2_part_5.py |
| TC-SET-6394 | P2 | Invalid update METRICS_PORT = '' | key=METRICS_PORT,value='' | rejected | test_settings_phase2_part_5.py |
| TC-SET-6395 | P2 | Invalid update MODELSCOPE_ENDPOINT = '' | key=MODELSCOPE_ENDPOINT,value='' | rejected | test_settings_phase2_part_5.py |
| TC-SET-6396 | P2 | Invalid update MODEL_BATCH_SIZE = -5 | key=MODEL_BATCH_SIZE,value=-5 | rejected | test_settings_phase2_part_5.py |
| TC-SET-6397 | P2 | Invalid update MODEL_BATCH_SIZE = -1 | key=MODEL_BATCH_SIZE,value=-1 | rejected | test_settings_phase2_part_5.py |
| TC-SET-6398 | P2 | Invalid update MODEL_BATCH_SIZE = 0 | key=MODEL_BATCH_SIZE,value=0 | rejected | test_settings_phase2_part_5.py |
| TC-SET-6399 | P2 | Invalid update MODEL_BATCH_SIZE = 1000000000 | key=MODEL_BATCH_SIZE,value=1000000000 | rejected | test_settings_phase2_part_5.py |
| TC-SET-6400 | P2 | Invalid update MODEL_BATCH_SIZE = 'not-a-number' | key=MODEL_BATCH_SIZE,value='not-a-number' | rejected | test_settings_phase2_part_5.py |
| TC-SET-6401 | P2 | Invalid update MODEL_BATCH_SIZE = 2.5 | key=MODEL_BATCH_SIZE,value=2.5 | rejected | test_settings_phase2_part_5.py |
| TC-SET-6402 | P2 | Invalid update MODEL_CACHE_TYPE_K = '' | key=MODEL_CACHE_TYPE_K,value='' | rejected | test_settings_phase2_part_5.py |
| TC-SET-6403 | P2 | Invalid update MODEL_CACHE_TYPE_V = '' | key=MODEL_CACHE_TYPE_V,value='' | rejected | test_settings_phase2_part_5.py |
| TC-SET-6404 | P2 | Invalid update MODEL_CONTEXT_SIZE = -5 | key=MODEL_CONTEXT_SIZE,value=-5 | rejected | test_settings_phase2_part_5.py |
| TC-SET-6405 | P2 | Invalid update MODEL_CONTEXT_SIZE = -1 | key=MODEL_CONTEXT_SIZE,value=-1 | rejected | test_settings_phase2_part_5.py |
| TC-SET-6406 | P2 | Invalid update MODEL_CONTEXT_SIZE = 0 | key=MODEL_CONTEXT_SIZE,value=0 | rejected | test_settings_phase2_part_5.py |
| TC-SET-6407 | P2 | Invalid update MODEL_CONTEXT_SIZE = 1000000000 | key=MODEL_CONTEXT_SIZE,value=1000000000 | rejected | test_settings_phase2_part_5.py |
| TC-SET-6408 | P2 | Invalid update MODEL_CONTEXT_SIZE = 'not-a-number' | key=MODEL_CONTEXT_SIZE,value='not-a-number' | rejected | test_settings_phase2_part_5.py |
| TC-SET-6409 | P2 | Invalid update MODEL_CONTEXT_SIZE = 2.5 | key=MODEL_CONTEXT_SIZE,value=2.5 | rejected | test_settings_phase2_part_5.py |
| TC-SET-6410 | P2 | Invalid update MODEL_DIR = '' | key=MODEL_DIR,value='' | rejected | test_settings_phase2_part_5.py |
| TC-SET-6411 | P2 | Invalid update MODEL_FALLBACK_REPO = '' | key=MODEL_FALLBACK_REPO,value='' | rejected | test_settings_phase2_part_5.py |
| TC-SET-6412 | P2 | Invalid update MODEL_FILENAME = '' | key=MODEL_FILENAME,value='' | rejected | test_settings_phase2_part_5.py |
| TC-SET-6413 | P2 | Invalid update MODEL_FLASH_ATTN = 'maybe' | key=MODEL_FLASH_ATTN,value='maybe' | rejected | test_settings_phase2_part_5.py |
| TC-SET-6414 | P2 | Invalid update MODEL_FLASH_ATTN = 'bogus' | key=MODEL_FLASH_ATTN,value='bogus' | rejected | test_settings_phase2_part_5.py |
| TC-SET-6415 | P2 | Invalid update MODEL_FLASH_ATTN = 5 | key=MODEL_FLASH_ATTN,value=5 | rejected | test_settings_phase2_part_5.py |
| TC-SET-6416 | P2 | Invalid update MODEL_FLASH_ATTN = 'not-bool' | key=MODEL_FLASH_ATTN,value='not-bool' | rejected | test_settings_phase2_part_5.py |
| TC-SET-6417 | P2 | Invalid update MODEL_IDLE_TIMEOUT_SECONDS = -5 | key=MODEL_IDLE_TIMEOUT_SECONDS,value=-5 | rejected | test_settings_phase2_part_5.py |
| TC-SET-6418 | P2 | Invalid update MODEL_IDLE_TIMEOUT_SECONDS = -1 | key=MODEL_IDLE_TIMEOUT_SECONDS,value=-1 | rejected | test_settings_phase2_part_5.py |
| TC-SET-6419 | P2 | Invalid update MODEL_IDLE_TIMEOUT_SECONDS = 0 | key=MODEL_IDLE_TIMEOUT_SECONDS,value=0 | rejected | test_settings_phase2_part_5.py |
| TC-SET-6420 | P2 | Invalid update MODEL_IDLE_TIMEOUT_SECONDS = 1000000000 | key=MODEL_IDLE_TIMEOUT_SECONDS,value=1000000000 | rejected | test_settings_phase2_part_5.py |
| TC-SET-6421 | P2 | Invalid update MODEL_IDLE_TIMEOUT_SECONDS = 'not-a-number' | key=MODEL_IDLE_TIMEOUT_SECONDS,value='not-a-number' | rejected | test_settings_phase2_part_5.py |
| TC-SET-6422 | P2 | Invalid update MODEL_IDLE_TIMEOUT_SECONDS = 2.5 | key=MODEL_IDLE_TIMEOUT_SECONDS,value=2.5 | rejected | test_settings_phase2_part_5.py |
| TC-SET-6423 | P2 | Invalid update MODEL_MAX_TOKENS = -5 | key=MODEL_MAX_TOKENS,value=-5 | rejected | test_settings_phase2_part_5.py |
| TC-SET-6424 | P2 | Invalid update MODEL_MAX_TOKENS = -1 | key=MODEL_MAX_TOKENS,value=-1 | rejected | test_settings_phase2_part_5.py |
| TC-SET-6425 | P2 | Invalid update MODEL_MAX_TOKENS = 0 | key=MODEL_MAX_TOKENS,value=0 | rejected | test_settings_phase2_part_5.py |
| TC-SET-6426 | P2 | Invalid update MODEL_MAX_TOKENS = 1000000000 | key=MODEL_MAX_TOKENS,value=1000000000 | rejected | test_settings_phase2_part_5.py |
| TC-SET-6427 | P2 | Invalid update MODEL_MAX_TOKENS = 'not-a-number' | key=MODEL_MAX_TOKENS,value='not-a-number' | rejected | test_settings_phase2_part_5.py |
| TC-SET-6428 | P2 | Invalid update MODEL_MLOCK = 'maybe' | key=MODEL_MLOCK,value='maybe' | rejected | test_settings_phase2_part_5.py |
| TC-SET-6429 | P2 | Invalid update MODEL_MLOCK = 'bogus' | key=MODEL_MLOCK,value='bogus' | rejected | test_settings_phase2_part_5.py |
| TC-SET-6589 | P2 | Coercion SAFE_WORD_ENABLED 'true' #0 | key=SAFE_WORD_ENABLED,raw=true | coerced=True | test_settings_phase2_part_5.py |
| TC-SET-6590 | P2 | Coercion SAFE_WORD_ENABLED 'true' #1 | key=SAFE_WORD_ENABLED,raw=true | coerced=True | test_settings_phase2_part_5.py |
| TC-SET-6591 | P2 | Coercion SAFE_WORD_ENABLED 'true' #2 | key=SAFE_WORD_ENABLED,raw=true | coerced=True | test_settings_phase2_part_5.py |
| TC-SET-6592 | P2 | Coercion SAFE_WORD_ENABLED 'true' #3 | key=SAFE_WORD_ENABLED,raw=true | coerced=True | test_settings_phase2_part_5.py |
| TC-SET-6593 | P2 | Coercion SAFE_WORD_ENABLED 'true' #4 | key=SAFE_WORD_ENABLED,raw=true | coerced=True | test_settings_phase2_part_5.py |
| TC-SET-6594 | P2 | Coercion SAFE_WORD_ENABLED 'true' #5 | key=SAFE_WORD_ENABLED,raw=true | coerced=True | test_settings_phase2_part_5.py |
| TC-SET-6595 | P2 | Coercion SAFE_WORD_ENABLED 'true' #6 | key=SAFE_WORD_ENABLED,raw=true | coerced=True | test_settings_phase2_part_5.py |
| TC-SET-6596 | P2 | Coercion SAFE_WORD_ENABLED 'true' #7 | key=SAFE_WORD_ENABLED,raw=true | coerced=True | test_settings_phase2_part_5.py |
| TC-SET-6597 | P2 | Coercion SAFE_WORD_ENABLED 'true' #8 | key=SAFE_WORD_ENABLED,raw=true | coerced=True | test_settings_phase2_part_5.py |
| TC-SET-6598 | P2 | Coercion SAFE_WORD_ENABLED 'true' #9 | key=SAFE_WORD_ENABLED,raw=true | coerced=True | test_settings_phase2_part_5.py |
| TC-SET-6599 | P2 | Coercion SAFE_WORD_ENABLED '1' #0 | key=SAFE_WORD_ENABLED,raw=1 | coerced=True | test_settings_phase2_part_5.py |
| TC-SET-6600 | P2 | Coercion SAFE_WORD_ENABLED '1' #1 | key=SAFE_WORD_ENABLED,raw=1 | coerced=True | test_settings_phase2_part_5.py |
| TC-SET-6601 | P2 | Coercion SAFE_WORD_ENABLED '1' #2 | key=SAFE_WORD_ENABLED,raw=1 | coerced=True | test_settings_phase2_part_5.py |
| TC-SET-6602 | P2 | Coercion SAFE_WORD_ENABLED '1' #3 | key=SAFE_WORD_ENABLED,raw=1 | coerced=True | test_settings_phase2_part_5.py |
| TC-SET-6603 | P2 | Coercion SAFE_WORD_ENABLED '1' #4 | key=SAFE_WORD_ENABLED,raw=1 | coerced=True | test_settings_phase2_part_5.py |
| TC-SET-6604 | P2 | Coercion SAFE_WORD_ENABLED '1' #5 | key=SAFE_WORD_ENABLED,raw=1 | coerced=True | test_settings_phase2_part_5.py |
| TC-SET-6605 | P2 | Coercion SAFE_WORD_ENABLED '1' #6 | key=SAFE_WORD_ENABLED,raw=1 | coerced=True | test_settings_phase2_part_5.py |
| TC-SET-6606 | P2 | Coercion SAFE_WORD_ENABLED '1' #7 | key=SAFE_WORD_ENABLED,raw=1 | coerced=True | test_settings_phase2_part_5.py |
| TC-SET-6607 | P2 | Coercion SAFE_WORD_ENABLED '1' #8 | key=SAFE_WORD_ENABLED,raw=1 | coerced=True | test_settings_phase2_part_5.py |
| TC-SET-6608 | P2 | Coercion SAFE_WORD_ENABLED '1' #9 | key=SAFE_WORD_ENABLED,raw=1 | coerced=True | test_settings_phase2_part_5.py |
| TC-SET-6609 | P2 | Coercion SAFE_WORD_ENABLED 'yes' #0 | key=SAFE_WORD_ENABLED,raw=yes | coerced=True | test_settings_phase2_part_5.py |
| TC-SET-6610 | P2 | Coercion SAFE_WORD_ENABLED 'yes' #1 | key=SAFE_WORD_ENABLED,raw=yes | coerced=True | test_settings_phase2_part_5.py |
| TC-SET-6611 | P2 | Coercion SAFE_WORD_ENABLED 'yes' #2 | key=SAFE_WORD_ENABLED,raw=yes | coerced=True | test_settings_phase2_part_5.py |
| TC-SET-6612 | P2 | Coercion SAFE_WORD_ENABLED 'yes' #3 | key=SAFE_WORD_ENABLED,raw=yes | coerced=True | test_settings_phase2_part_5.py |
| TC-SET-6613 | P2 | Coercion SAFE_WORD_ENABLED 'yes' #4 | key=SAFE_WORD_ENABLED,raw=yes | coerced=True | test_settings_phase2_part_5.py |
| TC-SET-6614 | P2 | Coercion SAFE_WORD_ENABLED 'yes' #5 | key=SAFE_WORD_ENABLED,raw=yes | coerced=True | test_settings_phase2_part_5.py |
| TC-SET-6615 | P2 | Coercion SAFE_WORD_ENABLED 'yes' #6 | key=SAFE_WORD_ENABLED,raw=yes | coerced=True | test_settings_phase2_part_5.py |
| TC-SET-6616 | P2 | Coercion SAFE_WORD_ENABLED 'yes' #7 | key=SAFE_WORD_ENABLED,raw=yes | coerced=True | test_settings_phase2_part_5.py |
| TC-SET-6617 | P2 | Coercion SAFE_WORD_ENABLED 'yes' #8 | key=SAFE_WORD_ENABLED,raw=yes | coerced=True | test_settings_phase2_part_5.py |
| TC-SET-6618 | P2 | Coercion SAFE_WORD_ENABLED 'yes' #9 | key=SAFE_WORD_ENABLED,raw=yes | coerced=True | test_settings_phase2_part_5.py |
| TC-SET-6619 | P2 | Coercion SAFE_WORD_ENABLED 'false' #0 | key=SAFE_WORD_ENABLED,raw=false | coerced=False | test_settings_phase2_part_5.py |
| TC-SET-6620 | P2 | Coercion SAFE_WORD_ENABLED 'false' #1 | key=SAFE_WORD_ENABLED,raw=false | coerced=False | test_settings_phase2_part_5.py |
| TC-SET-6621 | P2 | Coercion SAFE_WORD_ENABLED 'false' #2 | key=SAFE_WORD_ENABLED,raw=false | coerced=False | test_settings_phase2_part_5.py |
| TC-SET-6622 | P2 | Coercion SAFE_WORD_ENABLED 'false' #3 | key=SAFE_WORD_ENABLED,raw=false | coerced=False | test_settings_phase2_part_5.py |
| TC-SET-6623 | P2 | Coercion SAFE_WORD_ENABLED 'false' #4 | key=SAFE_WORD_ENABLED,raw=false | coerced=False | test_settings_phase2_part_5.py |
| TC-SET-6624 | P2 | Coercion SAFE_WORD_ENABLED 'false' #5 | key=SAFE_WORD_ENABLED,raw=false | coerced=False | test_settings_phase2_part_5.py |
| TC-SET-6625 | P2 | Coercion SAFE_WORD_ENABLED 'false' #6 | key=SAFE_WORD_ENABLED,raw=false | coerced=False | test_settings_phase2_part_5.py |
| TC-SET-6626 | P2 | Coercion SAFE_WORD_ENABLED 'false' #7 | key=SAFE_WORD_ENABLED,raw=false | coerced=False | test_settings_phase2_part_5.py |
| TC-SET-6627 | P2 | Coercion SAFE_WORD_ENABLED 'false' #8 | key=SAFE_WORD_ENABLED,raw=false | coerced=False | test_settings_phase2_part_5.py |
| TC-SET-6628 | P2 | Coercion SAFE_WORD_ENABLED 'false' #9 | key=SAFE_WORD_ENABLED,raw=false | coerced=False | test_settings_phase2_part_5.py |
| TC-SET-6629 | P2 | Coercion SAFE_WORD_ENABLED '0' #0 | key=SAFE_WORD_ENABLED,raw=0 | coerced=False | test_settings_phase2_part_5.py |
| TC-SET-6630 | P2 | Coercion SAFE_WORD_ENABLED '0' #1 | key=SAFE_WORD_ENABLED,raw=0 | coerced=False | test_settings_phase2_part_5.py |
| TC-SET-6631 | P2 | Coercion SAFE_WORD_ENABLED '0' #2 | key=SAFE_WORD_ENABLED,raw=0 | coerced=False | test_settings_phase2_part_5.py |
| TC-SET-6632 | P2 | Coercion SAFE_WORD_ENABLED '0' #3 | key=SAFE_WORD_ENABLED,raw=0 | coerced=False | test_settings_phase2_part_5.py |
| TC-SET-6633 | P2 | Coercion SAFE_WORD_ENABLED '0' #4 | key=SAFE_WORD_ENABLED,raw=0 | coerced=False | test_settings_phase2_part_5.py |
| TC-SET-6634 | P2 | Coercion SAFE_WORD_ENABLED '0' #5 | key=SAFE_WORD_ENABLED,raw=0 | coerced=False | test_settings_phase2_part_5.py |
| TC-SET-6635 | P2 | Coercion SAFE_WORD_ENABLED '0' #6 | key=SAFE_WORD_ENABLED,raw=0 | coerced=False | test_settings_phase2_part_5.py |
| TC-SET-6636 | P2 | Coercion SAFE_WORD_ENABLED '0' #7 | key=SAFE_WORD_ENABLED,raw=0 | coerced=False | test_settings_phase2_part_5.py |
| TC-SET-6637 | P2 | Coercion SAFE_WORD_ENABLED '0' #8 | key=SAFE_WORD_ENABLED,raw=0 | coerced=False | test_settings_phase2_part_5.py |
| TC-SET-6638 | P2 | Coercion SAFE_WORD_ENABLED '0' #9 | key=SAFE_WORD_ENABLED,raw=0 | coerced=False | test_settings_phase2_part_5.py |
| TC-SET-6639 | P2 | Coercion SAFE_WORD_ENABLED 'no' #0 | key=SAFE_WORD_ENABLED,raw=no | coerced=False | test_settings_phase2_part_6.py |
| TC-SET-6640 | P2 | Coercion SAFE_WORD_ENABLED 'no' #1 | key=SAFE_WORD_ENABLED,raw=no | coerced=False | test_settings_phase2_part_6.py |
| TC-SET-6641 | P2 | Coercion SAFE_WORD_ENABLED 'no' #2 | key=SAFE_WORD_ENABLED,raw=no | coerced=False | test_settings_phase2_part_6.py |
| TC-SET-6642 | P2 | Coercion SAFE_WORD_ENABLED 'no' #3 | key=SAFE_WORD_ENABLED,raw=no | coerced=False | test_settings_phase2_part_6.py |
| TC-SET-6643 | P2 | Coercion SAFE_WORD_ENABLED 'no' #4 | key=SAFE_WORD_ENABLED,raw=no | coerced=False | test_settings_phase2_part_6.py |
| TC-SET-6644 | P2 | Coercion SAFE_WORD_ENABLED 'no' #5 | key=SAFE_WORD_ENABLED,raw=no | coerced=False | test_settings_phase2_part_6.py |
| TC-SET-6645 | P2 | Coercion SAFE_WORD_ENABLED 'no' #6 | key=SAFE_WORD_ENABLED,raw=no | coerced=False | test_settings_phase2_part_6.py |
| TC-SET-6646 | P2 | Coercion SAFE_WORD_ENABLED 'no' #7 | key=SAFE_WORD_ENABLED,raw=no | coerced=False | test_settings_phase2_part_6.py |
| TC-SET-6647 | P2 | Coercion SAFE_WORD_ENABLED 'no' #8 | key=SAFE_WORD_ENABLED,raw=no | coerced=False | test_settings_phase2_part_6.py |
| TC-SET-6648 | P2 | Coercion SAFE_WORD_ENABLED 'no' #9 | key=SAFE_WORD_ENABLED,raw=no | coerced=False | test_settings_phase2_part_6.py |
| TC-SET-6649 | P2 | Coercion USER_WINDOW_DAYS '91' #0 | key=USER_WINDOW_DAYS,raw=91 | coerced=91 | test_settings_phase2_part_6.py |
| TC-SET-6650 | P2 | Coercion USER_WINDOW_DAYS '91' #1 | key=USER_WINDOW_DAYS,raw=91 | coerced=91 | test_settings_phase2_part_6.py |
| TC-SET-6651 | P2 | Coercion USER_WINDOW_DAYS '91' #2 | key=USER_WINDOW_DAYS,raw=91 | coerced=91 | test_settings_phase2_part_6.py |
| TC-SET-6652 | P2 | Coercion USER_WINDOW_DAYS '91' #3 | key=USER_WINDOW_DAYS,raw=91 | coerced=91 | test_settings_phase2_part_6.py |
| TC-SET-6653 | P2 | Coercion USER_WINDOW_DAYS '91' #4 | key=USER_WINDOW_DAYS,raw=91 | coerced=91 | test_settings_phase2_part_6.py |
| TC-SET-6654 | P2 | Coercion USER_WINDOW_DAYS '91' #5 | key=USER_WINDOW_DAYS,raw=91 | coerced=91 | test_settings_phase2_part_6.py |
| TC-SET-6655 | P2 | Coercion USER_WINDOW_DAYS '91' #6 | key=USER_WINDOW_DAYS,raw=91 | coerced=91 | test_settings_phase2_part_6.py |
| TC-SET-6656 | P2 | Coercion USER_WINDOW_DAYS '91' #7 | key=USER_WINDOW_DAYS,raw=91 | coerced=91 | test_settings_phase2_part_6.py |
| TC-SET-6657 | P2 | Coercion USER_WINDOW_DAYS '91' #8 | key=USER_WINDOW_DAYS,raw=91 | coerced=91 | test_settings_phase2_part_6.py |
| TC-SET-6658 | P2 | Coercion USER_WINDOW_DAYS '91' #9 | key=USER_WINDOW_DAYS,raw=91 | coerced=91 | test_settings_phase2_part_6.py |
| TC-SET-6659 | P2 | Coercion CACHE_MAX_SIZE '500' #0 | key=CACHE_MAX_SIZE,raw=500 | coerced=500 | test_settings_phase2_part_6.py |
| TC-SET-6660 | P2 | Coercion CACHE_MAX_SIZE '500' #1 | key=CACHE_MAX_SIZE,raw=500 | coerced=500 | test_settings_phase2_part_6.py |
| TC-SET-6661 | P2 | Coercion CACHE_MAX_SIZE '500' #2 | key=CACHE_MAX_SIZE,raw=500 | coerced=500 | test_settings_phase2_part_6.py |
| TC-SET-6662 | P2 | Coercion CACHE_MAX_SIZE '500' #3 | key=CACHE_MAX_SIZE,raw=500 | coerced=500 | test_settings_phase2_part_6.py |
| TC-SET-6663 | P2 | Coercion CACHE_MAX_SIZE '500' #4 | key=CACHE_MAX_SIZE,raw=500 | coerced=500 | test_settings_phase2_part_6.py |
| TC-SET-6664 | P2 | Coercion CACHE_MAX_SIZE '500' #5 | key=CACHE_MAX_SIZE,raw=500 | coerced=500 | test_settings_phase2_part_6.py |
| TC-SET-6665 | P2 | Coercion CACHE_MAX_SIZE '500' #6 | key=CACHE_MAX_SIZE,raw=500 | coerced=500 | test_settings_phase2_part_6.py |
| TC-SET-6666 | P2 | Coercion CACHE_MAX_SIZE '500' #7 | key=CACHE_MAX_SIZE,raw=500 | coerced=500 | test_settings_phase2_part_6.py |
| TC-SET-6667 | P2 | Coercion CACHE_MAX_SIZE '500' #8 | key=CACHE_MAX_SIZE,raw=500 | coerced=500 | test_settings_phase2_part_6.py |
| TC-SET-6668 | P2 | Coercion CACHE_MAX_SIZE '500' #9 | key=CACHE_MAX_SIZE,raw=500 | coerced=500 | test_settings_phase2_part_6.py |
| TC-SET-6669 | P2 | Coercion MODEL_MAX_TOKENS '64' #0 | key=MODEL_MAX_TOKENS,raw=64 | coerced=64 | test_settings_phase2_part_6.py |
| TC-SET-6670 | P2 | Coercion MODEL_MAX_TOKENS '64' #1 | key=MODEL_MAX_TOKENS,raw=64 | coerced=64 | test_settings_phase2_part_6.py |
| TC-SET-6671 | P2 | Coercion MODEL_MAX_TOKENS '64' #2 | key=MODEL_MAX_TOKENS,raw=64 | coerced=64 | test_settings_phase2_part_6.py |
| TC-SET-6672 | P2 | Coercion MODEL_MAX_TOKENS '64' #3 | key=MODEL_MAX_TOKENS,raw=64 | coerced=64 | test_settings_phase2_part_6.py |
| TC-SET-6673 | P2 | Coercion MODEL_MAX_TOKENS '64' #4 | key=MODEL_MAX_TOKENS,raw=64 | coerced=64 | test_settings_phase2_part_6.py |
| TC-SET-6674 | P2 | Coercion MODEL_MAX_TOKENS '64' #5 | key=MODEL_MAX_TOKENS,raw=64 | coerced=64 | test_settings_phase2_part_6.py |
| TC-SET-6675 | P2 | Coercion MODEL_MAX_TOKENS '64' #6 | key=MODEL_MAX_TOKENS,raw=64 | coerced=64 | test_settings_phase2_part_6.py |
| TC-SET-6676 | P2 | Coercion MODEL_MAX_TOKENS '64' #7 | key=MODEL_MAX_TOKENS,raw=64 | coerced=64 | test_settings_phase2_part_6.py |
| TC-SET-6677 | P2 | Coercion MODEL_MAX_TOKENS '64' #8 | key=MODEL_MAX_TOKENS,raw=64 | coerced=64 | test_settings_phase2_part_6.py |
| TC-SET-6678 | P2 | Coercion MODEL_MAX_TOKENS '64' #9 | key=MODEL_MAX_TOKENS,raw=64 | coerced=64 | test_settings_phase2_part_6.py |
| TC-SET-6679 | P2 | Coercion SEMANTIC_SIMILARITY_THRESHOLD '0.9' #0 | key=SEMANTIC_SIMILARITY_THRESHOLD,raw=0.9 | coerced=0.9 | test_settings_phase2_part_6.py |
| TC-SET-6680 | P2 | Coercion SEMANTIC_SIMILARITY_THRESHOLD '0.9' #1 | key=SEMANTIC_SIMILARITY_THRESHOLD,raw=0.9 | coerced=0.9 | test_settings_phase2_part_6.py |
| TC-SET-6681 | P2 | Coercion SEMANTIC_SIMILARITY_THRESHOLD '0.9' #2 | key=SEMANTIC_SIMILARITY_THRESHOLD,raw=0.9 | coerced=0.9 | test_settings_phase2_part_6.py |
| TC-SET-6682 | P2 | Coercion SEMANTIC_SIMILARITY_THRESHOLD '0.9' #3 | key=SEMANTIC_SIMILARITY_THRESHOLD,raw=0.9 | coerced=0.9 | test_settings_phase2_part_6.py |
| TC-SET-6683 | P2 | Coercion SEMANTIC_SIMILARITY_THRESHOLD '0.9' #4 | key=SEMANTIC_SIMILARITY_THRESHOLD,raw=0.9 | coerced=0.9 | test_settings_phase2_part_6.py |
| TC-SET-6684 | P2 | Coercion SEMANTIC_SIMILARITY_THRESHOLD '0.9' #5 | key=SEMANTIC_SIMILARITY_THRESHOLD,raw=0.9 | coerced=0.9 | test_settings_phase2_part_6.py |
| TC-SET-6685 | P2 | Coercion SEMANTIC_SIMILARITY_THRESHOLD '0.9' #6 | key=SEMANTIC_SIMILARITY_THRESHOLD,raw=0.9 | coerced=0.9 | test_settings_phase2_part_6.py |
| TC-SET-6686 | P2 | Coercion SEMANTIC_SIMILARITY_THRESHOLD '0.9' #7 | key=SEMANTIC_SIMILARITY_THRESHOLD,raw=0.9 | coerced=0.9 | test_settings_phase2_part_6.py |
| TC-SET-6687 | P2 | Coercion SEMANTIC_SIMILARITY_THRESHOLD '0.9' #8 | key=SEMANTIC_SIMILARITY_THRESHOLD,raw=0.9 | coerced=0.9 | test_settings_phase2_part_6.py |
| TC-SET-6688 | P2 | Coercion SEMANTIC_SIMILARITY_THRESHOLD '0.9' #9 | key=SEMANTIC_SIMILARITY_THRESHOLD,raw=0.9 | coerced=0.9 | test_settings_phase2_part_6.py |

### Phase 3 - 10,000 cases
- Planned sweeps over the full dimension matrix, IDs TC-SET-0611 onward.

### Phase 4 - 100,000 cases
- Planned high-scale scenarios, IDs TC-SET-10611 onward.

### Phase 5 - 789,390 cases
- Planned exhaustive dimension sweep, IDs TC-SET-110611 onward.

## Implementation Status
| File | Test Cases | Priority | Status |
| :--- | :--- | :--- | :--- |
| test_settings_phase2_part_1.py | 5563-5662 | P1 | :white_check_mark: Phase 2 |
| test_settings_phase2_part_2.py | 5663-6016 | P1 | :white_check_mark: Phase 2 |
| test_settings_phase2_part_3.py | 6017-6116 | P2 | :white_check_mark: Phase 2 |
| test_settings_phase2_part_4.py | 6280-6379 | P2 | :white_check_mark: Phase 2 |
| test_settings_phase2_part_5.py | 6380-6638 | P2 | :white_check_mark: Phase 2 |
| test_settings_phase2_part_6.py | 6639-6688 | P2 | :white_check_mark: Phase 2 |

## Adding New Test Cases (Step-by-Step)

1. Determine the target phase and priority (P0-P3).
2. Confirm the dimension combination is not already in the matrix above.
3. Create `test_<module>_phase2_part_<N>.py` (max 100 cases per file).
4. Follow the golden-master pattern: compute expectations with the real
   application (see `tests/tools/phase2_generator.py`) or assert stable
   properties; use `BaseTest` helpers and the conftest fixtures.
5. Update this README (new row in the Phase 2 table + status table).
6. Run: `uv run python -m pytest tests/<module>/ -v`
7. Commit one file per commit: `[TEST-<TYPE>] Add <module> tests part <N>`.

## Related Documentation
- Configuration
- Settings API
