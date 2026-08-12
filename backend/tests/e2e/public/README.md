# Public API Test Documentation

## Overview
- **Total Planned:** 2,100,000
- **Phase 1:** 80 (IDs TC-PUB-001 to TC-PUB-0080) :white_check_mark: Implemented
- **Phase 2:** 700 (IDs TC-PUB-0081 to TC-PUB-0780) :white_check_mark: Implemented
- **Phase 3:** 20,000 (IDs TC-PUB-0781 to TC-PUB-20780) :hourglass: Planned
- **Phase 4:** 200,000 (IDs TC-PUB-20781 to TC-PUB-220780) :hourglass: Planned
- **Phase 5:** 1,879,220 (IDs TC-PUB-220781 to TC-PUB-2100000) :hourglass: Planned

## Dimension Matrix
| Dimension | Values (Phase 2) |
| :--- | :--- |
| Endpoint | /moderate, /moderate/batch, /health |
| Verdict | PASS, BLOCK, REVIEW |
| Text length | 1-8192 |
| Unicode | ascii, CJK, Arabic, emoji |
| Batch size | 1-100 |
| User/app | 0-100 |

## Test Case List

### Phase 1 - 80 cases
- 80 cases (moderate, batch, health).

### Phase 2 (Current) - 700 cases
| ID | Priority | Description | Dimensions | Expected Outcome | File |
| :--- | :--- | :--- | :--- | :--- | :--- |
| TC-PUB-6689 | P1 | Moderate en clean at 5 | lang=en,len=5 | verdict=PASS | test_public_api_phase2_part_1.py |
| TC-PUB-6690 | P1 | Moderate en clean at 25 | lang=en,len=25 | verdict=PASS | test_public_api_phase2_part_1.py |
| TC-PUB-6691 | P1 | Moderate en clean at 100 | lang=en,len=100 | verdict=PASS | test_public_api_phase2_part_1.py |
| TC-PUB-6692 | P1 | Moderate en clean at 250 | lang=en,len=250 | verdict=PASS | test_public_api_phase2_part_1.py |
| TC-PUB-6693 | P1 | Moderate en clean at 500 | lang=en,len=500 | verdict=PASS | test_public_api_phase2_part_1.py |
| TC-PUB-6694 | P1 | Moderate en clean at 1000 | lang=en,len=1000 | verdict=PASS | test_public_api_phase2_part_1.py |
| TC-PUB-6695 | P1 | Moderate en clean at 2000 | lang=en,len=2000 | verdict=PASS | test_public_api_phase2_part_1.py |
| TC-PUB-6696 | P1 | Moderate en flagged | lang=en | verdict=BLOCK | test_public_api_phase2_part_1.py |
| TC-PUB-6697 | P1 | Moderate zh-CN clean at 5 | lang=zh-CN,len=5 | verdict=PASS | test_public_api_phase2_part_1.py |
| TC-PUB-6698 | P1 | Moderate zh-CN clean at 25 | lang=zh-CN,len=25 | verdict=PASS | test_public_api_phase2_part_1.py |
| TC-PUB-6699 | P1 | Moderate zh-CN clean at 100 | lang=zh-CN,len=100 | verdict=PASS | test_public_api_phase2_part_1.py |
| TC-PUB-6700 | P1 | Moderate zh-CN clean at 250 | lang=zh-CN,len=250 | verdict=PASS | test_public_api_phase2_part_1.py |
| TC-PUB-6701 | P1 | Moderate zh-CN clean at 500 | lang=zh-CN,len=500 | verdict=PASS | test_public_api_phase2_part_1.py |
| TC-PUB-6702 | P1 | Moderate zh-CN clean at 1000 | lang=zh-CN,len=1000 | verdict=PASS | test_public_api_phase2_part_1.py |
| TC-PUB-6703 | P1 | Moderate zh-CN clean at 2000 | lang=zh-CN,len=2000 | verdict=PASS | test_public_api_phase2_part_1.py |
| TC-PUB-6704 | P1 | Moderate zh-CN flagged | lang=zh-CN | verdict=BLOCK | test_public_api_phase2_part_1.py |
| TC-PUB-6705 | P1 | Moderate ja clean at 5 | lang=ja,len=5 | verdict=PASS | test_public_api_phase2_part_1.py |
| TC-PUB-6706 | P1 | Moderate ja clean at 25 | lang=ja,len=25 | verdict=PASS | test_public_api_phase2_part_1.py |
| TC-PUB-6707 | P1 | Moderate ja clean at 100 | lang=ja,len=100 | verdict=PASS | test_public_api_phase2_part_1.py |
| TC-PUB-6708 | P1 | Moderate ja clean at 250 | lang=ja,len=250 | verdict=PASS | test_public_api_phase2_part_1.py |
| TC-PUB-6709 | P1 | Moderate ja clean at 500 | lang=ja,len=500 | verdict=PASS | test_public_api_phase2_part_1.py |
| TC-PUB-6710 | P1 | Moderate ja clean at 1000 | lang=ja,len=1000 | verdict=PASS | test_public_api_phase2_part_1.py |
| TC-PUB-6711 | P1 | Moderate ja clean at 2000 | lang=ja,len=2000 | verdict=PASS | test_public_api_phase2_part_1.py |
| TC-PUB-6712 | P1 | Moderate ja flagged | lang=ja | verdict=BLOCK | test_public_api_phase2_part_1.py |
| TC-PUB-6713 | P1 | Moderate ko clean at 5 | lang=ko,len=5 | verdict=PASS | test_public_api_phase2_part_1.py |
| TC-PUB-6714 | P1 | Moderate ko clean at 25 | lang=ko,len=25 | verdict=PASS | test_public_api_phase2_part_1.py |
| TC-PUB-6715 | P1 | Moderate ko clean at 100 | lang=ko,len=100 | verdict=PASS | test_public_api_phase2_part_1.py |
| TC-PUB-6716 | P1 | Moderate ko clean at 250 | lang=ko,len=250 | verdict=PASS | test_public_api_phase2_part_1.py |
| TC-PUB-6717 | P1 | Moderate ko clean at 500 | lang=ko,len=500 | verdict=PASS | test_public_api_phase2_part_1.py |
| TC-PUB-6718 | P1 | Moderate ko clean at 1000 | lang=ko,len=1000 | verdict=PASS | test_public_api_phase2_part_1.py |
| TC-PUB-6719 | P1 | Moderate ko clean at 2000 | lang=ko,len=2000 | verdict=PASS | test_public_api_phase2_part_1.py |
| TC-PUB-6720 | P1 | Moderate ko flagged | lang=ko | verdict=BLOCK | test_public_api_phase2_part_1.py |
| TC-PUB-6721 | P1 | Moderate ru clean at 5 | lang=ru,len=5 | verdict=PASS | test_public_api_phase2_part_1.py |
| TC-PUB-6722 | P1 | Moderate ru clean at 25 | lang=ru,len=25 | verdict=PASS | test_public_api_phase2_part_1.py |
| TC-PUB-6723 | P1 | Moderate ru clean at 100 | lang=ru,len=100 | verdict=PASS | test_public_api_phase2_part_1.py |
| TC-PUB-6724 | P1 | Moderate ru clean at 250 | lang=ru,len=250 | verdict=PASS | test_public_api_phase2_part_1.py |
| TC-PUB-6725 | P1 | Moderate ru clean at 500 | lang=ru,len=500 | verdict=PASS | test_public_api_phase2_part_1.py |
| TC-PUB-6726 | P1 | Moderate ru clean at 1000 | lang=ru,len=1000 | verdict=PASS | test_public_api_phase2_part_1.py |
| TC-PUB-6727 | P1 | Moderate ru clean at 2000 | lang=ru,len=2000 | verdict=PASS | test_public_api_phase2_part_1.py |
| TC-PUB-6728 | P1 | Moderate ru flagged | lang=ru | verdict=BLOCK | test_public_api_phase2_part_1.py |
| TC-PUB-6729 | P1 | Moderate es clean at 5 | lang=es,len=5 | verdict=PASS | test_public_api_phase2_part_1.py |
| TC-PUB-6730 | P1 | Moderate es clean at 25 | lang=es,len=25 | verdict=PASS | test_public_api_phase2_part_1.py |
| TC-PUB-6731 | P1 | Moderate es clean at 100 | lang=es,len=100 | verdict=PASS | test_public_api_phase2_part_1.py |
| TC-PUB-6732 | P1 | Moderate es clean at 250 | lang=es,len=250 | verdict=PASS | test_public_api_phase2_part_1.py |
| TC-PUB-6733 | P1 | Moderate es clean at 500 | lang=es,len=500 | verdict=PASS | test_public_api_phase2_part_1.py |
| TC-PUB-6734 | P1 | Moderate es clean at 1000 | lang=es,len=1000 | verdict=PASS | test_public_api_phase2_part_1.py |
| TC-PUB-6735 | P1 | Moderate es clean at 2000 | lang=es,len=2000 | verdict=PASS | test_public_api_phase2_part_1.py |
| TC-PUB-6736 | P1 | Moderate es flagged | lang=es | verdict=BLOCK | test_public_api_phase2_part_1.py |
| TC-PUB-6737 | P1 | Moderate fr clean at 5 | lang=fr,len=5 | verdict=PASS | test_public_api_phase2_part_1.py |
| TC-PUB-6738 | P1 | Moderate fr clean at 25 | lang=fr,len=25 | verdict=PASS | test_public_api_phase2_part_1.py |
| TC-PUB-6739 | P1 | Moderate fr clean at 100 | lang=fr,len=100 | verdict=BLOCK | test_public_api_phase2_part_1.py |
| TC-PUB-6740 | P1 | Moderate fr clean at 250 | lang=fr,len=250 | verdict=BLOCK | test_public_api_phase2_part_1.py |
| TC-PUB-6741 | P1 | Moderate fr clean at 500 | lang=fr,len=500 | verdict=BLOCK | test_public_api_phase2_part_1.py |
| TC-PUB-6742 | P1 | Moderate fr clean at 1000 | lang=fr,len=1000 | verdict=BLOCK | test_public_api_phase2_part_1.py |
| TC-PUB-6743 | P1 | Moderate fr clean at 2000 | lang=fr,len=2000 | verdict=BLOCK | test_public_api_phase2_part_1.py |
| TC-PUB-6744 | P1 | Moderate fr flagged | lang=fr | verdict=BLOCK | test_public_api_phase2_part_1.py |
| TC-PUB-6745 | P1 | Moderate de clean at 5 | lang=de,len=5 | verdict=PASS | test_public_api_phase2_part_1.py |
| TC-PUB-6746 | P1 | Moderate de clean at 25 | lang=de,len=25 | verdict=PASS | test_public_api_phase2_part_1.py |
| TC-PUB-6747 | P1 | Moderate de clean at 100 | lang=de,len=100 | verdict=PASS | test_public_api_phase2_part_1.py |
| TC-PUB-6748 | P1 | Moderate de clean at 250 | lang=de,len=250 | verdict=PASS | test_public_api_phase2_part_1.py |
| TC-PUB-6749 | P1 | Moderate de clean at 500 | lang=de,len=500 | verdict=PASS | test_public_api_phase2_part_1.py |
| TC-PUB-6750 | P1 | Moderate de clean at 1000 | lang=de,len=1000 | verdict=PASS | test_public_api_phase2_part_1.py |
| TC-PUB-6751 | P1 | Moderate de clean at 2000 | lang=de,len=2000 | verdict=PASS | test_public_api_phase2_part_1.py |
| TC-PUB-6752 | P1 | Moderate de flagged | lang=de | verdict=BLOCK | test_public_api_phase2_part_1.py |
| TC-PUB-6753 | P1 | Moderate it clean at 5 | lang=it,len=5 | verdict=PASS | test_public_api_phase2_part_1.py |
| TC-PUB-6754 | P1 | Moderate it clean at 25 | lang=it,len=25 | verdict=PASS | test_public_api_phase2_part_1.py |
| TC-PUB-6755 | P1 | Moderate it clean at 100 | lang=it,len=100 | verdict=PASS | test_public_api_phase2_part_1.py |
| TC-PUB-6756 | P1 | Moderate it clean at 250 | lang=it,len=250 | verdict=PASS | test_public_api_phase2_part_1.py |
| TC-PUB-6757 | P1 | Moderate it clean at 500 | lang=it,len=500 | verdict=PASS | test_public_api_phase2_part_1.py |
| TC-PUB-6758 | P1 | Moderate it clean at 1000 | lang=it,len=1000 | verdict=PASS | test_public_api_phase2_part_1.py |
| TC-PUB-6759 | P1 | Moderate it clean at 2000 | lang=it,len=2000 | verdict=PASS | test_public_api_phase2_part_1.py |
| TC-PUB-6760 | P1 | Moderate it flagged | lang=it | verdict=BLOCK | test_public_api_phase2_part_1.py |
| TC-PUB-6761 | P1 | Moderate ar clean at 5 | lang=ar,len=5 | verdict=PASS | test_public_api_phase2_part_1.py |
| TC-PUB-6762 | P1 | Moderate ar clean at 25 | lang=ar,len=25 | verdict=PASS | test_public_api_phase2_part_1.py |
| TC-PUB-6763 | P1 | Moderate ar clean at 100 | lang=ar,len=100 | verdict=PASS | test_public_api_phase2_part_1.py |
| TC-PUB-6764 | P1 | Moderate ar clean at 250 | lang=ar,len=250 | verdict=PASS | test_public_api_phase2_part_1.py |
| TC-PUB-6765 | P1 | Moderate ar clean at 500 | lang=ar,len=500 | verdict=PASS | test_public_api_phase2_part_1.py |
| TC-PUB-6766 | P1 | Moderate ar clean at 1000 | lang=ar,len=1000 | verdict=PASS | test_public_api_phase2_part_1.py |
| TC-PUB-6767 | P1 | Moderate ar clean at 2000 | lang=ar,len=2000 | verdict=PASS | test_public_api_phase2_part_1.py |
| TC-PUB-6768 | P1 | Moderate ar flagged | lang=ar | verdict=PASS | test_public_api_phase2_part_1.py |
| TC-PUB-6769 | P1 | Moderate hi clean at 5 | lang=hi,len=5 | verdict=PASS | test_public_api_phase2_part_1.py |
| TC-PUB-6770 | P1 | Moderate hi clean at 25 | lang=hi,len=25 | verdict=PASS | test_public_api_phase2_part_1.py |
| TC-PUB-6771 | P1 | Moderate hi clean at 100 | lang=hi,len=100 | verdict=PASS | test_public_api_phase2_part_1.py |
| TC-PUB-6772 | P1 | Moderate hi clean at 250 | lang=hi,len=250 | verdict=PASS | test_public_api_phase2_part_1.py |
| TC-PUB-6773 | P1 | Moderate hi clean at 500 | lang=hi,len=500 | verdict=PASS | test_public_api_phase2_part_1.py |
| TC-PUB-6774 | P1 | Moderate hi clean at 1000 | lang=hi,len=1000 | verdict=PASS | test_public_api_phase2_part_1.py |
| TC-PUB-6775 | P1 | Moderate hi clean at 2000 | lang=hi,len=2000 | verdict=PASS | test_public_api_phase2_part_1.py |
| TC-PUB-6776 | P1 | Moderate hi flagged | lang=hi | verdict=BLOCK | test_public_api_phase2_part_1.py |
| TC-PUB-6777 | P1 | Moderate tr clean at 5 | lang=tr,len=5 | verdict=PASS | test_public_api_phase2_part_1.py |
| TC-PUB-6778 | P1 | Moderate tr clean at 25 | lang=tr,len=25 | verdict=PASS | test_public_api_phase2_part_1.py |
| TC-PUB-6779 | P1 | Moderate tr clean at 100 | lang=tr,len=100 | verdict=PASS | test_public_api_phase2_part_1.py |
| TC-PUB-6780 | P1 | Moderate tr clean at 250 | lang=tr,len=250 | verdict=PASS | test_public_api_phase2_part_1.py |
| TC-PUB-6781 | P1 | Moderate tr clean at 500 | lang=tr,len=500 | verdict=PASS | test_public_api_phase2_part_1.py |
| TC-PUB-6782 | P1 | Moderate tr clean at 1000 | lang=tr,len=1000 | verdict=PASS | test_public_api_phase2_part_1.py |
| TC-PUB-6783 | P1 | Moderate tr clean at 2000 | lang=tr,len=2000 | verdict=PASS | test_public_api_phase2_part_1.py |
| TC-PUB-6784 | P1 | Moderate tr flagged | lang=tr | verdict=BLOCK | test_public_api_phase2_part_1.py |
| TC-PUB-6785 | P1 | Moderate pt clean at 5 | lang=pt,len=5 | verdict=PASS | test_public_api_phase2_part_1.py |
| TC-PUB-6786 | P1 | Moderate pt clean at 25 | lang=pt,len=25 | verdict=PASS | test_public_api_phase2_part_1.py |
| TC-PUB-6787 | P1 | Moderate pt clean at 100 | lang=pt,len=100 | verdict=BLOCK | test_public_api_phase2_part_1.py |
| TC-PUB-6788 | P1 | Moderate pt clean at 250 | lang=pt,len=250 | verdict=BLOCK | test_public_api_phase2_part_1.py |
| TC-PUB-6789 | P1 | Moderate pt clean at 500 | lang=pt,len=500 | verdict=BLOCK | test_public_api_phase2_part_2.py |
| TC-PUB-6790 | P1 | Moderate pt clean at 1000 | lang=pt,len=1000 | verdict=BLOCK | test_public_api_phase2_part_2.py |
| TC-PUB-6791 | P1 | Moderate pt clean at 2000 | lang=pt,len=2000 | verdict=BLOCK | test_public_api_phase2_part_2.py |
| TC-PUB-6792 | P1 | Moderate pt flagged | lang=pt | verdict=BLOCK | test_public_api_phase2_part_2.py |
| TC-PUB-6793 | P1 | Moderate nl clean at 5 | lang=nl,len=5 | verdict=PASS | test_public_api_phase2_part_2.py |
| TC-PUB-6794 | P1 | Moderate nl clean at 25 | lang=nl,len=25 | verdict=PASS | test_public_api_phase2_part_2.py |
| TC-PUB-6795 | P1 | Moderate nl clean at 100 | lang=nl,len=100 | verdict=PASS | test_public_api_phase2_part_2.py |
| TC-PUB-6796 | P1 | Moderate nl clean at 250 | lang=nl,len=250 | verdict=PASS | test_public_api_phase2_part_2.py |
| TC-PUB-6797 | P1 | Moderate nl clean at 500 | lang=nl,len=500 | verdict=PASS | test_public_api_phase2_part_2.py |
| TC-PUB-6798 | P1 | Moderate nl clean at 1000 | lang=nl,len=1000 | verdict=PASS | test_public_api_phase2_part_2.py |
| TC-PUB-6799 | P1 | Moderate nl clean at 2000 | lang=nl,len=2000 | verdict=PASS | test_public_api_phase2_part_2.py |
| TC-PUB-6800 | P1 | Moderate nl flagged | lang=nl | verdict=BLOCK | test_public_api_phase2_part_2.py |
| TC-PUB-6801 | P1 | Moderate pl clean at 5 | lang=pl,len=5 | verdict=PASS | test_public_api_phase2_part_2.py |
| TC-PUB-6802 | P1 | Moderate pl clean at 25 | lang=pl,len=25 | verdict=PASS | test_public_api_phase2_part_2.py |
| TC-PUB-6803 | P1 | Moderate pl clean at 100 | lang=pl,len=100 | verdict=PASS | test_public_api_phase2_part_2.py |
| TC-PUB-6804 | P1 | Moderate pl clean at 250 | lang=pl,len=250 | verdict=PASS | test_public_api_phase2_part_2.py |
| TC-PUB-6805 | P1 | Moderate pl clean at 500 | lang=pl,len=500 | verdict=PASS | test_public_api_phase2_part_2.py |
| TC-PUB-6806 | P1 | Moderate pl clean at 1000 | lang=pl,len=1000 | verdict=PASS | test_public_api_phase2_part_2.py |
| TC-PUB-6807 | P1 | Moderate pl clean at 2000 | lang=pl,len=2000 | verdict=PASS | test_public_api_phase2_part_2.py |
| TC-PUB-6808 | P1 | Moderate pl flagged | lang=pl | verdict=BLOCK | test_public_api_phase2_part_2.py |
| TC-PUB-6809 | P1 | Moderate uk clean at 5 | lang=uk,len=5 | verdict=PASS | test_public_api_phase2_part_2.py |
| TC-PUB-6810 | P1 | Moderate uk clean at 25 | lang=uk,len=25 | verdict=PASS | test_public_api_phase2_part_2.py |
| TC-PUB-6811 | P1 | Moderate uk clean at 100 | lang=uk,len=100 | verdict=PASS | test_public_api_phase2_part_2.py |
| TC-PUB-6812 | P1 | Moderate uk clean at 250 | lang=uk,len=250 | verdict=PASS | test_public_api_phase2_part_2.py |
| TC-PUB-6813 | P1 | Moderate uk clean at 500 | lang=uk,len=500 | verdict=PASS | test_public_api_phase2_part_2.py |
| TC-PUB-6814 | P1 | Moderate uk clean at 1000 | lang=uk,len=1000 | verdict=PASS | test_public_api_phase2_part_2.py |
| TC-PUB-6815 | P1 | Moderate uk clean at 2000 | lang=uk,len=2000 | verdict=PASS | test_public_api_phase2_part_2.py |
| TC-PUB-6816 | P1 | Moderate uk flagged | lang=uk | verdict=PASS | test_public_api_phase2_part_2.py |
| TC-PUB-6817 | P1 | Moderate cs clean at 5 | lang=cs,len=5 | verdict=PASS | test_public_api_phase2_part_2.py |
| TC-PUB-6818 | P1 | Moderate cs clean at 25 | lang=cs,len=25 | verdict=PASS | test_public_api_phase2_part_2.py |
| TC-PUB-6819 | P1 | Moderate cs clean at 100 | lang=cs,len=100 | verdict=PASS | test_public_api_phase2_part_2.py |
| TC-PUB-6820 | P1 | Moderate cs clean at 250 | lang=cs,len=250 | verdict=PASS | test_public_api_phase2_part_2.py |
| TC-PUB-6821 | P1 | Moderate cs clean at 500 | lang=cs,len=500 | verdict=PASS | test_public_api_phase2_part_2.py |
| TC-PUB-6822 | P1 | Moderate cs clean at 1000 | lang=cs,len=1000 | verdict=PASS | test_public_api_phase2_part_2.py |
| TC-PUB-6823 | P1 | Moderate cs clean at 2000 | lang=cs,len=2000 | verdict=PASS | test_public_api_phase2_part_2.py |
| TC-PUB-6824 | P1 | Moderate cs flagged | lang=cs | verdict=BLOCK | test_public_api_phase2_part_2.py |
| TC-PUB-6825 | P1 | Moderate el clean at 5 | lang=el,len=5 | verdict=PASS | test_public_api_phase2_part_2.py |
| TC-PUB-6826 | P1 | Moderate el clean at 25 | lang=el,len=25 | verdict=PASS | test_public_api_phase2_part_2.py |
| TC-PUB-6827 | P1 | Moderate el clean at 100 | lang=el,len=100 | verdict=PASS | test_public_api_phase2_part_2.py |
| TC-PUB-6828 | P1 | Moderate el clean at 250 | lang=el,len=250 | verdict=PASS | test_public_api_phase2_part_2.py |
| TC-PUB-6829 | P1 | Moderate el clean at 500 | lang=el,len=500 | verdict=PASS | test_public_api_phase2_part_2.py |
| TC-PUB-6830 | P1 | Moderate el clean at 1000 | lang=el,len=1000 | verdict=PASS | test_public_api_phase2_part_2.py |
| TC-PUB-6831 | P1 | Moderate el clean at 2000 | lang=el,len=2000 | verdict=PASS | test_public_api_phase2_part_2.py |
| TC-PUB-6832 | P1 | Moderate el flagged | lang=el | verdict=BLOCK | test_public_api_phase2_part_2.py |
| TC-PUB-6833 | P1 | Moderate sv clean at 5 | lang=sv,len=5 | verdict=PASS | test_public_api_phase2_part_2.py |
| TC-PUB-6834 | P1 | Moderate sv clean at 25 | lang=sv,len=25 | verdict=PASS | test_public_api_phase2_part_2.py |
| TC-PUB-6835 | P1 | Moderate sv clean at 100 | lang=sv,len=100 | verdict=PASS | test_public_api_phase2_part_2.py |
| TC-PUB-6836 | P1 | Moderate sv clean at 250 | lang=sv,len=250 | verdict=PASS | test_public_api_phase2_part_2.py |
| TC-PUB-6837 | P1 | Moderate sv clean at 500 | lang=sv,len=500 | verdict=PASS | test_public_api_phase2_part_2.py |
| TC-PUB-6838 | P1 | Moderate sv clean at 1000 | lang=sv,len=1000 | verdict=PASS | test_public_api_phase2_part_2.py |
| TC-PUB-6839 | P1 | Moderate sv clean at 2000 | lang=sv,len=2000 | verdict=PASS | test_public_api_phase2_part_2.py |
| TC-PUB-6840 | P1 | Moderate sv flagged | lang=sv | verdict=BLOCK | test_public_api_phase2_part_2.py |
| TC-PUB-6841 | P1 | Moderate no clean at 5 | lang=no,len=5 | verdict=PASS | test_public_api_phase2_part_2.py |
| TC-PUB-6842 | P1 | Moderate no clean at 25 | lang=no,len=25 | verdict=PASS | test_public_api_phase2_part_2.py |
| TC-PUB-6843 | P1 | Moderate no clean at 100 | lang=no,len=100 | verdict=PASS | test_public_api_phase2_part_2.py |
| TC-PUB-6844 | P1 | Moderate no clean at 250 | lang=no,len=250 | verdict=PASS | test_public_api_phase2_part_2.py |
| TC-PUB-6845 | P1 | Moderate no clean at 500 | lang=no,len=500 | verdict=PASS | test_public_api_phase2_part_2.py |
| TC-PUB-6846 | P1 | Moderate no clean at 1000 | lang=no,len=1000 | verdict=PASS | test_public_api_phase2_part_2.py |
| TC-PUB-6847 | P1 | Moderate no clean at 2000 | lang=no,len=2000 | verdict=PASS | test_public_api_phase2_part_2.py |
| TC-PUB-6848 | P1 | Moderate no flagged | lang=no | verdict=BLOCK | test_public_api_phase2_part_2.py |
| TC-PUB-6849 | P1 | Moderate da clean at 5 | lang=da,len=5 | verdict=PASS | test_public_api_phase2_part_2.py |
| TC-PUB-6850 | P1 | Moderate da clean at 25 | lang=da,len=25 | verdict=PASS | test_public_api_phase2_part_2.py |
| TC-PUB-6851 | P1 | Moderate da clean at 100 | lang=da,len=100 | verdict=PASS | test_public_api_phase2_part_2.py |
| TC-PUB-6852 | P1 | Moderate da clean at 250 | lang=da,len=250 | verdict=PASS | test_public_api_phase2_part_2.py |
| TC-PUB-6853 | P1 | Moderate da clean at 500 | lang=da,len=500 | verdict=PASS | test_public_api_phase2_part_2.py |
| TC-PUB-6854 | P1 | Moderate da clean at 1000 | lang=da,len=1000 | verdict=PASS | test_public_api_phase2_part_2.py |
| TC-PUB-6855 | P1 | Moderate da clean at 2000 | lang=da,len=2000 | verdict=PASS | test_public_api_phase2_part_2.py |
| TC-PUB-6856 | P1 | Moderate da flagged | lang=da | verdict=PASS | test_public_api_phase2_part_2.py |
| TC-PUB-6857 | P1 | Moderate fi clean at 5 | lang=fi,len=5 | verdict=PASS | test_public_api_phase2_part_2.py |
| TC-PUB-6858 | P1 | Moderate fi clean at 25 | lang=fi,len=25 | verdict=PASS | test_public_api_phase2_part_2.py |
| TC-PUB-6859 | P1 | Moderate fi clean at 100 | lang=fi,len=100 | verdict=PASS | test_public_api_phase2_part_2.py |
| TC-PUB-6860 | P1 | Moderate fi clean at 250 | lang=fi,len=250 | verdict=PASS | test_public_api_phase2_part_2.py |
| TC-PUB-6861 | P1 | Moderate fi clean at 500 | lang=fi,len=500 | verdict=PASS | test_public_api_phase2_part_2.py |
| TC-PUB-6862 | P1 | Moderate fi clean at 1000 | lang=fi,len=1000 | verdict=PASS | test_public_api_phase2_part_2.py |
| TC-PUB-6863 | P1 | Moderate fi clean at 2000 | lang=fi,len=2000 | verdict=PASS | test_public_api_phase2_part_2.py |
| TC-PUB-6864 | P1 | Moderate fi flagged | lang=fi | verdict=BLOCK | test_public_api_phase2_part_2.py |
| TC-PUB-6865 | P1 | Moderate hu clean at 5 | lang=hu,len=5 | verdict=PASS | test_public_api_phase2_part_2.py |
| TC-PUB-6866 | P1 | Moderate hu clean at 25 | lang=hu,len=25 | verdict=PASS | test_public_api_phase2_part_2.py |
| TC-PUB-6867 | P1 | Moderate hu clean at 100 | lang=hu,len=100 | verdict=PASS | test_public_api_phase2_part_2.py |
| TC-PUB-6868 | P1 | Moderate hu clean at 250 | lang=hu,len=250 | verdict=PASS | test_public_api_phase2_part_2.py |
| TC-PUB-6869 | P1 | Moderate hu clean at 500 | lang=hu,len=500 | verdict=PASS | test_public_api_phase2_part_2.py |
| TC-PUB-6870 | P1 | Moderate hu clean at 1000 | lang=hu,len=1000 | verdict=PASS | test_public_api_phase2_part_2.py |
| TC-PUB-6871 | P1 | Moderate hu clean at 2000 | lang=hu,len=2000 | verdict=PASS | test_public_api_phase2_part_2.py |
| TC-PUB-6872 | P1 | Moderate hu flagged | lang=hu | verdict=PASS | test_public_api_phase2_part_2.py |
| TC-PUB-6873 | P1 | Moderate ro clean at 5 | lang=ro,len=5 | verdict=PASS | test_public_api_phase2_part_2.py |
| TC-PUB-6874 | P1 | Moderate ro clean at 25 | lang=ro,len=25 | verdict=PASS | test_public_api_phase2_part_2.py |
| TC-PUB-6875 | P1 | Moderate ro clean at 100 | lang=ro,len=100 | verdict=PASS | test_public_api_phase2_part_2.py |
| TC-PUB-6876 | P1 | Moderate ro clean at 250 | lang=ro,len=250 | verdict=PASS | test_public_api_phase2_part_2.py |
| TC-PUB-6877 | P1 | Moderate ro clean at 500 | lang=ro,len=500 | verdict=PASS | test_public_api_phase2_part_2.py |
| TC-PUB-6878 | P1 | Moderate ro clean at 1000 | lang=ro,len=1000 | verdict=PASS | test_public_api_phase2_part_2.py |
| TC-PUB-6879 | P1 | Moderate ro clean at 2000 | lang=ro,len=2000 | verdict=PASS | test_public_api_phase2_part_2.py |
| TC-PUB-6880 | P1 | Moderate ro flagged | lang=ro | verdict=BLOCK | test_public_api_phase2_part_2.py |
| TC-PUB-6881 | P1 | Moderate bg clean at 5 | lang=bg,len=5 | verdict=PASS | test_public_api_phase2_part_2.py |
| TC-PUB-6882 | P1 | Moderate bg clean at 25 | lang=bg,len=25 | verdict=PASS | test_public_api_phase2_part_2.py |
| TC-PUB-6883 | P1 | Moderate bg clean at 100 | lang=bg,len=100 | verdict=PASS | test_public_api_phase2_part_2.py |
| TC-PUB-6884 | P1 | Moderate bg clean at 250 | lang=bg,len=250 | verdict=PASS | test_public_api_phase2_part_2.py |
| TC-PUB-6885 | P1 | Moderate bg clean at 500 | lang=bg,len=500 | verdict=PASS | test_public_api_phase2_part_2.py |
| TC-PUB-6886 | P1 | Moderate bg clean at 1000 | lang=bg,len=1000 | verdict=PASS | test_public_api_phase2_part_2.py |
| TC-PUB-6887 | P1 | Moderate bg clean at 2000 | lang=bg,len=2000 | verdict=PASS | test_public_api_phase2_part_2.py |
| TC-PUB-6888 | P1 | Moderate bg flagged | lang=bg | verdict=PASS | test_public_api_phase2_part_2.py |
| TC-PUB-6912 | P1 | Batch size 2 scenario 0 | size=2,scenario=0 | all results | test_public_api_phase2_part_3.py |
| TC-PUB-6913 | P1 | Batch size 2 scenario 1 | size=2,scenario=1 | all results | test_public_api_phase2_part_3.py |
| TC-PUB-6914 | P1 | Batch size 2 scenario 2 | size=2,scenario=2 | all results | test_public_api_phase2_part_3.py |
| TC-PUB-6915 | P1 | Batch size 2 scenario 3 | size=2,scenario=3 | all results | test_public_api_phase2_part_3.py |
| TC-PUB-6916 | P1 | Batch size 2 scenario 4 | size=2,scenario=4 | all results | test_public_api_phase2_part_3.py |
| TC-PUB-6917 | P1 | Batch size 2 scenario 5 | size=2,scenario=5 | all results | test_public_api_phase2_part_3.py |
| TC-PUB-6918 | P1 | Batch size 2 scenario 6 | size=2,scenario=6 | all results | test_public_api_phase2_part_3.py |
| TC-PUB-6919 | P1 | Batch size 2 scenario 7 | size=2,scenario=7 | all results | test_public_api_phase2_part_3.py |
| TC-PUB-6920 | P1 | Batch size 2 scenario 8 | size=2,scenario=8 | all results | test_public_api_phase2_part_3.py |
| TC-PUB-6921 | P1 | Batch size 2 scenario 9 | size=2,scenario=9 | all results | test_public_api_phase2_part_3.py |
| TC-PUB-6922 | P1 | Batch size 2 scenario 10 | size=2,scenario=10 | all results | test_public_api_phase2_part_3.py |
| TC-PUB-6923 | P1 | Batch size 2 scenario 11 | size=2,scenario=11 | all results | test_public_api_phase2_part_3.py |
| TC-PUB-6924 | P1 | Batch size 2 scenario 12 | size=2,scenario=12 | all results | test_public_api_phase2_part_3.py |
| TC-PUB-6925 | P1 | Batch size 2 scenario 13 | size=2,scenario=13 | all results | test_public_api_phase2_part_3.py |
| TC-PUB-6926 | P1 | Batch size 2 scenario 14 | size=2,scenario=14 | all results | test_public_api_phase2_part_3.py |
| TC-PUB-6927 | P1 | Batch size 5 scenario 0 | size=5,scenario=0 | all results | test_public_api_phase2_part_3.py |
| TC-PUB-6928 | P1 | Batch size 5 scenario 1 | size=5,scenario=1 | all results | test_public_api_phase2_part_3.py |
| TC-PUB-6929 | P1 | Batch size 5 scenario 2 | size=5,scenario=2 | all results | test_public_api_phase2_part_3.py |
| TC-PUB-6930 | P1 | Batch size 5 scenario 3 | size=5,scenario=3 | all results | test_public_api_phase2_part_3.py |
| TC-PUB-6931 | P1 | Batch size 5 scenario 4 | size=5,scenario=4 | all results | test_public_api_phase2_part_3.py |
| TC-PUB-6932 | P1 | Batch size 5 scenario 5 | size=5,scenario=5 | all results | test_public_api_phase2_part_3.py |
| TC-PUB-6933 | P1 | Batch size 5 scenario 6 | size=5,scenario=6 | all results | test_public_api_phase2_part_3.py |
| TC-PUB-6934 | P1 | Batch size 5 scenario 7 | size=5,scenario=7 | all results | test_public_api_phase2_part_3.py |
| TC-PUB-6935 | P1 | Batch size 5 scenario 8 | size=5,scenario=8 | all results | test_public_api_phase2_part_3.py |
| TC-PUB-6936 | P1 | Batch size 5 scenario 9 | size=5,scenario=9 | all results | test_public_api_phase2_part_3.py |
| TC-PUB-6937 | P1 | Batch size 5 scenario 10 | size=5,scenario=10 | all results | test_public_api_phase2_part_3.py |
| TC-PUB-6938 | P1 | Batch size 5 scenario 11 | size=5,scenario=11 | all results | test_public_api_phase2_part_3.py |
| TC-PUB-6939 | P1 | Batch size 5 scenario 12 | size=5,scenario=12 | all results | test_public_api_phase2_part_3.py |
| TC-PUB-6940 | P1 | Batch size 5 scenario 13 | size=5,scenario=13 | all results | test_public_api_phase2_part_3.py |
| TC-PUB-6941 | P1 | Batch size 5 scenario 14 | size=5,scenario=14 | all results | test_public_api_phase2_part_3.py |
| TC-PUB-6942 | P1 | Batch size 10 scenario 0 | size=10,scenario=0 | all results | test_public_api_phase2_part_3.py |
| TC-PUB-6943 | P1 | Batch size 10 scenario 1 | size=10,scenario=1 | all results | test_public_api_phase2_part_3.py |
| TC-PUB-6944 | P1 | Batch size 10 scenario 2 | size=10,scenario=2 | all results | test_public_api_phase2_part_3.py |
| TC-PUB-6945 | P1 | Batch size 10 scenario 3 | size=10,scenario=3 | all results | test_public_api_phase2_part_3.py |
| TC-PUB-6946 | P1 | Batch size 10 scenario 4 | size=10,scenario=4 | all results | test_public_api_phase2_part_3.py |
| TC-PUB-6947 | P1 | Batch size 10 scenario 5 | size=10,scenario=5 | all results | test_public_api_phase2_part_3.py |
| TC-PUB-6948 | P1 | Batch size 10 scenario 6 | size=10,scenario=6 | all results | test_public_api_phase2_part_3.py |
| TC-PUB-6949 | P1 | Batch size 10 scenario 7 | size=10,scenario=7 | all results | test_public_api_phase2_part_3.py |
| TC-PUB-6950 | P1 | Batch size 10 scenario 8 | size=10,scenario=8 | all results | test_public_api_phase2_part_3.py |
| TC-PUB-6951 | P1 | Batch size 10 scenario 9 | size=10,scenario=9 | all results | test_public_api_phase2_part_3.py |
| TC-PUB-6952 | P1 | Batch size 10 scenario 10 | size=10,scenario=10 | all results | test_public_api_phase2_part_3.py |
| TC-PUB-6953 | P1 | Batch size 10 scenario 11 | size=10,scenario=11 | all results | test_public_api_phase2_part_3.py |
| TC-PUB-6954 | P1 | Batch size 10 scenario 12 | size=10,scenario=12 | all results | test_public_api_phase2_part_3.py |
| TC-PUB-6955 | P1 | Batch size 10 scenario 13 | size=10,scenario=13 | all results | test_public_api_phase2_part_3.py |
| TC-PUB-6956 | P1 | Batch size 10 scenario 14 | size=10,scenario=14 | all results | test_public_api_phase2_part_3.py |
| TC-PUB-6957 | P1 | Batch size 25 scenario 0 | size=25,scenario=0 | all results | test_public_api_phase2_part_3.py |
| TC-PUB-6958 | P1 | Batch size 25 scenario 1 | size=25,scenario=1 | all results | test_public_api_phase2_part_3.py |
| TC-PUB-6959 | P1 | Batch size 25 scenario 2 | size=25,scenario=2 | all results | test_public_api_phase2_part_3.py |
| TC-PUB-6960 | P1 | Batch size 25 scenario 3 | size=25,scenario=3 | all results | test_public_api_phase2_part_3.py |
| TC-PUB-6961 | P1 | Batch size 25 scenario 4 | size=25,scenario=4 | all results | test_public_api_phase2_part_3.py |
| TC-PUB-6962 | P1 | Batch size 25 scenario 5 | size=25,scenario=5 | all results | test_public_api_phase2_part_3.py |
| TC-PUB-6963 | P1 | Batch size 25 scenario 6 | size=25,scenario=6 | all results | test_public_api_phase2_part_3.py |
| TC-PUB-6964 | P1 | Batch size 25 scenario 7 | size=25,scenario=7 | all results | test_public_api_phase2_part_3.py |
| TC-PUB-6965 | P1 | Batch size 25 scenario 8 | size=25,scenario=8 | all results | test_public_api_phase2_part_3.py |
| TC-PUB-6966 | P1 | Batch size 25 scenario 9 | size=25,scenario=9 | all results | test_public_api_phase2_part_3.py |
| TC-PUB-6967 | P1 | Batch size 25 scenario 10 | size=25,scenario=10 | all results | test_public_api_phase2_part_3.py |
| TC-PUB-6968 | P1 | Batch size 25 scenario 11 | size=25,scenario=11 | all results | test_public_api_phase2_part_3.py |
| TC-PUB-6969 | P1 | Batch size 25 scenario 12 | size=25,scenario=12 | all results | test_public_api_phase2_part_3.py |
| TC-PUB-6970 | P1 | Batch size 25 scenario 13 | size=25,scenario=13 | all results | test_public_api_phase2_part_3.py |
| TC-PUB-6971 | P1 | Batch size 25 scenario 14 | size=25,scenario=14 | all results | test_public_api_phase2_part_3.py |
| TC-PUB-6972 | P1 | Batch size 50 scenario 0 | size=50,scenario=0 | all results | test_public_api_phase2_part_3.py |
| TC-PUB-6973 | P1 | Batch size 50 scenario 1 | size=50,scenario=1 | all results | test_public_api_phase2_part_3.py |
| TC-PUB-6974 | P1 | Batch size 50 scenario 2 | size=50,scenario=2 | all results | test_public_api_phase2_part_3.py |
| TC-PUB-6975 | P1 | Batch size 50 scenario 3 | size=50,scenario=3 | all results | test_public_api_phase2_part_3.py |
| TC-PUB-6976 | P1 | Batch size 50 scenario 4 | size=50,scenario=4 | all results | test_public_api_phase2_part_3.py |
| TC-PUB-6977 | P1 | Batch size 50 scenario 5 | size=50,scenario=5 | all results | test_public_api_phase2_part_3.py |
| TC-PUB-6978 | P1 | Batch size 50 scenario 6 | size=50,scenario=6 | all results | test_public_api_phase2_part_3.py |
| TC-PUB-6979 | P1 | Batch size 50 scenario 7 | size=50,scenario=7 | all results | test_public_api_phase2_part_3.py |
| TC-PUB-6980 | P1 | Batch size 50 scenario 8 | size=50,scenario=8 | all results | test_public_api_phase2_part_3.py |
| TC-PUB-6981 | P1 | Batch size 50 scenario 9 | size=50,scenario=9 | all results | test_public_api_phase2_part_3.py |
| TC-PUB-6982 | P1 | Batch size 50 scenario 10 | size=50,scenario=10 | all results | test_public_api_phase2_part_3.py |
| TC-PUB-6983 | P1 | Batch size 50 scenario 11 | size=50,scenario=11 | all results | test_public_api_phase2_part_3.py |
| TC-PUB-6984 | P1 | Batch size 50 scenario 12 | size=50,scenario=12 | all results | test_public_api_phase2_part_3.py |
| TC-PUB-6985 | P1 | Batch size 50 scenario 13 | size=50,scenario=13 | all results | test_public_api_phase2_part_3.py |
| TC-PUB-6986 | P1 | Batch size 50 scenario 14 | size=50,scenario=14 | all results | test_public_api_phase2_part_3.py |
| TC-PUB-6987 | P1 | Batch size 75 scenario 0 | size=75,scenario=0 | all results | test_public_api_phase2_part_3.py |
| TC-PUB-6988 | P1 | Batch size 75 scenario 1 | size=75,scenario=1 | all results | test_public_api_phase2_part_3.py |
| TC-PUB-6989 | P1 | Batch size 75 scenario 2 | size=75,scenario=2 | all results | test_public_api_phase2_part_3.py |
| TC-PUB-6990 | P1 | Batch size 75 scenario 3 | size=75,scenario=3 | all results | test_public_api_phase2_part_3.py |
| TC-PUB-6991 | P1 | Batch size 75 scenario 4 | size=75,scenario=4 | all results | test_public_api_phase2_part_3.py |
| TC-PUB-6992 | P1 | Batch size 75 scenario 5 | size=75,scenario=5 | all results | test_public_api_phase2_part_3.py |
| TC-PUB-6993 | P1 | Batch size 75 scenario 6 | size=75,scenario=6 | all results | test_public_api_phase2_part_3.py |
| TC-PUB-6994 | P1 | Batch size 75 scenario 7 | size=75,scenario=7 | all results | test_public_api_phase2_part_3.py |
| TC-PUB-6995 | P1 | Batch size 75 scenario 8 | size=75,scenario=8 | all results | test_public_api_phase2_part_3.py |
| TC-PUB-6996 | P1 | Batch size 75 scenario 9 | size=75,scenario=9 | all results | test_public_api_phase2_part_3.py |
| TC-PUB-6997 | P1 | Batch size 75 scenario 10 | size=75,scenario=10 | all results | test_public_api_phase2_part_3.py |
| TC-PUB-6998 | P1 | Batch size 75 scenario 11 | size=75,scenario=11 | all results | test_public_api_phase2_part_3.py |
| TC-PUB-6999 | P1 | Batch size 75 scenario 12 | size=75,scenario=12 | all results | test_public_api_phase2_part_3.py |
| TC-PUB-7000 | P1 | Batch size 75 scenario 13 | size=75,scenario=13 | all results | test_public_api_phase2_part_3.py |
| TC-PUB-7001 | P1 | Batch size 75 scenario 14 | size=75,scenario=14 | all results | test_public_api_phase2_part_3.py |
| TC-PUB-7002 | P1 | Batch size 100 scenario 0 | size=100,scenario=0 | all results | test_public_api_phase2_part_3.py |
| TC-PUB-7003 | P1 | Batch size 100 scenario 1 | size=100,scenario=1 | all results | test_public_api_phase2_part_3.py |
| TC-PUB-7004 | P1 | Batch size 100 scenario 2 | size=100,scenario=2 | all results | test_public_api_phase2_part_3.py |
| TC-PUB-7005 | P1 | Batch size 100 scenario 3 | size=100,scenario=3 | all results | test_public_api_phase2_part_3.py |
| TC-PUB-7006 | P1 | Batch size 100 scenario 4 | size=100,scenario=4 | all results | test_public_api_phase2_part_3.py |
| TC-PUB-7007 | P1 | Batch size 100 scenario 5 | size=100,scenario=5 | all results | test_public_api_phase2_part_3.py |
| TC-PUB-7008 | P1 | Batch size 100 scenario 6 | size=100,scenario=6 | all results | test_public_api_phase2_part_3.py |
| TC-PUB-7009 | P1 | Batch size 100 scenario 7 | size=100,scenario=7 | all results | test_public_api_phase2_part_3.py |
| TC-PUB-7010 | P1 | Batch size 100 scenario 8 | size=100,scenario=8 | all results | test_public_api_phase2_part_3.py |
| TC-PUB-7011 | P1 | Batch size 100 scenario 9 | size=100,scenario=9 | all results | test_public_api_phase2_part_3.py |
| TC-PUB-7017 | P2 | Validation empty text #0 | case=empty text | rejected cleanly | test_public_api_phase2_part_4.py |
| TC-PUB-7018 | P2 | Validation empty text #1 | case=empty text | rejected cleanly | test_public_api_phase2_part_4.py |
| TC-PUB-7019 | P2 | Validation empty text #2 | case=empty text | rejected cleanly | test_public_api_phase2_part_4.py |
| TC-PUB-7020 | P2 | Validation empty text #3 | case=empty text | rejected cleanly | test_public_api_phase2_part_4.py |
| TC-PUB-7021 | P2 | Validation empty text #4 | case=empty text | rejected cleanly | test_public_api_phase2_part_4.py |
| TC-PUB-7022 | P2 | Validation empty text #5 | case=empty text | rejected cleanly | test_public_api_phase2_part_4.py |
| TC-PUB-7023 | P2 | Validation empty text #6 | case=empty text | rejected cleanly | test_public_api_phase2_part_4.py |
| TC-PUB-7024 | P2 | Validation empty text #7 | case=empty text | rejected cleanly | test_public_api_phase2_part_4.py |
| TC-PUB-7025 | P2 | Validation empty text #8 | case=empty text | rejected cleanly | test_public_api_phase2_part_4.py |
| TC-PUB-7026 | P2 | Validation empty text #9 | case=empty text | rejected cleanly | test_public_api_phase2_part_4.py |
| TC-PUB-7027 | P2 | Validation null text #0 | case=null text | rejected cleanly | test_public_api_phase2_part_4.py |
| TC-PUB-7028 | P2 | Validation null text #1 | case=null text | rejected cleanly | test_public_api_phase2_part_4.py |
| TC-PUB-7029 | P2 | Validation null text #2 | case=null text | rejected cleanly | test_public_api_phase2_part_4.py |
| TC-PUB-7030 | P2 | Validation null text #3 | case=null text | rejected cleanly | test_public_api_phase2_part_4.py |
| TC-PUB-7031 | P2 | Validation null text #4 | case=null text | rejected cleanly | test_public_api_phase2_part_4.py |
| TC-PUB-7032 | P2 | Validation null text #5 | case=null text | rejected cleanly | test_public_api_phase2_part_4.py |
| TC-PUB-7033 | P2 | Validation null text #6 | case=null text | rejected cleanly | test_public_api_phase2_part_4.py |
| TC-PUB-7034 | P2 | Validation null text #7 | case=null text | rejected cleanly | test_public_api_phase2_part_4.py |
| TC-PUB-7035 | P2 | Validation null text #8 | case=null text | rejected cleanly | test_public_api_phase2_part_4.py |
| TC-PUB-7036 | P2 | Validation null text #9 | case=null text | rejected cleanly | test_public_api_phase2_part_4.py |
| TC-PUB-7037 | P2 | Validation missing text #0 | case=missing text | rejected cleanly | test_public_api_phase2_part_4.py |
| TC-PUB-7038 | P2 | Validation missing text #1 | case=missing text | rejected cleanly | test_public_api_phase2_part_4.py |
| TC-PUB-7039 | P2 | Validation missing text #2 | case=missing text | rejected cleanly | test_public_api_phase2_part_4.py |
| TC-PUB-7040 | P2 | Validation missing text #3 | case=missing text | rejected cleanly | test_public_api_phase2_part_4.py |
| TC-PUB-7041 | P2 | Validation missing text #4 | case=missing text | rejected cleanly | test_public_api_phase2_part_4.py |
| TC-PUB-7042 | P2 | Validation missing text #5 | case=missing text | rejected cleanly | test_public_api_phase2_part_4.py |
| TC-PUB-7043 | P2 | Validation missing text #6 | case=missing text | rejected cleanly | test_public_api_phase2_part_4.py |
| TC-PUB-7044 | P2 | Validation missing text #7 | case=missing text | rejected cleanly | test_public_api_phase2_part_4.py |
| TC-PUB-7045 | P2 | Validation missing text #8 | case=missing text | rejected cleanly | test_public_api_phase2_part_4.py |
| TC-PUB-7046 | P2 | Validation missing text #9 | case=missing text | rejected cleanly | test_public_api_phase2_part_4.py |
| TC-PUB-7047 | P2 | Validation unknown field #0 | case=unknown field | rejected cleanly | test_public_api_phase2_part_4.py |
| TC-PUB-7048 | P2 | Validation unknown field #1 | case=unknown field | rejected cleanly | test_public_api_phase2_part_4.py |
| TC-PUB-7049 | P2 | Validation unknown field #2 | case=unknown field | rejected cleanly | test_public_api_phase2_part_4.py |
| TC-PUB-7050 | P2 | Validation unknown field #3 | case=unknown field | rejected cleanly | test_public_api_phase2_part_4.py |
| TC-PUB-7051 | P2 | Validation unknown field #4 | case=unknown field | rejected cleanly | test_public_api_phase2_part_4.py |
| TC-PUB-7052 | P2 | Validation unknown field #5 | case=unknown field | rejected cleanly | test_public_api_phase2_part_4.py |
| TC-PUB-7053 | P2 | Validation unknown field #6 | case=unknown field | rejected cleanly | test_public_api_phase2_part_4.py |
| TC-PUB-7054 | P2 | Validation unknown field #7 | case=unknown field | rejected cleanly | test_public_api_phase2_part_4.py |
| TC-PUB-7055 | P2 | Validation unknown field #8 | case=unknown field | rejected cleanly | test_public_api_phase2_part_4.py |
| TC-PUB-7056 | P2 | Validation unknown field #9 | case=unknown field | rejected cleanly | test_public_api_phase2_part_4.py |
| TC-PUB-7057 | P2 | Validation non-string text #0 | case=non-string text | rejected cleanly | test_public_api_phase2_part_4.py |
| TC-PUB-7058 | P2 | Validation non-string text #1 | case=non-string text | rejected cleanly | test_public_api_phase2_part_4.py |
| TC-PUB-7059 | P2 | Validation non-string text #2 | case=non-string text | rejected cleanly | test_public_api_phase2_part_4.py |
| TC-PUB-7060 | P2 | Validation non-string text #3 | case=non-string text | rejected cleanly | test_public_api_phase2_part_4.py |
| TC-PUB-7061 | P2 | Validation non-string text #4 | case=non-string text | rejected cleanly | test_public_api_phase2_part_4.py |
| TC-PUB-7062 | P2 | Validation non-string text #5 | case=non-string text | rejected cleanly | test_public_api_phase2_part_4.py |
| TC-PUB-7063 | P2 | Validation non-string text #6 | case=non-string text | rejected cleanly | test_public_api_phase2_part_4.py |
| TC-PUB-7064 | P2 | Validation non-string text #7 | case=non-string text | rejected cleanly | test_public_api_phase2_part_4.py |
| TC-PUB-7065 | P2 | Validation non-string text #8 | case=non-string text | rejected cleanly | test_public_api_phase2_part_4.py |
| TC-PUB-7066 | P2 | Validation non-string text #9 | case=non-string text | rejected cleanly | test_public_api_phase2_part_4.py |
| TC-PUB-7067 | P2 | Validation over limit #0 | case=over limit | rejected cleanly | test_public_api_phase2_part_4.py |
| TC-PUB-7068 | P2 | Validation over limit #1 | case=over limit | rejected cleanly | test_public_api_phase2_part_4.py |
| TC-PUB-7069 | P2 | Validation over limit #2 | case=over limit | rejected cleanly | test_public_api_phase2_part_4.py |
| TC-PUB-7070 | P2 | Validation over limit #3 | case=over limit | rejected cleanly | test_public_api_phase2_part_4.py |
| TC-PUB-7071 | P2 | Validation over limit #4 | case=over limit | rejected cleanly | test_public_api_phase2_part_4.py |
| TC-PUB-7072 | P2 | Validation over limit #5 | case=over limit | rejected cleanly | test_public_api_phase2_part_4.py |
| TC-PUB-7073 | P2 | Validation over limit #6 | case=over limit | rejected cleanly | test_public_api_phase2_part_4.py |
| TC-PUB-7074 | P2 | Validation over limit #7 | case=over limit | rejected cleanly | test_public_api_phase2_part_4.py |
| TC-PUB-7075 | P2 | Validation over limit #8 | case=over limit | rejected cleanly | test_public_api_phase2_part_4.py |
| TC-PUB-7076 | P2 | Validation over limit #9 | case=over limit | rejected cleanly | test_public_api_phase2_part_4.py |
| TC-PUB-7077 | P2 | Validation empty batch #0 | case=empty batch | rejected cleanly | test_public_api_phase2_part_4.py |
| TC-PUB-7078 | P2 | Validation empty batch #1 | case=empty batch | rejected cleanly | test_public_api_phase2_part_4.py |
| TC-PUB-7079 | P2 | Validation empty batch #2 | case=empty batch | rejected cleanly | test_public_api_phase2_part_4.py |
| TC-PUB-7080 | P2 | Validation empty batch #3 | case=empty batch | rejected cleanly | test_public_api_phase2_part_4.py |
| TC-PUB-7081 | P2 | Validation empty batch #4 | case=empty batch | rejected cleanly | test_public_api_phase2_part_4.py |
| TC-PUB-7082 | P2 | Validation empty batch #5 | case=empty batch | rejected cleanly | test_public_api_phase2_part_4.py |
| TC-PUB-7083 | P2 | Validation empty batch #6 | case=empty batch | rejected cleanly | test_public_api_phase2_part_4.py |
| TC-PUB-7084 | P2 | Validation empty batch #7 | case=empty batch | rejected cleanly | test_public_api_phase2_part_4.py |
| TC-PUB-7085 | P2 | Validation empty batch #8 | case=empty batch | rejected cleanly | test_public_api_phase2_part_4.py |
| TC-PUB-7086 | P2 | Validation empty batch #9 | case=empty batch | rejected cleanly | test_public_api_phase2_part_4.py |
| TC-PUB-7087 | P2 | Validation bad batch item #0 | case=bad batch item | rejected cleanly | test_public_api_phase2_part_4.py |
| TC-PUB-7088 | P2 | Validation bad batch item #1 | case=bad batch item | rejected cleanly | test_public_api_phase2_part_4.py |
| TC-PUB-7089 | P2 | Validation bad batch item #2 | case=bad batch item | rejected cleanly | test_public_api_phase2_part_4.py |
| TC-PUB-7090 | P2 | Validation bad batch item #3 | case=bad batch item | rejected cleanly | test_public_api_phase2_part_4.py |
| TC-PUB-7091 | P2 | Validation bad batch item #4 | case=bad batch item | rejected cleanly | test_public_api_phase2_part_4.py |
| TC-PUB-7092 | P2 | Validation bad batch item #5 | case=bad batch item | rejected cleanly | test_public_api_phase2_part_4.py |
| TC-PUB-7093 | P2 | Validation bad batch item #6 | case=bad batch item | rejected cleanly | test_public_api_phase2_part_4.py |
| TC-PUB-7094 | P2 | Validation bad batch item #7 | case=bad batch item | rejected cleanly | test_public_api_phase2_part_4.py |
| TC-PUB-7095 | P2 | Validation bad batch item #8 | case=bad batch item | rejected cleanly | test_public_api_phase2_part_4.py |
| TC-PUB-7096 | P2 | Validation bad batch item #9 | case=bad batch item | rejected cleanly | test_public_api_phase2_part_4.py |
| TC-PUB-7097 | P2 | Validation malformed json #0 | case=malformed json | rejected cleanly | test_public_api_phase2_part_4.py |
| TC-PUB-7098 | P2 | Validation malformed json #1 | case=malformed json | rejected cleanly | test_public_api_phase2_part_4.py |
| TC-PUB-7099 | P2 | Validation malformed json #2 | case=malformed json | rejected cleanly | test_public_api_phase2_part_4.py |
| TC-PUB-7100 | P2 | Validation malformed json #3 | case=malformed json | rejected cleanly | test_public_api_phase2_part_4.py |
| TC-PUB-7101 | P2 | Validation malformed json #4 | case=malformed json | rejected cleanly | test_public_api_phase2_part_4.py |
| TC-PUB-7102 | P2 | Validation malformed json #5 | case=malformed json | rejected cleanly | test_public_api_phase2_part_4.py |
| TC-PUB-7103 | P2 | Validation malformed json #6 | case=malformed json | rejected cleanly | test_public_api_phase2_part_4.py |
| TC-PUB-7104 | P2 | Validation malformed json #7 | case=malformed json | rejected cleanly | test_public_api_phase2_part_4.py |
| TC-PUB-7105 | P2 | Validation malformed json #8 | case=malformed json | rejected cleanly | test_public_api_phase2_part_4.py |
| TC-PUB-7106 | P2 | Validation malformed json #9 | case=malformed json | rejected cleanly | test_public_api_phase2_part_4.py |
| TC-PUB-7107 | P2 | Validation at limit #0 | case=at limit | rejected cleanly | test_public_api_phase2_part_4.py |
| TC-PUB-7108 | P2 | Validation at limit #1 | case=at limit | rejected cleanly | test_public_api_phase2_part_4.py |
| TC-PUB-7109 | P2 | Validation at limit #2 | case=at limit | rejected cleanly | test_public_api_phase2_part_4.py |
| TC-PUB-7110 | P2 | Validation at limit #3 | case=at limit | rejected cleanly | test_public_api_phase2_part_4.py |
| TC-PUB-7111 | P2 | Validation at limit #4 | case=at limit | rejected cleanly | test_public_api_phase2_part_4.py |
| TC-PUB-7112 | P2 | Validation at limit #5 | case=at limit | rejected cleanly | test_public_api_phase2_part_4.py |
| TC-PUB-7113 | P2 | Validation at limit #6 | case=at limit | rejected cleanly | test_public_api_phase2_part_4.py |
| TC-PUB-7114 | P2 | Validation at limit #7 | case=at limit | rejected cleanly | test_public_api_phase2_part_4.py |
| TC-PUB-7115 | P2 | Validation at limit #8 | case=at limit | rejected cleanly | test_public_api_phase2_part_4.py |
| TC-PUB-7116 | P2 | Validation at limit #9 | case=at limit | rejected cleanly | test_public_api_phase2_part_4.py |
| TC-PUB-7117 | P2 | Edge content #0 scenario 0 | text='emoji 😀 test' | moderated | test_public_api_phase2_part_5.py |
| TC-PUB-7118 | P2 | Edge content #0 scenario 1 | text='emoji 😀 test' | moderated | test_public_api_phase2_part_5.py |
| TC-PUB-7119 | P2 | Edge content #0 scenario 2 | text='emoji 😀 test' | moderated | test_public_api_phase2_part_5.py |
| TC-PUB-7120 | P2 | Edge content #0 scenario 3 | text='emoji 😀 test' | moderated | test_public_api_phase2_part_5.py |
| TC-PUB-7121 | P2 | Edge content #0 scenario 4 | text='emoji 😀 test' | moderated | test_public_api_phase2_part_5.py |
| TC-PUB-7122 | P2 | Edge content #1 scenario 0 | text='café au lait' | moderated | test_public_api_phase2_part_5.py |
| TC-PUB-7123 | P2 | Edge content #1 scenario 1 | text='café au lait' | moderated | test_public_api_phase2_part_5.py |
| TC-PUB-7124 | P2 | Edge content #1 scenario 2 | text='café au lait' | moderated | test_public_api_phase2_part_5.py |
| TC-PUB-7125 | P2 | Edge content #1 scenario 3 | text='café au lait' | moderated | test_public_api_phase2_part_5.py |
| TC-PUB-7126 | P2 | Edge content #1 scenario 4 | text='café au lait' | moderated | test_public_api_phase2_part_5.py |
| TC-PUB-7127 | P2 | Edge content #2 scenario 0 | text='ｆｕｌｌｗｉｄｔｈ' | moderated | test_public_api_phase2_part_5.py |
| TC-PUB-7128 | P2 | Edge content #2 scenario 1 | text='ｆｕｌｌｗｉｄｔｈ' | moderated | test_public_api_phase2_part_5.py |
| TC-PUB-7129 | P2 | Edge content #2 scenario 2 | text='ｆｕｌｌｗｉｄｔｈ' | moderated | test_public_api_phase2_part_5.py |
| TC-PUB-7130 | P2 | Edge content #2 scenario 3 | text='ｆｕｌｌｗｉｄｔｈ' | moderated | test_public_api_phase2_part_5.py |
| TC-PUB-7131 | P2 | Edge content #2 scenario 4 | text='ｆｕｌｌｗｉｄｔｈ' | moderated | test_public_api_phase2_part_5.py |
| TC-PUB-7132 | P2 | Edge content #3 scenario 0 | text='mixed 中文 eng' | moderated | test_public_api_phase2_part_5.py |
| TC-PUB-7133 | P2 | Edge content #3 scenario 1 | text='mixed 中文 eng' | moderated | test_public_api_phase2_part_5.py |
| TC-PUB-7134 | P2 | Edge content #3 scenario 2 | text='mixed 中文 eng' | moderated | test_public_api_phase2_part_5.py |
| TC-PUB-7135 | P2 | Edge content #3 scenario 3 | text='mixed 中文 eng' | moderated | test_public_api_phase2_part_5.py |
| TC-PUB-7136 | P2 | Edge content #3 scenario 4 | text='mixed 中文 eng' | moderated | test_public_api_phase2_part_5.py |
| TC-PUB-7137 | P2 | Edge content #4 scenario 0 | text='tab\tseparate' | moderated | test_public_api_phase2_part_5.py |
| TC-PUB-7138 | P2 | Edge content #4 scenario 1 | text='tab\tseparate' | moderated | test_public_api_phase2_part_5.py |
| TC-PUB-7139 | P2 | Edge content #4 scenario 2 | text='tab\tseparate' | moderated | test_public_api_phase2_part_5.py |
| TC-PUB-7140 | P2 | Edge content #4 scenario 3 | text='tab\tseparate' | moderated | test_public_api_phase2_part_5.py |
| TC-PUB-7141 | P2 | Edge content #4 scenario 4 | text='tab\tseparate' | moderated | test_public_api_phase2_part_5.py |
| TC-PUB-7142 | P2 | Edge content #5 scenario 0 | text='line\nbreak' | moderated | test_public_api_phase2_part_5.py |
| TC-PUB-7143 | P2 | Edge content #5 scenario 1 | text='line\nbreak' | moderated | test_public_api_phase2_part_5.py |
| TC-PUB-7144 | P2 | Edge content #5 scenario 2 | text='line\nbreak' | moderated | test_public_api_phase2_part_5.py |
| TC-PUB-7145 | P2 | Edge content #5 scenario 3 | text='line\nbreak' | moderated | test_public_api_phase2_part_5.py |
| TC-PUB-7146 | P2 | Edge content #5 scenario 4 | text='line\nbreak' | moderated | test_public_api_phase2_part_5.py |
| TC-PUB-7147 | P2 | Edge content #6 scenario 0 | text='multiple   s' | moderated | test_public_api_phase2_part_5.py |
| TC-PUB-7148 | P2 | Edge content #6 scenario 1 | text='multiple   s' | moderated | test_public_api_phase2_part_5.py |
| TC-PUB-7149 | P2 | Edge content #6 scenario 2 | text='multiple   s' | moderated | test_public_api_phase2_part_5.py |
| TC-PUB-7150 | P2 | Edge content #6 scenario 3 | text='multiple   s' | moderated | test_public_api_phase2_part_5.py |
| TC-PUB-7151 | P2 | Edge content #6 scenario 4 | text='multiple   s' | moderated | test_public_api_phase2_part_5.py |
| TC-PUB-7152 | P2 | Edge content #7 scenario 0 | text='!!! ??? ...' | moderated | test_public_api_phase2_part_5.py |
| TC-PUB-7153 | P2 | Edge content #7 scenario 1 | text='!!! ??? ...' | moderated | test_public_api_phase2_part_5.py |
| TC-PUB-7154 | P2 | Edge content #7 scenario 2 | text='!!! ??? ...' | moderated | test_public_api_phase2_part_5.py |
| TC-PUB-7155 | P2 | Edge content #7 scenario 3 | text='!!! ??? ...' | moderated | test_public_api_phase2_part_5.py |
| TC-PUB-7156 | P2 | Edge content #7 scenario 4 | text='!!! ??? ...' | moderated | test_public_api_phase2_part_5.py |
| TC-PUB-7157 | P2 | Edge content #8 scenario 0 | text='12345 67890' | moderated | test_public_api_phase2_part_5.py |
| TC-PUB-7158 | P2 | Edge content #8 scenario 1 | text='12345 67890' | moderated | test_public_api_phase2_part_5.py |
| TC-PUB-7159 | P2 | Edge content #8 scenario 2 | text='12345 67890' | moderated | test_public_api_phase2_part_5.py |
| TC-PUB-7160 | P2 | Edge content #8 scenario 3 | text='12345 67890' | moderated | test_public_api_phase2_part_5.py |
| TC-PUB-7161 | P2 | Edge content #8 scenario 4 | text='12345 67890' | moderated | test_public_api_phase2_part_5.py |
| TC-PUB-7162 | P2 | Edge content #9 scenario 0 | text='x' | moderated | test_public_api_phase2_part_5.py |
| TC-PUB-7163 | P2 | Edge content #9 scenario 1 | text='x' | moderated | test_public_api_phase2_part_5.py |
| TC-PUB-7164 | P2 | Edge content #9 scenario 2 | text='x' | moderated | test_public_api_phase2_part_5.py |
| TC-PUB-7165 | P2 | Edge content #9 scenario 3 | text='x' | moderated | test_public_api_phase2_part_5.py |
| TC-PUB-7166 | P2 | Edge content #9 scenario 4 | text='x' | moderated | test_public_api_phase2_part_5.py |
| TC-PUB-7167 | P2 | Edge content #10 scenario 0 | text='ßæøåñ' | moderated | test_public_api_phase2_part_5.py |
| TC-PUB-7168 | P2 | Edge content #10 scenario 1 | text='ßæøåñ' | moderated | test_public_api_phase2_part_5.py |
| TC-PUB-7169 | P2 | Edge content #10 scenario 2 | text='ßæøåñ' | moderated | test_public_api_phase2_part_5.py |
| TC-PUB-7170 | P2 | Edge content #10 scenario 3 | text='ßæøåñ' | moderated | test_public_api_phase2_part_5.py |
| TC-PUB-7171 | P2 | Edge content #10 scenario 4 | text='ßæøåñ' | moderated | test_public_api_phase2_part_5.py |
| TC-PUB-7172 | P2 | Edge content #11 scenario 0 | text='\u2028hidden' | moderated | test_public_api_phase2_part_5.py |
| TC-PUB-7173 | P2 | Edge content #11 scenario 1 | text='\u2028hidden' | moderated | test_public_api_phase2_part_5.py |
| TC-PUB-7174 | P2 | Edge content #11 scenario 2 | text='\u2028hidden' | moderated | test_public_api_phase2_part_5.py |
| TC-PUB-7175 | P2 | Edge content #11 scenario 3 | text='\u2028hidden' | moderated | test_public_api_phase2_part_5.py |
| TC-PUB-7176 | P2 | Edge content #11 scenario 4 | text='\u2028hidden' | moderated | test_public_api_phase2_part_5.py |
| TC-PUB-7177 | P2 | Edge content #12 scenario 0 | text='zero width \u200b' | moderated | test_public_api_phase2_part_5.py |
| TC-PUB-7178 | P2 | Edge content #12 scenario 1 | text='zero width \u200b' | moderated | test_public_api_phase2_part_5.py |
| TC-PUB-7179 | P2 | Edge content #12 scenario 2 | text='zero width \u200b' | moderated | test_public_api_phase2_part_5.py |
| TC-PUB-7180 | P2 | Edge content #12 scenario 3 | text='zero width \u200b' | moderated | test_public_api_phase2_part_5.py |
| TC-PUB-7181 | P2 | Edge content #12 scenario 4 | text='zero width \u200b' | moderated | test_public_api_phase2_part_5.py |
| TC-PUB-7182 | P2 | Edge content #13 scenario 0 | text='directional ' | moderated | test_public_api_phase2_part_5.py |
| TC-PUB-7183 | P2 | Edge content #13 scenario 1 | text='directional ' | moderated | test_public_api_phase2_part_5.py |
| TC-PUB-7184 | P2 | Edge content #13 scenario 2 | text='directional ' | moderated | test_public_api_phase2_part_5.py |
| TC-PUB-7185 | P2 | Edge content #13 scenario 3 | text='directional ' | moderated | test_public_api_phase2_part_5.py |
| TC-PUB-7186 | P2 | Edge content #13 scenario 4 | text='directional ' | moderated | test_public_api_phase2_part_5.py |
| TC-PUB-7187 | P2 | Edge content #14 scenario 0 | text='combining é' | moderated | test_public_api_phase2_part_5.py |
| TC-PUB-7188 | P2 | Edge content #14 scenario 1 | text='combining é' | moderated | test_public_api_phase2_part_5.py |
| TC-PUB-7189 | P2 | Edge content #14 scenario 2 | text='combining é' | moderated | test_public_api_phase2_part_5.py |
| TC-PUB-7190 | P2 | Edge content #14 scenario 3 | text='combining é' | moderated | test_public_api_phase2_part_5.py |
| TC-PUB-7191 | P2 | Edge content #14 scenario 4 | text='combining é' | moderated | test_public_api_phase2_part_5.py |
| TC-PUB-7192 | P2 | Edge content #15 scenario 0 | text='русский текс' | moderated | test_public_api_phase2_part_5.py |
| TC-PUB-7193 | P2 | Edge content #15 scenario 1 | text='русский текс' | moderated | test_public_api_phase2_part_5.py |
| TC-PUB-7194 | P2 | Edge content #15 scenario 2 | text='русский текс' | moderated | test_public_api_phase2_part_5.py |
| TC-PUB-7195 | P2 | Edge content #15 scenario 3 | text='русский текс' | moderated | test_public_api_phase2_part_5.py |
| TC-PUB-7196 | P2 | Edge content #15 scenario 4 | text='русский текс' | moderated | test_public_api_phase2_part_5.py |
| TC-PUB-7197 | P2 | Edge content #16 scenario 0 | text='日本語の文章' | moderated | test_public_api_phase2_part_5.py |
| TC-PUB-7198 | P2 | Edge content #16 scenario 1 | text='日本語の文章' | moderated | test_public_api_phase2_part_5.py |
| TC-PUB-7199 | P2 | Edge content #16 scenario 2 | text='日本語の文章' | moderated | test_public_api_phase2_part_5.py |
| TC-PUB-7200 | P2 | Edge content #16 scenario 3 | text='日本語の文章' | moderated | test_public_api_phase2_part_5.py |
| TC-PUB-7201 | P2 | Edge content #16 scenario 4 | text='日本語の文章' | moderated | test_public_api_phase2_part_5.py |
| TC-PUB-7202 | P2 | Edge content #17 scenario 0 | text='한국어 문장' | moderated | test_public_api_phase2_part_5.py |
| TC-PUB-7203 | P2 | Edge content #17 scenario 1 | text='한국어 문장' | moderated | test_public_api_phase2_part_5.py |
| TC-PUB-7204 | P2 | Edge content #17 scenario 2 | text='한국어 문장' | moderated | test_public_api_phase2_part_5.py |
| TC-PUB-7205 | P2 | Edge content #17 scenario 3 | text='한국어 문장' | moderated | test_public_api_phase2_part_5.py |
| TC-PUB-7206 | P2 | Edge content #17 scenario 4 | text='한국어 문장' | moderated | test_public_api_phase2_part_5.py |
| TC-PUB-7207 | P2 | Edge content #18 scenario 0 | text='العربية نص' | moderated | test_public_api_phase2_part_5.py |
| TC-PUB-7208 | P2 | Edge content #18 scenario 1 | text='العربية نص' | moderated | test_public_api_phase2_part_5.py |
| TC-PUB-7209 | P2 | Edge content #18 scenario 2 | text='العربية نص' | moderated | test_public_api_phase2_part_5.py |
| TC-PUB-7210 | P2 | Edge content #18 scenario 3 | text='العربية نص' | moderated | test_public_api_phase2_part_5.py |
| TC-PUB-7211 | P2 | Edge content #18 scenario 4 | text='العربية نص' | moderated | test_public_api_phase2_part_5.py |
| TC-PUB-7212 | P2 | Edge content #19 scenario 0 | text='עברית טקסט' | moderated | test_public_api_phase2_part_5.py |
| TC-PUB-7213 | P2 | Edge content #19 scenario 1 | text='עברית טקסט' | moderated | test_public_api_phase2_part_5.py |
| TC-PUB-7214 | P2 | Edge content #19 scenario 2 | text='עברית טקסט' | moderated | test_public_api_phase2_part_5.py |
| TC-PUB-7215 | P2 | Edge content #19 scenario 3 | text='עברית טקסט' | moderated | test_public_api_phase2_part_5.py |
| TC-PUB-7216 | P2 | Edge content #19 scenario 4 | text='עברית טקסט' | moderated | test_public_api_phase2_part_5.py |
| TC-PUB-7217 | P2 | Profiling flow scenario 0 | user=pubuser0 | rows recorded | test_public_api_phase2_part_6.py |
| TC-PUB-7218 | P2 | Profiling flow scenario 1 | user=pubuser1 | rows recorded | test_public_api_phase2_part_6.py |
| TC-PUB-7219 | P2 | Profiling flow scenario 2 | user=pubuser2 | rows recorded | test_public_api_phase2_part_6.py |
| TC-PUB-7220 | P2 | Profiling flow scenario 3 | user=pubuser3 | rows recorded | test_public_api_phase2_part_6.py |
| TC-PUB-7221 | P2 | Profiling flow scenario 4 | user=pubuser4 | rows recorded | test_public_api_phase2_part_6.py |
| TC-PUB-7222 | P2 | Profiling flow scenario 5 | user=pubuser5 | rows recorded | test_public_api_phase2_part_6.py |
| TC-PUB-7223 | P2 | Profiling flow scenario 6 | user=pubuser6 | rows recorded | test_public_api_phase2_part_6.py |
| TC-PUB-7224 | P2 | Profiling flow scenario 7 | user=pubuser7 | rows recorded | test_public_api_phase2_part_6.py |
| TC-PUB-7225 | P2 | Profiling flow scenario 8 | user=pubuser8 | rows recorded | test_public_api_phase2_part_6.py |
| TC-PUB-7226 | P2 | Profiling flow scenario 9 | user=pubuser9 | rows recorded | test_public_api_phase2_part_6.py |
| TC-PUB-7227 | P2 | Profiling flow scenario 10 | user=pubuser10 | rows recorded | test_public_api_phase2_part_6.py |
| TC-PUB-7228 | P2 | Profiling flow scenario 11 | user=pubuser11 | rows recorded | test_public_api_phase2_part_6.py |
| TC-PUB-7229 | P2 | Profiling flow scenario 12 | user=pubuser12 | rows recorded | test_public_api_phase2_part_6.py |
| TC-PUB-7230 | P2 | Profiling flow scenario 13 | user=pubuser13 | rows recorded | test_public_api_phase2_part_6.py |
| TC-PUB-7231 | P2 | Profiling flow scenario 14 | user=pubuser14 | rows recorded | test_public_api_phase2_part_6.py |
| TC-PUB-7232 | P2 | Profiling flow scenario 15 | user=pubuser15 | rows recorded | test_public_api_phase2_part_6.py |
| TC-PUB-7233 | P2 | Profiling flow scenario 16 | user=pubuser16 | rows recorded | test_public_api_phase2_part_6.py |
| TC-PUB-7234 | P2 | Profiling flow scenario 17 | user=pubuser17 | rows recorded | test_public_api_phase2_part_6.py |
| TC-PUB-7235 | P2 | Profiling flow scenario 18 | user=pubuser18 | rows recorded | test_public_api_phase2_part_6.py |
| TC-PUB-7236 | P2 | Profiling flow scenario 19 | user=pubuser19 | rows recorded | test_public_api_phase2_part_6.py |
| TC-PUB-7237 | P2 | Profiling flow scenario 20 | user=pubuser20 | rows recorded | test_public_api_phase2_part_6.py |
| TC-PUB-7238 | P2 | Profiling flow scenario 21 | user=pubuser21 | rows recorded | test_public_api_phase2_part_6.py |
| TC-PUB-7239 | P2 | Profiling flow scenario 22 | user=pubuser22 | rows recorded | test_public_api_phase2_part_6.py |
| TC-PUB-7240 | P2 | Profiling flow scenario 23 | user=pubuser23 | rows recorded | test_public_api_phase2_part_6.py |
| TC-PUB-7241 | P2 | Profiling flow scenario 24 | user=pubuser24 | rows recorded | test_public_api_phase2_part_6.py |
| TC-PUB-7242 | P2 | Profiling flow scenario 25 | user=pubuser25 | rows recorded | test_public_api_phase2_part_6.py |
| TC-PUB-7243 | P2 | Profiling flow scenario 26 | user=pubuser26 | rows recorded | test_public_api_phase2_part_6.py |
| TC-PUB-7244 | P2 | Profiling flow scenario 27 | user=pubuser27 | rows recorded | test_public_api_phase2_part_6.py |
| TC-PUB-7245 | P2 | Profiling flow scenario 28 | user=pubuser28 | rows recorded | test_public_api_phase2_part_6.py |
| TC-PUB-7246 | P2 | Profiling flow scenario 29 | user=pubuser29 | rows recorded | test_public_api_phase2_part_6.py |
| TC-PUB-7247 | P2 | Profiling flow scenario 30 | user=pubuser30 | rows recorded | test_public_api_phase2_part_6.py |
| TC-PUB-7248 | P2 | Profiling flow scenario 31 | user=pubuser31 | rows recorded | test_public_api_phase2_part_6.py |
| TC-PUB-7249 | P2 | Profiling flow scenario 32 | user=pubuser32 | rows recorded | test_public_api_phase2_part_6.py |
| TC-PUB-7250 | P2 | Profiling flow scenario 33 | user=pubuser33 | rows recorded | test_public_api_phase2_part_6.py |
| TC-PUB-7251 | P2 | Profiling flow scenario 34 | user=pubuser34 | rows recorded | test_public_api_phase2_part_6.py |
| TC-PUB-7252 | P2 | Profiling flow scenario 35 | user=pubuser35 | rows recorded | test_public_api_phase2_part_6.py |
| TC-PUB-7253 | P2 | Profiling flow scenario 36 | user=pubuser36 | rows recorded | test_public_api_phase2_part_6.py |
| TC-PUB-7254 | P2 | Profiling flow scenario 37 | user=pubuser37 | rows recorded | test_public_api_phase2_part_6.py |
| TC-PUB-7255 | P2 | Profiling flow scenario 38 | user=pubuser38 | rows recorded | test_public_api_phase2_part_6.py |
| TC-PUB-7256 | P2 | Profiling flow scenario 39 | user=pubuser39 | rows recorded | test_public_api_phase2_part_6.py |
| TC-PUB-7257 | P2 | Profiling flow scenario 40 | user=pubuser40 | rows recorded | test_public_api_phase2_part_6.py |
| TC-PUB-7258 | P2 | Profiling flow scenario 41 | user=pubuser41 | rows recorded | test_public_api_phase2_part_6.py |
| TC-PUB-7259 | P2 | Profiling flow scenario 42 | user=pubuser42 | rows recorded | test_public_api_phase2_part_6.py |
| TC-PUB-7260 | P2 | Profiling flow scenario 43 | user=pubuser43 | rows recorded | test_public_api_phase2_part_6.py |
| TC-PUB-7261 | P2 | Profiling flow scenario 44 | user=pubuser44 | rows recorded | test_public_api_phase2_part_6.py |
| TC-PUB-7262 | P2 | Profiling flow scenario 45 | user=pubuser45 | rows recorded | test_public_api_phase2_part_6.py |
| TC-PUB-7263 | P2 | Profiling flow scenario 46 | user=pubuser46 | rows recorded | test_public_api_phase2_part_6.py |
| TC-PUB-7264 | P2 | Profiling flow scenario 47 | user=pubuser47 | rows recorded | test_public_api_phase2_part_6.py |
| TC-PUB-7265 | P2 | Profiling flow scenario 48 | user=pubuser48 | rows recorded | test_public_api_phase2_part_6.py |
| TC-PUB-7266 | P2 | Profiling flow scenario 49 | user=pubuser49 | rows recorded | test_public_api_phase2_part_6.py |
| TC-PUB-7267 | P2 | Profiling flow scenario 50 | user=pubuser50 | rows recorded | test_public_api_phase2_part_6.py |
| TC-PUB-7268 | P2 | Profiling flow scenario 51 | user=pubuser51 | rows recorded | test_public_api_phase2_part_6.py |
| TC-PUB-7269 | P2 | Profiling flow scenario 52 | user=pubuser52 | rows recorded | test_public_api_phase2_part_6.py |
| TC-PUB-7270 | P2 | Profiling flow scenario 53 | user=pubuser53 | rows recorded | test_public_api_phase2_part_6.py |
| TC-PUB-7271 | P2 | Profiling flow scenario 54 | user=pubuser54 | rows recorded | test_public_api_phase2_part_6.py |
| TC-PUB-7272 | P2 | Profiling flow scenario 55 | user=pubuser55 | rows recorded | test_public_api_phase2_part_6.py |
| TC-PUB-7273 | P2 | Profiling flow scenario 56 | user=pubuser56 | rows recorded | test_public_api_phase2_part_6.py |
| TC-PUB-7274 | P2 | Profiling flow scenario 57 | user=pubuser57 | rows recorded | test_public_api_phase2_part_6.py |
| TC-PUB-7275 | P2 | Profiling flow scenario 58 | user=pubuser58 | rows recorded | test_public_api_phase2_part_6.py |
| TC-PUB-7276 | P2 | Profiling flow scenario 59 | user=pubuser59 | rows recorded | test_public_api_phase2_part_6.py |
| TC-PUB-7277 | P2 | Profiling flow scenario 60 | user=pubuser60 | rows recorded | test_public_api_phase2_part_6.py |
| TC-PUB-7278 | P2 | Profiling flow scenario 61 | user=pubuser61 | rows recorded | test_public_api_phase2_part_6.py |
| TC-PUB-7279 | P2 | Profiling flow scenario 62 | user=pubuser62 | rows recorded | test_public_api_phase2_part_6.py |
| TC-PUB-7280 | P2 | Profiling flow scenario 63 | user=pubuser63 | rows recorded | test_public_api_phase2_part_6.py |
| TC-PUB-7281 | P2 | Profiling flow scenario 64 | user=pubuser64 | rows recorded | test_public_api_phase2_part_6.py |
| TC-PUB-7282 | P2 | Profiling flow scenario 65 | user=pubuser65 | rows recorded | test_public_api_phase2_part_6.py |
| TC-PUB-7283 | P2 | Profiling flow scenario 66 | user=pubuser66 | rows recorded | test_public_api_phase2_part_6.py |
| TC-PUB-7284 | P2 | Profiling flow scenario 67 | user=pubuser67 | rows recorded | test_public_api_phase2_part_6.py |
| TC-PUB-7285 | P2 | Profiling flow scenario 68 | user=pubuser68 | rows recorded | test_public_api_phase2_part_6.py |
| TC-PUB-7286 | P2 | Profiling flow scenario 69 | user=pubuser69 | rows recorded | test_public_api_phase2_part_6.py |
| TC-PUB-7287 | P2 | Profiling flow scenario 70 | user=pubuser70 | rows recorded | test_public_api_phase2_part_6.py |
| TC-PUB-7288 | P2 | Profiling flow scenario 71 | user=pubuser71 | rows recorded | test_public_api_phase2_part_6.py |
| TC-PUB-7289 | P2 | Profiling flow scenario 72 | user=pubuser72 | rows recorded | test_public_api_phase2_part_6.py |
| TC-PUB-7290 | P2 | Profiling flow scenario 73 | user=pubuser73 | rows recorded | test_public_api_phase2_part_6.py |
| TC-PUB-7291 | P2 | Profiling flow scenario 74 | user=pubuser74 | rows recorded | test_public_api_phase2_part_6.py |
| TC-PUB-7292 | P2 | Profiling flow scenario 75 | user=pubuser75 | rows recorded | test_public_api_phase2_part_6.py |
| TC-PUB-7293 | P2 | Profiling flow scenario 76 | user=pubuser76 | rows recorded | test_public_api_phase2_part_6.py |
| TC-PUB-7294 | P2 | Profiling flow scenario 77 | user=pubuser77 | rows recorded | test_public_api_phase2_part_6.py |
| TC-PUB-7295 | P2 | Profiling flow scenario 78 | user=pubuser78 | rows recorded | test_public_api_phase2_part_6.py |
| TC-PUB-7296 | P2 | Profiling flow scenario 79 | user=pubuser79 | rows recorded | test_public_api_phase2_part_6.py |
| TC-PUB-7297 | P2 | Profiling flow scenario 80 | user=pubuser80 | rows recorded | test_public_api_phase2_part_6.py |
| TC-PUB-7298 | P2 | Profiling flow scenario 81 | user=pubuser81 | rows recorded | test_public_api_phase2_part_6.py |
| TC-PUB-7299 | P2 | Profiling flow scenario 82 | user=pubuser82 | rows recorded | test_public_api_phase2_part_6.py |
| TC-PUB-7300 | P2 | Profiling flow scenario 83 | user=pubuser83 | rows recorded | test_public_api_phase2_part_6.py |
| TC-PUB-7301 | P2 | Profiling flow scenario 84 | user=pubuser84 | rows recorded | test_public_api_phase2_part_6.py |
| TC-PUB-7302 | P2 | Profiling flow scenario 85 | user=pubuser85 | rows recorded | test_public_api_phase2_part_6.py |
| TC-PUB-7303 | P2 | Profiling flow scenario 86 | user=pubuser86 | rows recorded | test_public_api_phase2_part_6.py |
| TC-PUB-7304 | P2 | Profiling flow scenario 87 | user=pubuser87 | rows recorded | test_public_api_phase2_part_6.py |
| TC-PUB-7305 | P2 | Profiling flow scenario 88 | user=pubuser88 | rows recorded | test_public_api_phase2_part_6.py |
| TC-PUB-7306 | P2 | Profiling flow scenario 89 | user=pubuser89 | rows recorded | test_public_api_phase2_part_6.py |
| TC-PUB-7307 | P2 | Profiling flow scenario 90 | user=pubuser90 | rows recorded | test_public_api_phase2_part_6.py |
| TC-PUB-7308 | P2 | Profiling flow scenario 91 | user=pubuser91 | rows recorded | test_public_api_phase2_part_6.py |
| TC-PUB-7309 | P2 | Profiling flow scenario 92 | user=pubuser92 | rows recorded | test_public_api_phase2_part_6.py |
| TC-PUB-7310 | P2 | Profiling flow scenario 93 | user=pubuser93 | rows recorded | test_public_api_phase2_part_6.py |
| TC-PUB-7311 | P2 | Profiling flow scenario 94 | user=pubuser94 | rows recorded | test_public_api_phase2_part_6.py |
| TC-PUB-7312 | P2 | Profiling flow scenario 95 | user=pubuser95 | rows recorded | test_public_api_phase2_part_6.py |
| TC-PUB-7313 | P2 | Profiling flow scenario 96 | user=pubuser96 | rows recorded | test_public_api_phase2_part_6.py |
| TC-PUB-7314 | P2 | Profiling flow scenario 97 | user=pubuser97 | rows recorded | test_public_api_phase2_part_6.py |
| TC-PUB-7315 | P2 | Profiling flow scenario 98 | user=pubuser98 | rows recorded | test_public_api_phase2_part_6.py |
| TC-PUB-7316 | P2 | Profiling flow scenario 99 | user=pubuser99 | rows recorded | test_public_api_phase2_part_6.py |
| TC-PUB-7317 | P2 | Response shape id #0 | field=id | present | test_public_api_phase2_part_7.py |
| TC-PUB-7318 | P2 | Response shape id #1 | field=id | present | test_public_api_phase2_part_7.py |
| TC-PUB-7319 | P2 | Response shape id #2 | field=id | present | test_public_api_phase2_part_7.py |
| TC-PUB-7320 | P2 | Response shape id #3 | field=id | present | test_public_api_phase2_part_7.py |
| TC-PUB-7321 | P2 | Response shape id #4 | field=id | present | test_public_api_phase2_part_7.py |
| TC-PUB-7322 | P2 | Response shape id #5 | field=id | present | test_public_api_phase2_part_7.py |
| TC-PUB-7323 | P2 | Response shape id #6 | field=id | present | test_public_api_phase2_part_7.py |
| TC-PUB-7324 | P2 | Response shape id #7 | field=id | present | test_public_api_phase2_part_7.py |
| TC-PUB-7325 | P2 | Response shape verdict #0 | field=verdict | present | test_public_api_phase2_part_7.py |
| TC-PUB-7326 | P2 | Response shape verdict #1 | field=verdict | present | test_public_api_phase2_part_7.py |
| TC-PUB-7327 | P2 | Response shape verdict #2 | field=verdict | present | test_public_api_phase2_part_7.py |
| TC-PUB-7328 | P2 | Response shape verdict #3 | field=verdict | present | test_public_api_phase2_part_7.py |
| TC-PUB-7329 | P2 | Response shape verdict #4 | field=verdict | present | test_public_api_phase2_part_7.py |
| TC-PUB-7330 | P2 | Response shape verdict #5 | field=verdict | present | test_public_api_phase2_part_7.py |
| TC-PUB-7331 | P2 | Response shape verdict #6 | field=verdict | present | test_public_api_phase2_part_7.py |
| TC-PUB-7332 | P2 | Response shape verdict #7 | field=verdict | present | test_public_api_phase2_part_7.py |
| TC-PUB-7333 | P2 | Response shape allowed #0 | field=allowed | present | test_public_api_phase2_part_7.py |
| TC-PUB-7334 | P2 | Response shape allowed #1 | field=allowed | present | test_public_api_phase2_part_7.py |
| TC-PUB-7335 | P2 | Response shape allowed #2 | field=allowed | present | test_public_api_phase2_part_7.py |
| TC-PUB-7336 | P2 | Response shape allowed #3 | field=allowed | present | test_public_api_phase2_part_7.py |
| TC-PUB-7337 | P2 | Response shape allowed #4 | field=allowed | present | test_public_api_phase2_part_7.py |
| TC-PUB-7338 | P2 | Response shape allowed #5 | field=allowed | present | test_public_api_phase2_part_7.py |
| TC-PUB-7339 | P2 | Response shape allowed #6 | field=allowed | present | test_public_api_phase2_part_7.py |
| TC-PUB-7340 | P2 | Response shape allowed #7 | field=allowed | present | test_public_api_phase2_part_7.py |
| TC-PUB-7341 | P2 | Response shape levelUsed #0 | field=levelUsed | present | test_public_api_phase2_part_7.py |
| TC-PUB-7342 | P2 | Response shape levelUsed #1 | field=levelUsed | present | test_public_api_phase2_part_7.py |
| TC-PUB-7343 | P2 | Response shape levelUsed #2 | field=levelUsed | present | test_public_api_phase2_part_7.py |
| TC-PUB-7344 | P2 | Response shape levelUsed #3 | field=levelUsed | present | test_public_api_phase2_part_7.py |
| TC-PUB-7345 | P2 | Response shape levelUsed #4 | field=levelUsed | present | test_public_api_phase2_part_7.py |
| TC-PUB-7346 | P2 | Response shape levelUsed #5 | field=levelUsed | present | test_public_api_phase2_part_7.py |
| TC-PUB-7347 | P2 | Response shape levelUsed #6 | field=levelUsed | present | test_public_api_phase2_part_7.py |
| TC-PUB-7348 | P2 | Response shape levelUsed #7 | field=levelUsed | present | test_public_api_phase2_part_7.py |
| TC-PUB-7349 | P2 | Response shape aiTriggered #0 | field=aiTriggered | present | test_public_api_phase2_part_7.py |
| TC-PUB-7350 | P2 | Response shape aiTriggered #1 | field=aiTriggered | present | test_public_api_phase2_part_7.py |
| TC-PUB-7351 | P2 | Response shape aiTriggered #2 | field=aiTriggered | present | test_public_api_phase2_part_7.py |
| TC-PUB-7352 | P2 | Response shape aiTriggered #3 | field=aiTriggered | present | test_public_api_phase2_part_7.py |
| TC-PUB-7353 | P2 | Response shape aiTriggered #4 | field=aiTriggered | present | test_public_api_phase2_part_7.py |
| TC-PUB-7354 | P2 | Response shape aiTriggered #5 | field=aiTriggered | present | test_public_api_phase2_part_7.py |
| TC-PUB-7355 | P2 | Response shape aiTriggered #6 | field=aiTriggered | present | test_public_api_phase2_part_7.py |
| TC-PUB-7356 | P2 | Response shape aiTriggered #7 | field=aiTriggered | present | test_public_api_phase2_part_7.py |
| TC-PUB-7357 | P2 | Response shape suspicionScore #0 | field=suspicionScore | present | test_public_api_phase2_part_7.py |
| TC-PUB-7358 | P2 | Response shape suspicionScore #1 | field=suspicionScore | present | test_public_api_phase2_part_7.py |
| TC-PUB-7359 | P2 | Response shape suspicionScore #2 | field=suspicionScore | present | test_public_api_phase2_part_7.py |
| TC-PUB-7360 | P2 | Response shape suspicionScore #3 | field=suspicionScore | present | test_public_api_phase2_part_7.py |
| TC-PUB-7361 | P2 | Response shape suspicionScore #4 | field=suspicionScore | present | test_public_api_phase2_part_7.py |
| TC-PUB-7362 | P2 | Response shape suspicionScore #5 | field=suspicionScore | present | test_public_api_phase2_part_7.py |
| TC-PUB-7363 | P2 | Response shape suspicionScore #6 | field=suspicionScore | present | test_public_api_phase2_part_7.py |
| TC-PUB-7364 | P2 | Response shape suspicionScore #7 | field=suspicionScore | present | test_public_api_phase2_part_7.py |
| TC-PUB-7365 | P2 | Response shape reasons #0 | field=reasons | present | test_public_api_phase2_part_7.py |
| TC-PUB-7366 | P2 | Response shape reasons #1 | field=reasons | present | test_public_api_phase2_part_7.py |
| TC-PUB-7367 | P2 | Response shape reasons #2 | field=reasons | present | test_public_api_phase2_part_7.py |
| TC-PUB-7368 | P2 | Response shape reasons #3 | field=reasons | present | test_public_api_phase2_part_7.py |
| TC-PUB-7369 | P2 | Response shape reasons #4 | field=reasons | present | test_public_api_phase2_part_7.py |
| TC-PUB-7370 | P2 | Response shape reasons #5 | field=reasons | present | test_public_api_phase2_part_7.py |
| TC-PUB-7371 | P2 | Response shape reasons #6 | field=reasons | present | test_public_api_phase2_part_7.py |
| TC-PUB-7372 | P2 | Response shape reasons #7 | field=reasons | present | test_public_api_phase2_part_7.py |
| TC-PUB-7373 | P2 | Response shape reason #0 | field=reason | present | test_public_api_phase2_part_7.py |
| TC-PUB-7374 | P2 | Response shape reason #1 | field=reason | present | test_public_api_phase2_part_7.py |
| TC-PUB-7375 | P2 | Response shape reason #2 | field=reason | present | test_public_api_phase2_part_7.py |
| TC-PUB-7376 | P2 | Response shape reason #3 | field=reason | present | test_public_api_phase2_part_7.py |
| TC-PUB-7377 | P2 | Response shape reason #4 | field=reason | present | test_public_api_phase2_part_7.py |
| TC-PUB-7378 | P2 | Response shape reason #5 | field=reason | present | test_public_api_phase2_part_7.py |
| TC-PUB-7379 | P2 | Response shape reason #6 | field=reason | present | test_public_api_phase2_part_7.py |
| TC-PUB-7380 | P2 | Response shape reason #7 | field=reason | present | test_public_api_phase2_part_7.py |
| TC-PUB-7381 | P2 | Response shape matchedWords #0 | field=matchedWords | present | test_public_api_phase2_part_7.py |
| TC-PUB-7382 | P2 | Response shape matchedWords #1 | field=matchedWords | present | test_public_api_phase2_part_7.py |
| TC-PUB-7383 | P2 | Response shape matchedWords #2 | field=matchedWords | present | test_public_api_phase2_part_7.py |
| TC-PUB-7384 | P2 | Response shape matchedWords #3 | field=matchedWords | present | test_public_api_phase2_part_7.py |
| TC-PUB-7385 | P2 | Response shape matchedWords #4 | field=matchedWords | present | test_public_api_phase2_part_7.py |
| TC-PUB-7386 | P2 | Response shape matchedWords #5 | field=matchedWords | present | test_public_api_phase2_part_7.py |
| TC-PUB-7387 | P2 | Response shape matchedWords #6 | field=matchedWords | present | test_public_api_phase2_part_7.py |
| TC-PUB-7388 | P2 | Response shape matchedWords #7 | field=matchedWords | present | test_public_api_phase2_part_7.py |
| TC-PUB-7389 | P2 | Response shape matchedWord #0 | field=matchedWord | present | test_public_api_phase2_part_7.py |
| TC-PUB-7390 | P2 | Response shape matchedWord #1 | field=matchedWord | present | test_public_api_phase2_part_7.py |
| TC-PUB-7391 | P2 | Response shape matchedWord #2 | field=matchedWord | present | test_public_api_phase2_part_7.py |
| TC-PUB-7392 | P2 | Response shape matchedWord #3 | field=matchedWord | present | test_public_api_phase2_part_7.py |
| TC-PUB-7393 | P2 | Response shape matchedWord #4 | field=matchedWord | present | test_public_api_phase2_part_7.py |
| TC-PUB-7394 | P2 | Response shape matchedWord #5 | field=matchedWord | present | test_public_api_phase2_part_7.py |
| TC-PUB-7395 | P2 | Response shape matchedWord #6 | field=matchedWord | present | test_public_api_phase2_part_7.py |
| TC-PUB-7396 | P2 | Response shape matchedWord #7 | field=matchedWord | present | test_public_api_phase2_part_7.py |
| TC-PUB-7397 | P2 | Response shape matchedLanguage #0 | field=matchedLanguage | present | test_public_api_phase2_part_7.py |
| TC-PUB-7398 | P2 | Response shape matchedLanguage #1 | field=matchedLanguage | present | test_public_api_phase2_part_7.py |
| TC-PUB-7399 | P2 | Response shape matchedLanguage #2 | field=matchedLanguage | present | test_public_api_phase2_part_7.py |
| TC-PUB-7400 | P2 | Response shape matchedLanguage #3 | field=matchedLanguage | present | test_public_api_phase2_part_7.py |
| TC-PUB-7401 | P2 | Response shape matchedLanguage #4 | field=matchedLanguage | present | test_public_api_phase2_part_7.py |
| TC-PUB-7402 | P2 | Response shape matchedLanguage #5 | field=matchedLanguage | present | test_public_api_phase2_part_7.py |
| TC-PUB-7403 | P2 | Response shape matchedLanguage #6 | field=matchedLanguage | present | test_public_api_phase2_part_7.py |
| TC-PUB-7404 | P2 | Response shape matchedLanguage #7 | field=matchedLanguage | present | test_public_api_phase2_part_7.py |
| TC-PUB-7405 | P2 | Response shape confidenceScore #0 | field=confidenceScore | present | test_public_api_phase2_part_7.py |
| TC-PUB-7406 | P2 | Response shape confidenceScore #1 | field=confidenceScore | present | test_public_api_phase2_part_7.py |
| TC-PUB-7407 | P2 | Response shape confidenceScore #2 | field=confidenceScore | present | test_public_api_phase2_part_7.py |
| TC-PUB-7408 | P2 | Response shape confidenceScore #3 | field=confidenceScore | present | test_public_api_phase2_part_7.py |
| TC-PUB-7409 | P2 | Response shape confidenceScore #4 | field=confidenceScore | present | test_public_api_phase2_part_7.py |
| TC-PUB-7410 | P2 | Response shape confidenceScore #5 | field=confidenceScore | present | test_public_api_phase2_part_7.py |
| TC-PUB-7411 | P2 | Response shape confidenceScore #6 | field=confidenceScore | present | test_public_api_phase2_part_7.py |
| TC-PUB-7412 | P2 | Response shape confidenceScore #7 | field=confidenceScore | present | test_public_api_phase2_part_7.py |
| TC-PUB-7413 | P2 | Response shape latencyMs #0 | field=latencyMs | present | test_public_api_phase2_part_7.py |
| TC-PUB-7414 | P2 | Response shape latencyMs #1 | field=latencyMs | present | test_public_api_phase2_part_7.py |
| TC-PUB-7415 | P2 | Response shape latencyMs #2 | field=latencyMs | present | test_public_api_phase2_part_7.py |
| TC-PUB-7416 | P2 | Response shape latencyMs #3 | field=latencyMs | present | test_public_api_phase2_part_7.py |

