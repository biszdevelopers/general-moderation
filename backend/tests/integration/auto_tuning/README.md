# Auto-Tuning Module Test Documentation

## Overview
- **Total Planned:** 1,050,000
- **Phase 1:** 60 (IDs TC-TUNE-001 to TC-TUNE-0060) :white_check_mark: Implemented
- **Phase 2:** 550 (IDs TC-TUNE-0061 to TC-TUNE-0610) :white_check_mark: Implemented
- **Phase 3:** 10,000 (IDs TC-TUNE-0611 to TC-TUNE-10610) :hourglass: Planned
- **Phase 4:** 100,000 (IDs TC-TUNE-10611 to TC-TUNE-110610) :hourglass: Planned
- **Phase 5:** 939,390 (IDs TC-TUNE-110611 to TC-TUNE-1050000) :hourglass: Planned

## Dimension Matrix
| Dimension | Values (Phase 2) |
| :--- | :--- |
| Precision | 0.0-1.0 |
| Feedback rows | 0-5000 |
| LLM pass rate | 0.0-1.0 |
| Half-life days | 1-3650 |

## Test Case List

### Phase 1 - 60 cases
- 60 cases (weights, thresholds, decay).

### Phase 2 (Current) - 550 cases
| ID | Priority | Description | Dimensions | Expected Outcome | File |
| :--- | :--- | :--- | :--- | :--- | :--- |
| TC-TUNE-4459 | P1 | Precision 0/2 | correct=0,total=2 | delta=0 | test_auto_tuning_phase2_part_1.py |
| TC-TUNE-4460 | P1 | Precision 1/2 | correct=1,total=2 | delta=0 | test_auto_tuning_phase2_part_1.py |
| TC-TUNE-4461 | P1 | Precision 2/2 | correct=2,total=2 | delta=0 | test_auto_tuning_phase2_part_1.py |
| TC-TUNE-4462 | P1 | Precision 0/4 | correct=0,total=4 | delta=0 | test_auto_tuning_phase2_part_1.py |
| TC-TUNE-4463 | P1 | Precision 1/4 | correct=1,total=4 | delta=0 | test_auto_tuning_phase2_part_1.py |
| TC-TUNE-4464 | P1 | Precision 2/4 | correct=2,total=4 | delta=0 | test_auto_tuning_phase2_part_1.py |
| TC-TUNE-4465 | P1 | Precision 3/4 | correct=3,total=4 | delta=0 | test_auto_tuning_phase2_part_1.py |
| TC-TUNE-4466 | P1 | Precision 4/4 | correct=4,total=4 | delta=0 | test_auto_tuning_phase2_part_1.py |
| TC-TUNE-4467 | P1 | Precision 0/6 | correct=0,total=6 | delta=0 | test_auto_tuning_phase2_part_1.py |
| TC-TUNE-4468 | P1 | Precision 1/6 | correct=1,total=6 | delta=0 | test_auto_tuning_phase2_part_1.py |
| TC-TUNE-4469 | P1 | Precision 2/6 | correct=2,total=6 | delta=0 | test_auto_tuning_phase2_part_1.py |
| TC-TUNE-4470 | P1 | Precision 3/6 | correct=3,total=6 | delta=0 | test_auto_tuning_phase2_part_1.py |
| TC-TUNE-4471 | P1 | Precision 4/6 | correct=4,total=6 | delta=0 | test_auto_tuning_phase2_part_1.py |
| TC-TUNE-4472 | P1 | Precision 5/6 | correct=5,total=6 | delta=0 | test_auto_tuning_phase2_part_1.py |
| TC-TUNE-4473 | P1 | Precision 6/6 | correct=6,total=6 | delta=0 | test_auto_tuning_phase2_part_1.py |
| TC-TUNE-4474 | P1 | Precision 0/8 | correct=0,total=8 | delta=0 | test_auto_tuning_phase2_part_1.py |
| TC-TUNE-4475 | P1 | Precision 1/8 | correct=1,total=8 | delta=0 | test_auto_tuning_phase2_part_1.py |
| TC-TUNE-4476 | P1 | Precision 2/8 | correct=2,total=8 | delta=0 | test_auto_tuning_phase2_part_1.py |
| TC-TUNE-4477 | P1 | Precision 3/8 | correct=3,total=8 | delta=0 | test_auto_tuning_phase2_part_1.py |
| TC-TUNE-4478 | P1 | Precision 4/8 | correct=4,total=8 | delta=0 | test_auto_tuning_phase2_part_1.py |
| TC-TUNE-4479 | P1 | Precision 5/8 | correct=5,total=8 | delta=0 | test_auto_tuning_phase2_part_1.py |
| TC-TUNE-4480 | P1 | Precision 6/8 | correct=6,total=8 | delta=0 | test_auto_tuning_phase2_part_1.py |
| TC-TUNE-4481 | P1 | Precision 7/8 | correct=7,total=8 | delta=0 | test_auto_tuning_phase2_part_1.py |
| TC-TUNE-4482 | P1 | Precision 8/8 | correct=8,total=8 | delta=0 | test_auto_tuning_phase2_part_1.py |
| TC-TUNE-4483 | P1 | Precision 0/10 | correct=0,total=10 | delta=-1 | test_auto_tuning_phase2_part_1.py |
| TC-TUNE-4484 | P1 | Precision 1/10 | correct=1,total=10 | delta=-1 | test_auto_tuning_phase2_part_1.py |
| TC-TUNE-4485 | P1 | Precision 2/10 | correct=2,total=10 | delta=-1 | test_auto_tuning_phase2_part_1.py |
| TC-TUNE-4486 | P1 | Precision 3/10 | correct=3,total=10 | delta=-1 | test_auto_tuning_phase2_part_1.py |
| TC-TUNE-4487 | P1 | Precision 4/10 | correct=4,total=10 | delta=0 | test_auto_tuning_phase2_part_1.py |
| TC-TUNE-4488 | P1 | Precision 5/10 | correct=5,total=10 | delta=0 | test_auto_tuning_phase2_part_1.py |
| TC-TUNE-4489 | P1 | Precision 6/10 | correct=6,total=10 | delta=0 | test_auto_tuning_phase2_part_1.py |
| TC-TUNE-4490 | P1 | Precision 7/10 | correct=7,total=10 | delta=1 | test_auto_tuning_phase2_part_1.py |
| TC-TUNE-4491 | P1 | Precision 8/10 | correct=8,total=10 | delta=1 | test_auto_tuning_phase2_part_1.py |
| TC-TUNE-4492 | P1 | Precision 9/10 | correct=9,total=10 | delta=1 | test_auto_tuning_phase2_part_1.py |
| TC-TUNE-4493 | P1 | Precision 10/10 | correct=10,total=10 | delta=1 | test_auto_tuning_phase2_part_1.py |
| TC-TUNE-4494 | P1 | Precision 0/15 | correct=0,total=15 | delta=-1 | test_auto_tuning_phase2_part_1.py |
| TC-TUNE-4495 | P1 | Precision 1/15 | correct=1,total=15 | delta=-1 | test_auto_tuning_phase2_part_1.py |
| TC-TUNE-4496 | P1 | Precision 2/15 | correct=2,total=15 | delta=-1 | test_auto_tuning_phase2_part_1.py |
| TC-TUNE-4497 | P1 | Precision 3/15 | correct=3,total=15 | delta=-1 | test_auto_tuning_phase2_part_1.py |
| TC-TUNE-4498 | P1 | Precision 4/15 | correct=4,total=15 | delta=-1 | test_auto_tuning_phase2_part_1.py |
| TC-TUNE-4499 | P1 | Precision 5/15 | correct=5,total=15 | delta=-1 | test_auto_tuning_phase2_part_1.py |
| TC-TUNE-4500 | P1 | Precision 6/15 | correct=6,total=15 | delta=0 | test_auto_tuning_phase2_part_1.py |
| TC-TUNE-4501 | P1 | Precision 7/15 | correct=7,total=15 | delta=0 | test_auto_tuning_phase2_part_1.py |
| TC-TUNE-4502 | P1 | Precision 8/15 | correct=8,total=15 | delta=0 | test_auto_tuning_phase2_part_1.py |
| TC-TUNE-4503 | P1 | Precision 9/15 | correct=9,total=15 | delta=0 | test_auto_tuning_phase2_part_1.py |
| TC-TUNE-4504 | P1 | Precision 10/15 | correct=10,total=15 | delta=1 | test_auto_tuning_phase2_part_1.py |
| TC-TUNE-4505 | P1 | Precision 11/15 | correct=11,total=15 | delta=1 | test_auto_tuning_phase2_part_1.py |
| TC-TUNE-4506 | P1 | Precision 12/15 | correct=12,total=15 | delta=1 | test_auto_tuning_phase2_part_1.py |
| TC-TUNE-4507 | P1 | Precision 13/15 | correct=13,total=15 | delta=1 | test_auto_tuning_phase2_part_1.py |
| TC-TUNE-4508 | P1 | Precision 14/15 | correct=14,total=15 | delta=1 | test_auto_tuning_phase2_part_1.py |
| TC-TUNE-4509 | P1 | Precision 15/15 | correct=15,total=15 | delta=1 | test_auto_tuning_phase2_part_1.py |
| TC-TUNE-4510 | P1 | Precision 0/20 | correct=0,total=20 | delta=-1 | test_auto_tuning_phase2_part_1.py |
| TC-TUNE-4511 | P1 | Precision 1/20 | correct=1,total=20 | delta=-1 | test_auto_tuning_phase2_part_1.py |
| TC-TUNE-4512 | P1 | Precision 2/20 | correct=2,total=20 | delta=-1 | test_auto_tuning_phase2_part_1.py |
| TC-TUNE-4513 | P1 | Precision 3/20 | correct=3,total=20 | delta=-1 | test_auto_tuning_phase2_part_1.py |
| TC-TUNE-4514 | P1 | Precision 4/20 | correct=4,total=20 | delta=-1 | test_auto_tuning_phase2_part_1.py |
| TC-TUNE-4515 | P1 | Precision 5/20 | correct=5,total=20 | delta=-1 | test_auto_tuning_phase2_part_1.py |
| TC-TUNE-4516 | P1 | Precision 6/20 | correct=6,total=20 | delta=-1 | test_auto_tuning_phase2_part_1.py |
| TC-TUNE-4517 | P1 | Precision 7/20 | correct=7,total=20 | delta=-1 | test_auto_tuning_phase2_part_1.py |
| TC-TUNE-4518 | P1 | Precision 8/20 | correct=8,total=20 | delta=0 | test_auto_tuning_phase2_part_1.py |
| TC-TUNE-4519 | P1 | Precision 9/20 | correct=9,total=20 | delta=0 | test_auto_tuning_phase2_part_1.py |
| TC-TUNE-4520 | P1 | Precision 10/20 | correct=10,total=20 | delta=0 | test_auto_tuning_phase2_part_1.py |
| TC-TUNE-4521 | P1 | Precision 11/20 | correct=11,total=20 | delta=0 | test_auto_tuning_phase2_part_1.py |
| TC-TUNE-4522 | P1 | Precision 12/20 | correct=12,total=20 | delta=0 | test_auto_tuning_phase2_part_1.py |
| TC-TUNE-4523 | P1 | Precision 13/20 | correct=13,total=20 | delta=1 | test_auto_tuning_phase2_part_1.py |
| TC-TUNE-4524 | P1 | Precision 14/20 | correct=14,total=20 | delta=1 | test_auto_tuning_phase2_part_1.py |
| TC-TUNE-4525 | P1 | Precision 15/20 | correct=15,total=20 | delta=1 | test_auto_tuning_phase2_part_1.py |
| TC-TUNE-4526 | P1 | Precision 16/20 | correct=16,total=20 | delta=1 | test_auto_tuning_phase2_part_1.py |
| TC-TUNE-4527 | P1 | Precision 17/20 | correct=17,total=20 | delta=1 | test_auto_tuning_phase2_part_1.py |
| TC-TUNE-4528 | P1 | Precision 18/20 | correct=18,total=20 | delta=1 | test_auto_tuning_phase2_part_1.py |
| TC-TUNE-4529 | P1 | Precision 19/20 | correct=19,total=20 | delta=1 | test_auto_tuning_phase2_part_1.py |
| TC-TUNE-4530 | P1 | Precision 20/20 | correct=20,total=20 | delta=1 | test_auto_tuning_phase2_part_1.py |
| TC-TUNE-4531 | P1 | Precision 0/25 | correct=0,total=25 | delta=-1 | test_auto_tuning_phase2_part_1.py |
| TC-TUNE-4532 | P1 | Precision 1/25 | correct=1,total=25 | delta=-1 | test_auto_tuning_phase2_part_1.py |
| TC-TUNE-4533 | P1 | Precision 2/25 | correct=2,total=25 | delta=-1 | test_auto_tuning_phase2_part_1.py |
| TC-TUNE-4534 | P1 | Precision 3/25 | correct=3,total=25 | delta=-1 | test_auto_tuning_phase2_part_1.py |
| TC-TUNE-4535 | P1 | Precision 4/25 | correct=4,total=25 | delta=-1 | test_auto_tuning_phase2_part_1.py |
| TC-TUNE-4536 | P1 | Precision 5/25 | correct=5,total=25 | delta=-1 | test_auto_tuning_phase2_part_1.py |
| TC-TUNE-4537 | P1 | Precision 6/25 | correct=6,total=25 | delta=-1 | test_auto_tuning_phase2_part_1.py |
| TC-TUNE-4538 | P1 | Precision 7/25 | correct=7,total=25 | delta=-1 | test_auto_tuning_phase2_part_1.py |
| TC-TUNE-4539 | P1 | Precision 8/25 | correct=8,total=25 | delta=-1 | test_auto_tuning_phase2_part_1.py |
| TC-TUNE-4540 | P1 | Precision 9/25 | correct=9,total=25 | delta=-1 | test_auto_tuning_phase2_part_1.py |
| TC-TUNE-4541 | P1 | Precision 10/25 | correct=10,total=25 | delta=0 | test_auto_tuning_phase2_part_1.py |
| TC-TUNE-4542 | P1 | Precision 11/25 | correct=11,total=25 | delta=0 | test_auto_tuning_phase2_part_1.py |
| TC-TUNE-4543 | P1 | Precision 12/25 | correct=12,total=25 | delta=0 | test_auto_tuning_phase2_part_1.py |
| TC-TUNE-4544 | P1 | Precision 13/25 | correct=13,total=25 | delta=0 | test_auto_tuning_phase2_part_1.py |
| TC-TUNE-4545 | P1 | Precision 14/25 | correct=14,total=25 | delta=0 | test_auto_tuning_phase2_part_1.py |
| TC-TUNE-4546 | P1 | Precision 15/25 | correct=15,total=25 | delta=0 | test_auto_tuning_phase2_part_1.py |
| TC-TUNE-4547 | P1 | Precision 16/25 | correct=16,total=25 | delta=1 | test_auto_tuning_phase2_part_1.py |
| TC-TUNE-4548 | P1 | Precision 17/25 | correct=17,total=25 | delta=1 | test_auto_tuning_phase2_part_1.py |
| TC-TUNE-4549 | P1 | Precision 18/25 | correct=18,total=25 | delta=1 | test_auto_tuning_phase2_part_1.py |
| TC-TUNE-4550 | P1 | Precision 19/25 | correct=19,total=25 | delta=1 | test_auto_tuning_phase2_part_1.py |
| TC-TUNE-4551 | P1 | Precision 20/25 | correct=20,total=25 | delta=1 | test_auto_tuning_phase2_part_1.py |
| TC-TUNE-4552 | P1 | Precision 21/25 | correct=21,total=25 | delta=1 | test_auto_tuning_phase2_part_1.py |
| TC-TUNE-4553 | P1 | Precision 22/25 | correct=22,total=25 | delta=1 | test_auto_tuning_phase2_part_1.py |
| TC-TUNE-4554 | P1 | Precision 23/25 | correct=23,total=25 | delta=1 | test_auto_tuning_phase2_part_1.py |
| TC-TUNE-4555 | P1 | Precision 24/25 | correct=24,total=25 | delta=1 | test_auto_tuning_phase2_part_1.py |
| TC-TUNE-4556 | P1 | Precision 25/25 | correct=25,total=25 | delta=1 | test_auto_tuning_phase2_part_1.py |
| TC-TUNE-4557 | P1 | Precision 0/30 | correct=0,total=30 | delta=-1 | test_auto_tuning_phase2_part_1.py |
| TC-TUNE-4558 | P1 | Precision 1/30 | correct=1,total=30 | delta=-1 | test_auto_tuning_phase2_part_1.py |
| TC-TUNE-4559 | P1 | Precision 2/30 | correct=2,total=30 | delta=-1 | test_auto_tuning_phase2_part_2.py |
| TC-TUNE-4560 | P1 | Precision 3/30 | correct=3,total=30 | delta=-1 | test_auto_tuning_phase2_part_2.py |
| TC-TUNE-4561 | P1 | Precision 4/30 | correct=4,total=30 | delta=-1 | test_auto_tuning_phase2_part_2.py |
| TC-TUNE-4562 | P1 | Precision 5/30 | correct=5,total=30 | delta=-1 | test_auto_tuning_phase2_part_2.py |
| TC-TUNE-4563 | P1 | Precision 6/30 | correct=6,total=30 | delta=-1 | test_auto_tuning_phase2_part_2.py |
| TC-TUNE-4564 | P1 | Precision 7/30 | correct=7,total=30 | delta=-1 | test_auto_tuning_phase2_part_2.py |
| TC-TUNE-4565 | P1 | Precision 8/30 | correct=8,total=30 | delta=-1 | test_auto_tuning_phase2_part_2.py |
| TC-TUNE-4566 | P1 | Precision 9/30 | correct=9,total=30 | delta=-1 | test_auto_tuning_phase2_part_2.py |
| TC-TUNE-4567 | P1 | Precision 10/30 | correct=10,total=30 | delta=-1 | test_auto_tuning_phase2_part_2.py |
| TC-TUNE-4568 | P1 | Precision 11/30 | correct=11,total=30 | delta=-1 | test_auto_tuning_phase2_part_2.py |
| TC-TUNE-4569 | P1 | Precision 12/30 | correct=12,total=30 | delta=0 | test_auto_tuning_phase2_part_2.py |
| TC-TUNE-4570 | P1 | Precision 13/30 | correct=13,total=30 | delta=0 | test_auto_tuning_phase2_part_2.py |
| TC-TUNE-4571 | P1 | Precision 14/30 | correct=14,total=30 | delta=0 | test_auto_tuning_phase2_part_2.py |
| TC-TUNE-4572 | P1 | Precision 15/30 | correct=15,total=30 | delta=0 | test_auto_tuning_phase2_part_2.py |
| TC-TUNE-4573 | P1 | Precision 16/30 | correct=16,total=30 | delta=0 | test_auto_tuning_phase2_part_2.py |
| TC-TUNE-4574 | P1 | Precision 17/30 | correct=17,total=30 | delta=0 | test_auto_tuning_phase2_part_2.py |
| TC-TUNE-4575 | P1 | Precision 18/30 | correct=18,total=30 | delta=0 | test_auto_tuning_phase2_part_2.py |
| TC-TUNE-4576 | P1 | Precision 19/30 | correct=19,total=30 | delta=1 | test_auto_tuning_phase2_part_2.py |
| TC-TUNE-4577 | P1 | Precision 20/30 | correct=20,total=30 | delta=1 | test_auto_tuning_phase2_part_2.py |
| TC-TUNE-4578 | P1 | Precision 21/30 | correct=21,total=30 | delta=1 | test_auto_tuning_phase2_part_2.py |
| TC-TUNE-4579 | P1 | Precision 22/30 | correct=22,total=30 | delta=1 | test_auto_tuning_phase2_part_2.py |
| TC-TUNE-4580 | P1 | Precision 23/30 | correct=23,total=30 | delta=1 | test_auto_tuning_phase2_part_2.py |
| TC-TUNE-4581 | P1 | Precision 24/30 | correct=24,total=30 | delta=1 | test_auto_tuning_phase2_part_2.py |
| TC-TUNE-4582 | P1 | Precision 25/30 | correct=25,total=30 | delta=1 | test_auto_tuning_phase2_part_2.py |
| TC-TUNE-4583 | P1 | Precision 26/30 | correct=26,total=30 | delta=1 | test_auto_tuning_phase2_part_2.py |
| TC-TUNE-4584 | P1 | Precision 27/30 | correct=27,total=30 | delta=1 | test_auto_tuning_phase2_part_2.py |
| TC-TUNE-4585 | P1 | Precision 28/30 | correct=28,total=30 | delta=1 | test_auto_tuning_phase2_part_2.py |
| TC-TUNE-4586 | P1 | Precision 29/30 | correct=29,total=30 | delta=1 | test_auto_tuning_phase2_part_2.py |
| TC-TUNE-4587 | P1 | Precision 30/30 | correct=30,total=30 | delta=1 | test_auto_tuning_phase2_part_2.py |
| TC-TUNE-4588 | P1 | Precision 0/40 | correct=0,total=40 | delta=-1 | test_auto_tuning_phase2_part_2.py |
| TC-TUNE-4589 | P1 | Precision 1/40 | correct=1,total=40 | delta=-1 | test_auto_tuning_phase2_part_2.py |
| TC-TUNE-4590 | P1 | Precision 2/40 | correct=2,total=40 | delta=-1 | test_auto_tuning_phase2_part_2.py |
| TC-TUNE-4591 | P1 | Precision 3/40 | correct=3,total=40 | delta=-1 | test_auto_tuning_phase2_part_2.py |
| TC-TUNE-4592 | P1 | Precision 4/40 | correct=4,total=40 | delta=-1 | test_auto_tuning_phase2_part_2.py |
| TC-TUNE-4593 | P1 | Precision 5/40 | correct=5,total=40 | delta=-1 | test_auto_tuning_phase2_part_2.py |
| TC-TUNE-4594 | P1 | Precision 6/40 | correct=6,total=40 | delta=-1 | test_auto_tuning_phase2_part_2.py |
| TC-TUNE-4595 | P1 | Precision 7/40 | correct=7,total=40 | delta=-1 | test_auto_tuning_phase2_part_2.py |
| TC-TUNE-4596 | P1 | Precision 8/40 | correct=8,total=40 | delta=-1 | test_auto_tuning_phase2_part_2.py |
| TC-TUNE-4597 | P1 | Precision 9/40 | correct=9,total=40 | delta=-1 | test_auto_tuning_phase2_part_2.py |
| TC-TUNE-4598 | P1 | Precision 10/40 | correct=10,total=40 | delta=-1 | test_auto_tuning_phase2_part_2.py |
| TC-TUNE-4599 | P1 | Precision 11/40 | correct=11,total=40 | delta=-1 | test_auto_tuning_phase2_part_2.py |
| TC-TUNE-4600 | P1 | Precision 12/40 | correct=12,total=40 | delta=-1 | test_auto_tuning_phase2_part_2.py |
| TC-TUNE-4601 | P1 | Precision 13/40 | correct=13,total=40 | delta=-1 | test_auto_tuning_phase2_part_2.py |
| TC-TUNE-4602 | P1 | Precision 14/40 | correct=14,total=40 | delta=-1 | test_auto_tuning_phase2_part_2.py |
| TC-TUNE-4603 | P1 | Precision 15/40 | correct=15,total=40 | delta=-1 | test_auto_tuning_phase2_part_2.py |
| TC-TUNE-4604 | P1 | Precision 16/40 | correct=16,total=40 | delta=0 | test_auto_tuning_phase2_part_2.py |
| TC-TUNE-4605 | P1 | Precision 17/40 | correct=17,total=40 | delta=0 | test_auto_tuning_phase2_part_2.py |
| TC-TUNE-4606 | P1 | Precision 18/40 | correct=18,total=40 | delta=0 | test_auto_tuning_phase2_part_2.py |
| TC-TUNE-4607 | P1 | Precision 19/40 | correct=19,total=40 | delta=0 | test_auto_tuning_phase2_part_2.py |
| TC-TUNE-4608 | P1 | Precision 20/40 | correct=20,total=40 | delta=0 | test_auto_tuning_phase2_part_2.py |
| TC-TUNE-4609 | P1 | Threshold pass rate 0/2 | passes=0,total=2 | delta=-1 | test_auto_tuning_phase2_part_2.py |
| TC-TUNE-4610 | P1 | Threshold pass rate 1/2 | passes=1,total=2 | delta=-1 | test_auto_tuning_phase2_part_2.py |
| TC-TUNE-4611 | P1 | Threshold pass rate 2/2 | passes=2,total=2 | delta=1 | test_auto_tuning_phase2_part_2.py |
| TC-TUNE-4612 | P1 | Threshold pass rate 0/4 | passes=0,total=4 | delta=-1 | test_auto_tuning_phase2_part_2.py |
| TC-TUNE-4613 | P1 | Threshold pass rate 1/4 | passes=1,total=4 | delta=-1 | test_auto_tuning_phase2_part_2.py |
| TC-TUNE-4614 | P1 | Threshold pass rate 2/4 | passes=2,total=4 | delta=-1 | test_auto_tuning_phase2_part_2.py |
| TC-TUNE-4615 | P1 | Threshold pass rate 3/4 | passes=3,total=4 | delta=0 | test_auto_tuning_phase2_part_2.py |
| TC-TUNE-4616 | P1 | Threshold pass rate 4/4 | passes=4,total=4 | delta=1 | test_auto_tuning_phase2_part_2.py |
| TC-TUNE-4617 | P1 | Threshold pass rate 0/6 | passes=0,total=6 | delta=-1 | test_auto_tuning_phase2_part_2.py |
| TC-TUNE-4618 | P1 | Threshold pass rate 1/6 | passes=1,total=6 | delta=-1 | test_auto_tuning_phase2_part_2.py |
| TC-TUNE-4619 | P1 | Threshold pass rate 2/6 | passes=2,total=6 | delta=-1 | test_auto_tuning_phase2_part_2.py |
| TC-TUNE-4620 | P1 | Threshold pass rate 3/6 | passes=3,total=6 | delta=-1 | test_auto_tuning_phase2_part_2.py |
| TC-TUNE-4621 | P1 | Threshold pass rate 4/6 | passes=4,total=6 | delta=-1 | test_auto_tuning_phase2_part_2.py |
| TC-TUNE-4622 | P1 | Threshold pass rate 5/6 | passes=5,total=6 | delta=0 | test_auto_tuning_phase2_part_2.py |
| TC-TUNE-4623 | P1 | Threshold pass rate 6/6 | passes=6,total=6 | delta=1 | test_auto_tuning_phase2_part_2.py |
| TC-TUNE-4624 | P1 | Threshold pass rate 0/8 | passes=0,total=8 | delta=-1 | test_auto_tuning_phase2_part_2.py |
| TC-TUNE-4625 | P1 | Threshold pass rate 1/8 | passes=1,total=8 | delta=-1 | test_auto_tuning_phase2_part_2.py |
| TC-TUNE-4626 | P1 | Threshold pass rate 2/8 | passes=2,total=8 | delta=-1 | test_auto_tuning_phase2_part_2.py |
| TC-TUNE-4627 | P1 | Threshold pass rate 3/8 | passes=3,total=8 | delta=-1 | test_auto_tuning_phase2_part_2.py |
| TC-TUNE-4628 | P1 | Threshold pass rate 4/8 | passes=4,total=8 | delta=-1 | test_auto_tuning_phase2_part_2.py |
| TC-TUNE-4629 | P1 | Threshold pass rate 5/8 | passes=5,total=8 | delta=-1 | test_auto_tuning_phase2_part_2.py |
| TC-TUNE-4630 | P1 | Threshold pass rate 6/8 | passes=6,total=8 | delta=0 | test_auto_tuning_phase2_part_2.py |
| TC-TUNE-4631 | P1 | Threshold pass rate 7/8 | passes=7,total=8 | delta=0 | test_auto_tuning_phase2_part_2.py |
| TC-TUNE-4632 | P1 | Threshold pass rate 8/8 | passes=8,total=8 | delta=1 | test_auto_tuning_phase2_part_2.py |
| TC-TUNE-4633 | P1 | Threshold pass rate 0/10 | passes=0,total=10 | delta=-1 | test_auto_tuning_phase2_part_2.py |
| TC-TUNE-4634 | P1 | Threshold pass rate 1/10 | passes=1,total=10 | delta=-1 | test_auto_tuning_phase2_part_2.py |
| TC-TUNE-4635 | P1 | Threshold pass rate 2/10 | passes=2,total=10 | delta=-1 | test_auto_tuning_phase2_part_2.py |
| TC-TUNE-4636 | P1 | Threshold pass rate 3/10 | passes=3,total=10 | delta=-1 | test_auto_tuning_phase2_part_2.py |
| TC-TUNE-4637 | P1 | Threshold pass rate 4/10 | passes=4,total=10 | delta=-1 | test_auto_tuning_phase2_part_2.py |
| TC-TUNE-4638 | P1 | Threshold pass rate 5/10 | passes=5,total=10 | delta=-1 | test_auto_tuning_phase2_part_2.py |
| TC-TUNE-4639 | P1 | Threshold pass rate 6/10 | passes=6,total=10 | delta=-1 | test_auto_tuning_phase2_part_2.py |
| TC-TUNE-4640 | P1 | Threshold pass rate 7/10 | passes=7,total=10 | delta=-1 | test_auto_tuning_phase2_part_2.py |
| TC-TUNE-4641 | P1 | Threshold pass rate 8/10 | passes=8,total=10 | delta=0 | test_auto_tuning_phase2_part_2.py |
| TC-TUNE-4642 | P1 | Threshold pass rate 9/10 | passes=9,total=10 | delta=0 | test_auto_tuning_phase2_part_2.py |
| TC-TUNE-4643 | P1 | Threshold pass rate 10/10 | passes=10,total=10 | delta=1 | test_auto_tuning_phase2_part_2.py |
| TC-TUNE-4644 | P1 | Threshold pass rate 0/15 | passes=0,total=15 | delta=-1 | test_auto_tuning_phase2_part_2.py |
| TC-TUNE-4645 | P1 | Threshold pass rate 1/15 | passes=1,total=15 | delta=-1 | test_auto_tuning_phase2_part_2.py |
| TC-TUNE-4646 | P1 | Threshold pass rate 2/15 | passes=2,total=15 | delta=-1 | test_auto_tuning_phase2_part_2.py |
| TC-TUNE-4647 | P1 | Threshold pass rate 3/15 | passes=3,total=15 | delta=-1 | test_auto_tuning_phase2_part_2.py |
| TC-TUNE-4648 | P1 | Threshold pass rate 4/15 | passes=4,total=15 | delta=-1 | test_auto_tuning_phase2_part_2.py |
| TC-TUNE-4649 | P1 | Threshold pass rate 5/15 | passes=5,total=15 | delta=-1 | test_auto_tuning_phase2_part_2.py |
| TC-TUNE-4650 | P1 | Threshold pass rate 6/15 | passes=6,total=15 | delta=-1 | test_auto_tuning_phase2_part_2.py |
| TC-TUNE-4651 | P1 | Threshold pass rate 7/15 | passes=7,total=15 | delta=-1 | test_auto_tuning_phase2_part_2.py |
| TC-TUNE-4652 | P1 | Threshold pass rate 8/15 | passes=8,total=15 | delta=-1 | test_auto_tuning_phase2_part_2.py |
| TC-TUNE-4653 | P1 | Threshold pass rate 9/15 | passes=9,total=15 | delta=-1 | test_auto_tuning_phase2_part_2.py |
| TC-TUNE-4654 | P1 | Threshold pass rate 10/15 | passes=10,total=15 | delta=-1 | test_auto_tuning_phase2_part_2.py |
| TC-TUNE-4655 | P1 | Threshold pass rate 11/15 | passes=11,total=15 | delta=0 | test_auto_tuning_phase2_part_2.py |
| TC-TUNE-4656 | P1 | Threshold pass rate 12/15 | passes=12,total=15 | delta=0 | test_auto_tuning_phase2_part_2.py |
| TC-TUNE-4657 | P1 | Threshold pass rate 13/15 | passes=13,total=15 | delta=0 | test_auto_tuning_phase2_part_2.py |
| TC-TUNE-4658 | P1 | Threshold pass rate 14/15 | passes=14,total=15 | delta=1 | test_auto_tuning_phase2_part_2.py |
| TC-TUNE-4659 | P1 | Threshold pass rate 15/15 | passes=15,total=15 | delta=1 | test_auto_tuning_phase2_part_3.py |
| TC-TUNE-4660 | P1 | Threshold pass rate 0/20 | passes=0,total=20 | delta=-1 | test_auto_tuning_phase2_part_3.py |
| TC-TUNE-4661 | P1 | Threshold pass rate 1/20 | passes=1,total=20 | delta=-1 | test_auto_tuning_phase2_part_3.py |
| TC-TUNE-4662 | P1 | Threshold pass rate 2/20 | passes=2,total=20 | delta=-1 | test_auto_tuning_phase2_part_3.py |
| TC-TUNE-4663 | P1 | Threshold pass rate 3/20 | passes=3,total=20 | delta=-1 | test_auto_tuning_phase2_part_3.py |
| TC-TUNE-4664 | P1 | Threshold pass rate 4/20 | passes=4,total=20 | delta=-1 | test_auto_tuning_phase2_part_3.py |
| TC-TUNE-4665 | P1 | Threshold pass rate 5/20 | passes=5,total=20 | delta=-1 | test_auto_tuning_phase2_part_3.py |
| TC-TUNE-4666 | P1 | Threshold pass rate 6/20 | passes=6,total=20 | delta=-1 | test_auto_tuning_phase2_part_3.py |
| TC-TUNE-4667 | P1 | Threshold pass rate 7/20 | passes=7,total=20 | delta=-1 | test_auto_tuning_phase2_part_3.py |
| TC-TUNE-4668 | P1 | Threshold pass rate 8/20 | passes=8,total=20 | delta=-1 | test_auto_tuning_phase2_part_3.py |
| TC-TUNE-4669 | P1 | Threshold pass rate 9/20 | passes=9,total=20 | delta=-1 | test_auto_tuning_phase2_part_3.py |
| TC-TUNE-4670 | P1 | Threshold pass rate 10/20 | passes=10,total=20 | delta=-1 | test_auto_tuning_phase2_part_3.py |
| TC-TUNE-4671 | P1 | Threshold pass rate 11/20 | passes=11,total=20 | delta=-1 | test_auto_tuning_phase2_part_3.py |
| TC-TUNE-4672 | P1 | Threshold pass rate 12/20 | passes=12,total=20 | delta=-1 | test_auto_tuning_phase2_part_3.py |
| TC-TUNE-4673 | P1 | Threshold pass rate 13/20 | passes=13,total=20 | delta=-1 | test_auto_tuning_phase2_part_3.py |
| TC-TUNE-4674 | P1 | Threshold pass rate 14/20 | passes=14,total=20 | delta=-1 | test_auto_tuning_phase2_part_3.py |
| TC-TUNE-4675 | P1 | Threshold pass rate 15/20 | passes=15,total=20 | delta=0 | test_auto_tuning_phase2_part_3.py |
| TC-TUNE-4676 | P1 | Threshold pass rate 16/20 | passes=16,total=20 | delta=0 | test_auto_tuning_phase2_part_3.py |
| TC-TUNE-4677 | P1 | Threshold pass rate 17/20 | passes=17,total=20 | delta=0 | test_auto_tuning_phase2_part_3.py |
| TC-TUNE-4678 | P1 | Threshold pass rate 18/20 | passes=18,total=20 | delta=0 | test_auto_tuning_phase2_part_3.py |
| TC-TUNE-4679 | P1 | Threshold pass rate 19/20 | passes=19,total=20 | delta=1 | test_auto_tuning_phase2_part_3.py |
| TC-TUNE-4680 | P1 | Threshold pass rate 20/20 | passes=20,total=20 | delta=1 | test_auto_tuning_phase2_part_3.py |
| TC-TUNE-4681 | P1 | Threshold pass rate 0/30 | passes=0,total=30 | delta=-1 | test_auto_tuning_phase2_part_3.py |
| TC-TUNE-4682 | P1 | Threshold pass rate 1/30 | passes=1,total=30 | delta=-1 | test_auto_tuning_phase2_part_3.py |
| TC-TUNE-4683 | P1 | Threshold pass rate 2/30 | passes=2,total=30 | delta=-1 | test_auto_tuning_phase2_part_3.py |
| TC-TUNE-4684 | P1 | Threshold pass rate 3/30 | passes=3,total=30 | delta=-1 | test_auto_tuning_phase2_part_3.py |
| TC-TUNE-4685 | P1 | Threshold pass rate 4/30 | passes=4,total=30 | delta=-1 | test_auto_tuning_phase2_part_3.py |
| TC-TUNE-4686 | P1 | Threshold pass rate 5/30 | passes=5,total=30 | delta=-1 | test_auto_tuning_phase2_part_3.py |
| TC-TUNE-4687 | P1 | Threshold pass rate 6/30 | passes=6,total=30 | delta=-1 | test_auto_tuning_phase2_part_3.py |
| TC-TUNE-4688 | P1 | Threshold pass rate 7/30 | passes=7,total=30 | delta=-1 | test_auto_tuning_phase2_part_3.py |
| TC-TUNE-4689 | P1 | Threshold pass rate 8/30 | passes=8,total=30 | delta=-1 | test_auto_tuning_phase2_part_3.py |
| TC-TUNE-4690 | P1 | Threshold pass rate 9/30 | passes=9,total=30 | delta=-1 | test_auto_tuning_phase2_part_3.py |
| TC-TUNE-4691 | P1 | Threshold pass rate 10/30 | passes=10,total=30 | delta=-1 | test_auto_tuning_phase2_part_3.py |
| TC-TUNE-4692 | P1 | Threshold pass rate 11/30 | passes=11,total=30 | delta=-1 | test_auto_tuning_phase2_part_3.py |
| TC-TUNE-4693 | P1 | Threshold pass rate 12/30 | passes=12,total=30 | delta=-1 | test_auto_tuning_phase2_part_3.py |
| TC-TUNE-4694 | P1 | Threshold pass rate 13/30 | passes=13,total=30 | delta=-1 | test_auto_tuning_phase2_part_3.py |
| TC-TUNE-4695 | P1 | Threshold pass rate 14/30 | passes=14,total=30 | delta=-1 | test_auto_tuning_phase2_part_3.py |
| TC-TUNE-4696 | P1 | Threshold pass rate 15/30 | passes=15,total=30 | delta=-1 | test_auto_tuning_phase2_part_3.py |
| TC-TUNE-4697 | P1 | Threshold pass rate 16/30 | passes=16,total=30 | delta=-1 | test_auto_tuning_phase2_part_3.py |
| TC-TUNE-4698 | P1 | Threshold pass rate 17/30 | passes=17,total=30 | delta=-1 | test_auto_tuning_phase2_part_3.py |
| TC-TUNE-4699 | P1 | Threshold pass rate 18/30 | passes=18,total=30 | delta=-1 | test_auto_tuning_phase2_part_3.py |
| TC-TUNE-4700 | P1 | Threshold pass rate 19/30 | passes=19,total=30 | delta=-1 | test_auto_tuning_phase2_part_3.py |
| TC-TUNE-4701 | P1 | Threshold pass rate 20/30 | passes=20,total=30 | delta=-1 | test_auto_tuning_phase2_part_3.py |
| TC-TUNE-4702 | P1 | Threshold pass rate 21/30 | passes=21,total=30 | delta=-1 | test_auto_tuning_phase2_part_3.py |
| TC-TUNE-4703 | P1 | Threshold pass rate 22/30 | passes=22,total=30 | delta=0 | test_auto_tuning_phase2_part_3.py |
| TC-TUNE-4704 | P1 | Threshold pass rate 23/30 | passes=23,total=30 | delta=0 | test_auto_tuning_phase2_part_3.py |
| TC-TUNE-4705 | P1 | Threshold pass rate 24/30 | passes=24,total=30 | delta=0 | test_auto_tuning_phase2_part_3.py |
| TC-TUNE-4706 | P1 | Threshold pass rate 25/30 | passes=25,total=30 | delta=0 | test_auto_tuning_phase2_part_3.py |
| TC-TUNE-4707 | P1 | Threshold pass rate 26/30 | passes=26,total=30 | delta=0 | test_auto_tuning_phase2_part_3.py |
| TC-TUNE-4708 | P1 | Threshold pass rate 27/30 | passes=27,total=30 | delta=0 | test_auto_tuning_phase2_part_3.py |
| TC-TUNE-4709 | P1 | Threshold pass rate 28/30 | passes=28,total=30 | delta=1 | test_auto_tuning_phase2_part_3.py |
| TC-TUNE-4710 | P1 | Threshold pass rate 29/30 | passes=29,total=30 | delta=1 | test_auto_tuning_phase2_part_3.py |
| TC-TUNE-4711 | P1 | Threshold pass rate 30/30 | passes=30,total=30 | delta=1 | test_auto_tuning_phase2_part_3.py |
| TC-TUNE-4712 | P1 | Threshold pass rate 0/40 | passes=0,total=40 | delta=-1 | test_auto_tuning_phase2_part_3.py |
| TC-TUNE-4713 | P1 | Threshold pass rate 1/40 | passes=1,total=40 | delta=-1 | test_auto_tuning_phase2_part_3.py |
| TC-TUNE-4714 | P1 | Threshold pass rate 2/40 | passes=2,total=40 | delta=-1 | test_auto_tuning_phase2_part_3.py |
| TC-TUNE-4715 | P1 | Threshold pass rate 3/40 | passes=3,total=40 | delta=-1 | test_auto_tuning_phase2_part_3.py |
| TC-TUNE-4716 | P1 | Threshold pass rate 4/40 | passes=4,total=40 | delta=-1 | test_auto_tuning_phase2_part_3.py |
| TC-TUNE-4717 | P1 | Threshold pass rate 5/40 | passes=5,total=40 | delta=-1 | test_auto_tuning_phase2_part_3.py |
| TC-TUNE-4718 | P1 | Threshold pass rate 6/40 | passes=6,total=40 | delta=-1 | test_auto_tuning_phase2_part_3.py |
| TC-TUNE-4719 | P1 | Threshold pass rate 7/40 | passes=7,total=40 | delta=-1 | test_auto_tuning_phase2_part_3.py |
| TC-TUNE-4720 | P1 | Threshold pass rate 8/40 | passes=8,total=40 | delta=-1 | test_auto_tuning_phase2_part_3.py |
| TC-TUNE-4721 | P1 | Threshold pass rate 9/40 | passes=9,total=40 | delta=-1 | test_auto_tuning_phase2_part_3.py |
| TC-TUNE-4722 | P1 | Threshold pass rate 10/40 | passes=10,total=40 | delta=-1 | test_auto_tuning_phase2_part_3.py |
| TC-TUNE-4723 | P1 | Threshold pass rate 11/40 | passes=11,total=40 | delta=-1 | test_auto_tuning_phase2_part_3.py |
| TC-TUNE-4724 | P1 | Threshold pass rate 12/40 | passes=12,total=40 | delta=-1 | test_auto_tuning_phase2_part_3.py |
| TC-TUNE-4725 | P1 | Threshold pass rate 13/40 | passes=13,total=40 | delta=-1 | test_auto_tuning_phase2_part_3.py |
| TC-TUNE-4726 | P1 | Threshold pass rate 14/40 | passes=14,total=40 | delta=-1 | test_auto_tuning_phase2_part_3.py |
| TC-TUNE-4727 | P1 | Threshold pass rate 15/40 | passes=15,total=40 | delta=-1 | test_auto_tuning_phase2_part_3.py |
| TC-TUNE-4728 | P1 | Threshold pass rate 16/40 | passes=16,total=40 | delta=-1 | test_auto_tuning_phase2_part_3.py |
| TC-TUNE-4729 | P1 | Threshold pass rate 17/40 | passes=17,total=40 | delta=-1 | test_auto_tuning_phase2_part_3.py |
| TC-TUNE-4730 | P1 | Threshold pass rate 18/40 | passes=18,total=40 | delta=-1 | test_auto_tuning_phase2_part_3.py |
| TC-TUNE-4731 | P1 | Threshold pass rate 19/40 | passes=19,total=40 | delta=-1 | test_auto_tuning_phase2_part_3.py |
| TC-TUNE-4732 | P1 | Threshold pass rate 20/40 | passes=20,total=40 | delta=-1 | test_auto_tuning_phase2_part_3.py |
| TC-TUNE-4733 | P1 | Threshold pass rate 21/40 | passes=21,total=40 | delta=-1 | test_auto_tuning_phase2_part_3.py |
| TC-TUNE-4734 | P1 | Threshold pass rate 22/40 | passes=22,total=40 | delta=-1 | test_auto_tuning_phase2_part_3.py |
| TC-TUNE-4735 | P1 | Threshold pass rate 23/40 | passes=23,total=40 | delta=-1 | test_auto_tuning_phase2_part_3.py |
| TC-TUNE-4736 | P1 | Threshold pass rate 24/40 | passes=24,total=40 | delta=-1 | test_auto_tuning_phase2_part_3.py |
| TC-TUNE-4737 | P1 | Threshold pass rate 25/40 | passes=25,total=40 | delta=-1 | test_auto_tuning_phase2_part_3.py |
| TC-TUNE-4738 | P1 | Threshold pass rate 26/40 | passes=26,total=40 | delta=-1 | test_auto_tuning_phase2_part_3.py |
| TC-TUNE-4739 | P1 | Threshold pass rate 27/40 | passes=27,total=40 | delta=-1 | test_auto_tuning_phase2_part_3.py |
| TC-TUNE-4740 | P1 | Threshold pass rate 28/40 | passes=28,total=40 | delta=-1 | test_auto_tuning_phase2_part_3.py |
| TC-TUNE-4741 | P1 | Threshold pass rate 29/40 | passes=29,total=40 | delta=0 | test_auto_tuning_phase2_part_3.py |
| TC-TUNE-4742 | P1 | Threshold pass rate 30/40 | passes=30,total=40 | delta=0 | test_auto_tuning_phase2_part_3.py |
| TC-TUNE-4743 | P1 | Threshold pass rate 31/40 | passes=31,total=40 | delta=0 | test_auto_tuning_phase2_part_3.py |
| TC-TUNE-4744 | P1 | Threshold pass rate 32/40 | passes=32,total=40 | delta=0 | test_auto_tuning_phase2_part_3.py |
| TC-TUNE-4745 | P1 | Threshold pass rate 33/40 | passes=33,total=40 | delta=0 | test_auto_tuning_phase2_part_3.py |
| TC-TUNE-4746 | P1 | Threshold pass rate 34/40 | passes=34,total=40 | delta=0 | test_auto_tuning_phase2_part_3.py |
| TC-TUNE-4747 | P1 | Threshold pass rate 35/40 | passes=35,total=40 | delta=0 | test_auto_tuning_phase2_part_3.py |
| TC-TUNE-4748 | P1 | Threshold pass rate 36/40 | passes=36,total=40 | delta=0 | test_auto_tuning_phase2_part_3.py |
| TC-TUNE-4749 | P1 | Threshold pass rate 37/40 | passes=37,total=40 | delta=1 | test_auto_tuning_phase2_part_3.py |
| TC-TUNE-4750 | P1 | Threshold pass rate 38/40 | passes=38,total=40 | delta=1 | test_auto_tuning_phase2_part_3.py |
| TC-TUNE-4751 | P1 | Threshold pass rate 39/40 | passes=39,total=40 | delta=1 | test_auto_tuning_phase2_part_3.py |
| TC-TUNE-4752 | P1 | Threshold pass rate 40/40 | passes=40,total=40 | delta=1 | test_auto_tuning_phase2_part_3.py |
| TC-TUNE-4753 | P1 | Threshold pass rate 0/50 | passes=0,total=50 | delta=-1 | test_auto_tuning_phase2_part_3.py |
| TC-TUNE-4754 | P1 | Threshold pass rate 1/50 | passes=1,total=50 | delta=-1 | test_auto_tuning_phase2_part_3.py |
| TC-TUNE-4755 | P1 | Threshold pass rate 2/50 | passes=2,total=50 | delta=-1 | test_auto_tuning_phase2_part_3.py |
| TC-TUNE-4756 | P1 | Threshold pass rate 3/50 | passes=3,total=50 | delta=-1 | test_auto_tuning_phase2_part_3.py |
| TC-TUNE-4757 | P1 | Threshold pass rate 4/50 | passes=4,total=50 | delta=-1 | test_auto_tuning_phase2_part_3.py |
| TC-TUNE-4758 | P1 | Threshold pass rate 5/50 | passes=5,total=50 | delta=-1 | test_auto_tuning_phase2_part_3.py |
| TC-TUNE-4759 | P2 | Decay after 0 days from 50 | days_ago=0,initial=50 | value=50 | test_auto_tuning_phase2_part_4.py |
| TC-TUNE-4760 | P2 | Decay after 0 days from 40 | days_ago=0,initial=40 | value=40 | test_auto_tuning_phase2_part_4.py |
| TC-TUNE-4761 | P2 | Decay after 0 days from 30 | days_ago=0,initial=30 | value=30 | test_auto_tuning_phase2_part_4.py |
| TC-TUNE-4762 | P2 | Decay after 0 days from 20 | days_ago=0,initial=20 | value=20 | test_auto_tuning_phase2_part_4.py |
| TC-TUNE-4763 | P2 | Decay after 0 days from 10 | days_ago=0,initial=10 | value=10 | test_auto_tuning_phase2_part_4.py |
| TC-TUNE-4764 | P2 | Decay after 1 days from 50 | days_ago=1,initial=50 | value=50 | test_auto_tuning_phase2_part_4.py |
| TC-TUNE-4765 | P2 | Decay after 1 days from 40 | days_ago=1,initial=40 | value=40 | test_auto_tuning_phase2_part_4.py |
| TC-TUNE-4766 | P2 | Decay after 1 days from 30 | days_ago=1,initial=30 | value=30 | test_auto_tuning_phase2_part_4.py |
| TC-TUNE-4767 | P2 | Decay after 1 days from 20 | days_ago=1,initial=20 | value=20 | test_auto_tuning_phase2_part_4.py |
| TC-TUNE-4768 | P2 | Decay after 1 days from 10 | days_ago=1,initial=10 | value=10 | test_auto_tuning_phase2_part_4.py |
| TC-TUNE-4769 | P2 | Decay after 3 days from 50 | days_ago=3,initial=50 | value=49 | test_auto_tuning_phase2_part_4.py |
| TC-TUNE-4770 | P2 | Decay after 3 days from 40 | days_ago=3,initial=40 | value=39 | test_auto_tuning_phase2_part_4.py |
| TC-TUNE-4771 | P2 | Decay after 3 days from 30 | days_ago=3,initial=30 | value=30 | test_auto_tuning_phase2_part_4.py |
| TC-TUNE-4772 | P2 | Decay after 3 days from 20 | days_ago=3,initial=20 | value=21 | test_auto_tuning_phase2_part_4.py |
| TC-TUNE-4773 | P2 | Decay after 3 days from 10 | days_ago=3,initial=10 | value=11 | test_auto_tuning_phase2_part_4.py |
| TC-TUNE-4774 | P2 | Decay after 7 days from 50 | days_ago=7,initial=50 | value=47 | test_auto_tuning_phase2_part_4.py |
| TC-TUNE-4775 | P2 | Decay after 7 days from 40 | days_ago=7,initial=40 | value=39 | test_auto_tuning_phase2_part_4.py |
| TC-TUNE-4776 | P2 | Decay after 7 days from 30 | days_ago=7,initial=30 | value=30 | test_auto_tuning_phase2_part_4.py |
| TC-TUNE-4777 | P2 | Decay after 7 days from 20 | days_ago=7,initial=20 | value=21 | test_auto_tuning_phase2_part_4.py |
| TC-TUNE-4778 | P2 | Decay after 7 days from 10 | days_ago=7,initial=10 | value=13 | test_auto_tuning_phase2_part_4.py |
| TC-TUNE-4779 | P2 | Decay after 14 days from 50 | days_ago=14,initial=50 | value=44 | test_auto_tuning_phase2_part_4.py |
| TC-TUNE-4780 | P2 | Decay after 14 days from 40 | days_ago=14,initial=40 | value=37 | test_auto_tuning_phase2_part_4.py |
| TC-TUNE-4781 | P2 | Decay after 14 days from 30 | days_ago=14,initial=30 | value=30 | test_auto_tuning_phase2_part_4.py |
| TC-TUNE-4782 | P2 | Decay after 14 days from 20 | days_ago=14,initial=20 | value=23 | test_auto_tuning_phase2_part_4.py |
| TC-TUNE-4783 | P2 | Decay after 14 days from 10 | days_ago=14,initial=10 | value=16 | test_auto_tuning_phase2_part_4.py |
| TC-TUNE-4784 | P2 | Decay after 21 days from 50 | days_ago=21,initial=50 | value=42 | test_auto_tuning_phase2_part_4.py |
| TC-TUNE-4785 | P2 | Decay after 21 days from 40 | days_ago=21,initial=40 | value=36 | test_auto_tuning_phase2_part_4.py |
| TC-TUNE-4786 | P2 | Decay after 21 days from 30 | days_ago=21,initial=30 | value=30 | test_auto_tuning_phase2_part_4.py |
| TC-TUNE-4787 | P2 | Decay after 21 days from 20 | days_ago=21,initial=20 | value=24 | test_auto_tuning_phase2_part_4.py |
| TC-TUNE-4788 | P2 | Decay after 21 days from 10 | days_ago=21,initial=10 | value=18 | test_auto_tuning_phase2_part_4.py |
| TC-TUNE-4789 | P2 | Decay after 30 days from 50 | days_ago=30,initial=50 | value=40 | test_auto_tuning_phase2_part_4.py |
| TC-TUNE-4790 | P2 | Decay after 30 days from 40 | days_ago=30,initial=40 | value=35 | test_auto_tuning_phase2_part_4.py |
| TC-TUNE-4791 | P2 | Decay after 30 days from 30 | days_ago=30,initial=30 | value=30 | test_auto_tuning_phase2_part_4.py |
| TC-TUNE-4792 | P2 | Decay after 30 days from 20 | days_ago=30,initial=20 | value=25 | test_auto_tuning_phase2_part_4.py |
| TC-TUNE-4793 | P2 | Decay after 30 days from 10 | days_ago=30,initial=10 | value=20 | test_auto_tuning_phase2_part_4.py |
| TC-TUNE-4794 | P2 | Decay after 45 days from 50 | days_ago=45,initial=50 | value=37 | test_auto_tuning_phase2_part_4.py |
| TC-TUNE-4795 | P2 | Decay after 45 days from 40 | days_ago=45,initial=40 | value=34 | test_auto_tuning_phase2_part_4.py |
| TC-TUNE-4796 | P2 | Decay after 45 days from 30 | days_ago=45,initial=30 | value=30 | test_auto_tuning_phase2_part_4.py |
| TC-TUNE-4797 | P2 | Decay after 45 days from 20 | days_ago=45,initial=20 | value=26 | test_auto_tuning_phase2_part_4.py |
| TC-TUNE-4798 | P2 | Decay after 45 days from 10 | days_ago=45,initial=10 | value=23 | test_auto_tuning_phase2_part_4.py |
| TC-TUNE-4799 | P2 | Decay after 60 days from 50 | days_ago=60,initial=50 | value=35 | test_auto_tuning_phase2_part_4.py |
| TC-TUNE-4800 | P2 | Decay after 60 days from 40 | days_ago=60,initial=40 | value=32 | test_auto_tuning_phase2_part_4.py |
| TC-TUNE-4801 | P2 | Decay after 60 days from 30 | days_ago=60,initial=30 | value=30 | test_auto_tuning_phase2_part_4.py |
| TC-TUNE-4802 | P2 | Decay after 60 days from 20 | days_ago=60,initial=20 | value=28 | test_auto_tuning_phase2_part_4.py |
| TC-TUNE-4803 | P2 | Decay after 60 days from 10 | days_ago=60,initial=10 | value=25 | test_auto_tuning_phase2_part_4.py |
| TC-TUNE-4804 | P2 | Decay after 90 days from 50 | days_ago=90,initial=50 | value=32 | test_auto_tuning_phase2_part_4.py |
| TC-TUNE-4805 | P2 | Decay after 90 days from 40 | days_ago=90,initial=40 | value=31 | test_auto_tuning_phase2_part_4.py |
| TC-TUNE-4806 | P2 | Decay after 90 days from 30 | days_ago=90,initial=30 | value=30 | test_auto_tuning_phase2_part_4.py |
| TC-TUNE-4807 | P2 | Decay after 90 days from 20 | days_ago=90,initial=20 | value=29 | test_auto_tuning_phase2_part_4.py |
| TC-TUNE-4808 | P2 | Decay after 90 days from 10 | days_ago=90,initial=10 | value=28 | test_auto_tuning_phase2_part_4.py |
| TC-TUNE-4809 | P2 | Decay after 120 days from 50 | days_ago=120,initial=50 | value=31 | test_auto_tuning_phase2_part_4.py |
| TC-TUNE-4810 | P2 | Decay after 120 days from 40 | days_ago=120,initial=40 | value=31 | test_auto_tuning_phase2_part_4.py |
| TC-TUNE-4811 | P2 | Decay after 120 days from 30 | days_ago=120,initial=30 | value=30 | test_auto_tuning_phase2_part_4.py |
| TC-TUNE-4812 | P2 | Decay after 120 days from 20 | days_ago=120,initial=20 | value=29 | test_auto_tuning_phase2_part_4.py |
| TC-TUNE-4813 | P2 | Decay after 120 days from 10 | days_ago=120,initial=10 | value=29 | test_auto_tuning_phase2_part_4.py |
| TC-TUNE-4814 | P2 | Decay after 180 days from 50 | days_ago=180,initial=50 | value=30 | test_auto_tuning_phase2_part_4.py |
| TC-TUNE-4815 | P2 | Decay after 180 days from 40 | days_ago=180,initial=40 | value=30 | test_auto_tuning_phase2_part_4.py |
| TC-TUNE-4816 | P2 | Decay after 180 days from 30 | days_ago=180,initial=30 | value=30 | test_auto_tuning_phase2_part_4.py |
| TC-TUNE-4817 | P2 | Decay after 180 days from 20 | days_ago=180,initial=20 | value=30 | test_auto_tuning_phase2_part_4.py |
| TC-TUNE-4818 | P2 | Decay after 180 days from 10 | days_ago=180,initial=10 | value=30 | test_auto_tuning_phase2_part_4.py |
| TC-TUNE-4819 | P2 | Decay after 300 days from 50 | days_ago=300,initial=50 | value=30 | test_auto_tuning_phase2_part_4.py |
| TC-TUNE-4820 | P2 | Decay after 300 days from 40 | days_ago=300,initial=40 | value=30 | test_auto_tuning_phase2_part_4.py |
| TC-TUNE-4821 | P2 | Decay after 300 days from 30 | days_ago=300,initial=30 | value=30 | test_auto_tuning_phase2_part_4.py |
| TC-TUNE-4822 | P2 | Decay after 300 days from 20 | days_ago=300,initial=20 | value=30 | test_auto_tuning_phase2_part_4.py |
| TC-TUNE-4823 | P2 | Decay after 300 days from 10 | days_ago=300,initial=10 | value=30 | test_auto_tuning_phase2_part_4.py |
| TC-TUNE-4824 | P2 | Decay after 365 days from 50 | days_ago=365,initial=50 | value=30 | test_auto_tuning_phase2_part_4.py |
| TC-TUNE-4825 | P2 | Decay after 365 days from 40 | days_ago=365,initial=40 | value=30 | test_auto_tuning_phase2_part_4.py |
| TC-TUNE-4826 | P2 | Decay after 365 days from 30 | days_ago=365,initial=30 | value=30 | test_auto_tuning_phase2_part_4.py |
| TC-TUNE-4827 | P2 | Decay after 365 days from 20 | days_ago=365,initial=20 | value=30 | test_auto_tuning_phase2_part_4.py |
| TC-TUNE-4828 | P2 | Decay after 365 days from 10 | days_ago=365,initial=10 | value=30 | test_auto_tuning_phase2_part_4.py |
| TC-TUNE-4829 | P2 | Decay after 500 days from 50 | days_ago=500,initial=50 | value=30 | test_auto_tuning_phase2_part_4.py |
| TC-TUNE-4830 | P2 | Decay after 500 days from 40 | days_ago=500,initial=40 | value=30 | test_auto_tuning_phase2_part_4.py |
| TC-TUNE-4831 | P2 | Decay after 500 days from 30 | days_ago=500,initial=30 | value=30 | test_auto_tuning_phase2_part_4.py |
| TC-TUNE-4832 | P2 | Decay after 500 days from 20 | days_ago=500,initial=20 | value=30 | test_auto_tuning_phase2_part_4.py |
| TC-TUNE-4833 | P2 | Decay after 500 days from 10 | days_ago=500,initial=10 | value=30 | test_auto_tuning_phase2_part_4.py |
| TC-TUNE-4834 | P2 | Decay after 730 days from 50 | days_ago=730,initial=50 | value=30 | test_auto_tuning_phase2_part_4.py |
| TC-TUNE-4835 | P2 | Decay after 730 days from 40 | days_ago=730,initial=40 | value=30 | test_auto_tuning_phase2_part_4.py |
| TC-TUNE-4836 | P2 | Decay after 730 days from 30 | days_ago=730,initial=30 | value=30 | test_auto_tuning_phase2_part_4.py |
| TC-TUNE-4837 | P2 | Decay after 730 days from 20 | days_ago=730,initial=20 | value=30 | test_auto_tuning_phase2_part_4.py |
| TC-TUNE-4838 | P2 | Decay after 730 days from 10 | days_ago=730,initial=10 | value=30 | test_auto_tuning_phase2_part_4.py |
| TC-TUNE-4839 | P2 | Decay after 1000 days from 50 | days_ago=1000,initial=50 | value=30 | test_auto_tuning_phase2_part_4.py |
| TC-TUNE-4840 | P2 | Decay after 1000 days from 40 | days_ago=1000,initial=40 | value=30 | test_auto_tuning_phase2_part_4.py |
| TC-TUNE-4841 | P2 | Decay after 1000 days from 30 | days_ago=1000,initial=30 | value=30 | test_auto_tuning_phase2_part_4.py |
| TC-TUNE-4842 | P2 | Decay after 1000 days from 20 | days_ago=1000,initial=20 | value=30 | test_auto_tuning_phase2_part_4.py |
| TC-TUNE-4843 | P2 | Decay after 1000 days from 10 | days_ago=1000,initial=10 | value=30 | test_auto_tuning_phase2_part_4.py |
| TC-TUNE-4844 | P2 | Decay after 1500 days from 50 | days_ago=1500,initial=50 | value=30 | test_auto_tuning_phase2_part_4.py |
| TC-TUNE-4845 | P2 | Decay after 1500 days from 40 | days_ago=1500,initial=40 | value=30 | test_auto_tuning_phase2_part_4.py |
| TC-TUNE-4846 | P2 | Decay after 1500 days from 30 | days_ago=1500,initial=30 | value=30 | test_auto_tuning_phase2_part_4.py |
| TC-TUNE-4847 | P2 | Decay after 1500 days from 20 | days_ago=1500,initial=20 | value=30 | test_auto_tuning_phase2_part_4.py |
| TC-TUNE-4848 | P2 | Decay after 1500 days from 10 | days_ago=1500,initial=10 | value=30 | test_auto_tuning_phase2_part_4.py |
| TC-TUNE-4849 | P2 | Decay after 2000 days from 50 | days_ago=2000,initial=50 | value=30 | test_auto_tuning_phase2_part_4.py |
| TC-TUNE-4850 | P2 | Decay after 2000 days from 40 | days_ago=2000,initial=40 | value=30 | test_auto_tuning_phase2_part_4.py |
| TC-TUNE-4851 | P2 | Decay after 2000 days from 30 | days_ago=2000,initial=30 | value=30 | test_auto_tuning_phase2_part_4.py |
| TC-TUNE-4852 | P2 | Decay after 2000 days from 20 | days_ago=2000,initial=20 | value=30 | test_auto_tuning_phase2_part_4.py |
| TC-TUNE-4853 | P2 | Decay after 2000 days from 10 | days_ago=2000,initial=10 | value=30 | test_auto_tuning_phase2_part_4.py |
| TC-TUNE-4854 | P2 | Decay after 3650 days from 50 | days_ago=3650,initial=50 | value=30 | test_auto_tuning_phase2_part_4.py |
| TC-TUNE-4855 | P2 | Decay after 3650 days from 40 | days_ago=3650,initial=40 | value=30 | test_auto_tuning_phase2_part_4.py |
| TC-TUNE-4856 | P2 | Decay after 3650 days from 30 | days_ago=3650,initial=30 | value=30 | test_auto_tuning_phase2_part_4.py |
| TC-TUNE-4857 | P2 | Decay after 3650 days from 20 | days_ago=3650,initial=20 | value=30 | test_auto_tuning_phase2_part_4.py |
| TC-TUNE-4858 | P2 | Decay after 3650 days from 10 | days_ago=3650,initial=10 | value=30 | test_auto_tuning_phase2_part_4.py |
| TC-TUNE-4859 | P2 | Feedback BLOCK/BLOCK correct=True | verdict=BLOCK,actual=BLOCK,correct=True | stored | test_auto_tuning_phase2_part_5.py |
| TC-TUNE-4860 | P2 | Feedback BLOCK/BLOCK correct=False | verdict=BLOCK,actual=BLOCK,correct=False | stored | test_auto_tuning_phase2_part_5.py |
| TC-TUNE-4861 | P2 | Feedback BLOCK/PASS correct=True | verdict=BLOCK,actual=PASS,correct=True | stored | test_auto_tuning_phase2_part_5.py |
| TC-TUNE-4862 | P2 | Feedback BLOCK/PASS correct=False | verdict=BLOCK,actual=PASS,correct=False | stored | test_auto_tuning_phase2_part_5.py |
| TC-TUNE-4863 | P2 | Feedback PASS/BLOCK correct=True | verdict=PASS,actual=BLOCK,correct=True | stored | test_auto_tuning_phase2_part_5.py |
| TC-TUNE-4864 | P2 | Feedback PASS/BLOCK correct=False | verdict=PASS,actual=BLOCK,correct=False | stored | test_auto_tuning_phase2_part_5.py |
| TC-TUNE-4865 | P2 | Feedback PASS/PASS correct=True | verdict=PASS,actual=PASS,correct=True | stored | test_auto_tuning_phase2_part_5.py |
| TC-TUNE-4866 | P2 | Feedback PASS/PASS correct=False | verdict=PASS,actual=PASS,correct=False | stored | test_auto_tuning_phase2_part_5.py |
| TC-TUNE-4867 | P2 | Feedback REVIEW/BLOCK correct=True | verdict=REVIEW,actual=BLOCK,correct=True | stored | test_auto_tuning_phase2_part_5.py |
| TC-TUNE-4868 | P2 | Feedback REVIEW/BLOCK correct=False | verdict=REVIEW,actual=BLOCK,correct=False | stored | test_auto_tuning_phase2_part_5.py |
| TC-TUNE-4869 | P2 | Feedback REVIEW/PASS correct=True | verdict=REVIEW,actual=PASS,correct=True | stored | test_auto_tuning_phase2_part_5.py |
| TC-TUNE-4870 | P2 | Feedback REVIEW/PASS correct=False | verdict=REVIEW,actual=PASS,correct=False | stored | test_auto_tuning_phase2_part_5.py |
| TC-TUNE-4871 | P3 | Feedback count 1 | count=1 | persisted | test_auto_tuning_phase2_part_5.py |
| TC-TUNE-4872 | P3 | Feedback count 3 | count=3 | persisted | test_auto_tuning_phase2_part_5.py |
| TC-TUNE-4873 | P3 | Feedback count 7 | count=7 | persisted | test_auto_tuning_phase2_part_5.py |
| TC-TUNE-4874 | P3 | Feedback count 12 | count=12 | persisted | test_auto_tuning_phase2_part_5.py |
| TC-TUNE-4875 | P3 | Feedback count 16 | count=16 | persisted | test_auto_tuning_phase2_part_5.py |
| TC-TUNE-4876 | P3 | Feedback count 24 | count=24 | persisted | test_auto_tuning_phase2_part_5.py |
| TC-TUNE-4877 | P3 | Feedback count 25 | count=25 | persisted | test_auto_tuning_phase2_part_5.py |
| TC-TUNE-4878 | P3 | Feedback count 32 | count=32 | persisted | test_auto_tuning_phase2_part_5.py |
| TC-TUNE-4879 | P3 | Feedback count 48 | count=48 | persisted | test_auto_tuning_phase2_part_5.py |
| TC-TUNE-4880 | P3 | Feedback count 100 | count=100 | persisted | test_auto_tuning_phase2_part_5.py |
| TC-TUNE-4881 | P3 | Feedback count 500 | count=500 | persisted | test_auto_tuning_phase2_part_5.py |
| TC-TUNE-4882 | P3 | Feedback count 1000 | count=1000 | persisted | test_auto_tuning_phase2_part_5.py |
| TC-TUNE-4883 | P3 | Feedback count 2000 | count=2000 | persisted | test_auto_tuning_phase2_part_5.py |
| TC-TUNE-4884 | P3 | Feedback count 5000 | count=5000 | persisted | test_auto_tuning_phase2_part_5.py |
| TC-TUNE-4885 | P3 | Report with 1 feedback, 1 decisions | feedback=1,decisions=1 | report valid | test_auto_tuning_phase2_part_5.py |
| TC-TUNE-4886 | P3 | Report with 1 feedback, 2 decisions | feedback=1,decisions=2 | report valid | test_auto_tuning_phase2_part_5.py |
| TC-TUNE-4887 | P3 | Report with 1 feedback, 3 decisions | feedback=1,decisions=3 | report valid | test_auto_tuning_phase2_part_5.py |
| TC-TUNE-4888 | P3 | Report with 1 feedback, 4 decisions | feedback=1,decisions=4 | report valid | test_auto_tuning_phase2_part_5.py |
| TC-TUNE-4889 | P3 | Report with 1 feedback, 5 decisions | feedback=1,decisions=5 | report valid | test_auto_tuning_phase2_part_5.py |
| TC-TUNE-4890 | P3 | Report with 2 feedback, 1 decisions | feedback=2,decisions=1 | report valid | test_auto_tuning_phase2_part_5.py |
| TC-TUNE-4891 | P3 | Report with 2 feedback, 2 decisions | feedback=2,decisions=2 | report valid | test_auto_tuning_phase2_part_5.py |
| TC-TUNE-4892 | P3 | Report with 2 feedback, 3 decisions | feedback=2,decisions=3 | report valid | test_auto_tuning_phase2_part_5.py |
| TC-TUNE-4893 | P3 | Report with 2 feedback, 4 decisions | feedback=2,decisions=4 | report valid | test_auto_tuning_phase2_part_5.py |
| TC-TUNE-4894 | P3 | Report with 2 feedback, 5 decisions | feedback=2,decisions=5 | report valid | test_auto_tuning_phase2_part_5.py |
| TC-TUNE-4895 | P3 | Report with 3 feedback, 1 decisions | feedback=3,decisions=1 | report valid | test_auto_tuning_phase2_part_5.py |
| TC-TUNE-4896 | P3 | Report with 3 feedback, 2 decisions | feedback=3,decisions=2 | report valid | test_auto_tuning_phase2_part_5.py |
| TC-TUNE-4897 | P3 | Report with 3 feedback, 3 decisions | feedback=3,decisions=3 | report valid | test_auto_tuning_phase2_part_5.py |
| TC-TUNE-4898 | P3 | Report with 3 feedback, 4 decisions | feedback=3,decisions=4 | report valid | test_auto_tuning_phase2_part_5.py |
| TC-TUNE-4899 | P3 | Report with 3 feedback, 5 decisions | feedback=3,decisions=5 | report valid | test_auto_tuning_phase2_part_5.py |
| TC-TUNE-4900 | P3 | Report with 4 feedback, 1 decisions | feedback=4,decisions=1 | report valid | test_auto_tuning_phase2_part_5.py |
| TC-TUNE-4901 | P3 | Report with 4 feedback, 2 decisions | feedback=4,decisions=2 | report valid | test_auto_tuning_phase2_part_5.py |
| TC-TUNE-4902 | P3 | Report with 4 feedback, 3 decisions | feedback=4,decisions=3 | report valid | test_auto_tuning_phase2_part_5.py |
| TC-TUNE-4903 | P3 | Report with 4 feedback, 4 decisions | feedback=4,decisions=4 | report valid | test_auto_tuning_phase2_part_5.py |
| TC-TUNE-4904 | P3 | Report with 4 feedback, 5 decisions | feedback=4,decisions=5 | report valid | test_auto_tuning_phase2_part_5.py |
| TC-TUNE-4905 | P3 | Report with 5 feedback, 1 decisions | feedback=5,decisions=1 | report valid | test_auto_tuning_phase2_part_5.py |
| TC-TUNE-4906 | P3 | Report with 5 feedback, 2 decisions | feedback=5,decisions=2 | report valid | test_auto_tuning_phase2_part_5.py |
| TC-TUNE-4907 | P3 | Report with 5 feedback, 3 decisions | feedback=5,decisions=3 | report valid | test_auto_tuning_phase2_part_5.py |
| TC-TUNE-4908 | P3 | Report with 5 feedback, 4 decisions | feedback=5,decisions=4 | report valid | test_auto_tuning_phase2_part_5.py |
| TC-TUNE-4909 | P3 | Report with 5 feedback, 5 decisions | feedback=5,decisions=5 | report valid | test_auto_tuning_phase2_part_5.py |
| TC-TUNE-4910 | P3 | Report with 6 feedback, 1 decisions | feedback=6,decisions=1 | report valid | test_auto_tuning_phase2_part_5.py |
| TC-TUNE-4911 | P3 | Report with 6 feedback, 2 decisions | feedback=6,decisions=2 | report valid | test_auto_tuning_phase2_part_5.py |
| TC-TUNE-4912 | P3 | Report with 6 feedback, 3 decisions | feedback=6,decisions=3 | report valid | test_auto_tuning_phase2_part_5.py |
| TC-TUNE-4913 | P3 | Report with 6 feedback, 4 decisions | feedback=6,decisions=4 | report valid | test_auto_tuning_phase2_part_5.py |
| TC-TUNE-4914 | P3 | Report with 6 feedback, 5 decisions | feedback=6,decisions=5 | report valid | test_auto_tuning_phase2_part_5.py |
| TC-TUNE-4915 | P3 | Report with 7 feedback, 1 decisions | feedback=7,decisions=1 | report valid | test_auto_tuning_phase2_part_5.py |
| TC-TUNE-4916 | P3 | Report with 7 feedback, 2 decisions | feedback=7,decisions=2 | report valid | test_auto_tuning_phase2_part_5.py |
| TC-TUNE-4917 | P3 | Report with 7 feedback, 3 decisions | feedback=7,decisions=3 | report valid | test_auto_tuning_phase2_part_5.py |
| TC-TUNE-4918 | P3 | Report with 7 feedback, 4 decisions | feedback=7,decisions=4 | report valid | test_auto_tuning_phase2_part_5.py |
| TC-TUNE-4919 | P3 | Report with 7 feedback, 5 decisions | feedback=7,decisions=5 | report valid | test_auto_tuning_phase2_part_5.py |
| TC-TUNE-4920 | P3 | Report with 8 feedback, 1 decisions | feedback=8,decisions=1 | report valid | test_auto_tuning_phase2_part_5.py |
| TC-TUNE-4921 | P3 | Report with 8 feedback, 2 decisions | feedback=8,decisions=2 | report valid | test_auto_tuning_phase2_part_5.py |
| TC-TUNE-4922 | P3 | Report with 8 feedback, 3 decisions | feedback=8,decisions=3 | report valid | test_auto_tuning_phase2_part_5.py |
| TC-TUNE-4923 | P3 | Report with 8 feedback, 4 decisions | feedback=8,decisions=4 | report valid | test_auto_tuning_phase2_part_5.py |
| TC-TUNE-4924 | P3 | Report with 8 feedback, 5 decisions | feedback=8,decisions=5 | report valid | test_auto_tuning_phase2_part_5.py |
| TC-TUNE-4925 | P3 | Report with 9 feedback, 1 decisions | feedback=9,decisions=1 | report valid | test_auto_tuning_phase2_part_5.py |
| TC-TUNE-4926 | P3 | Report with 9 feedback, 2 decisions | feedback=9,decisions=2 | report valid | test_auto_tuning_phase2_part_5.py |
| TC-TUNE-4927 | P3 | Report with 9 feedback, 3 decisions | feedback=9,decisions=3 | report valid | test_auto_tuning_phase2_part_5.py |
| TC-TUNE-4928 | P3 | Report with 9 feedback, 4 decisions | feedback=9,decisions=4 | report valid | test_auto_tuning_phase2_part_5.py |
| TC-TUNE-4929 | P3 | Report with 9 feedback, 5 decisions | feedback=9,decisions=5 | report valid | test_auto_tuning_phase2_part_5.py |
| TC-TUNE-4930 | P3 | Report with 10 feedback, 1 decisions | feedback=10,decisions=1 | report valid | test_auto_tuning_phase2_part_5.py |
| TC-TUNE-4931 | P3 | Report with 10 feedback, 2 decisions | feedback=10,decisions=2 | report valid | test_auto_tuning_phase2_part_5.py |
| TC-TUNE-4932 | P3 | Report with 10 feedback, 3 decisions | feedback=10,decisions=3 | report valid | test_auto_tuning_phase2_part_5.py |
| TC-TUNE-4933 | P3 | Report with 10 feedback, 4 decisions | feedback=10,decisions=4 | report valid | test_auto_tuning_phase2_part_5.py |
| TC-TUNE-4934 | P3 | Report with 10 feedback, 5 decisions | feedback=10,decisions=5 | report valid | test_auto_tuning_phase2_part_5.py |
| TC-TUNE-4935 | P3 | Weight clamp WEIGHT_DETECTOR_BADWORDS=5 | key=WEIGHT_DETECTOR_BADWORDS,value=5 | in range | test_auto_tuning_phase2_part_5.py |
| TC-TUNE-4936 | P3 | Weight clamp WEIGHT_DETECTOR_BADWORDS=15 | key=WEIGHT_DETECTOR_BADWORDS,value=15 | in range | test_auto_tuning_phase2_part_5.py |
| TC-TUNE-4937 | P3 | Weight clamp WEIGHT_DETECTOR_BADWORDS=25 | key=WEIGHT_DETECTOR_BADWORDS,value=25 | in range | test_auto_tuning_phase2_part_5.py |
| TC-TUNE-4938 | P3 | Weight clamp WEIGHT_DETECTOR_BADWORDS=35 | key=WEIGHT_DETECTOR_BADWORDS,value=35 | in range | test_auto_tuning_phase2_part_5.py |
| TC-TUNE-4939 | P3 | Weight clamp WEIGHT_DETECTOR_BADWORDS=45 | key=WEIGHT_DETECTOR_BADWORDS,value=45 | in range | test_auto_tuning_phase2_part_5.py |
| TC-TUNE-4940 | P3 | Weight clamp WEIGHT_DETECTOR_BADWORDS=50 | key=WEIGHT_DETECTOR_BADWORDS,value=50 | in range | test_auto_tuning_phase2_part_5.py |
| TC-TUNE-4941 | P3 | Weight clamp WEIGHT_DETECTOR_PROFANITE=5 | key=WEIGHT_DETECTOR_PROFANITE,value=5 | in range | test_auto_tuning_phase2_part_5.py |
| TC-TUNE-4942 | P3 | Weight clamp WEIGHT_DETECTOR_PROFANITE=15 | key=WEIGHT_DETECTOR_PROFANITE,value=15 | in range | test_auto_tuning_phase2_part_5.py |
| TC-TUNE-4943 | P3 | Weight clamp WEIGHT_DETECTOR_PROFANITE=25 | key=WEIGHT_DETECTOR_PROFANITE,value=25 | in range | test_auto_tuning_phase2_part_5.py |
| TC-TUNE-4944 | P3 | Weight clamp WEIGHT_DETECTOR_PROFANITE=35 | key=WEIGHT_DETECTOR_PROFANITE,value=35 | in range | test_auto_tuning_phase2_part_5.py |
| TC-TUNE-4945 | P3 | Weight clamp WEIGHT_DETECTOR_PROFANITE=45 | key=WEIGHT_DETECTOR_PROFANITE,value=45 | in range | test_auto_tuning_phase2_part_5.py |
| TC-TUNE-4946 | P3 | Weight clamp WEIGHT_DETECTOR_PROFANITE=50 | key=WEIGHT_DETECTOR_PROFANITE,value=50 | in range | test_auto_tuning_phase2_part_5.py |
| TC-TUNE-4947 | P3 | Weight clamp WEIGHT_DETECTOR_GLIN=5 | key=WEIGHT_DETECTOR_GLIN,value=5 | in range | test_auto_tuning_phase2_part_5.py |
| TC-TUNE-4948 | P3 | Weight clamp WEIGHT_DETECTOR_GLIN=15 | key=WEIGHT_DETECTOR_GLIN,value=15 | in range | test_auto_tuning_phase2_part_5.py |
| TC-TUNE-4949 | P3 | Weight clamp WEIGHT_DETECTOR_GLIN=25 | key=WEIGHT_DETECTOR_GLIN,value=25 | in range | test_auto_tuning_phase2_part_5.py |
| TC-TUNE-4950 | P3 | Weight clamp WEIGHT_DETECTOR_GLIN=35 | key=WEIGHT_DETECTOR_GLIN,value=35 | in range | test_auto_tuning_phase2_part_5.py |
| TC-TUNE-4951 | P3 | Weight clamp WEIGHT_DETECTOR_GLIN=45 | key=WEIGHT_DETECTOR_GLIN,value=45 | in range | test_auto_tuning_phase2_part_5.py |
| TC-TUNE-4952 | P3 | Weight clamp WEIGHT_DETECTOR_GLIN=50 | key=WEIGHT_DETECTOR_GLIN,value=50 | in range | test_auto_tuning_phase2_part_5.py |
| TC-TUNE-4953 | P3 | Weight clamp WEIGHT_DETECTOR_AHO=5 | key=WEIGHT_DETECTOR_AHO,value=5 | in range | test_auto_tuning_phase2_part_5.py |
| TC-TUNE-4954 | P3 | Weight clamp WEIGHT_DETECTOR_AHO=15 | key=WEIGHT_DETECTOR_AHO,value=15 | in range | test_auto_tuning_phase2_part_5.py |
| TC-TUNE-4955 | P3 | Weight clamp WEIGHT_DETECTOR_AHO=25 | key=WEIGHT_DETECTOR_AHO,value=25 | in range | test_auto_tuning_phase2_part_5.py |
| TC-TUNE-4956 | P3 | Weight clamp WEIGHT_DETECTOR_AHO=35 | key=WEIGHT_DETECTOR_AHO,value=35 | in range | test_auto_tuning_phase2_part_5.py |
| TC-TUNE-4957 | P3 | Weight clamp WEIGHT_DETECTOR_AHO=45 | key=WEIGHT_DETECTOR_AHO,value=45 | in range | test_auto_tuning_phase2_part_5.py |
| TC-TUNE-4958 | P3 | Weight clamp WEIGHT_DETECTOR_AHO=50 | key=WEIGHT_DETECTOR_AHO,value=50 | in range | test_auto_tuning_phase2_part_5.py |
| TC-TUNE-4959 | P3 | Weight clamp WEIGHT_DETECTOR_BKTREE=5 | key=WEIGHT_DETECTOR_BKTREE,value=5 | in range | test_auto_tuning_phase2_part_6.py |
| TC-TUNE-4960 | P3 | Weight clamp WEIGHT_DETECTOR_BKTREE=15 | key=WEIGHT_DETECTOR_BKTREE,value=15 | in range | test_auto_tuning_phase2_part_6.py |
| TC-TUNE-4961 | P3 | Weight clamp WEIGHT_DETECTOR_BKTREE=25 | key=WEIGHT_DETECTOR_BKTREE,value=25 | in range | test_auto_tuning_phase2_part_6.py |
| TC-TUNE-4962 | P3 | Weight clamp WEIGHT_DETECTOR_BKTREE=35 | key=WEIGHT_DETECTOR_BKTREE,value=35 | in range | test_auto_tuning_phase2_part_6.py |
| TC-TUNE-4963 | P3 | Weight clamp WEIGHT_DETECTOR_BKTREE=45 | key=WEIGHT_DETECTOR_BKTREE,value=45 | in range | test_auto_tuning_phase2_part_6.py |
| TC-TUNE-4964 | P3 | Weight clamp WEIGHT_DETECTOR_BKTREE=50 | key=WEIGHT_DETECTOR_BKTREE,value=50 | in range | test_auto_tuning_phase2_part_6.py |
| TC-TUNE-4965 | P3 | Weight clamp WEIGHT_DETECTOR_METAPHONE=5 | key=WEIGHT_DETECTOR_METAPHONE,value=5 | in range | test_auto_tuning_phase2_part_6.py |
| TC-TUNE-4966 | P3 | Weight clamp WEIGHT_DETECTOR_METAPHONE=15 | key=WEIGHT_DETECTOR_METAPHONE,value=15 | in range | test_auto_tuning_phase2_part_6.py |
| TC-TUNE-4967 | P3 | Weight clamp WEIGHT_DETECTOR_METAPHONE=25 | key=WEIGHT_DETECTOR_METAPHONE,value=25 | in range | test_auto_tuning_phase2_part_6.py |
| TC-TUNE-4968 | P3 | Weight clamp WEIGHT_DETECTOR_METAPHONE=35 | key=WEIGHT_DETECTOR_METAPHONE,value=35 | in range | test_auto_tuning_phase2_part_6.py |
| TC-TUNE-4969 | P3 | Weight clamp WEIGHT_DETECTOR_METAPHONE=45 | key=WEIGHT_DETECTOR_METAPHONE,value=45 | in range | test_auto_tuning_phase2_part_6.py |
| TC-TUNE-4970 | P3 | Weight clamp WEIGHT_DETECTOR_METAPHONE=50 | key=WEIGHT_DETECTOR_METAPHONE,value=50 | in range | test_auto_tuning_phase2_part_6.py |
| TC-TUNE-4971 | P3 | Weight clamp WEIGHT_SEMANTIC_POLITICAL=5 | key=WEIGHT_SEMANTIC_POLITICAL,value=5 | in range | test_auto_tuning_phase2_part_6.py |
| TC-TUNE-4972 | P3 | Weight clamp WEIGHT_SEMANTIC_POLITICAL=15 | key=WEIGHT_SEMANTIC_POLITICAL,value=15 | in range | test_auto_tuning_phase2_part_6.py |
| TC-TUNE-4973 | P3 | Weight clamp WEIGHT_SEMANTIC_POLITICAL=25 | key=WEIGHT_SEMANTIC_POLITICAL,value=25 | in range | test_auto_tuning_phase2_part_6.py |
| TC-TUNE-4974 | P3 | Weight clamp WEIGHT_SEMANTIC_POLITICAL=35 | key=WEIGHT_SEMANTIC_POLITICAL,value=35 | in range | test_auto_tuning_phase2_part_6.py |
| TC-TUNE-4975 | P3 | Weight clamp WEIGHT_SEMANTIC_POLITICAL=45 | key=WEIGHT_SEMANTIC_POLITICAL,value=45 | in range | test_auto_tuning_phase2_part_6.py |
| TC-TUNE-4976 | P3 | Weight clamp WEIGHT_SEMANTIC_POLITICAL=50 | key=WEIGHT_SEMANTIC_POLITICAL,value=50 | in range | test_auto_tuning_phase2_part_6.py |
| TC-TUNE-4977 | P3 | Weight clamp WEIGHT_SEMANTIC_VIOLENCE=5 | key=WEIGHT_SEMANTIC_VIOLENCE,value=5 | in range | test_auto_tuning_phase2_part_6.py |
| TC-TUNE-4978 | P3 | Weight clamp WEIGHT_SEMANTIC_VIOLENCE=15 | key=WEIGHT_SEMANTIC_VIOLENCE,value=15 | in range | test_auto_tuning_phase2_part_6.py |
| TC-TUNE-4979 | P3 | Weight clamp WEIGHT_SEMANTIC_VIOLENCE=25 | key=WEIGHT_SEMANTIC_VIOLENCE,value=25 | in range | test_auto_tuning_phase2_part_6.py |
| TC-TUNE-4980 | P3 | Weight clamp WEIGHT_SEMANTIC_VIOLENCE=35 | key=WEIGHT_SEMANTIC_VIOLENCE,value=35 | in range | test_auto_tuning_phase2_part_6.py |
| TC-TUNE-4981 | P3 | Weight clamp WEIGHT_SEMANTIC_VIOLENCE=45 | key=WEIGHT_SEMANTIC_VIOLENCE,value=45 | in range | test_auto_tuning_phase2_part_6.py |
| TC-TUNE-4982 | P3 | Weight clamp WEIGHT_SEMANTIC_VIOLENCE=50 | key=WEIGHT_SEMANTIC_VIOLENCE,value=50 | in range | test_auto_tuning_phase2_part_6.py |
| TC-TUNE-4983 | P3 | Weight clamp WEIGHT_SEMANTIC_SEXUAL=5 | key=WEIGHT_SEMANTIC_SEXUAL,value=5 | in range | test_auto_tuning_phase2_part_6.py |
| TC-TUNE-4984 | P3 | Weight clamp WEIGHT_SEMANTIC_SEXUAL=15 | key=WEIGHT_SEMANTIC_SEXUAL,value=15 | in range | test_auto_tuning_phase2_part_6.py |
| TC-TUNE-4985 | P3 | Weight clamp WEIGHT_SEMANTIC_SEXUAL=25 | key=WEIGHT_SEMANTIC_SEXUAL,value=25 | in range | test_auto_tuning_phase2_part_6.py |
| TC-TUNE-4986 | P3 | Weight clamp WEIGHT_SEMANTIC_SEXUAL=35 | key=WEIGHT_SEMANTIC_SEXUAL,value=35 | in range | test_auto_tuning_phase2_part_6.py |
| TC-TUNE-4987 | P3 | Weight clamp WEIGHT_SEMANTIC_SEXUAL=45 | key=WEIGHT_SEMANTIC_SEXUAL,value=45 | in range | test_auto_tuning_phase2_part_6.py |
| TC-TUNE-4988 | P3 | Weight clamp WEIGHT_SEMANTIC_SEXUAL=50 | key=WEIGHT_SEMANTIC_SEXUAL,value=50 | in range | test_auto_tuning_phase2_part_6.py |
| TC-TUNE-4989 | P3 | Weight clamp WEIGHT_SEMANTIC_HATE=5 | key=WEIGHT_SEMANTIC_HATE,value=5 | in range | test_auto_tuning_phase2_part_6.py |
| TC-TUNE-4990 | P3 | Weight clamp WEIGHT_SEMANTIC_HATE=15 | key=WEIGHT_SEMANTIC_HATE,value=15 | in range | test_auto_tuning_phase2_part_6.py |
| TC-TUNE-4991 | P3 | Weight clamp WEIGHT_SEMANTIC_HATE=25 | key=WEIGHT_SEMANTIC_HATE,value=25 | in range | test_auto_tuning_phase2_part_6.py |
| TC-TUNE-4992 | P3 | Weight clamp WEIGHT_SEMANTIC_HATE=35 | key=WEIGHT_SEMANTIC_HATE,value=35 | in range | test_auto_tuning_phase2_part_6.py |
| TC-TUNE-4993 | P3 | Weight clamp WEIGHT_SEMANTIC_HATE=45 | key=WEIGHT_SEMANTIC_HATE,value=45 | in range | test_auto_tuning_phase2_part_6.py |
| TC-TUNE-4994 | P3 | Weight clamp WEIGHT_SEMANTIC_HATE=50 | key=WEIGHT_SEMANTIC_HATE,value=50 | in range | test_auto_tuning_phase2_part_6.py |
| TC-TUNE-4995 | P3 | Weight clamp WEIGHT_SEMANTIC_PII=5 | key=WEIGHT_SEMANTIC_PII,value=5 | in range | test_auto_tuning_phase2_part_6.py |
| TC-TUNE-4996 | P3 | Weight clamp WEIGHT_SEMANTIC_PII=15 | key=WEIGHT_SEMANTIC_PII,value=15 | in range | test_auto_tuning_phase2_part_6.py |
| TC-TUNE-4997 | P3 | Weight clamp WEIGHT_SEMANTIC_PII=25 | key=WEIGHT_SEMANTIC_PII,value=25 | in range | test_auto_tuning_phase2_part_6.py |
| TC-TUNE-4998 | P3 | Weight clamp WEIGHT_SEMANTIC_PII=35 | key=WEIGHT_SEMANTIC_PII,value=35 | in range | test_auto_tuning_phase2_part_6.py |
| TC-TUNE-4999 | P3 | Weight clamp WEIGHT_SEMANTIC_PII=45 | key=WEIGHT_SEMANTIC_PII,value=45 | in range | test_auto_tuning_phase2_part_6.py |
| TC-TUNE-5000 | P3 | Weight clamp WEIGHT_SEMANTIC_PII=50 | key=WEIGHT_SEMANTIC_PII,value=50 | in range | test_auto_tuning_phase2_part_6.py |
| TC-TUNE-5001 | P3 | Weight clamp WEIGHT_SEMANTIC_ADS=5 | key=WEIGHT_SEMANTIC_ADS,value=5 | in range | test_auto_tuning_phase2_part_6.py |
| TC-TUNE-5002 | P3 | Weight clamp WEIGHT_SEMANTIC_ADS=15 | key=WEIGHT_SEMANTIC_ADS,value=15 | in range | test_auto_tuning_phase2_part_6.py |
| TC-TUNE-5003 | P3 | Weight clamp WEIGHT_SEMANTIC_ADS=25 | key=WEIGHT_SEMANTIC_ADS,value=25 | in range | test_auto_tuning_phase2_part_6.py |
| TC-TUNE-5004 | P3 | Weight clamp WEIGHT_SEMANTIC_ADS=35 | key=WEIGHT_SEMANTIC_ADS,value=35 | in range | test_auto_tuning_phase2_part_6.py |
| TC-TUNE-5005 | P3 | Weight clamp WEIGHT_SEMANTIC_ADS=45 | key=WEIGHT_SEMANTIC_ADS,value=45 | in range | test_auto_tuning_phase2_part_6.py |
| TC-TUNE-5006 | P3 | Weight clamp WEIGHT_SEMANTIC_ADS=50 | key=WEIGHT_SEMANTIC_ADS,value=50 | in range | test_auto_tuning_phase2_part_6.py |
| TC-TUNE-5007 | P3 | Weight clamp WEIGHT_USER=5 | key=WEIGHT_USER,value=5 | in range | test_auto_tuning_phase2_part_6.py |
| TC-TUNE-5008 | P3 | Weight clamp WEIGHT_USER=15 | key=WEIGHT_USER,value=15 | in range | test_auto_tuning_phase2_part_6.py |

### Phase 3 - 10,000 cases
- Planned sweeps over the full dimension matrix, IDs TC-TUNE-0611 onward.

### Phase 4 - 100,000 cases
- Planned high-scale scenarios, IDs TC-TUNE-10611 onward.

### Phase 5 - 939,390 cases
- Planned exhaustive dimension sweep, IDs TC-TUNE-110611 onward.

## Implementation Status
| File | Test Cases | Priority | Status |
| :--- | :--- | :--- | :--- |
| test_auto_tuning_phase2_part_1.py | 4459-4558 | P1 | :white_check_mark: Phase 2 |
| test_auto_tuning_phase2_part_2.py | 4559-4658 | P1 | :white_check_mark: Phase 2 |
| test_auto_tuning_phase2_part_3.py | 4659-4758 | P1 | :white_check_mark: Phase 2 |
| test_auto_tuning_phase2_part_4.py | 4759-4858 | P2 | :white_check_mark: Phase 2 |
| test_auto_tuning_phase2_part_5.py | 4859-4958 | P2 | :white_check_mark: Phase 2 |
| test_auto_tuning_phase2_part_6.py | 4959-5008 | P3 | :white_check_mark: Phase 2 |

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
- Active Learning
- Algorithm Formulations
