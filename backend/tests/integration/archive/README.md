# Archive Module Test Documentation

## Overview
- **Total Planned:** 23,124,528
- **Phase 1:** 115 (IDs TC-ARCH-001 to TC-ARCH-115)
- **Phase 2:** 500 (IDs TC-ARCH-201 to TC-ARCH-700)
- **Phase 3:** 5,000 (IDs TC-ARCH-701 to TC-ARCH-5,700)
- **Phase 4:** 100,000 (IDs TC-ARCH-5,701 to TC-ARCH-105,700)
- **Phase 5:** 23,018,828 (IDs TC-ARCH-105,701 to TC-ARCH-23,124,528)

## Dimension Matrix
| Dimension | Values | Phase 1 | Phase 2 | Phase 3 | Phase 4 | Phase 5 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| Cycle Number | 1, 2, 3, 4, 5, 10, 25, 50, 100 | 1-3 | 1-10 | 1-25 | 1-50 | All |
| Data Volume per Day | 1..10000 | 1-1000 | 1-250 | 1-1000 | 1-5000 | All |
| Flagged Percentage | 0-100 | 0-100 step 10 | 0-50 step 5 | 0-50 | 0-80 | All |
| Blocked Percentage | 0-100 | 0-100 step 10 | 0-50 step 5 | 0-50 | 0-80 | All |
| Reviewed Percentage | 0-100 | 0-100 | 0-100 | All | All | All |
| User Count | 1-10000 | 1-25 | 1-100 | 1-500 | 1-2500 | All |
| App Count | 1-100 | 1-10 | 1-10 | 1-20 | 1-50 | All |

## Test Case List

### Phase 1 (Current) - 115 cases
| ID | Priority | Description | Dimensions | Expected Outcome | File |
| :--- | :--- | :--- | :--- | :--- | :--- |
| TC-ARCH-001 | P0 | Single user, 1 app, clean cycle | cycle=1, users=1, apps=1, vol=1, flag=0 | Summary created, days 1-91 archived | test_archive_part_1.py |
| TC-ARCH-002..015 | P0 | Volume × flag/block matrices | cycle=1, vol=1-1000 | Totals match volume×91 | test_archive_part_1.py |
| TC-ARCH-016..056 | P0/P1 | Volume, percentage, summary metadata | cycle=1 | Correct aggregate counts | test_archive_part_1.py |
| TC-ARCH-057..115 | P1/P2 | Multi-user, multi-app, chains, boundaries, persistence | cycles=2-3, users=1-25 | Linked summaries, isolated ratios | test_archive_part_2.py |

### Phase 2 - 500 cases
| ID | Priority | Description | Dimensions | Expected Outcome | File |
| :--- | :--- | :--- | :--- | :--- | :--- |
| TC-ARCH-201 | P1 | 2 cycles linked | cycles=2 | next_cycle_id set | ⏳ Planned |
| TC-ARCH-202..700 | P1/P2 | Cycle × volume matrices | cycles=1-10 | Totals and chains correct | ⏳ Planned |

### Phase 3 - 5,000 cases
| ID | Priority | Description | Dimensions | Expected Outcome | File |
| :--- | :--- | :--- | :--- | :--- | :--- |
| TC-ARCH-701..5700 | P2 | Medium-scale archive sweeps | 25 cycles, 1000 vol | Correct summaries | ⏳ Planned |

### Phase 4 - 100,000 cases
| ID | Priority | Description | Dimensions | Expected Outcome | File |
| :--- | :--- | :--- | :--- | :--- | :--- |
| TC-ARCH-5701..105700 | P2 | High-scale archives | 50 cycles, 5000 vol | Correct summaries | ⏳ Planned |

### Phase 5 - 23,018,828 cases
| ID | Priority | Description | Dimensions | Expected Outcome | File |
| :--- | :--- | :--- | :--- | :--- | :--- |
| TC-ARCH-105701..23124528 | P3 | Exhaustive dimension sweep | All combinations | Property-consistent | ⏳ Planned |

## Implementation Status
| File | Test Cases | Priority | Status |
| :--- | :--- | :--- | :--- |
| test_archive_part_1.py | 001-056 | P0/P1 | ✅ Implemented |
| test_archive_part_2.py | 057-115 | P1/P2 | ✅ Implemented |
| test_archive_part_3.py | 201-300 | P1/P2 | ⏳ Phase 2 |
| test_archive_part_4.py | 301-500 | P1/P2 | ⏳ Phase 2 |

## Adding New Test Cases (Step-by-Step)

### Step 1: Determine Which Phase and Priority
- Phase 1 (P0/P1): IDs 001-115 (complete)
- Phase 2 (P1/P2): IDs 201-700 (planned)
- Phase 3 (P2): IDs 701-5,700 (planned)
- Phase 4 (P3): IDs 5,701-105,700 (planned)
- Phase 5 (P3): IDs 105,701-23,124,528 (planned)

### Step 2: Check for Uniqueness
Verify the (cycle, volume, flag%, block%, review%, users, apps) tuple is not
already covered in the dimension matrix.

### Step 3: Create the Test File
`test_archive_part_{N}.py`, maximum 100 cases. Example:
```python
def test_two_cycles_linked_{unique_id}(self) -> None:
    """Test that two archive cycles are properly linked.

    :param: none
    :return: none
    """
    profiler = UserProfiler(...)
    # Record cycle 1 and cycle 2
    # Verify next_cycle_id is set
    # Assert chain is correct
```

### Step 4: Update This README
Add rows to the phase tables and update the implementation status.

### Step 5: Run and Commit
```bash
uv run python -m pytest tests/integration/archive/test_archive_part_{N}.py -v
git add tests/integration/archive/test_archive_part_{N}.py
git commit -m "[TEST-INT] Add 91-day archive tests part {N}"
```

## Related Documentation
- [Archive Strategy](../../docs/architecture/)
- [User Profiling](../../docs/architecture/)