### Phase 3 - 20,000 cases
- Planned sweeps over the full dimension matrix, IDs TC-PUB-0781 onward.

### Phase 4 - 200,000 cases
- Planned high-scale scenarios, IDs TC-PUB-20781 onward.

### Phase 5 - 1,879,220 cases
- Planned exhaustive dimension sweep, IDs TC-PUB-220781 onward.

## Implementation Status
| File | Test Cases | Priority | Status |
| :--- | :--- | :--- | :--- |
| test_public_api_phase2_part_1.py | 6689-6788 | P1 | :white_check_mark: Phase 2 |
| test_public_api_phase2_part_2.py | 6789-6888 | P1 | :white_check_mark: Phase 2 |
| test_public_api_phase2_part_3.py | 6912-7011 | P1 | :white_check_mark: Phase 2 |
| test_public_api_phase2_part_4.py | 7017-7116 | P2 | :white_check_mark: Phase 2 |
| test_public_api_phase2_part_5.py | 7117-7216 | P2 | :white_check_mark: Phase 2 |
| test_public_api_phase2_part_6.py | 7217-7316 | P2 | :white_check_mark: Phase 2 |
| test_public_api_phase2_part_7.py | 7317-7416 | P2 | :white_check_mark: Phase 2 |

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
- API Reference
