# User Profiling Module Test Documentation

## Overview
- **Total Planned:** 1,050,000
- **Phase 1:** 80 (IDs TC-PRF-001 to TC-PRF-0080) :white_check_mark: Implemented
- **Phase 2:** 700 (IDs TC-PRF-0081 to TC-PRF-0780) :white_check_mark: Implemented
- **Phase 3:** 12,000 (IDs TC-PRF-0781 to TC-PRF-12780) :hourglass: Planned
- **Phase 4:** 120,000 (IDs TC-PRF-12781 to TC-PRF-132780) :hourglass: Planned
- **Phase 5:** 917,220 (IDs TC-PRF-132781 to TC-PRF-1050000) :hourglass: Planned

## Dimension Matrix
| Dimension | Values (Phase 2) |
| :--- | :--- |
| Window | 1-365 days |
| Users | 1-1000 |
| Apps | 1-100 |
| Flagged % | 0-100 |
| Cycles | 1-100 |

## Test Case List

### Phase 1 - 80 cases
- 80 cases (ratios, cycles, isolation).

### Phase 2 (Current) - 700 cases
| ID | Priority | Description | Dimensions | Expected Outcome | File |
| :--- | :--- | :--- | :--- | :--- | :--- |
| TC-PRF-2801 | P1 | Ratio (0,0)/1 | flag=0,block=0,total=1 | ratio=0.0000 | test_profiling_phase2_part_1.py |
| TC-PRF-2802 | P1 | Ratio (0,1)/2 | flag=0,block=1,total=2 | ratio=0.5000 | test_profiling_phase2_part_1.py |
| TC-PRF-2803 | P1 | Ratio (0,2)/3 | flag=0,block=2,total=3 | ratio=0.6667 | test_profiling_phase2_part_1.py |
| TC-PRF-2804 | P1 | Ratio (0,3)/4 | flag=0,block=3,total=4 | ratio=0.7500 | test_profiling_phase2_part_1.py |
| TC-PRF-2805 | P1 | Ratio (0,4)/5 | flag=0,block=4,total=5 | ratio=0.8000 | test_profiling_phase2_part_1.py |
| TC-PRF-2806 | P1 | Ratio (1,0)/2 | flag=1,block=0,total=2 | ratio=0.5000 | test_profiling_phase2_part_1.py |
| TC-PRF-2807 | P1 | Ratio (1,1)/4 | flag=1,block=1,total=4 | ratio=0.5000 | test_profiling_phase2_part_1.py |
| TC-PRF-2808 | P1 | Ratio (1,2)/6 | flag=1,block=2,total=6 | ratio=0.5000 | test_profiling_phase2_part_1.py |
| TC-PRF-2809 | P1 | Ratio (1,3)/8 | flag=1,block=3,total=8 | ratio=0.5000 | test_profiling_phase2_part_1.py |
| TC-PRF-2810 | P1 | Ratio (1,4)/10 | flag=1,block=4,total=10 | ratio=0.5000 | test_profiling_phase2_part_1.py |
| TC-PRF-2811 | P1 | Ratio (2,0)/3 | flag=2,block=0,total=3 | ratio=0.6667 | test_profiling_phase2_part_1.py |
| TC-PRF-2812 | P1 | Ratio (2,1)/6 | flag=2,block=1,total=6 | ratio=0.5000 | test_profiling_phase2_part_1.py |
| TC-PRF-2813 | P1 | Ratio (2,2)/9 | flag=2,block=2,total=9 | ratio=0.4444 | test_profiling_phase2_part_1.py |
| TC-PRF-2814 | P1 | Ratio (2,3)/7 | flag=2,block=3,total=7 | ratio=0.7143 | test_profiling_phase2_part_1.py |
| TC-PRF-2815 | P1 | Ratio (2,4)/10 | flag=2,block=4,total=10 | ratio=0.6000 | test_profiling_phase2_part_1.py |
| TC-PRF-2816 | P1 | Ratio (3,0)/4 | flag=3,block=0,total=4 | ratio=0.7500 | test_profiling_phase2_part_1.py |
| TC-PRF-2817 | P1 | Ratio (3,1)/8 | flag=3,block=1,total=8 | ratio=0.5000 | test_profiling_phase2_part_1.py |
| TC-PRF-2818 | P1 | Ratio (3,2)/7 | flag=3,block=2,total=7 | ratio=0.7143 | test_profiling_phase2_part_1.py |
| TC-PRF-2819 | P1 | Ratio (3,3)/11 | flag=3,block=3,total=11 | ratio=0.5455 | test_profiling_phase2_part_1.py |
| TC-PRF-2820 | P1 | Ratio (3,4)/10 | flag=3,block=4,total=10 | ratio=0.7000 | test_profiling_phase2_part_1.py |
| TC-PRF-2821 | P1 | Ratio (4,0)/5 | flag=4,block=0,total=5 | ratio=0.8000 | test_profiling_phase2_part_1.py |
| TC-PRF-2822 | P1 | Ratio (4,1)/10 | flag=4,block=1,total=10 | ratio=0.5000 | test_profiling_phase2_part_1.py |
| TC-PRF-2823 | P1 | Ratio (4,2)/10 | flag=4,block=2,total=10 | ratio=0.6000 | test_profiling_phase2_part_1.py |
| TC-PRF-2824 | P1 | Ratio (4,3)/10 | flag=4,block=3,total=10 | ratio=0.7000 | test_profiling_phase2_part_1.py |
| TC-PRF-2825 | P1 | Ratio (4,4)/10 | flag=4,block=4,total=10 | ratio=0.8000 | test_profiling_phase2_part_1.py |
| TC-PRF-2826 | P1 | Ratio (5,0)/6 | flag=5,block=0,total=6 | ratio=0.8333 | test_profiling_phase2_part_1.py |
| TC-PRF-2827 | P1 | Ratio (5,1)/7 | flag=5,block=1,total=7 | ratio=0.8571 | test_profiling_phase2_part_1.py |
| TC-PRF-2828 | P1 | Ratio (5,2)/8 | flag=5,block=2,total=8 | ratio=0.8750 | test_profiling_phase2_part_1.py |
| TC-PRF-2829 | P1 | Ratio (5,3)/9 | flag=5,block=3,total=9 | ratio=0.8889 | test_profiling_phase2_part_1.py |
| TC-PRF-2830 | P1 | Ratio (5,4)/10 | flag=5,block=4,total=10 | ratio=0.9000 | test_profiling_phase2_part_1.py |
| TC-PRF-2831 | P1 | Ratio (6,0)/7 | flag=6,block=0,total=7 | ratio=0.8571 | test_profiling_phase2_part_1.py |
| TC-PRF-2832 | P1 | Ratio (6,1)/9 | flag=6,block=1,total=9 | ratio=0.7778 | test_profiling_phase2_part_1.py |
| TC-PRF-2833 | P1 | Ratio (6,2)/11 | flag=6,block=2,total=11 | ratio=0.7273 | test_profiling_phase2_part_1.py |
| TC-PRF-2834 | P1 | Ratio (6,3)/13 | flag=6,block=3,total=13 | ratio=0.6923 | test_profiling_phase2_part_1.py |
| TC-PRF-2835 | P1 | Ratio (6,4)/15 | flag=6,block=4,total=15 | ratio=0.6667 | test_profiling_phase2_part_1.py |
| TC-PRF-2836 | P1 | Ratio (7,0)/8 | flag=7,block=0,total=8 | ratio=0.8750 | test_profiling_phase2_part_1.py |
| TC-PRF-2837 | P1 | Ratio (7,1)/11 | flag=7,block=1,total=11 | ratio=0.7273 | test_profiling_phase2_part_1.py |
| TC-PRF-2838 | P1 | Ratio (7,2)/14 | flag=7,block=2,total=14 | ratio=0.6429 | test_profiling_phase2_part_1.py |
| TC-PRF-2839 | P1 | Ratio (7,3)/12 | flag=7,block=3,total=12 | ratio=0.8333 | test_profiling_phase2_part_1.py |
| TC-PRF-2840 | P1 | Ratio (7,4)/15 | flag=7,block=4,total=15 | ratio=0.7333 | test_profiling_phase2_part_1.py |
| TC-PRF-2841 | P1 | Ratio (8,0)/9 | flag=8,block=0,total=9 | ratio=0.8889 | test_profiling_phase2_part_1.py |
| TC-PRF-2842 | P1 | Ratio (8,1)/13 | flag=8,block=1,total=13 | ratio=0.6923 | test_profiling_phase2_part_1.py |
| TC-PRF-2843 | P1 | Ratio (8,2)/12 | flag=8,block=2,total=12 | ratio=0.8333 | test_profiling_phase2_part_1.py |
| TC-PRF-2844 | P1 | Ratio (8,3)/16 | flag=8,block=3,total=16 | ratio=0.6875 | test_profiling_phase2_part_1.py |
| TC-PRF-2845 | P1 | Ratio (8,4)/15 | flag=8,block=4,total=15 | ratio=0.8000 | test_profiling_phase2_part_1.py |
| TC-PRF-2846 | P1 | Ratio (9,0)/10 | flag=9,block=0,total=10 | ratio=0.9000 | test_profiling_phase2_part_1.py |
| TC-PRF-2847 | P1 | Ratio (9,1)/15 | flag=9,block=1,total=15 | ratio=0.6667 | test_profiling_phase2_part_1.py |
| TC-PRF-2848 | P1 | Ratio (9,2)/15 | flag=9,block=2,total=15 | ratio=0.7333 | test_profiling_phase2_part_1.py |
| TC-PRF-2849 | P1 | Ratio (9,3)/15 | flag=9,block=3,total=15 | ratio=0.8000 | test_profiling_phase2_part_1.py |
| TC-PRF-2850 | P1 | Ratio (9,4)/15 | flag=9,block=4,total=15 | ratio=0.8667 | test_profiling_phase2_part_1.py |
| TC-PRF-2851 | P1 | Ratio (10,0)/11 | flag=10,block=0,total=11 | ratio=0.9091 | test_profiling_phase2_part_1.py |
| TC-PRF-2852 | P1 | Ratio (10,1)/12 | flag=10,block=1,total=12 | ratio=0.9167 | test_profiling_phase2_part_1.py |
| TC-PRF-2853 | P1 | Ratio (10,2)/13 | flag=10,block=2,total=13 | ratio=0.9231 | test_profiling_phase2_part_1.py |
| TC-PRF-2854 | P1 | Ratio (10,3)/14 | flag=10,block=3,total=14 | ratio=0.9286 | test_profiling_phase2_part_1.py |
| TC-PRF-2855 | P1 | Ratio (10,4)/15 | flag=10,block=4,total=15 | ratio=0.9333 | test_profiling_phase2_part_1.py |
| TC-PRF-2856 | P1 | Ratio (11,0)/12 | flag=11,block=0,total=12 | ratio=0.9167 | test_profiling_phase2_part_1.py |
| TC-PRF-2857 | P1 | Ratio (11,1)/14 | flag=11,block=1,total=14 | ratio=0.8571 | test_profiling_phase2_part_1.py |
| TC-PRF-2858 | P1 | Ratio (11,2)/16 | flag=11,block=2,total=16 | ratio=0.8125 | test_profiling_phase2_part_1.py |
| TC-PRF-2859 | P1 | Ratio (11,3)/18 | flag=11,block=3,total=18 | ratio=0.7778 | test_profiling_phase2_part_1.py |
| TC-PRF-2860 | P1 | Ratio (11,4)/20 | flag=11,block=4,total=20 | ratio=0.7500 | test_profiling_phase2_part_1.py |
| TC-PRF-2861 | P1 | Ratio (12,0)/13 | flag=12,block=0,total=13 | ratio=0.9231 | test_profiling_phase2_part_1.py |
| TC-PRF-2862 | P1 | Ratio (12,1)/16 | flag=12,block=1,total=16 | ratio=0.8125 | test_profiling_phase2_part_1.py |
| TC-PRF-2863 | P1 | Ratio (12,2)/19 | flag=12,block=2,total=19 | ratio=0.7368 | test_profiling_phase2_part_1.py |
| TC-PRF-2864 | P1 | Ratio (12,3)/17 | flag=12,block=3,total=17 | ratio=0.8824 | test_profiling_phase2_part_1.py |
| TC-PRF-2865 | P1 | Ratio (12,4)/20 | flag=12,block=4,total=20 | ratio=0.8000 | test_profiling_phase2_part_1.py |
| TC-PRF-2866 | P1 | Ratio (13,0)/14 | flag=13,block=0,total=14 | ratio=0.9286 | test_profiling_phase2_part_1.py |
| TC-PRF-2867 | P1 | Ratio (13,1)/18 | flag=13,block=1,total=18 | ratio=0.7778 | test_profiling_phase2_part_1.py |
| TC-PRF-2868 | P1 | Ratio (13,2)/17 | flag=13,block=2,total=17 | ratio=0.8824 | test_profiling_phase2_part_1.py |
| TC-PRF-2869 | P1 | Ratio (13,3)/21 | flag=13,block=3,total=21 | ratio=0.7619 | test_profiling_phase2_part_1.py |
| TC-PRF-2870 | P1 | Ratio (13,4)/20 | flag=13,block=4,total=20 | ratio=0.8500 | test_profiling_phase2_part_1.py |
| TC-PRF-2871 | P1 | Ratio (14,0)/15 | flag=14,block=0,total=15 | ratio=0.9333 | test_profiling_phase2_part_1.py |
| TC-PRF-2872 | P1 | Ratio (14,1)/20 | flag=14,block=1,total=20 | ratio=0.7500 | test_profiling_phase2_part_1.py |
| TC-PRF-2873 | P1 | Ratio (14,2)/20 | flag=14,block=2,total=20 | ratio=0.8000 | test_profiling_phase2_part_1.py |
| TC-PRF-2874 | P1 | Ratio (14,3)/20 | flag=14,block=3,total=20 | ratio=0.8500 | test_profiling_phase2_part_1.py |
| TC-PRF-2875 | P1 | Ratio (14,4)/20 | flag=14,block=4,total=20 | ratio=0.9000 | test_profiling_phase2_part_1.py |
| TC-PRF-2876 | P1 | Ratio (15,0)/16 | flag=15,block=0,total=16 | ratio=0.9375 | test_profiling_phase2_part_1.py |
| TC-PRF-2877 | P1 | Ratio (15,1)/17 | flag=15,block=1,total=17 | ratio=0.9412 | test_profiling_phase2_part_1.py |
| TC-PRF-2878 | P1 | Ratio (15,2)/18 | flag=15,block=2,total=18 | ratio=0.9444 | test_profiling_phase2_part_1.py |
| TC-PRF-2879 | P1 | Ratio (15,3)/19 | flag=15,block=3,total=19 | ratio=0.9474 | test_profiling_phase2_part_1.py |
| TC-PRF-2880 | P1 | Ratio (15,4)/20 | flag=15,block=4,total=20 | ratio=0.9500 | test_profiling_phase2_part_1.py |
| TC-PRF-2881 | P1 | Ratio (16,0)/17 | flag=16,block=0,total=17 | ratio=0.9412 | test_profiling_phase2_part_1.py |
| TC-PRF-2882 | P1 | Ratio (16,1)/19 | flag=16,block=1,total=19 | ratio=0.8947 | test_profiling_phase2_part_1.py |
| TC-PRF-2883 | P1 | Ratio (16,2)/21 | flag=16,block=2,total=21 | ratio=0.8571 | test_profiling_phase2_part_1.py |
| TC-PRF-2884 | P1 | Ratio (16,3)/23 | flag=16,block=3,total=23 | ratio=0.8261 | test_profiling_phase2_part_1.py |
| TC-PRF-2885 | P1 | Ratio (16,4)/25 | flag=16,block=4,total=25 | ratio=0.8000 | test_profiling_phase2_part_1.py |
| TC-PRF-2886 | P1 | Ratio (17,0)/18 | flag=17,block=0,total=18 | ratio=0.9444 | test_profiling_phase2_part_1.py |
| TC-PRF-2887 | P1 | Ratio (17,1)/21 | flag=17,block=1,total=21 | ratio=0.8571 | test_profiling_phase2_part_1.py |
| TC-PRF-2888 | P1 | Ratio (17,2)/24 | flag=17,block=2,total=24 | ratio=0.7917 | test_profiling_phase2_part_1.py |
| TC-PRF-2889 | P1 | Ratio (17,3)/22 | flag=17,block=3,total=22 | ratio=0.9091 | test_profiling_phase2_part_1.py |
| TC-PRF-2890 | P1 | Ratio (17,4)/25 | flag=17,block=4,total=25 | ratio=0.8400 | test_profiling_phase2_part_1.py |
| TC-PRF-2891 | P1 | Ratio (18,0)/19 | flag=18,block=0,total=19 | ratio=0.9474 | test_profiling_phase2_part_1.py |
| TC-PRF-2892 | P1 | Ratio (18,1)/23 | flag=18,block=1,total=23 | ratio=0.8261 | test_profiling_phase2_part_1.py |
| TC-PRF-2893 | P1 | Ratio (18,2)/22 | flag=18,block=2,total=22 | ratio=0.9091 | test_profiling_phase2_part_1.py |
| TC-PRF-2894 | P1 | Ratio (18,3)/26 | flag=18,block=3,total=26 | ratio=0.8077 | test_profiling_phase2_part_1.py |
| TC-PRF-2895 | P1 | Ratio (18,4)/25 | flag=18,block=4,total=25 | ratio=0.8800 | test_profiling_phase2_part_1.py |
| TC-PRF-2896 | P1 | Ratio (19,0)/20 | flag=19,block=0,total=20 | ratio=0.9500 | test_profiling_phase2_part_1.py |
| TC-PRF-2897 | P1 | Ratio (19,1)/25 | flag=19,block=1,total=25 | ratio=0.8000 | test_profiling_phase2_part_1.py |
| TC-PRF-2898 | P1 | Ratio (19,2)/25 | flag=19,block=2,total=25 | ratio=0.8400 | test_profiling_phase2_part_1.py |
| TC-PRF-2899 | P1 | Ratio (19,3)/25 | flag=19,block=3,total=25 | ratio=0.8800 | test_profiling_phase2_part_1.py |
| TC-PRF-2900 | P1 | Ratio (19,4)/25 | flag=19,block=4,total=25 | ratio=0.9200 | test_profiling_phase2_part_1.py |
| TC-PRF-2901 | P1 | Ratio (20,0)/21 | flag=20,block=0,total=21 | ratio=0.9524 | test_profiling_phase2_part_2.py |
| TC-PRF-2902 | P1 | Ratio (20,1)/22 | flag=20,block=1,total=22 | ratio=0.9545 | test_profiling_phase2_part_2.py |
| TC-PRF-2903 | P1 | Ratio (20,2)/23 | flag=20,block=2,total=23 | ratio=0.9565 | test_profiling_phase2_part_2.py |
| TC-PRF-2904 | P1 | Ratio (20,3)/24 | flag=20,block=3,total=24 | ratio=0.9583 | test_profiling_phase2_part_2.py |
| TC-PRF-2905 | P1 | Ratio (20,4)/25 | flag=20,block=4,total=25 | ratio=0.9600 | test_profiling_phase2_part_2.py |
| TC-PRF-2906 | P1 | Ratio (21,0)/22 | flag=21,block=0,total=22 | ratio=0.9545 | test_profiling_phase2_part_2.py |
| TC-PRF-2907 | P1 | Ratio (21,1)/24 | flag=21,block=1,total=24 | ratio=0.9167 | test_profiling_phase2_part_2.py |
| TC-PRF-2908 | P1 | Ratio (21,2)/26 | flag=21,block=2,total=26 | ratio=0.8846 | test_profiling_phase2_part_2.py |
| TC-PRF-2909 | P1 | Ratio (21,3)/28 | flag=21,block=3,total=28 | ratio=0.8571 | test_profiling_phase2_part_2.py |
| TC-PRF-2910 | P1 | Ratio (21,4)/30 | flag=21,block=4,total=30 | ratio=0.8333 | test_profiling_phase2_part_2.py |
| TC-PRF-2911 | P1 | Ratio (22,0)/23 | flag=22,block=0,total=23 | ratio=0.9565 | test_profiling_phase2_part_2.py |
| TC-PRF-2912 | P1 | Ratio (22,1)/26 | flag=22,block=1,total=26 | ratio=0.8846 | test_profiling_phase2_part_2.py |
| TC-PRF-2913 | P1 | Ratio (22,2)/29 | flag=22,block=2,total=29 | ratio=0.8276 | test_profiling_phase2_part_2.py |
| TC-PRF-2914 | P1 | Ratio (22,3)/27 | flag=22,block=3,total=27 | ratio=0.9259 | test_profiling_phase2_part_2.py |
| TC-PRF-2915 | P1 | Ratio (22,4)/30 | flag=22,block=4,total=30 | ratio=0.8667 | test_profiling_phase2_part_2.py |
| TC-PRF-2916 | P1 | Ratio (23,0)/24 | flag=23,block=0,total=24 | ratio=0.9583 | test_profiling_phase2_part_2.py |
| TC-PRF-2917 | P1 | Ratio (23,1)/28 | flag=23,block=1,total=28 | ratio=0.8571 | test_profiling_phase2_part_2.py |
| TC-PRF-2918 | P1 | Ratio (23,2)/27 | flag=23,block=2,total=27 | ratio=0.9259 | test_profiling_phase2_part_2.py |
| TC-PRF-2919 | P1 | Ratio (23,3)/31 | flag=23,block=3,total=31 | ratio=0.8387 | test_profiling_phase2_part_2.py |
| TC-PRF-2920 | P1 | Ratio (23,4)/30 | flag=23,block=4,total=30 | ratio=0.9000 | test_profiling_phase2_part_2.py |
| TC-PRF-2921 | P1 | Ratio (24,0)/25 | flag=24,block=0,total=25 | ratio=0.9600 | test_profiling_phase2_part_2.py |
| TC-PRF-2922 | P1 | Ratio (24,1)/30 | flag=24,block=1,total=30 | ratio=0.8333 | test_profiling_phase2_part_2.py |
| TC-PRF-2923 | P1 | Ratio (24,2)/30 | flag=24,block=2,total=30 | ratio=0.8667 | test_profiling_phase2_part_2.py |
| TC-PRF-2924 | P1 | Ratio (24,3)/30 | flag=24,block=3,total=30 | ratio=0.9000 | test_profiling_phase2_part_2.py |
| TC-PRF-2925 | P1 | Ratio (24,4)/30 | flag=24,block=4,total=30 | ratio=0.9333 | test_profiling_phase2_part_2.py |
| TC-PRF-2926 | P1 | Ratio (25,0)/26 | flag=25,block=0,total=26 | ratio=0.9615 | test_profiling_phase2_part_2.py |
| TC-PRF-2927 | P1 | Ratio (30,1)/32 | flag=30,block=1,total=32 | ratio=0.9688 | test_profiling_phase2_part_2.py |
| TC-PRF-2928 | P1 | Ratio (40,5)/46 | flag=40,block=5,total=46 | ratio=0.9783 | test_profiling_phase2_part_2.py |
| TC-PRF-2929 | P1 | Ratio (50,10)/61 | flag=50,block=10,total=61 | ratio=0.9836 | test_profiling_phase2_part_2.py |
| TC-PRF-2930 | P1 | Ratio (75,20)/96 | flag=75,block=20,total=96 | ratio=0.9896 | test_profiling_phase2_part_2.py |
| TC-PRF-2931 | P1 | Ratio (100,50)/151 | flag=100,block=50,total=151 | ratio=0.9934 | test_profiling_phase2_part_2.py |
| TC-PRF-2932 | P1 | Ratio (60,0)/61 | flag=60,block=0,total=61 | ratio=0.9836 | test_profiling_phase2_part_2.py |
| TC-PRF-2933 | P1 | Ratio (80,1)/82 | flag=80,block=1,total=82 | ratio=0.9878 | test_profiling_phase2_part_2.py |
| TC-PRF-2934 | P1 | Ratio (2,5)/9 | flag=2,block=5,total=9 | ratio=0.7778 | test_profiling_phase2_part_2.py |
| TC-PRF-2935 | P1 | Ratio (2,7)/11 | flag=2,block=7,total=11 | ratio=0.8182 | test_profiling_phase2_part_2.py |
| TC-PRF-2936 | P1 | Ratio (2,9)/13 | flag=2,block=9,total=13 | ratio=0.8462 | test_profiling_phase2_part_2.py |
| TC-PRF-2937 | P1 | Ratio (2,11)/15 | flag=2,block=11,total=15 | ratio=0.8667 | test_profiling_phase2_part_2.py |
| TC-PRF-2938 | P1 | Ratio (4,5)/11 | flag=4,block=5,total=11 | ratio=0.8182 | test_profiling_phase2_part_2.py |
| TC-PRF-2939 | P1 | Ratio (4,7)/13 | flag=4,block=7,total=13 | ratio=0.8462 | test_profiling_phase2_part_2.py |
| TC-PRF-2940 | P1 | Ratio (4,9)/15 | flag=4,block=9,total=15 | ratio=0.8667 | test_profiling_phase2_part_2.py |
| TC-PRF-2941 | P1 | Ratio (4,11)/17 | flag=4,block=11,total=17 | ratio=0.8824 | test_profiling_phase2_part_2.py |
| TC-PRF-2942 | P1 | Ratio (6,5)/13 | flag=6,block=5,total=13 | ratio=0.8462 | test_profiling_phase2_part_2.py |
| TC-PRF-2943 | P1 | Ratio (6,7)/15 | flag=6,block=7,total=15 | ratio=0.8667 | test_profiling_phase2_part_2.py |
| TC-PRF-2944 | P1 | Ratio (6,9)/17 | flag=6,block=9,total=17 | ratio=0.8824 | test_profiling_phase2_part_2.py |
| TC-PRF-2945 | P1 | Ratio (6,11)/19 | flag=6,block=11,total=19 | ratio=0.8947 | test_profiling_phase2_part_2.py |
| TC-PRF-2946 | P1 | Ratio (8,5)/15 | flag=8,block=5,total=15 | ratio=0.8667 | test_profiling_phase2_part_2.py |
| TC-PRF-2947 | P1 | Ratio (8,7)/17 | flag=8,block=7,total=17 | ratio=0.8824 | test_profiling_phase2_part_2.py |
| TC-PRF-2948 | P1 | Ratio (8,9)/19 | flag=8,block=9,total=19 | ratio=0.8947 | test_profiling_phase2_part_2.py |
| TC-PRF-2949 | P1 | Ratio (8,11)/21 | flag=8,block=11,total=21 | ratio=0.9048 | test_profiling_phase2_part_2.py |
| TC-PRF-2950 | P1 | Ratio (10,5)/17 | flag=10,block=5,total=17 | ratio=0.8824 | test_profiling_phase2_part_2.py |
| TC-PRF-2951 | P1 | Ratio (10,7)/19 | flag=10,block=7,total=19 | ratio=0.8947 | test_profiling_phase2_part_2.py |
| TC-PRF-2952 | P1 | Ratio (10,9)/21 | flag=10,block=9,total=21 | ratio=0.9048 | test_profiling_phase2_part_2.py |
| TC-PRF-2953 | P1 | Ratio (10,11)/23 | flag=10,block=11,total=23 | ratio=0.9130 | test_profiling_phase2_part_2.py |
| TC-PRF-2954 | P1 | Ratio (12,5)/19 | flag=12,block=5,total=19 | ratio=0.8947 | test_profiling_phase2_part_2.py |
| TC-PRF-2955 | P1 | Ratio (12,7)/21 | flag=12,block=7,total=21 | ratio=0.9048 | test_profiling_phase2_part_2.py |
| TC-PRF-2956 | P1 | Ratio (12,9)/23 | flag=12,block=9,total=23 | ratio=0.9130 | test_profiling_phase2_part_2.py |
| TC-PRF-2957 | P1 | Ratio (12,11)/25 | flag=12,block=11,total=25 | ratio=0.9200 | test_profiling_phase2_part_2.py |
| TC-PRF-2958 | P1 | Ratio (14,5)/21 | flag=14,block=5,total=21 | ratio=0.9048 | test_profiling_phase2_part_2.py |
| TC-PRF-2959 | P1 | Ratio (14,7)/23 | flag=14,block=7,total=23 | ratio=0.9130 | test_profiling_phase2_part_2.py |
| TC-PRF-2960 | P1 | Ratio (14,9)/25 | flag=14,block=9,total=25 | ratio=0.9200 | test_profiling_phase2_part_2.py |
| TC-PRF-2961 | P1 | Ratio (14,11)/27 | flag=14,block=11,total=27 | ratio=0.9259 | test_profiling_phase2_part_2.py |
| TC-PRF-2962 | P1 | Ratio (16,5)/23 | flag=16,block=5,total=23 | ratio=0.9130 | test_profiling_phase2_part_2.py |
| TC-PRF-2963 | P1 | Ratio (16,7)/25 | flag=16,block=7,total=25 | ratio=0.9200 | test_profiling_phase2_part_2.py |
| TC-PRF-2964 | P1 | Ratio (16,9)/27 | flag=16,block=9,total=27 | ratio=0.9259 | test_profiling_phase2_part_2.py |
| TC-PRF-2965 | P1 | Ratio (16,11)/29 | flag=16,block=11,total=29 | ratio=0.9310 | test_profiling_phase2_part_2.py |
| TC-PRF-2966 | P1 | Ratio (18,5)/25 | flag=18,block=5,total=25 | ratio=0.9200 | test_profiling_phase2_part_2.py |
| TC-PRF-2967 | P1 | Ratio (18,7)/27 | flag=18,block=7,total=27 | ratio=0.9259 | test_profiling_phase2_part_2.py |
| TC-PRF-2968 | P1 | Ratio (18,9)/29 | flag=18,block=9,total=29 | ratio=0.9310 | test_profiling_phase2_part_2.py |
| TC-PRF-2969 | P1 | Ratio (18,11)/31 | flag=18,block=11,total=31 | ratio=0.9355 | test_profiling_phase2_part_2.py |
| TC-PRF-2970 | P1 | Ratio (1,6)/10 | flag=1,block=6,total=10 | ratio=0.7000 | test_profiling_phase2_part_2.py |
| TC-PRF-2971 | P1 | Ratio (1,8)/12 | flag=1,block=8,total=12 | ratio=0.7500 | test_profiling_phase2_part_2.py |
| TC-PRF-2972 | P1 | Ratio (1,10)/14 | flag=1,block=10,total=14 | ratio=0.7857 | test_profiling_phase2_part_2.py |
| TC-PRF-2973 | P1 | Ratio (1,12)/16 | flag=1,block=12,total=16 | ratio=0.8125 | test_profiling_phase2_part_2.py |
| TC-PRF-2974 | P1 | Ratio (3,6)/12 | flag=3,block=6,total=12 | ratio=0.7500 | test_profiling_phase2_part_2.py |
| TC-PRF-2975 | P1 | Ratio (3,8)/14 | flag=3,block=8,total=14 | ratio=0.7857 | test_profiling_phase2_part_2.py |
| TC-PRF-2976 | P1 | Ratio (3,10)/16 | flag=3,block=10,total=16 | ratio=0.8125 | test_profiling_phase2_part_2.py |
| TC-PRF-2977 | P1 | Ratio (3,12)/18 | flag=3,block=12,total=18 | ratio=0.8333 | test_profiling_phase2_part_2.py |
| TC-PRF-2978 | P1 | Ratio (5,6)/14 | flag=5,block=6,total=14 | ratio=0.7857 | test_profiling_phase2_part_2.py |
| TC-PRF-2979 | P1 | Ratio (5,8)/16 | flag=5,block=8,total=16 | ratio=0.8125 | test_profiling_phase2_part_2.py |
| TC-PRF-2980 | P1 | Ratio (5,10)/18 | flag=5,block=10,total=18 | ratio=0.8333 | test_profiling_phase2_part_2.py |
| TC-PRF-2981 | P1 | Ratio (5,12)/20 | flag=5,block=12,total=20 | ratio=0.8500 | test_profiling_phase2_part_2.py |
| TC-PRF-2982 | P1 | Ratio (7,6)/16 | flag=7,block=6,total=16 | ratio=0.8125 | test_profiling_phase2_part_2.py |
| TC-PRF-2983 | P1 | Ratio (7,8)/18 | flag=7,block=8,total=18 | ratio=0.8333 | test_profiling_phase2_part_2.py |
| TC-PRF-2984 | P1 | Ratio (7,10)/20 | flag=7,block=10,total=20 | ratio=0.8500 | test_profiling_phase2_part_2.py |
| TC-PRF-2985 | P1 | Ratio (7,12)/22 | flag=7,block=12,total=22 | ratio=0.8636 | test_profiling_phase2_part_2.py |
| TC-PRF-2986 | P1 | Ratio (9,6)/18 | flag=9,block=6,total=18 | ratio=0.8333 | test_profiling_phase2_part_2.py |
| TC-PRF-2987 | P1 | Ratio (9,8)/20 | flag=9,block=8,total=20 | ratio=0.8500 | test_profiling_phase2_part_2.py |
| TC-PRF-2988 | P1 | Ratio (9,10)/22 | flag=9,block=10,total=22 | ratio=0.8636 | test_profiling_phase2_part_2.py |
| TC-PRF-2989 | P1 | Ratio (9,12)/24 | flag=9,block=12,total=24 | ratio=0.8750 | test_profiling_phase2_part_2.py |
| TC-PRF-2990 | P1 | Ratio (11,6)/20 | flag=11,block=6,total=20 | ratio=0.8500 | test_profiling_phase2_part_2.py |
| TC-PRF-2991 | P1 | Ratio (11,8)/22 | flag=11,block=8,total=22 | ratio=0.8636 | test_profiling_phase2_part_2.py |
| TC-PRF-2992 | P1 | Ratio (11,10)/24 | flag=11,block=10,total=24 | ratio=0.8750 | test_profiling_phase2_part_2.py |
| TC-PRF-2993 | P1 | Ratio (11,12)/26 | flag=11,block=12,total=26 | ratio=0.8846 | test_profiling_phase2_part_2.py |
| TC-PRF-2994 | P1 | Ratio (13,6)/22 | flag=13,block=6,total=22 | ratio=0.8636 | test_profiling_phase2_part_2.py |
| TC-PRF-2995 | P1 | Ratio (13,8)/24 | flag=13,block=8,total=24 | ratio=0.8750 | test_profiling_phase2_part_2.py |
| TC-PRF-2996 | P1 | Ratio (13,10)/26 | flag=13,block=10,total=26 | ratio=0.8846 | test_profiling_phase2_part_2.py |
| TC-PRF-2997 | P1 | Ratio (13,12)/28 | flag=13,block=12,total=28 | ratio=0.8929 | test_profiling_phase2_part_2.py |
| TC-PRF-2998 | P1 | Ratio (15,6)/24 | flag=15,block=6,total=24 | ratio=0.8750 | test_profiling_phase2_part_2.py |
| TC-PRF-2999 | P1 | Ratio (15,8)/26 | flag=15,block=8,total=26 | ratio=0.8846 | test_profiling_phase2_part_2.py |
| TC-PRF-3000 | P1 | Ratio (15,10)/28 | flag=15,block=10,total=28 | ratio=0.8929 | test_profiling_phase2_part_2.py |
| TC-PRF-3001 | P1 | Window 1 flagged=0 | window=1,flag=0 | ratio=0.0000 | test_profiling_phase2_part_3.py |
| TC-PRF-3002 | P1 | Window 1 flagged=1 | window=1,flag=1 | ratio=0.5000 | test_profiling_phase2_part_3.py |
| TC-PRF-3003 | P2 | Window 1 flagged=2 | window=1,flag=2 | ratio=0.5000 | test_profiling_phase2_part_3.py |
| TC-PRF-3004 | P2 | Window 1 flagged=3 | window=1,flag=3 | ratio=0.7500 | test_profiling_phase2_part_3.py |
| TC-PRF-3005 | P2 | Window 1 boundary | window=1,days=1 | summaries=1 | test_profiling_phase2_part_3.py |
| TC-PRF-3006 | P1 | Window 2 flagged=0 | window=2,flag=0 | ratio=0.0000 | test_profiling_phase2_part_3.py |
| TC-PRF-3007 | P1 | Window 2 flagged=1 | window=2,flag=1 | ratio=0.5000 | test_profiling_phase2_part_3.py |
| TC-PRF-3008 | P2 | Window 2 flagged=2 | window=2,flag=2 | ratio=0.5000 | test_profiling_phase2_part_3.py |
| TC-PRF-3009 | P2 | Window 2 flagged=3 | window=2,flag=3 | ratio=0.7500 | test_profiling_phase2_part_3.py |
| TC-PRF-3010 | P2 | Window 2 boundary | window=2,days=2 | summaries=1 | test_profiling_phase2_part_3.py |
| TC-PRF-3011 | P1 | Window 3 flagged=0 | window=3,flag=0 | ratio=0.0000 | test_profiling_phase2_part_3.py |
| TC-PRF-3012 | P1 | Window 3 flagged=1 | window=3,flag=1 | ratio=0.5000 | test_profiling_phase2_part_3.py |
| TC-PRF-3013 | P2 | Window 3 flagged=2 | window=3,flag=2 | ratio=0.5000 | test_profiling_phase2_part_3.py |
| TC-PRF-3014 | P2 | Window 3 flagged=3 | window=3,flag=3 | ratio=0.7500 | test_profiling_phase2_part_3.py |
| TC-PRF-3015 | P2 | Window 3 boundary | window=3,days=3 | summaries=1 | test_profiling_phase2_part_3.py |
| TC-PRF-3016 | P1 | Window 4 flagged=0 | window=4,flag=0 | ratio=0.0000 | test_profiling_phase2_part_3.py |
| TC-PRF-3017 | P1 | Window 4 flagged=1 | window=4,flag=1 | ratio=0.5000 | test_profiling_phase2_part_3.py |
| TC-PRF-3018 | P2 | Window 4 flagged=2 | window=4,flag=2 | ratio=0.5000 | test_profiling_phase2_part_3.py |
| TC-PRF-3019 | P2 | Window 4 flagged=3 | window=4,flag=3 | ratio=0.7500 | test_profiling_phase2_part_3.py |
| TC-PRF-3020 | P2 | Window 4 boundary | window=4,days=4 | summaries=1 | test_profiling_phase2_part_3.py |
| TC-PRF-3021 | P1 | Window 5 flagged=0 | window=5,flag=0 | ratio=0.0000 | test_profiling_phase2_part_3.py |
| TC-PRF-3022 | P1 | Window 5 flagged=1 | window=5,flag=1 | ratio=0.5000 | test_profiling_phase2_part_3.py |
| TC-PRF-3023 | P2 | Window 5 flagged=2 | window=5,flag=2 | ratio=0.5000 | test_profiling_phase2_part_3.py |
| TC-PRF-3024 | P2 | Window 5 flagged=3 | window=5,flag=3 | ratio=0.7500 | test_profiling_phase2_part_3.py |
| TC-PRF-3025 | P2 | Window 5 boundary | window=5,days=5 | summaries=1 | test_profiling_phase2_part_3.py |
| TC-PRF-3026 | P1 | Window 6 flagged=0 | window=6,flag=0 | ratio=0.0000 | test_profiling_phase2_part_3.py |
| TC-PRF-3027 | P1 | Window 6 flagged=1 | window=6,flag=1 | ratio=0.5000 | test_profiling_phase2_part_3.py |
| TC-PRF-3028 | P2 | Window 6 flagged=2 | window=6,flag=2 | ratio=0.5000 | test_profiling_phase2_part_3.py |
| TC-PRF-3029 | P2 | Window 6 flagged=3 | window=6,flag=3 | ratio=0.7500 | test_profiling_phase2_part_3.py |
| TC-PRF-3030 | P2 | Window 6 boundary | window=6,days=6 | summaries=1 | test_profiling_phase2_part_3.py |
| TC-PRF-3031 | P1 | Window 7 flagged=0 | window=7,flag=0 | ratio=0.0000 | test_profiling_phase2_part_3.py |
| TC-PRF-3032 | P1 | Window 7 flagged=1 | window=7,flag=1 | ratio=0.5000 | test_profiling_phase2_part_3.py |
| TC-PRF-3033 | P2 | Window 7 flagged=2 | window=7,flag=2 | ratio=0.5000 | test_profiling_phase2_part_3.py |
| TC-PRF-3034 | P2 | Window 7 flagged=3 | window=7,flag=3 | ratio=0.7500 | test_profiling_phase2_part_3.py |
| TC-PRF-3035 | P2 | Window 7 boundary | window=7,days=7 | summaries=1 | test_profiling_phase2_part_3.py |
| TC-PRF-3036 | P1 | Window 10 flagged=0 | window=10,flag=0 | ratio=0.0000 | test_profiling_phase2_part_3.py |
| TC-PRF-3037 | P1 | Window 10 flagged=1 | window=10,flag=1 | ratio=0.5000 | test_profiling_phase2_part_3.py |
| TC-PRF-3038 | P2 | Window 10 flagged=2 | window=10,flag=2 | ratio=0.5000 | test_profiling_phase2_part_3.py |
| TC-PRF-3039 | P2 | Window 10 flagged=3 | window=10,flag=3 | ratio=0.7500 | test_profiling_phase2_part_3.py |
| TC-PRF-3040 | P2 | Window 10 boundary | window=10,days=10 | summaries=1 | test_profiling_phase2_part_3.py |
| TC-PRF-3041 | P1 | Window 14 flagged=0 | window=14,flag=0 | ratio=0.0000 | test_profiling_phase2_part_3.py |
| TC-PRF-3042 | P1 | Window 14 flagged=1 | window=14,flag=1 | ratio=0.5000 | test_profiling_phase2_part_3.py |
| TC-PRF-3043 | P2 | Window 14 flagged=2 | window=14,flag=2 | ratio=0.5000 | test_profiling_phase2_part_3.py |
| TC-PRF-3044 | P2 | Window 14 flagged=3 | window=14,flag=3 | ratio=0.7500 | test_profiling_phase2_part_3.py |
| TC-PRF-3045 | P2 | Window 14 boundary | window=14,days=14 | summaries=1 | test_profiling_phase2_part_3.py |
| TC-PRF-3046 | P1 | Window 15 flagged=0 | window=15,flag=0 | ratio=0.0000 | test_profiling_phase2_part_3.py |
| TC-PRF-3047 | P1 | Window 15 flagged=1 | window=15,flag=1 | ratio=0.5000 | test_profiling_phase2_part_3.py |
| TC-PRF-3048 | P2 | Window 15 flagged=2 | window=15,flag=2 | ratio=0.5000 | test_profiling_phase2_part_3.py |
| TC-PRF-3049 | P2 | Window 15 flagged=3 | window=15,flag=3 | ratio=0.7500 | test_profiling_phase2_part_3.py |
| TC-PRF-3050 | P2 | Window 15 boundary | window=15,days=15 | summaries=1 | test_profiling_phase2_part_3.py |
| TC-PRF-3051 | P1 | Window 21 flagged=0 | window=21,flag=0 | ratio=0.0000 | test_profiling_phase2_part_3.py |
| TC-PRF-3052 | P1 | Window 21 flagged=1 | window=21,flag=1 | ratio=0.5000 | test_profiling_phase2_part_3.py |
| TC-PRF-3053 | P2 | Window 21 flagged=2 | window=21,flag=2 | ratio=0.5000 | test_profiling_phase2_part_3.py |
| TC-PRF-3054 | P2 | Window 21 flagged=3 | window=21,flag=3 | ratio=0.7500 | test_profiling_phase2_part_3.py |
| TC-PRF-3055 | P2 | Window 21 boundary | window=21,days=21 | summaries=1 | test_profiling_phase2_part_3.py |
| TC-PRF-3056 | P1 | Window 28 flagged=0 | window=28,flag=0 | ratio=0.0000 | test_profiling_phase2_part_3.py |
| TC-PRF-3057 | P1 | Window 28 flagged=1 | window=28,flag=1 | ratio=0.5000 | test_profiling_phase2_part_3.py |
| TC-PRF-3058 | P2 | Window 28 flagged=2 | window=28,flag=2 | ratio=0.5000 | test_profiling_phase2_part_3.py |
| TC-PRF-3059 | P2 | Window 28 flagged=3 | window=28,flag=3 | ratio=0.7500 | test_profiling_phase2_part_3.py |
| TC-PRF-3060 | P2 | Window 28 boundary | window=28,days=28 | summaries=1 | test_profiling_phase2_part_3.py |
| TC-PRF-3061 | P1 | Window 30 flagged=0 | window=30,flag=0 | ratio=0.0000 | test_profiling_phase2_part_3.py |
| TC-PRF-3062 | P1 | Window 30 flagged=1 | window=30,flag=1 | ratio=0.5000 | test_profiling_phase2_part_3.py |
| TC-PRF-3063 | P2 | Window 30 flagged=2 | window=30,flag=2 | ratio=0.5000 | test_profiling_phase2_part_3.py |
| TC-PRF-3064 | P2 | Window 30 flagged=3 | window=30,flag=3 | ratio=0.7500 | test_profiling_phase2_part_3.py |
| TC-PRF-3065 | P2 | Window 30 boundary | window=30,days=30 | summaries=1 | test_profiling_phase2_part_3.py |
| TC-PRF-3066 | P1 | Window 45 flagged=0 | window=45,flag=0 | ratio=0.0000 | test_profiling_phase2_part_3.py |
| TC-PRF-3067 | P1 | Window 45 flagged=1 | window=45,flag=1 | ratio=0.5000 | test_profiling_phase2_part_3.py |
| TC-PRF-3068 | P2 | Window 45 flagged=2 | window=45,flag=2 | ratio=0.5000 | test_profiling_phase2_part_3.py |
| TC-PRF-3069 | P2 | Window 45 flagged=3 | window=45,flag=3 | ratio=0.7500 | test_profiling_phase2_part_3.py |
| TC-PRF-3070 | P2 | Window 45 boundary | window=45,days=45 | summaries=1 | test_profiling_phase2_part_3.py |
| TC-PRF-3071 | P1 | Window 60 flagged=0 | window=60,flag=0 | ratio=0.0000 | test_profiling_phase2_part_3.py |
| TC-PRF-3072 | P1 | Window 60 flagged=1 | window=60,flag=1 | ratio=0.5000 | test_profiling_phase2_part_3.py |
| TC-PRF-3073 | P2 | Window 60 flagged=2 | window=60,flag=2 | ratio=0.5000 | test_profiling_phase2_part_3.py |
| TC-PRF-3074 | P2 | Window 60 flagged=3 | window=60,flag=3 | ratio=0.7500 | test_profiling_phase2_part_3.py |
| TC-PRF-3075 | P2 | Window 60 boundary | window=60,days=60 | summaries=1 | test_profiling_phase2_part_3.py |
| TC-PRF-3076 | P1 | Window 90 flagged=0 | window=90,flag=0 | ratio=0.0000 | test_profiling_phase2_part_3.py |
| TC-PRF-3077 | P1 | Window 90 flagged=1 | window=90,flag=1 | ratio=0.5000 | test_profiling_phase2_part_3.py |
| TC-PRF-3078 | P2 | Window 90 flagged=2 | window=90,flag=2 | ratio=0.5000 | test_profiling_phase2_part_3.py |
| TC-PRF-3079 | P2 | Window 90 flagged=3 | window=90,flag=3 | ratio=0.7500 | test_profiling_phase2_part_3.py |
| TC-PRF-3080 | P2 | Window 90 boundary | window=90,days=90 | summaries=1 | test_profiling_phase2_part_3.py |
| TC-PRF-3081 | P1 | Window 91 flagged=0 | window=91,flag=0 | ratio=0.0000 | test_profiling_phase2_part_3.py |
| TC-PRF-3082 | P1 | Window 91 flagged=1 | window=91,flag=1 | ratio=0.5000 | test_profiling_phase2_part_3.py |
| TC-PRF-3083 | P2 | Window 91 flagged=2 | window=91,flag=2 | ratio=0.5000 | test_profiling_phase2_part_3.py |
| TC-PRF-3084 | P2 | Window 91 flagged=3 | window=91,flag=3 | ratio=0.7500 | test_profiling_phase2_part_3.py |
| TC-PRF-3085 | P2 | Window 91 boundary | window=91,days=91 | summaries=1 | test_profiling_phase2_part_3.py |
| TC-PRF-3086 | P1 | Window 120 flagged=0 | window=120,flag=0 | ratio=0.0000 | test_profiling_phase2_part_3.py |
| TC-PRF-3087 | P1 | Window 120 flagged=1 | window=120,flag=1 | ratio=0.5000 | test_profiling_phase2_part_3.py |
| TC-PRF-3088 | P2 | Window 120 flagged=2 | window=120,flag=2 | ratio=0.5000 | test_profiling_phase2_part_3.py |
| TC-PRF-3089 | P2 | Window 120 flagged=3 | window=120,flag=3 | ratio=0.7500 | test_profiling_phase2_part_3.py |
| TC-PRF-3090 | P2 | Window 120 boundary | window=120,days=120 | summaries=1 | test_profiling_phase2_part_3.py |
| TC-PRF-3091 | P1 | Window 180 flagged=0 | window=180,flag=0 | ratio=0.0000 | test_profiling_phase2_part_3.py |
| TC-PRF-3092 | P1 | Window 180 flagged=1 | window=180,flag=1 | ratio=0.5000 | test_profiling_phase2_part_3.py |
| TC-PRF-3093 | P2 | Window 180 flagged=2 | window=180,flag=2 | ratio=0.5000 | test_profiling_phase2_part_3.py |
| TC-PRF-3094 | P2 | Window 180 flagged=3 | window=180,flag=3 | ratio=0.7500 | test_profiling_phase2_part_3.py |
| TC-PRF-3095 | P2 | Window 180 boundary | window=180,days=180 | summaries=1 | test_profiling_phase2_part_3.py |
| TC-PRF-3096 | P1 | Window 365 flagged=0 | window=365,flag=0 | ratio=0.0000 | test_profiling_phase2_part_3.py |
| TC-PRF-3097 | P1 | Window 365 flagged=1 | window=365,flag=1 | ratio=0.5000 | test_profiling_phase2_part_3.py |
| TC-PRF-3098 | P2 | Window 365 flagged=2 | window=365,flag=2 | ratio=0.5000 | test_profiling_phase2_part_3.py |
| TC-PRF-3099 | P2 | Window 365 flagged=3 | window=365,flag=3 | ratio=0.7500 | test_profiling_phase2_part_3.py |
| TC-PRF-3100 | P2 | Window 365 boundary | window=365,days=365 | summaries=1 | test_profiling_phase2_part_3.py |
| TC-PRF-3101 | P1 | Multi-user 10 pattern 0 | users=10,pattern=0 | summaries=10 | test_profiling_phase2_part_4.py |
| TC-PRF-3102 | P1 | Multi-user 10 pattern 1 | users=10,pattern=1 | summaries=10 | test_profiling_phase2_part_4.py |
| TC-PRF-3103 | P1 | Multi-user 10 pattern 2 | users=10,pattern=2 | summaries=10 | test_profiling_phase2_part_4.py |
| TC-PRF-3104 | P1 | Multi-user 10 pattern 3 | users=10,pattern=3 | summaries=10 | test_profiling_phase2_part_4.py |
| TC-PRF-3105 | P1 | Multi-user 10 pattern 4 | users=10,pattern=4 | summaries=10 | test_profiling_phase2_part_4.py |
| TC-PRF-3106 | P1 | Multi-user 10 pattern 5 | users=10,pattern=5 | summaries=10 | test_profiling_phase2_part_4.py |
| TC-PRF-3107 | P1 | Multi-user 10 pattern 6 | users=10,pattern=6 | summaries=10 | test_profiling_phase2_part_4.py |
| TC-PRF-3108 | P1 | Multi-user 10 pattern 7 | users=10,pattern=7 | summaries=10 | test_profiling_phase2_part_4.py |
| TC-PRF-3109 | P1 | Multi-user 10 pattern 8 | users=10,pattern=8 | summaries=10 | test_profiling_phase2_part_4.py |
| TC-PRF-3110 | P1 | Multi-user 10 pattern 9 | users=10,pattern=9 | summaries=10 | test_profiling_phase2_part_4.py |
| TC-PRF-3111 | P1 | Multi-user 10 pattern 10 | users=10,pattern=10 | summaries=10 | test_profiling_phase2_part_4.py |
| TC-PRF-3112 | P1 | Multi-user 10 pattern 11 | users=10,pattern=11 | summaries=10 | test_profiling_phase2_part_4.py |
| TC-PRF-3113 | P1 | Multi-user 10 pattern 12 | users=10,pattern=12 | summaries=10 | test_profiling_phase2_part_4.py |
| TC-PRF-3114 | P1 | Multi-user 10 pattern 13 | users=10,pattern=13 | summaries=10 | test_profiling_phase2_part_4.py |
| TC-PRF-3115 | P1 | Multi-user 10 pattern 14 | users=10,pattern=14 | summaries=10 | test_profiling_phase2_part_4.py |
| TC-PRF-3116 | P1 | Multi-user 10 pattern 15 | users=10,pattern=15 | summaries=10 | test_profiling_phase2_part_4.py |
| TC-PRF-3117 | P1 | Multi-user 10 pattern 16 | users=10,pattern=16 | summaries=10 | test_profiling_phase2_part_4.py |
| TC-PRF-3118 | P1 | Multi-user 10 pattern 17 | users=10,pattern=17 | summaries=10 | test_profiling_phase2_part_4.py |
| TC-PRF-3119 | P1 | Multi-user 10 pattern 18 | users=10,pattern=18 | summaries=10 | test_profiling_phase2_part_4.py |
| TC-PRF-3120 | P1 | Multi-user 10 pattern 19 | users=10,pattern=19 | summaries=10 | test_profiling_phase2_part_4.py |
| TC-PRF-3121 | P1 | Multi-user 25 pattern 0 | users=25,pattern=0 | summaries=25 | test_profiling_phase2_part_4.py |
| TC-PRF-3122 | P1 | Multi-user 25 pattern 1 | users=25,pattern=1 | summaries=25 | test_profiling_phase2_part_4.py |
| TC-PRF-3123 | P1 | Multi-user 25 pattern 2 | users=25,pattern=2 | summaries=25 | test_profiling_phase2_part_4.py |
| TC-PRF-3124 | P1 | Multi-user 25 pattern 3 | users=25,pattern=3 | summaries=25 | test_profiling_phase2_part_4.py |
| TC-PRF-3125 | P1 | Multi-user 25 pattern 4 | users=25,pattern=4 | summaries=25 | test_profiling_phase2_part_4.py |
| TC-PRF-3126 | P1 | Multi-user 25 pattern 5 | users=25,pattern=5 | summaries=25 | test_profiling_phase2_part_4.py |
| TC-PRF-3127 | P1 | Multi-user 25 pattern 6 | users=25,pattern=6 | summaries=25 | test_profiling_phase2_part_4.py |
| TC-PRF-3128 | P1 | Multi-user 25 pattern 7 | users=25,pattern=7 | summaries=25 | test_profiling_phase2_part_4.py |
| TC-PRF-3129 | P1 | Multi-user 25 pattern 8 | users=25,pattern=8 | summaries=25 | test_profiling_phase2_part_4.py |
| TC-PRF-3130 | P1 | Multi-user 25 pattern 9 | users=25,pattern=9 | summaries=25 | test_profiling_phase2_part_4.py |
| TC-PRF-3131 | P1 | Multi-user 25 pattern 10 | users=25,pattern=10 | summaries=25 | test_profiling_phase2_part_4.py |
| TC-PRF-3132 | P1 | Multi-user 25 pattern 11 | users=25,pattern=11 | summaries=25 | test_profiling_phase2_part_4.py |
| TC-PRF-3133 | P1 | Multi-user 25 pattern 12 | users=25,pattern=12 | summaries=25 | test_profiling_phase2_part_4.py |
| TC-PRF-3134 | P1 | Multi-user 25 pattern 13 | users=25,pattern=13 | summaries=25 | test_profiling_phase2_part_4.py |
| TC-PRF-3135 | P1 | Multi-user 25 pattern 14 | users=25,pattern=14 | summaries=25 | test_profiling_phase2_part_4.py |
| TC-PRF-3136 | P1 | Multi-user 25 pattern 15 | users=25,pattern=15 | summaries=25 | test_profiling_phase2_part_4.py |
| TC-PRF-3137 | P1 | Multi-user 25 pattern 16 | users=25,pattern=16 | summaries=25 | test_profiling_phase2_part_4.py |
| TC-PRF-3138 | P1 | Multi-user 25 pattern 17 | users=25,pattern=17 | summaries=25 | test_profiling_phase2_part_4.py |
| TC-PRF-3139 | P1 | Multi-user 25 pattern 18 | users=25,pattern=18 | summaries=25 | test_profiling_phase2_part_4.py |
| TC-PRF-3140 | P1 | Multi-user 25 pattern 19 | users=25,pattern=19 | summaries=25 | test_profiling_phase2_part_4.py |
| TC-PRF-3141 | P1 | Multi-user 50 pattern 0 | users=50,pattern=0 | summaries=50 | test_profiling_phase2_part_4.py |
| TC-PRF-3142 | P1 | Multi-user 50 pattern 1 | users=50,pattern=1 | summaries=50 | test_profiling_phase2_part_4.py |
| TC-PRF-3143 | P1 | Multi-user 50 pattern 2 | users=50,pattern=2 | summaries=50 | test_profiling_phase2_part_4.py |
| TC-PRF-3144 | P1 | Multi-user 50 pattern 3 | users=50,pattern=3 | summaries=50 | test_profiling_phase2_part_4.py |
| TC-PRF-3145 | P1 | Multi-user 50 pattern 4 | users=50,pattern=4 | summaries=50 | test_profiling_phase2_part_4.py |
| TC-PRF-3146 | P1 | Multi-user 50 pattern 5 | users=50,pattern=5 | summaries=50 | test_profiling_phase2_part_4.py |
| TC-PRF-3147 | P1 | Multi-user 50 pattern 6 | users=50,pattern=6 | summaries=50 | test_profiling_phase2_part_4.py |
| TC-PRF-3148 | P1 | Multi-user 50 pattern 7 | users=50,pattern=7 | summaries=50 | test_profiling_phase2_part_4.py |
| TC-PRF-3149 | P1 | Multi-user 50 pattern 8 | users=50,pattern=8 | summaries=50 | test_profiling_phase2_part_4.py |
| TC-PRF-3150 | P1 | Multi-user 50 pattern 9 | users=50,pattern=9 | summaries=50 | test_profiling_phase2_part_4.py |
| TC-PRF-3151 | P1 | Multi-user 50 pattern 10 | users=50,pattern=10 | summaries=50 | test_profiling_phase2_part_4.py |
| TC-PRF-3152 | P1 | Multi-user 50 pattern 11 | users=50,pattern=11 | summaries=50 | test_profiling_phase2_part_4.py |
| TC-PRF-3153 | P1 | Multi-user 50 pattern 12 | users=50,pattern=12 | summaries=50 | test_profiling_phase2_part_4.py |
| TC-PRF-3154 | P1 | Multi-user 50 pattern 13 | users=50,pattern=13 | summaries=50 | test_profiling_phase2_part_4.py |
| TC-PRF-3155 | P1 | Multi-user 50 pattern 14 | users=50,pattern=14 | summaries=50 | test_profiling_phase2_part_4.py |
| TC-PRF-3156 | P1 | Multi-user 50 pattern 15 | users=50,pattern=15 | summaries=50 | test_profiling_phase2_part_4.py |
| TC-PRF-3157 | P1 | Multi-user 50 pattern 16 | users=50,pattern=16 | summaries=50 | test_profiling_phase2_part_4.py |
| TC-PRF-3158 | P1 | Multi-user 50 pattern 17 | users=50,pattern=17 | summaries=50 | test_profiling_phase2_part_4.py |
| TC-PRF-3159 | P1 | Multi-user 50 pattern 18 | users=50,pattern=18 | summaries=50 | test_profiling_phase2_part_4.py |
| TC-PRF-3160 | P1 | Multi-user 50 pattern 19 | users=50,pattern=19 | summaries=50 | test_profiling_phase2_part_4.py |
| TC-PRF-3161 | P1 | Multi-user 100 pattern 0 | users=100,pattern=0 | summaries=100 | test_profiling_phase2_part_4.py |
| TC-PRF-3162 | P1 | Multi-user 100 pattern 1 | users=100,pattern=1 | summaries=100 | test_profiling_phase2_part_4.py |
| TC-PRF-3163 | P1 | Multi-user 100 pattern 2 | users=100,pattern=2 | summaries=100 | test_profiling_phase2_part_4.py |
| TC-PRF-3164 | P1 | Multi-user 100 pattern 3 | users=100,pattern=3 | summaries=100 | test_profiling_phase2_part_4.py |
| TC-PRF-3165 | P1 | Multi-user 100 pattern 4 | users=100,pattern=4 | summaries=100 | test_profiling_phase2_part_4.py |
| TC-PRF-3166 | P1 | Multi-user 100 pattern 5 | users=100,pattern=5 | summaries=100 | test_profiling_phase2_part_4.py |
| TC-PRF-3167 | P1 | Multi-user 100 pattern 6 | users=100,pattern=6 | summaries=100 | test_profiling_phase2_part_4.py |
| TC-PRF-3168 | P1 | Multi-user 100 pattern 7 | users=100,pattern=7 | summaries=100 | test_profiling_phase2_part_4.py |
| TC-PRF-3169 | P1 | Multi-user 100 pattern 8 | users=100,pattern=8 | summaries=100 | test_profiling_phase2_part_4.py |
| TC-PRF-3170 | P1 | Multi-user 100 pattern 9 | users=100,pattern=9 | summaries=100 | test_profiling_phase2_part_4.py |
| TC-PRF-3171 | P1 | Multi-user 100 pattern 10 | users=100,pattern=10 | summaries=100 | test_profiling_phase2_part_4.py |
| TC-PRF-3172 | P1 | Multi-user 100 pattern 11 | users=100,pattern=11 | summaries=100 | test_profiling_phase2_part_4.py |
| TC-PRF-3173 | P1 | Multi-user 100 pattern 12 | users=100,pattern=12 | summaries=100 | test_profiling_phase2_part_4.py |
| TC-PRF-3174 | P1 | Multi-user 100 pattern 13 | users=100,pattern=13 | summaries=100 | test_profiling_phase2_part_4.py |
| TC-PRF-3175 | P1 | Multi-user 100 pattern 14 | users=100,pattern=14 | summaries=100 | test_profiling_phase2_part_4.py |
| TC-PRF-3176 | P1 | Multi-user 100 pattern 15 | users=100,pattern=15 | summaries=100 | test_profiling_phase2_part_4.py |
| TC-PRF-3177 | P1 | Multi-user 100 pattern 16 | users=100,pattern=16 | summaries=100 | test_profiling_phase2_part_4.py |
| TC-PRF-3178 | P1 | Multi-user 100 pattern 17 | users=100,pattern=17 | summaries=100 | test_profiling_phase2_part_4.py |
| TC-PRF-3179 | P1 | Multi-user 100 pattern 18 | users=100,pattern=18 | summaries=100 | test_profiling_phase2_part_4.py |
| TC-PRF-3180 | P1 | Multi-user 100 pattern 19 | users=100,pattern=19 | summaries=100 | test_profiling_phase2_part_4.py |
| TC-PRF-3181 | P1 | Multi-user 250 pattern 0 | users=250,pattern=0 | summaries=250 | test_profiling_phase2_part_4.py |
| TC-PRF-3182 | P1 | Multi-user 250 pattern 1 | users=250,pattern=1 | summaries=250 | test_profiling_phase2_part_4.py |
| TC-PRF-3183 | P1 | Multi-user 250 pattern 2 | users=250,pattern=2 | summaries=250 | test_profiling_phase2_part_4.py |
| TC-PRF-3184 | P1 | Multi-user 250 pattern 3 | users=250,pattern=3 | summaries=250 | test_profiling_phase2_part_4.py |
| TC-PRF-3185 | P1 | Multi-user 250 pattern 4 | users=250,pattern=4 | summaries=250 | test_profiling_phase2_part_4.py |
| TC-PRF-3186 | P1 | Multi-user 250 pattern 5 | users=250,pattern=5 | summaries=250 | test_profiling_phase2_part_4.py |
| TC-PRF-3187 | P1 | Multi-user 250 pattern 6 | users=250,pattern=6 | summaries=250 | test_profiling_phase2_part_4.py |
| TC-PRF-3188 | P1 | Multi-user 250 pattern 7 | users=250,pattern=7 | summaries=250 | test_profiling_phase2_part_4.py |
| TC-PRF-3189 | P1 | Multi-user 250 pattern 8 | users=250,pattern=8 | summaries=250 | test_profiling_phase2_part_4.py |
| TC-PRF-3190 | P1 | Multi-user 250 pattern 9 | users=250,pattern=9 | summaries=250 | test_profiling_phase2_part_4.py |
| TC-PRF-3191 | P1 | Multi-user 250 pattern 10 | users=250,pattern=10 | summaries=250 | test_profiling_phase2_part_4.py |
| TC-PRF-3192 | P1 | Multi-user 250 pattern 11 | users=250,pattern=11 | summaries=250 | test_profiling_phase2_part_4.py |
| TC-PRF-3193 | P1 | Multi-user 250 pattern 12 | users=250,pattern=12 | summaries=250 | test_profiling_phase2_part_4.py |
| TC-PRF-3194 | P1 | Multi-user 250 pattern 13 | users=250,pattern=13 | summaries=250 | test_profiling_phase2_part_4.py |
| TC-PRF-3195 | P1 | Multi-user 250 pattern 14 | users=250,pattern=14 | summaries=250 | test_profiling_phase2_part_4.py |
| TC-PRF-3196 | P1 | Multi-user 250 pattern 15 | users=250,pattern=15 | summaries=250 | test_profiling_phase2_part_4.py |
| TC-PRF-3197 | P1 | Multi-user 250 pattern 16 | users=250,pattern=16 | summaries=250 | test_profiling_phase2_part_4.py |
| TC-PRF-3198 | P1 | Multi-user 250 pattern 17 | users=250,pattern=17 | summaries=250 | test_profiling_phase2_part_4.py |
| TC-PRF-3199 | P1 | Multi-user 250 pattern 18 | users=250,pattern=18 | summaries=250 | test_profiling_phase2_part_4.py |
| TC-PRF-3200 | P1 | Multi-user 250 pattern 19 | users=250,pattern=19 | summaries=250 | test_profiling_phase2_part_4.py |
| TC-PRF-3201 | P1 | Multi-user 500 pattern 0 | users=500,pattern=0 | summaries=500 | test_profiling_phase2_part_5.py |
| TC-PRF-3202 | P1 | Multi-user 500 pattern 1 | users=500,pattern=1 | summaries=500 | test_profiling_phase2_part_5.py |
| TC-PRF-3203 | P1 | Multi-user 500 pattern 2 | users=500,pattern=2 | summaries=500 | test_profiling_phase2_part_5.py |
| TC-PRF-3204 | P1 | Multi-user 500 pattern 3 | users=500,pattern=3 | summaries=500 | test_profiling_phase2_part_5.py |
| TC-PRF-3205 | P1 | Multi-user 500 pattern 4 | users=500,pattern=4 | summaries=500 | test_profiling_phase2_part_5.py |
| TC-PRF-3206 | P1 | Multi-user 500 pattern 5 | users=500,pattern=5 | summaries=500 | test_profiling_phase2_part_5.py |
| TC-PRF-3207 | P1 | Multi-user 500 pattern 6 | users=500,pattern=6 | summaries=500 | test_profiling_phase2_part_5.py |
| TC-PRF-3208 | P1 | Multi-user 500 pattern 7 | users=500,pattern=7 | summaries=500 | test_profiling_phase2_part_5.py |
| TC-PRF-3209 | P1 | Multi-user 500 pattern 8 | users=500,pattern=8 | summaries=500 | test_profiling_phase2_part_5.py |
| TC-PRF-3210 | P1 | Multi-user 500 pattern 9 | users=500,pattern=9 | summaries=500 | test_profiling_phase2_part_5.py |
| TC-PRF-3211 | P1 | Multi-user 500 pattern 10 | users=500,pattern=10 | summaries=500 | test_profiling_phase2_part_5.py |
| TC-PRF-3212 | P1 | Multi-user 500 pattern 11 | users=500,pattern=11 | summaries=500 | test_profiling_phase2_part_5.py |
| TC-PRF-3213 | P1 | Multi-user 500 pattern 12 | users=500,pattern=12 | summaries=500 | test_profiling_phase2_part_5.py |
| TC-PRF-3214 | P1 | Multi-user 500 pattern 13 | users=500,pattern=13 | summaries=500 | test_profiling_phase2_part_5.py |
| TC-PRF-3215 | P1 | Multi-user 500 pattern 14 | users=500,pattern=14 | summaries=500 | test_profiling_phase2_part_5.py |
| TC-PRF-3216 | P1 | Multi-user 500 pattern 15 | users=500,pattern=15 | summaries=500 | test_profiling_phase2_part_5.py |
| TC-PRF-3217 | P1 | Multi-user 500 pattern 16 | users=500,pattern=16 | summaries=500 | test_profiling_phase2_part_5.py |
| TC-PRF-3218 | P1 | Multi-user 500 pattern 17 | users=500,pattern=17 | summaries=500 | test_profiling_phase2_part_5.py |
| TC-PRF-3219 | P1 | Multi-user 500 pattern 18 | users=500,pattern=18 | summaries=500 | test_profiling_phase2_part_5.py |
| TC-PRF-3220 | P1 | Multi-user 500 pattern 19 | users=500,pattern=19 | summaries=500 | test_profiling_phase2_part_5.py |
| TC-PRF-3221 | P1 | Multi-user 1000 pattern 0 | users=1000,pattern=0 | summaries=1000 | test_profiling_phase2_part_5.py |
| TC-PRF-3222 | P1 | Multi-user 1000 pattern 1 | users=1000,pattern=1 | summaries=1000 | test_profiling_phase2_part_5.py |
| TC-PRF-3223 | P1 | Multi-user 1000 pattern 2 | users=1000,pattern=2 | summaries=1000 | test_profiling_phase2_part_5.py |
| TC-PRF-3224 | P1 | Multi-user 1000 pattern 3 | users=1000,pattern=3 | summaries=1000 | test_profiling_phase2_part_5.py |
| TC-PRF-3225 | P1 | Multi-user 1000 pattern 4 | users=1000,pattern=4 | summaries=1000 | test_profiling_phase2_part_5.py |
| TC-PRF-3226 | P1 | Multi-user 1000 pattern 5 | users=1000,pattern=5 | summaries=1000 | test_profiling_phase2_part_5.py |
| TC-PRF-3227 | P1 | Multi-user 1000 pattern 6 | users=1000,pattern=6 | summaries=1000 | test_profiling_phase2_part_5.py |
| TC-PRF-3228 | P1 | Multi-user 1000 pattern 7 | users=1000,pattern=7 | summaries=1000 | test_profiling_phase2_part_5.py |
| TC-PRF-3229 | P1 | Multi-user 1000 pattern 8 | users=1000,pattern=8 | summaries=1000 | test_profiling_phase2_part_5.py |
| TC-PRF-3230 | P1 | Multi-user 1000 pattern 9 | users=1000,pattern=9 | summaries=1000 | test_profiling_phase2_part_5.py |
| TC-PRF-3231 | P1 | Multi-user 1000 pattern 10 | users=1000,pattern=10 | summaries=1000 | test_profiling_phase2_part_5.py |
| TC-PRF-3232 | P1 | Multi-user 1000 pattern 11 | users=1000,pattern=11 | summaries=1000 | test_profiling_phase2_part_5.py |
| TC-PRF-3233 | P1 | Multi-user 1000 pattern 12 | users=1000,pattern=12 | summaries=1000 | test_profiling_phase2_part_5.py |
| TC-PRF-3234 | P1 | Multi-user 1000 pattern 13 | users=1000,pattern=13 | summaries=1000 | test_profiling_phase2_part_5.py |
| TC-PRF-3235 | P1 | Multi-user 1000 pattern 14 | users=1000,pattern=14 | summaries=1000 | test_profiling_phase2_part_5.py |
| TC-PRF-3236 | P1 | Multi-user 1000 pattern 15 | users=1000,pattern=15 | summaries=1000 | test_profiling_phase2_part_5.py |
| TC-PRF-3237 | P1 | Multi-user 1000 pattern 16 | users=1000,pattern=16 | summaries=1000 | test_profiling_phase2_part_5.py |
| TC-PRF-3238 | P1 | Multi-user 1000 pattern 17 | users=1000,pattern=17 | summaries=1000 | test_profiling_phase2_part_5.py |
| TC-PRF-3239 | P1 | Multi-user 1000 pattern 18 | users=1000,pattern=18 | summaries=1000 | test_profiling_phase2_part_5.py |
| TC-PRF-3240 | P1 | Multi-user 1000 pattern 19 | users=1000,pattern=19 | summaries=1000 | test_profiling_phase2_part_5.py |
| TC-PRF-3241 | P2 | Multi-app 4 scenario 0 | apps=4,scenario=0 | summaries=4 | test_profiling_phase2_part_5.py |
| TC-PRF-3242 | P2 | Multi-app 4 scenario 1 | apps=4,scenario=1 | summaries=4 | test_profiling_phase2_part_5.py |
| TC-PRF-3243 | P2 | Multi-app 4 scenario 2 | apps=4,scenario=2 | summaries=4 | test_profiling_phase2_part_5.py |
| TC-PRF-3244 | P2 | Multi-app 4 scenario 3 | apps=4,scenario=3 | summaries=4 | test_profiling_phase2_part_5.py |
| TC-PRF-3245 | P2 | Multi-app 4 scenario 4 | apps=4,scenario=4 | summaries=4 | test_profiling_phase2_part_5.py |
| TC-PRF-3246 | P2 | Multi-app 4 scenario 5 | apps=4,scenario=5 | summaries=4 | test_profiling_phase2_part_5.py |
| TC-PRF-3247 | P2 | Multi-app 4 scenario 6 | apps=4,scenario=6 | summaries=4 | test_profiling_phase2_part_5.py |
| TC-PRF-3248 | P2 | Multi-app 4 scenario 7 | apps=4,scenario=7 | summaries=4 | test_profiling_phase2_part_5.py |
| TC-PRF-3249 | P2 | Multi-app 4 scenario 8 | apps=4,scenario=8 | summaries=4 | test_profiling_phase2_part_5.py |
| TC-PRF-3250 | P2 | Multi-app 4 scenario 9 | apps=4,scenario=9 | summaries=4 | test_profiling_phase2_part_5.py |
| TC-PRF-3251 | P2 | Multi-app 4 scenario 10 | apps=4,scenario=10 | summaries=4 | test_profiling_phase2_part_5.py |
| TC-PRF-3252 | P2 | Multi-app 4 scenario 11 | apps=4,scenario=11 | summaries=4 | test_profiling_phase2_part_5.py |
| TC-PRF-3253 | P2 | Multi-app 4 scenario 12 | apps=4,scenario=12 | summaries=4 | test_profiling_phase2_part_5.py |
| TC-PRF-3254 | P2 | Multi-app 4 scenario 13 | apps=4,scenario=13 | summaries=4 | test_profiling_phase2_part_5.py |
| TC-PRF-3255 | P2 | Multi-app 4 scenario 14 | apps=4,scenario=14 | summaries=4 | test_profiling_phase2_part_5.py |
| TC-PRF-3256 | P2 | Multi-app 4 scenario 15 | apps=4,scenario=15 | summaries=4 | test_profiling_phase2_part_5.py |
| TC-PRF-3257 | P2 | Multi-app 4 scenario 16 | apps=4,scenario=16 | summaries=4 | test_profiling_phase2_part_5.py |
| TC-PRF-3258 | P2 | Multi-app 5 scenario 0 | apps=5,scenario=0 | summaries=5 | test_profiling_phase2_part_5.py |
| TC-PRF-3259 | P2 | Multi-app 5 scenario 1 | apps=5,scenario=1 | summaries=5 | test_profiling_phase2_part_5.py |
| TC-PRF-3260 | P2 | Multi-app 5 scenario 2 | apps=5,scenario=2 | summaries=5 | test_profiling_phase2_part_5.py |
| TC-PRF-3261 | P2 | Multi-app 5 scenario 3 | apps=5,scenario=3 | summaries=5 | test_profiling_phase2_part_5.py |
| TC-PRF-3262 | P2 | Multi-app 5 scenario 4 | apps=5,scenario=4 | summaries=5 | test_profiling_phase2_part_5.py |
| TC-PRF-3263 | P2 | Multi-app 5 scenario 5 | apps=5,scenario=5 | summaries=5 | test_profiling_phase2_part_5.py |
| TC-PRF-3264 | P2 | Multi-app 5 scenario 6 | apps=5,scenario=6 | summaries=5 | test_profiling_phase2_part_5.py |
| TC-PRF-3265 | P2 | Multi-app 5 scenario 7 | apps=5,scenario=7 | summaries=5 | test_profiling_phase2_part_5.py |
| TC-PRF-3266 | P2 | Multi-app 5 scenario 8 | apps=5,scenario=8 | summaries=5 | test_profiling_phase2_part_5.py |
| TC-PRF-3267 | P2 | Multi-app 5 scenario 9 | apps=5,scenario=9 | summaries=5 | test_profiling_phase2_part_5.py |
| TC-PRF-3268 | P2 | Multi-app 5 scenario 10 | apps=5,scenario=10 | summaries=5 | test_profiling_phase2_part_5.py |
| TC-PRF-3269 | P2 | Multi-app 5 scenario 11 | apps=5,scenario=11 | summaries=5 | test_profiling_phase2_part_5.py |
| TC-PRF-3270 | P2 | Multi-app 5 scenario 12 | apps=5,scenario=12 | summaries=5 | test_profiling_phase2_part_5.py |
| TC-PRF-3271 | P2 | Multi-app 5 scenario 13 | apps=5,scenario=13 | summaries=5 | test_profiling_phase2_part_5.py |
| TC-PRF-3272 | P2 | Multi-app 5 scenario 14 | apps=5,scenario=14 | summaries=5 | test_profiling_phase2_part_5.py |
| TC-PRF-3273 | P2 | Multi-app 5 scenario 15 | apps=5,scenario=15 | summaries=5 | test_profiling_phase2_part_5.py |
| TC-PRF-3274 | P2 | Multi-app 5 scenario 16 | apps=5,scenario=16 | summaries=5 | test_profiling_phase2_part_5.py |
| TC-PRF-3275 | P2 | Multi-app 10 scenario 0 | apps=10,scenario=0 | summaries=10 | test_profiling_phase2_part_5.py |
| TC-PRF-3276 | P2 | Multi-app 10 scenario 1 | apps=10,scenario=1 | summaries=10 | test_profiling_phase2_part_5.py |
| TC-PRF-3277 | P2 | Multi-app 10 scenario 2 | apps=10,scenario=2 | summaries=10 | test_profiling_phase2_part_5.py |
| TC-PRF-3278 | P2 | Multi-app 10 scenario 3 | apps=10,scenario=3 | summaries=10 | test_profiling_phase2_part_5.py |
| TC-PRF-3279 | P2 | Multi-app 10 scenario 4 | apps=10,scenario=4 | summaries=10 | test_profiling_phase2_part_5.py |
| TC-PRF-3280 | P2 | Multi-app 10 scenario 5 | apps=10,scenario=5 | summaries=10 | test_profiling_phase2_part_5.py |
| TC-PRF-3281 | P2 | Multi-app 10 scenario 6 | apps=10,scenario=6 | summaries=10 | test_profiling_phase2_part_5.py |
| TC-PRF-3282 | P2 | Multi-app 10 scenario 7 | apps=10,scenario=7 | summaries=10 | test_profiling_phase2_part_5.py |
| TC-PRF-3283 | P2 | Multi-app 10 scenario 8 | apps=10,scenario=8 | summaries=10 | test_profiling_phase2_part_5.py |
| TC-PRF-3284 | P2 | Multi-app 10 scenario 9 | apps=10,scenario=9 | summaries=10 | test_profiling_phase2_part_5.py |
| TC-PRF-3285 | P2 | Multi-app 10 scenario 10 | apps=10,scenario=10 | summaries=10 | test_profiling_phase2_part_5.py |
| TC-PRF-3286 | P2 | Multi-app 10 scenario 11 | apps=10,scenario=11 | summaries=10 | test_profiling_phase2_part_5.py |
| TC-PRF-3287 | P2 | Multi-app 10 scenario 12 | apps=10,scenario=12 | summaries=10 | test_profiling_phase2_part_5.py |
| TC-PRF-3288 | P2 | Multi-app 10 scenario 13 | apps=10,scenario=13 | summaries=10 | test_profiling_phase2_part_5.py |
| TC-PRF-3289 | P2 | Multi-app 10 scenario 14 | apps=10,scenario=14 | summaries=10 | test_profiling_phase2_part_5.py |
| TC-PRF-3290 | P2 | Multi-app 10 scenario 15 | apps=10,scenario=15 | summaries=10 | test_profiling_phase2_part_5.py |
| TC-PRF-3291 | P2 | Multi-app 10 scenario 16 | apps=10,scenario=16 | summaries=10 | test_profiling_phase2_part_5.py |
| TC-PRF-3292 | P2 | Multi-app 20 scenario 0 | apps=20,scenario=0 | summaries=20 | test_profiling_phase2_part_5.py |
| TC-PRF-3293 | P2 | Multi-app 20 scenario 1 | apps=20,scenario=1 | summaries=20 | test_profiling_phase2_part_5.py |
| TC-PRF-3294 | P2 | Multi-app 20 scenario 2 | apps=20,scenario=2 | summaries=20 | test_profiling_phase2_part_5.py |
| TC-PRF-3295 | P2 | Multi-app 20 scenario 3 | apps=20,scenario=3 | summaries=20 | test_profiling_phase2_part_5.py |
| TC-PRF-3296 | P2 | Multi-app 20 scenario 4 | apps=20,scenario=4 | summaries=20 | test_profiling_phase2_part_5.py |
| TC-PRF-3297 | P2 | Multi-app 20 scenario 5 | apps=20,scenario=5 | summaries=20 | test_profiling_phase2_part_5.py |
| TC-PRF-3298 | P2 | Multi-app 20 scenario 6 | apps=20,scenario=6 | summaries=20 | test_profiling_phase2_part_5.py |
| TC-PRF-3299 | P2 | Multi-app 20 scenario 7 | apps=20,scenario=7 | summaries=20 | test_profiling_phase2_part_5.py |
| TC-PRF-3300 | P2 | Multi-app 20 scenario 8 | apps=20,scenario=8 | summaries=20 | test_profiling_phase2_part_5.py |
| TC-PRF-3301 | P2 | Multi-app 20 scenario 9 | apps=20,scenario=9 | summaries=20 | test_profiling_phase2_part_6.py |
| TC-PRF-3302 | P2 | Multi-app 20 scenario 10 | apps=20,scenario=10 | summaries=20 | test_profiling_phase2_part_6.py |
| TC-PRF-3303 | P2 | Multi-app 20 scenario 11 | apps=20,scenario=11 | summaries=20 | test_profiling_phase2_part_6.py |
| TC-PRF-3304 | P2 | Multi-app 20 scenario 12 | apps=20,scenario=12 | summaries=20 | test_profiling_phase2_part_6.py |
| TC-PRF-3305 | P2 | Multi-app 20 scenario 13 | apps=20,scenario=13 | summaries=20 | test_profiling_phase2_part_6.py |
| TC-PRF-3306 | P2 | Multi-app 20 scenario 14 | apps=20,scenario=14 | summaries=20 | test_profiling_phase2_part_6.py |
| TC-PRF-3307 | P2 | Multi-app 20 scenario 15 | apps=20,scenario=15 | summaries=20 | test_profiling_phase2_part_6.py |
| TC-PRF-3308 | P2 | Multi-app 20 scenario 16 | apps=20,scenario=16 | summaries=20 | test_profiling_phase2_part_6.py |
| TC-PRF-3309 | P2 | Multi-app 50 scenario 0 | apps=50,scenario=0 | summaries=50 | test_profiling_phase2_part_6.py |
| TC-PRF-3310 | P2 | Multi-app 50 scenario 1 | apps=50,scenario=1 | summaries=50 | test_profiling_phase2_part_6.py |
| TC-PRF-3311 | P2 | Multi-app 50 scenario 2 | apps=50,scenario=2 | summaries=50 | test_profiling_phase2_part_6.py |
| TC-PRF-3312 | P2 | Multi-app 50 scenario 3 | apps=50,scenario=3 | summaries=50 | test_profiling_phase2_part_6.py |
| TC-PRF-3313 | P2 | Multi-app 50 scenario 4 | apps=50,scenario=4 | summaries=50 | test_profiling_phase2_part_6.py |
| TC-PRF-3314 | P2 | Multi-app 50 scenario 5 | apps=50,scenario=5 | summaries=50 | test_profiling_phase2_part_6.py |
| TC-PRF-3315 | P2 | Multi-app 50 scenario 6 | apps=50,scenario=6 | summaries=50 | test_profiling_phase2_part_6.py |
| TC-PRF-3316 | P2 | Multi-app 50 scenario 7 | apps=50,scenario=7 | summaries=50 | test_profiling_phase2_part_6.py |
| TC-PRF-3317 | P2 | Multi-app 50 scenario 8 | apps=50,scenario=8 | summaries=50 | test_profiling_phase2_part_6.py |
| TC-PRF-3318 | P2 | Multi-app 50 scenario 9 | apps=50,scenario=9 | summaries=50 | test_profiling_phase2_part_6.py |
| TC-PRF-3319 | P2 | Multi-app 50 scenario 10 | apps=50,scenario=10 | summaries=50 | test_profiling_phase2_part_6.py |
| TC-PRF-3320 | P2 | Multi-app 50 scenario 11 | apps=50,scenario=11 | summaries=50 | test_profiling_phase2_part_6.py |
| TC-PRF-3321 | P2 | Multi-app 50 scenario 12 | apps=50,scenario=12 | summaries=50 | test_profiling_phase2_part_6.py |
| TC-PRF-3322 | P2 | Multi-app 50 scenario 13 | apps=50,scenario=13 | summaries=50 | test_profiling_phase2_part_6.py |
| TC-PRF-3323 | P2 | Multi-app 50 scenario 14 | apps=50,scenario=14 | summaries=50 | test_profiling_phase2_part_6.py |
| TC-PRF-3324 | P2 | Multi-app 50 scenario 15 | apps=50,scenario=15 | summaries=50 | test_profiling_phase2_part_6.py |
| TC-PRF-3325 | P2 | Multi-app 50 scenario 16 | apps=50,scenario=16 | summaries=50 | test_profiling_phase2_part_6.py |
| TC-PRF-3326 | P2 | Multi-app 100 scenario 0 | apps=100,scenario=0 | summaries=100 | test_profiling_phase2_part_6.py |
| TC-PRF-3327 | P2 | Multi-app 100 scenario 1 | apps=100,scenario=1 | summaries=100 | test_profiling_phase2_part_6.py |
| TC-PRF-3328 | P2 | Multi-app 100 scenario 2 | apps=100,scenario=2 | summaries=100 | test_profiling_phase2_part_6.py |
| TC-PRF-3329 | P2 | Multi-app 100 scenario 3 | apps=100,scenario=3 | summaries=100 | test_profiling_phase2_part_6.py |
| TC-PRF-3330 | P2 | Multi-app 100 scenario 4 | apps=100,scenario=4 | summaries=100 | test_profiling_phase2_part_6.py |
| TC-PRF-3331 | P2 | Multi-app 100 scenario 5 | apps=100,scenario=5 | summaries=100 | test_profiling_phase2_part_6.py |
| TC-PRF-3332 | P2 | Multi-app 100 scenario 6 | apps=100,scenario=6 | summaries=100 | test_profiling_phase2_part_6.py |
| TC-PRF-3333 | P2 | Multi-app 100 scenario 7 | apps=100,scenario=7 | summaries=100 | test_profiling_phase2_part_6.py |
| TC-PRF-3334 | P2 | Multi-app 100 scenario 8 | apps=100,scenario=8 | summaries=100 | test_profiling_phase2_part_6.py |
| TC-PRF-3335 | P2 | Multi-app 100 scenario 9 | apps=100,scenario=9 | summaries=100 | test_profiling_phase2_part_6.py |
| TC-PRF-3336 | P2 | Multi-app 100 scenario 10 | apps=100,scenario=10 | summaries=100 | test_profiling_phase2_part_6.py |
| TC-PRF-3337 | P2 | Multi-app 100 scenario 11 | apps=100,scenario=11 | summaries=100 | test_profiling_phase2_part_6.py |
| TC-PRF-3338 | P2 | Multi-app 100 scenario 12 | apps=100,scenario=12 | summaries=100 | test_profiling_phase2_part_6.py |
| TC-PRF-3339 | P2 | Multi-app 100 scenario 13 | apps=100,scenario=13 | summaries=100 | test_profiling_phase2_part_6.py |
| TC-PRF-3340 | P2 | Multi-app 100 scenario 14 | apps=100,scenario=14 | summaries=100 | test_profiling_phase2_part_6.py |
| TC-PRF-3343 | P2 | Cycles 2 pattern 0 | cycles=2,pattern=0 | chain complete | test_profiling_phase2_part_6.py |
| TC-PRF-3344 | P2 | Cycles 2 pattern 1 | cycles=2,pattern=1 | chain complete | test_profiling_phase2_part_6.py |
| TC-PRF-3345 | P2 | Cycles 2 pattern 2 | cycles=2,pattern=2 | chain complete | test_profiling_phase2_part_6.py |
| TC-PRF-3346 | P2 | Cycles 2 pattern 3 | cycles=2,pattern=3 | chain complete | test_profiling_phase2_part_6.py |
| TC-PRF-3347 | P2 | Cycles 2 pattern 4 | cycles=2,pattern=4 | chain complete | test_profiling_phase2_part_6.py |
| TC-PRF-3348 | P2 | Cycles 2 pattern 5 | cycles=2,pattern=5 | chain complete | test_profiling_phase2_part_6.py |
| TC-PRF-3349 | P2 | Cycles 2 pattern 6 | cycles=2,pattern=6 | chain complete | test_profiling_phase2_part_6.py |
| TC-PRF-3350 | P2 | Cycles 2 pattern 7 | cycles=2,pattern=7 | chain complete | test_profiling_phase2_part_6.py |
| TC-PRF-3351 | P2 | Cycles 2 pattern 8 | cycles=2,pattern=8 | chain complete | test_profiling_phase2_part_6.py |
| TC-PRF-3352 | P2 | Cycles 2 pattern 9 | cycles=2,pattern=9 | chain complete | test_profiling_phase2_part_6.py |
| TC-PRF-3353 | P2 | Cycles 2 pattern 10 | cycles=2,pattern=10 | chain complete | test_profiling_phase2_part_6.py |
| TC-PRF-3354 | P2 | Cycles 2 pattern 11 | cycles=2,pattern=11 | chain complete | test_profiling_phase2_part_6.py |
| TC-PRF-3355 | P2 | Cycles 3 pattern 0 | cycles=3,pattern=0 | chain complete | test_profiling_phase2_part_6.py |
| TC-PRF-3356 | P2 | Cycles 3 pattern 1 | cycles=3,pattern=1 | chain complete | test_profiling_phase2_part_6.py |
| TC-PRF-3357 | P2 | Cycles 3 pattern 2 | cycles=3,pattern=2 | chain complete | test_profiling_phase2_part_6.py |
| TC-PRF-3358 | P2 | Cycles 3 pattern 3 | cycles=3,pattern=3 | chain complete | test_profiling_phase2_part_6.py |
| TC-PRF-3359 | P2 | Cycles 3 pattern 4 | cycles=3,pattern=4 | chain complete | test_profiling_phase2_part_6.py |
| TC-PRF-3360 | P2 | Cycles 3 pattern 5 | cycles=3,pattern=5 | chain complete | test_profiling_phase2_part_6.py |
| TC-PRF-3361 | P2 | Cycles 3 pattern 6 | cycles=3,pattern=6 | chain complete | test_profiling_phase2_part_6.py |
| TC-PRF-3362 | P2 | Cycles 3 pattern 7 | cycles=3,pattern=7 | chain complete | test_profiling_phase2_part_6.py |
| TC-PRF-3363 | P2 | Cycles 3 pattern 8 | cycles=3,pattern=8 | chain complete | test_profiling_phase2_part_6.py |
| TC-PRF-3364 | P2 | Cycles 3 pattern 9 | cycles=3,pattern=9 | chain complete | test_profiling_phase2_part_6.py |
| TC-PRF-3365 | P2 | Cycles 3 pattern 10 | cycles=3,pattern=10 | chain complete | test_profiling_phase2_part_6.py |
| TC-PRF-3366 | P2 | Cycles 3 pattern 11 | cycles=3,pattern=11 | chain complete | test_profiling_phase2_part_6.py |
| TC-PRF-3367 | P2 | Cycles 4 pattern 0 | cycles=4,pattern=0 | chain complete | test_profiling_phase2_part_6.py |
| TC-PRF-3368 | P2 | Cycles 4 pattern 1 | cycles=4,pattern=1 | chain complete | test_profiling_phase2_part_6.py |
| TC-PRF-3369 | P2 | Cycles 4 pattern 2 | cycles=4,pattern=2 | chain complete | test_profiling_phase2_part_6.py |
| TC-PRF-3370 | P2 | Cycles 4 pattern 3 | cycles=4,pattern=3 | chain complete | test_profiling_phase2_part_6.py |
| TC-PRF-3371 | P2 | Cycles 4 pattern 4 | cycles=4,pattern=4 | chain complete | test_profiling_phase2_part_6.py |
| TC-PRF-3372 | P2 | Cycles 4 pattern 5 | cycles=4,pattern=5 | chain complete | test_profiling_phase2_part_6.py |
| TC-PRF-3373 | P2 | Cycles 4 pattern 6 | cycles=4,pattern=6 | chain complete | test_profiling_phase2_part_6.py |
| TC-PRF-3374 | P2 | Cycles 4 pattern 7 | cycles=4,pattern=7 | chain complete | test_profiling_phase2_part_6.py |
| TC-PRF-3375 | P2 | Cycles 4 pattern 8 | cycles=4,pattern=8 | chain complete | test_profiling_phase2_part_6.py |
| TC-PRF-3376 | P2 | Cycles 4 pattern 9 | cycles=4,pattern=9 | chain complete | test_profiling_phase2_part_6.py |
| TC-PRF-3377 | P2 | Cycles 4 pattern 10 | cycles=4,pattern=10 | chain complete | test_profiling_phase2_part_6.py |
| TC-PRF-3378 | P2 | Cycles 4 pattern 11 | cycles=4,pattern=11 | chain complete | test_profiling_phase2_part_6.py |
| TC-PRF-3379 | P2 | Cycles 5 pattern 0 | cycles=5,pattern=0 | chain complete | test_profiling_phase2_part_6.py |
| TC-PRF-3380 | P2 | Cycles 5 pattern 1 | cycles=5,pattern=1 | chain complete | test_profiling_phase2_part_6.py |
| TC-PRF-3381 | P2 | Cycles 5 pattern 2 | cycles=5,pattern=2 | chain complete | test_profiling_phase2_part_6.py |
| TC-PRF-3382 | P2 | Cycles 5 pattern 3 | cycles=5,pattern=3 | chain complete | test_profiling_phase2_part_6.py |
| TC-PRF-3383 | P2 | Cycles 5 pattern 4 | cycles=5,pattern=4 | chain complete | test_profiling_phase2_part_6.py |
| TC-PRF-3384 | P2 | Cycles 5 pattern 5 | cycles=5,pattern=5 | chain complete | test_profiling_phase2_part_6.py |
| TC-PRF-3385 | P2 | Cycles 5 pattern 6 | cycles=5,pattern=6 | chain complete | test_profiling_phase2_part_6.py |
| TC-PRF-3386 | P2 | Cycles 5 pattern 7 | cycles=5,pattern=7 | chain complete | test_profiling_phase2_part_6.py |
| TC-PRF-3387 | P2 | Cycles 5 pattern 8 | cycles=5,pattern=8 | chain complete | test_profiling_phase2_part_6.py |
| TC-PRF-3388 | P2 | Cycles 5 pattern 9 | cycles=5,pattern=9 | chain complete | test_profiling_phase2_part_6.py |
| TC-PRF-3389 | P2 | Cycles 5 pattern 10 | cycles=5,pattern=10 | chain complete | test_profiling_phase2_part_6.py |
| TC-PRF-3390 | P2 | Cycles 5 pattern 11 | cycles=5,pattern=11 | chain complete | test_profiling_phase2_part_6.py |
| TC-PRF-3391 | P2 | Cycles 10 pattern 0 | cycles=10,pattern=0 | chain complete | test_profiling_phase2_part_6.py |
| TC-PRF-3392 | P2 | Cycles 10 pattern 1 | cycles=10,pattern=1 | chain complete | test_profiling_phase2_part_6.py |
| TC-PRF-3393 | P2 | Cycles 10 pattern 2 | cycles=10,pattern=2 | chain complete | test_profiling_phase2_part_6.py |
| TC-PRF-3394 | P2 | Cycles 10 pattern 3 | cycles=10,pattern=3 | chain complete | test_profiling_phase2_part_6.py |
| TC-PRF-3395 | P2 | Cycles 10 pattern 4 | cycles=10,pattern=4 | chain complete | test_profiling_phase2_part_6.py |
| TC-PRF-3396 | P2 | Cycles 10 pattern 5 | cycles=10,pattern=5 | chain complete | test_profiling_phase2_part_6.py |
| TC-PRF-3397 | P2 | Cycles 10 pattern 6 | cycles=10,pattern=6 | chain complete | test_profiling_phase2_part_6.py |
| TC-PRF-3398 | P2 | Cycles 10 pattern 7 | cycles=10,pattern=7 | chain complete | test_profiling_phase2_part_6.py |
| TC-PRF-3399 | P2 | Cycles 10 pattern 8 | cycles=10,pattern=8 | chain complete | test_profiling_phase2_part_6.py |
| TC-PRF-3400 | P2 | Cycles 10 pattern 9 | cycles=10,pattern=9 | chain complete | test_profiling_phase2_part_6.py |
| TC-PRF-3401 | P2 | Cycles 10 pattern 10 | cycles=10,pattern=10 | chain complete | test_profiling_phase2_part_6.py |
| TC-PRF-3402 | P2 | Cycles 10 pattern 11 | cycles=10,pattern=11 | chain complete | test_profiling_phase2_part_6.py |
| TC-PRF-3403 | P2 | Cycles 25 pattern 0 | cycles=25,pattern=0 | chain complete | test_profiling_phase2_part_7.py |
| TC-PRF-3404 | P2 | Cycles 25 pattern 1 | cycles=25,pattern=1 | chain complete | test_profiling_phase2_part_7.py |
| TC-PRF-3405 | P2 | Cycles 25 pattern 2 | cycles=25,pattern=2 | chain complete | test_profiling_phase2_part_7.py |
| TC-PRF-3406 | P2 | Cycles 25 pattern 3 | cycles=25,pattern=3 | chain complete | test_profiling_phase2_part_7.py |
| TC-PRF-3407 | P2 | Cycles 25 pattern 4 | cycles=25,pattern=4 | chain complete | test_profiling_phase2_part_7.py |
| TC-PRF-3408 | P2 | Cycles 25 pattern 5 | cycles=25,pattern=5 | chain complete | test_profiling_phase2_part_7.py |
| TC-PRF-3409 | P2 | Cycles 25 pattern 6 | cycles=25,pattern=6 | chain complete | test_profiling_phase2_part_7.py |
| TC-PRF-3410 | P2 | Cycles 25 pattern 7 | cycles=25,pattern=7 | chain complete | test_profiling_phase2_part_7.py |
| TC-PRF-3411 | P2 | Cycles 25 pattern 8 | cycles=25,pattern=8 | chain complete | test_profiling_phase2_part_7.py |
| TC-PRF-3412 | P2 | Cycles 25 pattern 9 | cycles=25,pattern=9 | chain complete | test_profiling_phase2_part_7.py |
| TC-PRF-3413 | P2 | Cycles 25 pattern 10 | cycles=25,pattern=10 | chain complete | test_profiling_phase2_part_7.py |
| TC-PRF-3414 | P2 | Cycles 25 pattern 11 | cycles=25,pattern=11 | chain complete | test_profiling_phase2_part_7.py |
| TC-PRF-3415 | P2 | Cycles 50 pattern 0 | cycles=50,pattern=0 | chain complete | test_profiling_phase2_part_7.py |
| TC-PRF-3416 | P2 | Cycles 50 pattern 1 | cycles=50,pattern=1 | chain complete | test_profiling_phase2_part_7.py |
| TC-PRF-3417 | P2 | Cycles 50 pattern 2 | cycles=50,pattern=2 | chain complete | test_profiling_phase2_part_7.py |
| TC-PRF-3418 | P2 | Cycles 50 pattern 3 | cycles=50,pattern=3 | chain complete | test_profiling_phase2_part_7.py |
| TC-PRF-3419 | P2 | Cycles 50 pattern 4 | cycles=50,pattern=4 | chain complete | test_profiling_phase2_part_7.py |
| TC-PRF-3420 | P2 | Cycles 50 pattern 5 | cycles=50,pattern=5 | chain complete | test_profiling_phase2_part_7.py |
| TC-PRF-3421 | P2 | Cycles 50 pattern 6 | cycles=50,pattern=6 | chain complete | test_profiling_phase2_part_7.py |
| TC-PRF-3422 | P2 | Cycles 50 pattern 7 | cycles=50,pattern=7 | chain complete | test_profiling_phase2_part_7.py |
| TC-PRF-3423 | P2 | Cycles 50 pattern 8 | cycles=50,pattern=8 | chain complete | test_profiling_phase2_part_7.py |
| TC-PRF-3424 | P2 | Cycles 50 pattern 9 | cycles=50,pattern=9 | chain complete | test_profiling_phase2_part_7.py |
| TC-PRF-3425 | P2 | Cycles 50 pattern 10 | cycles=50,pattern=10 | chain complete | test_profiling_phase2_part_7.py |
| TC-PRF-3426 | P2 | Cycles 50 pattern 11 | cycles=50,pattern=11 | chain complete | test_profiling_phase2_part_7.py |
| TC-PRF-3427 | P2 | Cycles 100 pattern 0 | cycles=100,pattern=0 | chain complete | test_profiling_phase2_part_7.py |
| TC-PRF-3428 | P2 | Cycles 100 pattern 1 | cycles=100,pattern=1 | chain complete | test_profiling_phase2_part_7.py |
| TC-PRF-3429 | P2 | Cycles 100 pattern 2 | cycles=100,pattern=2 | chain complete | test_profiling_phase2_part_7.py |
| TC-PRF-3430 | P2 | Cycles 100 pattern 3 | cycles=100,pattern=3 | chain complete | test_profiling_phase2_part_7.py |
| TC-PRF-3431 | P2 | Cycles 100 pattern 4 | cycles=100,pattern=4 | chain complete | test_profiling_phase2_part_7.py |
| TC-PRF-3432 | P2 | Cycles 100 pattern 5 | cycles=100,pattern=5 | chain complete | test_profiling_phase2_part_7.py |
| TC-PRF-3433 | P2 | Cycles 100 pattern 6 | cycles=100,pattern=6 | chain complete | test_profiling_phase2_part_7.py |
| TC-PRF-3434 | P2 | Cycles 100 pattern 7 | cycles=100,pattern=7 | chain complete | test_profiling_phase2_part_7.py |
| TC-PRF-3435 | P2 | Cycles 100 pattern 8 | cycles=100,pattern=8 | chain complete | test_profiling_phase2_part_7.py |
| TC-PRF-3436 | P2 | Cycles 100 pattern 9 | cycles=100,pattern=9 | chain complete | test_profiling_phase2_part_7.py |
| TC-PRF-3437 | P2 | Cycles 100 pattern 10 | cycles=100,pattern=10 | chain complete | test_profiling_phase2_part_7.py |
| TC-PRF-3438 | P2 | Cycles 100 pattern 11 | cycles=100,pattern=11 | chain complete | test_profiling_phase2_part_7.py |
| TC-PRF-3439 | P2 | Cycles 6 clean | cycles=6 | chain complete | test_profiling_phase2_part_7.py |
| TC-PRF-3440 | P2 | Cycles 7 clean | cycles=7 | chain complete | test_profiling_phase2_part_7.py |
| TC-PRF-3441 | P2 | Cycles 8 clean | cycles=8 | chain complete | test_profiling_phase2_part_7.py |
| TC-PRF-3442 | P2 | Cycles 9 clean | cycles=9 | chain complete | test_profiling_phase2_part_7.py |
| TC-PRF-3443 | P3 | Isolation scenario 0 | scenario=0 | isolated | test_profiling_phase2_part_7.py |
| TC-PRF-3444 | P3 | Isolation scenario 1 | scenario=1 | isolated | test_profiling_phase2_part_7.py |
| TC-PRF-3445 | P3 | Isolation scenario 2 | scenario=2 | isolated | test_profiling_phase2_part_7.py |
| TC-PRF-3446 | P3 | Isolation scenario 3 | scenario=3 | isolated | test_profiling_phase2_part_7.py |
| TC-PRF-3447 | P3 | Isolation scenario 4 | scenario=4 | isolated | test_profiling_phase2_part_7.py |
| TC-PRF-3448 | P3 | Isolation scenario 5 | scenario=5 | isolated | test_profiling_phase2_part_7.py |
| TC-PRF-3449 | P3 | Isolation scenario 6 | scenario=6 | isolated | test_profiling_phase2_part_7.py |
| TC-PRF-3450 | P3 | Isolation scenario 7 | scenario=7 | isolated | test_profiling_phase2_part_7.py |
| TC-PRF-3451 | P3 | Isolation scenario 8 | scenario=8 | isolated | test_profiling_phase2_part_7.py |
| TC-PRF-3452 | P3 | Isolation scenario 9 | scenario=9 | isolated | test_profiling_phase2_part_7.py |
| TC-PRF-3453 | P3 | Isolation scenario 10 | scenario=10 | isolated | test_profiling_phase2_part_7.py |
| TC-PRF-3454 | P3 | Isolation scenario 11 | scenario=11 | isolated | test_profiling_phase2_part_7.py |
| TC-PRF-3455 | P3 | Isolation scenario 12 | scenario=12 | isolated | test_profiling_phase2_part_7.py |
| TC-PRF-3456 | P3 | Isolation scenario 13 | scenario=13 | isolated | test_profiling_phase2_part_7.py |
| TC-PRF-3457 | P3 | Isolation scenario 14 | scenario=14 | isolated | test_profiling_phase2_part_7.py |
| TC-PRF-3458 | P3 | Isolation scenario 15 | scenario=15 | isolated | test_profiling_phase2_part_7.py |
| TC-PRF-3459 | P3 | Isolation scenario 16 | scenario=16 | isolated | test_profiling_phase2_part_7.py |
| TC-PRF-3460 | P3 | Isolation scenario 17 | scenario=17 | isolated | test_profiling_phase2_part_7.py |
| TC-PRF-3461 | P3 | Isolation scenario 18 | scenario=18 | isolated | test_profiling_phase2_part_7.py |
| TC-PRF-3462 | P3 | Isolation scenario 19 | scenario=19 | isolated | test_profiling_phase2_part_7.py |
| TC-PRF-3463 | P3 | Isolation scenario 20 | scenario=20 | isolated | test_profiling_phase2_part_7.py |
| TC-PRF-3464 | P3 | Isolation scenario 21 | scenario=21 | isolated | test_profiling_phase2_part_7.py |
| TC-PRF-3465 | P3 | Isolation scenario 22 | scenario=22 | isolated | test_profiling_phase2_part_7.py |
| TC-PRF-3466 | P3 | Isolation scenario 23 | scenario=23 | isolated | test_profiling_phase2_part_7.py |
| TC-PRF-3467 | P3 | Isolation scenario 24 | scenario=24 | isolated | test_profiling_phase2_part_7.py |
| TC-PRF-3468 | P3 | Isolation scenario 25 | scenario=25 | isolated | test_profiling_phase2_part_7.py |
| TC-PRF-3469 | P3 | Isolation scenario 26 | scenario=26 | isolated | test_profiling_phase2_part_7.py |
| TC-PRF-3470 | P3 | Isolation scenario 27 | scenario=27 | isolated | test_profiling_phase2_part_7.py |
| TC-PRF-3471 | P3 | Isolation scenario 28 | scenario=28 | isolated | test_profiling_phase2_part_7.py |
| TC-PRF-3472 | P3 | Isolation scenario 29 | scenario=29 | isolated | test_profiling_phase2_part_7.py |
| TC-PRF-3473 | P3 | Isolation scenario 30 | scenario=30 | isolated | test_profiling_phase2_part_7.py |
| TC-PRF-3474 | P3 | Isolation scenario 31 | scenario=31 | isolated | test_profiling_phase2_part_7.py |
| TC-PRF-3475 | P3 | Isolation scenario 32 | scenario=32 | isolated | test_profiling_phase2_part_7.py |
| TC-PRF-3476 | P3 | Isolation scenario 33 | scenario=33 | isolated | test_profiling_phase2_part_7.py |
| TC-PRF-3477 | P3 | Isolation scenario 34 | scenario=34 | isolated | test_profiling_phase2_part_7.py |
| TC-PRF-3478 | P3 | Isolation scenario 35 | scenario=35 | isolated | test_profiling_phase2_part_7.py |
| TC-PRF-3479 | P3 | Isolation scenario 36 | scenario=36 | isolated | test_profiling_phase2_part_7.py |
| TC-PRF-3480 | P3 | Isolation scenario 37 | scenario=37 | isolated | test_profiling_phase2_part_7.py |
| TC-PRF-3481 | P3 | Isolation scenario 38 | scenario=38 | isolated | test_profiling_phase2_part_7.py |
| TC-PRF-3482 | P3 | Isolation scenario 39 | scenario=39 | isolated | test_profiling_phase2_part_7.py |
| TC-PRF-3483 | P3 | Isolation scenario 40 | scenario=40 | isolated | test_profiling_phase2_part_7.py |
| TC-PRF-3484 | P3 | Isolation scenario 41 | scenario=41 | isolated | test_profiling_phase2_part_7.py |
| TC-PRF-3485 | P3 | Isolation scenario 42 | scenario=42 | isolated | test_profiling_phase2_part_7.py |
| TC-PRF-3486 | P3 | Isolation scenario 43 | scenario=43 | isolated | test_profiling_phase2_part_7.py |
| TC-PRF-3487 | P3 | Isolation scenario 44 | scenario=44 | isolated | test_profiling_phase2_part_7.py |
| TC-PRF-3488 | P3 | Isolation scenario 45 | scenario=45 | isolated | test_profiling_phase2_part_7.py |
| TC-PRF-3489 | P3 | Isolation scenario 46 | scenario=46 | isolated | test_profiling_phase2_part_7.py |
| TC-PRF-3490 | P3 | Isolation scenario 47 | scenario=47 | isolated | test_profiling_phase2_part_7.py |
| TC-PRF-3491 | P3 | Isolation scenario 48 | scenario=48 | isolated | test_profiling_phase2_part_7.py |
| TC-PRF-3492 | P3 | Isolation scenario 49 | scenario=49 | isolated | test_profiling_phase2_part_7.py |
| TC-PRF-3493 | P3 | Isolation scenario 50 | scenario=50 | isolated | test_profiling_phase2_part_7.py |
| TC-PRF-3494 | P3 | Isolation scenario 51 | scenario=51 | isolated | test_profiling_phase2_part_7.py |
| TC-PRF-3495 | P3 | Isolation scenario 52 | scenario=52 | isolated | test_profiling_phase2_part_7.py |
| TC-PRF-3496 | P3 | Isolation scenario 53 | scenario=53 | isolated | test_profiling_phase2_part_7.py |
| TC-PRF-3497 | P3 | Isolation scenario 54 | scenario=54 | isolated | test_profiling_phase2_part_7.py |
| TC-PRF-3498 | P3 | Isolation scenario 55 | scenario=55 | isolated | test_profiling_phase2_part_7.py |
| TC-PRF-3499 | P3 | Isolation scenario 56 | scenario=56 | isolated | test_profiling_phase2_part_7.py |
| TC-PRF-3500 | P3 | Isolation scenario 57 | scenario=57 | isolated | test_profiling_phase2_part_7.py |
| TC-PRF-3501 | P3 | Isolation scenario 58 | scenario=58 | isolated | test_profiling_phase2_part_7.py |
| TC-PRF-3502 | P3 | Isolation scenario 59 | scenario=59 | isolated | test_profiling_phase2_part_7.py |

