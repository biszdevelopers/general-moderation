# Admin API Test Documentation

## Overview
- **Total Planned:** 1,050,000
- **Phase 1:** 50 (IDs TC-ADM-001 to TC-ADM-0050) :white_check_mark: Implemented
- **Phase 2:** 600 (IDs TC-ADM-0051 to TC-ADM-0650) :white_check_mark: Implemented
- **Phase 3:** 10,000 (IDs TC-ADM-0651 to TC-ADM-10650) :hourglass: Planned
- **Phase 4:** 100,000 (IDs TC-ADM-10651 to TC-ADM-110650) :hourglass: Planned
- **Phase 5:** 939,350 (IDs TC-ADM-110651 to TC-ADM-1050000) :hourglass: Planned

## Dimension Matrix
| Dimension | Values (Phase 2) |
| :--- | :--- |
| Endpoint | words, import, export, stats, health, logs, settings, app-config |
| Auth | valid, missing, wrong |
| Word payload | valid, empty, long, unicode, injection |
| App config | or, and, thresholds |
| Settings | valid, invalid, secret |

## Test Case List

### Phase 1 - 50 cases
- 50 cases (word bank, app config, settings).

### Phase 2 (Current) - 600 cases
| ID | Priority | Description | Dimensions | Expected Outcome | File |
| :--- | :--- | :--- | :--- | :--- | :--- |
| TC-ADM-7429 | P1 | Word CRUD other sev=0 lang=en | category=other,severity=0,language=en | roundtrip ok | test_admin_api_phase2_part_1.py |
| TC-ADM-7430 | P1 | Word CRUD other sev=0 lang=zh-CN | category=other,severity=0,language=zh-CN | roundtrip ok | test_admin_api_phase2_part_1.py |
| TC-ADM-7431 | P1 | Word CRUD other sev=0 lang=ru | category=other,severity=0,language=ru | roundtrip ok | test_admin_api_phase2_part_1.py |
| TC-ADM-7432 | P1 | Word CRUD other sev=0 lang=ar | category=other,severity=0,language=ar | roundtrip ok | test_admin_api_phase2_part_1.py |
| TC-ADM-7433 | P1 | Word CRUD other sev=0 lang=ja | category=other,severity=0,language=ja | roundtrip ok | test_admin_api_phase2_part_1.py |
| TC-ADM-7434 | P1 | Word CRUD other sev=1 lang=en | category=other,severity=1,language=en | roundtrip ok | test_admin_api_phase2_part_1.py |
| TC-ADM-7435 | P1 | Word CRUD other sev=1 lang=zh-CN | category=other,severity=1,language=zh-CN | roundtrip ok | test_admin_api_phase2_part_1.py |
| TC-ADM-7436 | P1 | Word CRUD other sev=1 lang=ru | category=other,severity=1,language=ru | roundtrip ok | test_admin_api_phase2_part_1.py |
| TC-ADM-7437 | P1 | Word CRUD other sev=1 lang=ar | category=other,severity=1,language=ar | roundtrip ok | test_admin_api_phase2_part_1.py |
| TC-ADM-7438 | P1 | Word CRUD other sev=1 lang=ja | category=other,severity=1,language=ja | roundtrip ok | test_admin_api_phase2_part_1.py |
| TC-ADM-7439 | P1 | Word CRUD other sev=3 lang=en | category=other,severity=3,language=en | roundtrip ok | test_admin_api_phase2_part_1.py |
| TC-ADM-7440 | P1 | Word CRUD other sev=3 lang=zh-CN | category=other,severity=3,language=zh-CN | roundtrip ok | test_admin_api_phase2_part_1.py |
| TC-ADM-7441 | P1 | Word CRUD other sev=3 lang=ru | category=other,severity=3,language=ru | roundtrip ok | test_admin_api_phase2_part_1.py |
| TC-ADM-7442 | P1 | Word CRUD other sev=3 lang=ar | category=other,severity=3,language=ar | roundtrip ok | test_admin_api_phase2_part_1.py |
| TC-ADM-7443 | P1 | Word CRUD other sev=3 lang=ja | category=other,severity=3,language=ja | roundtrip ok | test_admin_api_phase2_part_1.py |
| TC-ADM-7444 | P1 | Word CRUD other sev=5 lang=en | category=other,severity=5,language=en | roundtrip ok | test_admin_api_phase2_part_1.py |
| TC-ADM-7445 | P1 | Word CRUD other sev=5 lang=zh-CN | category=other,severity=5,language=zh-CN | roundtrip ok | test_admin_api_phase2_part_1.py |
| TC-ADM-7446 | P1 | Word CRUD other sev=5 lang=ru | category=other,severity=5,language=ru | roundtrip ok | test_admin_api_phase2_part_1.py |
| TC-ADM-7447 | P1 | Word CRUD other sev=5 lang=ar | category=other,severity=5,language=ar | roundtrip ok | test_admin_api_phase2_part_1.py |
| TC-ADM-7448 | P1 | Word CRUD other sev=5 lang=ja | category=other,severity=5,language=ja | roundtrip ok | test_admin_api_phase2_part_1.py |
| TC-ADM-7449 | P1 | Word CRUD other sev=7 lang=en | category=other,severity=7,language=en | roundtrip ok | test_admin_api_phase2_part_1.py |
| TC-ADM-7450 | P1 | Word CRUD other sev=7 lang=zh-CN | category=other,severity=7,language=zh-CN | roundtrip ok | test_admin_api_phase2_part_1.py |
| TC-ADM-7451 | P1 | Word CRUD other sev=7 lang=ru | category=other,severity=7,language=ru | roundtrip ok | test_admin_api_phase2_part_1.py |
| TC-ADM-7452 | P1 | Word CRUD other sev=7 lang=ar | category=other,severity=7,language=ar | roundtrip ok | test_admin_api_phase2_part_1.py |
| TC-ADM-7453 | P1 | Word CRUD other sev=7 lang=ja | category=other,severity=7,language=ja | roundtrip ok | test_admin_api_phase2_part_1.py |
| TC-ADM-7454 | P1 | Word CRUD other sev=10 lang=en | category=other,severity=10,language=en | roundtrip ok | test_admin_api_phase2_part_1.py |
| TC-ADM-7455 | P1 | Word CRUD other sev=10 lang=zh-CN | category=other,severity=10,language=zh-CN | roundtrip ok | test_admin_api_phase2_part_1.py |
| TC-ADM-7456 | P1 | Word CRUD other sev=10 lang=ru | category=other,severity=10,language=ru | roundtrip ok | test_admin_api_phase2_part_1.py |
| TC-ADM-7457 | P1 | Word CRUD other sev=10 lang=ar | category=other,severity=10,language=ar | roundtrip ok | test_admin_api_phase2_part_1.py |
| TC-ADM-7458 | P1 | Word CRUD other sev=10 lang=ja | category=other,severity=10,language=ja | roundtrip ok | test_admin_api_phase2_part_1.py |
| TC-ADM-7459 | P1 | Word CRUD hate_speech sev=0 lang=en | category=hate_speech,severity=0,language=en | roundtrip ok | test_admin_api_phase2_part_1.py |
| TC-ADM-7460 | P1 | Word CRUD hate_speech sev=0 lang=zh-CN | category=hate_speech,severity=0,language=zh-CN | roundtrip ok | test_admin_api_phase2_part_1.py |
| TC-ADM-7461 | P1 | Word CRUD hate_speech sev=0 lang=ru | category=hate_speech,severity=0,language=ru | roundtrip ok | test_admin_api_phase2_part_1.py |
| TC-ADM-7462 | P1 | Word CRUD hate_speech sev=0 lang=ar | category=hate_speech,severity=0,language=ar | roundtrip ok | test_admin_api_phase2_part_1.py |
| TC-ADM-7463 | P1 | Word CRUD hate_speech sev=0 lang=ja | category=hate_speech,severity=0,language=ja | roundtrip ok | test_admin_api_phase2_part_1.py |
| TC-ADM-7464 | P1 | Word CRUD hate_speech sev=1 lang=en | category=hate_speech,severity=1,language=en | roundtrip ok | test_admin_api_phase2_part_1.py |
| TC-ADM-7465 | P1 | Word CRUD hate_speech sev=1 lang=zh-CN | category=hate_speech,severity=1,language=zh-CN | roundtrip ok | test_admin_api_phase2_part_1.py |
| TC-ADM-7466 | P1 | Word CRUD hate_speech sev=1 lang=ru | category=hate_speech,severity=1,language=ru | roundtrip ok | test_admin_api_phase2_part_1.py |
| TC-ADM-7467 | P1 | Word CRUD hate_speech sev=1 lang=ar | category=hate_speech,severity=1,language=ar | roundtrip ok | test_admin_api_phase2_part_1.py |
| TC-ADM-7468 | P1 | Word CRUD hate_speech sev=1 lang=ja | category=hate_speech,severity=1,language=ja | roundtrip ok | test_admin_api_phase2_part_1.py |
| TC-ADM-7469 | P1 | Word CRUD hate_speech sev=3 lang=en | category=hate_speech,severity=3,language=en | roundtrip ok | test_admin_api_phase2_part_1.py |
| TC-ADM-7470 | P1 | Word CRUD hate_speech sev=3 lang=zh-CN | category=hate_speech,severity=3,language=zh-CN | roundtrip ok | test_admin_api_phase2_part_1.py |
| TC-ADM-7471 | P1 | Word CRUD hate_speech sev=3 lang=ru | category=hate_speech,severity=3,language=ru | roundtrip ok | test_admin_api_phase2_part_1.py |
| TC-ADM-7472 | P1 | Word CRUD hate_speech sev=3 lang=ar | category=hate_speech,severity=3,language=ar | roundtrip ok | test_admin_api_phase2_part_1.py |
| TC-ADM-7473 | P1 | Word CRUD hate_speech sev=3 lang=ja | category=hate_speech,severity=3,language=ja | roundtrip ok | test_admin_api_phase2_part_1.py |
| TC-ADM-7474 | P1 | Word CRUD hate_speech sev=5 lang=en | category=hate_speech,severity=5,language=en | roundtrip ok | test_admin_api_phase2_part_1.py |
| TC-ADM-7475 | P1 | Word CRUD hate_speech sev=5 lang=zh-CN | category=hate_speech,severity=5,language=zh-CN | roundtrip ok | test_admin_api_phase2_part_1.py |
| TC-ADM-7476 | P1 | Word CRUD hate_speech sev=5 lang=ru | category=hate_speech,severity=5,language=ru | roundtrip ok | test_admin_api_phase2_part_1.py |
| TC-ADM-7477 | P1 | Word CRUD hate_speech sev=5 lang=ar | category=hate_speech,severity=5,language=ar | roundtrip ok | test_admin_api_phase2_part_1.py |
| TC-ADM-7478 | P1 | Word CRUD hate_speech sev=5 lang=ja | category=hate_speech,severity=5,language=ja | roundtrip ok | test_admin_api_phase2_part_1.py |
| TC-ADM-7479 | P1 | Word CRUD hate_speech sev=7 lang=en | category=hate_speech,severity=7,language=en | roundtrip ok | test_admin_api_phase2_part_1.py |
| TC-ADM-7480 | P1 | Word CRUD hate_speech sev=7 lang=zh-CN | category=hate_speech,severity=7,language=zh-CN | roundtrip ok | test_admin_api_phase2_part_1.py |
| TC-ADM-7481 | P1 | Word CRUD hate_speech sev=7 lang=ru | category=hate_speech,severity=7,language=ru | roundtrip ok | test_admin_api_phase2_part_1.py |
| TC-ADM-7482 | P1 | Word CRUD hate_speech sev=7 lang=ar | category=hate_speech,severity=7,language=ar | roundtrip ok | test_admin_api_phase2_part_1.py |
| TC-ADM-7483 | P1 | Word CRUD hate_speech sev=7 lang=ja | category=hate_speech,severity=7,language=ja | roundtrip ok | test_admin_api_phase2_part_1.py |
| TC-ADM-7484 | P1 | Word CRUD hate_speech sev=10 lang=en | category=hate_speech,severity=10,language=en | roundtrip ok | test_admin_api_phase2_part_1.py |
| TC-ADM-7485 | P1 | Word CRUD hate_speech sev=10 lang=zh-CN | category=hate_speech,severity=10,language=zh-CN | roundtrip ok | test_admin_api_phase2_part_1.py |
| TC-ADM-7486 | P1 | Word CRUD hate_speech sev=10 lang=ru | category=hate_speech,severity=10,language=ru | roundtrip ok | test_admin_api_phase2_part_1.py |
| TC-ADM-7487 | P1 | Word CRUD hate_speech sev=10 lang=ar | category=hate_speech,severity=10,language=ar | roundtrip ok | test_admin_api_phase2_part_1.py |
| TC-ADM-7488 | P1 | Word CRUD hate_speech sev=10 lang=ja | category=hate_speech,severity=10,language=ja | roundtrip ok | test_admin_api_phase2_part_1.py |
| TC-ADM-7489 | P1 | Word CRUD violence sev=0 lang=en | category=violence,severity=0,language=en | roundtrip ok | test_admin_api_phase2_part_1.py |
| TC-ADM-7490 | P1 | Word CRUD violence sev=0 lang=zh-CN | category=violence,severity=0,language=zh-CN | roundtrip ok | test_admin_api_phase2_part_1.py |
| TC-ADM-7491 | P1 | Word CRUD violence sev=0 lang=ru | category=violence,severity=0,language=ru | roundtrip ok | test_admin_api_phase2_part_1.py |
| TC-ADM-7492 | P1 | Word CRUD violence sev=0 lang=ar | category=violence,severity=0,language=ar | roundtrip ok | test_admin_api_phase2_part_1.py |
| TC-ADM-7493 | P1 | Word CRUD violence sev=0 lang=ja | category=violence,severity=0,language=ja | roundtrip ok | test_admin_api_phase2_part_1.py |
| TC-ADM-7494 | P1 | Word CRUD violence sev=1 lang=en | category=violence,severity=1,language=en | roundtrip ok | test_admin_api_phase2_part_1.py |
| TC-ADM-7495 | P1 | Word CRUD violence sev=1 lang=zh-CN | category=violence,severity=1,language=zh-CN | roundtrip ok | test_admin_api_phase2_part_1.py |
| TC-ADM-7496 | P1 | Word CRUD violence sev=1 lang=ru | category=violence,severity=1,language=ru | roundtrip ok | test_admin_api_phase2_part_1.py |
| TC-ADM-7497 | P1 | Word CRUD violence sev=1 lang=ar | category=violence,severity=1,language=ar | roundtrip ok | test_admin_api_phase2_part_1.py |
| TC-ADM-7498 | P1 | Word CRUD violence sev=1 lang=ja | category=violence,severity=1,language=ja | roundtrip ok | test_admin_api_phase2_part_1.py |
| TC-ADM-7499 | P1 | Word CRUD violence sev=3 lang=en | category=violence,severity=3,language=en | roundtrip ok | test_admin_api_phase2_part_1.py |
| TC-ADM-7500 | P1 | Word CRUD violence sev=3 lang=zh-CN | category=violence,severity=3,language=zh-CN | roundtrip ok | test_admin_api_phase2_part_1.py |
| TC-ADM-7501 | P1 | Word CRUD violence sev=3 lang=ru | category=violence,severity=3,language=ru | roundtrip ok | test_admin_api_phase2_part_1.py |
| TC-ADM-7502 | P1 | Word CRUD violence sev=3 lang=ar | category=violence,severity=3,language=ar | roundtrip ok | test_admin_api_phase2_part_1.py |
| TC-ADM-7503 | P1 | Word CRUD violence sev=3 lang=ja | category=violence,severity=3,language=ja | roundtrip ok | test_admin_api_phase2_part_1.py |
| TC-ADM-7504 | P1 | Word CRUD violence sev=5 lang=en | category=violence,severity=5,language=en | roundtrip ok | test_admin_api_phase2_part_1.py |
| TC-ADM-7505 | P1 | Word CRUD violence sev=5 lang=zh-CN | category=violence,severity=5,language=zh-CN | roundtrip ok | test_admin_api_phase2_part_1.py |
| TC-ADM-7506 | P1 | Word CRUD violence sev=5 lang=ru | category=violence,severity=5,language=ru | roundtrip ok | test_admin_api_phase2_part_1.py |
| TC-ADM-7507 | P1 | Word CRUD violence sev=5 lang=ar | category=violence,severity=5,language=ar | roundtrip ok | test_admin_api_phase2_part_1.py |
| TC-ADM-7508 | P1 | Word CRUD violence sev=5 lang=ja | category=violence,severity=5,language=ja | roundtrip ok | test_admin_api_phase2_part_1.py |
| TC-ADM-7509 | P1 | Word CRUD violence sev=7 lang=en | category=violence,severity=7,language=en | roundtrip ok | test_admin_api_phase2_part_1.py |
| TC-ADM-7510 | P1 | Word CRUD violence sev=7 lang=zh-CN | category=violence,severity=7,language=zh-CN | roundtrip ok | test_admin_api_phase2_part_1.py |
| TC-ADM-7511 | P1 | Word CRUD violence sev=7 lang=ru | category=violence,severity=7,language=ru | roundtrip ok | test_admin_api_phase2_part_1.py |
| TC-ADM-7512 | P1 | Word CRUD violence sev=7 lang=ar | category=violence,severity=7,language=ar | roundtrip ok | test_admin_api_phase2_part_1.py |
| TC-ADM-7513 | P1 | Word CRUD violence sev=7 lang=ja | category=violence,severity=7,language=ja | roundtrip ok | test_admin_api_phase2_part_1.py |
| TC-ADM-7514 | P1 | Word CRUD violence sev=10 lang=en | category=violence,severity=10,language=en | roundtrip ok | test_admin_api_phase2_part_1.py |
| TC-ADM-7515 | P1 | Word CRUD violence sev=10 lang=zh-CN | category=violence,severity=10,language=zh-CN | roundtrip ok | test_admin_api_phase2_part_1.py |
| TC-ADM-7516 | P1 | Word CRUD violence sev=10 lang=ru | category=violence,severity=10,language=ru | roundtrip ok | test_admin_api_phase2_part_1.py |
| TC-ADM-7517 | P1 | Word CRUD violence sev=10 lang=ar | category=violence,severity=10,language=ar | roundtrip ok | test_admin_api_phase2_part_1.py |
| TC-ADM-7518 | P1 | Word CRUD violence sev=10 lang=ja | category=violence,severity=10,language=ja | roundtrip ok | test_admin_api_phase2_part_1.py |
| TC-ADM-7519 | P1 | Word CRUD sexual sev=0 lang=en | category=sexual,severity=0,language=en | roundtrip ok | test_admin_api_phase2_part_1.py |
| TC-ADM-7520 | P1 | Word CRUD sexual sev=0 lang=zh-CN | category=sexual,severity=0,language=zh-CN | roundtrip ok | test_admin_api_phase2_part_1.py |
| TC-ADM-7521 | P1 | Word CRUD sexual sev=0 lang=ru | category=sexual,severity=0,language=ru | roundtrip ok | test_admin_api_phase2_part_1.py |
| TC-ADM-7522 | P1 | Word CRUD sexual sev=0 lang=ar | category=sexual,severity=0,language=ar | roundtrip ok | test_admin_api_phase2_part_1.py |
| TC-ADM-7523 | P1 | Word CRUD sexual sev=0 lang=ja | category=sexual,severity=0,language=ja | roundtrip ok | test_admin_api_phase2_part_1.py |
| TC-ADM-7524 | P1 | Word CRUD sexual sev=1 lang=en | category=sexual,severity=1,language=en | roundtrip ok | test_admin_api_phase2_part_1.py |
| TC-ADM-7525 | P1 | Word CRUD sexual sev=1 lang=zh-CN | category=sexual,severity=1,language=zh-CN | roundtrip ok | test_admin_api_phase2_part_1.py |
| TC-ADM-7526 | P1 | Word CRUD sexual sev=1 lang=ru | category=sexual,severity=1,language=ru | roundtrip ok | test_admin_api_phase2_part_1.py |
| TC-ADM-7527 | P1 | Word CRUD sexual sev=1 lang=ar | category=sexual,severity=1,language=ar | roundtrip ok | test_admin_api_phase2_part_1.py |
| TC-ADM-7528 | P1 | Word CRUD sexual sev=1 lang=ja | category=sexual,severity=1,language=ja | roundtrip ok | test_admin_api_phase2_part_1.py |
| TC-ADM-7529 | P1 | Word CRUD sexual sev=3 lang=en | category=sexual,severity=3,language=en | roundtrip ok | test_admin_api_phase2_part_2.py |
| TC-ADM-7530 | P1 | Word CRUD sexual sev=3 lang=zh-CN | category=sexual,severity=3,language=zh-CN | roundtrip ok | test_admin_api_phase2_part_2.py |
| TC-ADM-7531 | P1 | Word CRUD sexual sev=3 lang=ru | category=sexual,severity=3,language=ru | roundtrip ok | test_admin_api_phase2_part_2.py |
| TC-ADM-7532 | P1 | Word CRUD sexual sev=3 lang=ar | category=sexual,severity=3,language=ar | roundtrip ok | test_admin_api_phase2_part_2.py |
| TC-ADM-7533 | P1 | Word CRUD sexual sev=3 lang=ja | category=sexual,severity=3,language=ja | roundtrip ok | test_admin_api_phase2_part_2.py |
| TC-ADM-7534 | P1 | Word CRUD sexual sev=5 lang=en | category=sexual,severity=5,language=en | roundtrip ok | test_admin_api_phase2_part_2.py |
| TC-ADM-7535 | P1 | Word CRUD sexual sev=5 lang=zh-CN | category=sexual,severity=5,language=zh-CN | roundtrip ok | test_admin_api_phase2_part_2.py |
| TC-ADM-7536 | P1 | Word CRUD sexual sev=5 lang=ru | category=sexual,severity=5,language=ru | roundtrip ok | test_admin_api_phase2_part_2.py |
| TC-ADM-7537 | P1 | Word CRUD sexual sev=5 lang=ar | category=sexual,severity=5,language=ar | roundtrip ok | test_admin_api_phase2_part_2.py |
| TC-ADM-7538 | P1 | Word CRUD sexual sev=5 lang=ja | category=sexual,severity=5,language=ja | roundtrip ok | test_admin_api_phase2_part_2.py |
| TC-ADM-7539 | P1 | Word CRUD sexual sev=7 lang=en | category=sexual,severity=7,language=en | roundtrip ok | test_admin_api_phase2_part_2.py |
| TC-ADM-7540 | P1 | Word CRUD sexual sev=7 lang=zh-CN | category=sexual,severity=7,language=zh-CN | roundtrip ok | test_admin_api_phase2_part_2.py |
| TC-ADM-7541 | P1 | Word CRUD sexual sev=7 lang=ru | category=sexual,severity=7,language=ru | roundtrip ok | test_admin_api_phase2_part_2.py |
| TC-ADM-7542 | P1 | Word CRUD sexual sev=7 lang=ar | category=sexual,severity=7,language=ar | roundtrip ok | test_admin_api_phase2_part_2.py |
| TC-ADM-7543 | P1 | Word CRUD sexual sev=7 lang=ja | category=sexual,severity=7,language=ja | roundtrip ok | test_admin_api_phase2_part_2.py |
| TC-ADM-7544 | P1 | Word CRUD sexual sev=10 lang=en | category=sexual,severity=10,language=en | roundtrip ok | test_admin_api_phase2_part_2.py |
| TC-ADM-7545 | P1 | Word CRUD sexual sev=10 lang=zh-CN | category=sexual,severity=10,language=zh-CN | roundtrip ok | test_admin_api_phase2_part_2.py |
| TC-ADM-7546 | P1 | Word CRUD sexual sev=10 lang=ru | category=sexual,severity=10,language=ru | roundtrip ok | test_admin_api_phase2_part_2.py |
| TC-ADM-7547 | P1 | Word CRUD sexual sev=10 lang=ar | category=sexual,severity=10,language=ar | roundtrip ok | test_admin_api_phase2_part_2.py |
| TC-ADM-7548 | P1 | Word CRUD sexual sev=10 lang=ja | category=sexual,severity=10,language=ja | roundtrip ok | test_admin_api_phase2_part_2.py |
| TC-ADM-7549 | P1 | Word CRUD political sev=0 lang=en | category=political,severity=0,language=en | roundtrip ok | test_admin_api_phase2_part_2.py |
| TC-ADM-7550 | P1 | Word CRUD political sev=0 lang=zh-CN | category=political,severity=0,language=zh-CN | roundtrip ok | test_admin_api_phase2_part_2.py |
| TC-ADM-7551 | P1 | Word CRUD political sev=0 lang=ru | category=political,severity=0,language=ru | roundtrip ok | test_admin_api_phase2_part_2.py |
| TC-ADM-7552 | P1 | Word CRUD political sev=0 lang=ar | category=political,severity=0,language=ar | roundtrip ok | test_admin_api_phase2_part_2.py |
| TC-ADM-7553 | P1 | Word CRUD political sev=0 lang=ja | category=political,severity=0,language=ja | roundtrip ok | test_admin_api_phase2_part_2.py |
| TC-ADM-7554 | P1 | Word CRUD political sev=1 lang=en | category=political,severity=1,language=en | roundtrip ok | test_admin_api_phase2_part_2.py |
| TC-ADM-7555 | P1 | Word CRUD political sev=1 lang=zh-CN | category=political,severity=1,language=zh-CN | roundtrip ok | test_admin_api_phase2_part_2.py |
| TC-ADM-7556 | P1 | Word CRUD political sev=1 lang=ru | category=political,severity=1,language=ru | roundtrip ok | test_admin_api_phase2_part_2.py |
| TC-ADM-7557 | P1 | Word CRUD political sev=1 lang=ar | category=political,severity=1,language=ar | roundtrip ok | test_admin_api_phase2_part_2.py |
| TC-ADM-7558 | P1 | Word CRUD political sev=1 lang=ja | category=political,severity=1,language=ja | roundtrip ok | test_admin_api_phase2_part_2.py |
| TC-ADM-7559 | P1 | Word CRUD political sev=3 lang=en | category=political,severity=3,language=en | roundtrip ok | test_admin_api_phase2_part_2.py |
| TC-ADM-7560 | P1 | Word CRUD political sev=3 lang=zh-CN | category=political,severity=3,language=zh-CN | roundtrip ok | test_admin_api_phase2_part_2.py |
| TC-ADM-7561 | P1 | Word CRUD political sev=3 lang=ru | category=political,severity=3,language=ru | roundtrip ok | test_admin_api_phase2_part_2.py |
| TC-ADM-7562 | P1 | Word CRUD political sev=3 lang=ar | category=political,severity=3,language=ar | roundtrip ok | test_admin_api_phase2_part_2.py |
| TC-ADM-7563 | P1 | Word CRUD political sev=3 lang=ja | category=political,severity=3,language=ja | roundtrip ok | test_admin_api_phase2_part_2.py |
| TC-ADM-7564 | P1 | Word CRUD political sev=5 lang=en | category=political,severity=5,language=en | roundtrip ok | test_admin_api_phase2_part_2.py |
| TC-ADM-7565 | P1 | Word CRUD political sev=5 lang=zh-CN | category=political,severity=5,language=zh-CN | roundtrip ok | test_admin_api_phase2_part_2.py |
| TC-ADM-7566 | P1 | Word CRUD political sev=5 lang=ru | category=political,severity=5,language=ru | roundtrip ok | test_admin_api_phase2_part_2.py |
| TC-ADM-7567 | P1 | Word CRUD political sev=5 lang=ar | category=political,severity=5,language=ar | roundtrip ok | test_admin_api_phase2_part_2.py |
| TC-ADM-7568 | P1 | Word CRUD political sev=5 lang=ja | category=political,severity=5,language=ja | roundtrip ok | test_admin_api_phase2_part_2.py |
| TC-ADM-7569 | P1 | Word CRUD political sev=7 lang=en | category=political,severity=7,language=en | roundtrip ok | test_admin_api_phase2_part_2.py |
| TC-ADM-7570 | P1 | Word CRUD political sev=7 lang=zh-CN | category=political,severity=7,language=zh-CN | roundtrip ok | test_admin_api_phase2_part_2.py |
| TC-ADM-7571 | P1 | Word CRUD political sev=7 lang=ru | category=political,severity=7,language=ru | roundtrip ok | test_admin_api_phase2_part_2.py |
| TC-ADM-7572 | P1 | Word CRUD political sev=7 lang=ar | category=political,severity=7,language=ar | roundtrip ok | test_admin_api_phase2_part_2.py |
| TC-ADM-7573 | P1 | Word CRUD political sev=7 lang=ja | category=political,severity=7,language=ja | roundtrip ok | test_admin_api_phase2_part_2.py |
| TC-ADM-7574 | P1 | Word CRUD political sev=10 lang=en | category=political,severity=10,language=en | roundtrip ok | test_admin_api_phase2_part_2.py |
| TC-ADM-7575 | P1 | Word CRUD political sev=10 lang=zh-CN | category=political,severity=10,language=zh-CN | roundtrip ok | test_admin_api_phase2_part_2.py |
| TC-ADM-7576 | P1 | Word CRUD political sev=10 lang=ru | category=political,severity=10,language=ru | roundtrip ok | test_admin_api_phase2_part_2.py |
| TC-ADM-7577 | P1 | Word CRUD political sev=10 lang=ar | category=political,severity=10,language=ar | roundtrip ok | test_admin_api_phase2_part_2.py |
| TC-ADM-7578 | P1 | Word CRUD political sev=10 lang=ja | category=political,severity=10,language=ja | roundtrip ok | test_admin_api_phase2_part_2.py |
| TC-ADM-7669 | P1 | Import 1 scenario 0 | size=1,scenario=0 | imported | test_admin_api_phase2_part_2.py |
| TC-ADM-7670 | P1 | Import 1 scenario 1 | size=1,scenario=1 | imported | test_admin_api_phase2_part_2.py |
| TC-ADM-7671 | P1 | Import 1 scenario 2 | size=1,scenario=2 | imported | test_admin_api_phase2_part_2.py |
| TC-ADM-7672 | P1 | Import 1 scenario 3 | size=1,scenario=3 | imported | test_admin_api_phase2_part_2.py |
| TC-ADM-7673 | P1 | Import 1 scenario 4 | size=1,scenario=4 | imported | test_admin_api_phase2_part_2.py |
| TC-ADM-7674 | P1 | Import 1 scenario 5 | size=1,scenario=5 | imported | test_admin_api_phase2_part_2.py |
| TC-ADM-7675 | P1 | Import 1 scenario 6 | size=1,scenario=6 | imported | test_admin_api_phase2_part_2.py |
| TC-ADM-7676 | P1 | Import 1 scenario 7 | size=1,scenario=7 | imported | test_admin_api_phase2_part_2.py |
| TC-ADM-7677 | P1 | Import 1 scenario 8 | size=1,scenario=8 | imported | test_admin_api_phase2_part_2.py |
| TC-ADM-7678 | P1 | Import 1 scenario 9 | size=1,scenario=9 | imported | test_admin_api_phase2_part_2.py |
| TC-ADM-7679 | P1 | Import 1 scenario 10 | size=1,scenario=10 | imported | test_admin_api_phase2_part_2.py |
| TC-ADM-7680 | P1 | Import 1 scenario 11 | size=1,scenario=11 | imported | test_admin_api_phase2_part_2.py |
| TC-ADM-7681 | P1 | Import 1 scenario 12 | size=1,scenario=12 | imported | test_admin_api_phase2_part_2.py |
| TC-ADM-7682 | P1 | Import 1 scenario 13 | size=1,scenario=13 | imported | test_admin_api_phase2_part_2.py |
| TC-ADM-7683 | P1 | Import 1 scenario 14 | size=1,scenario=14 | imported | test_admin_api_phase2_part_2.py |
| TC-ADM-7684 | P1 | Import 2 scenario 0 | size=2,scenario=0 | imported | test_admin_api_phase2_part_2.py |
| TC-ADM-7685 | P1 | Import 2 scenario 1 | size=2,scenario=1 | imported | test_admin_api_phase2_part_2.py |
| TC-ADM-7686 | P1 | Import 2 scenario 2 | size=2,scenario=2 | imported | test_admin_api_phase2_part_2.py |
| TC-ADM-7687 | P1 | Import 2 scenario 3 | size=2,scenario=3 | imported | test_admin_api_phase2_part_2.py |
| TC-ADM-7688 | P1 | Import 2 scenario 4 | size=2,scenario=4 | imported | test_admin_api_phase2_part_2.py |
| TC-ADM-7689 | P1 | Import 2 scenario 5 | size=2,scenario=5 | imported | test_admin_api_phase2_part_2.py |
| TC-ADM-7690 | P1 | Import 2 scenario 6 | size=2,scenario=6 | imported | test_admin_api_phase2_part_2.py |
| TC-ADM-7691 | P1 | Import 2 scenario 7 | size=2,scenario=7 | imported | test_admin_api_phase2_part_2.py |
| TC-ADM-7692 | P1 | Import 2 scenario 8 | size=2,scenario=8 | imported | test_admin_api_phase2_part_2.py |
| TC-ADM-7693 | P1 | Import 2 scenario 9 | size=2,scenario=9 | imported | test_admin_api_phase2_part_2.py |
| TC-ADM-7694 | P1 | Import 2 scenario 10 | size=2,scenario=10 | imported | test_admin_api_phase2_part_2.py |
| TC-ADM-7695 | P1 | Import 2 scenario 11 | size=2,scenario=11 | imported | test_admin_api_phase2_part_2.py |
| TC-ADM-7696 | P1 | Import 2 scenario 12 | size=2,scenario=12 | imported | test_admin_api_phase2_part_2.py |
| TC-ADM-7697 | P1 | Import 2 scenario 13 | size=2,scenario=13 | imported | test_admin_api_phase2_part_2.py |
| TC-ADM-7698 | P1 | Import 2 scenario 14 | size=2,scenario=14 | imported | test_admin_api_phase2_part_2.py |
| TC-ADM-7699 | P1 | Import 5 scenario 0 | size=5,scenario=0 | imported | test_admin_api_phase2_part_2.py |
| TC-ADM-7700 | P1 | Import 5 scenario 1 | size=5,scenario=1 | imported | test_admin_api_phase2_part_2.py |
| TC-ADM-7701 | P1 | Import 5 scenario 2 | size=5,scenario=2 | imported | test_admin_api_phase2_part_2.py |
| TC-ADM-7702 | P1 | Import 5 scenario 3 | size=5,scenario=3 | imported | test_admin_api_phase2_part_2.py |
| TC-ADM-7703 | P1 | Import 5 scenario 4 | size=5,scenario=4 | imported | test_admin_api_phase2_part_2.py |
| TC-ADM-7704 | P1 | Import 5 scenario 5 | size=5,scenario=5 | imported | test_admin_api_phase2_part_2.py |
| TC-ADM-7705 | P1 | Import 5 scenario 6 | size=5,scenario=6 | imported | test_admin_api_phase2_part_2.py |
| TC-ADM-7706 | P1 | Import 5 scenario 7 | size=5,scenario=7 | imported | test_admin_api_phase2_part_2.py |
| TC-ADM-7707 | P1 | Import 5 scenario 8 | size=5,scenario=8 | imported | test_admin_api_phase2_part_2.py |
| TC-ADM-7708 | P1 | Import 5 scenario 9 | size=5,scenario=9 | imported | test_admin_api_phase2_part_2.py |
| TC-ADM-7709 | P1 | Import 5 scenario 10 | size=5,scenario=10 | imported | test_admin_api_phase2_part_2.py |
| TC-ADM-7710 | P1 | Import 5 scenario 11 | size=5,scenario=11 | imported | test_admin_api_phase2_part_2.py |
| TC-ADM-7711 | P1 | Import 5 scenario 12 | size=5,scenario=12 | imported | test_admin_api_phase2_part_2.py |
| TC-ADM-7712 | P1 | Import 5 scenario 13 | size=5,scenario=13 | imported | test_admin_api_phase2_part_2.py |
| TC-ADM-7713 | P1 | Import 5 scenario 14 | size=5,scenario=14 | imported | test_admin_api_phase2_part_2.py |
| TC-ADM-7714 | P1 | Import 10 scenario 0 | size=10,scenario=0 | imported | test_admin_api_phase2_part_2.py |
| TC-ADM-7715 | P1 | Import 10 scenario 1 | size=10,scenario=1 | imported | test_admin_api_phase2_part_2.py |
| TC-ADM-7716 | P1 | Import 10 scenario 2 | size=10,scenario=2 | imported | test_admin_api_phase2_part_2.py |
| TC-ADM-7717 | P1 | Import 10 scenario 3 | size=10,scenario=3 | imported | test_admin_api_phase2_part_2.py |
| TC-ADM-7718 | P1 | Import 10 scenario 4 | size=10,scenario=4 | imported | test_admin_api_phase2_part_2.py |
| TC-ADM-7719 | P1 | Import 10 scenario 5 | size=10,scenario=5 | imported | test_admin_api_phase2_part_3.py |
| TC-ADM-7720 | P1 | Import 10 scenario 6 | size=10,scenario=6 | imported | test_admin_api_phase2_part_3.py |
| TC-ADM-7721 | P1 | Import 10 scenario 7 | size=10,scenario=7 | imported | test_admin_api_phase2_part_3.py |
| TC-ADM-7722 | P1 | Import 10 scenario 8 | size=10,scenario=8 | imported | test_admin_api_phase2_part_3.py |
| TC-ADM-7723 | P1 | Import 10 scenario 9 | size=10,scenario=9 | imported | test_admin_api_phase2_part_3.py |
| TC-ADM-7724 | P1 | Import 10 scenario 10 | size=10,scenario=10 | imported | test_admin_api_phase2_part_3.py |
| TC-ADM-7725 | P1 | Import 10 scenario 11 | size=10,scenario=11 | imported | test_admin_api_phase2_part_3.py |
| TC-ADM-7726 | P1 | Import 10 scenario 12 | size=10,scenario=12 | imported | test_admin_api_phase2_part_3.py |
| TC-ADM-7727 | P1 | Import 10 scenario 13 | size=10,scenario=13 | imported | test_admin_api_phase2_part_3.py |
| TC-ADM-7728 | P1 | Import 10 scenario 14 | size=10,scenario=14 | imported | test_admin_api_phase2_part_3.py |
| TC-ADM-7729 | P1 | Import 25 scenario 0 | size=25,scenario=0 | imported | test_admin_api_phase2_part_3.py |
| TC-ADM-7730 | P1 | Import 25 scenario 1 | size=25,scenario=1 | imported | test_admin_api_phase2_part_3.py |
| TC-ADM-7731 | P1 | Import 25 scenario 2 | size=25,scenario=2 | imported | test_admin_api_phase2_part_3.py |
| TC-ADM-7732 | P1 | Import 25 scenario 3 | size=25,scenario=3 | imported | test_admin_api_phase2_part_3.py |
| TC-ADM-7733 | P1 | Import 25 scenario 4 | size=25,scenario=4 | imported | test_admin_api_phase2_part_3.py |
| TC-ADM-7734 | P1 | Import 25 scenario 5 | size=25,scenario=5 | imported | test_admin_api_phase2_part_3.py |
| TC-ADM-7735 | P1 | Import 25 scenario 6 | size=25,scenario=6 | imported | test_admin_api_phase2_part_3.py |
| TC-ADM-7736 | P1 | Import 25 scenario 7 | size=25,scenario=7 | imported | test_admin_api_phase2_part_3.py |
| TC-ADM-7737 | P1 | Import 25 scenario 8 | size=25,scenario=8 | imported | test_admin_api_phase2_part_3.py |
| TC-ADM-7738 | P1 | Import 25 scenario 9 | size=25,scenario=9 | imported | test_admin_api_phase2_part_3.py |
| TC-ADM-7739 | P1 | Import 25 scenario 10 | size=25,scenario=10 | imported | test_admin_api_phase2_part_3.py |
| TC-ADM-7740 | P1 | Import 25 scenario 11 | size=25,scenario=11 | imported | test_admin_api_phase2_part_3.py |
| TC-ADM-7741 | P1 | Import 25 scenario 12 | size=25,scenario=12 | imported | test_admin_api_phase2_part_3.py |
| TC-ADM-7742 | P1 | Import 25 scenario 13 | size=25,scenario=13 | imported | test_admin_api_phase2_part_3.py |
| TC-ADM-7743 | P1 | Import 25 scenario 14 | size=25,scenario=14 | imported | test_admin_api_phase2_part_3.py |
| TC-ADM-7744 | P1 | Import 50 scenario 0 | size=50,scenario=0 | imported | test_admin_api_phase2_part_3.py |
| TC-ADM-7745 | P1 | Import 50 scenario 1 | size=50,scenario=1 | imported | test_admin_api_phase2_part_3.py |
| TC-ADM-7746 | P1 | Import 50 scenario 2 | size=50,scenario=2 | imported | test_admin_api_phase2_part_3.py |
| TC-ADM-7747 | P1 | Import 50 scenario 3 | size=50,scenario=3 | imported | test_admin_api_phase2_part_3.py |
| TC-ADM-7748 | P1 | Import 50 scenario 4 | size=50,scenario=4 | imported | test_admin_api_phase2_part_3.py |
| TC-ADM-7749 | P1 | Import 50 scenario 5 | size=50,scenario=5 | imported | test_admin_api_phase2_part_3.py |
| TC-ADM-7750 | P1 | Import 50 scenario 6 | size=50,scenario=6 | imported | test_admin_api_phase2_part_3.py |
| TC-ADM-7751 | P1 | Import 50 scenario 7 | size=50,scenario=7 | imported | test_admin_api_phase2_part_3.py |
| TC-ADM-7752 | P1 | Import 50 scenario 8 | size=50,scenario=8 | imported | test_admin_api_phase2_part_3.py |
| TC-ADM-7753 | P1 | Import 50 scenario 9 | size=50,scenario=9 | imported | test_admin_api_phase2_part_3.py |
| TC-ADM-7754 | P1 | Import 50 scenario 10 | size=50,scenario=10 | imported | test_admin_api_phase2_part_3.py |
| TC-ADM-7755 | P1 | Import 50 scenario 11 | size=50,scenario=11 | imported | test_admin_api_phase2_part_3.py |
| TC-ADM-7756 | P1 | Import 50 scenario 12 | size=50,scenario=12 | imported | test_admin_api_phase2_part_3.py |
| TC-ADM-7757 | P1 | Import 50 scenario 13 | size=50,scenario=13 | imported | test_admin_api_phase2_part_3.py |
| TC-ADM-7758 | P1 | Import 50 scenario 14 | size=50,scenario=14 | imported | test_admin_api_phase2_part_3.py |
| TC-ADM-7759 | P1 | Import 100 scenario 0 | size=100,scenario=0 | imported | test_admin_api_phase2_part_3.py |
| TC-ADM-7760 | P1 | Import 100 scenario 1 | size=100,scenario=1 | imported | test_admin_api_phase2_part_3.py |
| TC-ADM-7761 | P1 | Import 100 scenario 2 | size=100,scenario=2 | imported | test_admin_api_phase2_part_3.py |
| TC-ADM-7762 | P1 | Import 100 scenario 3 | size=100,scenario=3 | imported | test_admin_api_phase2_part_3.py |
| TC-ADM-7763 | P1 | Import 100 scenario 4 | size=100,scenario=4 | imported | test_admin_api_phase2_part_3.py |
| TC-ADM-7764 | P1 | Import 100 scenario 5 | size=100,scenario=5 | imported | test_admin_api_phase2_part_3.py |
| TC-ADM-7765 | P1 | Import 100 scenario 6 | size=100,scenario=6 | imported | test_admin_api_phase2_part_3.py |
| TC-ADM-7766 | P1 | Import 100 scenario 7 | size=100,scenario=7 | imported | test_admin_api_phase2_part_3.py |
| TC-ADM-7767 | P1 | Import 100 scenario 8 | size=100,scenario=8 | imported | test_admin_api_phase2_part_3.py |
| TC-ADM-7768 | P1 | Import 100 scenario 9 | size=100,scenario=9 | imported | test_admin_api_phase2_part_3.py |
| TC-ADM-7774 | P1 | App config threshold=0 logic=or boosts=True,True | threshold=0,logic=or,sboost=True,uboost=True | stored | test_admin_api_phase2_part_3.py |
| TC-ADM-7775 | P1 | App config threshold=0 logic=or boosts=True,False | threshold=0,logic=or,sboost=True,uboost=False | stored | test_admin_api_phase2_part_3.py |
| TC-ADM-7776 | P1 | App config threshold=0 logic=or boosts=False,True | threshold=0,logic=or,sboost=False,uboost=True | stored | test_admin_api_phase2_part_3.py |
| TC-ADM-7777 | P1 | App config threshold=0 logic=or boosts=False,False | threshold=0,logic=or,sboost=False,uboost=False | stored | test_admin_api_phase2_part_3.py |
| TC-ADM-7778 | P1 | App config threshold=0 logic=and boosts=True,True | threshold=0,logic=and,sboost=True,uboost=True | stored | test_admin_api_phase2_part_3.py |
| TC-ADM-7779 | P1 | App config threshold=0 logic=and boosts=True,False | threshold=0,logic=and,sboost=True,uboost=False | stored | test_admin_api_phase2_part_3.py |
| TC-ADM-7780 | P1 | App config threshold=0 logic=and boosts=False,True | threshold=0,logic=and,sboost=False,uboost=True | stored | test_admin_api_phase2_part_3.py |
| TC-ADM-7781 | P1 | App config threshold=0 logic=and boosts=False,False | threshold=0,logic=and,sboost=False,uboost=False | stored | test_admin_api_phase2_part_3.py |
| TC-ADM-7782 | P1 | App config threshold=10 logic=or boosts=True,True | threshold=10,logic=or,sboost=True,uboost=True | stored | test_admin_api_phase2_part_3.py |
| TC-ADM-7783 | P1 | App config threshold=10 logic=or boosts=True,False | threshold=10,logic=or,sboost=True,uboost=False | stored | test_admin_api_phase2_part_3.py |
| TC-ADM-7784 | P1 | App config threshold=10 logic=or boosts=False,True | threshold=10,logic=or,sboost=False,uboost=True | stored | test_admin_api_phase2_part_3.py |
| TC-ADM-7785 | P1 | App config threshold=10 logic=or boosts=False,False | threshold=10,logic=or,sboost=False,uboost=False | stored | test_admin_api_phase2_part_3.py |
| TC-ADM-7786 | P1 | App config threshold=10 logic=and boosts=True,True | threshold=10,logic=and,sboost=True,uboost=True | stored | test_admin_api_phase2_part_3.py |
| TC-ADM-7787 | P1 | App config threshold=10 logic=and boosts=True,False | threshold=10,logic=and,sboost=True,uboost=False | stored | test_admin_api_phase2_part_3.py |
| TC-ADM-7788 | P1 | App config threshold=10 logic=and boosts=False,True | threshold=10,logic=and,sboost=False,uboost=True | stored | test_admin_api_phase2_part_3.py |
| TC-ADM-7789 | P1 | App config threshold=10 logic=and boosts=False,False | threshold=10,logic=and,sboost=False,uboost=False | stored | test_admin_api_phase2_part_3.py |
| TC-ADM-7790 | P1 | App config threshold=20 logic=or boosts=True,True | threshold=20,logic=or,sboost=True,uboost=True | stored | test_admin_api_phase2_part_3.py |
| TC-ADM-7791 | P1 | App config threshold=20 logic=or boosts=True,False | threshold=20,logic=or,sboost=True,uboost=False | stored | test_admin_api_phase2_part_3.py |
| TC-ADM-7792 | P1 | App config threshold=20 logic=or boosts=False,True | threshold=20,logic=or,sboost=False,uboost=True | stored | test_admin_api_phase2_part_3.py |
| TC-ADM-7793 | P1 | App config threshold=20 logic=or boosts=False,False | threshold=20,logic=or,sboost=False,uboost=False | stored | test_admin_api_phase2_part_3.py |
| TC-ADM-7794 | P1 | App config threshold=20 logic=and boosts=True,True | threshold=20,logic=and,sboost=True,uboost=True | stored | test_admin_api_phase2_part_3.py |
| TC-ADM-7795 | P1 | App config threshold=20 logic=and boosts=True,False | threshold=20,logic=and,sboost=True,uboost=False | stored | test_admin_api_phase2_part_3.py |
| TC-ADM-7796 | P1 | App config threshold=20 logic=and boosts=False,True | threshold=20,logic=and,sboost=False,uboost=True | stored | test_admin_api_phase2_part_3.py |
| TC-ADM-7797 | P1 | App config threshold=20 logic=and boosts=False,False | threshold=20,logic=and,sboost=False,uboost=False | stored | test_admin_api_phase2_part_3.py |
| TC-ADM-7798 | P1 | App config threshold=30 logic=or boosts=True,True | threshold=30,logic=or,sboost=True,uboost=True | stored | test_admin_api_phase2_part_3.py |
| TC-ADM-7799 | P1 | App config threshold=30 logic=or boosts=True,False | threshold=30,logic=or,sboost=True,uboost=False | stored | test_admin_api_phase2_part_3.py |
| TC-ADM-7800 | P1 | App config threshold=30 logic=or boosts=False,True | threshold=30,logic=or,sboost=False,uboost=True | stored | test_admin_api_phase2_part_3.py |
| TC-ADM-7801 | P1 | App config threshold=30 logic=or boosts=False,False | threshold=30,logic=or,sboost=False,uboost=False | stored | test_admin_api_phase2_part_3.py |
| TC-ADM-7802 | P1 | App config threshold=30 logic=and boosts=True,True | threshold=30,logic=and,sboost=True,uboost=True | stored | test_admin_api_phase2_part_3.py |
| TC-ADM-7803 | P1 | App config threshold=30 logic=and boosts=True,False | threshold=30,logic=and,sboost=True,uboost=False | stored | test_admin_api_phase2_part_3.py |
| TC-ADM-7804 | P1 | App config threshold=30 logic=and boosts=False,True | threshold=30,logic=and,sboost=False,uboost=True | stored | test_admin_api_phase2_part_3.py |
| TC-ADM-7805 | P1 | App config threshold=30 logic=and boosts=False,False | threshold=30,logic=and,sboost=False,uboost=False | stored | test_admin_api_phase2_part_3.py |
| TC-ADM-7806 | P1 | App config threshold=40 logic=or boosts=True,True | threshold=40,logic=or,sboost=True,uboost=True | stored | test_admin_api_phase2_part_3.py |
| TC-ADM-7807 | P1 | App config threshold=40 logic=or boosts=True,False | threshold=40,logic=or,sboost=True,uboost=False | stored | test_admin_api_phase2_part_3.py |
| TC-ADM-7808 | P1 | App config threshold=40 logic=or boosts=False,True | threshold=40,logic=or,sboost=False,uboost=True | stored | test_admin_api_phase2_part_3.py |
| TC-ADM-7809 | P1 | App config threshold=40 logic=or boosts=False,False | threshold=40,logic=or,sboost=False,uboost=False | stored | test_admin_api_phase2_part_3.py |
| TC-ADM-7810 | P1 | App config threshold=40 logic=and boosts=True,True | threshold=40,logic=and,sboost=True,uboost=True | stored | test_admin_api_phase2_part_3.py |
| TC-ADM-7811 | P1 | App config threshold=40 logic=and boosts=True,False | threshold=40,logic=and,sboost=True,uboost=False | stored | test_admin_api_phase2_part_3.py |
| TC-ADM-7812 | P1 | App config threshold=40 logic=and boosts=False,True | threshold=40,logic=and,sboost=False,uboost=True | stored | test_admin_api_phase2_part_3.py |
| TC-ADM-7813 | P1 | App config threshold=40 logic=and boosts=False,False | threshold=40,logic=and,sboost=False,uboost=False | stored | test_admin_api_phase2_part_3.py |
| TC-ADM-7814 | P1 | App config threshold=50 logic=or boosts=True,True | threshold=50,logic=or,sboost=True,uboost=True | stored | test_admin_api_phase2_part_3.py |
| TC-ADM-7815 | P1 | App config threshold=50 logic=or boosts=True,False | threshold=50,logic=or,sboost=True,uboost=False | stored | test_admin_api_phase2_part_3.py |
| TC-ADM-7816 | P1 | App config threshold=50 logic=or boosts=False,True | threshold=50,logic=or,sboost=False,uboost=True | stored | test_admin_api_phase2_part_3.py |
| TC-ADM-7817 | P1 | App config threshold=50 logic=or boosts=False,False | threshold=50,logic=or,sboost=False,uboost=False | stored | test_admin_api_phase2_part_3.py |
| TC-ADM-7818 | P1 | App config threshold=50 logic=and boosts=True,True | threshold=50,logic=and,sboost=True,uboost=True | stored | test_admin_api_phase2_part_3.py |
| TC-ADM-7819 | P1 | App config threshold=50 logic=and boosts=True,False | threshold=50,logic=and,sboost=True,uboost=False | stored | test_admin_api_phase2_part_3.py |
| TC-ADM-7820 | P1 | App config threshold=50 logic=and boosts=False,True | threshold=50,logic=and,sboost=False,uboost=True | stored | test_admin_api_phase2_part_3.py |
| TC-ADM-7821 | P1 | App config threshold=50 logic=and boosts=False,False | threshold=50,logic=and,sboost=False,uboost=False | stored | test_admin_api_phase2_part_3.py |
| TC-ADM-7822 | P1 | App config threshold=60 logic=or boosts=True,True | threshold=60,logic=or,sboost=True,uboost=True | stored | test_admin_api_phase2_part_3.py |
| TC-ADM-7823 | P1 | App config threshold=60 logic=or boosts=True,False | threshold=60,logic=or,sboost=True,uboost=False | stored | test_admin_api_phase2_part_3.py |
| TC-ADM-7824 | P1 | App config threshold=60 logic=or boosts=False,True | threshold=60,logic=or,sboost=False,uboost=True | stored | test_admin_api_phase2_part_4.py |
| TC-ADM-7825 | P1 | App config threshold=60 logic=or boosts=False,False | threshold=60,logic=or,sboost=False,uboost=False | stored | test_admin_api_phase2_part_4.py |
| TC-ADM-7826 | P1 | App config threshold=60 logic=and boosts=True,True | threshold=60,logic=and,sboost=True,uboost=True | stored | test_admin_api_phase2_part_4.py |
| TC-ADM-7827 | P1 | App config threshold=60 logic=and boosts=True,False | threshold=60,logic=and,sboost=True,uboost=False | stored | test_admin_api_phase2_part_4.py |
| TC-ADM-7828 | P1 | App config threshold=60 logic=and boosts=False,True | threshold=60,logic=and,sboost=False,uboost=True | stored | test_admin_api_phase2_part_4.py |
| TC-ADM-7829 | P1 | App config threshold=60 logic=and boosts=False,False | threshold=60,logic=and,sboost=False,uboost=False | stored | test_admin_api_phase2_part_4.py |
| TC-ADM-7830 | P1 | App config threshold=70 logic=or boosts=True,True | threshold=70,logic=or,sboost=True,uboost=True | stored | test_admin_api_phase2_part_4.py |
| TC-ADM-7831 | P1 | App config threshold=70 logic=or boosts=True,False | threshold=70,logic=or,sboost=True,uboost=False | stored | test_admin_api_phase2_part_4.py |
| TC-ADM-7832 | P1 | App config threshold=70 logic=or boosts=False,True | threshold=70,logic=or,sboost=False,uboost=True | stored | test_admin_api_phase2_part_4.py |
| TC-ADM-7833 | P1 | App config threshold=70 logic=or boosts=False,False | threshold=70,logic=or,sboost=False,uboost=False | stored | test_admin_api_phase2_part_4.py |
| TC-ADM-7834 | P1 | App config threshold=70 logic=and boosts=True,True | threshold=70,logic=and,sboost=True,uboost=True | stored | test_admin_api_phase2_part_4.py |
| TC-ADM-7835 | P1 | App config threshold=70 logic=and boosts=True,False | threshold=70,logic=and,sboost=True,uboost=False | stored | test_admin_api_phase2_part_4.py |
| TC-ADM-7836 | P1 | App config threshold=70 logic=and boosts=False,True | threshold=70,logic=and,sboost=False,uboost=True | stored | test_admin_api_phase2_part_4.py |
| TC-ADM-7837 | P1 | App config threshold=70 logic=and boosts=False,False | threshold=70,logic=and,sboost=False,uboost=False | stored | test_admin_api_phase2_part_4.py |
| TC-ADM-7838 | P1 | App config threshold=80 logic=or boosts=True,True | threshold=80,logic=or,sboost=True,uboost=True | stored | test_admin_api_phase2_part_4.py |
| TC-ADM-7839 | P1 | App config threshold=80 logic=or boosts=True,False | threshold=80,logic=or,sboost=True,uboost=False | stored | test_admin_api_phase2_part_4.py |
| TC-ADM-7840 | P1 | App config threshold=80 logic=or boosts=False,True | threshold=80,logic=or,sboost=False,uboost=True | stored | test_admin_api_phase2_part_4.py |
| TC-ADM-7841 | P1 | App config threshold=80 logic=or boosts=False,False | threshold=80,logic=or,sboost=False,uboost=False | stored | test_admin_api_phase2_part_4.py |
| TC-ADM-7842 | P1 | App config threshold=80 logic=and boosts=True,True | threshold=80,logic=and,sboost=True,uboost=True | stored | test_admin_api_phase2_part_4.py |
| TC-ADM-7843 | P1 | App config threshold=80 logic=and boosts=True,False | threshold=80,logic=and,sboost=True,uboost=False | stored | test_admin_api_phase2_part_4.py |
| TC-ADM-7844 | P1 | App config threshold=80 logic=and boosts=False,True | threshold=80,logic=and,sboost=False,uboost=True | stored | test_admin_api_phase2_part_4.py |
| TC-ADM-7845 | P1 | App config threshold=80 logic=and boosts=False,False | threshold=80,logic=and,sboost=False,uboost=False | stored | test_admin_api_phase2_part_4.py |
| TC-ADM-7846 | P1 | App config threshold=90 logic=or boosts=True,True | threshold=90,logic=or,sboost=True,uboost=True | stored | test_admin_api_phase2_part_4.py |
| TC-ADM-7847 | P1 | App config threshold=90 logic=or boosts=True,False | threshold=90,logic=or,sboost=True,uboost=False | stored | test_admin_api_phase2_part_4.py |
| TC-ADM-7848 | P1 | App config threshold=90 logic=or boosts=False,True | threshold=90,logic=or,sboost=False,uboost=True | stored | test_admin_api_phase2_part_4.py |
| TC-ADM-7849 | P1 | App config threshold=90 logic=or boosts=False,False | threshold=90,logic=or,sboost=False,uboost=False | stored | test_admin_api_phase2_part_4.py |
| TC-ADM-7850 | P1 | App config threshold=90 logic=and boosts=True,True | threshold=90,logic=and,sboost=True,uboost=True | stored | test_admin_api_phase2_part_4.py |
| TC-ADM-7851 | P1 | App config threshold=90 logic=and boosts=True,False | threshold=90,logic=and,sboost=True,uboost=False | stored | test_admin_api_phase2_part_4.py |
| TC-ADM-7852 | P1 | App config threshold=90 logic=and boosts=False,True | threshold=90,logic=and,sboost=False,uboost=True | stored | test_admin_api_phase2_part_4.py |
| TC-ADM-7853 | P1 | App config threshold=90 logic=and boosts=False,False | threshold=90,logic=and,sboost=False,uboost=False | stored | test_admin_api_phase2_part_4.py |
| TC-ADM-7854 | P1 | App config threshold=100 logic=or boosts=True,True | threshold=100,logic=or,sboost=True,uboost=True | stored | test_admin_api_phase2_part_4.py |
| TC-ADM-7855 | P1 | App config threshold=100 logic=or boosts=True,False | threshold=100,logic=or,sboost=True,uboost=False | stored | test_admin_api_phase2_part_4.py |
| TC-ADM-7856 | P1 | App config threshold=100 logic=or boosts=False,True | threshold=100,logic=or,sboost=False,uboost=True | stored | test_admin_api_phase2_part_4.py |
| TC-ADM-7857 | P1 | App config threshold=100 logic=or boosts=False,False | threshold=100,logic=or,sboost=False,uboost=False | stored | test_admin_api_phase2_part_4.py |
| TC-ADM-7858 | P1 | App config threshold=100 logic=and boosts=True,True | threshold=100,logic=and,sboost=True,uboost=True | stored | test_admin_api_phase2_part_4.py |
| TC-ADM-7859 | P1 | App config threshold=100 logic=and boosts=True,False | threshold=100,logic=and,sboost=True,uboost=False | stored | test_admin_api_phase2_part_4.py |
| TC-ADM-7860 | P1 | App config threshold=100 logic=and boosts=False,True | threshold=100,logic=and,sboost=False,uboost=True | stored | test_admin_api_phase2_part_4.py |
| TC-ADM-7861 | P1 | App config threshold=100 logic=and boosts=False,False | threshold=100,logic=and,sboost=False,uboost=False | stored | test_admin_api_phase2_part_4.py |
| TC-ADM-7862 | P2 | App config invalid threshold -1 | threshold=-1 | rejected | test_admin_api_phase2_part_4.py |
| TC-ADM-7863 | P2 | App config invalid threshold 101 | threshold=101 | rejected | test_admin_api_phase2_part_4.py |
| TC-ADM-7864 | P2 | App config default lookup 0 | app=ghost0 | defaults | test_admin_api_phase2_part_4.py |
| TC-ADM-7865 | P2 | App config default lookup 1 | app=ghost1 | defaults | test_admin_api_phase2_part_4.py |
| TC-ADM-7866 | P2 | App config default lookup 2 | app=ghost2 | defaults | test_admin_api_phase2_part_4.py |
| TC-ADM-7867 | P2 | App config default lookup 3 | app=ghost3 | defaults | test_admin_api_phase2_part_4.py |
| TC-ADM-7868 | P2 | App config default lookup 4 | app=ghost4 | defaults | test_admin_api_phase2_part_4.py |
| TC-ADM-7869 | P2 | App config default lookup 5 | app=ghost5 | defaults | test_admin_api_phase2_part_4.py |
| TC-ADM-7870 | P2 | App config default lookup 6 | app=ghost6 | defaults | test_admin_api_phase2_part_4.py |
| TC-ADM-7871 | P2 | App config default lookup 7 | app=ghost7 | defaults | test_admin_api_phase2_part_4.py |
| TC-ADM-7872 | P2 | App config default lookup 8 | app=ghost8 | defaults | test_admin_api_phase2_part_4.py |
| TC-ADM-7873 | P2 | App config default lookup 9 | app=ghost9 | defaults | test_admin_api_phase2_part_4.py |
| TC-ADM-7874 | P2 | Settings endpoint WEIGHT_DETECTOR_AHO #0 | key=WEIGHT_DETECTOR_AHO | updated | test_admin_api_phase2_part_4.py |
| TC-ADM-7875 | P2 | Settings endpoint WEIGHT_DETECTOR_AHO #1 | key=WEIGHT_DETECTOR_AHO | updated | test_admin_api_phase2_part_4.py |
| TC-ADM-7876 | P2 | Settings endpoint WEIGHT_DETECTOR_AHO #2 | key=WEIGHT_DETECTOR_AHO | updated | test_admin_api_phase2_part_4.py |
| TC-ADM-7877 | P2 | Settings endpoint WEIGHT_DETECTOR_AHO #3 | key=WEIGHT_DETECTOR_AHO | updated | test_admin_api_phase2_part_4.py |
| TC-ADM-7878 | P2 | Settings endpoint WEIGHT_DETECTOR_AHO #4 | key=WEIGHT_DETECTOR_AHO | updated | test_admin_api_phase2_part_4.py |
| TC-ADM-7879 | P2 | Settings endpoint WEIGHT_DETECTOR_AHO #5 | key=WEIGHT_DETECTOR_AHO | updated | test_admin_api_phase2_part_4.py |
| TC-ADM-7880 | P2 | Settings endpoint WEIGHT_DETECTOR_AHO #6 | key=WEIGHT_DETECTOR_AHO | updated | test_admin_api_phase2_part_4.py |
| TC-ADM-7881 | P2 | Settings endpoint WEIGHT_DETECTOR_AHO #7 | key=WEIGHT_DETECTOR_AHO | updated | test_admin_api_phase2_part_4.py |
| TC-ADM-7882 | P2 | Settings endpoint WEIGHT_DETECTOR_AHO #8 | key=WEIGHT_DETECTOR_AHO | updated | test_admin_api_phase2_part_4.py |
| TC-ADM-7883 | P2 | Settings endpoint WEIGHT_DETECTOR_AHO #9 | key=WEIGHT_DETECTOR_AHO | updated | test_admin_api_phase2_part_4.py |
| TC-ADM-7884 | P2 | Settings endpoint WEIGHT_DETECTOR_AHO #10 | key=WEIGHT_DETECTOR_AHO | updated | test_admin_api_phase2_part_4.py |
| TC-ADM-7885 | P2 | Settings endpoint WEIGHT_DETECTOR_AHO #11 | key=WEIGHT_DETECTOR_AHO | updated | test_admin_api_phase2_part_4.py |
| TC-ADM-7886 | P2 | Settings endpoint WEIGHT_DETECTOR_AHO #12 | key=WEIGHT_DETECTOR_AHO | updated | test_admin_api_phase2_part_4.py |
| TC-ADM-7887 | P2 | Settings endpoint WEIGHT_DETECTOR_AHO #13 | key=WEIGHT_DETECTOR_AHO | updated | test_admin_api_phase2_part_4.py |
| TC-ADM-7888 | P2 | Settings endpoint WEIGHT_DETECTOR_AHO #14 | key=WEIGHT_DETECTOR_AHO | updated | test_admin_api_phase2_part_4.py |
| TC-ADM-7889 | P2 | Settings endpoint WEIGHT_DETECTOR_AHO #15 | key=WEIGHT_DETECTOR_AHO | updated | test_admin_api_phase2_part_4.py |
| TC-ADM-7890 | P2 | Settings endpoint WEIGHT_DETECTOR_AHO #16 | key=WEIGHT_DETECTOR_AHO | updated | test_admin_api_phase2_part_4.py |
| TC-ADM-7891 | P2 | Settings endpoint WEIGHT_DETECTOR_AHO #17 | key=WEIGHT_DETECTOR_AHO | updated | test_admin_api_phase2_part_4.py |
| TC-ADM-7892 | P2 | Settings endpoint WEIGHT_DETECTOR_AHO #18 | key=WEIGHT_DETECTOR_AHO | updated | test_admin_api_phase2_part_4.py |
| TC-ADM-7893 | P2 | Settings endpoint WEIGHT_DETECTOR_AHO #19 | key=WEIGHT_DETECTOR_AHO | updated | test_admin_api_phase2_part_4.py |
| TC-ADM-7894 | P2 | Settings endpoint WEIGHT_USER #0 | key=WEIGHT_USER | updated | test_admin_api_phase2_part_4.py |
| TC-ADM-7895 | P2 | Settings endpoint WEIGHT_USER #1 | key=WEIGHT_USER | updated | test_admin_api_phase2_part_4.py |
| TC-ADM-7896 | P2 | Settings endpoint WEIGHT_USER #2 | key=WEIGHT_USER | updated | test_admin_api_phase2_part_4.py |
| TC-ADM-7897 | P2 | Settings endpoint WEIGHT_USER #3 | key=WEIGHT_USER | updated | test_admin_api_phase2_part_4.py |
| TC-ADM-7898 | P2 | Settings endpoint WEIGHT_USER #4 | key=WEIGHT_USER | updated | test_admin_api_phase2_part_4.py |
| TC-ADM-7899 | P2 | Settings endpoint WEIGHT_USER #5 | key=WEIGHT_USER | updated | test_admin_api_phase2_part_4.py |
| TC-ADM-7900 | P2 | Settings endpoint WEIGHT_USER #6 | key=WEIGHT_USER | updated | test_admin_api_phase2_part_4.py |
| TC-ADM-7901 | P2 | Settings endpoint WEIGHT_USER #7 | key=WEIGHT_USER | updated | test_admin_api_phase2_part_4.py |
| TC-ADM-7902 | P2 | Settings endpoint WEIGHT_USER #8 | key=WEIGHT_USER | updated | test_admin_api_phase2_part_4.py |
| TC-ADM-7903 | P2 | Settings endpoint WEIGHT_USER #9 | key=WEIGHT_USER | updated | test_admin_api_phase2_part_4.py |
| TC-ADM-7904 | P2 | Settings endpoint WEIGHT_USER #10 | key=WEIGHT_USER | updated | test_admin_api_phase2_part_4.py |
| TC-ADM-7905 | P2 | Settings endpoint WEIGHT_USER #11 | key=WEIGHT_USER | updated | test_admin_api_phase2_part_4.py |
| TC-ADM-7906 | P2 | Settings endpoint WEIGHT_USER #12 | key=WEIGHT_USER | updated | test_admin_api_phase2_part_4.py |
| TC-ADM-7907 | P2 | Settings endpoint WEIGHT_USER #13 | key=WEIGHT_USER | updated | test_admin_api_phase2_part_4.py |
| TC-ADM-7908 | P2 | Settings endpoint WEIGHT_USER #14 | key=WEIGHT_USER | updated | test_admin_api_phase2_part_4.py |
| TC-ADM-7909 | P2 | Settings endpoint WEIGHT_USER #15 | key=WEIGHT_USER | updated | test_admin_api_phase2_part_4.py |
| TC-ADM-7910 | P2 | Settings endpoint WEIGHT_USER #16 | key=WEIGHT_USER | updated | test_admin_api_phase2_part_4.py |
| TC-ADM-7911 | P2 | Settings endpoint WEIGHT_USER #17 | key=WEIGHT_USER | updated | test_admin_api_phase2_part_4.py |
| TC-ADM-7912 | P2 | Settings endpoint WEIGHT_USER #18 | key=WEIGHT_USER | updated | test_admin_api_phase2_part_4.py |
| TC-ADM-7913 | P2 | Settings endpoint WEIGHT_USER #19 | key=WEIGHT_USER | updated | test_admin_api_phase2_part_4.py |
| TC-ADM-7914 | P2 | Settings endpoint CACHE_MAX_SIZE #0 | key=CACHE_MAX_SIZE | updated | test_admin_api_phase2_part_4.py |
| TC-ADM-7915 | P2 | Settings endpoint CACHE_MAX_SIZE #1 | key=CACHE_MAX_SIZE | updated | test_admin_api_phase2_part_4.py |
| TC-ADM-7916 | P2 | Settings endpoint CACHE_MAX_SIZE #2 | key=CACHE_MAX_SIZE | updated | test_admin_api_phase2_part_4.py |
| TC-ADM-7917 | P2 | Settings endpoint CACHE_MAX_SIZE #3 | key=CACHE_MAX_SIZE | updated | test_admin_api_phase2_part_4.py |
| TC-ADM-7918 | P2 | Settings endpoint CACHE_MAX_SIZE #4 | key=CACHE_MAX_SIZE | updated | test_admin_api_phase2_part_4.py |
| TC-ADM-7919 | P2 | Settings endpoint CACHE_MAX_SIZE #5 | key=CACHE_MAX_SIZE | updated | test_admin_api_phase2_part_4.py |
| TC-ADM-7920 | P2 | Settings endpoint CACHE_MAX_SIZE #6 | key=CACHE_MAX_SIZE | updated | test_admin_api_phase2_part_4.py |
| TC-ADM-7921 | P2 | Settings endpoint CACHE_MAX_SIZE #7 | key=CACHE_MAX_SIZE | updated | test_admin_api_phase2_part_4.py |
| TC-ADM-7922 | P2 | Settings endpoint CACHE_MAX_SIZE #8 | key=CACHE_MAX_SIZE | updated | test_admin_api_phase2_part_4.py |
| TC-ADM-7923 | P2 | Settings endpoint CACHE_MAX_SIZE #9 | key=CACHE_MAX_SIZE | updated | test_admin_api_phase2_part_4.py |
| TC-ADM-7924 | P2 | Settings endpoint CACHE_MAX_SIZE #10 | key=CACHE_MAX_SIZE | updated | test_admin_api_phase2_part_5.py |
| TC-ADM-7925 | P2 | Settings endpoint CACHE_MAX_SIZE #11 | key=CACHE_MAX_SIZE | updated | test_admin_api_phase2_part_5.py |
| TC-ADM-7926 | P2 | Settings endpoint CACHE_MAX_SIZE #12 | key=CACHE_MAX_SIZE | updated | test_admin_api_phase2_part_5.py |
| TC-ADM-7927 | P2 | Settings endpoint CACHE_MAX_SIZE #13 | key=CACHE_MAX_SIZE | updated | test_admin_api_phase2_part_5.py |
| TC-ADM-7928 | P2 | Settings endpoint CACHE_MAX_SIZE #14 | key=CACHE_MAX_SIZE | updated | test_admin_api_phase2_part_5.py |
| TC-ADM-7929 | P2 | Settings endpoint CACHE_MAX_SIZE #15 | key=CACHE_MAX_SIZE | updated | test_admin_api_phase2_part_5.py |
| TC-ADM-7930 | P2 | Settings endpoint CACHE_MAX_SIZE #16 | key=CACHE_MAX_SIZE | updated | test_admin_api_phase2_part_5.py |
| TC-ADM-7931 | P2 | Settings endpoint CACHE_MAX_SIZE #17 | key=CACHE_MAX_SIZE | updated | test_admin_api_phase2_part_5.py |
| TC-ADM-7932 | P2 | Settings endpoint CACHE_MAX_SIZE #18 | key=CACHE_MAX_SIZE | updated | test_admin_api_phase2_part_5.py |
| TC-ADM-7933 | P2 | Settings endpoint CACHE_MAX_SIZE #19 | key=CACHE_MAX_SIZE | updated | test_admin_api_phase2_part_5.py |
| TC-ADM-7934 | P2 | Settings endpoint SAFE_WORD_ENABLED #0 | key=SAFE_WORD_ENABLED | updated | test_admin_api_phase2_part_5.py |
| TC-ADM-7935 | P2 | Settings endpoint SAFE_WORD_ENABLED #1 | key=SAFE_WORD_ENABLED | updated | test_admin_api_phase2_part_5.py |
| TC-ADM-7936 | P2 | Settings endpoint SAFE_WORD_ENABLED #2 | key=SAFE_WORD_ENABLED | updated | test_admin_api_phase2_part_5.py |
| TC-ADM-7937 | P2 | Settings endpoint SAFE_WORD_ENABLED #3 | key=SAFE_WORD_ENABLED | updated | test_admin_api_phase2_part_5.py |
| TC-ADM-7938 | P2 | Settings endpoint SAFE_WORD_ENABLED #4 | key=SAFE_WORD_ENABLED | updated | test_admin_api_phase2_part_5.py |
| TC-ADM-7939 | P2 | Settings endpoint SAFE_WORD_ENABLED #5 | key=SAFE_WORD_ENABLED | updated | test_admin_api_phase2_part_5.py |
| TC-ADM-7940 | P2 | Settings endpoint SAFE_WORD_ENABLED #6 | key=SAFE_WORD_ENABLED | updated | test_admin_api_phase2_part_5.py |
| TC-ADM-7941 | P2 | Settings endpoint SAFE_WORD_ENABLED #7 | key=SAFE_WORD_ENABLED | updated | test_admin_api_phase2_part_5.py |
| TC-ADM-7942 | P2 | Settings endpoint SAFE_WORD_ENABLED #8 | key=SAFE_WORD_ENABLED | updated | test_admin_api_phase2_part_5.py |
| TC-ADM-7943 | P2 | Settings endpoint SAFE_WORD_ENABLED #9 | key=SAFE_WORD_ENABLED | updated | test_admin_api_phase2_part_5.py |
| TC-ADM-7944 | P2 | Settings endpoint SAFE_WORD_ENABLED #10 | key=SAFE_WORD_ENABLED | updated | test_admin_api_phase2_part_5.py |
| TC-ADM-7945 | P2 | Settings endpoint SAFE_WORD_ENABLED #11 | key=SAFE_WORD_ENABLED | updated | test_admin_api_phase2_part_5.py |
| TC-ADM-7946 | P2 | Settings endpoint SAFE_WORD_ENABLED #12 | key=SAFE_WORD_ENABLED | updated | test_admin_api_phase2_part_5.py |
| TC-ADM-7947 | P2 | Settings endpoint SAFE_WORD_ENABLED #13 | key=SAFE_WORD_ENABLED | updated | test_admin_api_phase2_part_5.py |
| TC-ADM-7948 | P2 | Settings endpoint SAFE_WORD_ENABLED #14 | key=SAFE_WORD_ENABLED | updated | test_admin_api_phase2_part_5.py |
| TC-ADM-7949 | P2 | Settings endpoint SAFE_WORD_ENABLED #15 | key=SAFE_WORD_ENABLED | updated | test_admin_api_phase2_part_5.py |
| TC-ADM-7950 | P2 | Settings endpoint SAFE_WORD_ENABLED #16 | key=SAFE_WORD_ENABLED | updated | test_admin_api_phase2_part_5.py |
| TC-ADM-7951 | P2 | Settings endpoint SAFE_WORD_ENABLED #17 | key=SAFE_WORD_ENABLED | updated | test_admin_api_phase2_part_5.py |
| TC-ADM-7952 | P2 | Settings endpoint SAFE_WORD_ENABLED #18 | key=SAFE_WORD_ENABLED | updated | test_admin_api_phase2_part_5.py |
| TC-ADM-7953 | P2 | Settings endpoint SAFE_WORD_ENABLED #19 | key=SAFE_WORD_ENABLED | updated | test_admin_api_phase2_part_5.py |
| TC-ADM-7954 | P2 | Settings endpoint SEMANTIC_TOP_K #0 | key=SEMANTIC_TOP_K | updated | test_admin_api_phase2_part_5.py |
| TC-ADM-7955 | P2 | Settings endpoint SEMANTIC_TOP_K #1 | key=SEMANTIC_TOP_K | updated | test_admin_api_phase2_part_5.py |
| TC-ADM-7956 | P2 | Settings endpoint SEMANTIC_TOP_K #2 | key=SEMANTIC_TOP_K | updated | test_admin_api_phase2_part_5.py |
| TC-ADM-7957 | P2 | Settings endpoint SEMANTIC_TOP_K #3 | key=SEMANTIC_TOP_K | updated | test_admin_api_phase2_part_5.py |
| TC-ADM-7958 | P2 | Settings endpoint SEMANTIC_TOP_K #4 | key=SEMANTIC_TOP_K | updated | test_admin_api_phase2_part_5.py |
| TC-ADM-7959 | P2 | Settings endpoint SEMANTIC_TOP_K #5 | key=SEMANTIC_TOP_K | updated | test_admin_api_phase2_part_5.py |
| TC-ADM-7960 | P2 | Settings endpoint SEMANTIC_TOP_K #6 | key=SEMANTIC_TOP_K | updated | test_admin_api_phase2_part_5.py |
| TC-ADM-7961 | P2 | Settings endpoint SEMANTIC_TOP_K #7 | key=SEMANTIC_TOP_K | updated | test_admin_api_phase2_part_5.py |
| TC-ADM-7962 | P2 | Settings endpoint SEMANTIC_TOP_K #8 | key=SEMANTIC_TOP_K | updated | test_admin_api_phase2_part_5.py |
| TC-ADM-7963 | P2 | Settings endpoint SEMANTIC_TOP_K #9 | key=SEMANTIC_TOP_K | updated | test_admin_api_phase2_part_5.py |
| TC-ADM-7964 | P2 | Settings endpoint SEMANTIC_TOP_K #10 | key=SEMANTIC_TOP_K | updated | test_admin_api_phase2_part_5.py |
| TC-ADM-7965 | P2 | Settings endpoint SEMANTIC_TOP_K #11 | key=SEMANTIC_TOP_K | updated | test_admin_api_phase2_part_5.py |
| TC-ADM-7966 | P2 | Settings endpoint SEMANTIC_TOP_K #12 | key=SEMANTIC_TOP_K | updated | test_admin_api_phase2_part_5.py |
| TC-ADM-7967 | P2 | Settings endpoint SEMANTIC_TOP_K #13 | key=SEMANTIC_TOP_K | updated | test_admin_api_phase2_part_5.py |
| TC-ADM-7968 | P2 | Settings endpoint SEMANTIC_TOP_K #14 | key=SEMANTIC_TOP_K | updated | test_admin_api_phase2_part_5.py |
| TC-ADM-7969 | P2 | Settings endpoint SEMANTIC_TOP_K #15 | key=SEMANTIC_TOP_K | updated | test_admin_api_phase2_part_5.py |
| TC-ADM-7970 | P2 | Settings endpoint SEMANTIC_TOP_K #16 | key=SEMANTIC_TOP_K | updated | test_admin_api_phase2_part_5.py |
| TC-ADM-7971 | P2 | Settings endpoint SEMANTIC_TOP_K #17 | key=SEMANTIC_TOP_K | updated | test_admin_api_phase2_part_5.py |
| TC-ADM-7972 | P2 | Settings endpoint SEMANTIC_TOP_K #18 | key=SEMANTIC_TOP_K | updated | test_admin_api_phase2_part_5.py |
| TC-ADM-7973 | P2 | Settings endpoint SEMANTIC_TOP_K #19 | key=SEMANTIC_TOP_K | updated | test_admin_api_phase2_part_5.py |
| TC-ADM-7974 | P2 | Logs scenario 0 | scenario=0 | list ok | test_admin_api_phase2_part_5.py |
| TC-ADM-7975 | P2 | Logs scenario 1 | scenario=1 | list ok | test_admin_api_phase2_part_5.py |
| TC-ADM-7976 | P2 | Logs scenario 2 | scenario=2 | list ok | test_admin_api_phase2_part_5.py |
| TC-ADM-7977 | P2 | Logs scenario 3 | scenario=3 | list ok | test_admin_api_phase2_part_5.py |
| TC-ADM-7978 | P2 | Logs scenario 4 | scenario=4 | list ok | test_admin_api_phase2_part_5.py |
| TC-ADM-7979 | P2 | Logs scenario 5 | scenario=5 | list ok | test_admin_api_phase2_part_5.py |
| TC-ADM-7980 | P2 | Logs scenario 6 | scenario=6 | list ok | test_admin_api_phase2_part_5.py |
| TC-ADM-7981 | P2 | Logs scenario 7 | scenario=7 | list ok | test_admin_api_phase2_part_5.py |
| TC-ADM-7982 | P2 | Logs scenario 8 | scenario=8 | list ok | test_admin_api_phase2_part_5.py |
| TC-ADM-7983 | P2 | Logs scenario 9 | scenario=9 | list ok | test_admin_api_phase2_part_5.py |
| TC-ADM-7984 | P2 | Logs scenario 10 | scenario=10 | list ok | test_admin_api_phase2_part_5.py |
| TC-ADM-7985 | P2 | Logs scenario 11 | scenario=11 | list ok | test_admin_api_phase2_part_5.py |
| TC-ADM-7986 | P2 | Logs scenario 12 | scenario=12 | list ok | test_admin_api_phase2_part_5.py |
| TC-ADM-7987 | P2 | Logs scenario 13 | scenario=13 | list ok | test_admin_api_phase2_part_5.py |
| TC-ADM-7988 | P2 | Logs scenario 14 | scenario=14 | list ok | test_admin_api_phase2_part_5.py |
| TC-ADM-7989 | P2 | Logs scenario 15 | scenario=15 | list ok | test_admin_api_phase2_part_5.py |
| TC-ADM-7990 | P2 | Logs scenario 16 | scenario=16 | list ok | test_admin_api_phase2_part_5.py |
| TC-ADM-7991 | P2 | Logs scenario 17 | scenario=17 | list ok | test_admin_api_phase2_part_5.py |
| TC-ADM-7992 | P2 | Logs scenario 18 | scenario=18 | list ok | test_admin_api_phase2_part_5.py |
| TC-ADM-7993 | P2 | Logs scenario 19 | scenario=19 | list ok | test_admin_api_phase2_part_5.py |
| TC-ADM-7994 | P2 | Logs scenario 20 | scenario=20 | list ok | test_admin_api_phase2_part_5.py |
| TC-ADM-7995 | P2 | Logs scenario 21 | scenario=21 | list ok | test_admin_api_phase2_part_5.py |
| TC-ADM-7996 | P2 | Logs scenario 22 | scenario=22 | list ok | test_admin_api_phase2_part_5.py |
| TC-ADM-7997 | P2 | Logs scenario 23 | scenario=23 | list ok | test_admin_api_phase2_part_5.py |
| TC-ADM-7998 | P2 | Logs scenario 24 | scenario=24 | list ok | test_admin_api_phase2_part_5.py |
| TC-ADM-7999 | P2 | Logs scenario 25 | scenario=25 | list ok | test_admin_api_phase2_part_5.py |
| TC-ADM-8000 | P2 | Logs scenario 26 | scenario=26 | list ok | test_admin_api_phase2_part_5.py |
| TC-ADM-8001 | P2 | Logs scenario 27 | scenario=27 | list ok | test_admin_api_phase2_part_5.py |
| TC-ADM-8002 | P2 | Logs scenario 28 | scenario=28 | list ok | test_admin_api_phase2_part_5.py |
| TC-ADM-8003 | P2 | Logs scenario 29 | scenario=29 | list ok | test_admin_api_phase2_part_5.py |
| TC-ADM-8004 | P2 | Logs scenario 30 | scenario=30 | list ok | test_admin_api_phase2_part_5.py |
| TC-ADM-8005 | P2 | Logs scenario 31 | scenario=31 | list ok | test_admin_api_phase2_part_5.py |
| TC-ADM-8006 | P2 | Logs scenario 32 | scenario=32 | list ok | test_admin_api_phase2_part_5.py |
| TC-ADM-8007 | P2 | Logs scenario 33 | scenario=33 | list ok | test_admin_api_phase2_part_5.py |
| TC-ADM-8008 | P2 | Logs scenario 34 | scenario=34 | list ok | test_admin_api_phase2_part_5.py |
| TC-ADM-8009 | P2 | Logs scenario 35 | scenario=35 | list ok | test_admin_api_phase2_part_5.py |
| TC-ADM-8010 | P2 | Logs scenario 36 | scenario=36 | list ok | test_admin_api_phase2_part_5.py |
| TC-ADM-8011 | P2 | Logs scenario 37 | scenario=37 | list ok | test_admin_api_phase2_part_5.py |
| TC-ADM-8012 | P2 | Logs scenario 38 | scenario=38 | list ok | test_admin_api_phase2_part_5.py |
| TC-ADM-8013 | P2 | Logs scenario 39 | scenario=39 | list ok | test_admin_api_phase2_part_5.py |
| TC-ADM-8014 | P2 | Logs scenario 40 | scenario=40 | list ok | test_admin_api_phase2_part_5.py |
| TC-ADM-8015 | P2 | Logs scenario 41 | scenario=41 | list ok | test_admin_api_phase2_part_5.py |
| TC-ADM-8016 | P2 | Logs scenario 42 | scenario=42 | list ok | test_admin_api_phase2_part_5.py |
| TC-ADM-8017 | P2 | Logs scenario 43 | scenario=43 | list ok | test_admin_api_phase2_part_5.py |
| TC-ADM-8018 | P2 | Logs scenario 44 | scenario=44 | list ok | test_admin_api_phase2_part_5.py |
| TC-ADM-8019 | P2 | Logs scenario 45 | scenario=45 | list ok | test_admin_api_phase2_part_5.py |
| TC-ADM-8020 | P2 | Logs scenario 46 | scenario=46 | list ok | test_admin_api_phase2_part_5.py |
| TC-ADM-8021 | P2 | Logs scenario 47 | scenario=47 | list ok | test_admin_api_phase2_part_5.py |
| TC-ADM-8022 | P2 | Logs scenario 48 | scenario=48 | list ok | test_admin_api_phase2_part_5.py |
| TC-ADM-8023 | P2 | Logs scenario 49 | scenario=49 | list ok | test_admin_api_phase2_part_5.py |
| TC-ADM-8024 | P2 | Stats scenario 0 | scenario=0 | stats valid | test_admin_api_phase2_part_6.py |
| TC-ADM-8025 | P2 | Stats scenario 1 | scenario=1 | stats valid | test_admin_api_phase2_part_6.py |
| TC-ADM-8026 | P2 | Stats scenario 2 | scenario=2 | stats valid | test_admin_api_phase2_part_6.py |
| TC-ADM-8027 | P2 | Stats scenario 3 | scenario=3 | stats valid | test_admin_api_phase2_part_6.py |
| TC-ADM-8028 | P2 | Stats scenario 4 | scenario=4 | stats valid | test_admin_api_phase2_part_6.py |
| TC-ADM-8029 | P2 | Stats scenario 5 | scenario=5 | stats valid | test_admin_api_phase2_part_6.py |
| TC-ADM-8030 | P2 | Stats scenario 6 | scenario=6 | stats valid | test_admin_api_phase2_part_6.py |
| TC-ADM-8031 | P2 | Stats scenario 7 | scenario=7 | stats valid | test_admin_api_phase2_part_6.py |
| TC-ADM-8032 | P2 | Stats scenario 8 | scenario=8 | stats valid | test_admin_api_phase2_part_6.py |
| TC-ADM-8033 | P2 | Stats scenario 9 | scenario=9 | stats valid | test_admin_api_phase2_part_6.py |
| TC-ADM-8034 | P2 | Stats scenario 10 | scenario=10 | stats valid | test_admin_api_phase2_part_6.py |
| TC-ADM-8035 | P2 | Stats scenario 11 | scenario=11 | stats valid | test_admin_api_phase2_part_6.py |
| TC-ADM-8036 | P2 | Stats scenario 12 | scenario=12 | stats valid | test_admin_api_phase2_part_6.py |
| TC-ADM-8037 | P2 | Stats scenario 13 | scenario=13 | stats valid | test_admin_api_phase2_part_6.py |
| TC-ADM-8038 | P2 | Stats scenario 14 | scenario=14 | stats valid | test_admin_api_phase2_part_6.py |
| TC-ADM-8039 | P2 | Stats scenario 15 | scenario=15 | stats valid | test_admin_api_phase2_part_6.py |
| TC-ADM-8040 | P2 | Stats scenario 16 | scenario=16 | stats valid | test_admin_api_phase2_part_6.py |
| TC-ADM-8041 | P2 | Stats scenario 17 | scenario=17 | stats valid | test_admin_api_phase2_part_6.py |
| TC-ADM-8042 | P2 | Stats scenario 18 | scenario=18 | stats valid | test_admin_api_phase2_part_6.py |
| TC-ADM-8043 | P2 | Stats scenario 19 | scenario=19 | stats valid | test_admin_api_phase2_part_6.py |
| TC-ADM-8044 | P2 | Stats scenario 20 | scenario=20 | stats valid | test_admin_api_phase2_part_6.py |
| TC-ADM-8045 | P2 | Stats scenario 21 | scenario=21 | stats valid | test_admin_api_phase2_part_6.py |
| TC-ADM-8046 | P2 | Stats scenario 22 | scenario=22 | stats valid | test_admin_api_phase2_part_6.py |
| TC-ADM-8047 | P2 | Stats scenario 23 | scenario=23 | stats valid | test_admin_api_phase2_part_6.py |
| TC-ADM-8048 | P2 | Stats scenario 24 | scenario=24 | stats valid | test_admin_api_phase2_part_6.py |
| TC-ADM-8049 | P2 | Stats scenario 25 | scenario=25 | stats valid | test_admin_api_phase2_part_6.py |
| TC-ADM-8050 | P2 | Stats scenario 26 | scenario=26 | stats valid | test_admin_api_phase2_part_6.py |
| TC-ADM-8051 | P2 | Stats scenario 27 | scenario=27 | stats valid | test_admin_api_phase2_part_6.py |
| TC-ADM-8052 | P2 | Stats scenario 28 | scenario=28 | stats valid | test_admin_api_phase2_part_6.py |
| TC-ADM-8053 | P2 | Stats scenario 29 | scenario=29 | stats valid | test_admin_api_phase2_part_6.py |
| TC-ADM-8054 | P2 | Stats scenario 30 | scenario=30 | stats valid | test_admin_api_phase2_part_6.py |
| TC-ADM-8055 | P2 | Stats scenario 31 | scenario=31 | stats valid | test_admin_api_phase2_part_6.py |
| TC-ADM-8056 | P2 | Stats scenario 32 | scenario=32 | stats valid | test_admin_api_phase2_part_6.py |
| TC-ADM-8057 | P2 | Stats scenario 33 | scenario=33 | stats valid | test_admin_api_phase2_part_6.py |
| TC-ADM-8058 | P2 | Stats scenario 34 | scenario=34 | stats valid | test_admin_api_phase2_part_6.py |
| TC-ADM-8059 | P2 | Stats scenario 35 | scenario=35 | stats valid | test_admin_api_phase2_part_6.py |
| TC-ADM-8060 | P2 | Stats scenario 36 | scenario=36 | stats valid | test_admin_api_phase2_part_6.py |
| TC-ADM-8061 | P2 | Stats scenario 37 | scenario=37 | stats valid | test_admin_api_phase2_part_6.py |
| TC-ADM-8062 | P2 | Stats scenario 38 | scenario=38 | stats valid | test_admin_api_phase2_part_6.py |
| TC-ADM-8063 | P2 | Stats scenario 39 | scenario=39 | stats valid | test_admin_api_phase2_part_6.py |
| TC-ADM-8064 | P2 | Stats scenario 40 | scenario=40 | stats valid | test_admin_api_phase2_part_6.py |
| TC-ADM-8065 | P2 | Stats scenario 41 | scenario=41 | stats valid | test_admin_api_phase2_part_6.py |
| TC-ADM-8066 | P2 | Stats scenario 42 | scenario=42 | stats valid | test_admin_api_phase2_part_6.py |
| TC-ADM-8067 | P2 | Stats scenario 43 | scenario=43 | stats valid | test_admin_api_phase2_part_6.py |
| TC-ADM-8068 | P2 | Stats scenario 44 | scenario=44 | stats valid | test_admin_api_phase2_part_6.py |
| TC-ADM-8069 | P2 | Stats scenario 45 | scenario=45 | stats valid | test_admin_api_phase2_part_6.py |
| TC-ADM-8070 | P2 | Stats scenario 46 | scenario=46 | stats valid | test_admin_api_phase2_part_6.py |
| TC-ADM-8071 | P2 | Stats scenario 47 | scenario=47 | stats valid | test_admin_api_phase2_part_6.py |
| TC-ADM-8072 | P2 | Stats scenario 48 | scenario=48 | stats valid | test_admin_api_phase2_part_6.py |
| TC-ADM-8073 | P2 | Stats scenario 49 | scenario=49 | stats valid | test_admin_api_phase2_part_6.py |
| TC-ADM-8074 | P2 | Stats scenario 50 | scenario=50 | stats valid | test_admin_api_phase2_part_6.py |
| TC-ADM-8075 | P2 | Stats scenario 51 | scenario=51 | stats valid | test_admin_api_phase2_part_6.py |
| TC-ADM-8076 | P2 | Stats scenario 52 | scenario=52 | stats valid | test_admin_api_phase2_part_6.py |
| TC-ADM-8077 | P2 | Stats scenario 53 | scenario=53 | stats valid | test_admin_api_phase2_part_6.py |
| TC-ADM-8078 | P2 | Stats scenario 54 | scenario=54 | stats valid | test_admin_api_phase2_part_6.py |
| TC-ADM-8079 | P2 | Stats scenario 55 | scenario=55 | stats valid | test_admin_api_phase2_part_6.py |
| TC-ADM-8080 | P2 | Stats scenario 56 | scenario=56 | stats valid | test_admin_api_phase2_part_6.py |
| TC-ADM-8081 | P2 | Stats scenario 57 | scenario=57 | stats valid | test_admin_api_phase2_part_6.py |
| TC-ADM-8082 | P2 | Stats scenario 58 | scenario=58 | stats valid | test_admin_api_phase2_part_6.py |
| TC-ADM-8083 | P2 | Stats scenario 59 | scenario=59 | stats valid | test_admin_api_phase2_part_6.py |
| TC-ADM-8084 | P2 | Stats scenario 60 | scenario=60 | stats valid | test_admin_api_phase2_part_6.py |
| TC-ADM-8085 | P2 | Stats scenario 61 | scenario=61 | stats valid | test_admin_api_phase2_part_6.py |
| TC-ADM-8086 | P2 | Stats scenario 62 | scenario=62 | stats valid | test_admin_api_phase2_part_6.py |
| TC-ADM-8087 | P2 | Stats scenario 63 | scenario=63 | stats valid | test_admin_api_phase2_part_6.py |
| TC-ADM-8088 | P2 | Stats scenario 64 | scenario=64 | stats valid | test_admin_api_phase2_part_6.py |
| TC-ADM-8089 | P2 | Stats scenario 65 | scenario=65 | stats valid | test_admin_api_phase2_part_6.py |
| TC-ADM-8090 | P2 | Stats scenario 66 | scenario=66 | stats valid | test_admin_api_phase2_part_6.py |
| TC-ADM-8091 | P2 | Stats scenario 67 | scenario=67 | stats valid | test_admin_api_phase2_part_6.py |
| TC-ADM-8092 | P2 | Stats scenario 68 | scenario=68 | stats valid | test_admin_api_phase2_part_6.py |
| TC-ADM-8093 | P2 | Stats scenario 69 | scenario=69 | stats valid | test_admin_api_phase2_part_6.py |
| TC-ADM-8094 | P2 | Stats scenario 70 | scenario=70 | stats valid | test_admin_api_phase2_part_6.py |
| TC-ADM-8095 | P2 | Stats scenario 71 | scenario=71 | stats valid | test_admin_api_phase2_part_6.py |
| TC-ADM-8096 | P2 | Stats scenario 72 | scenario=72 | stats valid | test_admin_api_phase2_part_6.py |
| TC-ADM-8097 | P2 | Stats scenario 73 | scenario=73 | stats valid | test_admin_api_phase2_part_6.py |
| TC-ADM-8098 | P2 | Stats scenario 74 | scenario=74 | stats valid | test_admin_api_phase2_part_6.py |
| TC-ADM-8099 | P2 | Stats scenario 75 | scenario=75 | stats valid | test_admin_api_phase2_part_6.py |
| TC-ADM-8100 | P2 | Stats scenario 76 | scenario=76 | stats valid | test_admin_api_phase2_part_6.py |
| TC-ADM-8101 | P2 | Stats scenario 77 | scenario=77 | stats valid | test_admin_api_phase2_part_6.py |
| TC-ADM-8102 | P2 | Stats scenario 78 | scenario=78 | stats valid | test_admin_api_phase2_part_6.py |
| TC-ADM-8103 | P2 | Stats scenario 79 | scenario=79 | stats valid | test_admin_api_phase2_part_6.py |
| TC-ADM-8104 | P2 | Stats scenario 80 | scenario=80 | stats valid | test_admin_api_phase2_part_6.py |
| TC-ADM-8105 | P2 | Stats scenario 81 | scenario=81 | stats valid | test_admin_api_phase2_part_6.py |
| TC-ADM-8106 | P2 | Stats scenario 82 | scenario=82 | stats valid | test_admin_api_phase2_part_6.py |
| TC-ADM-8107 | P2 | Stats scenario 83 | scenario=83 | stats valid | test_admin_api_phase2_part_6.py |
| TC-ADM-8108 | P2 | Stats scenario 84 | scenario=84 | stats valid | test_admin_api_phase2_part_6.py |
| TC-ADM-8109 | P2 | Stats scenario 85 | scenario=85 | stats valid | test_admin_api_phase2_part_6.py |
| TC-ADM-8110 | P2 | Stats scenario 86 | scenario=86 | stats valid | test_admin_api_phase2_part_6.py |
| TC-ADM-8111 | P2 | Stats scenario 87 | scenario=87 | stats valid | test_admin_api_phase2_part_6.py |
| TC-ADM-8112 | P2 | Stats scenario 88 | scenario=88 | stats valid | test_admin_api_phase2_part_6.py |
| TC-ADM-8113 | P2 | Stats scenario 89 | scenario=89 | stats valid | test_admin_api_phase2_part_6.py |
| TC-ADM-8114 | P2 | Stats scenario 90 | scenario=90 | stats valid | test_admin_api_phase2_part_6.py |
| TC-ADM-8115 | P2 | Stats scenario 91 | scenario=91 | stats valid | test_admin_api_phase2_part_6.py |
| TC-ADM-8116 | P2 | Stats scenario 92 | scenario=92 | stats valid | test_admin_api_phase2_part_6.py |
| TC-ADM-8117 | P2 | Stats scenario 93 | scenario=93 | stats valid | test_admin_api_phase2_part_6.py |
| TC-ADM-8118 | P2 | Stats scenario 94 | scenario=94 | stats valid | test_admin_api_phase2_part_6.py |
| TC-ADM-8119 | P2 | Stats scenario 95 | scenario=95 | stats valid | test_admin_api_phase2_part_6.py |
| TC-ADM-8120 | P2 | Stats scenario 96 | scenario=96 | stats valid | test_admin_api_phase2_part_6.py |
| TC-ADM-8121 | P2 | Stats scenario 97 | scenario=97 | stats valid | test_admin_api_phase2_part_6.py |
| TC-ADM-8122 | P2 | Stats scenario 98 | scenario=98 | stats valid | test_admin_api_phase2_part_6.py |
| TC-ADM-8123 | P2 | Stats scenario 99 | scenario=99 | stats valid | test_admin_api_phase2_part_6.py |

### Phase 3 - 10,000 cases
- Planned sweeps over the full dimension matrix, IDs TC-ADM-0651 onward.

### Phase 4 - 100,000 cases
- Planned high-scale scenarios, IDs TC-ADM-10651 onward.

### Phase 5 - 939,350 cases
- Planned exhaustive dimension sweep, IDs TC-ADM-110651 onward.

## Implementation Status
| File | Test Cases | Priority | Status |
| :--- | :--- | :--- | :--- |
| test_admin_api_phase2_part_1.py | 7429-7528 | P1 | :white_check_mark: Phase 2 |
| test_admin_api_phase2_part_2.py | 7529-7718 | P1 | :white_check_mark: Phase 2 |
| test_admin_api_phase2_part_3.py | 7719-7823 | P1 | :white_check_mark: Phase 2 |
| test_admin_api_phase2_part_4.py | 7824-7923 | P1 | :white_check_mark: Phase 2 |
| test_admin_api_phase2_part_5.py | 7924-8023 | P2 | :white_check_mark: Phase 2 |
| test_admin_api_phase2_part_6.py | 8024-8123 | P2 | :white_check_mark: Phase 2 |

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
- Admin Console
- API Reference
