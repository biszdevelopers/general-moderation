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
| TC-SET-5611 | P1 | Describe field key for CRITICAL_PHRASES_DB_PATH | key=CRITICAL_PHRASES_DB_PATH,field=key | present | test_settings_phase2_part_1.py |
| TC-SET-5612 | P1 | Describe field value for CRITICAL_PHRASES_DB_PATH | key=CRITICAL_PHRASES_DB_PATH,field=value | present | test_settings_phase2_part_1.py |
| TC-SET-5613 | P1 | Describe field type for CRITICAL_PHRASES_DB_PATH | key=CRITICAL_PHRASES_DB_PATH,field=type | present | test_settings_phase2_part_1.py |
| TC-SET-5614 | P1 | Describe field editable for CRITICAL_PHRASES_DB_PATH | key=CRITICAL_PHRASES_DB_PATH,field=editable | present | test_settings_phase2_part_1.py |
| TC-SET-5615 | P1 | Describe field key for CUSTOM_WORDS_PATH | key=CUSTOM_WORDS_PATH,field=key | present | test_settings_phase2_part_1.py |
| TC-SET-5616 | P1 | Describe field value for CUSTOM_WORDS_PATH | key=CUSTOM_WORDS_PATH,field=value | present | test_settings_phase2_part_1.py |
| TC-SET-5617 | P1 | Describe field type for CUSTOM_WORDS_PATH | key=CUSTOM_WORDS_PATH,field=type | present | test_settings_phase2_part_1.py |
| TC-SET-5618 | P1 | Describe field editable for CUSTOM_WORDS_PATH | key=CUSTOM_WORDS_PATH,field=editable | present | test_settings_phase2_part_1.py |
| TC-SET-5619 | P1 | Describe field key for CUSTOM_WORDS_STORAGE | key=CUSTOM_WORDS_STORAGE,field=key | present | test_settings_phase2_part_1.py |
| TC-SET-5620 | P1 | Describe field value for CUSTOM_WORDS_STORAGE | key=CUSTOM_WORDS_STORAGE,field=value | present | test_settings_phase2_part_1.py |
| TC-SET-5621 | P1 | Describe field type for CUSTOM_WORDS_STORAGE | key=CUSTOM_WORDS_STORAGE,field=type | present | test_settings_phase2_part_1.py |
| TC-SET-5622 | P1 | Describe field editable for CUSTOM_WORDS_STORAGE | key=CUSTOM_WORDS_STORAGE,field=editable | present | test_settings_phase2_part_1.py |
| TC-SET-5623 | P1 | Describe field key for DETECTOR_THREAD_POOL_SIZE | key=DETECTOR_THREAD_POOL_SIZE,field=key | present | test_settings_phase2_part_1.py |
| TC-SET-5624 | P1 | Describe field value for DETECTOR_THREAD_POOL_SIZE | key=DETECTOR_THREAD_POOL_SIZE,field=value | present | test_settings_phase2_part_1.py |
| TC-SET-5625 | P1 | Describe field type for DETECTOR_THREAD_POOL_SIZE | key=DETECTOR_THREAD_POOL_SIZE,field=type | present | test_settings_phase2_part_1.py |
| TC-SET-5626 | P1 | Describe field editable for DETECTOR_THREAD_POOL_SIZE | key=DETECTOR_THREAD_POOL_SIZE,field=editable | present | test_settings_phase2_part_1.py |
| TC-SET-5627 | P1 | Describe field key for ENABLE_BADWORDS_PY | key=ENABLE_BADWORDS_PY,field=key | present | test_settings_phase2_part_1.py |
| TC-SET-5628 | P1 | Describe field value for ENABLE_BADWORDS_PY | key=ENABLE_BADWORDS_PY,field=value | present | test_settings_phase2_part_1.py |
| TC-SET-5629 | P1 | Describe field type for ENABLE_BADWORDS_PY | key=ENABLE_BADWORDS_PY,field=type | present | test_settings_phase2_part_1.py |
| TC-SET-5630 | P1 | Describe field editable for ENABLE_BADWORDS_PY | key=ENABLE_BADWORDS_PY,field=editable | present | test_settings_phase2_part_1.py |
| TC-SET-5631 | P1 | Describe field key for ENABLE_DETECTOR_AHO_CORASICK | key=ENABLE_DETECTOR_AHO_CORASICK,field=key | present | test_settings_phase2_part_1.py |
| TC-SET-5632 | P1 | Describe field value for ENABLE_DETECTOR_AHO_CORASICK | key=ENABLE_DETECTOR_AHO_CORASICK,field=value | present | test_settings_phase2_part_1.py |
| TC-SET-5633 | P1 | Describe field type for ENABLE_DETECTOR_AHO_CORASICK | key=ENABLE_DETECTOR_AHO_CORASICK,field=type | present | test_settings_phase2_part_1.py |
| TC-SET-5634 | P1 | Describe field editable for ENABLE_DETECTOR_AHO_CORASICK | key=ENABLE_DETECTOR_AHO_CORASICK,field=editable | present | test_settings_phase2_part_1.py |
| TC-SET-5635 | P1 | Describe field key for ENABLE_DETECTOR_BK_TREE | key=ENABLE_DETECTOR_BK_TREE,field=key | present | test_settings_phase2_part_1.py |
| TC-SET-5636 | P1 | Describe field value for ENABLE_DETECTOR_BK_TREE | key=ENABLE_DETECTOR_BK_TREE,field=value | present | test_settings_phase2_part_1.py |
| TC-SET-5637 | P1 | Describe field type for ENABLE_DETECTOR_BK_TREE | key=ENABLE_DETECTOR_BK_TREE,field=type | present | test_settings_phase2_part_1.py |
| TC-SET-5638 | P1 | Describe field editable for ENABLE_DETECTOR_BK_TREE | key=ENABLE_DETECTOR_BK_TREE,field=editable | present | test_settings_phase2_part_1.py |
| TC-SET-5639 | P1 | Describe field key for ENABLE_DETECTOR_BLOOM_FILTER | key=ENABLE_DETECTOR_BLOOM_FILTER,field=key | present | test_settings_phase2_part_1.py |
| TC-SET-5640 | P1 | Describe field value for ENABLE_DETECTOR_BLOOM_FILTER | key=ENABLE_DETECTOR_BLOOM_FILTER,field=value | present | test_settings_phase2_part_1.py |
| TC-SET-5641 | P1 | Describe field type for ENABLE_DETECTOR_BLOOM_FILTER | key=ENABLE_DETECTOR_BLOOM_FILTER,field=type | present | test_settings_phase2_part_1.py |
| TC-SET-5642 | P1 | Describe field editable for ENABLE_DETECTOR_BLOOM_FILTER | key=ENABLE_DETECTOR_BLOOM_FILTER,field=editable | present | test_settings_phase2_part_1.py |
| TC-SET-5643 | P1 | Describe field key for ENABLE_DETECTOR_DOUBLE_METAPHONE | key=ENABLE_DETECTOR_DOUBLE_METAPHONE,field=key | present | test_settings_phase2_part_1.py |
| TC-SET-5644 | P1 | Describe field value for ENABLE_DETECTOR_DOUBLE_METAPHONE | key=ENABLE_DETECTOR_DOUBLE_METAPHONE,field=value | present | test_settings_phase2_part_1.py |
| TC-SET-5645 | P1 | Describe field type for ENABLE_DETECTOR_DOUBLE_METAPHONE | key=ENABLE_DETECTOR_DOUBLE_METAPHONE,field=type | present | test_settings_phase2_part_1.py |
| TC-SET-5646 | P1 | Describe field editable for ENABLE_DETECTOR_DOUBLE_METAPHONE | key=ENABLE_DETECTOR_DOUBLE_METAPHONE,field=editable | present | test_settings_phase2_part_1.py |
| TC-SET-5647 | P1 | Describe field key for ENABLE_DETECTOR_MULTI_LANGUAGE | key=ENABLE_DETECTOR_MULTI_LANGUAGE,field=key | present | test_settings_phase2_part_1.py |
| TC-SET-5648 | P1 | Describe field value for ENABLE_DETECTOR_MULTI_LANGUAGE | key=ENABLE_DETECTOR_MULTI_LANGUAGE,field=value | present | test_settings_phase2_part_1.py |
| TC-SET-5649 | P1 | Describe field type for ENABLE_DETECTOR_MULTI_LANGUAGE | key=ENABLE_DETECTOR_MULTI_LANGUAGE,field=type | present | test_settings_phase2_part_1.py |
| TC-SET-5650 | P1 | Describe field editable for ENABLE_DETECTOR_MULTI_LANGUAGE | key=ENABLE_DETECTOR_MULTI_LANGUAGE,field=editable | present | test_settings_phase2_part_1.py |
| TC-SET-5651 | P1 | Describe field key for ENABLE_DETECTOR_ROLLING_HASH | key=ENABLE_DETECTOR_ROLLING_HASH,field=key | present | test_settings_phase2_part_1.py |
| TC-SET-5652 | P1 | Describe field value for ENABLE_DETECTOR_ROLLING_HASH | key=ENABLE_DETECTOR_ROLLING_HASH,field=value | present | test_settings_phase2_part_1.py |
| TC-SET-5653 | P1 | Describe field type for ENABLE_DETECTOR_ROLLING_HASH | key=ENABLE_DETECTOR_ROLLING_HASH,field=type | present | test_settings_phase2_part_1.py |
| TC-SET-5654 | P1 | Describe field editable for ENABLE_DETECTOR_ROLLING_HASH | key=ENABLE_DETECTOR_ROLLING_HASH,field=editable | present | test_settings_phase2_part_1.py |
| TC-SET-5655 | P1 | Describe field key for ENABLE_GANGAJAL | key=ENABLE_GANGAJAL,field=key | present | test_settings_phase2_part_1.py |
| TC-SET-5656 | P1 | Describe field value for ENABLE_GANGAJAL | key=ENABLE_GANGAJAL,field=value | present | test_settings_phase2_part_1.py |
| TC-SET-5657 | P1 | Describe field type for ENABLE_GANGAJAL | key=ENABLE_GANGAJAL,field=type | present | test_settings_phase2_part_1.py |
| TC-SET-5658 | P1 | Describe field editable for ENABLE_GANGAJAL | key=ENABLE_GANGAJAL,field=editable | present | test_settings_phase2_part_1.py |
| TC-SET-5659 | P1 | Describe field key for ENABLE_GLIN_PROFANITY | key=ENABLE_GLIN_PROFANITY,field=key | present | test_settings_phase2_part_1.py |
| TC-SET-5660 | P1 | Describe field value for ENABLE_GLIN_PROFANITY | key=ENABLE_GLIN_PROFANITY,field=value | present | test_settings_phase2_part_1.py |
| TC-SET-5661 | P1 | Describe field type for ENABLE_GLIN_PROFANITY | key=ENABLE_GLIN_PROFANITY,field=type | present | test_settings_phase2_part_1.py |
| TC-SET-5662 | P1 | Describe field editable for ENABLE_GLIN_PROFANITY | key=ENABLE_GLIN_PROFANITY,field=editable | present | test_settings_phase2_part_1.py |
| TC-SET-5663 | P1 | Describe field key for ENABLE_PHRASE_DETECTOR | key=ENABLE_PHRASE_DETECTOR,field=key | present | test_settings_phase2_part_2.py |
| TC-SET-5664 | P1 | Describe field value for ENABLE_PHRASE_DETECTOR | key=ENABLE_PHRASE_DETECTOR,field=value | present | test_settings_phase2_part_2.py |
| TC-SET-5665 | P1 | Describe field type for ENABLE_PHRASE_DETECTOR | key=ENABLE_PHRASE_DETECTOR,field=type | present | test_settings_phase2_part_2.py |
| TC-SET-5666 | P1 | Describe field editable for ENABLE_PHRASE_DETECTOR | key=ENABLE_PHRASE_DETECTOR,field=editable | present | test_settings_phase2_part_2.py |
| TC-SET-5667 | P1 | Describe field key for ENABLE_PROFANITE | key=ENABLE_PROFANITE,field=key | present | test_settings_phase2_part_2.py |
| TC-SET-5668 | P1 | Describe field value for ENABLE_PROFANITE | key=ENABLE_PROFANITE,field=value | present | test_settings_phase2_part_2.py |
| TC-SET-5669 | P1 | Describe field type for ENABLE_PROFANITE | key=ENABLE_PROFANITE,field=type | present | test_settings_phase2_part_2.py |
| TC-SET-5670 | P1 | Describe field editable for ENABLE_PROFANITE | key=ENABLE_PROFANITE,field=editable | present | test_settings_phase2_part_2.py |
| TC-SET-5671 | P1 | Describe field key for ENABLE_PROFANITY_FILTER | key=ENABLE_PROFANITY_FILTER,field=key | present | test_settings_phase2_part_2.py |
| TC-SET-5672 | P1 | Describe field value for ENABLE_PROFANITY_FILTER | key=ENABLE_PROFANITY_FILTER,field=value | present | test_settings_phase2_part_2.py |
| TC-SET-5673 | P1 | Describe field type for ENABLE_PROFANITY_FILTER | key=ENABLE_PROFANITY_FILTER,field=type | present | test_settings_phase2_part_2.py |
| TC-SET-5674 | P1 | Describe field editable for ENABLE_PROFANITY_FILTER | key=ENABLE_PROFANITY_FILTER,field=editable | present | test_settings_phase2_part_2.py |
| TC-SET-5675 | P1 | Describe field key for ENABLE_PYPROFANE | key=ENABLE_PYPROFANE,field=key | present | test_settings_phase2_part_2.py |
| TC-SET-5676 | P1 | Describe field value for ENABLE_PYPROFANE | key=ENABLE_PYPROFANE,field=value | present | test_settings_phase2_part_2.py |
| TC-SET-5677 | P1 | Describe field type for ENABLE_PYPROFANE | key=ENABLE_PYPROFANE,field=type | present | test_settings_phase2_part_2.py |
| TC-SET-5678 | P1 | Describe field editable for ENABLE_PYPROFANE | key=ENABLE_PYPROFANE,field=editable | present | test_settings_phase2_part_2.py |
| TC-SET-5679 | P1 | Describe field key for ENABLE_SAFETEXT | key=ENABLE_SAFETEXT,field=key | present | test_settings_phase2_part_2.py |
| TC-SET-5680 | P1 | Describe field value for ENABLE_SAFETEXT | key=ENABLE_SAFETEXT,field=value | present | test_settings_phase2_part_2.py |
| TC-SET-5681 | P1 | Describe field type for ENABLE_SAFETEXT | key=ENABLE_SAFETEXT,field=type | present | test_settings_phase2_part_2.py |
| TC-SET-5682 | P1 | Describe field editable for ENABLE_SAFETEXT | key=ENABLE_SAFETEXT,field=editable | present | test_settings_phase2_part_2.py |
| TC-SET-5683 | P1 | Describe field key for ENABLE_SENSITIVE_STOP_WORDS | key=ENABLE_SENSITIVE_STOP_WORDS,field=key | present | test_settings_phase2_part_2.py |
| TC-SET-5684 | P1 | Describe field value for ENABLE_SENSITIVE_STOP_WORDS | key=ENABLE_SENSITIVE_STOP_WORDS,field=value | present | test_settings_phase2_part_2.py |
| TC-SET-5685 | P1 | Describe field type for ENABLE_SENSITIVE_STOP_WORDS | key=ENABLE_SENSITIVE_STOP_WORDS,field=type | present | test_settings_phase2_part_2.py |
| TC-SET-5686 | P1 | Describe field editable for ENABLE_SENSITIVE_STOP_WORDS | key=ENABLE_SENSITIVE_STOP_WORDS,field=editable | present | test_settings_phase2_part_2.py |
| TC-SET-5687 | P1 | Describe field key for ENABLE_SENSITIVE_STOP_WORDS_AD | key=ENABLE_SENSITIVE_STOP_WORDS_AD,field=key | present | test_settings_phase2_part_2.py |
| TC-SET-5688 | P1 | Describe field value for ENABLE_SENSITIVE_STOP_WORDS_AD | key=ENABLE_SENSITIVE_STOP_WORDS_AD,field=value | present | test_settings_phase2_part_2.py |
| TC-SET-5689 | P1 | Describe field type for ENABLE_SENSITIVE_STOP_WORDS_AD | key=ENABLE_SENSITIVE_STOP_WORDS_AD,field=type | present | test_settings_phase2_part_2.py |
| TC-SET-5690 | P1 | Describe field editable for ENABLE_SENSITIVE_STOP_WORDS_AD | key=ENABLE_SENSITIVE_STOP_WORDS_AD,field=editable | present | test_settings_phase2_part_2.py |
| TC-SET-5691 | P1 | Describe field key for ENABLE_SENSITIVE_STOP_WORDS_GUN | key=ENABLE_SENSITIVE_STOP_WORDS_GUN,field=key | present | test_settings_phase2_part_2.py |
| TC-SET-5692 | P1 | Describe field value for ENABLE_SENSITIVE_STOP_WORDS_GUN | key=ENABLE_SENSITIVE_STOP_WORDS_GUN,field=value | present | test_settings_phase2_part_2.py |
| TC-SET-5693 | P1 | Describe field type for ENABLE_SENSITIVE_STOP_WORDS_GUN | key=ENABLE_SENSITIVE_STOP_WORDS_GUN,field=type | present | test_settings_phase2_part_2.py |
| TC-SET-5694 | P1 | Describe field editable for ENABLE_SENSITIVE_STOP_WORDS_GUN | key=ENABLE_SENSITIVE_STOP_WORDS_GUN,field=editable | present | test_settings_phase2_part_2.py |
| TC-SET-5695 | P1 | Describe field key for ENABLE_SENSITIVE_STOP_WORDS_POLITICAL | key=ENABLE_SENSITIVE_STOP_WORDS_POLITICAL,field=key | present | test_settings_phase2_part_2.py |
| TC-SET-5696 | P1 | Describe field value for ENABLE_SENSITIVE_STOP_WORDS_POLITICAL | key=ENABLE_SENSITIVE_STOP_WORDS_POLITICAL,field=value | present | test_settings_phase2_part_2.py |
| TC-SET-5697 | P1 | Describe field type for ENABLE_SENSITIVE_STOP_WORDS_POLITICAL | key=ENABLE_SENSITIVE_STOP_WORDS_POLITICAL,field=type | present | test_settings_phase2_part_2.py |
| TC-SET-5698 | P1 | Describe field editable for ENABLE_SENSITIVE_STOP_WORDS_POLITICAL | key=ENABLE_SENSITIVE_STOP_WORDS_POLITICAL,field=editable | present | test_settings_phase2_part_2.py |
| TC-SET-5699 | P1 | Describe field key for ENABLE_SENSITIVE_STOP_WORDS_PORN | key=ENABLE_SENSITIVE_STOP_WORDS_PORN,field=key | present | test_settings_phase2_part_2.py |
| TC-SET-5700 | P1 | Describe field value for ENABLE_SENSITIVE_STOP_WORDS_PORN | key=ENABLE_SENSITIVE_STOP_WORDS_PORN,field=value | present | test_settings_phase2_part_2.py |
| TC-SET-5701 | P1 | Describe field type for ENABLE_SENSITIVE_STOP_WORDS_PORN | key=ENABLE_SENSITIVE_STOP_WORDS_PORN,field=type | present | test_settings_phase2_part_2.py |
| TC-SET-5702 | P1 | Describe field editable for ENABLE_SENSITIVE_STOP_WORDS_PORN | key=ENABLE_SENSITIVE_STOP_WORDS_PORN,field=editable | present | test_settings_phase2_part_2.py |
| TC-SET-5703 | P1 | Describe field key for ENABLE_SENSITIVE_STOP_WORDS_URL | key=ENABLE_SENSITIVE_STOP_WORDS_URL,field=key | present | test_settings_phase2_part_2.py |
| TC-SET-5704 | P1 | Describe field value for ENABLE_SENSITIVE_STOP_WORDS_URL | key=ENABLE_SENSITIVE_STOP_WORDS_URL,field=value | present | test_settings_phase2_part_2.py |
| TC-SET-5705 | P1 | Describe field type for ENABLE_SENSITIVE_STOP_WORDS_URL | key=ENABLE_SENSITIVE_STOP_WORDS_URL,field=type | present | test_settings_phase2_part_2.py |
| TC-SET-5706 | P1 | Describe field editable for ENABLE_SENSITIVE_STOP_WORDS_URL | key=ENABLE_SENSITIVE_STOP_WORDS_URL,field=editable | present | test_settings_phase2_part_2.py |
| TC-SET-5707 | P1 | Describe field key for ENABLE_SENSITIVE_WORD_FILTER_CN | key=ENABLE_SENSITIVE_WORD_FILTER_CN,field=key | present | test_settings_phase2_part_2.py |
| TC-SET-5708 | P1 | Describe field value for ENABLE_SENSITIVE_WORD_FILTER_CN | key=ENABLE_SENSITIVE_WORD_FILTER_CN,field=value | present | test_settings_phase2_part_2.py |
| TC-SET-5709 | P1 | Describe field type for ENABLE_SENSITIVE_WORD_FILTER_CN | key=ENABLE_SENSITIVE_WORD_FILTER_CN,field=type | present | test_settings_phase2_part_2.py |
| TC-SET-5710 | P1 | Describe field editable for ENABLE_SENSITIVE_WORD_FILTER_CN | key=ENABLE_SENSITIVE_WORD_FILTER_CN,field=editable | present | test_settings_phase2_part_2.py |
| TC-SET-5711 | P1 | Describe field key for ENCRYPTION_KEY | key=ENCRYPTION_KEY,field=key | present | test_settings_phase2_part_2.py |
| TC-SET-5712 | P1 | Describe field value for ENCRYPTION_KEY | key=ENCRYPTION_KEY,field=value | present | test_settings_phase2_part_2.py |
| TC-SET-6051 | P1 | Read-only ADMIN_API_KEY attempt 0 | key=ADMIN_API_KEY,attempt=0 | rejected | test_settings_phase2_part_2.py |
| TC-SET-6052 | P1 | Read-only ADMIN_API_KEY attempt 1 | key=ADMIN_API_KEY,attempt=1 | rejected | test_settings_phase2_part_2.py |
| TC-SET-6053 | P1 | Read-only ADMIN_API_KEY attempt 2 | key=ADMIN_API_KEY,attempt=2 | rejected | test_settings_phase2_part_2.py |
| TC-SET-6054 | P1 | Read-only ADMIN_API_KEY attempt 3 | key=ADMIN_API_KEY,attempt=3 | rejected | test_settings_phase2_part_2.py |
| TC-SET-6055 | P1 | Read-only ADMIN_API_KEY attempt 4 | key=ADMIN_API_KEY,attempt=4 | rejected | test_settings_phase2_part_2.py |
| TC-SET-6056 | P1 | Read-only ADMIN_API_KEY attempt 5 | key=ADMIN_API_KEY,attempt=5 | rejected | test_settings_phase2_part_2.py |
| TC-SET-6057 | P1 | Read-only APP_PORT attempt 0 | key=APP_PORT,attempt=0 | rejected | test_settings_phase2_part_2.py |
| TC-SET-6058 | P1 | Read-only APP_PORT attempt 1 | key=APP_PORT,attempt=1 | rejected | test_settings_phase2_part_2.py |
| TC-SET-6059 | P1 | Read-only APP_PORT attempt 2 | key=APP_PORT,attempt=2 | rejected | test_settings_phase2_part_2.py |
| TC-SET-6060 | P1 | Read-only APP_PORT attempt 3 | key=APP_PORT,attempt=3 | rejected | test_settings_phase2_part_2.py |
| TC-SET-6061 | P1 | Read-only APP_PORT attempt 4 | key=APP_PORT,attempt=4 | rejected | test_settings_phase2_part_2.py |
| TC-SET-6062 | P1 | Read-only APP_PORT attempt 5 | key=APP_PORT,attempt=5 | rejected | test_settings_phase2_part_2.py |
| TC-SET-6063 | P1 | Read-only ENCRYPTION_KEY attempt 0 | key=ENCRYPTION_KEY,attempt=0 | rejected | test_settings_phase2_part_2.py |
| TC-SET-6064 | P1 | Read-only ENCRYPTION_KEY attempt 1 | key=ENCRYPTION_KEY,attempt=1 | rejected | test_settings_phase2_part_2.py |
| TC-SET-6065 | P1 | Read-only ENCRYPTION_KEY attempt 2 | key=ENCRYPTION_KEY,attempt=2 | rejected | test_settings_phase2_part_2.py |
| TC-SET-6066 | P1 | Read-only ENCRYPTION_KEY attempt 3 | key=ENCRYPTION_KEY,attempt=3 | rejected | test_settings_phase2_part_2.py |
| TC-SET-6067 | P1 | Read-only ENCRYPTION_KEY attempt 4 | key=ENCRYPTION_KEY,attempt=4 | rejected | test_settings_phase2_part_2.py |
| TC-SET-6068 | P1 | Read-only ENCRYPTION_KEY attempt 5 | key=ENCRYPTION_KEY,attempt=5 | rejected | test_settings_phase2_part_2.py |
| TC-SET-6069 | P1 | Read-only EXPORT_TEMP_DIR attempt 0 | key=EXPORT_TEMP_DIR,attempt=0 | rejected | test_settings_phase2_part_2.py |
| TC-SET-6070 | P1 | Read-only EXPORT_TEMP_DIR attempt 1 | key=EXPORT_TEMP_DIR,attempt=1 | rejected | test_settings_phase2_part_2.py |
| TC-SET-6071 | P1 | Read-only EXPORT_TEMP_DIR attempt 2 | key=EXPORT_TEMP_DIR,attempt=2 | rejected | test_settings_phase2_part_2.py |
| TC-SET-6072 | P1 | Read-only EXPORT_TEMP_DIR attempt 3 | key=EXPORT_TEMP_DIR,attempt=3 | rejected | test_settings_phase2_part_2.py |
| TC-SET-6073 | P1 | Read-only EXPORT_TEMP_DIR attempt 4 | key=EXPORT_TEMP_DIR,attempt=4 | rejected | test_settings_phase2_part_2.py |
| TC-SET-6074 | P1 | Read-only EXPORT_TEMP_DIR attempt 5 | key=EXPORT_TEMP_DIR,attempt=5 | rejected | test_settings_phase2_part_2.py |
| TC-SET-6075 | P1 | Read-only FEEDBACK_DB_PATH attempt 0 | key=FEEDBACK_DB_PATH,attempt=0 | rejected | test_settings_phase2_part_2.py |
| TC-SET-6076 | P1 | Read-only FEEDBACK_DB_PATH attempt 1 | key=FEEDBACK_DB_PATH,attempt=1 | rejected | test_settings_phase2_part_2.py |
| TC-SET-6077 | P1 | Read-only FEEDBACK_DB_PATH attempt 2 | key=FEEDBACK_DB_PATH,attempt=2 | rejected | test_settings_phase2_part_2.py |
| TC-SET-6078 | P1 | Read-only FEEDBACK_DB_PATH attempt 3 | key=FEEDBACK_DB_PATH,attempt=3 | rejected | test_settings_phase2_part_2.py |
| TC-SET-6079 | P1 | Read-only FEEDBACK_DB_PATH attempt 4 | key=FEEDBACK_DB_PATH,attempt=4 | rejected | test_settings_phase2_part_2.py |
| TC-SET-6080 | P1 | Read-only FEEDBACK_DB_PATH attempt 5 | key=FEEDBACK_DB_PATH,attempt=5 | rejected | test_settings_phase2_part_2.py |
| TC-SET-6081 | P1 | Read-only MODEL_PATH attempt 0 | key=MODEL_PATH,attempt=0 | rejected | test_settings_phase2_part_2.py |
| TC-SET-6082 | P1 | Read-only MODEL_PATH attempt 1 | key=MODEL_PATH,attempt=1 | rejected | test_settings_phase2_part_2.py |
| TC-SET-6083 | P1 | Read-only MODEL_PATH attempt 2 | key=MODEL_PATH,attempt=2 | rejected | test_settings_phase2_part_2.py |
| TC-SET-6084 | P1 | Read-only MODEL_PATH attempt 3 | key=MODEL_PATH,attempt=3 | rejected | test_settings_phase2_part_2.py |
| TC-SET-6085 | P1 | Read-only MODEL_PATH attempt 4 | key=MODEL_PATH,attempt=4 | rejected | test_settings_phase2_part_2.py |
| TC-SET-6086 | P1 | Read-only MODEL_PATH attempt 5 | key=MODEL_PATH,attempt=5 | rejected | test_settings_phase2_part_2.py |
| TC-SET-6087 | P1 | Read-only SECRET_KEY attempt 0 | key=SECRET_KEY,attempt=0 | rejected | test_settings_phase2_part_2.py |
| TC-SET-6088 | P1 | Read-only SECRET_KEY attempt 1 | key=SECRET_KEY,attempt=1 | rejected | test_settings_phase2_part_2.py |
| TC-SET-6089 | P1 | Read-only SECRET_KEY attempt 2 | key=SECRET_KEY,attempt=2 | rejected | test_settings_phase2_part_2.py |
| TC-SET-6090 | P1 | Read-only SECRET_KEY attempt 3 | key=SECRET_KEY,attempt=3 | rejected | test_settings_phase2_part_2.py |
| TC-SET-6091 | P1 | Read-only SECRET_KEY attempt 4 | key=SECRET_KEY,attempt=4 | rejected | test_settings_phase2_part_2.py |
| TC-SET-6092 | P1 | Read-only SECRET_KEY attempt 5 | key=SECRET_KEY,attempt=5 | rejected | test_settings_phase2_part_2.py |
| TC-SET-6093 | P1 | Read-only WEBUI_API_KEY attempt 0 | key=WEBUI_API_KEY,attempt=0 | rejected | test_settings_phase2_part_2.py |
| TC-SET-6094 | P1 | Read-only WEBUI_API_KEY attempt 1 | key=WEBUI_API_KEY,attempt=1 | rejected | test_settings_phase2_part_2.py |
| TC-SET-6095 | P1 | Read-only WEBUI_API_KEY attempt 2 | key=WEBUI_API_KEY,attempt=2 | rejected | test_settings_phase2_part_2.py |
| TC-SET-6096 | P1 | Read-only WEBUI_API_KEY attempt 3 | key=WEBUI_API_KEY,attempt=3 | rejected | test_settings_phase2_part_2.py |
| TC-SET-6097 | P1 | Read-only WEBUI_API_KEY attempt 4 | key=WEBUI_API_KEY,attempt=4 | rejected | test_settings_phase2_part_2.py |
| TC-SET-6098 | P1 | Read-only WEBUI_API_KEY attempt 5 | key=WEBUI_API_KEY,attempt=5 | rejected | test_settings_phase2_part_2.py |
| TC-SET-6099 | P1 | Read-only WORKERS attempt 0 | key=WORKERS,attempt=0 | rejected | test_settings_phase2_part_2.py |
| TC-SET-6100 | P1 | Read-only WORKERS attempt 1 | key=WORKERS,attempt=1 | rejected | test_settings_phase2_part_2.py |
| TC-SET-6101 | P2 | Valid update AI_TARGET_PERCENTAGE = 25 | key=AI_TARGET_PERCENTAGE,value=25 | accepted | test_settings_phase2_part_3.py |
| TC-SET-6102 | P2 | Valid update AI_TARGET_PERCENTAGE = 50 | key=AI_TARGET_PERCENTAGE,value=50 | accepted | test_settings_phase2_part_3.py |
| TC-SET-6103 | P2 | Valid update AI_TARGET_PERCENTAGE = 100 | key=AI_TARGET_PERCENTAGE,value=100 | accepted | test_settings_phase2_part_3.py |
| TC-SET-6104 | P2 | Valid update ALLOWED_ORIGINS = sample-value | key=ALLOWED_ORIGINS,value='sample-value' | accepted | test_settings_phase2_part_3.py |
| TC-SET-6105 | P2 | Valid update ALLOWED_ORIGINS = config-value | key=ALLOWED_ORIGINS,value='config-value' | accepted | test_settings_phase2_part_3.py |
| TC-SET-6106 | P2 | Valid update ALLOWED_ORIGINS = 192.168.0.1 | key=ALLOWED_ORIGINS,value='192.168.0.1' | accepted | test_settings_phase2_part_3.py |
| TC-SET-6107 | P2 | Valid update APP_CONFIG_DB_PATH = sample-value | key=APP_CONFIG_DB_PATH,value='sample-value' | accepted | test_settings_phase2_part_3.py |
| TC-SET-6108 | P2 | Valid update APP_CONFIG_DB_PATH = config-value | key=APP_CONFIG_DB_PATH,value='config-value' | accepted | test_settings_phase2_part_3.py |
| TC-SET-6109 | P2 | Valid update APP_CONFIG_DB_PATH = 192.168.0.1 | key=APP_CONFIG_DB_PATH,value='192.168.0.1' | accepted | test_settings_phase2_part_3.py |
| TC-SET-6110 | P2 | Valid update APP_HOST = sample-value | key=APP_HOST,value='sample-value' | accepted | test_settings_phase2_part_3.py |
| TC-SET-6111 | P2 | Valid update APP_HOST = config-value | key=APP_HOST,value='config-value' | accepted | test_settings_phase2_part_3.py |
| TC-SET-6112 | P2 | Valid update APP_HOST = 192.168.0.1 | key=APP_HOST,value='192.168.0.1' | accepted | test_settings_phase2_part_3.py |
| TC-SET-6113 | P2 | Valid update AUTO_TUNING_ENABLED = True | key=AUTO_TUNING_ENABLED,value=True | accepted | test_settings_phase2_part_3.py |
| TC-SET-6114 | P2 | Valid update AUTO_TUNING_ENABLED = False | key=AUTO_TUNING_ENABLED,value=False | accepted | test_settings_phase2_part_3.py |
| TC-SET-6115 | P2 | Valid update BLOOM_FILTER_CAPACITY = sample-value | key=BLOOM_FILTER_CAPACITY,value='sample-value' | accepted | test_settings_phase2_part_3.py |
| TC-SET-6116 | P2 | Valid update BLOOM_FILTER_CAPACITY = config-value | key=BLOOM_FILTER_CAPACITY,value='config-value' | accepted | test_settings_phase2_part_3.py |
| TC-SET-6117 | P2 | Valid update BLOOM_FILTER_CAPACITY = 192.168.0.1 | key=BLOOM_FILTER_CAPACITY,value='192.168.0.1' | accepted | test_settings_phase2_part_3.py |
| TC-SET-6118 | P2 | Valid update BLOOM_FILTER_ERROR_RATE = sample-value | key=BLOOM_FILTER_ERROR_RATE,value='sample-value' | accepted | test_settings_phase2_part_3.py |
| TC-SET-6119 | P2 | Valid update BLOOM_FILTER_ERROR_RATE = config-value | key=BLOOM_FILTER_ERROR_RATE,value='config-value' | accepted | test_settings_phase2_part_3.py |
| TC-SET-6120 | P2 | Valid update BLOOM_FILTER_ERROR_RATE = 192.168.0.1 | key=BLOOM_FILTER_ERROR_RATE,value='192.168.0.1' | accepted | test_settings_phase2_part_3.py |
| TC-SET-6121 | P2 | Valid update CACHE_MAX_SIZE = 25 | key=CACHE_MAX_SIZE,value=25 | accepted | test_settings_phase2_part_3.py |
| TC-SET-6122 | P2 | Valid update CACHE_MAX_SIZE = 50 | key=CACHE_MAX_SIZE,value=50 | accepted | test_settings_phase2_part_3.py |
| TC-SET-6123 | P2 | Valid update CACHE_MAX_SIZE = 100 | key=CACHE_MAX_SIZE,value=100 | accepted | test_settings_phase2_part_3.py |
| TC-SET-6124 | P2 | Valid update CACHE_MAX_SIZE = 250 | key=CACHE_MAX_SIZE,value=250 | accepted | test_settings_phase2_part_3.py |
| TC-SET-6125 | P2 | Valid update CACHE_MAX_SIZE = 500 | key=CACHE_MAX_SIZE,value=500 | accepted | test_settings_phase2_part_3.py |
| TC-SET-6126 | P2 | Valid update CACHE_TTL_SECONDS = 25 | key=CACHE_TTL_SECONDS,value=25 | accepted | test_settings_phase2_part_3.py |
| TC-SET-6127 | P2 | Valid update CACHE_TTL_SECONDS = 50 | key=CACHE_TTL_SECONDS,value=50 | accepted | test_settings_phase2_part_3.py |
| TC-SET-6128 | P2 | Valid update CACHE_TTL_SECONDS = 100 | key=CACHE_TTL_SECONDS,value=100 | accepted | test_settings_phase2_part_3.py |
| TC-SET-6129 | P2 | Valid update CACHE_TTL_SECONDS = 250 | key=CACHE_TTL_SECONDS,value=250 | accepted | test_settings_phase2_part_3.py |
| TC-SET-6130 | P2 | Valid update CACHE_TTL_SECONDS = 500 | key=CACHE_TTL_SECONDS,value=500 | accepted | test_settings_phase2_part_3.py |
| TC-SET-6131 | P2 | Valid update CRITICAL_PHRASES_DB_PATH = sample-value | key=CRITICAL_PHRASES_DB_PATH,value='sample-value' | accepted | test_settings_phase2_part_3.py |
| TC-SET-6132 | P2 | Valid update CRITICAL_PHRASES_DB_PATH = config-value | key=CRITICAL_PHRASES_DB_PATH,value='config-value' | accepted | test_settings_phase2_part_3.py |
| TC-SET-6133 | P2 | Valid update CRITICAL_PHRASES_DB_PATH = 192.168.0.1 | key=CRITICAL_PHRASES_DB_PATH,value='192.168.0.1' | accepted | test_settings_phase2_part_3.py |
| TC-SET-6134 | P2 | Valid update CUSTOM_WORDS_PATH = sample-value | key=CUSTOM_WORDS_PATH,value='sample-value' | accepted | test_settings_phase2_part_3.py |
| TC-SET-6135 | P2 | Valid update CUSTOM_WORDS_PATH = config-value | key=CUSTOM_WORDS_PATH,value='config-value' | accepted | test_settings_phase2_part_3.py |
| TC-SET-6136 | P2 | Valid update CUSTOM_WORDS_PATH = 192.168.0.1 | key=CUSTOM_WORDS_PATH,value='192.168.0.1' | accepted | test_settings_phase2_part_3.py |
| TC-SET-6137 | P2 | Valid update CUSTOM_WORDS_STORAGE = sample-value | key=CUSTOM_WORDS_STORAGE,value='sample-value' | accepted | test_settings_phase2_part_3.py |
| TC-SET-6138 | P2 | Valid update CUSTOM_WORDS_STORAGE = config-value | key=CUSTOM_WORDS_STORAGE,value='config-value' | accepted | test_settings_phase2_part_3.py |
| TC-SET-6139 | P2 | Valid update CUSTOM_WORDS_STORAGE = 192.168.0.1 | key=CUSTOM_WORDS_STORAGE,value='192.168.0.1' | accepted | test_settings_phase2_part_3.py |
| TC-SET-6140 | P2 | Valid update DETECTOR_THREAD_POOL_SIZE = 25 | key=DETECTOR_THREAD_POOL_SIZE,value=25 | accepted | test_settings_phase2_part_3.py |
| TC-SET-6141 | P2 | Valid update DETECTOR_THREAD_POOL_SIZE = 50 | key=DETECTOR_THREAD_POOL_SIZE,value=50 | accepted | test_settings_phase2_part_3.py |
| TC-SET-6142 | P2 | Valid update ENABLE_BADWORDS_PY = True | key=ENABLE_BADWORDS_PY,value=True | accepted | test_settings_phase2_part_3.py |
| TC-SET-6143 | P2 | Valid update ENABLE_BADWORDS_PY = False | key=ENABLE_BADWORDS_PY,value=False | accepted | test_settings_phase2_part_3.py |
| TC-SET-6144 | P2 | Valid update ENABLE_DETECTOR_AHO_CORASICK = True | key=ENABLE_DETECTOR_AHO_CORASICK,value=True | accepted | test_settings_phase2_part_3.py |
| TC-SET-6145 | P2 | Valid update ENABLE_DETECTOR_AHO_CORASICK = False | key=ENABLE_DETECTOR_AHO_CORASICK,value=False | accepted | test_settings_phase2_part_3.py |
| TC-SET-6146 | P2 | Valid update ENABLE_DETECTOR_BK_TREE = True | key=ENABLE_DETECTOR_BK_TREE,value=True | accepted | test_settings_phase2_part_3.py |
| TC-SET-6147 | P2 | Valid update ENABLE_DETECTOR_BK_TREE = False | key=ENABLE_DETECTOR_BK_TREE,value=False | accepted | test_settings_phase2_part_3.py |
| TC-SET-6148 | P2 | Valid update ENABLE_DETECTOR_BLOOM_FILTER = True | key=ENABLE_DETECTOR_BLOOM_FILTER,value=True | accepted | test_settings_phase2_part_3.py |
| TC-SET-6149 | P2 | Valid update ENABLE_DETECTOR_BLOOM_FILTER = False | key=ENABLE_DETECTOR_BLOOM_FILTER,value=False | accepted | test_settings_phase2_part_3.py |
| TC-SET-6150 | P2 | Valid update ENABLE_DETECTOR_DOUBLE_METAPHONE = True | key=ENABLE_DETECTOR_DOUBLE_METAPHONE,value=True | accepted | test_settings_phase2_part_3.py |
| TC-SET-6151 | P2 | Valid update ENABLE_DETECTOR_DOUBLE_METAPHONE = False | key=ENABLE_DETECTOR_DOUBLE_METAPHONE,value=False | accepted | test_settings_phase2_part_3.py |
| TC-SET-6152 | P2 | Valid update ENABLE_DETECTOR_MULTI_LANGUAGE = True | key=ENABLE_DETECTOR_MULTI_LANGUAGE,value=True | accepted | test_settings_phase2_part_3.py |
| TC-SET-6153 | P2 | Valid update ENABLE_DETECTOR_MULTI_LANGUAGE = False | key=ENABLE_DETECTOR_MULTI_LANGUAGE,value=False | accepted | test_settings_phase2_part_3.py |
| TC-SET-6154 | P2 | Valid update ENABLE_DETECTOR_ROLLING_HASH = True | key=ENABLE_DETECTOR_ROLLING_HASH,value=True | accepted | test_settings_phase2_part_3.py |
| TC-SET-6155 | P2 | Valid update ENABLE_DETECTOR_ROLLING_HASH = False | key=ENABLE_DETECTOR_ROLLING_HASH,value=False | accepted | test_settings_phase2_part_3.py |
| TC-SET-6156 | P2 | Valid update ENABLE_GANGAJAL = True | key=ENABLE_GANGAJAL,value=True | accepted | test_settings_phase2_part_3.py |
| TC-SET-6157 | P2 | Valid update ENABLE_GANGAJAL = False | key=ENABLE_GANGAJAL,value=False | accepted | test_settings_phase2_part_3.py |
| TC-SET-6158 | P2 | Valid update ENABLE_GLIN_PROFANITY = True | key=ENABLE_GLIN_PROFANITY,value=True | accepted | test_settings_phase2_part_3.py |
| TC-SET-6159 | P2 | Valid update ENABLE_GLIN_PROFANITY = False | key=ENABLE_GLIN_PROFANITY,value=False | accepted | test_settings_phase2_part_3.py |
| TC-SET-6160 | P2 | Valid update ENABLE_PHRASE_DETECTOR = True | key=ENABLE_PHRASE_DETECTOR,value=True | accepted | test_settings_phase2_part_3.py |
| TC-SET-6161 | P2 | Valid update ENABLE_PHRASE_DETECTOR = False | key=ENABLE_PHRASE_DETECTOR,value=False | accepted | test_settings_phase2_part_3.py |
| TC-SET-6162 | P2 | Valid update ENABLE_PROFANITE = True | key=ENABLE_PROFANITE,value=True | accepted | test_settings_phase2_part_3.py |
| TC-SET-6163 | P2 | Valid update ENABLE_PROFANITE = False | key=ENABLE_PROFANITE,value=False | accepted | test_settings_phase2_part_3.py |
| TC-SET-6164 | P2 | Valid update ENABLE_PROFANITY_FILTER = True | key=ENABLE_PROFANITY_FILTER,value=True | accepted | test_settings_phase2_part_3.py |
| TC-SET-6165 | P2 | Valid update ENABLE_PROFANITY_FILTER = False | key=ENABLE_PROFANITY_FILTER,value=False | accepted | test_settings_phase2_part_3.py |
| TC-SET-6166 | P2 | Valid update ENABLE_PYPROFANE = True | key=ENABLE_PYPROFANE,value=True | accepted | test_settings_phase2_part_3.py |
| TC-SET-6167 | P2 | Valid update ENABLE_PYPROFANE = False | key=ENABLE_PYPROFANE,value=False | accepted | test_settings_phase2_part_3.py |
| TC-SET-6168 | P2 | Valid update ENABLE_SAFETEXT = True | key=ENABLE_SAFETEXT,value=True | accepted | test_settings_phase2_part_3.py |
| TC-SET-6169 | P2 | Valid update ENABLE_SAFETEXT = False | key=ENABLE_SAFETEXT,value=False | accepted | test_settings_phase2_part_3.py |
| TC-SET-6170 | P2 | Valid update ENABLE_SENSITIVE_STOP_WORDS = True | key=ENABLE_SENSITIVE_STOP_WORDS,value=True | accepted | test_settings_phase2_part_3.py |
| TC-SET-6171 | P2 | Valid update ENABLE_SENSITIVE_STOP_WORDS = False | key=ENABLE_SENSITIVE_STOP_WORDS,value=False | accepted | test_settings_phase2_part_3.py |
| TC-SET-6172 | P2 | Valid update ENABLE_SENSITIVE_STOP_WORDS_AD = True | key=ENABLE_SENSITIVE_STOP_WORDS_AD,value=True | accepted | test_settings_phase2_part_3.py |
| TC-SET-6173 | P2 | Valid update ENABLE_SENSITIVE_STOP_WORDS_AD = False | key=ENABLE_SENSITIVE_STOP_WORDS_AD,value=False | accepted | test_settings_phase2_part_3.py |
| TC-SET-6174 | P2 | Valid update ENABLE_SENSITIVE_STOP_WORDS_GUN = True | key=ENABLE_SENSITIVE_STOP_WORDS_GUN,value=True | accepted | test_settings_phase2_part_3.py |
| TC-SET-6175 | P2 | Valid update ENABLE_SENSITIVE_STOP_WORDS_GUN = False | key=ENABLE_SENSITIVE_STOP_WORDS_GUN,value=False | accepted | test_settings_phase2_part_3.py |
| TC-SET-6176 | P2 | Valid update ENABLE_SENSITIVE_STOP_WORDS_POLITICAL = True | key=ENABLE_SENSITIVE_STOP_WORDS_POLITICAL,value=True | accepted | test_settings_phase2_part_3.py |
| TC-SET-6177 | P2 | Valid update ENABLE_SENSITIVE_STOP_WORDS_POLITICAL = False | key=ENABLE_SENSITIVE_STOP_WORDS_POLITICAL,value=False | accepted | test_settings_phase2_part_3.py |
| TC-SET-6178 | P2 | Valid update ENABLE_SENSITIVE_STOP_WORDS_PORN = True | key=ENABLE_SENSITIVE_STOP_WORDS_PORN,value=True | accepted | test_settings_phase2_part_3.py |
| TC-SET-6179 | P2 | Valid update ENABLE_SENSITIVE_STOP_WORDS_PORN = False | key=ENABLE_SENSITIVE_STOP_WORDS_PORN,value=False | accepted | test_settings_phase2_part_3.py |
| TC-SET-6180 | P2 | Valid update ENABLE_SENSITIVE_STOP_WORDS_URL = True | key=ENABLE_SENSITIVE_STOP_WORDS_URL,value=True | accepted | test_settings_phase2_part_3.py |
| TC-SET-6181 | P2 | Valid update ENABLE_SENSITIVE_STOP_WORDS_URL = False | key=ENABLE_SENSITIVE_STOP_WORDS_URL,value=False | accepted | test_settings_phase2_part_3.py |
| TC-SET-6182 | P2 | Valid update ENABLE_SENSITIVE_WORD_FILTER_CN = True | key=ENABLE_SENSITIVE_WORD_FILTER_CN,value=True | accepted | test_settings_phase2_part_3.py |
| TC-SET-6183 | P2 | Valid update ENABLE_SENSITIVE_WORD_FILTER_CN = False | key=ENABLE_SENSITIVE_WORD_FILTER_CN,value=False | accepted | test_settings_phase2_part_3.py |
| TC-SET-6184 | P2 | Valid update EXPORT_RETENTION_DAYS = 25 | key=EXPORT_RETENTION_DAYS,value=25 | accepted | test_settings_phase2_part_3.py |
| TC-SET-6185 | P2 | Valid update EXPORT_RETENTION_DAYS = 50 | key=EXPORT_RETENTION_DAYS,value=50 | accepted | test_settings_phase2_part_3.py |
| TC-SET-6186 | P2 | Valid update EXPORT_RETENTION_DAYS = 100 | key=EXPORT_RETENTION_DAYS,value=100 | accepted | test_settings_phase2_part_3.py |
| TC-SET-6187 | P2 | Valid update EXPORT_RETENTION_DAYS = 250 | key=EXPORT_RETENTION_DAYS,value=250 | accepted | test_settings_phase2_part_3.py |
| TC-SET-6188 | P2 | Valid update FORCE_LLM_ON_SEMANTIC_HIGH = True | key=FORCE_LLM_ON_SEMANTIC_HIGH,value=True | accepted | test_settings_phase2_part_3.py |
| TC-SET-6189 | P2 | Valid update FORCE_LLM_ON_SEMANTIC_HIGH = False | key=FORCE_LLM_ON_SEMANTIC_HIGH,value=False | accepted | test_settings_phase2_part_3.py |
| TC-SET-6190 | P2 | Valid update FORCE_LLM_ON_USER_RATIO_HIGH = True | key=FORCE_LLM_ON_USER_RATIO_HIGH,value=True | accepted | test_settings_phase2_part_3.py |
| TC-SET-6191 | P2 | Valid update FORCE_LLM_ON_USER_RATIO_HIGH = False | key=FORCE_LLM_ON_USER_RATIO_HIGH,value=False | accepted | test_settings_phase2_part_3.py |
| TC-SET-6192 | P2 | Valid update FRONTEND_DIST_PATH = sample-value | key=FRONTEND_DIST_PATH,value='sample-value' | accepted | test_settings_phase2_part_3.py |
| TC-SET-6193 | P2 | Valid update FRONTEND_DIST_PATH = config-value | key=FRONTEND_DIST_PATH,value='config-value' | accepted | test_settings_phase2_part_3.py |
| TC-SET-6194 | P2 | Valid update FRONTEND_DIST_PATH = 192.168.0.1 | key=FRONTEND_DIST_PATH,value='192.168.0.1' | accepted | test_settings_phase2_part_3.py |
| TC-SET-6195 | P2 | Valid update FUZZY_MAX_DISTANCE = sample-value | key=FUZZY_MAX_DISTANCE,value='sample-value' | accepted | test_settings_phase2_part_3.py |
| TC-SET-6196 | P2 | Valid update FUZZY_MAX_DISTANCE = config-value | key=FUZZY_MAX_DISTANCE,value='config-value' | accepted | test_settings_phase2_part_3.py |
| TC-SET-6197 | P2 | Valid update FUZZY_MAX_DISTANCE = 192.168.0.1 | key=FUZZY_MAX_DISTANCE,value='192.168.0.1' | accepted | test_settings_phase2_part_3.py |
| TC-SET-6198 | P2 | Valid update HF_ENDPOINT = sample-value | key=HF_ENDPOINT,value='sample-value' | accepted | test_settings_phase2_part_3.py |
| TC-SET-6199 | P2 | Valid update HF_ENDPOINT = config-value | key=HF_ENDPOINT,value='config-value' | accepted | test_settings_phase2_part_3.py |
| TC-SET-6200 | P2 | Valid update HF_ENDPOINT = 192.168.0.1 | key=HF_ENDPOINT,value='192.168.0.1' | accepted | test_settings_phase2_part_3.py |
| TC-SET-6411 | P2 | Invalid update AI_TARGET_PERCENTAGE = -5 | key=AI_TARGET_PERCENTAGE,value=-5 | rejected | test_settings_phase2_part_4.py |
| TC-SET-6412 | P2 | Invalid update AI_TARGET_PERCENTAGE = -1 | key=AI_TARGET_PERCENTAGE,value=-1 | rejected | test_settings_phase2_part_4.py |
| TC-SET-6413 | P2 | Invalid update AI_TARGET_PERCENTAGE = 1000000000 | key=AI_TARGET_PERCENTAGE,value=1000000000 | rejected | test_settings_phase2_part_4.py |
| TC-SET-6414 | P2 | Invalid update AI_TARGET_PERCENTAGE = 'not-a-number' | key=AI_TARGET_PERCENTAGE,value='not-a-number' | rejected | test_settings_phase2_part_4.py |
| TC-SET-6415 | P2 | Invalid update ALLOWED_ORIGINS = '' | key=ALLOWED_ORIGINS,value='' | rejected | test_settings_phase2_part_4.py |
| TC-SET-6416 | P2 | Invalid update APP_CONFIG_DB_PATH = '' | key=APP_CONFIG_DB_PATH,value='' | rejected | test_settings_phase2_part_4.py |
| TC-SET-6417 | P2 | Invalid update APP_HOST = '' | key=APP_HOST,value='' | rejected | test_settings_phase2_part_4.py |
| TC-SET-6418 | P2 | Invalid update AUTO_TUNING_BATCH_HOUR = -5 | key=AUTO_TUNING_BATCH_HOUR,value=-5 | rejected | test_settings_phase2_part_4.py |
| TC-SET-6419 | P2 | Invalid update AUTO_TUNING_BATCH_HOUR = -1 | key=AUTO_TUNING_BATCH_HOUR,value=-1 | rejected | test_settings_phase2_part_4.py |
| TC-SET-6420 | P2 | Invalid update AUTO_TUNING_BATCH_HOUR = 1000000000 | key=AUTO_TUNING_BATCH_HOUR,value=1000000000 | rejected | test_settings_phase2_part_4.py |
| TC-SET-6421 | P2 | Invalid update AUTO_TUNING_BATCH_HOUR = 'not-a-number' | key=AUTO_TUNING_BATCH_HOUR,value='not-a-number' | rejected | test_settings_phase2_part_4.py |
| TC-SET-6422 | P2 | Invalid update AUTO_TUNING_ENABLED = 'maybe' | key=AUTO_TUNING_ENABLED,value='maybe' | rejected | test_settings_phase2_part_4.py |
| TC-SET-6423 | P2 | Invalid update AUTO_TUNING_ENABLED = 'bogus' | key=AUTO_TUNING_ENABLED,value='bogus' | rejected | test_settings_phase2_part_4.py |
| TC-SET-6424 | P2 | Invalid update AUTO_TUNING_ENABLED = 5 | key=AUTO_TUNING_ENABLED,value=5 | rejected | test_settings_phase2_part_4.py |
| TC-SET-6425 | P2 | Invalid update AUTO_TUNING_ENABLED = 'not-bool' | key=AUTO_TUNING_ENABLED,value='not-bool' | rejected | test_settings_phase2_part_4.py |
| TC-SET-6426 | P2 | Invalid update BLOOM_FILTER_CAPACITY = '' | key=BLOOM_FILTER_CAPACITY,value='' | rejected | test_settings_phase2_part_4.py |
| TC-SET-6427 | P2 | Invalid update BLOOM_FILTER_ERROR_RATE = '' | key=BLOOM_FILTER_ERROR_RATE,value='' | rejected | test_settings_phase2_part_4.py |
| TC-SET-6428 | P2 | Invalid update CACHE_MAX_SIZE = -5 | key=CACHE_MAX_SIZE,value=-5 | rejected | test_settings_phase2_part_4.py |
| TC-SET-6429 | P2 | Invalid update CACHE_MAX_SIZE = -1 | key=CACHE_MAX_SIZE,value=-1 | rejected | test_settings_phase2_part_4.py |
| TC-SET-6430 | P2 | Invalid update CACHE_MAX_SIZE = 0 | key=CACHE_MAX_SIZE,value=0 | rejected | test_settings_phase2_part_4.py |
| TC-SET-6431 | P2 | Invalid update CACHE_MAX_SIZE = 1000000000 | key=CACHE_MAX_SIZE,value=1000000000 | rejected | test_settings_phase2_part_4.py |
| TC-SET-6432 | P2 | Invalid update CACHE_MAX_SIZE = 'not-a-number' | key=CACHE_MAX_SIZE,value='not-a-number' | rejected | test_settings_phase2_part_4.py |
| TC-SET-6433 | P2 | Invalid update CACHE_TTL_SECONDS = -5 | key=CACHE_TTL_SECONDS,value=-5 | rejected | test_settings_phase2_part_4.py |
| TC-SET-6434 | P2 | Invalid update CACHE_TTL_SECONDS = -1 | key=CACHE_TTL_SECONDS,value=-1 | rejected | test_settings_phase2_part_4.py |
| TC-SET-6435 | P2 | Invalid update CACHE_TTL_SECONDS = 0 | key=CACHE_TTL_SECONDS,value=0 | rejected | test_settings_phase2_part_4.py |
| TC-SET-6436 | P2 | Invalid update CACHE_TTL_SECONDS = 1000000000 | key=CACHE_TTL_SECONDS,value=1000000000 | rejected | test_settings_phase2_part_4.py |
| TC-SET-6437 | P2 | Invalid update CACHE_TTL_SECONDS = 'not-a-number' | key=CACHE_TTL_SECONDS,value='not-a-number' | rejected | test_settings_phase2_part_4.py |
| TC-SET-6438 | P2 | Invalid update CRITICAL_PHRASES_DB_PATH = '' | key=CRITICAL_PHRASES_DB_PATH,value='' | rejected | test_settings_phase2_part_4.py |
| TC-SET-6439 | P2 | Invalid update CUSTOM_WORDS_PATH = '' | key=CUSTOM_WORDS_PATH,value='' | rejected | test_settings_phase2_part_4.py |
| TC-SET-6440 | P2 | Invalid update CUSTOM_WORDS_STORAGE = '' | key=CUSTOM_WORDS_STORAGE,value='' | rejected | test_settings_phase2_part_4.py |
| TC-SET-6441 | P2 | Invalid update DETECTOR_THREAD_POOL_SIZE = -5 | key=DETECTOR_THREAD_POOL_SIZE,value=-5 | rejected | test_settings_phase2_part_4.py |
| TC-SET-6442 | P2 | Invalid update DETECTOR_THREAD_POOL_SIZE = -1 | key=DETECTOR_THREAD_POOL_SIZE,value=-1 | rejected | test_settings_phase2_part_4.py |
| TC-SET-6443 | P2 | Invalid update DETECTOR_THREAD_POOL_SIZE = 0 | key=DETECTOR_THREAD_POOL_SIZE,value=0 | rejected | test_settings_phase2_part_4.py |
| TC-SET-6444 | P2 | Invalid update DETECTOR_THREAD_POOL_SIZE = 1000000000 | key=DETECTOR_THREAD_POOL_SIZE,value=1000000000 | rejected | test_settings_phase2_part_4.py |
| TC-SET-6445 | P2 | Invalid update DETECTOR_THREAD_POOL_SIZE = 'not-a-number' | key=DETECTOR_THREAD_POOL_SIZE,value='not-a-number' | rejected | test_settings_phase2_part_4.py |
| TC-SET-6446 | P2 | Invalid update ENABLE_BADWORDS_PY = 'maybe' | key=ENABLE_BADWORDS_PY,value='maybe' | rejected | test_settings_phase2_part_4.py |
| TC-SET-6447 | P2 | Invalid update ENABLE_BADWORDS_PY = 'bogus' | key=ENABLE_BADWORDS_PY,value='bogus' | rejected | test_settings_phase2_part_4.py |
| TC-SET-6448 | P2 | Invalid update ENABLE_BADWORDS_PY = 5 | key=ENABLE_BADWORDS_PY,value=5 | rejected | test_settings_phase2_part_4.py |
| TC-SET-6449 | P2 | Invalid update ENABLE_BADWORDS_PY = 'not-bool' | key=ENABLE_BADWORDS_PY,value='not-bool' | rejected | test_settings_phase2_part_4.py |
| TC-SET-6450 | P2 | Invalid update ENABLE_DETECTOR_AHO_CORASICK = 'maybe' | key=ENABLE_DETECTOR_AHO_CORASICK,value='maybe' | rejected | test_settings_phase2_part_4.py |
| TC-SET-6451 | P2 | Invalid update ENABLE_DETECTOR_AHO_CORASICK = 'bogus' | key=ENABLE_DETECTOR_AHO_CORASICK,value='bogus' | rejected | test_settings_phase2_part_4.py |
| TC-SET-6452 | P2 | Invalid update ENABLE_DETECTOR_AHO_CORASICK = 5 | key=ENABLE_DETECTOR_AHO_CORASICK,value=5 | rejected | test_settings_phase2_part_4.py |
| TC-SET-6453 | P2 | Invalid update ENABLE_DETECTOR_AHO_CORASICK = 'not-bool' | key=ENABLE_DETECTOR_AHO_CORASICK,value='not-bool' | rejected | test_settings_phase2_part_4.py |
| TC-SET-6454 | P2 | Invalid update ENABLE_DETECTOR_BK_TREE = 'maybe' | key=ENABLE_DETECTOR_BK_TREE,value='maybe' | rejected | test_settings_phase2_part_4.py |
| TC-SET-6455 | P2 | Invalid update ENABLE_DETECTOR_BK_TREE = 'bogus' | key=ENABLE_DETECTOR_BK_TREE,value='bogus' | rejected | test_settings_phase2_part_4.py |
| TC-SET-6456 | P2 | Invalid update ENABLE_DETECTOR_BK_TREE = 5 | key=ENABLE_DETECTOR_BK_TREE,value=5 | rejected | test_settings_phase2_part_4.py |
| TC-SET-6457 | P2 | Invalid update ENABLE_DETECTOR_BK_TREE = 'not-bool' | key=ENABLE_DETECTOR_BK_TREE,value='not-bool' | rejected | test_settings_phase2_part_4.py |
| TC-SET-6458 | P2 | Invalid update ENABLE_DETECTOR_BLOOM_FILTER = 'maybe' | key=ENABLE_DETECTOR_BLOOM_FILTER,value='maybe' | rejected | test_settings_phase2_part_4.py |
| TC-SET-6459 | P2 | Invalid update ENABLE_DETECTOR_BLOOM_FILTER = 'bogus' | key=ENABLE_DETECTOR_BLOOM_FILTER,value='bogus' | rejected | test_settings_phase2_part_4.py |
| TC-SET-6460 | P2 | Invalid update ENABLE_DETECTOR_BLOOM_FILTER = 5 | key=ENABLE_DETECTOR_BLOOM_FILTER,value=5 | rejected | test_settings_phase2_part_4.py |
| TC-SET-6461 | P2 | Invalid update ENABLE_DETECTOR_BLOOM_FILTER = 'not-bool' | key=ENABLE_DETECTOR_BLOOM_FILTER,value='not-bool' | rejected | test_settings_phase2_part_4.py |
| TC-SET-6462 | P2 | Invalid update ENABLE_DETECTOR_DOUBLE_METAPHONE = 'maybe' | key=ENABLE_DETECTOR_DOUBLE_METAPHONE,value='maybe' | rejected | test_settings_phase2_part_4.py |
| TC-SET-6463 | P2 | Invalid update ENABLE_DETECTOR_DOUBLE_METAPHONE = 'bogus' | key=ENABLE_DETECTOR_DOUBLE_METAPHONE,value='bogus' | rejected | test_settings_phase2_part_4.py |
| TC-SET-6464 | P2 | Invalid update ENABLE_DETECTOR_DOUBLE_METAPHONE = 5 | key=ENABLE_DETECTOR_DOUBLE_METAPHONE,value=5 | rejected | test_settings_phase2_part_4.py |
| TC-SET-6465 | P2 | Invalid update ENABLE_DETECTOR_DOUBLE_METAPHONE = 'not-bool' | key=ENABLE_DETECTOR_DOUBLE_METAPHONE,value='not-bool' | rejected | test_settings_phase2_part_4.py |
| TC-SET-6466 | P2 | Invalid update ENABLE_DETECTOR_MULTI_LANGUAGE = 'maybe' | key=ENABLE_DETECTOR_MULTI_LANGUAGE,value='maybe' | rejected | test_settings_phase2_part_4.py |
| TC-SET-6467 | P2 | Invalid update ENABLE_DETECTOR_MULTI_LANGUAGE = 'bogus' | key=ENABLE_DETECTOR_MULTI_LANGUAGE,value='bogus' | rejected | test_settings_phase2_part_4.py |
| TC-SET-6468 | P2 | Invalid update ENABLE_DETECTOR_MULTI_LANGUAGE = 5 | key=ENABLE_DETECTOR_MULTI_LANGUAGE,value=5 | rejected | test_settings_phase2_part_4.py |
| TC-SET-6469 | P2 | Invalid update ENABLE_DETECTOR_MULTI_LANGUAGE = 'not-bool' | key=ENABLE_DETECTOR_MULTI_LANGUAGE,value='not-bool' | rejected | test_settings_phase2_part_4.py |
| TC-SET-6470 | P2 | Invalid update ENABLE_DETECTOR_ROLLING_HASH = 'maybe' | key=ENABLE_DETECTOR_ROLLING_HASH,value='maybe' | rejected | test_settings_phase2_part_4.py |
| TC-SET-6471 | P2 | Invalid update ENABLE_DETECTOR_ROLLING_HASH = 'bogus' | key=ENABLE_DETECTOR_ROLLING_HASH,value='bogus' | rejected | test_settings_phase2_part_4.py |
| TC-SET-6472 | P2 | Invalid update ENABLE_DETECTOR_ROLLING_HASH = 5 | key=ENABLE_DETECTOR_ROLLING_HASH,value=5 | rejected | test_settings_phase2_part_4.py |
| TC-SET-6473 | P2 | Invalid update ENABLE_DETECTOR_ROLLING_HASH = 'not-bool' | key=ENABLE_DETECTOR_ROLLING_HASH,value='not-bool' | rejected | test_settings_phase2_part_4.py |
| TC-SET-6474 | P2 | Invalid update ENABLE_GANGAJAL = 'maybe' | key=ENABLE_GANGAJAL,value='maybe' | rejected | test_settings_phase2_part_4.py |
| TC-SET-6475 | P2 | Invalid update ENABLE_GANGAJAL = 'bogus' | key=ENABLE_GANGAJAL,value='bogus' | rejected | test_settings_phase2_part_4.py |
| TC-SET-6476 | P2 | Invalid update ENABLE_GANGAJAL = 5 | key=ENABLE_GANGAJAL,value=5 | rejected | test_settings_phase2_part_4.py |
| TC-SET-6477 | P2 | Invalid update ENABLE_GANGAJAL = 'not-bool' | key=ENABLE_GANGAJAL,value='not-bool' | rejected | test_settings_phase2_part_4.py |
| TC-SET-6478 | P2 | Invalid update ENABLE_GLIN_PROFANITY = 'maybe' | key=ENABLE_GLIN_PROFANITY,value='maybe' | rejected | test_settings_phase2_part_4.py |
| TC-SET-6479 | P2 | Invalid update ENABLE_GLIN_PROFANITY = 'bogus' | key=ENABLE_GLIN_PROFANITY,value='bogus' | rejected | test_settings_phase2_part_4.py |
| TC-SET-6480 | P2 | Invalid update ENABLE_GLIN_PROFANITY = 5 | key=ENABLE_GLIN_PROFANITY,value=5 | rejected | test_settings_phase2_part_4.py |
| TC-SET-6481 | P2 | Invalid update ENABLE_GLIN_PROFANITY = 'not-bool' | key=ENABLE_GLIN_PROFANITY,value='not-bool' | rejected | test_settings_phase2_part_4.py |
| TC-SET-6482 | P2 | Invalid update ENABLE_PHRASE_DETECTOR = 'maybe' | key=ENABLE_PHRASE_DETECTOR,value='maybe' | rejected | test_settings_phase2_part_4.py |
| TC-SET-6483 | P2 | Invalid update ENABLE_PHRASE_DETECTOR = 'bogus' | key=ENABLE_PHRASE_DETECTOR,value='bogus' | rejected | test_settings_phase2_part_4.py |
| TC-SET-6484 | P2 | Invalid update ENABLE_PHRASE_DETECTOR = 5 | key=ENABLE_PHRASE_DETECTOR,value=5 | rejected | test_settings_phase2_part_4.py |
| TC-SET-6485 | P2 | Invalid update ENABLE_PHRASE_DETECTOR = 'not-bool' | key=ENABLE_PHRASE_DETECTOR,value='not-bool' | rejected | test_settings_phase2_part_4.py |
| TC-SET-6486 | P2 | Invalid update ENABLE_PROFANITE = 'maybe' | key=ENABLE_PROFANITE,value='maybe' | rejected | test_settings_phase2_part_4.py |
| TC-SET-6487 | P2 | Invalid update ENABLE_PROFANITE = 'bogus' | key=ENABLE_PROFANITE,value='bogus' | rejected | test_settings_phase2_part_4.py |
| TC-SET-6488 | P2 | Invalid update ENABLE_PROFANITE = 5 | key=ENABLE_PROFANITE,value=5 | rejected | test_settings_phase2_part_4.py |
| TC-SET-6489 | P2 | Invalid update ENABLE_PROFANITE = 'not-bool' | key=ENABLE_PROFANITE,value='not-bool' | rejected | test_settings_phase2_part_4.py |
| TC-SET-6490 | P2 | Invalid update ENABLE_PROFANITY_FILTER = 'maybe' | key=ENABLE_PROFANITY_FILTER,value='maybe' | rejected | test_settings_phase2_part_4.py |
| TC-SET-6491 | P2 | Invalid update ENABLE_PROFANITY_FILTER = 'bogus' | key=ENABLE_PROFANITY_FILTER,value='bogus' | rejected | test_settings_phase2_part_4.py |
| TC-SET-6492 | P2 | Invalid update ENABLE_PROFANITY_FILTER = 5 | key=ENABLE_PROFANITY_FILTER,value=5 | rejected | test_settings_phase2_part_4.py |
| TC-SET-6493 | P2 | Invalid update ENABLE_PROFANITY_FILTER = 'not-bool' | key=ENABLE_PROFANITY_FILTER,value='not-bool' | rejected | test_settings_phase2_part_4.py |
| TC-SET-6494 | P2 | Invalid update ENABLE_PYPROFANE = 'maybe' | key=ENABLE_PYPROFANE,value='maybe' | rejected | test_settings_phase2_part_4.py |
| TC-SET-6495 | P2 | Invalid update ENABLE_PYPROFANE = 'bogus' | key=ENABLE_PYPROFANE,value='bogus' | rejected | test_settings_phase2_part_4.py |
| TC-SET-6496 | P2 | Invalid update ENABLE_PYPROFANE = 5 | key=ENABLE_PYPROFANE,value=5 | rejected | test_settings_phase2_part_4.py |
| TC-SET-6497 | P2 | Invalid update ENABLE_PYPROFANE = 'not-bool' | key=ENABLE_PYPROFANE,value='not-bool' | rejected | test_settings_phase2_part_4.py |
| TC-SET-6498 | P2 | Invalid update ENABLE_SAFETEXT = 'maybe' | key=ENABLE_SAFETEXT,value='maybe' | rejected | test_settings_phase2_part_4.py |
| TC-SET-6499 | P2 | Invalid update ENABLE_SAFETEXT = 'bogus' | key=ENABLE_SAFETEXT,value='bogus' | rejected | test_settings_phase2_part_4.py |
| TC-SET-6500 | P2 | Invalid update ENABLE_SAFETEXT = 5 | key=ENABLE_SAFETEXT,value=5 | rejected | test_settings_phase2_part_4.py |
| TC-SET-6501 | P2 | Invalid update ENABLE_SAFETEXT = 'not-bool' | key=ENABLE_SAFETEXT,value='not-bool' | rejected | test_settings_phase2_part_4.py |
| TC-SET-6502 | P2 | Invalid update ENABLE_SENSITIVE_STOP_WORDS = 'maybe' | key=ENABLE_SENSITIVE_STOP_WORDS,value='maybe' | rejected | test_settings_phase2_part_4.py |
| TC-SET-6503 | P2 | Invalid update ENABLE_SENSITIVE_STOP_WORDS = 'bogus' | key=ENABLE_SENSITIVE_STOP_WORDS,value='bogus' | rejected | test_settings_phase2_part_4.py |
| TC-SET-6504 | P2 | Invalid update ENABLE_SENSITIVE_STOP_WORDS = 5 | key=ENABLE_SENSITIVE_STOP_WORDS,value=5 | rejected | test_settings_phase2_part_4.py |
| TC-SET-6505 | P2 | Invalid update ENABLE_SENSITIVE_STOP_WORDS = 'not-bool' | key=ENABLE_SENSITIVE_STOP_WORDS,value='not-bool' | rejected | test_settings_phase2_part_4.py |
| TC-SET-6506 | P2 | Invalid update ENABLE_SENSITIVE_STOP_WORDS_AD = 'maybe' | key=ENABLE_SENSITIVE_STOP_WORDS_AD,value='maybe' | rejected | test_settings_phase2_part_4.py |
| TC-SET-6507 | P2 | Invalid update ENABLE_SENSITIVE_STOP_WORDS_AD = 'bogus' | key=ENABLE_SENSITIVE_STOP_WORDS_AD,value='bogus' | rejected | test_settings_phase2_part_4.py |
| TC-SET-6508 | P2 | Invalid update ENABLE_SENSITIVE_STOP_WORDS_AD = 5 | key=ENABLE_SENSITIVE_STOP_WORDS_AD,value=5 | rejected | test_settings_phase2_part_4.py |
| TC-SET-6509 | P2 | Invalid update ENABLE_SENSITIVE_STOP_WORDS_AD = 'not-bool' | key=ENABLE_SENSITIVE_STOP_WORDS_AD,value='not-bool' | rejected | test_settings_phase2_part_4.py |
| TC-SET-6510 | P2 | Invalid update ENABLE_SENSITIVE_STOP_WORDS_GUN = 'maybe' | key=ENABLE_SENSITIVE_STOP_WORDS_GUN,value='maybe' | rejected | test_settings_phase2_part_4.py |
| TC-SET-6511 | P2 | Invalid update ENABLE_SENSITIVE_STOP_WORDS_GUN = 'bogus' | key=ENABLE_SENSITIVE_STOP_WORDS_GUN,value='bogus' | rejected | test_settings_phase2_part_5.py |
| TC-SET-6512 | P2 | Invalid update ENABLE_SENSITIVE_STOP_WORDS_GUN = 5 | key=ENABLE_SENSITIVE_STOP_WORDS_GUN,value=5 | rejected | test_settings_phase2_part_5.py |
| TC-SET-6513 | P2 | Invalid update ENABLE_SENSITIVE_STOP_WORDS_GUN = 'not-bool' | key=ENABLE_SENSITIVE_STOP_WORDS_GUN,value='not-bool' | rejected | test_settings_phase2_part_5.py |
| TC-SET-6514 | P2 | Invalid update ENABLE_SENSITIVE_STOP_WORDS_POLITICAL = 'maybe' | key=ENABLE_SENSITIVE_STOP_WORDS_POLITICAL,value='maybe' | rejected | test_settings_phase2_part_5.py |
| TC-SET-6515 | P2 | Invalid update ENABLE_SENSITIVE_STOP_WORDS_POLITICAL = 'bogus' | key=ENABLE_SENSITIVE_STOP_WORDS_POLITICAL,value='bogus' | rejected | test_settings_phase2_part_5.py |
| TC-SET-6516 | P2 | Invalid update ENABLE_SENSITIVE_STOP_WORDS_POLITICAL = 5 | key=ENABLE_SENSITIVE_STOP_WORDS_POLITICAL,value=5 | rejected | test_settings_phase2_part_5.py |
| TC-SET-6517 | P2 | Invalid update ENABLE_SENSITIVE_STOP_WORDS_POLITICAL = 'not-bool' | key=ENABLE_SENSITIVE_STOP_WORDS_POLITICAL,value='not-bool' | rejected | test_settings_phase2_part_5.py |
| TC-SET-6518 | P2 | Invalid update ENABLE_SENSITIVE_STOP_WORDS_PORN = 'maybe' | key=ENABLE_SENSITIVE_STOP_WORDS_PORN,value='maybe' | rejected | test_settings_phase2_part_5.py |
| TC-SET-6519 | P2 | Invalid update ENABLE_SENSITIVE_STOP_WORDS_PORN = 'bogus' | key=ENABLE_SENSITIVE_STOP_WORDS_PORN,value='bogus' | rejected | test_settings_phase2_part_5.py |
| TC-SET-6520 | P2 | Invalid update ENABLE_SENSITIVE_STOP_WORDS_PORN = 5 | key=ENABLE_SENSITIVE_STOP_WORDS_PORN,value=5 | rejected | test_settings_phase2_part_5.py |
| TC-SET-6521 | P2 | Invalid update ENABLE_SENSITIVE_STOP_WORDS_PORN = 'not-bool' | key=ENABLE_SENSITIVE_STOP_WORDS_PORN,value='not-bool' | rejected | test_settings_phase2_part_5.py |
| TC-SET-6522 | P2 | Invalid update ENABLE_SENSITIVE_STOP_WORDS_URL = 'maybe' | key=ENABLE_SENSITIVE_STOP_WORDS_URL,value='maybe' | rejected | test_settings_phase2_part_5.py |
| TC-SET-6523 | P2 | Invalid update ENABLE_SENSITIVE_STOP_WORDS_URL = 'bogus' | key=ENABLE_SENSITIVE_STOP_WORDS_URL,value='bogus' | rejected | test_settings_phase2_part_5.py |
| TC-SET-6524 | P2 | Invalid update ENABLE_SENSITIVE_STOP_WORDS_URL = 5 | key=ENABLE_SENSITIVE_STOP_WORDS_URL,value=5 | rejected | test_settings_phase2_part_5.py |
| TC-SET-6525 | P2 | Invalid update ENABLE_SENSITIVE_STOP_WORDS_URL = 'not-bool' | key=ENABLE_SENSITIVE_STOP_WORDS_URL,value='not-bool' | rejected | test_settings_phase2_part_5.py |
| TC-SET-6526 | P2 | Invalid update ENABLE_SENSITIVE_WORD_FILTER_CN = 'maybe' | key=ENABLE_SENSITIVE_WORD_FILTER_CN,value='maybe' | rejected | test_settings_phase2_part_5.py |
| TC-SET-6527 | P2 | Invalid update ENABLE_SENSITIVE_WORD_FILTER_CN = 'bogus' | key=ENABLE_SENSITIVE_WORD_FILTER_CN,value='bogus' | rejected | test_settings_phase2_part_5.py |
| TC-SET-6528 | P2 | Invalid update ENABLE_SENSITIVE_WORD_FILTER_CN = 5 | key=ENABLE_SENSITIVE_WORD_FILTER_CN,value=5 | rejected | test_settings_phase2_part_5.py |
| TC-SET-6529 | P2 | Invalid update ENABLE_SENSITIVE_WORD_FILTER_CN = 'not-bool' | key=ENABLE_SENSITIVE_WORD_FILTER_CN,value='not-bool' | rejected | test_settings_phase2_part_5.py |
| TC-SET-6530 | P2 | Invalid update EXPORT_RETENTION_DAYS = -5 | key=EXPORT_RETENTION_DAYS,value=-5 | rejected | test_settings_phase2_part_5.py |
| TC-SET-6531 | P2 | Invalid update EXPORT_RETENTION_DAYS = -1 | key=EXPORT_RETENTION_DAYS,value=-1 | rejected | test_settings_phase2_part_5.py |
| TC-SET-6532 | P2 | Invalid update EXPORT_RETENTION_DAYS = 0 | key=EXPORT_RETENTION_DAYS,value=0 | rejected | test_settings_phase2_part_5.py |
| TC-SET-6533 | P2 | Invalid update EXPORT_RETENTION_DAYS = 1000000000 | key=EXPORT_RETENTION_DAYS,value=1000000000 | rejected | test_settings_phase2_part_5.py |
| TC-SET-6534 | P2 | Invalid update EXPORT_RETENTION_DAYS = 'not-a-number' | key=EXPORT_RETENTION_DAYS,value='not-a-number' | rejected | test_settings_phase2_part_5.py |
| TC-SET-6535 | P2 | Invalid update FORCE_LLM_ON_SEMANTIC_HIGH = 'maybe' | key=FORCE_LLM_ON_SEMANTIC_HIGH,value='maybe' | rejected | test_settings_phase2_part_5.py |
| TC-SET-6536 | P2 | Invalid update FORCE_LLM_ON_SEMANTIC_HIGH = 'bogus' | key=FORCE_LLM_ON_SEMANTIC_HIGH,value='bogus' | rejected | test_settings_phase2_part_5.py |
| TC-SET-6537 | P2 | Invalid update FORCE_LLM_ON_SEMANTIC_HIGH = 5 | key=FORCE_LLM_ON_SEMANTIC_HIGH,value=5 | rejected | test_settings_phase2_part_5.py |
| TC-SET-6538 | P2 | Invalid update FORCE_LLM_ON_SEMANTIC_HIGH = 'not-bool' | key=FORCE_LLM_ON_SEMANTIC_HIGH,value='not-bool' | rejected | test_settings_phase2_part_5.py |
| TC-SET-6539 | P2 | Invalid update FORCE_LLM_ON_USER_RATIO_HIGH = 'maybe' | key=FORCE_LLM_ON_USER_RATIO_HIGH,value='maybe' | rejected | test_settings_phase2_part_5.py |
| TC-SET-6540 | P2 | Invalid update FORCE_LLM_ON_USER_RATIO_HIGH = 'bogus' | key=FORCE_LLM_ON_USER_RATIO_HIGH,value='bogus' | rejected | test_settings_phase2_part_5.py |
| TC-SET-6541 | P2 | Invalid update FORCE_LLM_ON_USER_RATIO_HIGH = 5 | key=FORCE_LLM_ON_USER_RATIO_HIGH,value=5 | rejected | test_settings_phase2_part_5.py |
| TC-SET-6542 | P2 | Invalid update FORCE_LLM_ON_USER_RATIO_HIGH = 'not-bool' | key=FORCE_LLM_ON_USER_RATIO_HIGH,value='not-bool' | rejected | test_settings_phase2_part_5.py |
| TC-SET-6543 | P2 | Invalid update FRONTEND_DIST_PATH = '' | key=FRONTEND_DIST_PATH,value='' | rejected | test_settings_phase2_part_5.py |
| TC-SET-6544 | P2 | Invalid update FUZZY_MAX_DISTANCE = '' | key=FUZZY_MAX_DISTANCE,value='' | rejected | test_settings_phase2_part_5.py |
| TC-SET-6545 | P2 | Invalid update HF_ENDPOINT = '' | key=HF_ENDPOINT,value='' | rejected | test_settings_phase2_part_5.py |
| TC-SET-6546 | P2 | Invalid update HF_MIRROR = '' | key=HF_MIRROR,value='' | rejected | test_settings_phase2_part_5.py |
| TC-SET-6547 | P2 | Invalid update LLM_RESPONSE_TIMEOUT_SECONDS = -5 | key=LLM_RESPONSE_TIMEOUT_SECONDS,value=-5 | rejected | test_settings_phase2_part_5.py |
| TC-SET-6548 | P2 | Invalid update LLM_RESPONSE_TIMEOUT_SECONDS = -1 | key=LLM_RESPONSE_TIMEOUT_SECONDS,value=-1 | rejected | test_settings_phase2_part_5.py |
| TC-SET-6549 | P2 | Invalid update LLM_RESPONSE_TIMEOUT_SECONDS = 0 | key=LLM_RESPONSE_TIMEOUT_SECONDS,value=0 | rejected | test_settings_phase2_part_5.py |
| TC-SET-6550 | P2 | Invalid update LLM_RESPONSE_TIMEOUT_SECONDS = 1000000000 | key=LLM_RESPONSE_TIMEOUT_SECONDS,value=1000000000 | rejected | test_settings_phase2_part_5.py |
| TC-SET-6551 | P2 | Invalid update LLM_RESPONSE_TIMEOUT_SECONDS = 'not-a-number' | key=LLM_RESPONSE_TIMEOUT_SECONDS,value='not-a-number' | rejected | test_settings_phase2_part_5.py |
| TC-SET-6552 | P2 | Invalid update LOG_BACKUP_COUNT = -5 | key=LOG_BACKUP_COUNT,value=-5 | rejected | test_settings_phase2_part_5.py |
| TC-SET-6553 | P2 | Invalid update LOG_BACKUP_COUNT = -1 | key=LOG_BACKUP_COUNT,value=-1 | rejected | test_settings_phase2_part_5.py |
| TC-SET-6554 | P2 | Invalid update LOG_BACKUP_COUNT = 1000000000 | key=LOG_BACKUP_COUNT,value=1000000000 | rejected | test_settings_phase2_part_5.py |
| TC-SET-6555 | P2 | Invalid update LOG_BACKUP_COUNT = 'not-a-number' | key=LOG_BACKUP_COUNT,value='not-a-number' | rejected | test_settings_phase2_part_5.py |
| TC-SET-6556 | P2 | Invalid update LOG_FILE_PATH = '' | key=LOG_FILE_PATH,value='' | rejected | test_settings_phase2_part_5.py |
| TC-SET-6557 | P2 | Invalid update LOG_LEVEL = '' | key=LOG_LEVEL,value='' | rejected | test_settings_phase2_part_5.py |
| TC-SET-6558 | P2 | Invalid update LOG_MAX_BYTES = -5 | key=LOG_MAX_BYTES,value=-5 | rejected | test_settings_phase2_part_5.py |
| TC-SET-6559 | P2 | Invalid update LOG_MAX_BYTES = -1 | key=LOG_MAX_BYTES,value=-1 | rejected | test_settings_phase2_part_5.py |
| TC-SET-6560 | P2 | Invalid update LOG_MAX_BYTES = 0 | key=LOG_MAX_BYTES,value=0 | rejected | test_settings_phase2_part_5.py |
| TC-SET-6788 | P2 | Coercion SAFE_WORD_ENABLED 'true' #0 | key=SAFE_WORD_ENABLED,raw=true | coerced=True | test_settings_phase2_part_5.py |
| TC-SET-6789 | P2 | Coercion SAFE_WORD_ENABLED 'true' #1 | key=SAFE_WORD_ENABLED,raw=true | coerced=True | test_settings_phase2_part_5.py |
| TC-SET-6790 | P2 | Coercion SAFE_WORD_ENABLED 'true' #2 | key=SAFE_WORD_ENABLED,raw=true | coerced=True | test_settings_phase2_part_5.py |
| TC-SET-6791 | P2 | Coercion SAFE_WORD_ENABLED 'true' #3 | key=SAFE_WORD_ENABLED,raw=true | coerced=True | test_settings_phase2_part_5.py |
| TC-SET-6792 | P2 | Coercion SAFE_WORD_ENABLED 'true' #4 | key=SAFE_WORD_ENABLED,raw=true | coerced=True | test_settings_phase2_part_5.py |
| TC-SET-6793 | P2 | Coercion SAFE_WORD_ENABLED 'true' #5 | key=SAFE_WORD_ENABLED,raw=true | coerced=True | test_settings_phase2_part_5.py |
| TC-SET-6794 | P2 | Coercion SAFE_WORD_ENABLED 'true' #6 | key=SAFE_WORD_ENABLED,raw=true | coerced=True | test_settings_phase2_part_5.py |
| TC-SET-6795 | P2 | Coercion SAFE_WORD_ENABLED 'true' #7 | key=SAFE_WORD_ENABLED,raw=true | coerced=True | test_settings_phase2_part_5.py |
| TC-SET-6796 | P2 | Coercion SAFE_WORD_ENABLED 'true' #8 | key=SAFE_WORD_ENABLED,raw=true | coerced=True | test_settings_phase2_part_5.py |
| TC-SET-6797 | P2 | Coercion SAFE_WORD_ENABLED 'true' #9 | key=SAFE_WORD_ENABLED,raw=true | coerced=True | test_settings_phase2_part_5.py |
| TC-SET-6798 | P2 | Coercion SAFE_WORD_ENABLED '1' #0 | key=SAFE_WORD_ENABLED,raw=1 | coerced=True | test_settings_phase2_part_5.py |
| TC-SET-6799 | P2 | Coercion SAFE_WORD_ENABLED '1' #1 | key=SAFE_WORD_ENABLED,raw=1 | coerced=True | test_settings_phase2_part_5.py |
| TC-SET-6800 | P2 | Coercion SAFE_WORD_ENABLED '1' #2 | key=SAFE_WORD_ENABLED,raw=1 | coerced=True | test_settings_phase2_part_5.py |
| TC-SET-6801 | P2 | Coercion SAFE_WORD_ENABLED '1' #3 | key=SAFE_WORD_ENABLED,raw=1 | coerced=True | test_settings_phase2_part_5.py |
| TC-SET-6802 | P2 | Coercion SAFE_WORD_ENABLED '1' #4 | key=SAFE_WORD_ENABLED,raw=1 | coerced=True | test_settings_phase2_part_5.py |
| TC-SET-6803 | P2 | Coercion SAFE_WORD_ENABLED '1' #5 | key=SAFE_WORD_ENABLED,raw=1 | coerced=True | test_settings_phase2_part_5.py |
| TC-SET-6804 | P2 | Coercion SAFE_WORD_ENABLED '1' #6 | key=SAFE_WORD_ENABLED,raw=1 | coerced=True | test_settings_phase2_part_5.py |
| TC-SET-6805 | P2 | Coercion SAFE_WORD_ENABLED '1' #7 | key=SAFE_WORD_ENABLED,raw=1 | coerced=True | test_settings_phase2_part_5.py |
| TC-SET-6806 | P2 | Coercion SAFE_WORD_ENABLED '1' #8 | key=SAFE_WORD_ENABLED,raw=1 | coerced=True | test_settings_phase2_part_5.py |
| TC-SET-6807 | P2 | Coercion SAFE_WORD_ENABLED '1' #9 | key=SAFE_WORD_ENABLED,raw=1 | coerced=True | test_settings_phase2_part_5.py |
| TC-SET-6808 | P2 | Coercion SAFE_WORD_ENABLED 'yes' #0 | key=SAFE_WORD_ENABLED,raw=yes | coerced=True | test_settings_phase2_part_5.py |
| TC-SET-6809 | P2 | Coercion SAFE_WORD_ENABLED 'yes' #1 | key=SAFE_WORD_ENABLED,raw=yes | coerced=True | test_settings_phase2_part_5.py |
| TC-SET-6810 | P2 | Coercion SAFE_WORD_ENABLED 'yes' #2 | key=SAFE_WORD_ENABLED,raw=yes | coerced=True | test_settings_phase2_part_5.py |
| TC-SET-6811 | P2 | Coercion SAFE_WORD_ENABLED 'yes' #3 | key=SAFE_WORD_ENABLED,raw=yes | coerced=True | test_settings_phase2_part_5.py |
| TC-SET-6812 | P2 | Coercion SAFE_WORD_ENABLED 'yes' #4 | key=SAFE_WORD_ENABLED,raw=yes | coerced=True | test_settings_phase2_part_5.py |
| TC-SET-6813 | P2 | Coercion SAFE_WORD_ENABLED 'yes' #5 | key=SAFE_WORD_ENABLED,raw=yes | coerced=True | test_settings_phase2_part_5.py |
| TC-SET-6814 | P2 | Coercion SAFE_WORD_ENABLED 'yes' #6 | key=SAFE_WORD_ENABLED,raw=yes | coerced=True | test_settings_phase2_part_5.py |
| TC-SET-6815 | P2 | Coercion SAFE_WORD_ENABLED 'yes' #7 | key=SAFE_WORD_ENABLED,raw=yes | coerced=True | test_settings_phase2_part_5.py |
| TC-SET-6816 | P2 | Coercion SAFE_WORD_ENABLED 'yes' #8 | key=SAFE_WORD_ENABLED,raw=yes | coerced=True | test_settings_phase2_part_5.py |
| TC-SET-6817 | P2 | Coercion SAFE_WORD_ENABLED 'yes' #9 | key=SAFE_WORD_ENABLED,raw=yes | coerced=True | test_settings_phase2_part_5.py |
| TC-SET-6818 | P2 | Coercion SAFE_WORD_ENABLED 'false' #0 | key=SAFE_WORD_ENABLED,raw=false | coerced=False | test_settings_phase2_part_5.py |
| TC-SET-6819 | P2 | Coercion SAFE_WORD_ENABLED 'false' #1 | key=SAFE_WORD_ENABLED,raw=false | coerced=False | test_settings_phase2_part_5.py |
| TC-SET-6820 | P2 | Coercion SAFE_WORD_ENABLED 'false' #2 | key=SAFE_WORD_ENABLED,raw=false | coerced=False | test_settings_phase2_part_5.py |
| TC-SET-6821 | P2 | Coercion SAFE_WORD_ENABLED 'false' #3 | key=SAFE_WORD_ENABLED,raw=false | coerced=False | test_settings_phase2_part_5.py |
| TC-SET-6822 | P2 | Coercion SAFE_WORD_ENABLED 'false' #4 | key=SAFE_WORD_ENABLED,raw=false | coerced=False | test_settings_phase2_part_5.py |
| TC-SET-6823 | P2 | Coercion SAFE_WORD_ENABLED 'false' #5 | key=SAFE_WORD_ENABLED,raw=false | coerced=False | test_settings_phase2_part_5.py |
| TC-SET-6824 | P2 | Coercion SAFE_WORD_ENABLED 'false' #6 | key=SAFE_WORD_ENABLED,raw=false | coerced=False | test_settings_phase2_part_5.py |
| TC-SET-6825 | P2 | Coercion SAFE_WORD_ENABLED 'false' #7 | key=SAFE_WORD_ENABLED,raw=false | coerced=False | test_settings_phase2_part_5.py |
| TC-SET-6826 | P2 | Coercion SAFE_WORD_ENABLED 'false' #8 | key=SAFE_WORD_ENABLED,raw=false | coerced=False | test_settings_phase2_part_5.py |
| TC-SET-6827 | P2 | Coercion SAFE_WORD_ENABLED 'false' #9 | key=SAFE_WORD_ENABLED,raw=false | coerced=False | test_settings_phase2_part_5.py |
| TC-SET-6828 | P2 | Coercion SAFE_WORD_ENABLED '0' #0 | key=SAFE_WORD_ENABLED,raw=0 | coerced=False | test_settings_phase2_part_5.py |
| TC-SET-6829 | P2 | Coercion SAFE_WORD_ENABLED '0' #1 | key=SAFE_WORD_ENABLED,raw=0 | coerced=False | test_settings_phase2_part_5.py |
| TC-SET-6830 | P2 | Coercion SAFE_WORD_ENABLED '0' #2 | key=SAFE_WORD_ENABLED,raw=0 | coerced=False | test_settings_phase2_part_5.py |
| TC-SET-6831 | P2 | Coercion SAFE_WORD_ENABLED '0' #3 | key=SAFE_WORD_ENABLED,raw=0 | coerced=False | test_settings_phase2_part_5.py |
| TC-SET-6832 | P2 | Coercion SAFE_WORD_ENABLED '0' #4 | key=SAFE_WORD_ENABLED,raw=0 | coerced=False | test_settings_phase2_part_5.py |
| TC-SET-6833 | P2 | Coercion SAFE_WORD_ENABLED '0' #5 | key=SAFE_WORD_ENABLED,raw=0 | coerced=False | test_settings_phase2_part_5.py |
| TC-SET-6834 | P2 | Coercion SAFE_WORD_ENABLED '0' #6 | key=SAFE_WORD_ENABLED,raw=0 | coerced=False | test_settings_phase2_part_5.py |
| TC-SET-6835 | P2 | Coercion SAFE_WORD_ENABLED '0' #7 | key=SAFE_WORD_ENABLED,raw=0 | coerced=False | test_settings_phase2_part_5.py |
| TC-SET-6836 | P2 | Coercion SAFE_WORD_ENABLED '0' #8 | key=SAFE_WORD_ENABLED,raw=0 | coerced=False | test_settings_phase2_part_5.py |
| TC-SET-6837 | P2 | Coercion SAFE_WORD_ENABLED '0' #9 | key=SAFE_WORD_ENABLED,raw=0 | coerced=False | test_settings_phase2_part_5.py |
| TC-SET-6838 | P2 | Coercion SAFE_WORD_ENABLED 'no' #0 | key=SAFE_WORD_ENABLED,raw=no | coerced=False | test_settings_phase2_part_6.py |
| TC-SET-6839 | P2 | Coercion SAFE_WORD_ENABLED 'no' #1 | key=SAFE_WORD_ENABLED,raw=no | coerced=False | test_settings_phase2_part_6.py |
| TC-SET-6840 | P2 | Coercion SAFE_WORD_ENABLED 'no' #2 | key=SAFE_WORD_ENABLED,raw=no | coerced=False | test_settings_phase2_part_6.py |
| TC-SET-6841 | P2 | Coercion SAFE_WORD_ENABLED 'no' #3 | key=SAFE_WORD_ENABLED,raw=no | coerced=False | test_settings_phase2_part_6.py |
| TC-SET-6842 | P2 | Coercion SAFE_WORD_ENABLED 'no' #4 | key=SAFE_WORD_ENABLED,raw=no | coerced=False | test_settings_phase2_part_6.py |
| TC-SET-6843 | P2 | Coercion SAFE_WORD_ENABLED 'no' #5 | key=SAFE_WORD_ENABLED,raw=no | coerced=False | test_settings_phase2_part_6.py |
| TC-SET-6844 | P2 | Coercion SAFE_WORD_ENABLED 'no' #6 | key=SAFE_WORD_ENABLED,raw=no | coerced=False | test_settings_phase2_part_6.py |
| TC-SET-6845 | P2 | Coercion SAFE_WORD_ENABLED 'no' #7 | key=SAFE_WORD_ENABLED,raw=no | coerced=False | test_settings_phase2_part_6.py |
| TC-SET-6846 | P2 | Coercion SAFE_WORD_ENABLED 'no' #8 | key=SAFE_WORD_ENABLED,raw=no | coerced=False | test_settings_phase2_part_6.py |
| TC-SET-6847 | P2 | Coercion SAFE_WORD_ENABLED 'no' #9 | key=SAFE_WORD_ENABLED,raw=no | coerced=False | test_settings_phase2_part_6.py |
| TC-SET-6848 | P2 | Coercion USER_WINDOW_DAYS '91' #0 | key=USER_WINDOW_DAYS,raw=91 | coerced=91 | test_settings_phase2_part_6.py |
| TC-SET-6849 | P2 | Coercion USER_WINDOW_DAYS '91' #1 | key=USER_WINDOW_DAYS,raw=91 | coerced=91 | test_settings_phase2_part_6.py |
| TC-SET-6850 | P2 | Coercion USER_WINDOW_DAYS '91' #2 | key=USER_WINDOW_DAYS,raw=91 | coerced=91 | test_settings_phase2_part_6.py |
| TC-SET-6851 | P2 | Coercion USER_WINDOW_DAYS '91' #3 | key=USER_WINDOW_DAYS,raw=91 | coerced=91 | test_settings_phase2_part_6.py |
| TC-SET-6852 | P2 | Coercion USER_WINDOW_DAYS '91' #4 | key=USER_WINDOW_DAYS,raw=91 | coerced=91 | test_settings_phase2_part_6.py |
| TC-SET-6853 | P2 | Coercion USER_WINDOW_DAYS '91' #5 | key=USER_WINDOW_DAYS,raw=91 | coerced=91 | test_settings_phase2_part_6.py |
| TC-SET-6854 | P2 | Coercion USER_WINDOW_DAYS '91' #6 | key=USER_WINDOW_DAYS,raw=91 | coerced=91 | test_settings_phase2_part_6.py |
| TC-SET-6855 | P2 | Coercion USER_WINDOW_DAYS '91' #7 | key=USER_WINDOW_DAYS,raw=91 | coerced=91 | test_settings_phase2_part_6.py |
| TC-SET-6856 | P2 | Coercion USER_WINDOW_DAYS '91' #8 | key=USER_WINDOW_DAYS,raw=91 | coerced=91 | test_settings_phase2_part_6.py |
| TC-SET-6857 | P2 | Coercion USER_WINDOW_DAYS '91' #9 | key=USER_WINDOW_DAYS,raw=91 | coerced=91 | test_settings_phase2_part_6.py |
| TC-SET-6858 | P2 | Coercion CACHE_MAX_SIZE '500' #0 | key=CACHE_MAX_SIZE,raw=500 | coerced=500 | test_settings_phase2_part_6.py |
| TC-SET-6859 | P2 | Coercion CACHE_MAX_SIZE '500' #1 | key=CACHE_MAX_SIZE,raw=500 | coerced=500 | test_settings_phase2_part_6.py |
| TC-SET-6860 | P2 | Coercion CACHE_MAX_SIZE '500' #2 | key=CACHE_MAX_SIZE,raw=500 | coerced=500 | test_settings_phase2_part_6.py |
| TC-SET-6861 | P2 | Coercion CACHE_MAX_SIZE '500' #3 | key=CACHE_MAX_SIZE,raw=500 | coerced=500 | test_settings_phase2_part_6.py |
| TC-SET-6862 | P2 | Coercion CACHE_MAX_SIZE '500' #4 | key=CACHE_MAX_SIZE,raw=500 | coerced=500 | test_settings_phase2_part_6.py |
| TC-SET-6863 | P2 | Coercion CACHE_MAX_SIZE '500' #5 | key=CACHE_MAX_SIZE,raw=500 | coerced=500 | test_settings_phase2_part_6.py |
| TC-SET-6864 | P2 | Coercion CACHE_MAX_SIZE '500' #6 | key=CACHE_MAX_SIZE,raw=500 | coerced=500 | test_settings_phase2_part_6.py |
| TC-SET-6865 | P2 | Coercion CACHE_MAX_SIZE '500' #7 | key=CACHE_MAX_SIZE,raw=500 | coerced=500 | test_settings_phase2_part_6.py |
| TC-SET-6866 | P2 | Coercion CACHE_MAX_SIZE '500' #8 | key=CACHE_MAX_SIZE,raw=500 | coerced=500 | test_settings_phase2_part_6.py |
| TC-SET-6867 | P2 | Coercion CACHE_MAX_SIZE '500' #9 | key=CACHE_MAX_SIZE,raw=500 | coerced=500 | test_settings_phase2_part_6.py |
| TC-SET-6868 | P2 | Coercion MODEL_MAX_TOKENS '64' #0 | key=MODEL_MAX_TOKENS,raw=64 | coerced=64 | test_settings_phase2_part_6.py |
| TC-SET-6869 | P2 | Coercion MODEL_MAX_TOKENS '64' #1 | key=MODEL_MAX_TOKENS,raw=64 | coerced=64 | test_settings_phase2_part_6.py |
| TC-SET-6870 | P2 | Coercion MODEL_MAX_TOKENS '64' #2 | key=MODEL_MAX_TOKENS,raw=64 | coerced=64 | test_settings_phase2_part_6.py |
| TC-SET-6871 | P2 | Coercion MODEL_MAX_TOKENS '64' #3 | key=MODEL_MAX_TOKENS,raw=64 | coerced=64 | test_settings_phase2_part_6.py |
| TC-SET-6872 | P2 | Coercion MODEL_MAX_TOKENS '64' #4 | key=MODEL_MAX_TOKENS,raw=64 | coerced=64 | test_settings_phase2_part_6.py |
| TC-SET-6873 | P2 | Coercion MODEL_MAX_TOKENS '64' #5 | key=MODEL_MAX_TOKENS,raw=64 | coerced=64 | test_settings_phase2_part_6.py |
| TC-SET-6874 | P2 | Coercion MODEL_MAX_TOKENS '64' #6 | key=MODEL_MAX_TOKENS,raw=64 | coerced=64 | test_settings_phase2_part_6.py |
| TC-SET-6875 | P2 | Coercion MODEL_MAX_TOKENS '64' #7 | key=MODEL_MAX_TOKENS,raw=64 | coerced=64 | test_settings_phase2_part_6.py |
| TC-SET-6876 | P2 | Coercion MODEL_MAX_TOKENS '64' #8 | key=MODEL_MAX_TOKENS,raw=64 | coerced=64 | test_settings_phase2_part_6.py |
| TC-SET-6877 | P2 | Coercion MODEL_MAX_TOKENS '64' #9 | key=MODEL_MAX_TOKENS,raw=64 | coerced=64 | test_settings_phase2_part_6.py |
| TC-SET-6878 | P2 | Coercion SEMANTIC_SIMILARITY_THRESHOLD '0.9' #0 | key=SEMANTIC_SIMILARITY_THRESHOLD,raw=0.9 | coerced=0.9 | test_settings_phase2_part_6.py |
| TC-SET-6879 | P2 | Coercion SEMANTIC_SIMILARITY_THRESHOLD '0.9' #1 | key=SEMANTIC_SIMILARITY_THRESHOLD,raw=0.9 | coerced=0.9 | test_settings_phase2_part_6.py |
| TC-SET-6880 | P2 | Coercion SEMANTIC_SIMILARITY_THRESHOLD '0.9' #2 | key=SEMANTIC_SIMILARITY_THRESHOLD,raw=0.9 | coerced=0.9 | test_settings_phase2_part_6.py |
| TC-SET-6881 | P2 | Coercion SEMANTIC_SIMILARITY_THRESHOLD '0.9' #3 | key=SEMANTIC_SIMILARITY_THRESHOLD,raw=0.9 | coerced=0.9 | test_settings_phase2_part_6.py |
| TC-SET-6882 | P2 | Coercion SEMANTIC_SIMILARITY_THRESHOLD '0.9' #4 | key=SEMANTIC_SIMILARITY_THRESHOLD,raw=0.9 | coerced=0.9 | test_settings_phase2_part_6.py |
| TC-SET-6883 | P2 | Coercion SEMANTIC_SIMILARITY_THRESHOLD '0.9' #5 | key=SEMANTIC_SIMILARITY_THRESHOLD,raw=0.9 | coerced=0.9 | test_settings_phase2_part_6.py |
| TC-SET-6884 | P2 | Coercion SEMANTIC_SIMILARITY_THRESHOLD '0.9' #6 | key=SEMANTIC_SIMILARITY_THRESHOLD,raw=0.9 | coerced=0.9 | test_settings_phase2_part_6.py |
| TC-SET-6885 | P2 | Coercion SEMANTIC_SIMILARITY_THRESHOLD '0.9' #7 | key=SEMANTIC_SIMILARITY_THRESHOLD,raw=0.9 | coerced=0.9 | test_settings_phase2_part_6.py |
| TC-SET-6886 | P2 | Coercion SEMANTIC_SIMILARITY_THRESHOLD '0.9' #8 | key=SEMANTIC_SIMILARITY_THRESHOLD,raw=0.9 | coerced=0.9 | test_settings_phase2_part_6.py |
| TC-SET-6887 | P2 | Coercion SEMANTIC_SIMILARITY_THRESHOLD '0.9' #9 | key=SEMANTIC_SIMILARITY_THRESHOLD,raw=0.9 | coerced=0.9 | test_settings_phase2_part_6.py |

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
| test_settings_phase2_part_2.py | 5663-6100 | P1 | :white_check_mark: Phase 2 |
| test_settings_phase2_part_3.py | 6101-6200 | P2 | :white_check_mark: Phase 2 |
| test_settings_phase2_part_4.py | 6411-6510 | P2 | :white_check_mark: Phase 2 |
| test_settings_phase2_part_5.py | 6511-6837 | P2 | :white_check_mark: Phase 2 |
| test_settings_phase2_part_6.py | 6838-6887 | P2 | :white_check_mark: Phase 2 |

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
