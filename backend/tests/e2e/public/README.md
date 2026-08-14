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
| TC-PUB-6848 | P1 | Moderate en clean at 5 | lang=en,len=5 | verdict=PASS | test_public_api_phase2_part_1.py |
| TC-PUB-6849 | P1 | Moderate en clean at 25 | lang=en,len=25 | verdict=PASS | test_public_api_phase2_part_1.py |
| TC-PUB-6850 | P1 | Moderate en clean at 100 | lang=en,len=100 | verdict=PASS | test_public_api_phase2_part_1.py |
| TC-PUB-6851 | P1 | Moderate en clean at 250 | lang=en,len=250 | verdict=PASS | test_public_api_phase2_part_1.py |
| TC-PUB-6852 | P1 | Moderate en clean at 500 | lang=en,len=500 | verdict=PASS | test_public_api_phase2_part_1.py |
| TC-PUB-6853 | P1 | Moderate en clean at 1000 | lang=en,len=1000 | verdict=PASS | test_public_api_phase2_part_1.py |
| TC-PUB-6854 | P1 | Moderate en clean at 2000 | lang=en,len=2000 | verdict=PASS | test_public_api_phase2_part_1.py |
| TC-PUB-6855 | P1 | Moderate en flagged | lang=en | verdict=BLOCK | test_public_api_phase2_part_1.py |
| TC-PUB-6856 | P1 | Moderate zh-CN clean at 5 | lang=zh-CN,len=5 | verdict=PASS | test_public_api_phase2_part_1.py |
| TC-PUB-6857 | P1 | Moderate zh-CN clean at 25 | lang=zh-CN,len=25 | verdict=PASS | test_public_api_phase2_part_1.py |
| TC-PUB-6858 | P1 | Moderate zh-CN clean at 100 | lang=zh-CN,len=100 | verdict=PASS | test_public_api_phase2_part_1.py |
| TC-PUB-6859 | P1 | Moderate zh-CN clean at 250 | lang=zh-CN,len=250 | verdict=PASS | test_public_api_phase2_part_1.py |
| TC-PUB-6860 | P1 | Moderate zh-CN clean at 500 | lang=zh-CN,len=500 | verdict=PASS | test_public_api_phase2_part_1.py |
| TC-PUB-6861 | P1 | Moderate zh-CN clean at 1000 | lang=zh-CN,len=1000 | verdict=PASS | test_public_api_phase2_part_1.py |
| TC-PUB-6862 | P1 | Moderate zh-CN clean at 2000 | lang=zh-CN,len=2000 | verdict=PASS | test_public_api_phase2_part_1.py |
| TC-PUB-6863 | P1 | Moderate zh-CN flagged | lang=zh-CN | verdict=BLOCK | test_public_api_phase2_part_1.py |
| TC-PUB-6864 | P1 | Moderate ja clean at 5 | lang=ja,len=5 | verdict=PASS | test_public_api_phase2_part_1.py |
| TC-PUB-6865 | P1 | Moderate ja clean at 25 | lang=ja,len=25 | verdict=PASS | test_public_api_phase2_part_1.py |
| TC-PUB-6866 | P1 | Moderate ja clean at 100 | lang=ja,len=100 | verdict=PASS | test_public_api_phase2_part_1.py |
| TC-PUB-6867 | P1 | Moderate ja clean at 250 | lang=ja,len=250 | verdict=PASS | test_public_api_phase2_part_1.py |
| TC-PUB-6868 | P1 | Moderate ja clean at 500 | lang=ja,len=500 | verdict=PASS | test_public_api_phase2_part_1.py |
| TC-PUB-6869 | P1 | Moderate ja clean at 1000 | lang=ja,len=1000 | verdict=PASS | test_public_api_phase2_part_1.py |
| TC-PUB-6870 | P1 | Moderate ja clean at 2000 | lang=ja,len=2000 | verdict=PASS | test_public_api_phase2_part_1.py |
| TC-PUB-6871 | P1 | Moderate ja flagged | lang=ja | verdict=BLOCK | test_public_api_phase2_part_1.py |
| TC-PUB-6872 | P1 | Moderate ko clean at 5 | lang=ko,len=5 | verdict=PASS | test_public_api_phase2_part_1.py |
| TC-PUB-6873 | P1 | Moderate ko clean at 25 | lang=ko,len=25 | verdict=PASS | test_public_api_phase2_part_1.py |
| TC-PUB-6874 | P1 | Moderate ko clean at 100 | lang=ko,len=100 | verdict=PASS | test_public_api_phase2_part_1.py |
| TC-PUB-6875 | P1 | Moderate ko clean at 250 | lang=ko,len=250 | verdict=PASS | test_public_api_phase2_part_1.py |
| TC-PUB-6876 | P1 | Moderate ko clean at 500 | lang=ko,len=500 | verdict=PASS | test_public_api_phase2_part_1.py |
| TC-PUB-6877 | P1 | Moderate ko clean at 1000 | lang=ko,len=1000 | verdict=PASS | test_public_api_phase2_part_1.py |
| TC-PUB-6878 | P1 | Moderate ko clean at 2000 | lang=ko,len=2000 | verdict=PASS | test_public_api_phase2_part_1.py |
| TC-PUB-6879 | P1 | Moderate ko flagged | lang=ko | verdict=BLOCK | test_public_api_phase2_part_1.py |
| TC-PUB-6880 | P1 | Moderate ru clean at 5 | lang=ru,len=5 | verdict=PASS | test_public_api_phase2_part_1.py |
| TC-PUB-6881 | P1 | Moderate ru clean at 25 | lang=ru,len=25 | verdict=PASS | test_public_api_phase2_part_1.py |
| TC-PUB-6882 | P1 | Moderate ru clean at 100 | lang=ru,len=100 | verdict=PASS | test_public_api_phase2_part_1.py |
| TC-PUB-6883 | P1 | Moderate ru clean at 250 | lang=ru,len=250 | verdict=PASS | test_public_api_phase2_part_1.py |
| TC-PUB-6884 | P1 | Moderate ru clean at 500 | lang=ru,len=500 | verdict=PASS | test_public_api_phase2_part_1.py |
| TC-PUB-6885 | P1 | Moderate ru clean at 1000 | lang=ru,len=1000 | verdict=PASS | test_public_api_phase2_part_1.py |
| TC-PUB-6886 | P1 | Moderate ru clean at 2000 | lang=ru,len=2000 | verdict=PASS | test_public_api_phase2_part_1.py |
| TC-PUB-6887 | P1 | Moderate ru flagged | lang=ru | verdict=BLOCK | test_public_api_phase2_part_1.py |
| TC-PUB-6888 | P1 | Moderate es clean at 5 | lang=es,len=5 | verdict=PASS | test_public_api_phase2_part_1.py |
| TC-PUB-6889 | P1 | Moderate es clean at 25 | lang=es,len=25 | verdict=PASS | test_public_api_phase2_part_1.py |
| TC-PUB-6890 | P1 | Moderate es clean at 100 | lang=es,len=100 | verdict=PASS | test_public_api_phase2_part_1.py |
| TC-PUB-6891 | P1 | Moderate es clean at 250 | lang=es,len=250 | verdict=PASS | test_public_api_phase2_part_1.py |
| TC-PUB-6892 | P1 | Moderate es clean at 500 | lang=es,len=500 | verdict=PASS | test_public_api_phase2_part_1.py |
| TC-PUB-6893 | P1 | Moderate es clean at 1000 | lang=es,len=1000 | verdict=PASS | test_public_api_phase2_part_1.py |
| TC-PUB-6894 | P1 | Moderate es clean at 2000 | lang=es,len=2000 | verdict=PASS | test_public_api_phase2_part_1.py |
| TC-PUB-6895 | P1 | Moderate es flagged | lang=es | verdict=BLOCK | test_public_api_phase2_part_1.py |
| TC-PUB-6896 | P1 | Moderate fr clean at 5 | lang=fr,len=5 | verdict=PASS | test_public_api_phase2_part_1.py |
| TC-PUB-6897 | P1 | Moderate fr clean at 25 | lang=fr,len=25 | verdict=PASS | test_public_api_phase2_part_1.py |
| TC-PUB-6898 | P1 | Moderate fr clean at 100 | lang=fr,len=100 | verdict=BLOCK | test_public_api_phase2_part_1.py |
| TC-PUB-6899 | P1 | Moderate fr clean at 250 | lang=fr,len=250 | verdict=BLOCK | test_public_api_phase2_part_1.py |
| TC-PUB-6900 | P1 | Moderate fr clean at 500 | lang=fr,len=500 | verdict=BLOCK | test_public_api_phase2_part_1.py |
| TC-PUB-6901 | P1 | Moderate fr clean at 1000 | lang=fr,len=1000 | verdict=BLOCK | test_public_api_phase2_part_1.py |
| TC-PUB-6902 | P1 | Moderate fr clean at 2000 | lang=fr,len=2000 | verdict=BLOCK | test_public_api_phase2_part_1.py |
| TC-PUB-6903 | P1 | Moderate fr flagged | lang=fr | verdict=BLOCK | test_public_api_phase2_part_1.py |
| TC-PUB-6904 | P1 | Moderate de clean at 5 | lang=de,len=5 | verdict=PASS | test_public_api_phase2_part_1.py |
| TC-PUB-6905 | P1 | Moderate de clean at 25 | lang=de,len=25 | verdict=PASS | test_public_api_phase2_part_1.py |
| TC-PUB-6906 | P1 | Moderate de clean at 100 | lang=de,len=100 | verdict=PASS | test_public_api_phase2_part_1.py |
| TC-PUB-6907 | P1 | Moderate de clean at 250 | lang=de,len=250 | verdict=PASS | test_public_api_phase2_part_1.py |
| TC-PUB-6908 | P1 | Moderate de clean at 500 | lang=de,len=500 | verdict=PASS | test_public_api_phase2_part_1.py |
| TC-PUB-6909 | P1 | Moderate de clean at 1000 | lang=de,len=1000 | verdict=PASS | test_public_api_phase2_part_1.py |
| TC-PUB-6910 | P1 | Moderate de clean at 2000 | lang=de,len=2000 | verdict=PASS | test_public_api_phase2_part_1.py |
| TC-PUB-6911 | P1 | Moderate de flagged | lang=de | verdict=BLOCK | test_public_api_phase2_part_1.py |
| TC-PUB-6912 | P1 | Moderate it clean at 5 | lang=it,len=5 | verdict=PASS | test_public_api_phase2_part_1.py |
| TC-PUB-6913 | P1 | Moderate it clean at 25 | lang=it,len=25 | verdict=PASS | test_public_api_phase2_part_1.py |
| TC-PUB-6914 | P1 | Moderate it clean at 100 | lang=it,len=100 | verdict=PASS | test_public_api_phase2_part_1.py |
| TC-PUB-6915 | P1 | Moderate it clean at 250 | lang=it,len=250 | verdict=PASS | test_public_api_phase2_part_1.py |
| TC-PUB-6916 | P1 | Moderate it clean at 500 | lang=it,len=500 | verdict=PASS | test_public_api_phase2_part_1.py |
| TC-PUB-6917 | P1 | Moderate it clean at 1000 | lang=it,len=1000 | verdict=PASS | test_public_api_phase2_part_1.py |
| TC-PUB-6918 | P1 | Moderate it clean at 2000 | lang=it,len=2000 | verdict=PASS | test_public_api_phase2_part_1.py |
| TC-PUB-6919 | P1 | Moderate it flagged | lang=it | verdict=BLOCK | test_public_api_phase2_part_1.py |
| TC-PUB-6920 | P1 | Moderate ar clean at 5 | lang=ar,len=5 | verdict=PASS | test_public_api_phase2_part_1.py |
| TC-PUB-6921 | P1 | Moderate ar clean at 25 | lang=ar,len=25 | verdict=PASS | test_public_api_phase2_part_1.py |
| TC-PUB-6922 | P1 | Moderate ar clean at 100 | lang=ar,len=100 | verdict=PASS | test_public_api_phase2_part_1.py |
| TC-PUB-6923 | P1 | Moderate ar clean at 250 | lang=ar,len=250 | verdict=PASS | test_public_api_phase2_part_1.py |
| TC-PUB-6924 | P1 | Moderate ar clean at 500 | lang=ar,len=500 | verdict=PASS | test_public_api_phase2_part_1.py |
| TC-PUB-6925 | P1 | Moderate ar clean at 1000 | lang=ar,len=1000 | verdict=PASS | test_public_api_phase2_part_1.py |
| TC-PUB-6926 | P1 | Moderate ar clean at 2000 | lang=ar,len=2000 | verdict=PASS | test_public_api_phase2_part_1.py |
| TC-PUB-6927 | P1 | Moderate ar flagged | lang=ar | verdict=PASS | test_public_api_phase2_part_1.py |
| TC-PUB-6928 | P1 | Moderate hi clean at 5 | lang=hi,len=5 | verdict=PASS | test_public_api_phase2_part_1.py |
| TC-PUB-6929 | P1 | Moderate hi clean at 25 | lang=hi,len=25 | verdict=PASS | test_public_api_phase2_part_1.py |
| TC-PUB-6930 | P1 | Moderate hi clean at 100 | lang=hi,len=100 | verdict=PASS | test_public_api_phase2_part_1.py |
| TC-PUB-6931 | P1 | Moderate hi clean at 250 | lang=hi,len=250 | verdict=PASS | test_public_api_phase2_part_1.py |
| TC-PUB-6932 | P1 | Moderate hi clean at 500 | lang=hi,len=500 | verdict=PASS | test_public_api_phase2_part_1.py |
| TC-PUB-6933 | P1 | Moderate hi clean at 1000 | lang=hi,len=1000 | verdict=PASS | test_public_api_phase2_part_1.py |
| TC-PUB-6934 | P1 | Moderate hi clean at 2000 | lang=hi,len=2000 | verdict=PASS | test_public_api_phase2_part_1.py |
| TC-PUB-6935 | P1 | Moderate hi flagged | lang=hi | verdict=BLOCK | test_public_api_phase2_part_1.py |
| TC-PUB-6936 | P1 | Moderate tr clean at 5 | lang=tr,len=5 | verdict=PASS | test_public_api_phase2_part_1.py |
| TC-PUB-6937 | P1 | Moderate tr clean at 25 | lang=tr,len=25 | verdict=PASS | test_public_api_phase2_part_1.py |
| TC-PUB-6938 | P1 | Moderate tr clean at 100 | lang=tr,len=100 | verdict=PASS | test_public_api_phase2_part_1.py |
| TC-PUB-6939 | P1 | Moderate tr clean at 250 | lang=tr,len=250 | verdict=PASS | test_public_api_phase2_part_1.py |
| TC-PUB-6940 | P1 | Moderate tr clean at 500 | lang=tr,len=500 | verdict=PASS | test_public_api_phase2_part_1.py |
| TC-PUB-6941 | P1 | Moderate tr clean at 1000 | lang=tr,len=1000 | verdict=PASS | test_public_api_phase2_part_1.py |
| TC-PUB-6942 | P1 | Moderate tr clean at 2000 | lang=tr,len=2000 | verdict=PASS | test_public_api_phase2_part_1.py |
| TC-PUB-6943 | P1 | Moderate tr flagged | lang=tr | verdict=BLOCK | test_public_api_phase2_part_1.py |
| TC-PUB-6944 | P1 | Moderate pt clean at 5 | lang=pt,len=5 | verdict=PASS | test_public_api_phase2_part_1.py |
| TC-PUB-6945 | P1 | Moderate pt clean at 25 | lang=pt,len=25 | verdict=PASS | test_public_api_phase2_part_1.py |
| TC-PUB-6946 | P1 | Moderate pt clean at 100 | lang=pt,len=100 | verdict=PASS | test_public_api_phase2_part_1.py |
| TC-PUB-6947 | P1 | Moderate pt clean at 250 | lang=pt,len=250 | verdict=PASS | test_public_api_phase2_part_1.py |
| TC-PUB-6948 | P1 | Moderate pt clean at 500 | lang=pt,len=500 | verdict=PASS | test_public_api_phase2_part_2.py |
| TC-PUB-6949 | P1 | Moderate pt clean at 1000 | lang=pt,len=1000 | verdict=PASS | test_public_api_phase2_part_2.py |
| TC-PUB-6950 | P1 | Moderate pt clean at 2000 | lang=pt,len=2000 | verdict=PASS | test_public_api_phase2_part_2.py |
| TC-PUB-6951 | P1 | Moderate pt flagged | lang=pt | verdict=BLOCK | test_public_api_phase2_part_2.py |
| TC-PUB-6952 | P1 | Moderate nl clean at 5 | lang=nl,len=5 | verdict=PASS | test_public_api_phase2_part_2.py |
| TC-PUB-6953 | P1 | Moderate nl clean at 25 | lang=nl,len=25 | verdict=PASS | test_public_api_phase2_part_2.py |
| TC-PUB-6954 | P1 | Moderate nl clean at 100 | lang=nl,len=100 | verdict=PASS | test_public_api_phase2_part_2.py |
| TC-PUB-6955 | P1 | Moderate nl clean at 250 | lang=nl,len=250 | verdict=PASS | test_public_api_phase2_part_2.py |
| TC-PUB-6956 | P1 | Moderate nl clean at 500 | lang=nl,len=500 | verdict=PASS | test_public_api_phase2_part_2.py |
| TC-PUB-6957 | P1 | Moderate nl clean at 1000 | lang=nl,len=1000 | verdict=PASS | test_public_api_phase2_part_2.py |
| TC-PUB-6958 | P1 | Moderate nl clean at 2000 | lang=nl,len=2000 | verdict=PASS | test_public_api_phase2_part_2.py |
| TC-PUB-6959 | P1 | Moderate nl flagged | lang=nl | verdict=BLOCK | test_public_api_phase2_part_2.py |
| TC-PUB-6960 | P1 | Moderate pl clean at 5 | lang=pl,len=5 | verdict=PASS | test_public_api_phase2_part_2.py |
| TC-PUB-6961 | P1 | Moderate pl clean at 25 | lang=pl,len=25 | verdict=PASS | test_public_api_phase2_part_2.py |
| TC-PUB-6962 | P1 | Moderate pl clean at 100 | lang=pl,len=100 | verdict=PASS | test_public_api_phase2_part_2.py |
| TC-PUB-6963 | P1 | Moderate pl clean at 250 | lang=pl,len=250 | verdict=PASS | test_public_api_phase2_part_2.py |
| TC-PUB-6964 | P1 | Moderate pl clean at 500 | lang=pl,len=500 | verdict=PASS | test_public_api_phase2_part_2.py |
| TC-PUB-6965 | P1 | Moderate pl clean at 1000 | lang=pl,len=1000 | verdict=PASS | test_public_api_phase2_part_2.py |
| TC-PUB-6966 | P1 | Moderate pl clean at 2000 | lang=pl,len=2000 | verdict=PASS | test_public_api_phase2_part_2.py |
| TC-PUB-6967 | P1 | Moderate pl flagged | lang=pl | verdict=BLOCK | test_public_api_phase2_part_2.py |
| TC-PUB-6968 | P1 | Moderate uk clean at 5 | lang=uk,len=5 | verdict=PASS | test_public_api_phase2_part_2.py |
| TC-PUB-6969 | P1 | Moderate uk clean at 25 | lang=uk,len=25 | verdict=PASS | test_public_api_phase2_part_2.py |
| TC-PUB-6970 | P1 | Moderate uk clean at 100 | lang=uk,len=100 | verdict=PASS | test_public_api_phase2_part_2.py |
| TC-PUB-6971 | P1 | Moderate uk clean at 250 | lang=uk,len=250 | verdict=PASS | test_public_api_phase2_part_2.py |
| TC-PUB-6972 | P1 | Moderate uk clean at 500 | lang=uk,len=500 | verdict=PASS | test_public_api_phase2_part_2.py |
| TC-PUB-6973 | P1 | Moderate uk clean at 1000 | lang=uk,len=1000 | verdict=PASS | test_public_api_phase2_part_2.py |
| TC-PUB-6974 | P1 | Moderate uk clean at 2000 | lang=uk,len=2000 | verdict=PASS | test_public_api_phase2_part_2.py |
| TC-PUB-6975 | P1 | Moderate uk flagged | lang=uk | verdict=PASS | test_public_api_phase2_part_2.py |
| TC-PUB-6976 | P1 | Moderate cs clean at 5 | lang=cs,len=5 | verdict=PASS | test_public_api_phase2_part_2.py |
| TC-PUB-6977 | P1 | Moderate cs clean at 25 | lang=cs,len=25 | verdict=PASS | test_public_api_phase2_part_2.py |
| TC-PUB-6978 | P1 | Moderate cs clean at 100 | lang=cs,len=100 | verdict=PASS | test_public_api_phase2_part_2.py |
| TC-PUB-6979 | P1 | Moderate cs clean at 250 | lang=cs,len=250 | verdict=PASS | test_public_api_phase2_part_2.py |
| TC-PUB-6980 | P1 | Moderate cs clean at 500 | lang=cs,len=500 | verdict=PASS | test_public_api_phase2_part_2.py |
| TC-PUB-6981 | P1 | Moderate cs clean at 1000 | lang=cs,len=1000 | verdict=PASS | test_public_api_phase2_part_2.py |
| TC-PUB-6982 | P1 | Moderate cs clean at 2000 | lang=cs,len=2000 | verdict=PASS | test_public_api_phase2_part_2.py |
| TC-PUB-6983 | P1 | Moderate cs flagged | lang=cs | verdict=BLOCK | test_public_api_phase2_part_2.py |
| TC-PUB-6984 | P1 | Moderate el clean at 5 | lang=el,len=5 | verdict=PASS | test_public_api_phase2_part_2.py |
| TC-PUB-6985 | P1 | Moderate el clean at 25 | lang=el,len=25 | verdict=PASS | test_public_api_phase2_part_2.py |
| TC-PUB-6986 | P1 | Moderate el clean at 100 | lang=el,len=100 | verdict=PASS | test_public_api_phase2_part_2.py |
| TC-PUB-6987 | P1 | Moderate el clean at 250 | lang=el,len=250 | verdict=PASS | test_public_api_phase2_part_2.py |
| TC-PUB-6988 | P1 | Moderate el clean at 500 | lang=el,len=500 | verdict=PASS | test_public_api_phase2_part_2.py |
| TC-PUB-6989 | P1 | Moderate el clean at 1000 | lang=el,len=1000 | verdict=PASS | test_public_api_phase2_part_2.py |
| TC-PUB-6990 | P1 | Moderate el clean at 2000 | lang=el,len=2000 | verdict=PASS | test_public_api_phase2_part_2.py |
| TC-PUB-6991 | P1 | Moderate el flagged | lang=el | verdict=BLOCK | test_public_api_phase2_part_2.py |
| TC-PUB-6992 | P1 | Moderate sv clean at 5 | lang=sv,len=5 | verdict=PASS | test_public_api_phase2_part_2.py |
| TC-PUB-6993 | P1 | Moderate sv clean at 25 | lang=sv,len=25 | verdict=PASS | test_public_api_phase2_part_2.py |
| TC-PUB-6994 | P1 | Moderate sv clean at 100 | lang=sv,len=100 | verdict=PASS | test_public_api_phase2_part_2.py |
| TC-PUB-6995 | P1 | Moderate sv clean at 250 | lang=sv,len=250 | verdict=PASS | test_public_api_phase2_part_2.py |
| TC-PUB-6996 | P1 | Moderate sv clean at 500 | lang=sv,len=500 | verdict=PASS | test_public_api_phase2_part_2.py |
| TC-PUB-6997 | P1 | Moderate sv clean at 1000 | lang=sv,len=1000 | verdict=PASS | test_public_api_phase2_part_2.py |
| TC-PUB-6998 | P1 | Moderate sv clean at 2000 | lang=sv,len=2000 | verdict=PASS | test_public_api_phase2_part_2.py |
| TC-PUB-6999 | P1 | Moderate sv flagged | lang=sv | verdict=BLOCK | test_public_api_phase2_part_2.py |
| TC-PUB-7000 | P1 | Moderate no clean at 5 | lang=no,len=5 | verdict=PASS | test_public_api_phase2_part_2.py |
| TC-PUB-7001 | P1 | Moderate no clean at 25 | lang=no,len=25 | verdict=PASS | test_public_api_phase2_part_2.py |
| TC-PUB-7002 | P1 | Moderate no clean at 100 | lang=no,len=100 | verdict=PASS | test_public_api_phase2_part_2.py |
| TC-PUB-7003 | P1 | Moderate no clean at 250 | lang=no,len=250 | verdict=PASS | test_public_api_phase2_part_2.py |
| TC-PUB-7004 | P1 | Moderate no clean at 500 | lang=no,len=500 | verdict=PASS | test_public_api_phase2_part_2.py |
| TC-PUB-7005 | P1 | Moderate no clean at 1000 | lang=no,len=1000 | verdict=PASS | test_public_api_phase2_part_2.py |
| TC-PUB-7006 | P1 | Moderate no clean at 2000 | lang=no,len=2000 | verdict=PASS | test_public_api_phase2_part_2.py |
| TC-PUB-7007 | P1 | Moderate no flagged | lang=no | verdict=BLOCK | test_public_api_phase2_part_2.py |
| TC-PUB-7008 | P1 | Moderate da clean at 5 | lang=da,len=5 | verdict=PASS | test_public_api_phase2_part_2.py |
| TC-PUB-7009 | P1 | Moderate da clean at 25 | lang=da,len=25 | verdict=PASS | test_public_api_phase2_part_2.py |
| TC-PUB-7010 | P1 | Moderate da clean at 100 | lang=da,len=100 | verdict=PASS | test_public_api_phase2_part_2.py |
| TC-PUB-7011 | P1 | Moderate da clean at 250 | lang=da,len=250 | verdict=PASS | test_public_api_phase2_part_2.py |
| TC-PUB-7012 | P1 | Moderate da clean at 500 | lang=da,len=500 | verdict=PASS | test_public_api_phase2_part_2.py |
| TC-PUB-7013 | P1 | Moderate da clean at 1000 | lang=da,len=1000 | verdict=PASS | test_public_api_phase2_part_2.py |
| TC-PUB-7014 | P1 | Moderate da clean at 2000 | lang=da,len=2000 | verdict=PASS | test_public_api_phase2_part_2.py |
| TC-PUB-7015 | P1 | Moderate da flagged | lang=da | verdict=PASS | test_public_api_phase2_part_2.py |
| TC-PUB-7016 | P1 | Moderate fi clean at 5 | lang=fi,len=5 | verdict=PASS | test_public_api_phase2_part_2.py |
| TC-PUB-7017 | P1 | Moderate fi clean at 25 | lang=fi,len=25 | verdict=PASS | test_public_api_phase2_part_2.py |
| TC-PUB-7018 | P1 | Moderate fi clean at 100 | lang=fi,len=100 | verdict=PASS | test_public_api_phase2_part_2.py |
| TC-PUB-7019 | P1 | Moderate fi clean at 250 | lang=fi,len=250 | verdict=PASS | test_public_api_phase2_part_2.py |
| TC-PUB-7020 | P1 | Moderate fi clean at 500 | lang=fi,len=500 | verdict=PASS | test_public_api_phase2_part_2.py |
| TC-PUB-7021 | P1 | Moderate fi clean at 1000 | lang=fi,len=1000 | verdict=PASS | test_public_api_phase2_part_2.py |
| TC-PUB-7022 | P1 | Moderate fi clean at 2000 | lang=fi,len=2000 | verdict=PASS | test_public_api_phase2_part_2.py |
| TC-PUB-7023 | P1 | Moderate fi flagged | lang=fi | verdict=BLOCK | test_public_api_phase2_part_2.py |
| TC-PUB-7024 | P1 | Moderate hu clean at 5 | lang=hu,len=5 | verdict=PASS | test_public_api_phase2_part_2.py |
| TC-PUB-7025 | P1 | Moderate hu clean at 25 | lang=hu,len=25 | verdict=PASS | test_public_api_phase2_part_2.py |
| TC-PUB-7026 | P1 | Moderate hu clean at 100 | lang=hu,len=100 | verdict=PASS | test_public_api_phase2_part_2.py |
| TC-PUB-7027 | P1 | Moderate hu clean at 250 | lang=hu,len=250 | verdict=PASS | test_public_api_phase2_part_2.py |
| TC-PUB-7028 | P1 | Moderate hu clean at 500 | lang=hu,len=500 | verdict=PASS | test_public_api_phase2_part_2.py |
| TC-PUB-7029 | P1 | Moderate hu clean at 1000 | lang=hu,len=1000 | verdict=PASS | test_public_api_phase2_part_2.py |
| TC-PUB-7030 | P1 | Moderate hu clean at 2000 | lang=hu,len=2000 | verdict=PASS | test_public_api_phase2_part_2.py |
| TC-PUB-7031 | P1 | Moderate hu flagged | lang=hu | verdict=PASS | test_public_api_phase2_part_2.py |
| TC-PUB-7032 | P1 | Moderate ro clean at 5 | lang=ro,len=5 | verdict=PASS | test_public_api_phase2_part_2.py |
| TC-PUB-7033 | P1 | Moderate ro clean at 25 | lang=ro,len=25 | verdict=PASS | test_public_api_phase2_part_2.py |
| TC-PUB-7034 | P1 | Moderate ro clean at 100 | lang=ro,len=100 | verdict=PASS | test_public_api_phase2_part_2.py |
| TC-PUB-7035 | P1 | Moderate ro clean at 250 | lang=ro,len=250 | verdict=PASS | test_public_api_phase2_part_2.py |
| TC-PUB-7036 | P1 | Moderate ro clean at 500 | lang=ro,len=500 | verdict=PASS | test_public_api_phase2_part_2.py |
| TC-PUB-7037 | P1 | Moderate ro clean at 1000 | lang=ro,len=1000 | verdict=PASS | test_public_api_phase2_part_2.py |
| TC-PUB-7038 | P1 | Moderate ro clean at 2000 | lang=ro,len=2000 | verdict=PASS | test_public_api_phase2_part_2.py |
| TC-PUB-7039 | P1 | Moderate ro flagged | lang=ro | verdict=BLOCK | test_public_api_phase2_part_2.py |
| TC-PUB-7040 | P1 | Moderate bg clean at 5 | lang=bg,len=5 | verdict=PASS | test_public_api_phase2_part_2.py |
| TC-PUB-7041 | P1 | Moderate bg clean at 25 | lang=bg,len=25 | verdict=PASS | test_public_api_phase2_part_2.py |
| TC-PUB-7042 | P1 | Moderate bg clean at 100 | lang=bg,len=100 | verdict=PASS | test_public_api_phase2_part_2.py |
| TC-PUB-7043 | P1 | Moderate bg clean at 250 | lang=bg,len=250 | verdict=PASS | test_public_api_phase2_part_2.py |
| TC-PUB-7044 | P1 | Moderate bg clean at 500 | lang=bg,len=500 | verdict=PASS | test_public_api_phase2_part_2.py |
| TC-PUB-7045 | P1 | Moderate bg clean at 1000 | lang=bg,len=1000 | verdict=PASS | test_public_api_phase2_part_2.py |
| TC-PUB-7046 | P1 | Moderate bg clean at 2000 | lang=bg,len=2000 | verdict=PASS | test_public_api_phase2_part_2.py |
| TC-PUB-7047 | P1 | Moderate bg flagged | lang=bg | verdict=PASS | test_public_api_phase2_part_2.py |
| TC-PUB-7071 | P1 | Batch size 2 scenario 0 | size=2,scenario=0 | all results | test_public_api_phase2_part_3.py |
| TC-PUB-7072 | P1 | Batch size 2 scenario 1 | size=2,scenario=1 | all results | test_public_api_phase2_part_3.py |
| TC-PUB-7073 | P1 | Batch size 2 scenario 2 | size=2,scenario=2 | all results | test_public_api_phase2_part_3.py |
| TC-PUB-7074 | P1 | Batch size 2 scenario 3 | size=2,scenario=3 | all results | test_public_api_phase2_part_3.py |
| TC-PUB-7075 | P1 | Batch size 2 scenario 4 | size=2,scenario=4 | all results | test_public_api_phase2_part_3.py |
| TC-PUB-7076 | P1 | Batch size 2 scenario 5 | size=2,scenario=5 | all results | test_public_api_phase2_part_3.py |
| TC-PUB-7077 | P1 | Batch size 2 scenario 6 | size=2,scenario=6 | all results | test_public_api_phase2_part_3.py |
| TC-PUB-7078 | P1 | Batch size 2 scenario 7 | size=2,scenario=7 | all results | test_public_api_phase2_part_3.py |
| TC-PUB-7079 | P1 | Batch size 2 scenario 8 | size=2,scenario=8 | all results | test_public_api_phase2_part_3.py |
| TC-PUB-7080 | P1 | Batch size 2 scenario 9 | size=2,scenario=9 | all results | test_public_api_phase2_part_3.py |
| TC-PUB-7081 | P1 | Batch size 2 scenario 10 | size=2,scenario=10 | all results | test_public_api_phase2_part_3.py |
| TC-PUB-7082 | P1 | Batch size 2 scenario 11 | size=2,scenario=11 | all results | test_public_api_phase2_part_3.py |
| TC-PUB-7083 | P1 | Batch size 2 scenario 12 | size=2,scenario=12 | all results | test_public_api_phase2_part_3.py |
| TC-PUB-7084 | P1 | Batch size 2 scenario 13 | size=2,scenario=13 | all results | test_public_api_phase2_part_3.py |
| TC-PUB-7085 | P1 | Batch size 2 scenario 14 | size=2,scenario=14 | all results | test_public_api_phase2_part_3.py |
| TC-PUB-7086 | P1 | Batch size 5 scenario 0 | size=5,scenario=0 | all results | test_public_api_phase2_part_3.py |
| TC-PUB-7087 | P1 | Batch size 5 scenario 1 | size=5,scenario=1 | all results | test_public_api_phase2_part_3.py |
| TC-PUB-7088 | P1 | Batch size 5 scenario 2 | size=5,scenario=2 | all results | test_public_api_phase2_part_3.py |
| TC-PUB-7089 | P1 | Batch size 5 scenario 3 | size=5,scenario=3 | all results | test_public_api_phase2_part_3.py |
| TC-PUB-7090 | P1 | Batch size 5 scenario 4 | size=5,scenario=4 | all results | test_public_api_phase2_part_3.py |
| TC-PUB-7091 | P1 | Batch size 5 scenario 5 | size=5,scenario=5 | all results | test_public_api_phase2_part_3.py |
| TC-PUB-7092 | P1 | Batch size 5 scenario 6 | size=5,scenario=6 | all results | test_public_api_phase2_part_3.py |
| TC-PUB-7093 | P1 | Batch size 5 scenario 7 | size=5,scenario=7 | all results | test_public_api_phase2_part_3.py |
| TC-PUB-7094 | P1 | Batch size 5 scenario 8 | size=5,scenario=8 | all results | test_public_api_phase2_part_3.py |
| TC-PUB-7095 | P1 | Batch size 5 scenario 9 | size=5,scenario=9 | all results | test_public_api_phase2_part_3.py |
| TC-PUB-7096 | P1 | Batch size 5 scenario 10 | size=5,scenario=10 | all results | test_public_api_phase2_part_3.py |
| TC-PUB-7097 | P1 | Batch size 5 scenario 11 | size=5,scenario=11 | all results | test_public_api_phase2_part_3.py |
| TC-PUB-7098 | P1 | Batch size 5 scenario 12 | size=5,scenario=12 | all results | test_public_api_phase2_part_3.py |
| TC-PUB-7099 | P1 | Batch size 5 scenario 13 | size=5,scenario=13 | all results | test_public_api_phase2_part_3.py |
| TC-PUB-7100 | P1 | Batch size 5 scenario 14 | size=5,scenario=14 | all results | test_public_api_phase2_part_3.py |
| TC-PUB-7101 | P1 | Batch size 10 scenario 0 | size=10,scenario=0 | all results | test_public_api_phase2_part_3.py |
| TC-PUB-7102 | P1 | Batch size 10 scenario 1 | size=10,scenario=1 | all results | test_public_api_phase2_part_3.py |
| TC-PUB-7103 | P1 | Batch size 10 scenario 2 | size=10,scenario=2 | all results | test_public_api_phase2_part_3.py |
| TC-PUB-7104 | P1 | Batch size 10 scenario 3 | size=10,scenario=3 | all results | test_public_api_phase2_part_3.py |
| TC-PUB-7105 | P1 | Batch size 10 scenario 4 | size=10,scenario=4 | all results | test_public_api_phase2_part_3.py |
| TC-PUB-7106 | P1 | Batch size 10 scenario 5 | size=10,scenario=5 | all results | test_public_api_phase2_part_3.py |
| TC-PUB-7107 | P1 | Batch size 10 scenario 6 | size=10,scenario=6 | all results | test_public_api_phase2_part_3.py |
| TC-PUB-7108 | P1 | Batch size 10 scenario 7 | size=10,scenario=7 | all results | test_public_api_phase2_part_3.py |
| TC-PUB-7109 | P1 | Batch size 10 scenario 8 | size=10,scenario=8 | all results | test_public_api_phase2_part_3.py |
| TC-PUB-7110 | P1 | Batch size 10 scenario 9 | size=10,scenario=9 | all results | test_public_api_phase2_part_3.py |
| TC-PUB-7111 | P1 | Batch size 10 scenario 10 | size=10,scenario=10 | all results | test_public_api_phase2_part_3.py |
| TC-PUB-7112 | P1 | Batch size 10 scenario 11 | size=10,scenario=11 | all results | test_public_api_phase2_part_3.py |
| TC-PUB-7113 | P1 | Batch size 10 scenario 12 | size=10,scenario=12 | all results | test_public_api_phase2_part_3.py |
| TC-PUB-7114 | P1 | Batch size 10 scenario 13 | size=10,scenario=13 | all results | test_public_api_phase2_part_3.py |
| TC-PUB-7115 | P1 | Batch size 10 scenario 14 | size=10,scenario=14 | all results | test_public_api_phase2_part_3.py |
| TC-PUB-7116 | P1 | Batch size 25 scenario 0 | size=25,scenario=0 | all results | test_public_api_phase2_part_3.py |
| TC-PUB-7117 | P1 | Batch size 25 scenario 1 | size=25,scenario=1 | all results | test_public_api_phase2_part_3.py |
| TC-PUB-7118 | P1 | Batch size 25 scenario 2 | size=25,scenario=2 | all results | test_public_api_phase2_part_3.py |
| TC-PUB-7119 | P1 | Batch size 25 scenario 3 | size=25,scenario=3 | all results | test_public_api_phase2_part_3.py |
| TC-PUB-7120 | P1 | Batch size 25 scenario 4 | size=25,scenario=4 | all results | test_public_api_phase2_part_3.py |
| TC-PUB-7121 | P1 | Batch size 25 scenario 5 | size=25,scenario=5 | all results | test_public_api_phase2_part_3.py |
| TC-PUB-7122 | P1 | Batch size 25 scenario 6 | size=25,scenario=6 | all results | test_public_api_phase2_part_3.py |
| TC-PUB-7123 | P1 | Batch size 25 scenario 7 | size=25,scenario=7 | all results | test_public_api_phase2_part_3.py |
| TC-PUB-7124 | P1 | Batch size 25 scenario 8 | size=25,scenario=8 | all results | test_public_api_phase2_part_3.py |
| TC-PUB-7125 | P1 | Batch size 25 scenario 9 | size=25,scenario=9 | all results | test_public_api_phase2_part_3.py |
| TC-PUB-7126 | P1 | Batch size 25 scenario 10 | size=25,scenario=10 | all results | test_public_api_phase2_part_3.py |
| TC-PUB-7127 | P1 | Batch size 25 scenario 11 | size=25,scenario=11 | all results | test_public_api_phase2_part_3.py |
| TC-PUB-7128 | P1 | Batch size 25 scenario 12 | size=25,scenario=12 | all results | test_public_api_phase2_part_3.py |
| TC-PUB-7129 | P1 | Batch size 25 scenario 13 | size=25,scenario=13 | all results | test_public_api_phase2_part_3.py |
| TC-PUB-7130 | P1 | Batch size 25 scenario 14 | size=25,scenario=14 | all results | test_public_api_phase2_part_3.py |
| TC-PUB-7131 | P1 | Batch size 50 scenario 0 | size=50,scenario=0 | all results | test_public_api_phase2_part_3.py |
| TC-PUB-7132 | P1 | Batch size 50 scenario 1 | size=50,scenario=1 | all results | test_public_api_phase2_part_3.py |
| TC-PUB-7133 | P1 | Batch size 50 scenario 2 | size=50,scenario=2 | all results | test_public_api_phase2_part_3.py |
| TC-PUB-7134 | P1 | Batch size 50 scenario 3 | size=50,scenario=3 | all results | test_public_api_phase2_part_3.py |
| TC-PUB-7135 | P1 | Batch size 50 scenario 4 | size=50,scenario=4 | all results | test_public_api_phase2_part_3.py |
| TC-PUB-7136 | P1 | Batch size 50 scenario 5 | size=50,scenario=5 | all results | test_public_api_phase2_part_3.py |
| TC-PUB-7137 | P1 | Batch size 50 scenario 6 | size=50,scenario=6 | all results | test_public_api_phase2_part_3.py |
| TC-PUB-7138 | P1 | Batch size 50 scenario 7 | size=50,scenario=7 | all results | test_public_api_phase2_part_3.py |
| TC-PUB-7139 | P1 | Batch size 50 scenario 8 | size=50,scenario=8 | all results | test_public_api_phase2_part_3.py |
| TC-PUB-7140 | P1 | Batch size 50 scenario 9 | size=50,scenario=9 | all results | test_public_api_phase2_part_3.py |
| TC-PUB-7141 | P1 | Batch size 50 scenario 10 | size=50,scenario=10 | all results | test_public_api_phase2_part_3.py |
| TC-PUB-7142 | P1 | Batch size 50 scenario 11 | size=50,scenario=11 | all results | test_public_api_phase2_part_3.py |
| TC-PUB-7143 | P1 | Batch size 50 scenario 12 | size=50,scenario=12 | all results | test_public_api_phase2_part_3.py |
| TC-PUB-7144 | P1 | Batch size 50 scenario 13 | size=50,scenario=13 | all results | test_public_api_phase2_part_3.py |
| TC-PUB-7145 | P1 | Batch size 50 scenario 14 | size=50,scenario=14 | all results | test_public_api_phase2_part_3.py |
| TC-PUB-7146 | P1 | Batch size 75 scenario 0 | size=75,scenario=0 | all results | test_public_api_phase2_part_3.py |
| TC-PUB-7147 | P1 | Batch size 75 scenario 1 | size=75,scenario=1 | all results | test_public_api_phase2_part_3.py |
| TC-PUB-7148 | P1 | Batch size 75 scenario 2 | size=75,scenario=2 | all results | test_public_api_phase2_part_3.py |
| TC-PUB-7149 | P1 | Batch size 75 scenario 3 | size=75,scenario=3 | all results | test_public_api_phase2_part_3.py |
| TC-PUB-7150 | P1 | Batch size 75 scenario 4 | size=75,scenario=4 | all results | test_public_api_phase2_part_3.py |
| TC-PUB-7151 | P1 | Batch size 75 scenario 5 | size=75,scenario=5 | all results | test_public_api_phase2_part_3.py |
| TC-PUB-7152 | P1 | Batch size 75 scenario 6 | size=75,scenario=6 | all results | test_public_api_phase2_part_3.py |
| TC-PUB-7153 | P1 | Batch size 75 scenario 7 | size=75,scenario=7 | all results | test_public_api_phase2_part_3.py |
| TC-PUB-7154 | P1 | Batch size 75 scenario 8 | size=75,scenario=8 | all results | test_public_api_phase2_part_3.py |
| TC-PUB-7155 | P1 | Batch size 75 scenario 9 | size=75,scenario=9 | all results | test_public_api_phase2_part_3.py |
| TC-PUB-7156 | P1 | Batch size 75 scenario 10 | size=75,scenario=10 | all results | test_public_api_phase2_part_3.py |
| TC-PUB-7157 | P1 | Batch size 75 scenario 11 | size=75,scenario=11 | all results | test_public_api_phase2_part_3.py |
| TC-PUB-7158 | P1 | Batch size 75 scenario 12 | size=75,scenario=12 | all results | test_public_api_phase2_part_3.py |
| TC-PUB-7159 | P1 | Batch size 75 scenario 13 | size=75,scenario=13 | all results | test_public_api_phase2_part_3.py |
| TC-PUB-7160 | P1 | Batch size 75 scenario 14 | size=75,scenario=14 | all results | test_public_api_phase2_part_3.py |
| TC-PUB-7161 | P1 | Batch size 100 scenario 0 | size=100,scenario=0 | all results | test_public_api_phase2_part_3.py |
| TC-PUB-7162 | P1 | Batch size 100 scenario 1 | size=100,scenario=1 | all results | test_public_api_phase2_part_3.py |
| TC-PUB-7163 | P1 | Batch size 100 scenario 2 | size=100,scenario=2 | all results | test_public_api_phase2_part_3.py |
| TC-PUB-7164 | P1 | Batch size 100 scenario 3 | size=100,scenario=3 | all results | test_public_api_phase2_part_3.py |
| TC-PUB-7165 | P1 | Batch size 100 scenario 4 | size=100,scenario=4 | all results | test_public_api_phase2_part_3.py |
| TC-PUB-7166 | P1 | Batch size 100 scenario 5 | size=100,scenario=5 | all results | test_public_api_phase2_part_3.py |
| TC-PUB-7167 | P1 | Batch size 100 scenario 6 | size=100,scenario=6 | all results | test_public_api_phase2_part_3.py |
| TC-PUB-7168 | P1 | Batch size 100 scenario 7 | size=100,scenario=7 | all results | test_public_api_phase2_part_3.py |
| TC-PUB-7169 | P1 | Batch size 100 scenario 8 | size=100,scenario=8 | all results | test_public_api_phase2_part_3.py |
| TC-PUB-7170 | P1 | Batch size 100 scenario 9 | size=100,scenario=9 | all results | test_public_api_phase2_part_3.py |
| TC-PUB-7176 | P2 | Validation over-limit text length 8193 | case=over-limit:8193 | rejected cleanly | test_public_api_phase2_part_4.py |
| TC-PUB-7177 | P2 | Validation over-limit text length 8194 | case=over-limit:8194 | rejected cleanly | test_public_api_phase2_part_4.py |
| TC-PUB-7178 | P2 | Validation over-limit text length 8195 | case=over-limit:8195 | rejected cleanly | test_public_api_phase2_part_4.py |
| TC-PUB-7179 | P2 | Validation over-limit text length 8196 | case=over-limit:8196 | rejected cleanly | test_public_api_phase2_part_4.py |
| TC-PUB-7180 | P2 | Validation over-limit text length 8197 | case=over-limit:8197 | rejected cleanly | test_public_api_phase2_part_4.py |
| TC-PUB-7181 | P2 | Validation over-limit text length 8198 | case=over-limit:8198 | rejected cleanly | test_public_api_phase2_part_4.py |
| TC-PUB-7182 | P2 | Validation over-limit text length 8199 | case=over-limit:8199 | rejected cleanly | test_public_api_phase2_part_4.py |
| TC-PUB-7183 | P2 | Validation over-limit text length 8200 | case=over-limit:8200 | rejected cleanly | test_public_api_phase2_part_4.py |
| TC-PUB-7184 | P2 | Validation over-limit text length 8201 | case=over-limit:8201 | rejected cleanly | test_public_api_phase2_part_4.py |
| TC-PUB-7185 | P2 | Validation over-limit text length 8202 | case=over-limit:8202 | rejected cleanly | test_public_api_phase2_part_4.py |
| TC-PUB-7186 | P2 | Validation over-limit text length 8203 | case=over-limit:8203 | rejected cleanly | test_public_api_phase2_part_4.py |
| TC-PUB-7187 | P2 | Validation over-limit text length 8204 | case=over-limit:8204 | rejected cleanly | test_public_api_phase2_part_4.py |
| TC-PUB-7188 | P2 | Validation over-limit text length 8205 | case=over-limit:8205 | rejected cleanly | test_public_api_phase2_part_4.py |
| TC-PUB-7189 | P2 | Validation over-limit text length 8206 | case=over-limit:8206 | rejected cleanly | test_public_api_phase2_part_4.py |
| TC-PUB-7190 | P2 | Validation over-limit text length 8207 | case=over-limit:8207 | rejected cleanly | test_public_api_phase2_part_4.py |
| TC-PUB-7191 | P2 | Validation over-limit text length 8208 | case=over-limit:8208 | rejected cleanly | test_public_api_phase2_part_4.py |
| TC-PUB-7192 | P2 | Validation over-limit text length 8209 | case=over-limit:8209 | rejected cleanly | test_public_api_phase2_part_4.py |
| TC-PUB-7193 | P2 | Validation over-limit text length 8210 | case=over-limit:8210 | rejected cleanly | test_public_api_phase2_part_4.py |
| TC-PUB-7194 | P2 | Validation over-limit text length 8211 | case=over-limit:8211 | rejected cleanly | test_public_api_phase2_part_4.py |
| TC-PUB-7195 | P2 | Validation over-limit text length 8212 | case=over-limit:8212 | rejected cleanly | test_public_api_phase2_part_4.py |
| TC-PUB-7196 | P2 | Validation over-limit text length 8213 | case=over-limit:8213 | rejected cleanly | test_public_api_phase2_part_4.py |
| TC-PUB-7197 | P2 | Validation over-limit text length 8214 | case=over-limit:8214 | rejected cleanly | test_public_api_phase2_part_4.py |
| TC-PUB-7198 | P2 | Validation over-limit text length 8215 | case=over-limit:8215 | rejected cleanly | test_public_api_phase2_part_4.py |
| TC-PUB-7199 | P2 | Validation over-limit text length 8216 | case=over-limit:8216 | rejected cleanly | test_public_api_phase2_part_4.py |
| TC-PUB-7200 | P2 | Validation over-limit text length 8217 | case=over-limit:8217 | rejected cleanly | test_public_api_phase2_part_4.py |
| TC-PUB-7201 | P2 | Validation over-limit text length 8218 | case=over-limit:8218 | rejected cleanly | test_public_api_phase2_part_4.py |
| TC-PUB-7202 | P2 | Validation over-limit text length 8219 | case=over-limit:8219 | rejected cleanly | test_public_api_phase2_part_4.py |
| TC-PUB-7203 | P2 | Validation over-limit text length 8220 | case=over-limit:8220 | rejected cleanly | test_public_api_phase2_part_4.py |
| TC-PUB-7204 | P2 | Validation over-limit text length 8221 | case=over-limit:8221 | rejected cleanly | test_public_api_phase2_part_4.py |
| TC-PUB-7205 | P2 | Validation over-limit text length 8222 | case=over-limit:8222 | rejected cleanly | test_public_api_phase2_part_4.py |
| TC-PUB-7206 | P2 | Validation over-limit text length 8223 | case=over-limit:8223 | rejected cleanly | test_public_api_phase2_part_4.py |
| TC-PUB-7207 | P2 | Validation over-limit text length 8224 | case=over-limit:8224 | rejected cleanly | test_public_api_phase2_part_4.py |
| TC-PUB-7208 | P2 | Validation over-limit text length 8225 | case=over-limit:8225 | rejected cleanly | test_public_api_phase2_part_4.py |
| TC-PUB-7209 | P2 | Validation over-limit text length 8226 | case=over-limit:8226 | rejected cleanly | test_public_api_phase2_part_4.py |
| TC-PUB-7210 | P2 | Validation over-limit text length 8227 | case=over-limit:8227 | rejected cleanly | test_public_api_phase2_part_4.py |
| TC-PUB-7211 | P2 | Validation over-limit text length 8228 | case=over-limit:8228 | rejected cleanly | test_public_api_phase2_part_4.py |
| TC-PUB-7212 | P2 | Validation over-limit text length 8229 | case=over-limit:8229 | rejected cleanly | test_public_api_phase2_part_4.py |
| TC-PUB-7213 | P2 | Validation over-limit text length 8230 | case=over-limit:8230 | rejected cleanly | test_public_api_phase2_part_4.py |
| TC-PUB-7214 | P2 | Validation over-limit text length 8231 | case=over-limit:8231 | rejected cleanly | test_public_api_phase2_part_4.py |
| TC-PUB-7215 | P2 | Validation over-limit text length 8232 | case=over-limit:8232 | rejected cleanly | test_public_api_phase2_part_4.py |
| TC-PUB-7216 | P2 | Validation over-limit text length 8233 | case=over-limit:8233 | rejected cleanly | test_public_api_phase2_part_4.py |
| TC-PUB-7217 | P2 | Validation over-limit text length 8234 | case=over-limit:8234 | rejected cleanly | test_public_api_phase2_part_4.py |
| TC-PUB-7218 | P2 | Validation over-limit text length 8235 | case=over-limit:8235 | rejected cleanly | test_public_api_phase2_part_4.py |
| TC-PUB-7219 | P2 | Validation over-limit text length 8236 | case=over-limit:8236 | rejected cleanly | test_public_api_phase2_part_4.py |
| TC-PUB-7220 | P2 | Validation over-limit text length 8237 | case=over-limit:8237 | rejected cleanly | test_public_api_phase2_part_4.py |
| TC-PUB-7221 | P2 | Validation over-limit text length 8238 | case=over-limit:8238 | rejected cleanly | test_public_api_phase2_part_4.py |
| TC-PUB-7222 | P2 | Validation over-limit text length 8239 | case=over-limit:8239 | rejected cleanly | test_public_api_phase2_part_4.py |
| TC-PUB-7223 | P2 | Validation over-limit text length 8240 | case=over-limit:8240 | rejected cleanly | test_public_api_phase2_part_4.py |
| TC-PUB-7224 | P2 | Validation over-limit text length 8241 | case=over-limit:8241 | rejected cleanly | test_public_api_phase2_part_4.py |
| TC-PUB-7225 | P2 | Validation over-limit text length 8242 | case=over-limit:8242 | rejected cleanly | test_public_api_phase2_part_4.py |
| TC-PUB-7226 | P2 | Validation over-limit text length 8243 | case=over-limit:8243 | rejected cleanly | test_public_api_phase2_part_4.py |
| TC-PUB-7227 | P2 | Validation over-limit text length 8244 | case=over-limit:8244 | rejected cleanly | test_public_api_phase2_part_4.py |
| TC-PUB-7228 | P2 | Validation over-limit text length 8245 | case=over-limit:8245 | rejected cleanly | test_public_api_phase2_part_4.py |
| TC-PUB-7229 | P2 | Validation over-limit text length 8246 | case=over-limit:8246 | rejected cleanly | test_public_api_phase2_part_4.py |
| TC-PUB-7230 | P2 | Validation over-limit text length 8247 | case=over-limit:8247 | rejected cleanly | test_public_api_phase2_part_4.py |
| TC-PUB-7231 | P2 | Validation over-limit text length 8248 | case=over-limit:8248 | rejected cleanly | test_public_api_phase2_part_4.py |
| TC-PUB-7232 | P2 | Validation over-limit text length 8249 | case=over-limit:8249 | rejected cleanly | test_public_api_phase2_part_4.py |
| TC-PUB-7233 | P2 | Validation over-limit text length 8250 | case=over-limit:8250 | rejected cleanly | test_public_api_phase2_part_4.py |
| TC-PUB-7234 | P2 | Validation over-limit text length 8251 | case=over-limit:8251 | rejected cleanly | test_public_api_phase2_part_4.py |
| TC-PUB-7235 | P2 | Validation over-limit text length 8252 | case=over-limit:8252 | rejected cleanly | test_public_api_phase2_part_4.py |
| TC-PUB-7236 | P2 | Validation over-limit text length 8253 | case=over-limit:8253 | rejected cleanly | test_public_api_phase2_part_4.py |
| TC-PUB-7237 | P2 | Validation over-limit text length 8254 | case=over-limit:8254 | rejected cleanly | test_public_api_phase2_part_4.py |
| TC-PUB-7238 | P2 | Validation over-limit text length 8255 | case=over-limit:8255 | rejected cleanly | test_public_api_phase2_part_4.py |
| TC-PUB-7239 | P2 | Validation over-limit text length 8256 | case=over-limit:8256 | rejected cleanly | test_public_api_phase2_part_4.py |
| TC-PUB-7240 | P2 | Validation over-limit text length 8257 | case=over-limit:8257 | rejected cleanly | test_public_api_phase2_part_4.py |
| TC-PUB-7241 | P2 | Validation over-limit text length 8258 | case=over-limit:8258 | rejected cleanly | test_public_api_phase2_part_4.py |
| TC-PUB-7242 | P2 | Validation over-limit text length 8259 | case=over-limit:8259 | rejected cleanly | test_public_api_phase2_part_4.py |
| TC-PUB-7243 | P2 | Validation over-limit text length 8260 | case=over-limit:8260 | rejected cleanly | test_public_api_phase2_part_4.py |
| TC-PUB-7244 | P2 | Validation over-limit text length 8261 | case=over-limit:8261 | rejected cleanly | test_public_api_phase2_part_4.py |
| TC-PUB-7245 | P2 | Validation over-limit text length 8262 | case=over-limit:8262 | rejected cleanly | test_public_api_phase2_part_4.py |
| TC-PUB-7246 | P2 | Validation over-limit text length 8263 | case=over-limit:8263 | rejected cleanly | test_public_api_phase2_part_4.py |
| TC-PUB-7247 | P2 | Validation over-limit text length 8264 | case=over-limit:8264 | rejected cleanly | test_public_api_phase2_part_4.py |
| TC-PUB-7248 | P2 | Validation over-limit text length 8265 | case=over-limit:8265 | rejected cleanly | test_public_api_phase2_part_4.py |
| TC-PUB-7249 | P2 | Validation over-limit text length 8266 | case=over-limit:8266 | rejected cleanly | test_public_api_phase2_part_4.py |
| TC-PUB-7250 | P2 | Validation over-limit text length 8267 | case=over-limit:8267 | rejected cleanly | test_public_api_phase2_part_4.py |
| TC-PUB-7251 | P2 | Validation over-limit text length 8268 | case=over-limit:8268 | rejected cleanly | test_public_api_phase2_part_4.py |
| TC-PUB-7252 | P2 | Validation over-limit text length 8269 | case=over-limit:8269 | rejected cleanly | test_public_api_phase2_part_4.py |
| TC-PUB-7253 | P2 | Validation over-limit text length 8270 | case=over-limit:8270 | rejected cleanly | test_public_api_phase2_part_4.py |
| TC-PUB-7254 | P2 | Validation over-limit text length 8271 | case=over-limit:8271 | rejected cleanly | test_public_api_phase2_part_4.py |
| TC-PUB-7255 | P2 | Validation over-limit text length 8272 | case=over-limit:8272 | rejected cleanly | test_public_api_phase2_part_4.py |
| TC-PUB-7256 | P2 | Validation over-limit text length 8273 | case=over-limit:8273 | rejected cleanly | test_public_api_phase2_part_4.py |
| TC-PUB-7257 | P2 | Validation over-limit text length 8274 | case=over-limit:8274 | rejected cleanly | test_public_api_phase2_part_4.py |
| TC-PUB-7258 | P2 | Validation over-limit text length 8275 | case=over-limit:8275 | rejected cleanly | test_public_api_phase2_part_4.py |
| TC-PUB-7259 | P2 | Validation over-limit text length 8276 | case=over-limit:8276 | rejected cleanly | test_public_api_phase2_part_4.py |
| TC-PUB-7260 | P2 | Validation over-limit text length 8277 | case=over-limit:8277 | rejected cleanly | test_public_api_phase2_part_4.py |
| TC-PUB-7261 | P2 | Validation over-limit text length 8278 | case=over-limit:8278 | rejected cleanly | test_public_api_phase2_part_4.py |
| TC-PUB-7262 | P2 | Validation structural '{"text": ""}' | case=structural:'{"text": ""}' | rejected cleanly | test_public_api_phase2_part_4.py |
| TC-PUB-7263 | P2 | Validation structural '{"text": null}' | case=structural:'{"text": null}' | rejected cleanly | test_public_api_phase2_part_4.py |
| TC-PUB-7264 | P2 | Validation structural '{}' | case=structural:'{}' | rejected cleanly | test_public_api_phase2_part_4.py |
| TC-PUB-7265 | P2 | Validation structural '{"nope": 1}' | case=structural:'{"nope": 1}' | rejected cleanly | test_public_api_phase2_part_4.py |
| TC-PUB-7266 | P2 | Validation structural '{"text": 12345}' | case=structural:'{"text": 12345}' | rejected cleanly | test_public_api_phase2_part_4.py |
| TC-PUB-7267 | P2 | Validation structural '{"items": []}' | case=structural:'{"items": []}' | rejected cleanly | test_public_api_phase2_part_4.py |
| TC-PUB-7268 | P2 | Validation structural '{"items": [{"nope": 1}]}' | case=structural:'{"items": [{"nope": 1}]}' | rejected cleanly | test_public_api_phase2_part_4.py |
| TC-PUB-7269 | P2 | Validation structural '{not valid json' | case=structural:'{not valid json' | rejected cleanly | test_public_api_phase2_part_4.py |
| TC-PUB-7270 | P2 | Validation structural '{"text": "   "}' | case=structural:'{"text": "   "}' | rejected cleanly | test_public_api_phase2_part_4.py |
| TC-PUB-7271 | P2 | Validation structural '{"text": "x"}' | case=structural:'{"text": "x"}' | rejected cleanly | test_public_api_phase2_part_4.py |
| TC-PUB-7272 | P2 | Validation structural '{"text": "xxxxxxxxxxxxxx' | case=structural:'{"text": "xxxxxxxxxxxxxx' | rejected cleanly | test_public_api_phase2_part_4.py |
| TC-PUB-7273 | P2 | Validation structural '{"text": "xxxxxxxxxxxxxx' | case=structural:'{"text": "xxxxxxxxxxxxxx' | rejected cleanly | test_public_api_phase2_part_4.py |
| TC-PUB-7274 | P2 | Batch validation 200 | case=batch:1415 | bounded | test_public_api_phase2_part_4.py |
| TC-PUB-7275 | P2 | Batch validation 422 | case=batch:1429 | bounded | test_public_api_phase2_part_4.py |
| TC-PUB-7276 | P2 | Edge content #0 plain | text='emoji 😀 test',variant=plain | moderated | test_public_api_phase2_part_5.py |
| TC-PUB-7277 | P2 | Edge content #0 doubled | text='emoji 😀 test',variant=doubled | moderated | test_public_api_phase2_part_5.py |
| TC-PUB-7278 | P2 | Edge content #0 tripled | text='emoji 😀 test',variant=tripled | moderated | test_public_api_phase2_part_5.py |
| TC-PUB-7279 | P2 | Edge content #0 prefixed | text='emoji 😀 test',variant=prefixed | moderated | test_public_api_phase2_part_5.py |
| TC-PUB-7280 | P2 | Edge content #0 suffixed | text='emoji 😀 test',variant=suffixed | moderated | test_public_api_phase2_part_5.py |
| TC-PUB-7281 | P2 | Edge content #1 plain | text='café au lait',variant=plain | moderated | test_public_api_phase2_part_5.py |
| TC-PUB-7282 | P2 | Edge content #1 doubled | text='café au lait',variant=doubled | moderated | test_public_api_phase2_part_5.py |
| TC-PUB-7283 | P2 | Edge content #1 tripled | text='café au lait',variant=tripled | moderated | test_public_api_phase2_part_5.py |
| TC-PUB-7284 | P2 | Edge content #1 prefixed | text='café au lait',variant=prefixed | moderated | test_public_api_phase2_part_5.py |
| TC-PUB-7285 | P2 | Edge content #1 suffixed | text='café au lait',variant=suffixed | moderated | test_public_api_phase2_part_5.py |
| TC-PUB-7286 | P2 | Edge content #2 plain | text='ｆｕｌｌｗｉｄｔｈ',variant=plain | moderated | test_public_api_phase2_part_5.py |
| TC-PUB-7287 | P2 | Edge content #2 doubled | text='ｆｕｌｌｗｉｄｔｈ',variant=doubled | moderated | test_public_api_phase2_part_5.py |
| TC-PUB-7288 | P2 | Edge content #2 tripled | text='ｆｕｌｌｗｉｄｔｈ',variant=tripled | moderated | test_public_api_phase2_part_5.py |
| TC-PUB-7289 | P2 | Edge content #2 prefixed | text='ｆｕｌｌｗｉｄｔｈ',variant=prefixed | moderated | test_public_api_phase2_part_5.py |
| TC-PUB-7290 | P2 | Edge content #2 suffixed | text='ｆｕｌｌｗｉｄｔｈ',variant=suffixed | moderated | test_public_api_phase2_part_5.py |
| TC-PUB-7291 | P2 | Edge content #3 plain | text='mixed 中文 eng',variant=plain | moderated | test_public_api_phase2_part_5.py |
| TC-PUB-7292 | P2 | Edge content #3 doubled | text='mixed 中文 eng',variant=doubled | moderated | test_public_api_phase2_part_5.py |
| TC-PUB-7293 | P2 | Edge content #3 tripled | text='mixed 中文 eng',variant=tripled | moderated | test_public_api_phase2_part_5.py |
| TC-PUB-7294 | P2 | Edge content #3 prefixed | text='mixed 中文 eng',variant=prefixed | moderated | test_public_api_phase2_part_5.py |
| TC-PUB-7295 | P2 | Edge content #3 suffixed | text='mixed 中文 eng',variant=suffixed | moderated | test_public_api_phase2_part_5.py |
| TC-PUB-7296 | P2 | Edge content #4 plain | text='tab\tseparate',variant=plain | moderated | test_public_api_phase2_part_5.py |
| TC-PUB-7297 | P2 | Edge content #4 doubled | text='tab\tseparate',variant=doubled | moderated | test_public_api_phase2_part_5.py |
| TC-PUB-7298 | P2 | Edge content #4 tripled | text='tab\tseparate',variant=tripled | moderated | test_public_api_phase2_part_5.py |
| TC-PUB-7299 | P2 | Edge content #4 prefixed | text='tab\tseparate',variant=prefixed | moderated | test_public_api_phase2_part_5.py |
| TC-PUB-7300 | P2 | Edge content #4 suffixed | text='tab\tseparate',variant=suffixed | moderated | test_public_api_phase2_part_5.py |
| TC-PUB-7301 | P2 | Edge content #5 plain | text='line\nbreak',variant=plain | moderated | test_public_api_phase2_part_5.py |
| TC-PUB-7302 | P2 | Edge content #5 doubled | text='line\nbreak',variant=doubled | moderated | test_public_api_phase2_part_5.py |
| TC-PUB-7303 | P2 | Edge content #5 tripled | text='line\nbreak',variant=tripled | moderated | test_public_api_phase2_part_5.py |
| TC-PUB-7304 | P2 | Edge content #5 prefixed | text='line\nbreak',variant=prefixed | moderated | test_public_api_phase2_part_5.py |
| TC-PUB-7305 | P2 | Edge content #5 suffixed | text='line\nbreak',variant=suffixed | moderated | test_public_api_phase2_part_5.py |
| TC-PUB-7306 | P2 | Edge content #6 plain | text='multiple   s',variant=plain | moderated | test_public_api_phase2_part_5.py |
| TC-PUB-7307 | P2 | Edge content #6 doubled | text='multiple   s',variant=doubled | moderated | test_public_api_phase2_part_5.py |
| TC-PUB-7308 | P2 | Edge content #6 tripled | text='multiple   s',variant=tripled | moderated | test_public_api_phase2_part_5.py |
| TC-PUB-7309 | P2 | Edge content #6 prefixed | text='multiple   s',variant=prefixed | moderated | test_public_api_phase2_part_5.py |
| TC-PUB-7310 | P2 | Edge content #6 suffixed | text='multiple   s',variant=suffixed | moderated | test_public_api_phase2_part_5.py |
| TC-PUB-7311 | P2 | Edge content #7 plain | text='!!! ??? ...',variant=plain | moderated | test_public_api_phase2_part_5.py |
| TC-PUB-7312 | P2 | Edge content #7 doubled | text='!!! ??? ...',variant=doubled | moderated | test_public_api_phase2_part_5.py |
| TC-PUB-7313 | P2 | Edge content #7 tripled | text='!!! ??? ...',variant=tripled | moderated | test_public_api_phase2_part_5.py |
| TC-PUB-7314 | P2 | Edge content #7 prefixed | text='!!! ??? ...',variant=prefixed | moderated | test_public_api_phase2_part_5.py |
| TC-PUB-7315 | P2 | Edge content #7 suffixed | text='!!! ??? ...',variant=suffixed | moderated | test_public_api_phase2_part_5.py |
| TC-PUB-7316 | P2 | Edge content #8 plain | text='12345 67890',variant=plain | moderated | test_public_api_phase2_part_5.py |
| TC-PUB-7317 | P2 | Edge content #8 doubled | text='12345 67890',variant=doubled | moderated | test_public_api_phase2_part_5.py |
| TC-PUB-7318 | P2 | Edge content #8 tripled | text='12345 67890',variant=tripled | moderated | test_public_api_phase2_part_5.py |
| TC-PUB-7319 | P2 | Edge content #8 prefixed | text='12345 67890',variant=prefixed | moderated | test_public_api_phase2_part_5.py |
| TC-PUB-7320 | P2 | Edge content #8 suffixed | text='12345 67890',variant=suffixed | moderated | test_public_api_phase2_part_5.py |
| TC-PUB-7321 | P2 | Edge content #9 plain | text='x',variant=plain | moderated | test_public_api_phase2_part_5.py |
| TC-PUB-7322 | P2 | Edge content #9 doubled | text='x',variant=doubled | moderated | test_public_api_phase2_part_5.py |
| TC-PUB-7323 | P2 | Edge content #9 tripled | text='x',variant=tripled | moderated | test_public_api_phase2_part_5.py |
| TC-PUB-7324 | P2 | Edge content #9 prefixed | text='x',variant=prefixed | moderated | test_public_api_phase2_part_5.py |
| TC-PUB-7325 | P2 | Edge content #9 suffixed | text='x',variant=suffixed | moderated | test_public_api_phase2_part_5.py |
| TC-PUB-7326 | P2 | Edge content #10 plain | text='ßæøåñ',variant=plain | moderated | test_public_api_phase2_part_5.py |
| TC-PUB-7327 | P2 | Edge content #10 doubled | text='ßæøåñ',variant=doubled | moderated | test_public_api_phase2_part_5.py |
| TC-PUB-7328 | P2 | Edge content #10 tripled | text='ßæøåñ',variant=tripled | moderated | test_public_api_phase2_part_5.py |
| TC-PUB-7329 | P2 | Edge content #10 prefixed | text='ßæøåñ',variant=prefixed | moderated | test_public_api_phase2_part_5.py |
| TC-PUB-7330 | P2 | Edge content #10 suffixed | text='ßæøåñ',variant=suffixed | moderated | test_public_api_phase2_part_5.py |
| TC-PUB-7331 | P2 | Edge content #11 plain | text='\u2028hidden',variant=plain | moderated | test_public_api_phase2_part_5.py |
| TC-PUB-7332 | P2 | Edge content #11 doubled | text='\u2028hidden',variant=doubled | moderated | test_public_api_phase2_part_5.py |
| TC-PUB-7333 | P2 | Edge content #11 tripled | text='\u2028hidden',variant=tripled | moderated | test_public_api_phase2_part_5.py |
| TC-PUB-7334 | P2 | Edge content #11 prefixed | text='\u2028hidden',variant=prefixed | moderated | test_public_api_phase2_part_5.py |
| TC-PUB-7335 | P2 | Edge content #11 suffixed | text='\u2028hidden',variant=suffixed | moderated | test_public_api_phase2_part_5.py |
| TC-PUB-7336 | P2 | Edge content #12 plain | text='zero width \u200b',variant=plain | moderated | test_public_api_phase2_part_5.py |
| TC-PUB-7337 | P2 | Edge content #12 doubled | text='zero width \u200b',variant=doubled | moderated | test_public_api_phase2_part_5.py |
| TC-PUB-7338 | P2 | Edge content #12 tripled | text='zero width \u200b',variant=tripled | moderated | test_public_api_phase2_part_5.py |
| TC-PUB-7339 | P2 | Edge content #12 prefixed | text='zero width \u200b',variant=prefixed | moderated | test_public_api_phase2_part_5.py |
| TC-PUB-7340 | P2 | Edge content #12 suffixed | text='zero width \u200b',variant=suffixed | moderated | test_public_api_phase2_part_5.py |
| TC-PUB-7341 | P2 | Edge content #13 plain | text='directional ',variant=plain | moderated | test_public_api_phase2_part_5.py |
| TC-PUB-7342 | P2 | Edge content #13 doubled | text='directional ',variant=doubled | moderated | test_public_api_phase2_part_5.py |
| TC-PUB-7343 | P2 | Edge content #13 tripled | text='directional ',variant=tripled | moderated | test_public_api_phase2_part_5.py |
| TC-PUB-7344 | P2 | Edge content #13 prefixed | text='directional ',variant=prefixed | moderated | test_public_api_phase2_part_5.py |
| TC-PUB-7345 | P2 | Edge content #13 suffixed | text='directional ',variant=suffixed | moderated | test_public_api_phase2_part_5.py |
| TC-PUB-7346 | P2 | Edge content #14 plain | text='combining é',variant=plain | moderated | test_public_api_phase2_part_5.py |
| TC-PUB-7347 | P2 | Edge content #14 doubled | text='combining é',variant=doubled | moderated | test_public_api_phase2_part_5.py |
| TC-PUB-7348 | P2 | Edge content #14 tripled | text='combining é',variant=tripled | moderated | test_public_api_phase2_part_5.py |
| TC-PUB-7349 | P2 | Edge content #14 prefixed | text='combining é',variant=prefixed | moderated | test_public_api_phase2_part_5.py |
| TC-PUB-7350 | P2 | Edge content #14 suffixed | text='combining é',variant=suffixed | moderated | test_public_api_phase2_part_5.py |
| TC-PUB-7351 | P2 | Edge content #15 plain | text='русский текс',variant=plain | moderated | test_public_api_phase2_part_5.py |
| TC-PUB-7352 | P2 | Edge content #15 doubled | text='русский текс',variant=doubled | moderated | test_public_api_phase2_part_5.py |
| TC-PUB-7353 | P2 | Edge content #15 tripled | text='русский текс',variant=tripled | moderated | test_public_api_phase2_part_5.py |
| TC-PUB-7354 | P2 | Edge content #15 prefixed | text='русский текс',variant=prefixed | moderated | test_public_api_phase2_part_5.py |
| TC-PUB-7355 | P2 | Edge content #15 suffixed | text='русский текс',variant=suffixed | moderated | test_public_api_phase2_part_5.py |
| TC-PUB-7356 | P2 | Edge content #16 plain | text='日本語の文章',variant=plain | moderated | test_public_api_phase2_part_5.py |
| TC-PUB-7357 | P2 | Edge content #16 doubled | text='日本語の文章',variant=doubled | moderated | test_public_api_phase2_part_5.py |
| TC-PUB-7358 | P2 | Edge content #16 tripled | text='日本語の文章',variant=tripled | moderated | test_public_api_phase2_part_5.py |
| TC-PUB-7359 | P2 | Edge content #16 prefixed | text='日本語の文章',variant=prefixed | moderated | test_public_api_phase2_part_5.py |
| TC-PUB-7360 | P2 | Edge content #16 suffixed | text='日本語の文章',variant=suffixed | moderated | test_public_api_phase2_part_5.py |
| TC-PUB-7361 | P2 | Edge content #17 plain | text='한국어 문장',variant=plain | moderated | test_public_api_phase2_part_5.py |
| TC-PUB-7362 | P2 | Edge content #17 doubled | text='한국어 문장',variant=doubled | moderated | test_public_api_phase2_part_5.py |
| TC-PUB-7363 | P2 | Edge content #17 tripled | text='한국어 문장',variant=tripled | moderated | test_public_api_phase2_part_5.py |
| TC-PUB-7364 | P2 | Edge content #17 prefixed | text='한국어 문장',variant=prefixed | moderated | test_public_api_phase2_part_5.py |
| TC-PUB-7365 | P2 | Edge content #17 suffixed | text='한국어 문장',variant=suffixed | moderated | test_public_api_phase2_part_5.py |
| TC-PUB-7366 | P2 | Edge content #18 plain | text='العربية نص',variant=plain | moderated | test_public_api_phase2_part_5.py |
| TC-PUB-7367 | P2 | Edge content #18 doubled | text='العربية نص',variant=doubled | moderated | test_public_api_phase2_part_5.py |
| TC-PUB-7368 | P2 | Edge content #18 tripled | text='العربية نص',variant=tripled | moderated | test_public_api_phase2_part_5.py |
| TC-PUB-7369 | P2 | Edge content #18 prefixed | text='العربية نص',variant=prefixed | moderated | test_public_api_phase2_part_5.py |
| TC-PUB-7370 | P2 | Edge content #18 suffixed | text='العربية نص',variant=suffixed | moderated | test_public_api_phase2_part_5.py |
| TC-PUB-7371 | P2 | Edge content #19 plain | text='עברית טקסט',variant=plain | moderated | test_public_api_phase2_part_5.py |
| TC-PUB-7372 | P2 | Edge content #19 doubled | text='עברית טקסט',variant=doubled | moderated | test_public_api_phase2_part_5.py |
| TC-PUB-7373 | P2 | Edge content #19 tripled | text='עברית טקסט',variant=tripled | moderated | test_public_api_phase2_part_5.py |
| TC-PUB-7374 | P2 | Edge content #19 prefixed | text='עברית טקסט',variant=prefixed | moderated | test_public_api_phase2_part_5.py |
| TC-PUB-7375 | P2 | Edge content #19 suffixed | text='עברית טקסט',variant=suffixed | moderated | test_public_api_phase2_part_5.py |
| TC-PUB-7376 | P2 | Profiling flow scenario 0 | user=pubuser0 | rows recorded | test_public_api_phase2_part_6.py |
| TC-PUB-7377 | P2 | Profiling flow scenario 1 | user=pubuser1 | rows recorded | test_public_api_phase2_part_6.py |
| TC-PUB-7378 | P2 | Profiling flow scenario 2 | user=pubuser2 | rows recorded | test_public_api_phase2_part_6.py |
| TC-PUB-7379 | P2 | Profiling flow scenario 3 | user=pubuser3 | rows recorded | test_public_api_phase2_part_6.py |
| TC-PUB-7380 | P2 | Profiling flow scenario 4 | user=pubuser4 | rows recorded | test_public_api_phase2_part_6.py |
| TC-PUB-7381 | P2 | Profiling flow scenario 5 | user=pubuser5 | rows recorded | test_public_api_phase2_part_6.py |
| TC-PUB-7382 | P2 | Profiling flow scenario 6 | user=pubuser6 | rows recorded | test_public_api_phase2_part_6.py |
| TC-PUB-7383 | P2 | Profiling flow scenario 7 | user=pubuser7 | rows recorded | test_public_api_phase2_part_6.py |
| TC-PUB-7384 | P2 | Profiling flow scenario 8 | user=pubuser8 | rows recorded | test_public_api_phase2_part_6.py |
| TC-PUB-7385 | P2 | Profiling flow scenario 9 | user=pubuser9 | rows recorded | test_public_api_phase2_part_6.py |
| TC-PUB-7386 | P2 | Profiling flow scenario 10 | user=pubuser10 | rows recorded | test_public_api_phase2_part_6.py |
| TC-PUB-7387 | P2 | Profiling flow scenario 11 | user=pubuser11 | rows recorded | test_public_api_phase2_part_6.py |
| TC-PUB-7388 | P2 | Profiling flow scenario 12 | user=pubuser12 | rows recorded | test_public_api_phase2_part_6.py |
| TC-PUB-7389 | P2 | Profiling flow scenario 13 | user=pubuser13 | rows recorded | test_public_api_phase2_part_6.py |
| TC-PUB-7390 | P2 | Profiling flow scenario 14 | user=pubuser14 | rows recorded | test_public_api_phase2_part_6.py |
| TC-PUB-7391 | P2 | Profiling flow scenario 15 | user=pubuser15 | rows recorded | test_public_api_phase2_part_6.py |
| TC-PUB-7392 | P2 | Profiling flow scenario 16 | user=pubuser16 | rows recorded | test_public_api_phase2_part_6.py |
| TC-PUB-7393 | P2 | Profiling flow scenario 17 | user=pubuser17 | rows recorded | test_public_api_phase2_part_6.py |
| TC-PUB-7394 | P2 | Profiling flow scenario 18 | user=pubuser18 | rows recorded | test_public_api_phase2_part_6.py |
| TC-PUB-7395 | P2 | Profiling flow scenario 19 | user=pubuser19 | rows recorded | test_public_api_phase2_part_6.py |
| TC-PUB-7396 | P2 | Profiling flow scenario 20 | user=pubuser20 | rows recorded | test_public_api_phase2_part_6.py |
| TC-PUB-7397 | P2 | Profiling flow scenario 21 | user=pubuser21 | rows recorded | test_public_api_phase2_part_6.py |
| TC-PUB-7398 | P2 | Profiling flow scenario 22 | user=pubuser22 | rows recorded | test_public_api_phase2_part_6.py |
| TC-PUB-7399 | P2 | Profiling flow scenario 23 | user=pubuser23 | rows recorded | test_public_api_phase2_part_6.py |
| TC-PUB-7400 | P2 | Profiling flow scenario 24 | user=pubuser24 | rows recorded | test_public_api_phase2_part_6.py |
| TC-PUB-7401 | P2 | Profiling flow scenario 25 | user=pubuser25 | rows recorded | test_public_api_phase2_part_6.py |
| TC-PUB-7402 | P2 | Profiling flow scenario 26 | user=pubuser26 | rows recorded | test_public_api_phase2_part_6.py |
| TC-PUB-7403 | P2 | Profiling flow scenario 27 | user=pubuser27 | rows recorded | test_public_api_phase2_part_6.py |
| TC-PUB-7404 | P2 | Profiling flow scenario 28 | user=pubuser28 | rows recorded | test_public_api_phase2_part_6.py |
| TC-PUB-7405 | P2 | Profiling flow scenario 29 | user=pubuser29 | rows recorded | test_public_api_phase2_part_6.py |
| TC-PUB-7406 | P2 | Profiling flow scenario 30 | user=pubuser30 | rows recorded | test_public_api_phase2_part_6.py |
| TC-PUB-7407 | P2 | Profiling flow scenario 31 | user=pubuser31 | rows recorded | test_public_api_phase2_part_6.py |
| TC-PUB-7408 | P2 | Profiling flow scenario 32 | user=pubuser32 | rows recorded | test_public_api_phase2_part_6.py |
| TC-PUB-7409 | P2 | Profiling flow scenario 33 | user=pubuser33 | rows recorded | test_public_api_phase2_part_6.py |
| TC-PUB-7410 | P2 | Profiling flow scenario 34 | user=pubuser34 | rows recorded | test_public_api_phase2_part_6.py |
| TC-PUB-7411 | P2 | Profiling flow scenario 35 | user=pubuser35 | rows recorded | test_public_api_phase2_part_6.py |
| TC-PUB-7412 | P2 | Profiling flow scenario 36 | user=pubuser36 | rows recorded | test_public_api_phase2_part_6.py |
| TC-PUB-7413 | P2 | Profiling flow scenario 37 | user=pubuser37 | rows recorded | test_public_api_phase2_part_6.py |
| TC-PUB-7414 | P2 | Profiling flow scenario 38 | user=pubuser38 | rows recorded | test_public_api_phase2_part_6.py |
| TC-PUB-7415 | P2 | Profiling flow scenario 39 | user=pubuser39 | rows recorded | test_public_api_phase2_part_6.py |
| TC-PUB-7416 | P2 | Profiling flow scenario 40 | user=pubuser40 | rows recorded | test_public_api_phase2_part_6.py |
| TC-PUB-7417 | P2 | Profiling flow scenario 41 | user=pubuser41 | rows recorded | test_public_api_phase2_part_6.py |
| TC-PUB-7418 | P2 | Profiling flow scenario 42 | user=pubuser42 | rows recorded | test_public_api_phase2_part_6.py |
| TC-PUB-7419 | P2 | Profiling flow scenario 43 | user=pubuser43 | rows recorded | test_public_api_phase2_part_6.py |
| TC-PUB-7420 | P2 | Profiling flow scenario 44 | user=pubuser44 | rows recorded | test_public_api_phase2_part_6.py |
| TC-PUB-7421 | P2 | Profiling flow scenario 45 | user=pubuser45 | rows recorded | test_public_api_phase2_part_6.py |
| TC-PUB-7422 | P2 | Profiling flow scenario 46 | user=pubuser46 | rows recorded | test_public_api_phase2_part_6.py |
| TC-PUB-7423 | P2 | Profiling flow scenario 47 | user=pubuser47 | rows recorded | test_public_api_phase2_part_6.py |
| TC-PUB-7424 | P2 | Profiling flow scenario 48 | user=pubuser48 | rows recorded | test_public_api_phase2_part_6.py |
| TC-PUB-7425 | P2 | Profiling flow scenario 49 | user=pubuser49 | rows recorded | test_public_api_phase2_part_6.py |
| TC-PUB-7426 | P2 | Profiling flow scenario 50 | user=pubuser50 | rows recorded | test_public_api_phase2_part_6.py |
| TC-PUB-7427 | P2 | Profiling flow scenario 51 | user=pubuser51 | rows recorded | test_public_api_phase2_part_6.py |
| TC-PUB-7428 | P2 | Profiling flow scenario 52 | user=pubuser52 | rows recorded | test_public_api_phase2_part_6.py |
| TC-PUB-7429 | P2 | Profiling flow scenario 53 | user=pubuser53 | rows recorded | test_public_api_phase2_part_6.py |
| TC-PUB-7430 | P2 | Profiling flow scenario 54 | user=pubuser54 | rows recorded | test_public_api_phase2_part_6.py |
| TC-PUB-7431 | P2 | Profiling flow scenario 55 | user=pubuser55 | rows recorded | test_public_api_phase2_part_6.py |
| TC-PUB-7432 | P2 | Profiling flow scenario 56 | user=pubuser56 | rows recorded | test_public_api_phase2_part_6.py |
| TC-PUB-7433 | P2 | Profiling flow scenario 57 | user=pubuser57 | rows recorded | test_public_api_phase2_part_6.py |
| TC-PUB-7434 | P2 | Profiling flow scenario 58 | user=pubuser58 | rows recorded | test_public_api_phase2_part_6.py |
| TC-PUB-7435 | P2 | Profiling flow scenario 59 | user=pubuser59 | rows recorded | test_public_api_phase2_part_6.py |
| TC-PUB-7436 | P2 | Profiling flow scenario 60 | user=pubuser60 | rows recorded | test_public_api_phase2_part_6.py |
| TC-PUB-7437 | P2 | Profiling flow scenario 61 | user=pubuser61 | rows recorded | test_public_api_phase2_part_6.py |
| TC-PUB-7438 | P2 | Profiling flow scenario 62 | user=pubuser62 | rows recorded | test_public_api_phase2_part_6.py |
| TC-PUB-7439 | P2 | Profiling flow scenario 63 | user=pubuser63 | rows recorded | test_public_api_phase2_part_6.py |
| TC-PUB-7440 | P2 | Profiling flow scenario 64 | user=pubuser64 | rows recorded | test_public_api_phase2_part_6.py |
| TC-PUB-7441 | P2 | Profiling flow scenario 65 | user=pubuser65 | rows recorded | test_public_api_phase2_part_6.py |
| TC-PUB-7442 | P2 | Profiling flow scenario 66 | user=pubuser66 | rows recorded | test_public_api_phase2_part_6.py |
| TC-PUB-7443 | P2 | Profiling flow scenario 67 | user=pubuser67 | rows recorded | test_public_api_phase2_part_6.py |
| TC-PUB-7444 | P2 | Profiling flow scenario 68 | user=pubuser68 | rows recorded | test_public_api_phase2_part_6.py |
| TC-PUB-7445 | P2 | Profiling flow scenario 69 | user=pubuser69 | rows recorded | test_public_api_phase2_part_6.py |
| TC-PUB-7446 | P2 | Profiling flow scenario 70 | user=pubuser70 | rows recorded | test_public_api_phase2_part_6.py |
| TC-PUB-7447 | P2 | Profiling flow scenario 71 | user=pubuser71 | rows recorded | test_public_api_phase2_part_6.py |
| TC-PUB-7448 | P2 | Profiling flow scenario 72 | user=pubuser72 | rows recorded | test_public_api_phase2_part_6.py |
| TC-PUB-7449 | P2 | Profiling flow scenario 73 | user=pubuser73 | rows recorded | test_public_api_phase2_part_6.py |
| TC-PUB-7450 | P2 | Profiling flow scenario 74 | user=pubuser74 | rows recorded | test_public_api_phase2_part_6.py |
| TC-PUB-7451 | P2 | Profiling flow scenario 75 | user=pubuser75 | rows recorded | test_public_api_phase2_part_6.py |
| TC-PUB-7452 | P2 | Profiling flow scenario 76 | user=pubuser76 | rows recorded | test_public_api_phase2_part_6.py |
| TC-PUB-7453 | P2 | Profiling flow scenario 77 | user=pubuser77 | rows recorded | test_public_api_phase2_part_6.py |
| TC-PUB-7454 | P2 | Profiling flow scenario 78 | user=pubuser78 | rows recorded | test_public_api_phase2_part_6.py |
| TC-PUB-7455 | P2 | Profiling flow scenario 79 | user=pubuser79 | rows recorded | test_public_api_phase2_part_6.py |
| TC-PUB-7456 | P2 | Profiling flow scenario 80 | user=pubuser80 | rows recorded | test_public_api_phase2_part_6.py |
| TC-PUB-7457 | P2 | Profiling flow scenario 81 | user=pubuser81 | rows recorded | test_public_api_phase2_part_6.py |
| TC-PUB-7458 | P2 | Profiling flow scenario 82 | user=pubuser82 | rows recorded | test_public_api_phase2_part_6.py |
| TC-PUB-7459 | P2 | Profiling flow scenario 83 | user=pubuser83 | rows recorded | test_public_api_phase2_part_6.py |
| TC-PUB-7460 | P2 | Profiling flow scenario 84 | user=pubuser84 | rows recorded | test_public_api_phase2_part_6.py |
| TC-PUB-7461 | P2 | Profiling flow scenario 85 | user=pubuser85 | rows recorded | test_public_api_phase2_part_6.py |
| TC-PUB-7462 | P2 | Profiling flow scenario 86 | user=pubuser86 | rows recorded | test_public_api_phase2_part_6.py |
| TC-PUB-7463 | P2 | Profiling flow scenario 87 | user=pubuser87 | rows recorded | test_public_api_phase2_part_6.py |
| TC-PUB-7464 | P2 | Profiling flow scenario 88 | user=pubuser88 | rows recorded | test_public_api_phase2_part_6.py |
| TC-PUB-7465 | P2 | Profiling flow scenario 89 | user=pubuser89 | rows recorded | test_public_api_phase2_part_6.py |
| TC-PUB-7466 | P2 | Profiling flow scenario 90 | user=pubuser90 | rows recorded | test_public_api_phase2_part_6.py |
| TC-PUB-7467 | P2 | Profiling flow scenario 91 | user=pubuser91 | rows recorded | test_public_api_phase2_part_6.py |
| TC-PUB-7468 | P2 | Profiling flow scenario 92 | user=pubuser92 | rows recorded | test_public_api_phase2_part_6.py |
| TC-PUB-7469 | P2 | Profiling flow scenario 93 | user=pubuser93 | rows recorded | test_public_api_phase2_part_6.py |
| TC-PUB-7470 | P2 | Profiling flow scenario 94 | user=pubuser94 | rows recorded | test_public_api_phase2_part_6.py |
| TC-PUB-7471 | P2 | Profiling flow scenario 95 | user=pubuser95 | rows recorded | test_public_api_phase2_part_6.py |
| TC-PUB-7472 | P2 | Profiling flow scenario 96 | user=pubuser96 | rows recorded | test_public_api_phase2_part_6.py |
| TC-PUB-7473 | P2 | Profiling flow scenario 97 | user=pubuser97 | rows recorded | test_public_api_phase2_part_6.py |
| TC-PUB-7474 | P2 | Profiling flow scenario 98 | user=pubuser98 | rows recorded | test_public_api_phase2_part_6.py |
| TC-PUB-7475 | P2 | Profiling flow scenario 99 | user=pubuser99 | rows recorded | test_public_api_phase2_part_6.py |
| TC-PUB-7476 | P2 | Response shape id #0 | field=id | present | test_public_api_phase2_part_7.py |
| TC-PUB-7477 | P2 | Response shape id #1 | field=id | present | test_public_api_phase2_part_7.py |
| TC-PUB-7478 | P2 | Response shape id #2 | field=id | present | test_public_api_phase2_part_7.py |
| TC-PUB-7479 | P2 | Response shape id #3 | field=id | present | test_public_api_phase2_part_7.py |
| TC-PUB-7480 | P2 | Response shape id #4 | field=id | present | test_public_api_phase2_part_7.py |
| TC-PUB-7481 | P2 | Response shape id #5 | field=id | present | test_public_api_phase2_part_7.py |
| TC-PUB-7482 | P2 | Response shape id #6 | field=id | present | test_public_api_phase2_part_7.py |
| TC-PUB-7483 | P2 | Response shape id #7 | field=id | present | test_public_api_phase2_part_7.py |
| TC-PUB-7484 | P2 | Response shape verdict #0 | field=verdict | present | test_public_api_phase2_part_7.py |
| TC-PUB-7485 | P2 | Response shape verdict #1 | field=verdict | present | test_public_api_phase2_part_7.py |
| TC-PUB-7486 | P2 | Response shape verdict #2 | field=verdict | present | test_public_api_phase2_part_7.py |
| TC-PUB-7487 | P2 | Response shape verdict #3 | field=verdict | present | test_public_api_phase2_part_7.py |
| TC-PUB-7488 | P2 | Response shape verdict #4 | field=verdict | present | test_public_api_phase2_part_7.py |
| TC-PUB-7489 | P2 | Response shape verdict #5 | field=verdict | present | test_public_api_phase2_part_7.py |
| TC-PUB-7490 | P2 | Response shape verdict #6 | field=verdict | present | test_public_api_phase2_part_7.py |
| TC-PUB-7491 | P2 | Response shape verdict #7 | field=verdict | present | test_public_api_phase2_part_7.py |
| TC-PUB-7492 | P2 | Response shape allowed #0 | field=allowed | present | test_public_api_phase2_part_7.py |
| TC-PUB-7493 | P2 | Response shape allowed #1 | field=allowed | present | test_public_api_phase2_part_7.py |
| TC-PUB-7494 | P2 | Response shape allowed #2 | field=allowed | present | test_public_api_phase2_part_7.py |
| TC-PUB-7495 | P2 | Response shape allowed #3 | field=allowed | present | test_public_api_phase2_part_7.py |
| TC-PUB-7496 | P2 | Response shape allowed #4 | field=allowed | present | test_public_api_phase2_part_7.py |
| TC-PUB-7497 | P2 | Response shape allowed #5 | field=allowed | present | test_public_api_phase2_part_7.py |
| TC-PUB-7498 | P2 | Response shape allowed #6 | field=allowed | present | test_public_api_phase2_part_7.py |
| TC-PUB-7499 | P2 | Response shape allowed #7 | field=allowed | present | test_public_api_phase2_part_7.py |
| TC-PUB-7500 | P2 | Response shape levelUsed #0 | field=levelUsed | present | test_public_api_phase2_part_7.py |
| TC-PUB-7501 | P2 | Response shape levelUsed #1 | field=levelUsed | present | test_public_api_phase2_part_7.py |
| TC-PUB-7502 | P2 | Response shape levelUsed #2 | field=levelUsed | present | test_public_api_phase2_part_7.py |
| TC-PUB-7503 | P2 | Response shape levelUsed #3 | field=levelUsed | present | test_public_api_phase2_part_7.py |
| TC-PUB-7504 | P2 | Response shape levelUsed #4 | field=levelUsed | present | test_public_api_phase2_part_7.py |
| TC-PUB-7505 | P2 | Response shape levelUsed #5 | field=levelUsed | present | test_public_api_phase2_part_7.py |
| TC-PUB-7506 | P2 | Response shape levelUsed #6 | field=levelUsed | present | test_public_api_phase2_part_7.py |
| TC-PUB-7507 | P2 | Response shape levelUsed #7 | field=levelUsed | present | test_public_api_phase2_part_7.py |
| TC-PUB-7508 | P2 | Response shape aiTriggered #0 | field=aiTriggered | present | test_public_api_phase2_part_7.py |
| TC-PUB-7509 | P2 | Response shape aiTriggered #1 | field=aiTriggered | present | test_public_api_phase2_part_7.py |
| TC-PUB-7510 | P2 | Response shape aiTriggered #2 | field=aiTriggered | present | test_public_api_phase2_part_7.py |
| TC-PUB-7511 | P2 | Response shape aiTriggered #3 | field=aiTriggered | present | test_public_api_phase2_part_7.py |
| TC-PUB-7512 | P2 | Response shape aiTriggered #4 | field=aiTriggered | present | test_public_api_phase2_part_7.py |
| TC-PUB-7513 | P2 | Response shape aiTriggered #5 | field=aiTriggered | present | test_public_api_phase2_part_7.py |
| TC-PUB-7514 | P2 | Response shape aiTriggered #6 | field=aiTriggered | present | test_public_api_phase2_part_7.py |
| TC-PUB-7515 | P2 | Response shape aiTriggered #7 | field=aiTriggered | present | test_public_api_phase2_part_7.py |
| TC-PUB-7516 | P2 | Response shape suspicionScore #0 | field=suspicionScore | present | test_public_api_phase2_part_7.py |
| TC-PUB-7517 | P2 | Response shape suspicionScore #1 | field=suspicionScore | present | test_public_api_phase2_part_7.py |
| TC-PUB-7518 | P2 | Response shape suspicionScore #2 | field=suspicionScore | present | test_public_api_phase2_part_7.py |
| TC-PUB-7519 | P2 | Response shape suspicionScore #3 | field=suspicionScore | present | test_public_api_phase2_part_7.py |
| TC-PUB-7520 | P2 | Response shape suspicionScore #4 | field=suspicionScore | present | test_public_api_phase2_part_7.py |
| TC-PUB-7521 | P2 | Response shape suspicionScore #5 | field=suspicionScore | present | test_public_api_phase2_part_7.py |
| TC-PUB-7522 | P2 | Response shape suspicionScore #6 | field=suspicionScore | present | test_public_api_phase2_part_7.py |
| TC-PUB-7523 | P2 | Response shape suspicionScore #7 | field=suspicionScore | present | test_public_api_phase2_part_7.py |
| TC-PUB-7524 | P2 | Response shape reasons #0 | field=reasons | present | test_public_api_phase2_part_7.py |
| TC-PUB-7525 | P2 | Response shape reasons #1 | field=reasons | present | test_public_api_phase2_part_7.py |
| TC-PUB-7526 | P2 | Response shape reasons #2 | field=reasons | present | test_public_api_phase2_part_7.py |
| TC-PUB-7527 | P2 | Response shape reasons #3 | field=reasons | present | test_public_api_phase2_part_7.py |
| TC-PUB-7528 | P2 | Response shape reasons #4 | field=reasons | present | test_public_api_phase2_part_7.py |
| TC-PUB-7529 | P2 | Response shape reasons #5 | field=reasons | present | test_public_api_phase2_part_7.py |
| TC-PUB-7530 | P2 | Response shape reasons #6 | field=reasons | present | test_public_api_phase2_part_7.py |
| TC-PUB-7531 | P2 | Response shape reasons #7 | field=reasons | present | test_public_api_phase2_part_7.py |
| TC-PUB-7532 | P2 | Response shape reason #0 | field=reason | present | test_public_api_phase2_part_7.py |
| TC-PUB-7533 | P2 | Response shape reason #1 | field=reason | present | test_public_api_phase2_part_7.py |
| TC-PUB-7534 | P2 | Response shape reason #2 | field=reason | present | test_public_api_phase2_part_7.py |
| TC-PUB-7535 | P2 | Response shape reason #3 | field=reason | present | test_public_api_phase2_part_7.py |
| TC-PUB-7536 | P2 | Response shape reason #4 | field=reason | present | test_public_api_phase2_part_7.py |
| TC-PUB-7537 | P2 | Response shape reason #5 | field=reason | present | test_public_api_phase2_part_7.py |
| TC-PUB-7538 | P2 | Response shape reason #6 | field=reason | present | test_public_api_phase2_part_7.py |
| TC-PUB-7539 | P2 | Response shape reason #7 | field=reason | present | test_public_api_phase2_part_7.py |
| TC-PUB-7540 | P2 | Response shape matchedWords #0 | field=matchedWords | present | test_public_api_phase2_part_7.py |
| TC-PUB-7541 | P2 | Response shape matchedWords #1 | field=matchedWords | present | test_public_api_phase2_part_7.py |
| TC-PUB-7542 | P2 | Response shape matchedWords #2 | field=matchedWords | present | test_public_api_phase2_part_7.py |
| TC-PUB-7543 | P2 | Response shape matchedWords #3 | field=matchedWords | present | test_public_api_phase2_part_7.py |
| TC-PUB-7544 | P2 | Response shape matchedWords #4 | field=matchedWords | present | test_public_api_phase2_part_7.py |
| TC-PUB-7545 | P2 | Response shape matchedWords #5 | field=matchedWords | present | test_public_api_phase2_part_7.py |
| TC-PUB-7546 | P2 | Response shape matchedWords #6 | field=matchedWords | present | test_public_api_phase2_part_7.py |
| TC-PUB-7547 | P2 | Response shape matchedWords #7 | field=matchedWords | present | test_public_api_phase2_part_7.py |
| TC-PUB-7548 | P2 | Response shape matchedWord #0 | field=matchedWord | present | test_public_api_phase2_part_7.py |
| TC-PUB-7549 | P2 | Response shape matchedWord #1 | field=matchedWord | present | test_public_api_phase2_part_7.py |
| TC-PUB-7550 | P2 | Response shape matchedWord #2 | field=matchedWord | present | test_public_api_phase2_part_7.py |
| TC-PUB-7551 | P2 | Response shape matchedWord #3 | field=matchedWord | present | test_public_api_phase2_part_7.py |
| TC-PUB-7552 | P2 | Response shape matchedWord #4 | field=matchedWord | present | test_public_api_phase2_part_7.py |
| TC-PUB-7553 | P2 | Response shape matchedWord #5 | field=matchedWord | present | test_public_api_phase2_part_7.py |
| TC-PUB-7554 | P2 | Response shape matchedWord #6 | field=matchedWord | present | test_public_api_phase2_part_7.py |
| TC-PUB-7555 | P2 | Response shape matchedWord #7 | field=matchedWord | present | test_public_api_phase2_part_7.py |
| TC-PUB-7556 | P2 | Response shape matchedLanguage #0 | field=matchedLanguage | present | test_public_api_phase2_part_7.py |
| TC-PUB-7557 | P2 | Response shape matchedLanguage #1 | field=matchedLanguage | present | test_public_api_phase2_part_7.py |
| TC-PUB-7558 | P2 | Response shape matchedLanguage #2 | field=matchedLanguage | present | test_public_api_phase2_part_7.py |
| TC-PUB-7559 | P2 | Response shape matchedLanguage #3 | field=matchedLanguage | present | test_public_api_phase2_part_7.py |
| TC-PUB-7560 | P2 | Response shape matchedLanguage #4 | field=matchedLanguage | present | test_public_api_phase2_part_7.py |
| TC-PUB-7561 | P2 | Response shape matchedLanguage #5 | field=matchedLanguage | present | test_public_api_phase2_part_7.py |
| TC-PUB-7562 | P2 | Response shape matchedLanguage #6 | field=matchedLanguage | present | test_public_api_phase2_part_7.py |
| TC-PUB-7563 | P2 | Response shape matchedLanguage #7 | field=matchedLanguage | present | test_public_api_phase2_part_7.py |
| TC-PUB-7564 | P2 | Response shape confidenceScore #0 | field=confidenceScore | present | test_public_api_phase2_part_7.py |
| TC-PUB-7565 | P2 | Response shape confidenceScore #1 | field=confidenceScore | present | test_public_api_phase2_part_7.py |
| TC-PUB-7566 | P2 | Response shape confidenceScore #2 | field=confidenceScore | present | test_public_api_phase2_part_7.py |
| TC-PUB-7567 | P2 | Response shape confidenceScore #3 | field=confidenceScore | present | test_public_api_phase2_part_7.py |
| TC-PUB-7568 | P2 | Response shape confidenceScore #4 | field=confidenceScore | present | test_public_api_phase2_part_7.py |
| TC-PUB-7569 | P2 | Response shape confidenceScore #5 | field=confidenceScore | present | test_public_api_phase2_part_7.py |
| TC-PUB-7570 | P2 | Response shape confidenceScore #6 | field=confidenceScore | present | test_public_api_phase2_part_7.py |
| TC-PUB-7571 | P2 | Response shape confidenceScore #7 | field=confidenceScore | present | test_public_api_phase2_part_7.py |
| TC-PUB-7572 | P2 | Response shape latencyMs #0 | field=latencyMs | present | test_public_api_phase2_part_7.py |
| TC-PUB-7573 | P2 | Response shape latencyMs #1 | field=latencyMs | present | test_public_api_phase2_part_7.py |
| TC-PUB-7574 | P2 | Response shape latencyMs #2 | field=latencyMs | present | test_public_api_phase2_part_7.py |
| TC-PUB-7575 | P2 | Response shape latencyMs #3 | field=latencyMs | present | test_public_api_phase2_part_7.py |

### Phase 3 - 20,000 cases
- Planned sweeps over the full dimension matrix, IDs TC-PUB-0781 onward.

### Phase 4 - 200,000 cases
- Planned high-scale scenarios, IDs TC-PUB-20781 onward.

### Phase 5 - 1,879,220 cases
- Planned exhaustive dimension sweep, IDs TC-PUB-220781 onward.

## Implementation Status
| File | Test Cases | Priority | Status |
| :--- | :--- | :--- | :--- |
| test_public_api_phase2_part_1.py | 6848-6947 | P1 | :white_check_mark: Phase 2 |
| test_public_api_phase2_part_2.py | 6948-7047 | P1 | :white_check_mark: Phase 2 |
| test_public_api_phase2_part_3.py | 7071-7170 | P1 | :white_check_mark: Phase 2 |
| test_public_api_phase2_part_4.py | 7176-7275 | P2 | :white_check_mark: Phase 2 |
| test_public_api_phase2_part_5.py | 7276-7375 | P2 | :white_check_mark: Phase 2 |
| test_public_api_phase2_part_6.py | 7376-7475 | P2 | :white_check_mark: Phase 2 |
| test_public_api_phase2_part_7.py | 7476-7575 | P2 | :white_check_mark: Phase 2 |

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
