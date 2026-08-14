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
| TC-ADM-7628 | P1 | Word CRUD other sev=0 lang=en | category=other,severity=0,language=en | roundtrip ok | test_admin_api_phase2_part_1.py |
| TC-ADM-7629 | P1 | Word CRUD other sev=0 lang=zh-CN | category=other,severity=0,language=zh-CN | roundtrip ok | test_admin_api_phase2_part_1.py |
| TC-ADM-7630 | P1 | Word CRUD other sev=0 lang=ru | category=other,severity=0,language=ru | roundtrip ok | test_admin_api_phase2_part_1.py |
| TC-ADM-7631 | P1 | Word CRUD other sev=0 lang=ar | category=other,severity=0,language=ar | roundtrip ok | test_admin_api_phase2_part_1.py |
| TC-ADM-7632 | P1 | Word CRUD other sev=0 lang=ja | category=other,severity=0,language=ja | roundtrip ok | test_admin_api_phase2_part_1.py |
| TC-ADM-7633 | P1 | Word CRUD other sev=1 lang=en | category=other,severity=1,language=en | roundtrip ok | test_admin_api_phase2_part_1.py |
| TC-ADM-7634 | P1 | Word CRUD other sev=1 lang=zh-CN | category=other,severity=1,language=zh-CN | roundtrip ok | test_admin_api_phase2_part_1.py |
| TC-ADM-7635 | P1 | Word CRUD other sev=1 lang=ru | category=other,severity=1,language=ru | roundtrip ok | test_admin_api_phase2_part_1.py |
| TC-ADM-7636 | P1 | Word CRUD other sev=1 lang=ar | category=other,severity=1,language=ar | roundtrip ok | test_admin_api_phase2_part_1.py |
| TC-ADM-7637 | P1 | Word CRUD other sev=1 lang=ja | category=other,severity=1,language=ja | roundtrip ok | test_admin_api_phase2_part_1.py |
| TC-ADM-7638 | P1 | Word CRUD other sev=3 lang=en | category=other,severity=3,language=en | roundtrip ok | test_admin_api_phase2_part_1.py |
| TC-ADM-7639 | P1 | Word CRUD other sev=3 lang=zh-CN | category=other,severity=3,language=zh-CN | roundtrip ok | test_admin_api_phase2_part_1.py |
| TC-ADM-7640 | P1 | Word CRUD other sev=3 lang=ru | category=other,severity=3,language=ru | roundtrip ok | test_admin_api_phase2_part_1.py |
| TC-ADM-7641 | P1 | Word CRUD other sev=3 lang=ar | category=other,severity=3,language=ar | roundtrip ok | test_admin_api_phase2_part_1.py |
| TC-ADM-7642 | P1 | Word CRUD other sev=3 lang=ja | category=other,severity=3,language=ja | roundtrip ok | test_admin_api_phase2_part_1.py |
| TC-ADM-7643 | P1 | Word CRUD other sev=5 lang=en | category=other,severity=5,language=en | roundtrip ok | test_admin_api_phase2_part_1.py |
| TC-ADM-7644 | P1 | Word CRUD other sev=5 lang=zh-CN | category=other,severity=5,language=zh-CN | roundtrip ok | test_admin_api_phase2_part_1.py |
| TC-ADM-7645 | P1 | Word CRUD other sev=5 lang=ru | category=other,severity=5,language=ru | roundtrip ok | test_admin_api_phase2_part_1.py |
| TC-ADM-7646 | P1 | Word CRUD other sev=5 lang=ar | category=other,severity=5,language=ar | roundtrip ok | test_admin_api_phase2_part_1.py |
| TC-ADM-7647 | P1 | Word CRUD other sev=5 lang=ja | category=other,severity=5,language=ja | roundtrip ok | test_admin_api_phase2_part_1.py |
| TC-ADM-7648 | P1 | Word CRUD other sev=7 lang=en | category=other,severity=7,language=en | roundtrip ok | test_admin_api_phase2_part_1.py |
| TC-ADM-7649 | P1 | Word CRUD other sev=7 lang=zh-CN | category=other,severity=7,language=zh-CN | roundtrip ok | test_admin_api_phase2_part_1.py |
| TC-ADM-7650 | P1 | Word CRUD other sev=7 lang=ru | category=other,severity=7,language=ru | roundtrip ok | test_admin_api_phase2_part_1.py |
| TC-ADM-7651 | P1 | Word CRUD other sev=7 lang=ar | category=other,severity=7,language=ar | roundtrip ok | test_admin_api_phase2_part_1.py |
| TC-ADM-7652 | P1 | Word CRUD other sev=7 lang=ja | category=other,severity=7,language=ja | roundtrip ok | test_admin_api_phase2_part_1.py |
| TC-ADM-7653 | P1 | Word CRUD other sev=10 lang=en | category=other,severity=10,language=en | roundtrip ok | test_admin_api_phase2_part_1.py |
| TC-ADM-7654 | P1 | Word CRUD other sev=10 lang=zh-CN | category=other,severity=10,language=zh-CN | roundtrip ok | test_admin_api_phase2_part_1.py |
| TC-ADM-7655 | P1 | Word CRUD other sev=10 lang=ru | category=other,severity=10,language=ru | roundtrip ok | test_admin_api_phase2_part_1.py |
| TC-ADM-7656 | P1 | Word CRUD other sev=10 lang=ar | category=other,severity=10,language=ar | roundtrip ok | test_admin_api_phase2_part_1.py |
| TC-ADM-7657 | P1 | Word CRUD other sev=10 lang=ja | category=other,severity=10,language=ja | roundtrip ok | test_admin_api_phase2_part_1.py |
| TC-ADM-7658 | P1 | Word CRUD hate_speech sev=0 lang=en | category=hate_speech,severity=0,language=en | roundtrip ok | test_admin_api_phase2_part_1.py |
| TC-ADM-7659 | P1 | Word CRUD hate_speech sev=0 lang=zh-CN | category=hate_speech,severity=0,language=zh-CN | roundtrip ok | test_admin_api_phase2_part_1.py |
| TC-ADM-7660 | P1 | Word CRUD hate_speech sev=0 lang=ru | category=hate_speech,severity=0,language=ru | roundtrip ok | test_admin_api_phase2_part_1.py |
| TC-ADM-7661 | P1 | Word CRUD hate_speech sev=0 lang=ar | category=hate_speech,severity=0,language=ar | roundtrip ok | test_admin_api_phase2_part_1.py |
| TC-ADM-7662 | P1 | Word CRUD hate_speech sev=0 lang=ja | category=hate_speech,severity=0,language=ja | roundtrip ok | test_admin_api_phase2_part_1.py |
| TC-ADM-7663 | P1 | Word CRUD hate_speech sev=1 lang=en | category=hate_speech,severity=1,language=en | roundtrip ok | test_admin_api_phase2_part_1.py |
| TC-ADM-7664 | P1 | Word CRUD hate_speech sev=1 lang=zh-CN | category=hate_speech,severity=1,language=zh-CN | roundtrip ok | test_admin_api_phase2_part_1.py |
| TC-ADM-7665 | P1 | Word CRUD hate_speech sev=1 lang=ru | category=hate_speech,severity=1,language=ru | roundtrip ok | test_admin_api_phase2_part_1.py |
| TC-ADM-7666 | P1 | Word CRUD hate_speech sev=1 lang=ar | category=hate_speech,severity=1,language=ar | roundtrip ok | test_admin_api_phase2_part_1.py |
| TC-ADM-7667 | P1 | Word CRUD hate_speech sev=1 lang=ja | category=hate_speech,severity=1,language=ja | roundtrip ok | test_admin_api_phase2_part_1.py |
| TC-ADM-7668 | P1 | Word CRUD hate_speech sev=3 lang=en | category=hate_speech,severity=3,language=en | roundtrip ok | test_admin_api_phase2_part_1.py |
| TC-ADM-7669 | P1 | Word CRUD hate_speech sev=3 lang=zh-CN | category=hate_speech,severity=3,language=zh-CN | roundtrip ok | test_admin_api_phase2_part_1.py |
| TC-ADM-7670 | P1 | Word CRUD hate_speech sev=3 lang=ru | category=hate_speech,severity=3,language=ru | roundtrip ok | test_admin_api_phase2_part_1.py |
| TC-ADM-7671 | P1 | Word CRUD hate_speech sev=3 lang=ar | category=hate_speech,severity=3,language=ar | roundtrip ok | test_admin_api_phase2_part_1.py |
| TC-ADM-7672 | P1 | Word CRUD hate_speech sev=3 lang=ja | category=hate_speech,severity=3,language=ja | roundtrip ok | test_admin_api_phase2_part_1.py |
| TC-ADM-7673 | P1 | Word CRUD hate_speech sev=5 lang=en | category=hate_speech,severity=5,language=en | roundtrip ok | test_admin_api_phase2_part_1.py |
| TC-ADM-7674 | P1 | Word CRUD hate_speech sev=5 lang=zh-CN | category=hate_speech,severity=5,language=zh-CN | roundtrip ok | test_admin_api_phase2_part_1.py |
| TC-ADM-7675 | P1 | Word CRUD hate_speech sev=5 lang=ru | category=hate_speech,severity=5,language=ru | roundtrip ok | test_admin_api_phase2_part_1.py |
| TC-ADM-7676 | P1 | Word CRUD hate_speech sev=5 lang=ar | category=hate_speech,severity=5,language=ar | roundtrip ok | test_admin_api_phase2_part_1.py |
| TC-ADM-7677 | P1 | Word CRUD hate_speech sev=5 lang=ja | category=hate_speech,severity=5,language=ja | roundtrip ok | test_admin_api_phase2_part_1.py |
| TC-ADM-7678 | P1 | Word CRUD hate_speech sev=7 lang=en | category=hate_speech,severity=7,language=en | roundtrip ok | test_admin_api_phase2_part_1.py |
| TC-ADM-7679 | P1 | Word CRUD hate_speech sev=7 lang=zh-CN | category=hate_speech,severity=7,language=zh-CN | roundtrip ok | test_admin_api_phase2_part_1.py |
| TC-ADM-7680 | P1 | Word CRUD hate_speech sev=7 lang=ru | category=hate_speech,severity=7,language=ru | roundtrip ok | test_admin_api_phase2_part_1.py |
| TC-ADM-7681 | P1 | Word CRUD hate_speech sev=7 lang=ar | category=hate_speech,severity=7,language=ar | roundtrip ok | test_admin_api_phase2_part_1.py |
| TC-ADM-7682 | P1 | Word CRUD hate_speech sev=7 lang=ja | category=hate_speech,severity=7,language=ja | roundtrip ok | test_admin_api_phase2_part_1.py |
| TC-ADM-7683 | P1 | Word CRUD hate_speech sev=10 lang=en | category=hate_speech,severity=10,language=en | roundtrip ok | test_admin_api_phase2_part_1.py |
| TC-ADM-7684 | P1 | Word CRUD hate_speech sev=10 lang=zh-CN | category=hate_speech,severity=10,language=zh-CN | roundtrip ok | test_admin_api_phase2_part_1.py |
| TC-ADM-7685 | P1 | Word CRUD hate_speech sev=10 lang=ru | category=hate_speech,severity=10,language=ru | roundtrip ok | test_admin_api_phase2_part_1.py |
| TC-ADM-7686 | P1 | Word CRUD hate_speech sev=10 lang=ar | category=hate_speech,severity=10,language=ar | roundtrip ok | test_admin_api_phase2_part_1.py |
| TC-ADM-7687 | P1 | Word CRUD hate_speech sev=10 lang=ja | category=hate_speech,severity=10,language=ja | roundtrip ok | test_admin_api_phase2_part_1.py |
| TC-ADM-7688 | P1 | Word CRUD violence sev=0 lang=en | category=violence,severity=0,language=en | roundtrip ok | test_admin_api_phase2_part_1.py |
| TC-ADM-7689 | P1 | Word CRUD violence sev=0 lang=zh-CN | category=violence,severity=0,language=zh-CN | roundtrip ok | test_admin_api_phase2_part_1.py |
| TC-ADM-7690 | P1 | Word CRUD violence sev=0 lang=ru | category=violence,severity=0,language=ru | roundtrip ok | test_admin_api_phase2_part_1.py |
| TC-ADM-7691 | P1 | Word CRUD violence sev=0 lang=ar | category=violence,severity=0,language=ar | roundtrip ok | test_admin_api_phase2_part_1.py |
| TC-ADM-7692 | P1 | Word CRUD violence sev=0 lang=ja | category=violence,severity=0,language=ja | roundtrip ok | test_admin_api_phase2_part_1.py |
| TC-ADM-7693 | P1 | Word CRUD violence sev=1 lang=en | category=violence,severity=1,language=en | roundtrip ok | test_admin_api_phase2_part_1.py |
| TC-ADM-7694 | P1 | Word CRUD violence sev=1 lang=zh-CN | category=violence,severity=1,language=zh-CN | roundtrip ok | test_admin_api_phase2_part_1.py |
| TC-ADM-7695 | P1 | Word CRUD violence sev=1 lang=ru | category=violence,severity=1,language=ru | roundtrip ok | test_admin_api_phase2_part_1.py |
| TC-ADM-7696 | P1 | Word CRUD violence sev=1 lang=ar | category=violence,severity=1,language=ar | roundtrip ok | test_admin_api_phase2_part_1.py |
| TC-ADM-7697 | P1 | Word CRUD violence sev=1 lang=ja | category=violence,severity=1,language=ja | roundtrip ok | test_admin_api_phase2_part_1.py |
| TC-ADM-7698 | P1 | Word CRUD violence sev=3 lang=en | category=violence,severity=3,language=en | roundtrip ok | test_admin_api_phase2_part_1.py |
| TC-ADM-7699 | P1 | Word CRUD violence sev=3 lang=zh-CN | category=violence,severity=3,language=zh-CN | roundtrip ok | test_admin_api_phase2_part_1.py |
| TC-ADM-7700 | P1 | Word CRUD violence sev=3 lang=ru | category=violence,severity=3,language=ru | roundtrip ok | test_admin_api_phase2_part_1.py |
| TC-ADM-7701 | P1 | Word CRUD violence sev=3 lang=ar | category=violence,severity=3,language=ar | roundtrip ok | test_admin_api_phase2_part_1.py |
| TC-ADM-7702 | P1 | Word CRUD violence sev=3 lang=ja | category=violence,severity=3,language=ja | roundtrip ok | test_admin_api_phase2_part_1.py |
| TC-ADM-7703 | P1 | Word CRUD violence sev=5 lang=en | category=violence,severity=5,language=en | roundtrip ok | test_admin_api_phase2_part_1.py |
| TC-ADM-7704 | P1 | Word CRUD violence sev=5 lang=zh-CN | category=violence,severity=5,language=zh-CN | roundtrip ok | test_admin_api_phase2_part_1.py |
| TC-ADM-7705 | P1 | Word CRUD violence sev=5 lang=ru | category=violence,severity=5,language=ru | roundtrip ok | test_admin_api_phase2_part_1.py |
| TC-ADM-7706 | P1 | Word CRUD violence sev=5 lang=ar | category=violence,severity=5,language=ar | roundtrip ok | test_admin_api_phase2_part_1.py |
| TC-ADM-7707 | P1 | Word CRUD violence sev=5 lang=ja | category=violence,severity=5,language=ja | roundtrip ok | test_admin_api_phase2_part_1.py |
| TC-ADM-7708 | P1 | Word CRUD violence sev=7 lang=en | category=violence,severity=7,language=en | roundtrip ok | test_admin_api_phase2_part_1.py |
| TC-ADM-7709 | P1 | Word CRUD violence sev=7 lang=zh-CN | category=violence,severity=7,language=zh-CN | roundtrip ok | test_admin_api_phase2_part_1.py |
| TC-ADM-7710 | P1 | Word CRUD violence sev=7 lang=ru | category=violence,severity=7,language=ru | roundtrip ok | test_admin_api_phase2_part_1.py |
| TC-ADM-7711 | P1 | Word CRUD violence sev=7 lang=ar | category=violence,severity=7,language=ar | roundtrip ok | test_admin_api_phase2_part_1.py |
| TC-ADM-7712 | P1 | Word CRUD violence sev=7 lang=ja | category=violence,severity=7,language=ja | roundtrip ok | test_admin_api_phase2_part_1.py |
| TC-ADM-7713 | P1 | Word CRUD violence sev=10 lang=en | category=violence,severity=10,language=en | roundtrip ok | test_admin_api_phase2_part_1.py |
| TC-ADM-7714 | P1 | Word CRUD violence sev=10 lang=zh-CN | category=violence,severity=10,language=zh-CN | roundtrip ok | test_admin_api_phase2_part_1.py |
| TC-ADM-7715 | P1 | Word CRUD violence sev=10 lang=ru | category=violence,severity=10,language=ru | roundtrip ok | test_admin_api_phase2_part_1.py |
| TC-ADM-7716 | P1 | Word CRUD violence sev=10 lang=ar | category=violence,severity=10,language=ar | roundtrip ok | test_admin_api_phase2_part_1.py |
| TC-ADM-7717 | P1 | Word CRUD violence sev=10 lang=ja | category=violence,severity=10,language=ja | roundtrip ok | test_admin_api_phase2_part_1.py |
| TC-ADM-7718 | P1 | Word CRUD sexual sev=0 lang=en | category=sexual,severity=0,language=en | roundtrip ok | test_admin_api_phase2_part_1.py |
| TC-ADM-7719 | P1 | Word CRUD sexual sev=0 lang=zh-CN | category=sexual,severity=0,language=zh-CN | roundtrip ok | test_admin_api_phase2_part_1.py |
| TC-ADM-7720 | P1 | Word CRUD sexual sev=0 lang=ru | category=sexual,severity=0,language=ru | roundtrip ok | test_admin_api_phase2_part_1.py |
| TC-ADM-7721 | P1 | Word CRUD sexual sev=0 lang=ar | category=sexual,severity=0,language=ar | roundtrip ok | test_admin_api_phase2_part_1.py |
| TC-ADM-7722 | P1 | Word CRUD sexual sev=0 lang=ja | category=sexual,severity=0,language=ja | roundtrip ok | test_admin_api_phase2_part_1.py |
| TC-ADM-7723 | P1 | Word CRUD sexual sev=1 lang=en | category=sexual,severity=1,language=en | roundtrip ok | test_admin_api_phase2_part_1.py |
| TC-ADM-7724 | P1 | Word CRUD sexual sev=1 lang=zh-CN | category=sexual,severity=1,language=zh-CN | roundtrip ok | test_admin_api_phase2_part_1.py |
| TC-ADM-7725 | P1 | Word CRUD sexual sev=1 lang=ru | category=sexual,severity=1,language=ru | roundtrip ok | test_admin_api_phase2_part_1.py |
| TC-ADM-7726 | P1 | Word CRUD sexual sev=1 lang=ar | category=sexual,severity=1,language=ar | roundtrip ok | test_admin_api_phase2_part_1.py |
| TC-ADM-7727 | P1 | Word CRUD sexual sev=1 lang=ja | category=sexual,severity=1,language=ja | roundtrip ok | test_admin_api_phase2_part_1.py |
| TC-ADM-7728 | P1 | Word CRUD sexual sev=3 lang=en | category=sexual,severity=3,language=en | roundtrip ok | test_admin_api_phase2_part_2.py |
| TC-ADM-7729 | P1 | Word CRUD sexual sev=3 lang=zh-CN | category=sexual,severity=3,language=zh-CN | roundtrip ok | test_admin_api_phase2_part_2.py |
| TC-ADM-7730 | P1 | Word CRUD sexual sev=3 lang=ru | category=sexual,severity=3,language=ru | roundtrip ok | test_admin_api_phase2_part_2.py |
| TC-ADM-7731 | P1 | Word CRUD sexual sev=3 lang=ar | category=sexual,severity=3,language=ar | roundtrip ok | test_admin_api_phase2_part_2.py |
| TC-ADM-7732 | P1 | Word CRUD sexual sev=3 lang=ja | category=sexual,severity=3,language=ja | roundtrip ok | test_admin_api_phase2_part_2.py |
| TC-ADM-7733 | P1 | Word CRUD sexual sev=5 lang=en | category=sexual,severity=5,language=en | roundtrip ok | test_admin_api_phase2_part_2.py |
| TC-ADM-7734 | P1 | Word CRUD sexual sev=5 lang=zh-CN | category=sexual,severity=5,language=zh-CN | roundtrip ok | test_admin_api_phase2_part_2.py |
| TC-ADM-7735 | P1 | Word CRUD sexual sev=5 lang=ru | category=sexual,severity=5,language=ru | roundtrip ok | test_admin_api_phase2_part_2.py |
| TC-ADM-7736 | P1 | Word CRUD sexual sev=5 lang=ar | category=sexual,severity=5,language=ar | roundtrip ok | test_admin_api_phase2_part_2.py |
| TC-ADM-7737 | P1 | Word CRUD sexual sev=5 lang=ja | category=sexual,severity=5,language=ja | roundtrip ok | test_admin_api_phase2_part_2.py |
| TC-ADM-7738 | P1 | Word CRUD sexual sev=7 lang=en | category=sexual,severity=7,language=en | roundtrip ok | test_admin_api_phase2_part_2.py |
| TC-ADM-7739 | P1 | Word CRUD sexual sev=7 lang=zh-CN | category=sexual,severity=7,language=zh-CN | roundtrip ok | test_admin_api_phase2_part_2.py |
| TC-ADM-7740 | P1 | Word CRUD sexual sev=7 lang=ru | category=sexual,severity=7,language=ru | roundtrip ok | test_admin_api_phase2_part_2.py |
| TC-ADM-7741 | P1 | Word CRUD sexual sev=7 lang=ar | category=sexual,severity=7,language=ar | roundtrip ok | test_admin_api_phase2_part_2.py |
| TC-ADM-7742 | P1 | Word CRUD sexual sev=7 lang=ja | category=sexual,severity=7,language=ja | roundtrip ok | test_admin_api_phase2_part_2.py |
| TC-ADM-7743 | P1 | Word CRUD sexual sev=10 lang=en | category=sexual,severity=10,language=en | roundtrip ok | test_admin_api_phase2_part_2.py |
| TC-ADM-7744 | P1 | Word CRUD sexual sev=10 lang=zh-CN | category=sexual,severity=10,language=zh-CN | roundtrip ok | test_admin_api_phase2_part_2.py |
| TC-ADM-7745 | P1 | Word CRUD sexual sev=10 lang=ru | category=sexual,severity=10,language=ru | roundtrip ok | test_admin_api_phase2_part_2.py |
| TC-ADM-7746 | P1 | Word CRUD sexual sev=10 lang=ar | category=sexual,severity=10,language=ar | roundtrip ok | test_admin_api_phase2_part_2.py |
| TC-ADM-7747 | P1 | Word CRUD sexual sev=10 lang=ja | category=sexual,severity=10,language=ja | roundtrip ok | test_admin_api_phase2_part_2.py |
| TC-ADM-7748 | P1 | Word CRUD political sev=0 lang=en | category=political,severity=0,language=en | roundtrip ok | test_admin_api_phase2_part_2.py |
| TC-ADM-7749 | P1 | Word CRUD political sev=0 lang=zh-CN | category=political,severity=0,language=zh-CN | roundtrip ok | test_admin_api_phase2_part_2.py |
| TC-ADM-7750 | P1 | Word CRUD political sev=0 lang=ru | category=political,severity=0,language=ru | roundtrip ok | test_admin_api_phase2_part_2.py |
| TC-ADM-7751 | P1 | Word CRUD political sev=0 lang=ar | category=political,severity=0,language=ar | roundtrip ok | test_admin_api_phase2_part_2.py |
| TC-ADM-7752 | P1 | Word CRUD political sev=0 lang=ja | category=political,severity=0,language=ja | roundtrip ok | test_admin_api_phase2_part_2.py |
| TC-ADM-7753 | P1 | Word CRUD political sev=1 lang=en | category=political,severity=1,language=en | roundtrip ok | test_admin_api_phase2_part_2.py |
| TC-ADM-7754 | P1 | Word CRUD political sev=1 lang=zh-CN | category=political,severity=1,language=zh-CN | roundtrip ok | test_admin_api_phase2_part_2.py |
| TC-ADM-7755 | P1 | Word CRUD political sev=1 lang=ru | category=political,severity=1,language=ru | roundtrip ok | test_admin_api_phase2_part_2.py |
| TC-ADM-7756 | P1 | Word CRUD political sev=1 lang=ar | category=political,severity=1,language=ar | roundtrip ok | test_admin_api_phase2_part_2.py |
| TC-ADM-7757 | P1 | Word CRUD political sev=1 lang=ja | category=political,severity=1,language=ja | roundtrip ok | test_admin_api_phase2_part_2.py |
| TC-ADM-7758 | P1 | Word CRUD political sev=3 lang=en | category=political,severity=3,language=en | roundtrip ok | test_admin_api_phase2_part_2.py |
| TC-ADM-7759 | P1 | Word CRUD political sev=3 lang=zh-CN | category=political,severity=3,language=zh-CN | roundtrip ok | test_admin_api_phase2_part_2.py |
| TC-ADM-7760 | P1 | Word CRUD political sev=3 lang=ru | category=political,severity=3,language=ru | roundtrip ok | test_admin_api_phase2_part_2.py |
| TC-ADM-7761 | P1 | Word CRUD political sev=3 lang=ar | category=political,severity=3,language=ar | roundtrip ok | test_admin_api_phase2_part_2.py |
| TC-ADM-7762 | P1 | Word CRUD political sev=3 lang=ja | category=political,severity=3,language=ja | roundtrip ok | test_admin_api_phase2_part_2.py |
| TC-ADM-7763 | P1 | Word CRUD political sev=5 lang=en | category=political,severity=5,language=en | roundtrip ok | test_admin_api_phase2_part_2.py |
| TC-ADM-7764 | P1 | Word CRUD political sev=5 lang=zh-CN | category=political,severity=5,language=zh-CN | roundtrip ok | test_admin_api_phase2_part_2.py |
| TC-ADM-7765 | P1 | Word CRUD political sev=5 lang=ru | category=political,severity=5,language=ru | roundtrip ok | test_admin_api_phase2_part_2.py |
| TC-ADM-7766 | P1 | Word CRUD political sev=5 lang=ar | category=political,severity=5,language=ar | roundtrip ok | test_admin_api_phase2_part_2.py |
| TC-ADM-7767 | P1 | Word CRUD political sev=5 lang=ja | category=political,severity=5,language=ja | roundtrip ok | test_admin_api_phase2_part_2.py |
| TC-ADM-7768 | P1 | Word CRUD political sev=7 lang=en | category=political,severity=7,language=en | roundtrip ok | test_admin_api_phase2_part_2.py |
| TC-ADM-7769 | P1 | Word CRUD political sev=7 lang=zh-CN | category=political,severity=7,language=zh-CN | roundtrip ok | test_admin_api_phase2_part_2.py |
| TC-ADM-7770 | P1 | Word CRUD political sev=7 lang=ru | category=political,severity=7,language=ru | roundtrip ok | test_admin_api_phase2_part_2.py |
| TC-ADM-7771 | P1 | Word CRUD political sev=7 lang=ar | category=political,severity=7,language=ar | roundtrip ok | test_admin_api_phase2_part_2.py |
| TC-ADM-7772 | P1 | Word CRUD political sev=7 lang=ja | category=political,severity=7,language=ja | roundtrip ok | test_admin_api_phase2_part_2.py |
| TC-ADM-7773 | P1 | Word CRUD political sev=10 lang=en | category=political,severity=10,language=en | roundtrip ok | test_admin_api_phase2_part_2.py |
| TC-ADM-7774 | P1 | Word CRUD political sev=10 lang=zh-CN | category=political,severity=10,language=zh-CN | roundtrip ok | test_admin_api_phase2_part_2.py |
| TC-ADM-7775 | P1 | Word CRUD political sev=10 lang=ru | category=political,severity=10,language=ru | roundtrip ok | test_admin_api_phase2_part_2.py |
| TC-ADM-7776 | P1 | Word CRUD political sev=10 lang=ar | category=political,severity=10,language=ar | roundtrip ok | test_admin_api_phase2_part_2.py |
| TC-ADM-7777 | P1 | Word CRUD political sev=10 lang=ja | category=political,severity=10,language=ja | roundtrip ok | test_admin_api_phase2_part_2.py |
| TC-ADM-7868 | P1 | Import 1 scenario 0 | size=1,scenario=0 | imported | test_admin_api_phase2_part_2.py |
| TC-ADM-7869 | P1 | Import 1 scenario 1 | size=1,scenario=1 | imported | test_admin_api_phase2_part_2.py |
| TC-ADM-7870 | P1 | Import 1 scenario 2 | size=1,scenario=2 | imported | test_admin_api_phase2_part_2.py |
| TC-ADM-7871 | P1 | Import 1 scenario 3 | size=1,scenario=3 | imported | test_admin_api_phase2_part_2.py |
| TC-ADM-7872 | P1 | Import 1 scenario 4 | size=1,scenario=4 | imported | test_admin_api_phase2_part_2.py |
| TC-ADM-7873 | P1 | Import 1 scenario 5 | size=1,scenario=5 | imported | test_admin_api_phase2_part_2.py |
| TC-ADM-7874 | P1 | Import 1 scenario 6 | size=1,scenario=6 | imported | test_admin_api_phase2_part_2.py |
| TC-ADM-7875 | P1 | Import 1 scenario 7 | size=1,scenario=7 | imported | test_admin_api_phase2_part_2.py |
| TC-ADM-7876 | P1 | Import 1 scenario 8 | size=1,scenario=8 | imported | test_admin_api_phase2_part_2.py |
| TC-ADM-7877 | P1 | Import 1 scenario 9 | size=1,scenario=9 | imported | test_admin_api_phase2_part_2.py |
| TC-ADM-7878 | P1 | Import 1 scenario 10 | size=1,scenario=10 | imported | test_admin_api_phase2_part_2.py |
| TC-ADM-7879 | P1 | Import 1 scenario 11 | size=1,scenario=11 | imported | test_admin_api_phase2_part_2.py |
| TC-ADM-7880 | P1 | Import 1 scenario 12 | size=1,scenario=12 | imported | test_admin_api_phase2_part_2.py |
| TC-ADM-7881 | P1 | Import 1 scenario 13 | size=1,scenario=13 | imported | test_admin_api_phase2_part_2.py |
| TC-ADM-7882 | P1 | Import 1 scenario 14 | size=1,scenario=14 | imported | test_admin_api_phase2_part_2.py |
| TC-ADM-7883 | P1 | Import 2 scenario 0 | size=2,scenario=0 | imported | test_admin_api_phase2_part_2.py |
| TC-ADM-7884 | P1 | Import 2 scenario 1 | size=2,scenario=1 | imported | test_admin_api_phase2_part_2.py |
| TC-ADM-7885 | P1 | Import 2 scenario 2 | size=2,scenario=2 | imported | test_admin_api_phase2_part_2.py |
| TC-ADM-7886 | P1 | Import 2 scenario 3 | size=2,scenario=3 | imported | test_admin_api_phase2_part_2.py |
| TC-ADM-7887 | P1 | Import 2 scenario 4 | size=2,scenario=4 | imported | test_admin_api_phase2_part_2.py |
| TC-ADM-7888 | P1 | Import 2 scenario 5 | size=2,scenario=5 | imported | test_admin_api_phase2_part_2.py |
| TC-ADM-7889 | P1 | Import 2 scenario 6 | size=2,scenario=6 | imported | test_admin_api_phase2_part_2.py |
| TC-ADM-7890 | P1 | Import 2 scenario 7 | size=2,scenario=7 | imported | test_admin_api_phase2_part_2.py |
| TC-ADM-7891 | P1 | Import 2 scenario 8 | size=2,scenario=8 | imported | test_admin_api_phase2_part_2.py |
| TC-ADM-7892 | P1 | Import 2 scenario 9 | size=2,scenario=9 | imported | test_admin_api_phase2_part_2.py |
| TC-ADM-7893 | P1 | Import 2 scenario 10 | size=2,scenario=10 | imported | test_admin_api_phase2_part_2.py |
| TC-ADM-7894 | P1 | Import 2 scenario 11 | size=2,scenario=11 | imported | test_admin_api_phase2_part_2.py |
| TC-ADM-7895 | P1 | Import 2 scenario 12 | size=2,scenario=12 | imported | test_admin_api_phase2_part_2.py |
| TC-ADM-7896 | P1 | Import 2 scenario 13 | size=2,scenario=13 | imported | test_admin_api_phase2_part_2.py |
| TC-ADM-7897 | P1 | Import 2 scenario 14 | size=2,scenario=14 | imported | test_admin_api_phase2_part_2.py |
| TC-ADM-7898 | P1 | Import 5 scenario 0 | size=5,scenario=0 | imported | test_admin_api_phase2_part_2.py |
| TC-ADM-7899 | P1 | Import 5 scenario 1 | size=5,scenario=1 | imported | test_admin_api_phase2_part_2.py |
| TC-ADM-7900 | P1 | Import 5 scenario 2 | size=5,scenario=2 | imported | test_admin_api_phase2_part_2.py |
| TC-ADM-7901 | P1 | Import 5 scenario 3 | size=5,scenario=3 | imported | test_admin_api_phase2_part_2.py |
| TC-ADM-7902 | P1 | Import 5 scenario 4 | size=5,scenario=4 | imported | test_admin_api_phase2_part_2.py |
| TC-ADM-7903 | P1 | Import 5 scenario 5 | size=5,scenario=5 | imported | test_admin_api_phase2_part_2.py |
| TC-ADM-7904 | P1 | Import 5 scenario 6 | size=5,scenario=6 | imported | test_admin_api_phase2_part_2.py |
| TC-ADM-7905 | P1 | Import 5 scenario 7 | size=5,scenario=7 | imported | test_admin_api_phase2_part_2.py |
| TC-ADM-7906 | P1 | Import 5 scenario 8 | size=5,scenario=8 | imported | test_admin_api_phase2_part_2.py |
| TC-ADM-7907 | P1 | Import 5 scenario 9 | size=5,scenario=9 | imported | test_admin_api_phase2_part_2.py |
| TC-ADM-7908 | P1 | Import 5 scenario 10 | size=5,scenario=10 | imported | test_admin_api_phase2_part_2.py |
| TC-ADM-7909 | P1 | Import 5 scenario 11 | size=5,scenario=11 | imported | test_admin_api_phase2_part_2.py |
| TC-ADM-7910 | P1 | Import 5 scenario 12 | size=5,scenario=12 | imported | test_admin_api_phase2_part_2.py |
| TC-ADM-7911 | P1 | Import 5 scenario 13 | size=5,scenario=13 | imported | test_admin_api_phase2_part_2.py |
| TC-ADM-7912 | P1 | Import 5 scenario 14 | size=5,scenario=14 | imported | test_admin_api_phase2_part_2.py |
| TC-ADM-7913 | P1 | Import 10 scenario 0 | size=10,scenario=0 | imported | test_admin_api_phase2_part_2.py |
| TC-ADM-7914 | P1 | Import 10 scenario 1 | size=10,scenario=1 | imported | test_admin_api_phase2_part_2.py |
| TC-ADM-7915 | P1 | Import 10 scenario 2 | size=10,scenario=2 | imported | test_admin_api_phase2_part_2.py |
| TC-ADM-7916 | P1 | Import 10 scenario 3 | size=10,scenario=3 | imported | test_admin_api_phase2_part_2.py |
| TC-ADM-7917 | P1 | Import 10 scenario 4 | size=10,scenario=4 | imported | test_admin_api_phase2_part_2.py |
| TC-ADM-7918 | P1 | Import 10 scenario 5 | size=10,scenario=5 | imported | test_admin_api_phase2_part_3.py |
| TC-ADM-7919 | P1 | Import 10 scenario 6 | size=10,scenario=6 | imported | test_admin_api_phase2_part_3.py |
| TC-ADM-7920 | P1 | Import 10 scenario 7 | size=10,scenario=7 | imported | test_admin_api_phase2_part_3.py |
| TC-ADM-7921 | P1 | Import 10 scenario 8 | size=10,scenario=8 | imported | test_admin_api_phase2_part_3.py |
| TC-ADM-7922 | P1 | Import 10 scenario 9 | size=10,scenario=9 | imported | test_admin_api_phase2_part_3.py |
| TC-ADM-7923 | P1 | Import 10 scenario 10 | size=10,scenario=10 | imported | test_admin_api_phase2_part_3.py |
| TC-ADM-7924 | P1 | Import 10 scenario 11 | size=10,scenario=11 | imported | test_admin_api_phase2_part_3.py |
| TC-ADM-7925 | P1 | Import 10 scenario 12 | size=10,scenario=12 | imported | test_admin_api_phase2_part_3.py |
| TC-ADM-7926 | P1 | Import 10 scenario 13 | size=10,scenario=13 | imported | test_admin_api_phase2_part_3.py |
| TC-ADM-7927 | P1 | Import 10 scenario 14 | size=10,scenario=14 | imported | test_admin_api_phase2_part_3.py |
| TC-ADM-7928 | P1 | Import 25 scenario 0 | size=25,scenario=0 | imported | test_admin_api_phase2_part_3.py |
| TC-ADM-7929 | P1 | Import 25 scenario 1 | size=25,scenario=1 | imported | test_admin_api_phase2_part_3.py |
| TC-ADM-7930 | P1 | Import 25 scenario 2 | size=25,scenario=2 | imported | test_admin_api_phase2_part_3.py |
| TC-ADM-7931 | P1 | Import 25 scenario 3 | size=25,scenario=3 | imported | test_admin_api_phase2_part_3.py |
| TC-ADM-7932 | P1 | Import 25 scenario 4 | size=25,scenario=4 | imported | test_admin_api_phase2_part_3.py |
| TC-ADM-7933 | P1 | Import 25 scenario 5 | size=25,scenario=5 | imported | test_admin_api_phase2_part_3.py |
| TC-ADM-7934 | P1 | Import 25 scenario 6 | size=25,scenario=6 | imported | test_admin_api_phase2_part_3.py |
| TC-ADM-7935 | P1 | Import 25 scenario 7 | size=25,scenario=7 | imported | test_admin_api_phase2_part_3.py |
| TC-ADM-7936 | P1 | Import 25 scenario 8 | size=25,scenario=8 | imported | test_admin_api_phase2_part_3.py |
| TC-ADM-7937 | P1 | Import 25 scenario 9 | size=25,scenario=9 | imported | test_admin_api_phase2_part_3.py |
| TC-ADM-7938 | P1 | Import 25 scenario 10 | size=25,scenario=10 | imported | test_admin_api_phase2_part_3.py |
| TC-ADM-7939 | P1 | Import 25 scenario 11 | size=25,scenario=11 | imported | test_admin_api_phase2_part_3.py |
| TC-ADM-7940 | P1 | Import 25 scenario 12 | size=25,scenario=12 | imported | test_admin_api_phase2_part_3.py |
| TC-ADM-7941 | P1 | Import 25 scenario 13 | size=25,scenario=13 | imported | test_admin_api_phase2_part_3.py |
| TC-ADM-7942 | P1 | Import 25 scenario 14 | size=25,scenario=14 | imported | test_admin_api_phase2_part_3.py |
| TC-ADM-7943 | P1 | Import 50 scenario 0 | size=50,scenario=0 | imported | test_admin_api_phase2_part_3.py |
| TC-ADM-7944 | P1 | Import 50 scenario 1 | size=50,scenario=1 | imported | test_admin_api_phase2_part_3.py |
| TC-ADM-7945 | P1 | Import 50 scenario 2 | size=50,scenario=2 | imported | test_admin_api_phase2_part_3.py |
| TC-ADM-7946 | P1 | Import 50 scenario 3 | size=50,scenario=3 | imported | test_admin_api_phase2_part_3.py |
| TC-ADM-7947 | P1 | Import 50 scenario 4 | size=50,scenario=4 | imported | test_admin_api_phase2_part_3.py |
| TC-ADM-7948 | P1 | Import 50 scenario 5 | size=50,scenario=5 | imported | test_admin_api_phase2_part_3.py |
| TC-ADM-7949 | P1 | Import 50 scenario 6 | size=50,scenario=6 | imported | test_admin_api_phase2_part_3.py |
| TC-ADM-7950 | P1 | Import 50 scenario 7 | size=50,scenario=7 | imported | test_admin_api_phase2_part_3.py |
| TC-ADM-7951 | P1 | Import 50 scenario 8 | size=50,scenario=8 | imported | test_admin_api_phase2_part_3.py |
| TC-ADM-7952 | P1 | Import 50 scenario 9 | size=50,scenario=9 | imported | test_admin_api_phase2_part_3.py |
| TC-ADM-7953 | P1 | Import 50 scenario 10 | size=50,scenario=10 | imported | test_admin_api_phase2_part_3.py |
| TC-ADM-7954 | P1 | Import 50 scenario 11 | size=50,scenario=11 | imported | test_admin_api_phase2_part_3.py |
| TC-ADM-7955 | P1 | Import 50 scenario 12 | size=50,scenario=12 | imported | test_admin_api_phase2_part_3.py |
| TC-ADM-7956 | P1 | Import 50 scenario 13 | size=50,scenario=13 | imported | test_admin_api_phase2_part_3.py |
| TC-ADM-7957 | P1 | Import 50 scenario 14 | size=50,scenario=14 | imported | test_admin_api_phase2_part_3.py |
| TC-ADM-7958 | P1 | Import 100 scenario 0 | size=100,scenario=0 | imported | test_admin_api_phase2_part_3.py |
| TC-ADM-7959 | P1 | Import 100 scenario 1 | size=100,scenario=1 | imported | test_admin_api_phase2_part_3.py |
| TC-ADM-7960 | P1 | Import 100 scenario 2 | size=100,scenario=2 | imported | test_admin_api_phase2_part_3.py |
| TC-ADM-7961 | P1 | Import 100 scenario 3 | size=100,scenario=3 | imported | test_admin_api_phase2_part_3.py |
| TC-ADM-7962 | P1 | Import 100 scenario 4 | size=100,scenario=4 | imported | test_admin_api_phase2_part_3.py |
| TC-ADM-7963 | P1 | Import 100 scenario 5 | size=100,scenario=5 | imported | test_admin_api_phase2_part_3.py |
| TC-ADM-7964 | P1 | Import 100 scenario 6 | size=100,scenario=6 | imported | test_admin_api_phase2_part_3.py |
| TC-ADM-7965 | P1 | Import 100 scenario 7 | size=100,scenario=7 | imported | test_admin_api_phase2_part_3.py |
| TC-ADM-7966 | P1 | Import 100 scenario 8 | size=100,scenario=8 | imported | test_admin_api_phase2_part_3.py |
| TC-ADM-7967 | P1 | Import 100 scenario 9 | size=100,scenario=9 | imported | test_admin_api_phase2_part_3.py |
| TC-ADM-7973 | P1 | App config threshold=0 logic=or boosts=True,True | threshold=0,logic=or,sboost=True,uboost=True | stored | test_admin_api_phase2_part_3.py |
| TC-ADM-7974 | P1 | App config threshold=0 logic=or boosts=True,False | threshold=0,logic=or,sboost=True,uboost=False | stored | test_admin_api_phase2_part_3.py |
| TC-ADM-7975 | P1 | App config threshold=0 logic=or boosts=False,True | threshold=0,logic=or,sboost=False,uboost=True | stored | test_admin_api_phase2_part_3.py |
| TC-ADM-7976 | P1 | App config threshold=0 logic=or boosts=False,False | threshold=0,logic=or,sboost=False,uboost=False | stored | test_admin_api_phase2_part_3.py |
| TC-ADM-7977 | P1 | App config threshold=0 logic=and boosts=True,True | threshold=0,logic=and,sboost=True,uboost=True | stored | test_admin_api_phase2_part_3.py |
| TC-ADM-7978 | P1 | App config threshold=0 logic=and boosts=True,False | threshold=0,logic=and,sboost=True,uboost=False | stored | test_admin_api_phase2_part_3.py |
| TC-ADM-7979 | P1 | App config threshold=0 logic=and boosts=False,True | threshold=0,logic=and,sboost=False,uboost=True | stored | test_admin_api_phase2_part_3.py |
| TC-ADM-7980 | P1 | App config threshold=0 logic=and boosts=False,False | threshold=0,logic=and,sboost=False,uboost=False | stored | test_admin_api_phase2_part_3.py |
| TC-ADM-7981 | P1 | App config threshold=10 logic=or boosts=True,True | threshold=10,logic=or,sboost=True,uboost=True | stored | test_admin_api_phase2_part_3.py |
| TC-ADM-7982 | P1 | App config threshold=10 logic=or boosts=True,False | threshold=10,logic=or,sboost=True,uboost=False | stored | test_admin_api_phase2_part_3.py |
| TC-ADM-7983 | P1 | App config threshold=10 logic=or boosts=False,True | threshold=10,logic=or,sboost=False,uboost=True | stored | test_admin_api_phase2_part_3.py |
| TC-ADM-7984 | P1 | App config threshold=10 logic=or boosts=False,False | threshold=10,logic=or,sboost=False,uboost=False | stored | test_admin_api_phase2_part_3.py |
| TC-ADM-7985 | P1 | App config threshold=10 logic=and boosts=True,True | threshold=10,logic=and,sboost=True,uboost=True | stored | test_admin_api_phase2_part_3.py |
| TC-ADM-7986 | P1 | App config threshold=10 logic=and boosts=True,False | threshold=10,logic=and,sboost=True,uboost=False | stored | test_admin_api_phase2_part_3.py |
| TC-ADM-7987 | P1 | App config threshold=10 logic=and boosts=False,True | threshold=10,logic=and,sboost=False,uboost=True | stored | test_admin_api_phase2_part_3.py |
| TC-ADM-7988 | P1 | App config threshold=10 logic=and boosts=False,False | threshold=10,logic=and,sboost=False,uboost=False | stored | test_admin_api_phase2_part_3.py |
| TC-ADM-7989 | P1 | App config threshold=20 logic=or boosts=True,True | threshold=20,logic=or,sboost=True,uboost=True | stored | test_admin_api_phase2_part_3.py |
| TC-ADM-7990 | P1 | App config threshold=20 logic=or boosts=True,False | threshold=20,logic=or,sboost=True,uboost=False | stored | test_admin_api_phase2_part_3.py |
| TC-ADM-7991 | P1 | App config threshold=20 logic=or boosts=False,True | threshold=20,logic=or,sboost=False,uboost=True | stored | test_admin_api_phase2_part_3.py |
| TC-ADM-7992 | P1 | App config threshold=20 logic=or boosts=False,False | threshold=20,logic=or,sboost=False,uboost=False | stored | test_admin_api_phase2_part_3.py |
| TC-ADM-7993 | P1 | App config threshold=20 logic=and boosts=True,True | threshold=20,logic=and,sboost=True,uboost=True | stored | test_admin_api_phase2_part_3.py |
| TC-ADM-7994 | P1 | App config threshold=20 logic=and boosts=True,False | threshold=20,logic=and,sboost=True,uboost=False | stored | test_admin_api_phase2_part_3.py |
| TC-ADM-7995 | P1 | App config threshold=20 logic=and boosts=False,True | threshold=20,logic=and,sboost=False,uboost=True | stored | test_admin_api_phase2_part_3.py |
| TC-ADM-7996 | P1 | App config threshold=20 logic=and boosts=False,False | threshold=20,logic=and,sboost=False,uboost=False | stored | test_admin_api_phase2_part_3.py |
| TC-ADM-7997 | P1 | App config threshold=30 logic=or boosts=True,True | threshold=30,logic=or,sboost=True,uboost=True | stored | test_admin_api_phase2_part_3.py |
| TC-ADM-7998 | P1 | App config threshold=30 logic=or boosts=True,False | threshold=30,logic=or,sboost=True,uboost=False | stored | test_admin_api_phase2_part_3.py |
| TC-ADM-7999 | P1 | App config threshold=30 logic=or boosts=False,True | threshold=30,logic=or,sboost=False,uboost=True | stored | test_admin_api_phase2_part_3.py |
| TC-ADM-8000 | P1 | App config threshold=30 logic=or boosts=False,False | threshold=30,logic=or,sboost=False,uboost=False | stored | test_admin_api_phase2_part_3.py |
| TC-ADM-8001 | P1 | App config threshold=30 logic=and boosts=True,True | threshold=30,logic=and,sboost=True,uboost=True | stored | test_admin_api_phase2_part_3.py |
| TC-ADM-8002 | P1 | App config threshold=30 logic=and boosts=True,False | threshold=30,logic=and,sboost=True,uboost=False | stored | test_admin_api_phase2_part_3.py |
| TC-ADM-8003 | P1 | App config threshold=30 logic=and boosts=False,True | threshold=30,logic=and,sboost=False,uboost=True | stored | test_admin_api_phase2_part_3.py |
| TC-ADM-8004 | P1 | App config threshold=30 logic=and boosts=False,False | threshold=30,logic=and,sboost=False,uboost=False | stored | test_admin_api_phase2_part_3.py |
| TC-ADM-8005 | P1 | App config threshold=40 logic=or boosts=True,True | threshold=40,logic=or,sboost=True,uboost=True | stored | test_admin_api_phase2_part_3.py |
| TC-ADM-8006 | P1 | App config threshold=40 logic=or boosts=True,False | threshold=40,logic=or,sboost=True,uboost=False | stored | test_admin_api_phase2_part_3.py |
| TC-ADM-8007 | P1 | App config threshold=40 logic=or boosts=False,True | threshold=40,logic=or,sboost=False,uboost=True | stored | test_admin_api_phase2_part_3.py |
| TC-ADM-8008 | P1 | App config threshold=40 logic=or boosts=False,False | threshold=40,logic=or,sboost=False,uboost=False | stored | test_admin_api_phase2_part_3.py |
| TC-ADM-8009 | P1 | App config threshold=40 logic=and boosts=True,True | threshold=40,logic=and,sboost=True,uboost=True | stored | test_admin_api_phase2_part_3.py |
| TC-ADM-8010 | P1 | App config threshold=40 logic=and boosts=True,False | threshold=40,logic=and,sboost=True,uboost=False | stored | test_admin_api_phase2_part_3.py |
| TC-ADM-8011 | P1 | App config threshold=40 logic=and boosts=False,True | threshold=40,logic=and,sboost=False,uboost=True | stored | test_admin_api_phase2_part_3.py |
| TC-ADM-8012 | P1 | App config threshold=40 logic=and boosts=False,False | threshold=40,logic=and,sboost=False,uboost=False | stored | test_admin_api_phase2_part_3.py |
| TC-ADM-8013 | P1 | App config threshold=50 logic=or boosts=True,True | threshold=50,logic=or,sboost=True,uboost=True | stored | test_admin_api_phase2_part_3.py |
| TC-ADM-8014 | P1 | App config threshold=50 logic=or boosts=True,False | threshold=50,logic=or,sboost=True,uboost=False | stored | test_admin_api_phase2_part_3.py |
| TC-ADM-8015 | P1 | App config threshold=50 logic=or boosts=False,True | threshold=50,logic=or,sboost=False,uboost=True | stored | test_admin_api_phase2_part_3.py |
| TC-ADM-8016 | P1 | App config threshold=50 logic=or boosts=False,False | threshold=50,logic=or,sboost=False,uboost=False | stored | test_admin_api_phase2_part_3.py |
| TC-ADM-8017 | P1 | App config threshold=50 logic=and boosts=True,True | threshold=50,logic=and,sboost=True,uboost=True | stored | test_admin_api_phase2_part_3.py |
| TC-ADM-8018 | P1 | App config threshold=50 logic=and boosts=True,False | threshold=50,logic=and,sboost=True,uboost=False | stored | test_admin_api_phase2_part_3.py |
| TC-ADM-8019 | P1 | App config threshold=50 logic=and boosts=False,True | threshold=50,logic=and,sboost=False,uboost=True | stored | test_admin_api_phase2_part_3.py |
| TC-ADM-8020 | P1 | App config threshold=50 logic=and boosts=False,False | threshold=50,logic=and,sboost=False,uboost=False | stored | test_admin_api_phase2_part_3.py |
| TC-ADM-8021 | P1 | App config threshold=60 logic=or boosts=True,True | threshold=60,logic=or,sboost=True,uboost=True | stored | test_admin_api_phase2_part_3.py |
| TC-ADM-8022 | P1 | App config threshold=60 logic=or boosts=True,False | threshold=60,logic=or,sboost=True,uboost=False | stored | test_admin_api_phase2_part_3.py |
| TC-ADM-8023 | P1 | App config threshold=60 logic=or boosts=False,True | threshold=60,logic=or,sboost=False,uboost=True | stored | test_admin_api_phase2_part_4.py |
| TC-ADM-8024 | P1 | App config threshold=60 logic=or boosts=False,False | threshold=60,logic=or,sboost=False,uboost=False | stored | test_admin_api_phase2_part_4.py |
| TC-ADM-8025 | P1 | App config threshold=60 logic=and boosts=True,True | threshold=60,logic=and,sboost=True,uboost=True | stored | test_admin_api_phase2_part_4.py |
| TC-ADM-8026 | P1 | App config threshold=60 logic=and boosts=True,False | threshold=60,logic=and,sboost=True,uboost=False | stored | test_admin_api_phase2_part_4.py |
| TC-ADM-8027 | P1 | App config threshold=60 logic=and boosts=False,True | threshold=60,logic=and,sboost=False,uboost=True | stored | test_admin_api_phase2_part_4.py |
| TC-ADM-8028 | P1 | App config threshold=60 logic=and boosts=False,False | threshold=60,logic=and,sboost=False,uboost=False | stored | test_admin_api_phase2_part_4.py |
| TC-ADM-8029 | P1 | App config threshold=70 logic=or boosts=True,True | threshold=70,logic=or,sboost=True,uboost=True | stored | test_admin_api_phase2_part_4.py |
| TC-ADM-8030 | P1 | App config threshold=70 logic=or boosts=True,False | threshold=70,logic=or,sboost=True,uboost=False | stored | test_admin_api_phase2_part_4.py |
| TC-ADM-8031 | P1 | App config threshold=70 logic=or boosts=False,True | threshold=70,logic=or,sboost=False,uboost=True | stored | test_admin_api_phase2_part_4.py |
| TC-ADM-8032 | P1 | App config threshold=70 logic=or boosts=False,False | threshold=70,logic=or,sboost=False,uboost=False | stored | test_admin_api_phase2_part_4.py |
| TC-ADM-8033 | P1 | App config threshold=70 logic=and boosts=True,True | threshold=70,logic=and,sboost=True,uboost=True | stored | test_admin_api_phase2_part_4.py |
| TC-ADM-8034 | P1 | App config threshold=70 logic=and boosts=True,False | threshold=70,logic=and,sboost=True,uboost=False | stored | test_admin_api_phase2_part_4.py |
| TC-ADM-8035 | P1 | App config threshold=70 logic=and boosts=False,True | threshold=70,logic=and,sboost=False,uboost=True | stored | test_admin_api_phase2_part_4.py |
| TC-ADM-8036 | P1 | App config threshold=70 logic=and boosts=False,False | threshold=70,logic=and,sboost=False,uboost=False | stored | test_admin_api_phase2_part_4.py |
| TC-ADM-8037 | P1 | App config threshold=80 logic=or boosts=True,True | threshold=80,logic=or,sboost=True,uboost=True | stored | test_admin_api_phase2_part_4.py |
| TC-ADM-8038 | P1 | App config threshold=80 logic=or boosts=True,False | threshold=80,logic=or,sboost=True,uboost=False | stored | test_admin_api_phase2_part_4.py |
| TC-ADM-8039 | P1 | App config threshold=80 logic=or boosts=False,True | threshold=80,logic=or,sboost=False,uboost=True | stored | test_admin_api_phase2_part_4.py |
| TC-ADM-8040 | P1 | App config threshold=80 logic=or boosts=False,False | threshold=80,logic=or,sboost=False,uboost=False | stored | test_admin_api_phase2_part_4.py |
| TC-ADM-8041 | P1 | App config threshold=80 logic=and boosts=True,True | threshold=80,logic=and,sboost=True,uboost=True | stored | test_admin_api_phase2_part_4.py |
| TC-ADM-8042 | P1 | App config threshold=80 logic=and boosts=True,False | threshold=80,logic=and,sboost=True,uboost=False | stored | test_admin_api_phase2_part_4.py |
| TC-ADM-8043 | P1 | App config threshold=80 logic=and boosts=False,True | threshold=80,logic=and,sboost=False,uboost=True | stored | test_admin_api_phase2_part_4.py |
| TC-ADM-8044 | P1 | App config threshold=80 logic=and boosts=False,False | threshold=80,logic=and,sboost=False,uboost=False | stored | test_admin_api_phase2_part_4.py |
| TC-ADM-8045 | P1 | App config threshold=90 logic=or boosts=True,True | threshold=90,logic=or,sboost=True,uboost=True | stored | test_admin_api_phase2_part_4.py |
| TC-ADM-8046 | P1 | App config threshold=90 logic=or boosts=True,False | threshold=90,logic=or,sboost=True,uboost=False | stored | test_admin_api_phase2_part_4.py |
| TC-ADM-8047 | P1 | App config threshold=90 logic=or boosts=False,True | threshold=90,logic=or,sboost=False,uboost=True | stored | test_admin_api_phase2_part_4.py |
| TC-ADM-8048 | P1 | App config threshold=90 logic=or boosts=False,False | threshold=90,logic=or,sboost=False,uboost=False | stored | test_admin_api_phase2_part_4.py |
| TC-ADM-8049 | P1 | App config threshold=90 logic=and boosts=True,True | threshold=90,logic=and,sboost=True,uboost=True | stored | test_admin_api_phase2_part_4.py |
| TC-ADM-8050 | P1 | App config threshold=90 logic=and boosts=True,False | threshold=90,logic=and,sboost=True,uboost=False | stored | test_admin_api_phase2_part_4.py |
| TC-ADM-8051 | P1 | App config threshold=90 logic=and boosts=False,True | threshold=90,logic=and,sboost=False,uboost=True | stored | test_admin_api_phase2_part_4.py |
| TC-ADM-8052 | P1 | App config threshold=90 logic=and boosts=False,False | threshold=90,logic=and,sboost=False,uboost=False | stored | test_admin_api_phase2_part_4.py |
| TC-ADM-8053 | P1 | App config threshold=100 logic=or boosts=True,True | threshold=100,logic=or,sboost=True,uboost=True | stored | test_admin_api_phase2_part_4.py |
| TC-ADM-8054 | P1 | App config threshold=100 logic=or boosts=True,False | threshold=100,logic=or,sboost=True,uboost=False | stored | test_admin_api_phase2_part_4.py |
| TC-ADM-8055 | P1 | App config threshold=100 logic=or boosts=False,True | threshold=100,logic=or,sboost=False,uboost=True | stored | test_admin_api_phase2_part_4.py |
| TC-ADM-8056 | P1 | App config threshold=100 logic=or boosts=False,False | threshold=100,logic=or,sboost=False,uboost=False | stored | test_admin_api_phase2_part_4.py |
| TC-ADM-8057 | P1 | App config threshold=100 logic=and boosts=True,True | threshold=100,logic=and,sboost=True,uboost=True | stored | test_admin_api_phase2_part_4.py |
| TC-ADM-8058 | P1 | App config threshold=100 logic=and boosts=True,False | threshold=100,logic=and,sboost=True,uboost=False | stored | test_admin_api_phase2_part_4.py |
| TC-ADM-8059 | P1 | App config threshold=100 logic=and boosts=False,True | threshold=100,logic=and,sboost=False,uboost=True | stored | test_admin_api_phase2_part_4.py |
| TC-ADM-8060 | P1 | App config threshold=100 logic=and boosts=False,False | threshold=100,logic=and,sboost=False,uboost=False | stored | test_admin_api_phase2_part_4.py |
| TC-ADM-8061 | P2 | App config invalid threshold -1 | threshold=-1 | rejected | test_admin_api_phase2_part_4.py |
| TC-ADM-8062 | P2 | App config invalid threshold 101 | threshold=101 | rejected | test_admin_api_phase2_part_4.py |
| TC-ADM-8063 | P2 | App config default lookup 0 | app=ghost0 | defaults | test_admin_api_phase2_part_4.py |
| TC-ADM-8064 | P2 | App config default lookup 1 | app=ghost1 | defaults | test_admin_api_phase2_part_4.py |
| TC-ADM-8065 | P2 | App config default lookup 2 | app=ghost2 | defaults | test_admin_api_phase2_part_4.py |
| TC-ADM-8066 | P2 | App config default lookup 3 | app=ghost3 | defaults | test_admin_api_phase2_part_4.py |
| TC-ADM-8067 | P2 | App config default lookup 4 | app=ghost4 | defaults | test_admin_api_phase2_part_4.py |
| TC-ADM-8068 | P2 | App config default lookup 5 | app=ghost5 | defaults | test_admin_api_phase2_part_4.py |
| TC-ADM-8069 | P2 | App config default lookup 6 | app=ghost6 | defaults | test_admin_api_phase2_part_4.py |
| TC-ADM-8070 | P2 | App config default lookup 7 | app=ghost7 | defaults | test_admin_api_phase2_part_4.py |
| TC-ADM-8071 | P2 | App config default lookup 8 | app=ghost8 | defaults | test_admin_api_phase2_part_4.py |
| TC-ADM-8072 | P2 | App config default lookup 9 | app=ghost9 | defaults | test_admin_api_phase2_part_4.py |
| TC-ADM-8073 | P2 | Settings endpoint WEIGHT_DETECTOR_AHO = 5 | key=WEIGHT_DETECTOR_AHO,value=5 | updated | test_admin_api_phase2_part_4.py |
| TC-ADM-8074 | P2 | Settings endpoint WEIGHT_DETECTOR_AHO = 8 | key=WEIGHT_DETECTOR_AHO,value=8 | updated | test_admin_api_phase2_part_4.py |
| TC-ADM-8075 | P2 | Settings endpoint WEIGHT_DETECTOR_AHO = 10 | key=WEIGHT_DETECTOR_AHO,value=10 | updated | test_admin_api_phase2_part_4.py |
| TC-ADM-8076 | P2 | Settings endpoint WEIGHT_DETECTOR_AHO = 12 | key=WEIGHT_DETECTOR_AHO,value=12 | updated | test_admin_api_phase2_part_4.py |
| TC-ADM-8077 | P2 | Settings endpoint WEIGHT_DETECTOR_AHO = 15 | key=WEIGHT_DETECTOR_AHO,value=15 | updated | test_admin_api_phase2_part_4.py |
| TC-ADM-8078 | P2 | Settings endpoint WEIGHT_DETECTOR_AHO = 18 | key=WEIGHT_DETECTOR_AHO,value=18 | updated | test_admin_api_phase2_part_4.py |
| TC-ADM-8079 | P2 | Settings endpoint WEIGHT_DETECTOR_AHO = 20 | key=WEIGHT_DETECTOR_AHO,value=20 | updated | test_admin_api_phase2_part_4.py |
| TC-ADM-8080 | P2 | Settings endpoint WEIGHT_DETECTOR_AHO = 22 | key=WEIGHT_DETECTOR_AHO,value=22 | updated | test_admin_api_phase2_part_4.py |
| TC-ADM-8081 | P2 | Settings endpoint WEIGHT_DETECTOR_AHO = 25 | key=WEIGHT_DETECTOR_AHO,value=25 | updated | test_admin_api_phase2_part_4.py |
| TC-ADM-8082 | P2 | Settings endpoint WEIGHT_DETECTOR_AHO = 28 | key=WEIGHT_DETECTOR_AHO,value=28 | updated | test_admin_api_phase2_part_4.py |
| TC-ADM-8083 | P2 | Settings endpoint WEIGHT_DETECTOR_AHO = 30 | key=WEIGHT_DETECTOR_AHO,value=30 | updated | test_admin_api_phase2_part_4.py |
| TC-ADM-8084 | P2 | Settings endpoint WEIGHT_DETECTOR_AHO = 32 | key=WEIGHT_DETECTOR_AHO,value=32 | updated | test_admin_api_phase2_part_4.py |
| TC-ADM-8085 | P2 | Settings endpoint WEIGHT_DETECTOR_AHO = 35 | key=WEIGHT_DETECTOR_AHO,value=35 | updated | test_admin_api_phase2_part_4.py |
| TC-ADM-8086 | P2 | Settings endpoint WEIGHT_DETECTOR_AHO = 38 | key=WEIGHT_DETECTOR_AHO,value=38 | updated | test_admin_api_phase2_part_4.py |
| TC-ADM-8087 | P2 | Settings endpoint WEIGHT_DETECTOR_AHO = 40 | key=WEIGHT_DETECTOR_AHO,value=40 | updated | test_admin_api_phase2_part_4.py |
| TC-ADM-8088 | P2 | Settings endpoint WEIGHT_DETECTOR_AHO = 42 | key=WEIGHT_DETECTOR_AHO,value=42 | updated | test_admin_api_phase2_part_4.py |
| TC-ADM-8089 | P2 | Settings endpoint WEIGHT_DETECTOR_AHO = 45 | key=WEIGHT_DETECTOR_AHO,value=45 | updated | test_admin_api_phase2_part_4.py |
| TC-ADM-8090 | P2 | Settings endpoint WEIGHT_DETECTOR_AHO = 47 | key=WEIGHT_DETECTOR_AHO,value=47 | updated | test_admin_api_phase2_part_4.py |
| TC-ADM-8091 | P2 | Settings endpoint WEIGHT_DETECTOR_AHO = 49 | key=WEIGHT_DETECTOR_AHO,value=49 | updated | test_admin_api_phase2_part_4.py |
| TC-ADM-8092 | P2 | Settings endpoint WEIGHT_DETECTOR_AHO = 50 | key=WEIGHT_DETECTOR_AHO,value=50 | updated | test_admin_api_phase2_part_4.py |
| TC-ADM-8093 | P2 | Settings endpoint WEIGHT_USER = 5 | key=WEIGHT_USER,value=5 | updated | test_admin_api_phase2_part_4.py |
| TC-ADM-8094 | P2 | Settings endpoint WEIGHT_USER = 7 | key=WEIGHT_USER,value=7 | updated | test_admin_api_phase2_part_4.py |
| TC-ADM-8095 | P2 | Settings endpoint WEIGHT_USER = 9 | key=WEIGHT_USER,value=9 | updated | test_admin_api_phase2_part_4.py |
| TC-ADM-8096 | P2 | Settings endpoint WEIGHT_USER = 11 | key=WEIGHT_USER,value=11 | updated | test_admin_api_phase2_part_4.py |
| TC-ADM-8097 | P2 | Settings endpoint WEIGHT_USER = 13 | key=WEIGHT_USER,value=13 | updated | test_admin_api_phase2_part_4.py |
| TC-ADM-8098 | P2 | Settings endpoint WEIGHT_USER = 16 | key=WEIGHT_USER,value=16 | updated | test_admin_api_phase2_part_4.py |
| TC-ADM-8099 | P2 | Settings endpoint WEIGHT_USER = 19 | key=WEIGHT_USER,value=19 | updated | test_admin_api_phase2_part_4.py |
| TC-ADM-8100 | P2 | Settings endpoint WEIGHT_USER = 21 | key=WEIGHT_USER,value=21 | updated | test_admin_api_phase2_part_4.py |
| TC-ADM-8101 | P2 | Settings endpoint WEIGHT_USER = 24 | key=WEIGHT_USER,value=24 | updated | test_admin_api_phase2_part_4.py |
| TC-ADM-8102 | P2 | Settings endpoint WEIGHT_USER = 26 | key=WEIGHT_USER,value=26 | updated | test_admin_api_phase2_part_4.py |
| TC-ADM-8103 | P2 | Settings endpoint WEIGHT_USER = 29 | key=WEIGHT_USER,value=29 | updated | test_admin_api_phase2_part_4.py |
| TC-ADM-8104 | P2 | Settings endpoint WEIGHT_USER = 31 | key=WEIGHT_USER,value=31 | updated | test_admin_api_phase2_part_4.py |
| TC-ADM-8105 | P2 | Settings endpoint WEIGHT_USER = 34 | key=WEIGHT_USER,value=34 | updated | test_admin_api_phase2_part_4.py |
| TC-ADM-8106 | P2 | Settings endpoint WEIGHT_USER = 36 | key=WEIGHT_USER,value=36 | updated | test_admin_api_phase2_part_4.py |
| TC-ADM-8107 | P2 | Settings endpoint WEIGHT_USER = 39 | key=WEIGHT_USER,value=39 | updated | test_admin_api_phase2_part_4.py |
| TC-ADM-8108 | P2 | Settings endpoint WEIGHT_USER = 41 | key=WEIGHT_USER,value=41 | updated | test_admin_api_phase2_part_4.py |
| TC-ADM-8109 | P2 | Settings endpoint WEIGHT_USER = 44 | key=WEIGHT_USER,value=44 | updated | test_admin_api_phase2_part_4.py |
| TC-ADM-8110 | P2 | Settings endpoint WEIGHT_USER = 46 | key=WEIGHT_USER,value=46 | updated | test_admin_api_phase2_part_4.py |
| TC-ADM-8111 | P2 | Settings endpoint WEIGHT_USER = 48 | key=WEIGHT_USER,value=48 | updated | test_admin_api_phase2_part_4.py |
| TC-ADM-8112 | P2 | Settings endpoint WEIGHT_USER = 50 | key=WEIGHT_USER,value=50 | updated | test_admin_api_phase2_part_4.py |
| TC-ADM-8113 | P2 | Settings endpoint SEMANTIC_TOP_K = 1 | key=SEMANTIC_TOP_K,value=1 | updated | test_admin_api_phase2_part_4.py |
| TC-ADM-8114 | P2 | Settings endpoint SEMANTIC_TOP_K = 2 | key=SEMANTIC_TOP_K,value=2 | updated | test_admin_api_phase2_part_4.py |
| TC-ADM-8115 | P2 | Settings endpoint SEMANTIC_TOP_K = 3 | key=SEMANTIC_TOP_K,value=3 | updated | test_admin_api_phase2_part_4.py |
| TC-ADM-8116 | P2 | Settings endpoint SEMANTIC_TOP_K = 5 | key=SEMANTIC_TOP_K,value=5 | updated | test_admin_api_phase2_part_4.py |
| TC-ADM-8117 | P2 | Settings endpoint SEMANTIC_TOP_K = 8 | key=SEMANTIC_TOP_K,value=8 | updated | test_admin_api_phase2_part_4.py |
| TC-ADM-8118 | P2 | Settings endpoint SEMANTIC_TOP_K = 10 | key=SEMANTIC_TOP_K,value=10 | updated | test_admin_api_phase2_part_4.py |
| TC-ADM-8119 | P2 | Settings endpoint SEMANTIC_TOP_K = 12 | key=SEMANTIC_TOP_K,value=12 | updated | test_admin_api_phase2_part_4.py |
| TC-ADM-8120 | P2 | Settings endpoint SEMANTIC_TOP_K = 16 | key=SEMANTIC_TOP_K,value=16 | updated | test_admin_api_phase2_part_4.py |
| TC-ADM-8121 | P2 | Settings endpoint SEMANTIC_TOP_K = 20 | key=SEMANTIC_TOP_K,value=20 | updated | test_admin_api_phase2_part_4.py |
| TC-ADM-8122 | P2 | Settings endpoint SEMANTIC_TOP_K = 25 | key=SEMANTIC_TOP_K,value=25 | updated | test_admin_api_phase2_part_4.py |
| TC-ADM-8123 | P2 | Settings endpoint SEMANTIC_TOP_K = 32 | key=SEMANTIC_TOP_K,value=32 | updated | test_admin_api_phase2_part_5.py |
| TC-ADM-8124 | P2 | Settings endpoint SEMANTIC_TOP_K = 40 | key=SEMANTIC_TOP_K,value=40 | updated | test_admin_api_phase2_part_5.py |
| TC-ADM-8125 | P2 | Settings endpoint SEMANTIC_TOP_K = 50 | key=SEMANTIC_TOP_K,value=50 | updated | test_admin_api_phase2_part_5.py |
| TC-ADM-8126 | P2 | Settings endpoint SEMANTIC_TOP_K = 60 | key=SEMANTIC_TOP_K,value=60 | updated | test_admin_api_phase2_part_5.py |
| TC-ADM-8127 | P2 | Settings endpoint SEMANTIC_TOP_K = 70 | key=SEMANTIC_TOP_K,value=70 | updated | test_admin_api_phase2_part_5.py |
| TC-ADM-8128 | P2 | Settings endpoint SEMANTIC_TOP_K = 80 | key=SEMANTIC_TOP_K,value=80 | updated | test_admin_api_phase2_part_5.py |
| TC-ADM-8129 | P2 | Settings endpoint SEMANTIC_TOP_K = 88 | key=SEMANTIC_TOP_K,value=88 | updated | test_admin_api_phase2_part_5.py |
| TC-ADM-8130 | P2 | Settings endpoint SEMANTIC_TOP_K = 92 | key=SEMANTIC_TOP_K,value=92 | updated | test_admin_api_phase2_part_5.py |
| TC-ADM-8131 | P2 | Settings endpoint SEMANTIC_TOP_K = 96 | key=SEMANTIC_TOP_K,value=96 | updated | test_admin_api_phase2_part_5.py |
| TC-ADM-8132 | P2 | Settings endpoint SEMANTIC_TOP_K = 100 | key=SEMANTIC_TOP_K,value=100 | updated | test_admin_api_phase2_part_5.py |
| TC-ADM-8133 | P2 | Settings endpoint CACHE_MAX_SIZE = 1 | key=CACHE_MAX_SIZE,value=1 | updated | test_admin_api_phase2_part_5.py |
| TC-ADM-8134 | P2 | Settings endpoint CACHE_MAX_SIZE = 5 | key=CACHE_MAX_SIZE,value=5 | updated | test_admin_api_phase2_part_5.py |
| TC-ADM-8135 | P2 | Settings endpoint CACHE_MAX_SIZE = 10 | key=CACHE_MAX_SIZE,value=10 | updated | test_admin_api_phase2_part_5.py |
| TC-ADM-8136 | P2 | Settings endpoint CACHE_MAX_SIZE = 50 | key=CACHE_MAX_SIZE,value=50 | updated | test_admin_api_phase2_part_5.py |
| TC-ADM-8137 | P2 | Settings endpoint CACHE_MAX_SIZE = 100 | key=CACHE_MAX_SIZE,value=100 | updated | test_admin_api_phase2_part_5.py |
| TC-ADM-8138 | P2 | Settings endpoint CACHE_MAX_SIZE = 500 | key=CACHE_MAX_SIZE,value=500 | updated | test_admin_api_phase2_part_5.py |
| TC-ADM-8139 | P2 | Settings endpoint CACHE_MAX_SIZE = 1000 | key=CACHE_MAX_SIZE,value=1000 | updated | test_admin_api_phase2_part_5.py |
| TC-ADM-8140 | P2 | Settings endpoint CACHE_MAX_SIZE = 2500 | key=CACHE_MAX_SIZE,value=2500 | updated | test_admin_api_phase2_part_5.py |
| TC-ADM-8141 | P2 | Settings endpoint CACHE_MAX_SIZE = 5000 | key=CACHE_MAX_SIZE,value=5000 | updated | test_admin_api_phase2_part_5.py |
| TC-ADM-8142 | P2 | Settings endpoint CACHE_MAX_SIZE = 10000 | key=CACHE_MAX_SIZE,value=10000 | updated | test_admin_api_phase2_part_5.py |
| TC-ADM-8143 | P2 | Settings endpoint CACHE_MAX_SIZE = 20000 | key=CACHE_MAX_SIZE,value=20000 | updated | test_admin_api_phase2_part_5.py |
| TC-ADM-8144 | P2 | Settings endpoint CACHE_MAX_SIZE = 30000 | key=CACHE_MAX_SIZE,value=30000 | updated | test_admin_api_phase2_part_5.py |
| TC-ADM-8145 | P2 | Settings endpoint CACHE_MAX_SIZE = 40000 | key=CACHE_MAX_SIZE,value=40000 | updated | test_admin_api_phase2_part_5.py |
| TC-ADM-8146 | P2 | Settings endpoint CACHE_MAX_SIZE = 50000 | key=CACHE_MAX_SIZE,value=50000 | updated | test_admin_api_phase2_part_5.py |
| TC-ADM-8147 | P2 | Settings endpoint CACHE_MAX_SIZE = 60000 | key=CACHE_MAX_SIZE,value=60000 | updated | test_admin_api_phase2_part_5.py |
| TC-ADM-8148 | P2 | Settings endpoint CACHE_MAX_SIZE = 70000 | key=CACHE_MAX_SIZE,value=70000 | updated | test_admin_api_phase2_part_5.py |
| TC-ADM-8149 | P2 | Settings endpoint CACHE_MAX_SIZE = 80000 | key=CACHE_MAX_SIZE,value=80000 | updated | test_admin_api_phase2_part_5.py |
| TC-ADM-8150 | P2 | Settings endpoint CACHE_MAX_SIZE = 90000 | key=CACHE_MAX_SIZE,value=90000 | updated | test_admin_api_phase2_part_5.py |
| TC-ADM-8151 | P2 | Settings endpoint CACHE_MAX_SIZE = 95000 | key=CACHE_MAX_SIZE,value=95000 | updated | test_admin_api_phase2_part_5.py |
| TC-ADM-8152 | P2 | Settings endpoint CACHE_MAX_SIZE = 100000 | key=CACHE_MAX_SIZE,value=100000 | updated | test_admin_api_phase2_part_5.py |
| TC-ADM-8153 | P2 | Settings endpoint RATE_LIMIT_PERIOD = 1 | key=RATE_LIMIT_PERIOD,value=1 | updated | test_admin_api_phase2_part_5.py |
| TC-ADM-8154 | P2 | Settings endpoint RATE_LIMIT_PERIOD = 5 | key=RATE_LIMIT_PERIOD,value=5 | updated | test_admin_api_phase2_part_5.py |
| TC-ADM-8155 | P2 | Settings endpoint RATE_LIMIT_PERIOD = 10 | key=RATE_LIMIT_PERIOD,value=10 | updated | test_admin_api_phase2_part_5.py |
| TC-ADM-8156 | P2 | Settings endpoint RATE_LIMIT_PERIOD = 30 | key=RATE_LIMIT_PERIOD,value=30 | updated | test_admin_api_phase2_part_5.py |
| TC-ADM-8157 | P2 | Settings endpoint RATE_LIMIT_PERIOD = 60 | key=RATE_LIMIT_PERIOD,value=60 | updated | test_admin_api_phase2_part_5.py |
| TC-ADM-8158 | P2 | Settings endpoint RATE_LIMIT_PERIOD = 120 | key=RATE_LIMIT_PERIOD,value=120 | updated | test_admin_api_phase2_part_5.py |
| TC-ADM-8159 | P2 | Settings endpoint RATE_LIMIT_PERIOD = 300 | key=RATE_LIMIT_PERIOD,value=300 | updated | test_admin_api_phase2_part_5.py |
| TC-ADM-8160 | P2 | Settings endpoint RATE_LIMIT_PERIOD = 600 | key=RATE_LIMIT_PERIOD,value=600 | updated | test_admin_api_phase2_part_5.py |
| TC-ADM-8161 | P2 | Settings endpoint RATE_LIMIT_PERIOD = 900 | key=RATE_LIMIT_PERIOD,value=900 | updated | test_admin_api_phase2_part_5.py |
| TC-ADM-8162 | P2 | Settings endpoint RATE_LIMIT_PERIOD = 1800 | key=RATE_LIMIT_PERIOD,value=1800 | updated | test_admin_api_phase2_part_5.py |
| TC-ADM-8163 | P2 | Settings endpoint RATE_LIMIT_PERIOD = 3600 | key=RATE_LIMIT_PERIOD,value=3600 | updated | test_admin_api_phase2_part_5.py |
| TC-ADM-8164 | P2 | Settings endpoint RATE_LIMIT_PERIOD = 7200 | key=RATE_LIMIT_PERIOD,value=7200 | updated | test_admin_api_phase2_part_5.py |
| TC-ADM-8165 | P2 | Settings endpoint RATE_LIMIT_PERIOD = 10800 | key=RATE_LIMIT_PERIOD,value=10800 | updated | test_admin_api_phase2_part_5.py |
| TC-ADM-8166 | P2 | Settings endpoint RATE_LIMIT_PERIOD = 14400 | key=RATE_LIMIT_PERIOD,value=14400 | updated | test_admin_api_phase2_part_5.py |
| TC-ADM-8167 | P2 | Settings endpoint RATE_LIMIT_PERIOD = 21600 | key=RATE_LIMIT_PERIOD,value=21600 | updated | test_admin_api_phase2_part_5.py |
| TC-ADM-8168 | P2 | Settings endpoint RATE_LIMIT_PERIOD = 28800 | key=RATE_LIMIT_PERIOD,value=28800 | updated | test_admin_api_phase2_part_5.py |
| TC-ADM-8169 | P2 | Settings endpoint RATE_LIMIT_PERIOD = 43200 | key=RATE_LIMIT_PERIOD,value=43200 | updated | test_admin_api_phase2_part_5.py |
| TC-ADM-8170 | P2 | Settings endpoint RATE_LIMIT_PERIOD = 57600 | key=RATE_LIMIT_PERIOD,value=57600 | updated | test_admin_api_phase2_part_5.py |
| TC-ADM-8171 | P2 | Settings endpoint RATE_LIMIT_PERIOD = 72000 | key=RATE_LIMIT_PERIOD,value=72000 | updated | test_admin_api_phase2_part_5.py |
| TC-ADM-8172 | P2 | Settings endpoint RATE_LIMIT_PERIOD = 86400 | key=RATE_LIMIT_PERIOD,value=86400 | updated | test_admin_api_phase2_part_5.py |
| TC-ADM-8173 | P2 | Logs traversal variant 0 | target=..%2F..%2Fetc%2Fpasswd.0 | list ok | test_admin_api_phase2_part_5.py |
| TC-ADM-8174 | P2 | Logs traversal variant 1 | target=..%2F..%2Fetc%2Fpasswd.1 | list ok | test_admin_api_phase2_part_5.py |
| TC-ADM-8175 | P2 | Logs traversal variant 2 | target=..%2F..%2Fetc%2Fpasswd.2 | list ok | test_admin_api_phase2_part_5.py |
| TC-ADM-8176 | P2 | Logs traversal variant 3 | target=..%2F..%2Fetc%2Fpasswd.3 | list ok | test_admin_api_phase2_part_5.py |
| TC-ADM-8177 | P2 | Logs traversal variant 4 | target=..%2F..%2Fetc%2Fpasswd.4 | list ok | test_admin_api_phase2_part_5.py |
| TC-ADM-8178 | P2 | Logs traversal variant 5 | target=..%2F..%2Fetc%2Fpasswd.5 | list ok | test_admin_api_phase2_part_5.py |
| TC-ADM-8179 | P2 | Logs traversal variant 6 | target=..%2F..%2Fetc%2Fpasswd.6 | list ok | test_admin_api_phase2_part_5.py |
| TC-ADM-8180 | P2 | Logs traversal variant 7 | target=..%2F..%2Fetc%2Fpasswd.7 | list ok | test_admin_api_phase2_part_5.py |
| TC-ADM-8181 | P2 | Logs traversal variant 8 | target=..%2F..%2Fetc%2Fpasswd.8 | list ok | test_admin_api_phase2_part_5.py |
| TC-ADM-8182 | P2 | Logs traversal variant 9 | target=..%2F..%2Fetc%2Fpasswd.9 | list ok | test_admin_api_phase2_part_5.py |
| TC-ADM-8183 | P2 | Logs traversal variant 10 | target=..%2F..%2Fetc%2Fpasswd.10 | list ok | test_admin_api_phase2_part_5.py |
| TC-ADM-8184 | P2 | Logs traversal variant 11 | target=..%2F..%2Fetc%2Fpasswd.11 | list ok | test_admin_api_phase2_part_5.py |
| TC-ADM-8185 | P2 | Logs traversal variant 12 | target=..%2F..%2Fetc%2Fpasswd.12 | list ok | test_admin_api_phase2_part_5.py |
| TC-ADM-8186 | P2 | Logs traversal variant 13 | target=..%2F..%2Fetc%2Fpasswd.13 | list ok | test_admin_api_phase2_part_5.py |
| TC-ADM-8187 | P2 | Logs traversal variant 14 | target=..%2F..%2Fetc%2Fpasswd.14 | list ok | test_admin_api_phase2_part_5.py |
| TC-ADM-8188 | P2 | Logs traversal variant 15 | target=..%2F..%2Fetc%2Fpasswd.15 | list ok | test_admin_api_phase2_part_5.py |
| TC-ADM-8189 | P2 | Logs traversal variant 16 | target=..%2F..%2Fetc%2Fpasswd.16 | list ok | test_admin_api_phase2_part_5.py |
| TC-ADM-8190 | P2 | Logs traversal variant 17 | target=..%2F..%2Fetc%2Fpasswd.17 | list ok | test_admin_api_phase2_part_5.py |
| TC-ADM-8191 | P2 | Logs traversal variant 18 | target=..%2F..%2Fetc%2Fpasswd.18 | list ok | test_admin_api_phase2_part_5.py |
| TC-ADM-8192 | P2 | Logs traversal variant 19 | target=..%2F..%2Fetc%2Fpasswd.19 | list ok | test_admin_api_phase2_part_5.py |
| TC-ADM-8193 | P2 | Logs traversal variant 20 | target=..%2F..%2Fetc%2Fpasswd.20 | list ok | test_admin_api_phase2_part_5.py |
| TC-ADM-8194 | P2 | Logs traversal variant 21 | target=..%2F..%2Fetc%2Fpasswd.21 | list ok | test_admin_api_phase2_part_5.py |
| TC-ADM-8195 | P2 | Logs traversal variant 22 | target=..%2F..%2Fetc%2Fpasswd.22 | list ok | test_admin_api_phase2_part_5.py |
| TC-ADM-8196 | P2 | Logs traversal variant 23 | target=..%2F..%2Fetc%2Fpasswd.23 | list ok | test_admin_api_phase2_part_5.py |
| TC-ADM-8197 | P2 | Logs traversal variant 24 | target=..%2F..%2Fetc%2Fpasswd.24 | list ok | test_admin_api_phase2_part_5.py |
| TC-ADM-8198 | P2 | Logs traversal variant 25 | target=..%2F..%2Fetc%2Fpasswd.25 | list ok | test_admin_api_phase2_part_5.py |
| TC-ADM-8199 | P2 | Logs traversal variant 26 | target=..%2F..%2Fetc%2Fpasswd.26 | list ok | test_admin_api_phase2_part_5.py |
| TC-ADM-8200 | P2 | Logs traversal variant 27 | target=..%2F..%2Fetc%2Fpasswd.27 | list ok | test_admin_api_phase2_part_5.py |
| TC-ADM-8201 | P2 | Logs traversal variant 28 | target=..%2F..%2Fetc%2Fpasswd.28 | list ok | test_admin_api_phase2_part_5.py |
| TC-ADM-8202 | P2 | Logs traversal variant 29 | target=..%2F..%2Fetc%2Fpasswd.29 | list ok | test_admin_api_phase2_part_5.py |
| TC-ADM-8203 | P2 | Logs traversal variant 30 | target=..%2F..%2Fetc%2Fpasswd.30 | list ok | test_admin_api_phase2_part_5.py |
| TC-ADM-8204 | P2 | Logs traversal variant 31 | target=..%2F..%2Fetc%2Fpasswd.31 | list ok | test_admin_api_phase2_part_5.py |
| TC-ADM-8205 | P2 | Logs traversal variant 32 | target=..%2F..%2Fetc%2Fpasswd.32 | list ok | test_admin_api_phase2_part_5.py |
| TC-ADM-8206 | P2 | Logs traversal variant 33 | target=..%2F..%2Fetc%2Fpasswd.33 | list ok | test_admin_api_phase2_part_5.py |
| TC-ADM-8207 | P2 | Logs traversal variant 34 | target=..%2F..%2Fetc%2Fpasswd.34 | list ok | test_admin_api_phase2_part_5.py |
| TC-ADM-8208 | P2 | Logs traversal variant 35 | target=..%2F..%2Fetc%2Fpasswd.35 | list ok | test_admin_api_phase2_part_5.py |
| TC-ADM-8209 | P2 | Logs traversal variant 36 | target=..%2F..%2Fetc%2Fpasswd.36 | list ok | test_admin_api_phase2_part_5.py |
| TC-ADM-8210 | P2 | Logs traversal variant 37 | target=..%2F..%2Fetc%2Fpasswd.37 | list ok | test_admin_api_phase2_part_5.py |
| TC-ADM-8211 | P2 | Logs traversal variant 38 | target=..%2F..%2Fetc%2Fpasswd.38 | list ok | test_admin_api_phase2_part_5.py |
| TC-ADM-8212 | P2 | Logs traversal variant 39 | target=..%2F..%2Fetc%2Fpasswd.39 | list ok | test_admin_api_phase2_part_5.py |
| TC-ADM-8213 | P2 | Logs traversal variant 40 | target=..%2F..%2Fetc%2Fpasswd.40 | list ok | test_admin_api_phase2_part_5.py |
| TC-ADM-8214 | P2 | Logs traversal variant 41 | target=..%2F..%2Fetc%2Fpasswd.41 | list ok | test_admin_api_phase2_part_5.py |
| TC-ADM-8215 | P2 | Logs traversal variant 42 | target=..%2F..%2Fetc%2Fpasswd.42 | list ok | test_admin_api_phase2_part_5.py |
| TC-ADM-8216 | P2 | Logs traversal variant 43 | target=..%2F..%2Fetc%2Fpasswd.43 | list ok | test_admin_api_phase2_part_5.py |
| TC-ADM-8217 | P2 | Logs traversal variant 44 | target=..%2F..%2Fetc%2Fpasswd.44 | list ok | test_admin_api_phase2_part_5.py |
| TC-ADM-8218 | P2 | Logs traversal variant 45 | target=..%2F..%2Fetc%2Fpasswd.45 | list ok | test_admin_api_phase2_part_5.py |
| TC-ADM-8219 | P2 | Logs traversal variant 46 | target=..%2F..%2Fetc%2Fpasswd.46 | list ok | test_admin_api_phase2_part_5.py |
| TC-ADM-8220 | P2 | Logs traversal variant 47 | target=..%2F..%2Fetc%2Fpasswd.47 | list ok | test_admin_api_phase2_part_5.py |
| TC-ADM-8221 | P2 | Logs traversal variant 48 | target=..%2F..%2Fetc%2Fpasswd.48 | list ok | test_admin_api_phase2_part_5.py |
| TC-ADM-8222 | P2 | Logs traversal variant 49 | target=..%2F..%2Fetc%2Fpasswd.49 | list ok | test_admin_api_phase2_part_5.py |
| TC-ADM-8223 | P2 | Stats after 1 moderations | n=1 | stats valid | test_admin_api_phase2_part_6.py |
| TC-ADM-8224 | P2 | Stats after 2 moderations | n=2 | stats valid | test_admin_api_phase2_part_6.py |
| TC-ADM-8225 | P2 | Stats after 3 moderations | n=3 | stats valid | test_admin_api_phase2_part_6.py |
| TC-ADM-8226 | P2 | Stats after 4 moderations | n=4 | stats valid | test_admin_api_phase2_part_6.py |
| TC-ADM-8227 | P2 | Stats after 5 moderations | n=5 | stats valid | test_admin_api_phase2_part_6.py |
| TC-ADM-8228 | P2 | Stats after 6 moderations | n=6 | stats valid | test_admin_api_phase2_part_6.py |
| TC-ADM-8229 | P2 | Stats after 7 moderations | n=7 | stats valid | test_admin_api_phase2_part_6.py |
| TC-ADM-8230 | P2 | Stats after 8 moderations | n=8 | stats valid | test_admin_api_phase2_part_6.py |
| TC-ADM-8231 | P2 | Stats after 9 moderations | n=9 | stats valid | test_admin_api_phase2_part_6.py |
| TC-ADM-8232 | P2 | Stats after 10 moderations | n=10 | stats valid | test_admin_api_phase2_part_6.py |
| TC-ADM-8233 | P2 | Stats after 11 moderations | n=11 | stats valid | test_admin_api_phase2_part_6.py |
| TC-ADM-8234 | P2 | Stats after 12 moderations | n=12 | stats valid | test_admin_api_phase2_part_6.py |
| TC-ADM-8235 | P2 | Stats after 13 moderations | n=13 | stats valid | test_admin_api_phase2_part_6.py |
| TC-ADM-8236 | P2 | Stats after 14 moderations | n=14 | stats valid | test_admin_api_phase2_part_6.py |
| TC-ADM-8237 | P2 | Stats after 15 moderations | n=15 | stats valid | test_admin_api_phase2_part_6.py |
| TC-ADM-8238 | P2 | Stats after 16 moderations | n=16 | stats valid | test_admin_api_phase2_part_6.py |
| TC-ADM-8239 | P2 | Stats after 17 moderations | n=17 | stats valid | test_admin_api_phase2_part_6.py |
| TC-ADM-8240 | P2 | Stats after 18 moderations | n=18 | stats valid | test_admin_api_phase2_part_6.py |
| TC-ADM-8241 | P2 | Stats after 19 moderations | n=19 | stats valid | test_admin_api_phase2_part_6.py |
| TC-ADM-8242 | P2 | Stats after 20 moderations | n=20 | stats valid | test_admin_api_phase2_part_6.py |
| TC-ADM-8243 | P2 | Stats after 21 moderations | n=21 | stats valid | test_admin_api_phase2_part_6.py |
| TC-ADM-8244 | P2 | Stats after 22 moderations | n=22 | stats valid | test_admin_api_phase2_part_6.py |
| TC-ADM-8245 | P2 | Stats after 23 moderations | n=23 | stats valid | test_admin_api_phase2_part_6.py |
| TC-ADM-8246 | P2 | Stats after 24 moderations | n=24 | stats valid | test_admin_api_phase2_part_6.py |
| TC-ADM-8247 | P2 | Stats after 25 moderations | n=25 | stats valid | test_admin_api_phase2_part_6.py |
| TC-ADM-8248 | P2 | Stats after 26 moderations | n=26 | stats valid | test_admin_api_phase2_part_6.py |
| TC-ADM-8249 | P2 | Stats after 27 moderations | n=27 | stats valid | test_admin_api_phase2_part_6.py |
| TC-ADM-8250 | P2 | Stats after 28 moderations | n=28 | stats valid | test_admin_api_phase2_part_6.py |
| TC-ADM-8251 | P2 | Stats after 29 moderations | n=29 | stats valid | test_admin_api_phase2_part_6.py |
| TC-ADM-8252 | P2 | Stats after 30 moderations | n=30 | stats valid | test_admin_api_phase2_part_6.py |
| TC-ADM-8253 | P2 | Stats after 31 moderations | n=31 | stats valid | test_admin_api_phase2_part_6.py |
| TC-ADM-8254 | P2 | Stats after 32 moderations | n=32 | stats valid | test_admin_api_phase2_part_6.py |
| TC-ADM-8255 | P2 | Stats after 33 moderations | n=33 | stats valid | test_admin_api_phase2_part_6.py |
| TC-ADM-8256 | P2 | Stats after 34 moderations | n=34 | stats valid | test_admin_api_phase2_part_6.py |
| TC-ADM-8257 | P2 | Stats after 35 moderations | n=35 | stats valid | test_admin_api_phase2_part_6.py |
| TC-ADM-8258 | P2 | Stats after 36 moderations | n=36 | stats valid | test_admin_api_phase2_part_6.py |
| TC-ADM-8259 | P2 | Stats after 37 moderations | n=37 | stats valid | test_admin_api_phase2_part_6.py |
| TC-ADM-8260 | P2 | Stats after 38 moderations | n=38 | stats valid | test_admin_api_phase2_part_6.py |
| TC-ADM-8261 | P2 | Stats after 39 moderations | n=39 | stats valid | test_admin_api_phase2_part_6.py |
| TC-ADM-8262 | P2 | Stats after 40 moderations | n=40 | stats valid | test_admin_api_phase2_part_6.py |
| TC-ADM-8263 | P2 | Stats after 41 moderations | n=41 | stats valid | test_admin_api_phase2_part_6.py |
| TC-ADM-8264 | P2 | Stats after 42 moderations | n=42 | stats valid | test_admin_api_phase2_part_6.py |
| TC-ADM-8265 | P2 | Stats after 43 moderations | n=43 | stats valid | test_admin_api_phase2_part_6.py |
| TC-ADM-8266 | P2 | Stats after 44 moderations | n=44 | stats valid | test_admin_api_phase2_part_6.py |
| TC-ADM-8267 | P2 | Stats after 45 moderations | n=45 | stats valid | test_admin_api_phase2_part_6.py |
| TC-ADM-8268 | P2 | Stats after 46 moderations | n=46 | stats valid | test_admin_api_phase2_part_6.py |
| TC-ADM-8269 | P2 | Stats after 47 moderations | n=47 | stats valid | test_admin_api_phase2_part_6.py |
| TC-ADM-8270 | P2 | Stats after 48 moderations | n=48 | stats valid | test_admin_api_phase2_part_6.py |
| TC-ADM-8271 | P2 | Stats after 49 moderations | n=49 | stats valid | test_admin_api_phase2_part_6.py |
| TC-ADM-8272 | P2 | Stats after 50 moderations | n=50 | stats valid | test_admin_api_phase2_part_6.py |
| TC-ADM-8273 | P2 | Stats after 51 moderations | n=51 | stats valid | test_admin_api_phase2_part_6.py |
| TC-ADM-8274 | P2 | Stats after 52 moderations | n=52 | stats valid | test_admin_api_phase2_part_6.py |
| TC-ADM-8275 | P2 | Stats after 53 moderations | n=53 | stats valid | test_admin_api_phase2_part_6.py |
| TC-ADM-8276 | P2 | Stats after 54 moderations | n=54 | stats valid | test_admin_api_phase2_part_6.py |
| TC-ADM-8277 | P2 | Stats after 55 moderations | n=55 | stats valid | test_admin_api_phase2_part_6.py |
| TC-ADM-8278 | P2 | Stats after 56 moderations | n=56 | stats valid | test_admin_api_phase2_part_6.py |
| TC-ADM-8279 | P2 | Stats after 57 moderations | n=57 | stats valid | test_admin_api_phase2_part_6.py |
| TC-ADM-8280 | P2 | Stats after 58 moderations | n=58 | stats valid | test_admin_api_phase2_part_6.py |
| TC-ADM-8281 | P2 | Stats after 59 moderations | n=59 | stats valid | test_admin_api_phase2_part_6.py |
| TC-ADM-8282 | P2 | Stats after 60 moderations | n=60 | stats valid | test_admin_api_phase2_part_6.py |
| TC-ADM-8283 | P2 | Stats after 61 moderations | n=61 | stats valid | test_admin_api_phase2_part_6.py |
| TC-ADM-8284 | P2 | Stats after 62 moderations | n=62 | stats valid | test_admin_api_phase2_part_6.py |
| TC-ADM-8285 | P2 | Stats after 63 moderations | n=63 | stats valid | test_admin_api_phase2_part_6.py |
| TC-ADM-8286 | P2 | Stats after 64 moderations | n=64 | stats valid | test_admin_api_phase2_part_6.py |
| TC-ADM-8287 | P2 | Stats after 65 moderations | n=65 | stats valid | test_admin_api_phase2_part_6.py |
| TC-ADM-8288 | P2 | Stats after 66 moderations | n=66 | stats valid | test_admin_api_phase2_part_6.py |
| TC-ADM-8289 | P2 | Stats after 67 moderations | n=67 | stats valid | test_admin_api_phase2_part_6.py |
| TC-ADM-8290 | P2 | Stats after 68 moderations | n=68 | stats valid | test_admin_api_phase2_part_6.py |
| TC-ADM-8291 | P2 | Stats after 69 moderations | n=69 | stats valid | test_admin_api_phase2_part_6.py |
| TC-ADM-8292 | P2 | Stats after 70 moderations | n=70 | stats valid | test_admin_api_phase2_part_6.py |
| TC-ADM-8293 | P2 | Stats after 71 moderations | n=71 | stats valid | test_admin_api_phase2_part_6.py |
| TC-ADM-8294 | P2 | Stats after 72 moderations | n=72 | stats valid | test_admin_api_phase2_part_6.py |
| TC-ADM-8295 | P2 | Stats after 73 moderations | n=73 | stats valid | test_admin_api_phase2_part_6.py |
| TC-ADM-8296 | P2 | Stats after 74 moderations | n=74 | stats valid | test_admin_api_phase2_part_6.py |
| TC-ADM-8297 | P2 | Stats after 75 moderations | n=75 | stats valid | test_admin_api_phase2_part_6.py |
| TC-ADM-8298 | P2 | Stats after 76 moderations | n=76 | stats valid | test_admin_api_phase2_part_6.py |
| TC-ADM-8299 | P2 | Stats after 77 moderations | n=77 | stats valid | test_admin_api_phase2_part_6.py |
| TC-ADM-8300 | P2 | Stats after 78 moderations | n=78 | stats valid | test_admin_api_phase2_part_6.py |
| TC-ADM-8301 | P2 | Stats after 79 moderations | n=79 | stats valid | test_admin_api_phase2_part_6.py |
| TC-ADM-8302 | P2 | Stats after 80 moderations | n=80 | stats valid | test_admin_api_phase2_part_6.py |
| TC-ADM-8303 | P2 | Stats after 81 moderations | n=81 | stats valid | test_admin_api_phase2_part_6.py |
| TC-ADM-8304 | P2 | Stats after 82 moderations | n=82 | stats valid | test_admin_api_phase2_part_6.py |
| TC-ADM-8305 | P2 | Stats after 83 moderations | n=83 | stats valid | test_admin_api_phase2_part_6.py |
| TC-ADM-8306 | P2 | Stats after 84 moderations | n=84 | stats valid | test_admin_api_phase2_part_6.py |
| TC-ADM-8307 | P2 | Stats after 85 moderations | n=85 | stats valid | test_admin_api_phase2_part_6.py |
| TC-ADM-8308 | P2 | Stats after 86 moderations | n=86 | stats valid | test_admin_api_phase2_part_6.py |
| TC-ADM-8309 | P2 | Stats after 87 moderations | n=87 | stats valid | test_admin_api_phase2_part_6.py |
| TC-ADM-8310 | P2 | Stats after 88 moderations | n=88 | stats valid | test_admin_api_phase2_part_6.py |
| TC-ADM-8311 | P2 | Stats after 89 moderations | n=89 | stats valid | test_admin_api_phase2_part_6.py |
| TC-ADM-8312 | P2 | Stats after 90 moderations | n=90 | stats valid | test_admin_api_phase2_part_6.py |
| TC-ADM-8313 | P2 | Stats after 91 moderations | n=91 | stats valid | test_admin_api_phase2_part_6.py |
| TC-ADM-8314 | P2 | Stats after 92 moderations | n=92 | stats valid | test_admin_api_phase2_part_6.py |
| TC-ADM-8315 | P2 | Stats after 93 moderations | n=93 | stats valid | test_admin_api_phase2_part_6.py |
| TC-ADM-8316 | P2 | Stats after 94 moderations | n=94 | stats valid | test_admin_api_phase2_part_6.py |
| TC-ADM-8317 | P2 | Stats after 95 moderations | n=95 | stats valid | test_admin_api_phase2_part_6.py |
| TC-ADM-8318 | P2 | Stats after 96 moderations | n=96 | stats valid | test_admin_api_phase2_part_6.py |
| TC-ADM-8319 | P2 | Stats after 97 moderations | n=97 | stats valid | test_admin_api_phase2_part_6.py |
| TC-ADM-8320 | P2 | Stats after 98 moderations | n=98 | stats valid | test_admin_api_phase2_part_6.py |
| TC-ADM-8321 | P2 | Stats after 99 moderations | n=99 | stats valid | test_admin_api_phase2_part_6.py |
| TC-ADM-8322 | P2 | Stats after 100 moderations | n=100 | stats valid | test_admin_api_phase2_part_6.py |

### Phase 3 - 10,000 cases
- Planned sweeps over the full dimension matrix, IDs TC-ADM-0651 onward.

### Phase 4 - 100,000 cases
- Planned high-scale scenarios, IDs TC-ADM-10651 onward.

### Phase 5 - 939,350 cases
- Planned exhaustive dimension sweep, IDs TC-ADM-110651 onward.

## Implementation Status
| File | Test Cases | Priority | Status |
| :--- | :--- | :--- | :--- |
| test_admin_api_phase2_part_1.py | 7628-7727 | P1 | :white_check_mark: Phase 2 |
| test_admin_api_phase2_part_2.py | 7728-7917 | P1 | :white_check_mark: Phase 2 |
| test_admin_api_phase2_part_3.py | 7918-8022 | P1 | :white_check_mark: Phase 2 |
| test_admin_api_phase2_part_4.py | 8023-8122 | P1 | :white_check_mark: Phase 2 |
| test_admin_api_phase2_part_5.py | 8123-8222 | P2 | :white_check_mark: Phase 2 |
| test_admin_api_phase2_part_6.py | 8223-8322 | P2 | :white_check_mark: Phase 2 |

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
