# Detector Module Test Documentation

## Overview
- **Total Planned:** 2,100,000
- **Phase 1:** 125 (IDs TC-DET-001 to TC-DET-125)
- **Phase 2:** 2,000 (IDs TC-DET-201 to TC-DET-2,200)
- **Phase 3:** 20,000 (IDs TC-DET-2,201 to TC-DET-22,200)
- **Phase 4:** 200,000 (IDs TC-DET-22,201 to TC-DET-222,200)
- **Phase 5:** 1,877,800 (IDs TC-DET-222,201 to TC-DET-2,100,000)

## Dimension Matrix
| Dimension | Values | Phase 1 | Phase 2 | Phase 3 |
| :--- | :--- | :--- | :--- | :--- |
| Detector | aho, bk-tree, metaphone, bloom, rolling-hash, multi-language | aho, bk-tree, metaphone, multi-language | +bloom, rolling-hash | All |
| Language | en, zh, ru, ar, ja, ko, multi | en, multi | +zh, ru | All |
| Length | 1, 10, 100, 1000, 8192 | 1-100 | 1-1000 | All |
| Content | profanity, clean, obfuscated | profanity, clean | +obfuscated | All |
| Edit distance | 0, 1, 2, 3 | 1, 2 | 0, 3 | All |
| Case | lower, upper, mixed | mixed | all | All |
| Unicode | ascii, fullwidth, CJK | ascii, fullwidth | +CJK | All |

## Test Case List

### Phase 1 (Current) - 125 cases
| ID | Priority | Description | Dimensions | Expected Outcome | File |
| :--- | :--- | :--- | :--- | :--- | :--- |
| TC-DET-001 | P0 | Aho exact match blocks | en, profanity | matched=True, confidence 1.0 | test_aho_corasick_part_1.py |
| TC-DET-002..050 | P0/P1 | Aho exact/negative matrix | en, lengths 1-100 | matched flag per row | test_aho_corasick_part_1.py |
| TC-DET-051..080 | P0/P1 | BK-tree fuzzy matrix | en, distance 1-2 | matched per row | test_bk_tree_part_1.py |
| TC-DET-081..100 | P1 | Metaphone phonetic matrix | en | matched per row | test_metaphone_part_1.py |
| TC-DET-101..115 | P0/P1 | Multi-language packages | multi | package availability + positives | test_multi_language_part_1.py |
| TC-DET-116..125 | P1/P2 | Multi-language semantics | multi | language attribution, toggles | test_multi_language_part_2.py |

### Phase 2 - 2,000 cases
| ID | Priority | Description | Dimensions | Expected Outcome | File |
| :--- | :--- | :--- | :--- | :--- | :--- |
| TC-DET-201 | P1 | Bloom filter positive | en, bloom | weak positive (REVIEW) | test_bloom_part_1.py |
| TC-DET-202 | P1 | Rolling hash repeat | en, repeat | matched after flag | test_rolling_hash_part_1.py |
| TC-DET-203..2200 | P1/P2 | Language × length × content matrix | en/zh/ru, 1-1000 | verdict per row | ⏳ Phase 2 |

### Phase 3 - 20,000 cases
| ID | Priority | Description | Dimensions | Expected Outcome | File |
| :--- | :--- | :--- | :--- | :--- | :--- |
| TC-DET-2201 | P2 | CJK obfuscation | zh, fullwidth | matched | ⏳ Phase 3 |
| TC-DET-2202..22200 | P2 | All-detector × all-dimension matrix | All | verdict per row | ⏳ Phase 3 |

### Phase 4 - 200,000 cases
| ID | Priority | Description | Dimensions | Expected Outcome | File |
| :--- | :--- | :--- | :--- | :--- | :--- |
| TC-DET-22201..222200 | P2 | Multi-detector interaction | All | aggregated verdicts | ⏳ Phase 4 |

### Phase 5 - 1,877,800 cases
| ID | Priority | Description | Dimensions | Expected Outcome | File |
| :--- | :--- | :--- | :--- | :--- | :--- |
| TC-DET-222201..2100000 | P3 | Exhaustive dimension sweep | All | property-consistent verdicts | ⏳ Phase 5 |

## Implementation Status
| File | Test Cases | Priority | Status |
| :--- | :--- | :--- | :--- |
| test_aho_corasick_part_1.py | 001-050 | P0/P1 | ✅ Implemented |
| test_bk_tree_part_1.py | 051-080 | P0/P1 | ✅ Implemented |
| test_metaphone_part_1.py | 081-100 | P1 | ✅ Implemented |
| test_multi_language_part_1.py | 101-115 | P0/P1 | ✅ Implemented |
| test_multi_language_part_2.py | 116-125 | P1/P2 | ✅ Implemented |
| test_bloom_part_1.py | 201-230 | P1/P2 | ⏳ Phase 2 |
| test_rolling_hash_part_1.py | 231-260 | P1/P2 | ⏳ Phase 2 |

## Adding New Test Cases (Step-by-Step)

### Step 1: Determine Which Phase and Priority
- Phase 1 (P0/P1): IDs 001-125 (complete)
- Phase 2 (P1/P2): IDs 201-2,200 (planned)
- Phase 3 (P2): IDs 2,201-22,200 (planned)
- Phase 4 (P3): IDs 22,201-222,200 (planned)
- Phase 5 (P3): IDs 222,201-2,100,000 (planned)

### Step 2: Check for Uniqueness
Verify the (detector, language, length, content, distance) combination is not
already covered. Consult the dimension matrix above.

### Step 3: Create the Test File
- Naming: `test_{detector}_part_{N}.py`
- Maximum 100 test cases per file.
- Import: `from tests.base_test import BaseTest`

### Step 4: Write the Test Method
```python
def test_{scenario}_{expected}_{unique_id}(self) -> None:
    """{description}

    :param: none (uses class state)
    :return: none (assertions)
    """
    word_bank.add_word("targetword")
    detector = AhoCorasickDetector(word_bank)
    assert detector.detect("text under test").matched is True
```

### Step 5: Update This README
Add the row to the phase table and update the implementation status table.

### Step 6: Run the Test
```bash
uv run python -m pytest tests/unit/detectors/test_{detector}_part_{N}.py -v
```

### Step 7: Commit
```bash
git add tests/unit/detectors/test_{detector}_part_{N}.py
git commit -m "[TEST-UNIT] Add {detector} detector tests part {N}"
```

## Related Documentation
- [Detector Architecture](../../docs/architecture/)
- [Algorithm Formulations](../../docs/algorithms/)