### Phase 3 - 12,000 cases
- Planned sweeps over the full dimension matrix, IDs TC-PRF-0781 onward.

### Phase 4 - 120,000 cases
- Planned high-scale scenarios, IDs TC-PRF-12781 onward.

### Phase 5 - 917,220 cases
- Planned exhaustive dimension sweep, IDs TC-PRF-132781 onward.

## Implementation Status
| File | Test Cases | Priority | Status |
| :--- | :--- | :--- | :--- |
| test_profiling_phase2_part_1.py | 2801-2900 | P1 | :white_check_mark: Phase 2 |
| test_profiling_phase2_part_2.py | 2901-3000 | P1 | :white_check_mark: Phase 2 |
| test_profiling_phase2_part_3.py | 3001-3100 | P1 | :white_check_mark: Phase 2 |
| test_profiling_phase2_part_4.py | 3101-3200 | P1 | :white_check_mark: Phase 2 |
| test_profiling_phase2_part_5.py | 3201-3300 | P1 | :white_check_mark: Phase 2 |
| test_profiling_phase2_part_6.py | 3301-3402 | P2 | :white_check_mark: Phase 2 |
| test_profiling_phase2_part_7.py | 3403-3502 | P2 | :white_check_mark: Phase 2 |

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
- User Profiling
- Archive Strategy
