# Semantic Module Test Documentation

## Overview
- **Total Planned:** 1,200,000
- **Phase 1:** 80 (IDs TC-SEM-001 to TC-SEM-0080) :white_check_mark: Implemented
- **Phase 2:** 700 (IDs TC-SEM-0081 to TC-SEM-0780) :white_check_mark: Implemented
- **Phase 3:** 15,000 (IDs TC-SEM-0781 to TC-SEM-15780) :hourglass: Planned
- **Phase 4:** 150,000 (IDs TC-SEM-15781 to TC-SEM-165780) :hourglass: Planned
- **Phase 5:** 1,034,220 (IDs TC-SEM-165781 to TC-SEM-1200000) :hourglass: Planned

## Dimension Matrix
| Dimension | Values (Phase 2) |
| :--- | :--- |
| Category | political, violence, sexual, hate, pii, ads, other |
| Threshold | 0.1-1.0 step 0.05 |
| Availability | installed, missing |
| Top-k | 1-100 |

## Test Case List

### Phase 1 - 80 cases
- 80 cases (service + SuspicionScorer).

### Phase 2 (Current) - 700 cases
| ID | Priority | Description | Dimensions | Expected Outcome | File |
| :--- | :--- | :--- | :--- | :--- | :--- |
| TC-SEM-2101 | P2 | Unavailable path top_k 1 | top_k=1 | unavailable | test_semantic_phase2_part_1.py |
| TC-SEM-2102 | P2 | Unavailable path top_k 2 | top_k=2 | unavailable | test_semantic_phase2_part_1.py |
| TC-SEM-2103 | P2 | Unavailable path top_k 3 | top_k=3 | unavailable | test_semantic_phase2_part_1.py |
| TC-SEM-2104 | P2 | Unavailable path top_k 4 | top_k=4 | unavailable | test_semantic_phase2_part_1.py |
| TC-SEM-2105 | P2 | Unavailable path top_k 5 | top_k=5 | unavailable | test_semantic_phase2_part_1.py |
| TC-SEM-2106 | P2 | Unavailable path top_k 6 | top_k=6 | unavailable | test_semantic_phase2_part_1.py |
| TC-SEM-2107 | P2 | Unavailable path top_k 7 | top_k=7 | unavailable | test_semantic_phase2_part_1.py |
| TC-SEM-2108 | P2 | Unavailable path top_k 8 | top_k=8 | unavailable | test_semantic_phase2_part_1.py |
| TC-SEM-2109 | P2 | Unavailable path top_k 9 | top_k=9 | unavailable | test_semantic_phase2_part_1.py |
| TC-SEM-2110 | P2 | Unavailable path top_k 10 | top_k=10 | unavailable | test_semantic_phase2_part_1.py |
| TC-SEM-2111 | P2 | Unavailable path top_k 11 | top_k=11 | unavailable | test_semantic_phase2_part_1.py |
| TC-SEM-2112 | P2 | Unavailable path top_k 12 | top_k=12 | unavailable | test_semantic_phase2_part_1.py |
| TC-SEM-2113 | P2 | Unavailable path top_k 13 | top_k=13 | unavailable | test_semantic_phase2_part_1.py |
| TC-SEM-2114 | P2 | Unavailable path top_k 14 | top_k=14 | unavailable | test_semantic_phase2_part_1.py |
| TC-SEM-2115 | P2 | Unavailable path top_k 15 | top_k=15 | unavailable | test_semantic_phase2_part_1.py |
| TC-SEM-2116 | P2 | Unavailable path top_k 16 | top_k=16 | unavailable | test_semantic_phase2_part_1.py |
| TC-SEM-2117 | P2 | Unavailable path top_k 17 | top_k=17 | unavailable | test_semantic_phase2_part_1.py |
| TC-SEM-2118 | P2 | Unavailable path top_k 18 | top_k=18 | unavailable | test_semantic_phase2_part_1.py |
| TC-SEM-2119 | P2 | Unavailable path top_k 19 | top_k=19 | unavailable | test_semantic_phase2_part_1.py |
| TC-SEM-2120 | P2 | Unavailable path top_k 20 | top_k=20 | unavailable | test_semantic_phase2_part_1.py |
| TC-SEM-2121 | P2 | Unavailable path top_k 21 | top_k=21 | unavailable | test_semantic_phase2_part_1.py |
| TC-SEM-2122 | P2 | Unavailable path top_k 22 | top_k=22 | unavailable | test_semantic_phase2_part_1.py |
| TC-SEM-2123 | P2 | Unavailable path top_k 23 | top_k=23 | unavailable | test_semantic_phase2_part_1.py |
| TC-SEM-2124 | P2 | Unavailable path top_k 24 | top_k=24 | unavailable | test_semantic_phase2_part_1.py |
| TC-SEM-2125 | P2 | Unavailable path top_k 25 | top_k=25 | unavailable | test_semantic_phase2_part_1.py |
| TC-SEM-2126 | P2 | Unavailable path top_k 26 | top_k=26 | unavailable | test_semantic_phase2_part_1.py |
| TC-SEM-2127 | P2 | Unavailable path top_k 27 | top_k=27 | unavailable | test_semantic_phase2_part_1.py |
| TC-SEM-2128 | P2 | Unavailable path top_k 28 | top_k=28 | unavailable | test_semantic_phase2_part_1.py |
| TC-SEM-2129 | P2 | Unavailable path top_k 29 | top_k=29 | unavailable | test_semantic_phase2_part_1.py |
| TC-SEM-2130 | P2 | Unavailable path top_k 30 | top_k=30 | unavailable | test_semantic_phase2_part_1.py |
| TC-SEM-2131 | P2 | Unavailable path top_k 31 | top_k=31 | unavailable | test_semantic_phase2_part_1.py |
| TC-SEM-2132 | P2 | Unavailable path top_k 32 | top_k=32 | unavailable | test_semantic_phase2_part_1.py |
| TC-SEM-2133 | P2 | Unavailable path top_k 33 | top_k=33 | unavailable | test_semantic_phase2_part_1.py |
| TC-SEM-2134 | P2 | Unavailable path top_k 34 | top_k=34 | unavailable | test_semantic_phase2_part_1.py |
| TC-SEM-2135 | P2 | Unavailable path top_k 35 | top_k=35 | unavailable | test_semantic_phase2_part_1.py |
| TC-SEM-2136 | P2 | Unavailable path top_k 36 | top_k=36 | unavailable | test_semantic_phase2_part_1.py |
| TC-SEM-2137 | P2 | Unavailable path top_k 37 | top_k=37 | unavailable | test_semantic_phase2_part_1.py |
| TC-SEM-2138 | P2 | Unavailable path top_k 38 | top_k=38 | unavailable | test_semantic_phase2_part_1.py |
| TC-SEM-2139 | P2 | Unavailable path top_k 39 | top_k=39 | unavailable | test_semantic_phase2_part_1.py |
| TC-SEM-2140 | P2 | Unavailable path top_k 40 | top_k=40 | unavailable | test_semantic_phase2_part_1.py |
| TC-SEM-2141 | P2 | Unavailable path top_k 41 | top_k=41 | unavailable | test_semantic_phase2_part_1.py |
| TC-SEM-2142 | P2 | Unavailable path top_k 42 | top_k=42 | unavailable | test_semantic_phase2_part_1.py |
| TC-SEM-2143 | P2 | Unavailable path top_k 43 | top_k=43 | unavailable | test_semantic_phase2_part_1.py |
| TC-SEM-2144 | P2 | Unavailable path top_k 44 | top_k=44 | unavailable | test_semantic_phase2_part_1.py |
| TC-SEM-2145 | P2 | Unavailable path top_k 45 | top_k=45 | unavailable | test_semantic_phase2_part_1.py |
| TC-SEM-2146 | P2 | Unavailable path top_k 46 | top_k=46 | unavailable | test_semantic_phase2_part_1.py |
| TC-SEM-2147 | P2 | Unavailable path top_k 47 | top_k=47 | unavailable | test_semantic_phase2_part_1.py |
| TC-SEM-2148 | P2 | Unavailable path top_k 48 | top_k=48 | unavailable | test_semantic_phase2_part_1.py |
| TC-SEM-2149 | P2 | Unavailable path top_k 49 | top_k=49 | unavailable | test_semantic_phase2_part_1.py |
| TC-SEM-2150 | P2 | Unavailable path top_k 50 | top_k=50 | unavailable | test_semantic_phase2_part_1.py |
| TC-SEM-2151 | P2 | Unavailable path top_k 51 | top_k=51 | unavailable | test_semantic_phase2_part_1.py |
| TC-SEM-2152 | P2 | Unavailable path top_k 52 | top_k=52 | unavailable | test_semantic_phase2_part_1.py |
| TC-SEM-2153 | P2 | Unavailable path top_k 53 | top_k=53 | unavailable | test_semantic_phase2_part_1.py |
| TC-SEM-2154 | P2 | Unavailable path top_k 54 | top_k=54 | unavailable | test_semantic_phase2_part_1.py |
| TC-SEM-2155 | P2 | Unavailable path top_k 55 | top_k=55 | unavailable | test_semantic_phase2_part_1.py |
| TC-SEM-2156 | P2 | Unavailable path top_k 56 | top_k=56 | unavailable | test_semantic_phase2_part_1.py |
| TC-SEM-2157 | P2 | Unavailable path top_k 57 | top_k=57 | unavailable | test_semantic_phase2_part_1.py |
| TC-SEM-2158 | P2 | Unavailable path top_k 58 | top_k=58 | unavailable | test_semantic_phase2_part_1.py |
| TC-SEM-2159 | P2 | Unavailable path top_k 59 | top_k=59 | unavailable | test_semantic_phase2_part_1.py |
| TC-SEM-2160 | P2 | Unavailable path top_k 60 | top_k=60 | unavailable | test_semantic_phase2_part_1.py |
| TC-SEM-2161 | P2 | Unavailable path top_k 61 | top_k=61 | unavailable | test_semantic_phase2_part_1.py |
| TC-SEM-2162 | P2 | Unavailable path top_k 62 | top_k=62 | unavailable | test_semantic_phase2_part_1.py |
| TC-SEM-2163 | P2 | Unavailable path top_k 63 | top_k=63 | unavailable | test_semantic_phase2_part_1.py |
| TC-SEM-2164 | P2 | Unavailable path top_k 64 | top_k=64 | unavailable | test_semantic_phase2_part_1.py |
| TC-SEM-2165 | P2 | Unavailable path top_k 65 | top_k=65 | unavailable | test_semantic_phase2_part_1.py |
| TC-SEM-2166 | P2 | Unavailable path top_k 66 | top_k=66 | unavailable | test_semantic_phase2_part_1.py |
| TC-SEM-2167 | P2 | Unavailable path top_k 67 | top_k=67 | unavailable | test_semantic_phase2_part_1.py |
| TC-SEM-2168 | P2 | Unavailable path top_k 68 | top_k=68 | unavailable | test_semantic_phase2_part_1.py |
| TC-SEM-2169 | P2 | Unavailable path top_k 69 | top_k=69 | unavailable | test_semantic_phase2_part_1.py |
| TC-SEM-2170 | P2 | Unavailable path top_k 70 | top_k=70 | unavailable | test_semantic_phase2_part_1.py |
| TC-SEM-2171 | P2 | Unavailable path top_k 71 | top_k=71 | unavailable | test_semantic_phase2_part_1.py |
| TC-SEM-2172 | P2 | Unavailable path top_k 72 | top_k=72 | unavailable | test_semantic_phase2_part_1.py |
| TC-SEM-2173 | P2 | Unavailable path top_k 73 | top_k=73 | unavailable | test_semantic_phase2_part_1.py |
| TC-SEM-2174 | P2 | Unavailable path top_k 74 | top_k=74 | unavailable | test_semantic_phase2_part_1.py |
| TC-SEM-2175 | P2 | Unavailable path top_k 75 | top_k=75 | unavailable | test_semantic_phase2_part_1.py |
| TC-SEM-2176 | P2 | Unavailable path top_k 76 | top_k=76 | unavailable | test_semantic_phase2_part_1.py |
| TC-SEM-2177 | P2 | Unavailable path top_k 77 | top_k=77 | unavailable | test_semantic_phase2_part_1.py |
| TC-SEM-2178 | P2 | Unavailable path top_k 78 | top_k=78 | unavailable | test_semantic_phase2_part_1.py |
| TC-SEM-2179 | P2 | Unavailable path top_k 79 | top_k=79 | unavailable | test_semantic_phase2_part_1.py |
| TC-SEM-2180 | P2 | Unavailable path top_k 80 | top_k=80 | unavailable | test_semantic_phase2_part_1.py |
| TC-SEM-2181 | P2 | Unavailable path top_k 81 | top_k=81 | unavailable | test_semantic_phase2_part_1.py |
| TC-SEM-2182 | P2 | Unavailable path top_k 82 | top_k=82 | unavailable | test_semantic_phase2_part_1.py |
| TC-SEM-2183 | P2 | Unavailable path top_k 83 | top_k=83 | unavailable | test_semantic_phase2_part_1.py |
| TC-SEM-2184 | P2 | Unavailable path top_k 84 | top_k=84 | unavailable | test_semantic_phase2_part_1.py |
| TC-SEM-2185 | P2 | Unavailable path top_k 85 | top_k=85 | unavailable | test_semantic_phase2_part_1.py |
| TC-SEM-2186 | P2 | Unavailable path top_k 86 | top_k=86 | unavailable | test_semantic_phase2_part_1.py |
| TC-SEM-2187 | P2 | Unavailable path top_k 87 | top_k=87 | unavailable | test_semantic_phase2_part_1.py |
| TC-SEM-2188 | P2 | Unavailable path top_k 88 | top_k=88 | unavailable | test_semantic_phase2_part_1.py |
| TC-SEM-2189 | P2 | Unavailable path top_k 89 | top_k=89 | unavailable | test_semantic_phase2_part_1.py |
| TC-SEM-2190 | P2 | Unavailable path top_k 90 | top_k=90 | unavailable | test_semantic_phase2_part_1.py |
| TC-SEM-2191 | P2 | Unavailable path top_k 91 | top_k=91 | unavailable | test_semantic_phase2_part_1.py |
| TC-SEM-2192 | P2 | Unavailable path top_k 92 | top_k=92 | unavailable | test_semantic_phase2_part_1.py |
| TC-SEM-2193 | P2 | Unavailable path top_k 93 | top_k=93 | unavailable | test_semantic_phase2_part_1.py |
| TC-SEM-2194 | P2 | Unavailable path top_k 94 | top_k=94 | unavailable | test_semantic_phase2_part_1.py |
| TC-SEM-2195 | P2 | Unavailable path top_k 95 | top_k=95 | unavailable | test_semantic_phase2_part_1.py |
| TC-SEM-2196 | P2 | Unavailable path top_k 96 | top_k=96 | unavailable | test_semantic_phase2_part_1.py |
| TC-SEM-2197 | P2 | Unavailable path top_k 97 | top_k=97 | unavailable | test_semantic_phase2_part_1.py |
| TC-SEM-2198 | P2 | Unavailable path top_k 98 | top_k=98 | unavailable | test_semantic_phase2_part_1.py |
| TC-SEM-2199 | P2 | Unavailable path top_k 99 | top_k=99 | unavailable | test_semantic_phase2_part_1.py |
| TC-SEM-2200 | P2 | Unavailable path top_k 100 | top_k=100 | unavailable | test_semantic_phase2_part_1.py |
| TC-SEM-2201 | P1 | Threshold 0.1 similarity 0.0 | threshold=0.1,sim=0.0 | weighted or zero | test_semantic_phase2_part_2.py |
| TC-SEM-2202 | P1 | Threshold 0.1 similarity 0.1 | threshold=0.1,sim=0.1 | weighted or zero | test_semantic_phase2_part_2.py |
| TC-SEM-2203 | P1 | Threshold 0.1 similarity 0.25 | threshold=0.1,sim=0.25 | weighted or zero | test_semantic_phase2_part_2.py |
| TC-SEM-2204 | P1 | Threshold 0.1 similarity 0.5 | threshold=0.1,sim=0.5 | weighted or zero | test_semantic_phase2_part_2.py |
| TC-SEM-2205 | P1 | Threshold 0.1 similarity 0.75 | threshold=0.1,sim=0.75 | weighted or zero | test_semantic_phase2_part_2.py |
| TC-SEM-2206 | P1 | Threshold 0.1 similarity 0.9 | threshold=0.1,sim=0.9 | weighted or zero | test_semantic_phase2_part_2.py |
| TC-SEM-2207 | P1 | Threshold 0.1 similarity 0.95 | threshold=0.1,sim=0.95 | weighted or zero | test_semantic_phase2_part_2.py |
| TC-SEM-2208 | P1 | Threshold 0.1 similarity 0.99 | threshold=0.1,sim=0.99 | weighted or zero | test_semantic_phase2_part_2.py |
| TC-SEM-2209 | P1 | Threshold 0.1 similarity 1.0 | threshold=0.1,sim=1.0 | weighted or zero | test_semantic_phase2_part_2.py |
| TC-SEM-2210 | P1 | Threshold 0.3 similarity 0.0 | threshold=0.3,sim=0.0 | weighted or zero | test_semantic_phase2_part_2.py |
| TC-SEM-2211 | P1 | Threshold 0.3 similarity 0.1 | threshold=0.3,sim=0.1 | weighted or zero | test_semantic_phase2_part_2.py |
| TC-SEM-2212 | P1 | Threshold 0.3 similarity 0.25 | threshold=0.3,sim=0.25 | weighted or zero | test_semantic_phase2_part_2.py |
| TC-SEM-2213 | P1 | Threshold 0.3 similarity 0.5 | threshold=0.3,sim=0.5 | weighted or zero | test_semantic_phase2_part_2.py |
| TC-SEM-2214 | P1 | Threshold 0.3 similarity 0.75 | threshold=0.3,sim=0.75 | weighted or zero | test_semantic_phase2_part_2.py |
| TC-SEM-2215 | P1 | Threshold 0.3 similarity 0.9 | threshold=0.3,sim=0.9 | weighted or zero | test_semantic_phase2_part_2.py |
| TC-SEM-2216 | P1 | Threshold 0.3 similarity 0.95 | threshold=0.3,sim=0.95 | weighted or zero | test_semantic_phase2_part_2.py |
| TC-SEM-2217 | P1 | Threshold 0.3 similarity 0.99 | threshold=0.3,sim=0.99 | weighted or zero | test_semantic_phase2_part_2.py |
| TC-SEM-2218 | P1 | Threshold 0.3 similarity 1.0 | threshold=0.3,sim=1.0 | weighted or zero | test_semantic_phase2_part_2.py |
| TC-SEM-2219 | P1 | Threshold 0.5 similarity 0.0 | threshold=0.5,sim=0.0 | weighted or zero | test_semantic_phase2_part_2.py |
| TC-SEM-2220 | P1 | Threshold 0.5 similarity 0.1 | threshold=0.5,sim=0.1 | weighted or zero | test_semantic_phase2_part_2.py |
| TC-SEM-2221 | P1 | Threshold 0.5 similarity 0.25 | threshold=0.5,sim=0.25 | weighted or zero | test_semantic_phase2_part_2.py |
| TC-SEM-2222 | P1 | Threshold 0.5 similarity 0.5 | threshold=0.5,sim=0.5 | weighted or zero | test_semantic_phase2_part_2.py |
| TC-SEM-2223 | P1 | Threshold 0.5 similarity 0.75 | threshold=0.5,sim=0.75 | weighted or zero | test_semantic_phase2_part_2.py |
| TC-SEM-2224 | P1 | Threshold 0.5 similarity 0.9 | threshold=0.5,sim=0.9 | weighted or zero | test_semantic_phase2_part_2.py |
| TC-SEM-2225 | P1 | Threshold 0.5 similarity 0.95 | threshold=0.5,sim=0.95 | weighted or zero | test_semantic_phase2_part_2.py |
| TC-SEM-2226 | P1 | Threshold 0.5 similarity 0.99 | threshold=0.5,sim=0.99 | weighted or zero | test_semantic_phase2_part_2.py |
| TC-SEM-2227 | P1 | Threshold 0.5 similarity 1.0 | threshold=0.5,sim=1.0 | weighted or zero | test_semantic_phase2_part_2.py |
| TC-SEM-2228 | P1 | Threshold 0.7 similarity 0.0 | threshold=0.7,sim=0.0 | weighted or zero | test_semantic_phase2_part_2.py |
| TC-SEM-2229 | P1 | Threshold 0.7 similarity 0.1 | threshold=0.7,sim=0.1 | weighted or zero | test_semantic_phase2_part_2.py |
| TC-SEM-2230 | P1 | Threshold 0.7 similarity 0.25 | threshold=0.7,sim=0.25 | weighted or zero | test_semantic_phase2_part_2.py |
| TC-SEM-2231 | P1 | Threshold 0.7 similarity 0.5 | threshold=0.7,sim=0.5 | weighted or zero | test_semantic_phase2_part_2.py |
| TC-SEM-2232 | P1 | Threshold 0.7 similarity 0.75 | threshold=0.7,sim=0.75 | weighted or zero | test_semantic_phase2_part_2.py |
| TC-SEM-2233 | P1 | Threshold 0.7 similarity 0.9 | threshold=0.7,sim=0.9 | weighted or zero | test_semantic_phase2_part_2.py |
| TC-SEM-2234 | P1 | Threshold 0.7 similarity 0.95 | threshold=0.7,sim=0.95 | weighted or zero | test_semantic_phase2_part_2.py |
| TC-SEM-2235 | P1 | Threshold 0.7 similarity 0.99 | threshold=0.7,sim=0.99 | weighted or zero | test_semantic_phase2_part_2.py |
| TC-SEM-2236 | P1 | Threshold 0.7 similarity 1.0 | threshold=0.7,sim=1.0 | weighted or zero | test_semantic_phase2_part_2.py |
| TC-SEM-2237 | P1 | Threshold 0.85 similarity 0.0 | threshold=0.85,sim=0.0 | weighted or zero | test_semantic_phase2_part_2.py |
| TC-SEM-2238 | P1 | Threshold 0.85 similarity 0.1 | threshold=0.85,sim=0.1 | weighted or zero | test_semantic_phase2_part_2.py |
| TC-SEM-2239 | P1 | Threshold 0.85 similarity 0.25 | threshold=0.85,sim=0.25 | weighted or zero | test_semantic_phase2_part_2.py |
| TC-SEM-2240 | P1 | Threshold 0.85 similarity 0.5 | threshold=0.85,sim=0.5 | weighted or zero | test_semantic_phase2_part_2.py |
| TC-SEM-2241 | P1 | Threshold 0.85 similarity 0.75 | threshold=0.85,sim=0.75 | weighted or zero | test_semantic_phase2_part_2.py |
| TC-SEM-2242 | P1 | Threshold 0.85 similarity 0.9 | threshold=0.85,sim=0.9 | weighted or zero | test_semantic_phase2_part_2.py |
| TC-SEM-2243 | P1 | Threshold 0.85 similarity 0.95 | threshold=0.85,sim=0.95 | weighted or zero | test_semantic_phase2_part_2.py |
| TC-SEM-2244 | P1 | Threshold 0.85 similarity 0.99 | threshold=0.85,sim=0.99 | weighted or zero | test_semantic_phase2_part_2.py |
| TC-SEM-2245 | P1 | Threshold 0.85 similarity 1.0 | threshold=0.85,sim=1.0 | weighted or zero | test_semantic_phase2_part_2.py |
| TC-SEM-2246 | P1 | Threshold 0.9 similarity 0.0 | threshold=0.9,sim=0.0 | weighted or zero | test_semantic_phase2_part_2.py |
| TC-SEM-2247 | P1 | Threshold 0.9 similarity 0.1 | threshold=0.9,sim=0.1 | weighted or zero | test_semantic_phase2_part_2.py |
| TC-SEM-2248 | P1 | Threshold 0.9 similarity 0.25 | threshold=0.9,sim=0.25 | weighted or zero | test_semantic_phase2_part_2.py |
| TC-SEM-2249 | P1 | Threshold 0.9 similarity 0.5 | threshold=0.9,sim=0.5 | weighted or zero | test_semantic_phase2_part_2.py |
| TC-SEM-2250 | P1 | Threshold 0.9 similarity 0.75 | threshold=0.9,sim=0.75 | weighted or zero | test_semantic_phase2_part_2.py |
| TC-SEM-2251 | P1 | Threshold 0.9 similarity 0.9 | threshold=0.9,sim=0.9 | weighted or zero | test_semantic_phase2_part_2.py |
| TC-SEM-2252 | P1 | Threshold 0.9 similarity 0.95 | threshold=0.9,sim=0.95 | weighted or zero | test_semantic_phase2_part_2.py |
| TC-SEM-2253 | P1 | Threshold 0.9 similarity 0.99 | threshold=0.9,sim=0.99 | weighted or zero | test_semantic_phase2_part_2.py |
| TC-SEM-2254 | P1 | Threshold 0.9 similarity 1.0 | threshold=0.9,sim=1.0 | weighted or zero | test_semantic_phase2_part_2.py |
| TC-SEM-2255 | P1 | Threshold 0.95 similarity 0.0 | threshold=0.95,sim=0.0 | weighted or zero | test_semantic_phase2_part_2.py |
| TC-SEM-2256 | P1 | Threshold 0.95 similarity 0.1 | threshold=0.95,sim=0.1 | weighted or zero | test_semantic_phase2_part_2.py |
| TC-SEM-2257 | P1 | Threshold 0.95 similarity 0.25 | threshold=0.95,sim=0.25 | weighted or zero | test_semantic_phase2_part_2.py |
| TC-SEM-2258 | P1 | Threshold 0.95 similarity 0.5 | threshold=0.95,sim=0.5 | weighted or zero | test_semantic_phase2_part_2.py |
| TC-SEM-2259 | P1 | Threshold 0.95 similarity 0.75 | threshold=0.95,sim=0.75 | weighted or zero | test_semantic_phase2_part_2.py |
| TC-SEM-2260 | P1 | Threshold 0.95 similarity 0.9 | threshold=0.95,sim=0.9 | weighted or zero | test_semantic_phase2_part_2.py |
| TC-SEM-2261 | P1 | Threshold 0.95 similarity 0.95 | threshold=0.95,sim=0.95 | weighted or zero | test_semantic_phase2_part_2.py |
| TC-SEM-2262 | P1 | Threshold 0.95 similarity 0.99 | threshold=0.95,sim=0.99 | weighted or zero | test_semantic_phase2_part_2.py |
| TC-SEM-2263 | P1 | Threshold 0.95 similarity 1.0 | threshold=0.95,sim=1.0 | weighted or zero | test_semantic_phase2_part_2.py |
| TC-SEM-2264 | P1 | Threshold 0.99 similarity 0.0 | threshold=0.99,sim=0.0 | weighted or zero | test_semantic_phase2_part_2.py |
| TC-SEM-2265 | P1 | Threshold 0.99 similarity 0.1 | threshold=0.99,sim=0.1 | weighted or zero | test_semantic_phase2_part_2.py |
| TC-SEM-2266 | P1 | Threshold 0.99 similarity 0.25 | threshold=0.99,sim=0.25 | weighted or zero | test_semantic_phase2_part_2.py |
| TC-SEM-2267 | P1 | Threshold 0.99 similarity 0.5 | threshold=0.99,sim=0.5 | weighted or zero | test_semantic_phase2_part_2.py |
| TC-SEM-2268 | P1 | Threshold 0.99 similarity 0.75 | threshold=0.99,sim=0.75 | weighted or zero | test_semantic_phase2_part_2.py |
| TC-SEM-2269 | P1 | Threshold 0.99 similarity 0.9 | threshold=0.99,sim=0.9 | weighted or zero | test_semantic_phase2_part_2.py |
| TC-SEM-2270 | P1 | Threshold 0.99 similarity 0.95 | threshold=0.99,sim=0.95 | weighted or zero | test_semantic_phase2_part_2.py |
| TC-SEM-2271 | P1 | Threshold 0.99 similarity 0.99 | threshold=0.99,sim=0.99 | weighted or zero | test_semantic_phase2_part_2.py |
| TC-SEM-2272 | P1 | Threshold 0.99 similarity 1.0 | threshold=0.99,sim=1.0 | weighted or zero | test_semantic_phase2_part_2.py |
| TC-SEM-2273 | P1 | Threshold 1.0 similarity 0.0 | threshold=1.0,sim=0.0 | weighted or zero | test_semantic_phase2_part_2.py |
| TC-SEM-2274 | P1 | Threshold 1.0 similarity 0.1 | threshold=1.0,sim=0.1 | weighted or zero | test_semantic_phase2_part_2.py |
| TC-SEM-2275 | P1 | Threshold 1.0 similarity 0.25 | threshold=1.0,sim=0.25 | weighted or zero | test_semantic_phase2_part_2.py |
| TC-SEM-2276 | P1 | Threshold 1.0 similarity 0.5 | threshold=1.0,sim=0.5 | weighted or zero | test_semantic_phase2_part_2.py |
| TC-SEM-2277 | P1 | Threshold 1.0 similarity 0.75 | threshold=1.0,sim=0.75 | weighted or zero | test_semantic_phase2_part_2.py |
| TC-SEM-2278 | P1 | Threshold 1.0 similarity 0.9 | threshold=1.0,sim=0.9 | weighted or zero | test_semantic_phase2_part_2.py |
| TC-SEM-2279 | P1 | Threshold 1.0 similarity 0.95 | threshold=1.0,sim=0.95 | weighted or zero | test_semantic_phase2_part_2.py |
| TC-SEM-2280 | P1 | Threshold 1.0 similarity 0.99 | threshold=1.0,sim=0.99 | weighted or zero | test_semantic_phase2_part_2.py |
| TC-SEM-2281 | P1 | Threshold 1.0 similarity 1.0 | threshold=1.0,sim=1.0 | weighted or zero | test_semantic_phase2_part_2.py |
| TC-SEM-2282 | P1 | Query matrix at length 1 | len=1,type=the | all categories | test_semantic_phase2_part_2.py |
| TC-SEM-2283 | P1 | Query matrix at length 5 | len=5,type=the | all categories | test_semantic_phase2_part_2.py |
| TC-SEM-2284 | P1 | Query matrix at length 25 | len=25,type=the | all categories | test_semantic_phase2_part_2.py |
| TC-SEM-2285 | P1 | Query matrix at length 100 | len=100,type=the | all categories | test_semantic_phase2_part_2.py |
| TC-SEM-2286 | P1 | Query matrix at length 250 | len=250,type=the | all categories | test_semantic_phase2_part_2.py |
| TC-SEM-2287 | P1 | Query matrix at length 500 | len=500,type=the | all categories | test_semantic_phase2_part_2.py |
| TC-SEM-2288 | P1 | Query matrix at length 1000 | len=1000,type=the | all categories | test_semantic_phase2_part_2.py |
| TC-SEM-2289 | P1 | Query matrix at length 2000 | len=2000,type=the | all categories | test_semantic_phase2_part_2.py |
| TC-SEM-2290 | P1 | Query matrix at length 1 | len=1,type=i | all categories | test_semantic_phase2_part_2.py |
| TC-SEM-2291 | P1 | Query matrix at length 5 | len=5,type=i | all categories | test_semantic_phase2_part_2.py |
| TC-SEM-2292 | P1 | Query matrix at length 25 | len=25,type=i | all categories | test_semantic_phase2_part_2.py |
| TC-SEM-2293 | P1 | Query matrix at length 100 | len=100,type=i | all categories | test_semantic_phase2_part_2.py |
| TC-SEM-2294 | P1 | Query matrix at length 250 | len=250,type=i | all categories | test_semantic_phase2_part_2.py |
| TC-SEM-2295 | P1 | Query matrix at length 500 | len=500,type=i | all categories | test_semantic_phase2_part_2.py |
| TC-SEM-2296 | P1 | Query matrix at length 1000 | len=1000,type=i | all categories | test_semantic_phase2_part_2.py |
| TC-SEM-2297 | P1 | Query matrix at length 2000 | len=2000,type=i | all categories | test_semantic_phase2_part_2.py |
| TC-SEM-2298 | P1 | Query matrix at length 1 | len=1,type=explicit | all categories | test_semantic_phase2_part_2.py |
| TC-SEM-2299 | P1 | Query matrix at length 5 | len=5,type=explicit | all categories | test_semantic_phase2_part_2.py |
| TC-SEM-2300 | P1 | Query matrix at length 25 | len=25,type=explicit | all categories | test_semantic_phase2_part_2.py |
| TC-SEM-2301 | P1 | Query matrix at length 100 | len=100,type=explicit | all categories | test_semantic_phase2_part_3.py |
| TC-SEM-2302 | P1 | Query matrix at length 250 | len=250,type=explicit | all categories | test_semantic_phase2_part_3.py |
| TC-SEM-2303 | P1 | Query matrix at length 500 | len=500,type=explicit | all categories | test_semantic_phase2_part_3.py |
| TC-SEM-2304 | P1 | Query matrix at length 1000 | len=1000,type=explicit | all categories | test_semantic_phase2_part_3.py |
| TC-SEM-2305 | P1 | Query matrix at length 2000 | len=2000,type=explicit | all categories | test_semantic_phase2_part_3.py |
| TC-SEM-2306 | P1 | Query matrix at length 1 | len=1,type=i | all categories | test_semantic_phase2_part_3.py |
| TC-SEM-2307 | P1 | Query matrix at length 5 | len=5,type=i | all categories | test_semantic_phase2_part_3.py |
| TC-SEM-2308 | P1 | Query matrix at length 25 | len=25,type=i | all categories | test_semantic_phase2_part_3.py |
| TC-SEM-2309 | P1 | Query matrix at length 100 | len=100,type=i | all categories | test_semantic_phase2_part_3.py |
| TC-SEM-2310 | P1 | Query matrix at length 250 | len=250,type=i | all categories | test_semantic_phase2_part_3.py |
| TC-SEM-2311 | P1 | Query matrix at length 500 | len=500,type=i | all categories | test_semantic_phase2_part_3.py |
| TC-SEM-2312 | P1 | Query matrix at length 1000 | len=1000,type=i | all categories | test_semantic_phase2_part_3.py |
| TC-SEM-2313 | P1 | Query matrix at length 2000 | len=2000,type=i | all categories | test_semantic_phase2_part_3.py |
| TC-SEM-2314 | P1 | Query matrix at length 1 | len=1,type=your | all categories | test_semantic_phase2_part_3.py |
| TC-SEM-2315 | P1 | Query matrix at length 5 | len=5,type=your | all categories | test_semantic_phase2_part_3.py |
| TC-SEM-2316 | P1 | Query matrix at length 25 | len=25,type=your | all categories | test_semantic_phase2_part_3.py |
| TC-SEM-2317 | P1 | Query matrix at length 100 | len=100,type=your | all categories | test_semantic_phase2_part_3.py |
| TC-SEM-2318 | P1 | Query matrix at length 250 | len=250,type=your | all categories | test_semantic_phase2_part_3.py |
| TC-SEM-2319 | P1 | Query matrix at length 500 | len=500,type=your | all categories | test_semantic_phase2_part_3.py |
| TC-SEM-2320 | P1 | Query matrix at length 1000 | len=1000,type=your | all categories | test_semantic_phase2_part_3.py |
| TC-SEM-2321 | P1 | Query matrix at length 2000 | len=2000,type=your | all categories | test_semantic_phase2_part_3.py |
| TC-SEM-2322 | P1 | Query matrix at length 1 | len=1,type=buy | all categories | test_semantic_phase2_part_3.py |
| TC-SEM-2323 | P1 | Query matrix at length 5 | len=5,type=buy | all categories | test_semantic_phase2_part_3.py |
| TC-SEM-2324 | P1 | Query matrix at length 25 | len=25,type=buy | all categories | test_semantic_phase2_part_3.py |
| TC-SEM-2325 | P1 | Query matrix at length 100 | len=100,type=buy | all categories | test_semantic_phase2_part_3.py |
| TC-SEM-2326 | P1 | Query matrix at length 250 | len=250,type=buy | all categories | test_semantic_phase2_part_3.py |
| TC-SEM-2327 | P1 | Query matrix at length 500 | len=500,type=buy | all categories | test_semantic_phase2_part_3.py |
| TC-SEM-2328 | P1 | Query matrix at length 1000 | len=1000,type=buy | all categories | test_semantic_phase2_part_3.py |
| TC-SEM-2329 | P1 | Query matrix at length 2000 | len=2000,type=buy | all categories | test_semantic_phase2_part_3.py |
| TC-SEM-2330 | P1 | Query matrix at length 1 | len=1,type=the | all categories | test_semantic_phase2_part_3.py |
| TC-SEM-2331 | P1 | Query matrix at length 5 | len=5,type=the | all categories | test_semantic_phase2_part_3.py |
| TC-SEM-2332 | P1 | Query matrix at length 25 | len=25,type=the | all categories | test_semantic_phase2_part_3.py |
| TC-SEM-2333 | P1 | Query matrix at length 100 | len=100,type=the | all categories | test_semantic_phase2_part_3.py |
| TC-SEM-2334 | P1 | Query matrix at length 250 | len=250,type=the | all categories | test_semantic_phase2_part_3.py |
| TC-SEM-2335 | P1 | Query matrix at length 500 | len=500,type=the | all categories | test_semantic_phase2_part_3.py |
| TC-SEM-2336 | P1 | Query matrix at length 1000 | len=1000,type=the | all categories | test_semantic_phase2_part_3.py |
| TC-SEM-2337 | P1 | Query matrix at length 2000 | len=2000,type=the | all categories | test_semantic_phase2_part_3.py |
| TC-SEM-2338 | P1 | Query matrix at length 1 | len=1,type=politicians | all categories | test_semantic_phase2_part_3.py |
| TC-SEM-2339 | P1 | Query matrix at length 5 | len=5,type=politicians | all categories | test_semantic_phase2_part_3.py |
| TC-SEM-2340 | P1 | Query matrix at length 25 | len=25,type=politicians | all categories | test_semantic_phase2_part_3.py |
| TC-SEM-2341 | P1 | Query matrix at length 100 | len=100,type=politicians | all categories | test_semantic_phase2_part_3.py |
| TC-SEM-2342 | P1 | Query matrix at length 250 | len=250,type=politicians | all categories | test_semantic_phase2_part_3.py |
| TC-SEM-2343 | P1 | Query matrix at length 500 | len=500,type=politicians | all categories | test_semantic_phase2_part_3.py |
| TC-SEM-2344 | P1 | Query matrix at length 1000 | len=1000,type=politicians | all categories | test_semantic_phase2_part_3.py |
| TC-SEM-2345 | P1 | Query matrix at length 2000 | len=2000,type=politicians | all categories | test_semantic_phase2_part_3.py |
| TC-SEM-2346 | P1 | Query matrix at length 1 | len=1,type=he | all categories | test_semantic_phase2_part_3.py |
| TC-SEM-2347 | P1 | Query matrix at length 5 | len=5,type=he | all categories | test_semantic_phase2_part_3.py |
| TC-SEM-2348 | P1 | Query matrix at length 25 | len=25,type=he | all categories | test_semantic_phase2_part_3.py |
| TC-SEM-2349 | P1 | Query matrix at length 100 | len=100,type=he | all categories | test_semantic_phase2_part_3.py |
| TC-SEM-2350 | P1 | Query matrix at length 250 | len=250,type=he | all categories | test_semantic_phase2_part_3.py |
| TC-SEM-2351 | P1 | Query matrix at length 500 | len=500,type=he | all categories | test_semantic_phase2_part_3.py |
| TC-SEM-2352 | P1 | Query matrix at length 1000 | len=1000,type=he | all categories | test_semantic_phase2_part_3.py |
| TC-SEM-2353 | P1 | Query matrix at length 2000 | len=2000,type=he | all categories | test_semantic_phase2_part_3.py |
| TC-SEM-2354 | P1 | Query matrix at length 1 | len=1,type=she | all categories | test_semantic_phase2_part_3.py |
| TC-SEM-2355 | P1 | Query matrix at length 5 | len=5,type=she | all categories | test_semantic_phase2_part_3.py |
| TC-SEM-2356 | P1 | Query matrix at length 25 | len=25,type=she | all categories | test_semantic_phase2_part_3.py |
| TC-SEM-2357 | P1 | Query matrix at length 100 | len=100,type=she | all categories | test_semantic_phase2_part_3.py |
| TC-SEM-2358 | P1 | Query matrix at length 250 | len=250,type=she | all categories | test_semantic_phase2_part_3.py |
| TC-SEM-2359 | P1 | Query matrix at length 500 | len=500,type=she | all categories | test_semantic_phase2_part_3.py |
| TC-SEM-2360 | P1 | Query matrix at length 1000 | len=1000,type=she | all categories | test_semantic_phase2_part_3.py |
| TC-SEM-2361 | P1 | Query matrix at length 2000 | len=2000,type=she | all categories | test_semantic_phase2_part_3.py |
| TC-SEM-2362 | P1 | Query matrix at length 1 | len=1,type=watch | all categories | test_semantic_phase2_part_3.py |
| TC-SEM-2363 | P1 | Query matrix at length 5 | len=5,type=watch | all categories | test_semantic_phase2_part_3.py |
| TC-SEM-2364 | P1 | Query matrix at length 25 | len=25,type=watch | all categories | test_semantic_phase2_part_3.py |
| TC-SEM-2365 | P1 | Query matrix at length 100 | len=100,type=watch | all categories | test_semantic_phase2_part_3.py |
| TC-SEM-2366 | P1 | Query matrix at length 250 | len=250,type=watch | all categories | test_semantic_phase2_part_3.py |
| TC-SEM-2367 | P1 | Query matrix at length 500 | len=500,type=watch | all categories | test_semantic_phase2_part_3.py |
| TC-SEM-2368 | P1 | Query matrix at length 1000 | len=1000,type=watch | all categories | test_semantic_phase2_part_3.py |
| TC-SEM-2369 | P1 | Query matrix at length 2000 | len=2000,type=watch | all categories | test_semantic_phase2_part_3.py |
| TC-SEM-2370 | P1 | Query matrix at length 1 | len=1,type=the | all categories | test_semantic_phase2_part_3.py |
| TC-SEM-2371 | P1 | Query matrix at length 5 | len=5,type=the | all categories | test_semantic_phase2_part_3.py |
| TC-SEM-2372 | P1 | Query matrix at length 25 | len=25,type=the | all categories | test_semantic_phase2_part_3.py |
| TC-SEM-2373 | P1 | Query matrix at length 100 | len=100,type=the | all categories | test_semantic_phase2_part_3.py |
| TC-SEM-2374 | P1 | Query matrix at length 250 | len=250,type=the | all categories | test_semantic_phase2_part_3.py |
| TC-SEM-2375 | P1 | Query matrix at length 500 | len=500,type=the | all categories | test_semantic_phase2_part_3.py |
| TC-SEM-2376 | P1 | Query matrix at length 1000 | len=1000,type=the | all categories | test_semantic_phase2_part_3.py |
| TC-SEM-2377 | P1 | Query matrix at length 2000 | len=2000,type=the | all categories | test_semantic_phase2_part_3.py |
| TC-SEM-2378 | P1 | Query matrix at length 1 | len=1,type=secret | all categories | test_semantic_phase2_part_3.py |
| TC-SEM-2379 | P1 | Query matrix at length 5 | len=5,type=secret | all categories | test_semantic_phase2_part_3.py |
| TC-SEM-2380 | P1 | Query matrix at length 25 | len=25,type=secret | all categories | test_semantic_phase2_part_3.py |
| TC-SEM-2381 | P1 | Query matrix at length 100 | len=100,type=secret | all categories | test_semantic_phase2_part_3.py |
| TC-SEM-2382 | P1 | Query matrix at length 250 | len=250,type=secret | all categories | test_semantic_phase2_part_3.py |
| TC-SEM-2383 | P1 | Query matrix at length 500 | len=500,type=secret | all categories | test_semantic_phase2_part_3.py |
| TC-SEM-2384 | P1 | Query matrix at length 1000 | len=1000,type=secret | all categories | test_semantic_phase2_part_3.py |
| TC-SEM-2385 | P1 | Query matrix at length 2000 | len=2000,type=secret | all categories | test_semantic_phase2_part_3.py |
| TC-SEM-2386 | P1 | Query matrix at length 1 | len=1,type=join | all categories | test_semantic_phase2_part_3.py |
| TC-SEM-2387 | P1 | Query matrix at length 5 | len=5,type=join | all categories | test_semantic_phase2_part_3.py |
| TC-SEM-2388 | P1 | Query matrix at length 25 | len=25,type=join | all categories | test_semantic_phase2_part_3.py |
| TC-SEM-2389 | P1 | Query matrix at length 100 | len=100,type=join | all categories | test_semantic_phase2_part_3.py |
| TC-SEM-2390 | P1 | Query matrix at length 250 | len=250,type=join | all categories | test_semantic_phase2_part_3.py |
| TC-SEM-2391 | P1 | Query matrix at length 500 | len=500,type=join | all categories | test_semantic_phase2_part_3.py |
| TC-SEM-2392 | P1 | Query matrix at length 1000 | len=1000,type=join | all categories | test_semantic_phase2_part_3.py |
| TC-SEM-2393 | P1 | Query matrix at length 2000 | len=2000,type=join | all categories | test_semantic_phase2_part_3.py |
| TC-SEM-2394 | P1 | Query matrix at length 1 | len=1,type=ordinary | all categories | test_semantic_phase2_part_3.py |
| TC-SEM-2395 | P1 | Query matrix at length 5 | len=5,type=ordinary | all categories | test_semantic_phase2_part_3.py |
| TC-SEM-2396 | P1 | Query matrix at length 25 | len=25,type=ordinary | all categories | test_semantic_phase2_part_3.py |
| TC-SEM-2397 | P1 | Query matrix at length 100 | len=100,type=ordinary | all categories | test_semantic_phase2_part_3.py |
| TC-SEM-2398 | P1 | Query matrix at length 250 | len=250,type=ordinary | all categories | test_semantic_phase2_part_3.py |
| TC-SEM-2399 | P1 | Query matrix at length 500 | len=500,type=ordinary | all categories | test_semantic_phase2_part_3.py |
| TC-SEM-2400 | P1 | Query matrix at length 1000 | len=1000,type=ordinary | all categories | test_semantic_phase2_part_3.py |
| TC-SEM-2401 | P1 | Query matrix at length 2000 | len=2000,type=ordinary | all categories | test_semantic_phase2_part_4.py |
| TC-SEM-2402 | P1 | Add 1 examples to political | category=political,count=1 | count grows | test_semantic_phase2_part_4.py |
| TC-SEM-2403 | P2 | Delete roundtrip for political x 1 | category=political,count=1 | count restored | test_semantic_phase2_part_4.py |
| TC-SEM-2404 | P1 | Add 2 examples to political | category=political,count=2 | count grows | test_semantic_phase2_part_4.py |
| TC-SEM-2405 | P2 | Delete roundtrip for political x 2 | category=political,count=2 | count restored | test_semantic_phase2_part_4.py |
| TC-SEM-2406 | P1 | Add 3 examples to political | category=political,count=3 | count grows | test_semantic_phase2_part_4.py |
| TC-SEM-2407 | P2 | Delete roundtrip for political x 3 | category=political,count=3 | count restored | test_semantic_phase2_part_4.py |
| TC-SEM-2408 | P1 | Add 5 examples to political | category=political,count=5 | count grows | test_semantic_phase2_part_4.py |
| TC-SEM-2409 | P2 | Delete roundtrip for political x 5 | category=political,count=5 | count restored | test_semantic_phase2_part_4.py |
| TC-SEM-2410 | P1 | Add 10 examples to political | category=political,count=10 | count grows | test_semantic_phase2_part_4.py |
| TC-SEM-2411 | P2 | Delete roundtrip for political x 10 | category=political,count=10 | count restored | test_semantic_phase2_part_4.py |
| TC-SEM-2412 | P1 | Add 15 examples to political | category=political,count=15 | count grows | test_semantic_phase2_part_4.py |
| TC-SEM-2413 | P2 | Delete roundtrip for political x 15 | category=political,count=15 | count restored | test_semantic_phase2_part_4.py |
| TC-SEM-2414 | P1 | Add 20 examples to political | category=political,count=20 | count grows | test_semantic_phase2_part_4.py |
| TC-SEM-2415 | P2 | Delete roundtrip for political x 20 | category=political,count=20 | count restored | test_semantic_phase2_part_4.py |
| TC-SEM-2416 | P1 | Add 25 examples to political | category=political,count=25 | count grows | test_semantic_phase2_part_4.py |
| TC-SEM-2417 | P2 | Delete roundtrip for political x 25 | category=political,count=25 | count restored | test_semantic_phase2_part_4.py |
| TC-SEM-2418 | P1 | Add 1 examples to violence | category=violence,count=1 | count grows | test_semantic_phase2_part_4.py |
| TC-SEM-2419 | P2 | Delete roundtrip for violence x 1 | category=violence,count=1 | count restored | test_semantic_phase2_part_4.py |
| TC-SEM-2420 | P1 | Add 2 examples to violence | category=violence,count=2 | count grows | test_semantic_phase2_part_4.py |
| TC-SEM-2421 | P2 | Delete roundtrip for violence x 2 | category=violence,count=2 | count restored | test_semantic_phase2_part_4.py |
| TC-SEM-2422 | P1 | Add 3 examples to violence | category=violence,count=3 | count grows | test_semantic_phase2_part_4.py |
| TC-SEM-2423 | P2 | Delete roundtrip for violence x 3 | category=violence,count=3 | count restored | test_semantic_phase2_part_4.py |
| TC-SEM-2424 | P1 | Add 5 examples to violence | category=violence,count=5 | count grows | test_semantic_phase2_part_4.py |
| TC-SEM-2425 | P2 | Delete roundtrip for violence x 5 | category=violence,count=5 | count restored | test_semantic_phase2_part_4.py |
| TC-SEM-2426 | P1 | Add 10 examples to violence | category=violence,count=10 | count grows | test_semantic_phase2_part_4.py |
| TC-SEM-2427 | P2 | Delete roundtrip for violence x 10 | category=violence,count=10 | count restored | test_semantic_phase2_part_4.py |
| TC-SEM-2428 | P1 | Add 15 examples to violence | category=violence,count=15 | count grows | test_semantic_phase2_part_4.py |
| TC-SEM-2429 | P2 | Delete roundtrip for violence x 15 | category=violence,count=15 | count restored | test_semantic_phase2_part_4.py |
| TC-SEM-2430 | P1 | Add 20 examples to violence | category=violence,count=20 | count grows | test_semantic_phase2_part_4.py |
| TC-SEM-2431 | P2 | Delete roundtrip for violence x 20 | category=violence,count=20 | count restored | test_semantic_phase2_part_4.py |
| TC-SEM-2432 | P1 | Add 25 examples to violence | category=violence,count=25 | count grows | test_semantic_phase2_part_4.py |
| TC-SEM-2433 | P2 | Delete roundtrip for violence x 25 | category=violence,count=25 | count restored | test_semantic_phase2_part_4.py |
| TC-SEM-2434 | P1 | Add 1 examples to sexual | category=sexual,count=1 | count grows | test_semantic_phase2_part_4.py |
| TC-SEM-2435 | P2 | Delete roundtrip for sexual x 1 | category=sexual,count=1 | count restored | test_semantic_phase2_part_4.py |
| TC-SEM-2436 | P1 | Add 2 examples to sexual | category=sexual,count=2 | count grows | test_semantic_phase2_part_4.py |
| TC-SEM-2437 | P2 | Delete roundtrip for sexual x 2 | category=sexual,count=2 | count restored | test_semantic_phase2_part_4.py |
| TC-SEM-2438 | P1 | Add 3 examples to sexual | category=sexual,count=3 | count grows | test_semantic_phase2_part_4.py |
| TC-SEM-2439 | P2 | Delete roundtrip for sexual x 3 | category=sexual,count=3 | count restored | test_semantic_phase2_part_4.py |
| TC-SEM-2440 | P1 | Add 5 examples to sexual | category=sexual,count=5 | count grows | test_semantic_phase2_part_4.py |
| TC-SEM-2441 | P2 | Delete roundtrip for sexual x 5 | category=sexual,count=5 | count restored | test_semantic_phase2_part_4.py |
| TC-SEM-2442 | P1 | Add 10 examples to sexual | category=sexual,count=10 | count grows | test_semantic_phase2_part_4.py |
| TC-SEM-2443 | P2 | Delete roundtrip for sexual x 10 | category=sexual,count=10 | count restored | test_semantic_phase2_part_4.py |
| TC-SEM-2444 | P1 | Add 15 examples to sexual | category=sexual,count=15 | count grows | test_semantic_phase2_part_4.py |
| TC-SEM-2445 | P2 | Delete roundtrip for sexual x 15 | category=sexual,count=15 | count restored | test_semantic_phase2_part_4.py |
| TC-SEM-2446 | P1 | Add 20 examples to sexual | category=sexual,count=20 | count grows | test_semantic_phase2_part_4.py |
| TC-SEM-2447 | P2 | Delete roundtrip for sexual x 20 | category=sexual,count=20 | count restored | test_semantic_phase2_part_4.py |
| TC-SEM-2448 | P1 | Add 25 examples to sexual | category=sexual,count=25 | count grows | test_semantic_phase2_part_4.py |
| TC-SEM-2449 | P2 | Delete roundtrip for sexual x 25 | category=sexual,count=25 | count restored | test_semantic_phase2_part_4.py |
| TC-SEM-2450 | P1 | Add 1 examples to hate | category=hate,count=1 | count grows | test_semantic_phase2_part_4.py |
| TC-SEM-2451 | P2 | Delete roundtrip for hate x 1 | category=hate,count=1 | count restored | test_semantic_phase2_part_4.py |
| TC-SEM-2452 | P1 | Add 2 examples to hate | category=hate,count=2 | count grows | test_semantic_phase2_part_4.py |
| TC-SEM-2453 | P2 | Delete roundtrip for hate x 2 | category=hate,count=2 | count restored | test_semantic_phase2_part_4.py |
| TC-SEM-2454 | P1 | Add 3 examples to hate | category=hate,count=3 | count grows | test_semantic_phase2_part_4.py |
| TC-SEM-2455 | P2 | Delete roundtrip for hate x 3 | category=hate,count=3 | count restored | test_semantic_phase2_part_4.py |
| TC-SEM-2456 | P1 | Add 5 examples to hate | category=hate,count=5 | count grows | test_semantic_phase2_part_4.py |
| TC-SEM-2457 | P2 | Delete roundtrip for hate x 5 | category=hate,count=5 | count restored | test_semantic_phase2_part_4.py |
| TC-SEM-2458 | P1 | Add 10 examples to hate | category=hate,count=10 | count grows | test_semantic_phase2_part_4.py |
| TC-SEM-2459 | P2 | Delete roundtrip for hate x 10 | category=hate,count=10 | count restored | test_semantic_phase2_part_4.py |
| TC-SEM-2460 | P1 | Add 15 examples to hate | category=hate,count=15 | count grows | test_semantic_phase2_part_4.py |
| TC-SEM-2461 | P2 | Delete roundtrip for hate x 15 | category=hate,count=15 | count restored | test_semantic_phase2_part_4.py |
| TC-SEM-2462 | P1 | Add 20 examples to hate | category=hate,count=20 | count grows | test_semantic_phase2_part_4.py |
| TC-SEM-2463 | P2 | Delete roundtrip for hate x 20 | category=hate,count=20 | count restored | test_semantic_phase2_part_4.py |
| TC-SEM-2464 | P1 | Add 25 examples to hate | category=hate,count=25 | count grows | test_semantic_phase2_part_4.py |
| TC-SEM-2465 | P2 | Delete roundtrip for hate x 25 | category=hate,count=25 | count restored | test_semantic_phase2_part_4.py |
| TC-SEM-2466 | P1 | Add 1 examples to pii | category=pii,count=1 | count grows | test_semantic_phase2_part_4.py |
| TC-SEM-2467 | P2 | Delete roundtrip for pii x 1 | category=pii,count=1 | count restored | test_semantic_phase2_part_4.py |
| TC-SEM-2468 | P1 | Add 2 examples to pii | category=pii,count=2 | count grows | test_semantic_phase2_part_4.py |
| TC-SEM-2469 | P2 | Delete roundtrip for pii x 2 | category=pii,count=2 | count restored | test_semantic_phase2_part_4.py |
| TC-SEM-2470 | P1 | Add 3 examples to pii | category=pii,count=3 | count grows | test_semantic_phase2_part_4.py |
| TC-SEM-2471 | P2 | Delete roundtrip for pii x 3 | category=pii,count=3 | count restored | test_semantic_phase2_part_4.py |
| TC-SEM-2472 | P1 | Add 5 examples to pii | category=pii,count=5 | count grows | test_semantic_phase2_part_4.py |
| TC-SEM-2473 | P2 | Delete roundtrip for pii x 5 | category=pii,count=5 | count restored | test_semantic_phase2_part_4.py |
| TC-SEM-2474 | P1 | Add 10 examples to pii | category=pii,count=10 | count grows | test_semantic_phase2_part_4.py |
| TC-SEM-2475 | P2 | Delete roundtrip for pii x 10 | category=pii,count=10 | count restored | test_semantic_phase2_part_4.py |
| TC-SEM-2476 | P1 | Add 15 examples to pii | category=pii,count=15 | count grows | test_semantic_phase2_part_4.py |
| TC-SEM-2477 | P2 | Delete roundtrip for pii x 15 | category=pii,count=15 | count restored | test_semantic_phase2_part_4.py |
| TC-SEM-2478 | P1 | Add 20 examples to pii | category=pii,count=20 | count grows | test_semantic_phase2_part_4.py |
| TC-SEM-2479 | P2 | Delete roundtrip for pii x 20 | category=pii,count=20 | count restored | test_semantic_phase2_part_4.py |
| TC-SEM-2480 | P1 | Add 25 examples to pii | category=pii,count=25 | count grows | test_semantic_phase2_part_4.py |
| TC-SEM-2481 | P2 | Delete roundtrip for pii x 25 | category=pii,count=25 | count restored | test_semantic_phase2_part_4.py |
| TC-SEM-2482 | P1 | Add 1 examples to ads | category=ads,count=1 | count grows | test_semantic_phase2_part_4.py |
| TC-SEM-2483 | P2 | Delete roundtrip for ads x 1 | category=ads,count=1 | count restored | test_semantic_phase2_part_4.py |
| TC-SEM-2484 | P1 | Add 2 examples to ads | category=ads,count=2 | count grows | test_semantic_phase2_part_4.py |
| TC-SEM-2485 | P2 | Delete roundtrip for ads x 2 | category=ads,count=2 | count restored | test_semantic_phase2_part_4.py |
| TC-SEM-2486 | P1 | Add 3 examples to ads | category=ads,count=3 | count grows | test_semantic_phase2_part_4.py |
| TC-SEM-2487 | P2 | Delete roundtrip for ads x 3 | category=ads,count=3 | count restored | test_semantic_phase2_part_4.py |
| TC-SEM-2488 | P1 | Add 5 examples to ads | category=ads,count=5 | count grows | test_semantic_phase2_part_4.py |
| TC-SEM-2489 | P2 | Delete roundtrip for ads x 5 | category=ads,count=5 | count restored | test_semantic_phase2_part_4.py |
| TC-SEM-2490 | P1 | Add 10 examples to ads | category=ads,count=10 | count grows | test_semantic_phase2_part_4.py |
| TC-SEM-2491 | P2 | Delete roundtrip for ads x 10 | category=ads,count=10 | count restored | test_semantic_phase2_part_4.py |
| TC-SEM-2492 | P1 | Add 15 examples to ads | category=ads,count=15 | count grows | test_semantic_phase2_part_4.py |
| TC-SEM-2493 | P2 | Delete roundtrip for ads x 15 | category=ads,count=15 | count restored | test_semantic_phase2_part_4.py |
| TC-SEM-2494 | P1 | Add 20 examples to ads | category=ads,count=20 | count grows | test_semantic_phase2_part_4.py |
| TC-SEM-2495 | P2 | Delete roundtrip for ads x 20 | category=ads,count=20 | count restored | test_semantic_phase2_part_4.py |
| TC-SEM-2496 | P1 | Add 25 examples to ads | category=ads,count=25 | count grows | test_semantic_phase2_part_4.py |
| TC-SEM-2497 | P2 | Delete roundtrip for ads x 25 | category=ads,count=25 | count restored | test_semantic_phase2_part_4.py |
| TC-SEM-2498 | P1 | Add 1 examples to other | category=other,count=1 | count grows | test_semantic_phase2_part_4.py |
| TC-SEM-2499 | P2 | Delete roundtrip for other x 1 | category=other,count=1 | count restored | test_semantic_phase2_part_4.py |
| TC-SEM-2500 | P1 | Add 2 examples to other | category=other,count=2 | count grows | test_semantic_phase2_part_4.py |
| TC-SEM-2501 | P2 | Delete roundtrip for other x 2 | category=other,count=2 | count restored | test_semantic_phase2_part_5.py |
| TC-SEM-2502 | P1 | Add 3 examples to other | category=other,count=3 | count grows | test_semantic_phase2_part_5.py |
| TC-SEM-2503 | P2 | Delete roundtrip for other x 3 | category=other,count=3 | count restored | test_semantic_phase2_part_5.py |
| TC-SEM-2504 | P1 | Add 5 examples to other | category=other,count=5 | count grows | test_semantic_phase2_part_5.py |
| TC-SEM-2505 | P2 | Delete roundtrip for other x 5 | category=other,count=5 | count restored | test_semantic_phase2_part_5.py |
| TC-SEM-2506 | P1 | Add 10 examples to other | category=other,count=10 | count grows | test_semantic_phase2_part_5.py |
| TC-SEM-2507 | P2 | Delete roundtrip for other x 10 | category=other,count=10 | count restored | test_semantic_phase2_part_5.py |
| TC-SEM-2508 | P1 | Add 15 examples to other | category=other,count=15 | count grows | test_semantic_phase2_part_5.py |
| TC-SEM-2509 | P2 | Delete roundtrip for other x 15 | category=other,count=15 | count restored | test_semantic_phase2_part_5.py |
| TC-SEM-2510 | P1 | Add 20 examples to other | category=other,count=20 | count grows | test_semantic_phase2_part_5.py |
| TC-SEM-2511 | P2 | Delete roundtrip for other x 20 | category=other,count=20 | count restored | test_semantic_phase2_part_5.py |
| TC-SEM-2512 | P1 | Add 25 examples to other | category=other,count=25 | count grows | test_semantic_phase2_part_5.py |
| TC-SEM-2513 | P2 | Delete roundtrip for other x 25 | category=other,count=25 | count restored | test_semantic_phase2_part_5.py |
| TC-SEM-2514 | P2 | Stats field political (categories) | category=political,field=categories | stats valid | test_semantic_phase2_part_5.py |
| TC-SEM-2515 | P2 | Stats field political (model) | category=political,field=model | stats valid | test_semantic_phase2_part_5.py |
| TC-SEM-2516 | P2 | Stats field political (available) | category=political,field=available | stats valid | test_semantic_phase2_part_5.py |
| TC-SEM-2517 | P2 | Stats field political (top_k) | category=political,field=top_k | stats valid | test_semantic_phase2_part_5.py |
| TC-SEM-2518 | P2 | Stats field violence (categories) | category=violence,field=categories | stats valid | test_semantic_phase2_part_5.py |
| TC-SEM-2519 | P2 | Stats field violence (model) | category=violence,field=model | stats valid | test_semantic_phase2_part_5.py |
| TC-SEM-2520 | P2 | Stats field violence (available) | category=violence,field=available | stats valid | test_semantic_phase2_part_5.py |
| TC-SEM-2521 | P2 | Stats field violence (top_k) | category=violence,field=top_k | stats valid | test_semantic_phase2_part_5.py |
| TC-SEM-2522 | P2 | Stats field sexual (categories) | category=sexual,field=categories | stats valid | test_semantic_phase2_part_5.py |
| TC-SEM-2523 | P2 | Stats field sexual (model) | category=sexual,field=model | stats valid | test_semantic_phase2_part_5.py |
| TC-SEM-2524 | P2 | Stats field sexual (available) | category=sexual,field=available | stats valid | test_semantic_phase2_part_5.py |
| TC-SEM-2525 | P2 | Stats field sexual (top_k) | category=sexual,field=top_k | stats valid | test_semantic_phase2_part_5.py |
| TC-SEM-2526 | P2 | Stats field hate (categories) | category=hate,field=categories | stats valid | test_semantic_phase2_part_5.py |
| TC-SEM-2527 | P2 | Stats field hate (model) | category=hate,field=model | stats valid | test_semantic_phase2_part_5.py |
| TC-SEM-2528 | P2 | Stats field hate (available) | category=hate,field=available | stats valid | test_semantic_phase2_part_5.py |
| TC-SEM-2529 | P2 | Stats field hate (top_k) | category=hate,field=top_k | stats valid | test_semantic_phase2_part_5.py |
| TC-SEM-2530 | P2 | Stats field pii (categories) | category=pii,field=categories | stats valid | test_semantic_phase2_part_5.py |
| TC-SEM-2531 | P2 | Stats field pii (model) | category=pii,field=model | stats valid | test_semantic_phase2_part_5.py |
| TC-SEM-2532 | P2 | Stats field pii (available) | category=pii,field=available | stats valid | test_semantic_phase2_part_5.py |
| TC-SEM-2533 | P2 | Stats field pii (top_k) | category=pii,field=top_k | stats valid | test_semantic_phase2_part_5.py |
| TC-SEM-2534 | P2 | Stats field ads (categories) | category=ads,field=categories | stats valid | test_semantic_phase2_part_5.py |
| TC-SEM-2535 | P2 | Stats field ads (model) | category=ads,field=model | stats valid | test_semantic_phase2_part_5.py |
| TC-SEM-2536 | P2 | Stats field ads (available) | category=ads,field=available | stats valid | test_semantic_phase2_part_5.py |
| TC-SEM-2537 | P2 | Stats field ads (top_k) | category=ads,field=top_k | stats valid | test_semantic_phase2_part_5.py |
| TC-SEM-2538 | P2 | Stats field other (categories) | category=other,field=categories | stats valid | test_semantic_phase2_part_5.py |
| TC-SEM-2539 | P2 | Stats field other (model) | category=other,field=model | stats valid | test_semantic_phase2_part_5.py |
| TC-SEM-2540 | P2 | Stats field other (available) | category=other,field=available | stats valid | test_semantic_phase2_part_5.py |
| TC-SEM-2541 | P2 | Stats field other (top_k) | category=other,field=top_k | stats valid | test_semantic_phase2_part_5.py |
| TC-SEM-2542 | P3 | Top-k 1 accepted | top_k=1 | accepted | test_semantic_phase2_part_5.py |
| TC-SEM-2543 | P3 | Top-k 2 accepted | top_k=2 | accepted | test_semantic_phase2_part_5.py |
| TC-SEM-2544 | P3 | Top-k 3 accepted | top_k=3 | accepted | test_semantic_phase2_part_5.py |
| TC-SEM-2545 | P3 | Top-k 5 accepted | top_k=5 | accepted | test_semantic_phase2_part_5.py |
| TC-SEM-2546 | P3 | Top-k 8 accepted | top_k=8 | accepted | test_semantic_phase2_part_5.py |
| TC-SEM-2547 | P3 | Top-k 10 accepted | top_k=10 | accepted | test_semantic_phase2_part_5.py |
| TC-SEM-2548 | P3 | Top-k 16 accepted | top_k=16 | accepted | test_semantic_phase2_part_5.py |
| TC-SEM-2549 | P3 | Top-k 25 accepted | top_k=25 | accepted | test_semantic_phase2_part_5.py |
| TC-SEM-2550 | P3 | Top-k 32 accepted | top_k=32 | accepted | test_semantic_phase2_part_5.py |
| TC-SEM-2551 | P3 | Top-k 50 accepted | top_k=50 | accepted | test_semantic_phase2_part_5.py |
| TC-SEM-2552 | P3 | Top-k 64 accepted | top_k=64 | accepted | test_semantic_phase2_part_5.py |
| TC-SEM-2553 | P3 | Top-k 100 accepted | top_k=100 | accepted | test_semantic_phase2_part_5.py |
| TC-SEM-2554 | P3 | Top-k 128 accepted | top_k=128 | accepted | test_semantic_phase2_part_5.py |
| TC-SEM-2555 | P2 | Weight mapping badwords = 5 | detector=badwords,key=WEIGHT_DETECTOR_BADWORDS,value=5 | weight in range | test_semantic_phase2_part_5.py |
| TC-SEM-2556 | P2 | Weight mapping badwords = 8 | detector=badwords,key=WEIGHT_DETECTOR_BADWORDS,value=8 | weight in range | test_semantic_phase2_part_5.py |
| TC-SEM-2557 | P2 | Weight mapping badwords = 10 | detector=badwords,key=WEIGHT_DETECTOR_BADWORDS,value=10 | weight in range | test_semantic_phase2_part_5.py |
| TC-SEM-2558 | P2 | Weight mapping badwords = 12 | detector=badwords,key=WEIGHT_DETECTOR_BADWORDS,value=12 | weight in range | test_semantic_phase2_part_5.py |
| TC-SEM-2559 | P2 | Weight mapping badwords = 15 | detector=badwords,key=WEIGHT_DETECTOR_BADWORDS,value=15 | weight in range | test_semantic_phase2_part_5.py |
| TC-SEM-2560 | P2 | Weight mapping badwords = 20 | detector=badwords,key=WEIGHT_DETECTOR_BADWORDS,value=20 | weight in range | test_semantic_phase2_part_5.py |
| TC-SEM-2561 | P2 | Weight mapping badwords = 25 | detector=badwords,key=WEIGHT_DETECTOR_BADWORDS,value=25 | weight in range | test_semantic_phase2_part_5.py |
| TC-SEM-2562 | P2 | Weight mapping badwords = 30 | detector=badwords,key=WEIGHT_DETECTOR_BADWORDS,value=30 | weight in range | test_semantic_phase2_part_5.py |
| TC-SEM-2563 | P2 | Weight mapping badwords = 35 | detector=badwords,key=WEIGHT_DETECTOR_BADWORDS,value=35 | weight in range | test_semantic_phase2_part_5.py |
| TC-SEM-2564 | P2 | Weight mapping badwords = 40 | detector=badwords,key=WEIGHT_DETECTOR_BADWORDS,value=40 | weight in range | test_semantic_phase2_part_5.py |
| TC-SEM-2565 | P2 | Weight mapping badwords = 45 | detector=badwords,key=WEIGHT_DETECTOR_BADWORDS,value=45 | weight in range | test_semantic_phase2_part_5.py |
| TC-SEM-2566 | P2 | Weight mapping badwords = 50 | detector=badwords,key=WEIGHT_DETECTOR_BADWORDS,value=50 | weight in range | test_semantic_phase2_part_5.py |
| TC-SEM-2567 | P2 | Weight mapping profanite = 5 | detector=profanite,key=WEIGHT_DETECTOR_PROFANITE,value=5 | weight in range | test_semantic_phase2_part_5.py |
| TC-SEM-2568 | P2 | Weight mapping profanite = 8 | detector=profanite,key=WEIGHT_DETECTOR_PROFANITE,value=8 | weight in range | test_semantic_phase2_part_5.py |
| TC-SEM-2569 | P2 | Weight mapping profanite = 10 | detector=profanite,key=WEIGHT_DETECTOR_PROFANITE,value=10 | weight in range | test_semantic_phase2_part_5.py |
| TC-SEM-2570 | P2 | Weight mapping profanite = 12 | detector=profanite,key=WEIGHT_DETECTOR_PROFANITE,value=12 | weight in range | test_semantic_phase2_part_5.py |
| TC-SEM-2571 | P2 | Weight mapping profanite = 15 | detector=profanite,key=WEIGHT_DETECTOR_PROFANITE,value=15 | weight in range | test_semantic_phase2_part_5.py |
| TC-SEM-2572 | P2 | Weight mapping profanite = 20 | detector=profanite,key=WEIGHT_DETECTOR_PROFANITE,value=20 | weight in range | test_semantic_phase2_part_5.py |
| TC-SEM-2573 | P2 | Weight mapping profanite = 25 | detector=profanite,key=WEIGHT_DETECTOR_PROFANITE,value=25 | weight in range | test_semantic_phase2_part_5.py |
| TC-SEM-2574 | P2 | Weight mapping profanite = 30 | detector=profanite,key=WEIGHT_DETECTOR_PROFANITE,value=30 | weight in range | test_semantic_phase2_part_5.py |
| TC-SEM-2575 | P2 | Weight mapping profanite = 35 | detector=profanite,key=WEIGHT_DETECTOR_PROFANITE,value=35 | weight in range | test_semantic_phase2_part_5.py |
| TC-SEM-2576 | P2 | Weight mapping profanite = 40 | detector=profanite,key=WEIGHT_DETECTOR_PROFANITE,value=40 | weight in range | test_semantic_phase2_part_5.py |
| TC-SEM-2577 | P2 | Weight mapping profanite = 45 | detector=profanite,key=WEIGHT_DETECTOR_PROFANITE,value=45 | weight in range | test_semantic_phase2_part_5.py |
| TC-SEM-2578 | P2 | Weight mapping profanite = 50 | detector=profanite,key=WEIGHT_DETECTOR_PROFANITE,value=50 | weight in range | test_semantic_phase2_part_5.py |
| TC-SEM-2579 | P2 | Weight mapping glin-profanity = 5 | detector=glin-profanity,key=WEIGHT_DETECTOR_GLIN,value=5 | weight in range | test_semantic_phase2_part_5.py |
| TC-SEM-2580 | P2 | Weight mapping glin-profanity = 8 | detector=glin-profanity,key=WEIGHT_DETECTOR_GLIN,value=8 | weight in range | test_semantic_phase2_part_5.py |
| TC-SEM-2581 | P2 | Weight mapping glin-profanity = 10 | detector=glin-profanity,key=WEIGHT_DETECTOR_GLIN,value=10 | weight in range | test_semantic_phase2_part_5.py |
| TC-SEM-2582 | P2 | Weight mapping glin-profanity = 12 | detector=glin-profanity,key=WEIGHT_DETECTOR_GLIN,value=12 | weight in range | test_semantic_phase2_part_5.py |
| TC-SEM-2583 | P2 | Weight mapping glin-profanity = 15 | detector=glin-profanity,key=WEIGHT_DETECTOR_GLIN,value=15 | weight in range | test_semantic_phase2_part_5.py |
| TC-SEM-2584 | P2 | Weight mapping glin-profanity = 20 | detector=glin-profanity,key=WEIGHT_DETECTOR_GLIN,value=20 | weight in range | test_semantic_phase2_part_5.py |
| TC-SEM-2585 | P2 | Weight mapping glin-profanity = 25 | detector=glin-profanity,key=WEIGHT_DETECTOR_GLIN,value=25 | weight in range | test_semantic_phase2_part_5.py |
| TC-SEM-2586 | P2 | Weight mapping glin-profanity = 30 | detector=glin-profanity,key=WEIGHT_DETECTOR_GLIN,value=30 | weight in range | test_semantic_phase2_part_5.py |
| TC-SEM-2587 | P2 | Weight mapping glin-profanity = 35 | detector=glin-profanity,key=WEIGHT_DETECTOR_GLIN,value=35 | weight in range | test_semantic_phase2_part_5.py |
| TC-SEM-2588 | P2 | Weight mapping glin-profanity = 40 | detector=glin-profanity,key=WEIGHT_DETECTOR_GLIN,value=40 | weight in range | test_semantic_phase2_part_5.py |
| TC-SEM-2589 | P2 | Weight mapping glin-profanity = 45 | detector=glin-profanity,key=WEIGHT_DETECTOR_GLIN,value=45 | weight in range | test_semantic_phase2_part_5.py |
| TC-SEM-2590 | P2 | Weight mapping glin-profanity = 50 | detector=glin-profanity,key=WEIGHT_DETECTOR_GLIN,value=50 | weight in range | test_semantic_phase2_part_5.py |
| TC-SEM-2591 | P2 | Weight mapping bk_tree = 5 | detector=bk_tree,key=WEIGHT_DETECTOR_BKTREE,value=5 | weight in range | test_semantic_phase2_part_5.py |
| TC-SEM-2592 | P2 | Weight mapping bk_tree = 8 | detector=bk_tree,key=WEIGHT_DETECTOR_BKTREE,value=8 | weight in range | test_semantic_phase2_part_5.py |
| TC-SEM-2593 | P2 | Weight mapping bk_tree = 10 | detector=bk_tree,key=WEIGHT_DETECTOR_BKTREE,value=10 | weight in range | test_semantic_phase2_part_5.py |
| TC-SEM-2594 | P2 | Weight mapping bk_tree = 12 | detector=bk_tree,key=WEIGHT_DETECTOR_BKTREE,value=12 | weight in range | test_semantic_phase2_part_5.py |
| TC-SEM-2595 | P2 | Weight mapping bk_tree = 15 | detector=bk_tree,key=WEIGHT_DETECTOR_BKTREE,value=15 | weight in range | test_semantic_phase2_part_5.py |
| TC-SEM-2596 | P2 | Weight mapping bk_tree = 20 | detector=bk_tree,key=WEIGHT_DETECTOR_BKTREE,value=20 | weight in range | test_semantic_phase2_part_5.py |
| TC-SEM-2597 | P2 | Weight mapping bk_tree = 25 | detector=bk_tree,key=WEIGHT_DETECTOR_BKTREE,value=25 | weight in range | test_semantic_phase2_part_5.py |
| TC-SEM-2598 | P2 | Weight mapping bk_tree = 30 | detector=bk_tree,key=WEIGHT_DETECTOR_BKTREE,value=30 | weight in range | test_semantic_phase2_part_5.py |
| TC-SEM-2599 | P2 | Weight mapping bk_tree = 35 | detector=bk_tree,key=WEIGHT_DETECTOR_BKTREE,value=35 | weight in range | test_semantic_phase2_part_5.py |
| TC-SEM-2600 | P2 | Weight mapping bk_tree = 40 | detector=bk_tree,key=WEIGHT_DETECTOR_BKTREE,value=40 | weight in range | test_semantic_phase2_part_5.py |
| TC-SEM-2601 | P2 | Weight mapping bk_tree = 45 | detector=bk_tree,key=WEIGHT_DETECTOR_BKTREE,value=45 | weight in range | test_semantic_phase2_part_6.py |
| TC-SEM-2602 | P2 | Weight mapping bk_tree = 50 | detector=bk_tree,key=WEIGHT_DETECTOR_BKTREE,value=50 | weight in range | test_semantic_phase2_part_6.py |
| TC-SEM-2603 | P2 | Weight mapping double_metaphone = 5 | detector=double_metaphone,key=WEIGHT_DETECTOR_METAPHONE,value=5 | weight in range | test_semantic_phase2_part_6.py |
| TC-SEM-2604 | P2 | Weight mapping double_metaphone = 8 | detector=double_metaphone,key=WEIGHT_DETECTOR_METAPHONE,value=8 | weight in range | test_semantic_phase2_part_6.py |
| TC-SEM-2605 | P2 | Weight mapping double_metaphone = 10 | detector=double_metaphone,key=WEIGHT_DETECTOR_METAPHONE,value=10 | weight in range | test_semantic_phase2_part_6.py |
| TC-SEM-2606 | P2 | Weight mapping double_metaphone = 12 | detector=double_metaphone,key=WEIGHT_DETECTOR_METAPHONE,value=12 | weight in range | test_semantic_phase2_part_6.py |
| TC-SEM-2607 | P2 | Weight mapping double_metaphone = 15 | detector=double_metaphone,key=WEIGHT_DETECTOR_METAPHONE,value=15 | weight in range | test_semantic_phase2_part_6.py |
| TC-SEM-2608 | P2 | Weight mapping double_metaphone = 20 | detector=double_metaphone,key=WEIGHT_DETECTOR_METAPHONE,value=20 | weight in range | test_semantic_phase2_part_6.py |
| TC-SEM-2609 | P2 | Weight mapping double_metaphone = 25 | detector=double_metaphone,key=WEIGHT_DETECTOR_METAPHONE,value=25 | weight in range | test_semantic_phase2_part_6.py |
| TC-SEM-2610 | P2 | Weight mapping double_metaphone = 30 | detector=double_metaphone,key=WEIGHT_DETECTOR_METAPHONE,value=30 | weight in range | test_semantic_phase2_part_6.py |
| TC-SEM-2611 | P2 | Weight mapping double_metaphone = 35 | detector=double_metaphone,key=WEIGHT_DETECTOR_METAPHONE,value=35 | weight in range | test_semantic_phase2_part_6.py |
| TC-SEM-2612 | P2 | Weight mapping double_metaphone = 40 | detector=double_metaphone,key=WEIGHT_DETECTOR_METAPHONE,value=40 | weight in range | test_semantic_phase2_part_6.py |
| TC-SEM-2613 | P2 | Weight mapping double_metaphone = 45 | detector=double_metaphone,key=WEIGHT_DETECTOR_METAPHONE,value=45 | weight in range | test_semantic_phase2_part_6.py |
| TC-SEM-2614 | P2 | Weight mapping double_metaphone = 50 | detector=double_metaphone,key=WEIGHT_DETECTOR_METAPHONE,value=50 | weight in range | test_semantic_phase2_part_6.py |
| TC-SEM-2615 | P2 | Weight mapping multi_language = 5 | detector=multi_language,key=WEIGHT_DETECTOR_BADWORDS,value=5 | weight in range | test_semantic_phase2_part_6.py |
| TC-SEM-2616 | P2 | Weight mapping multi_language = 8 | detector=multi_language,key=WEIGHT_DETECTOR_BADWORDS,value=8 | weight in range | test_semantic_phase2_part_6.py |
| TC-SEM-2617 | P2 | Weight mapping multi_language = 10 | detector=multi_language,key=WEIGHT_DETECTOR_BADWORDS,value=10 | weight in range | test_semantic_phase2_part_6.py |
| TC-SEM-2618 | P2 | Weight mapping multi_language = 12 | detector=multi_language,key=WEIGHT_DETECTOR_BADWORDS,value=12 | weight in range | test_semantic_phase2_part_6.py |
| TC-SEM-2619 | P2 | Weight mapping multi_language = 15 | detector=multi_language,key=WEIGHT_DETECTOR_BADWORDS,value=15 | weight in range | test_semantic_phase2_part_6.py |
| TC-SEM-2620 | P2 | Weight mapping multi_language = 20 | detector=multi_language,key=WEIGHT_DETECTOR_BADWORDS,value=20 | weight in range | test_semantic_phase2_part_6.py |
| TC-SEM-2621 | P2 | Weight mapping multi_language = 25 | detector=multi_language,key=WEIGHT_DETECTOR_BADWORDS,value=25 | weight in range | test_semantic_phase2_part_6.py |
| TC-SEM-2622 | P2 | Weight mapping multi_language = 30 | detector=multi_language,key=WEIGHT_DETECTOR_BADWORDS,value=30 | weight in range | test_semantic_phase2_part_6.py |
| TC-SEM-2623 | P2 | Weight mapping multi_language = 35 | detector=multi_language,key=WEIGHT_DETECTOR_BADWORDS,value=35 | weight in range | test_semantic_phase2_part_6.py |
| TC-SEM-2624 | P2 | Weight mapping multi_language = 40 | detector=multi_language,key=WEIGHT_DETECTOR_BADWORDS,value=40 | weight in range | test_semantic_phase2_part_6.py |
| TC-SEM-2625 | P2 | Weight mapping multi_language = 45 | detector=multi_language,key=WEIGHT_DETECTOR_BADWORDS,value=45 | weight in range | test_semantic_phase2_part_6.py |
| TC-SEM-2626 | P2 | Weight mapping multi_language = 50 | detector=multi_language,key=WEIGHT_DETECTOR_BADWORDS,value=50 | weight in range | test_semantic_phase2_part_6.py |
| TC-SEM-2627 | P2 | Weight mapping rolling_hash = 5 | detector=rolling_hash,key=WEIGHT_DETECTOR_AHO,value=5 | weight in range | test_semantic_phase2_part_6.py |
| TC-SEM-2628 | P2 | Weight mapping rolling_hash = 8 | detector=rolling_hash,key=WEIGHT_DETECTOR_AHO,value=8 | weight in range | test_semantic_phase2_part_6.py |
| TC-SEM-2629 | P2 | Weight mapping rolling_hash = 10 | detector=rolling_hash,key=WEIGHT_DETECTOR_AHO,value=10 | weight in range | test_semantic_phase2_part_6.py |
| TC-SEM-2630 | P2 | Weight mapping rolling_hash = 12 | detector=rolling_hash,key=WEIGHT_DETECTOR_AHO,value=12 | weight in range | test_semantic_phase2_part_6.py |
| TC-SEM-2631 | P2 | Weight mapping rolling_hash = 15 | detector=rolling_hash,key=WEIGHT_DETECTOR_AHO,value=15 | weight in range | test_semantic_phase2_part_6.py |
| TC-SEM-2632 | P2 | Weight mapping rolling_hash = 20 | detector=rolling_hash,key=WEIGHT_DETECTOR_AHO,value=20 | weight in range | test_semantic_phase2_part_6.py |
| TC-SEM-2633 | P2 | Weight mapping rolling_hash = 25 | detector=rolling_hash,key=WEIGHT_DETECTOR_AHO,value=25 | weight in range | test_semantic_phase2_part_6.py |
| TC-SEM-2634 | P2 | Weight mapping rolling_hash = 30 | detector=rolling_hash,key=WEIGHT_DETECTOR_AHO,value=30 | weight in range | test_semantic_phase2_part_6.py |
| TC-SEM-2635 | P2 | Weight mapping rolling_hash = 35 | detector=rolling_hash,key=WEIGHT_DETECTOR_AHO,value=35 | weight in range | test_semantic_phase2_part_6.py |
| TC-SEM-2636 | P2 | Weight mapping rolling_hash = 40 | detector=rolling_hash,key=WEIGHT_DETECTOR_AHO,value=40 | weight in range | test_semantic_phase2_part_6.py |
| TC-SEM-2637 | P2 | Weight mapping rolling_hash = 45 | detector=rolling_hash,key=WEIGHT_DETECTOR_AHO,value=45 | weight in range | test_semantic_phase2_part_6.py |
| TC-SEM-2638 | P2 | Weight mapping rolling_hash = 50 | detector=rolling_hash,key=WEIGHT_DETECTOR_AHO,value=50 | weight in range | test_semantic_phase2_part_6.py |
| TC-SEM-2639 | P2 | Weight mapping bloom_filter = 5 | detector=bloom_filter,key=WEIGHT_DETECTOR_AHO,value=5 | weight in range | test_semantic_phase2_part_6.py |
| TC-SEM-2640 | P2 | Weight mapping bloom_filter = 8 | detector=bloom_filter,key=WEIGHT_DETECTOR_AHO,value=8 | weight in range | test_semantic_phase2_part_6.py |
| TC-SEM-2641 | P2 | Weight mapping bloom_filter = 10 | detector=bloom_filter,key=WEIGHT_DETECTOR_AHO,value=10 | weight in range | test_semantic_phase2_part_6.py |
| TC-SEM-2642 | P2 | Weight mapping bloom_filter = 12 | detector=bloom_filter,key=WEIGHT_DETECTOR_AHO,value=12 | weight in range | test_semantic_phase2_part_6.py |
| TC-SEM-2643 | P2 | Weight mapping bloom_filter = 15 | detector=bloom_filter,key=WEIGHT_DETECTOR_AHO,value=15 | weight in range | test_semantic_phase2_part_6.py |
| TC-SEM-2644 | P2 | Weight mapping bloom_filter = 20 | detector=bloom_filter,key=WEIGHT_DETECTOR_AHO,value=20 | weight in range | test_semantic_phase2_part_6.py |
| TC-SEM-2645 | P2 | Weight mapping bloom_filter = 25 | detector=bloom_filter,key=WEIGHT_DETECTOR_AHO,value=25 | weight in range | test_semantic_phase2_part_6.py |
| TC-SEM-2646 | P2 | Weight mapping bloom_filter = 30 | detector=bloom_filter,key=WEIGHT_DETECTOR_AHO,value=30 | weight in range | test_semantic_phase2_part_6.py |
| TC-SEM-2647 | P2 | Weight mapping bloom_filter = 35 | detector=bloom_filter,key=WEIGHT_DETECTOR_AHO,value=35 | weight in range | test_semantic_phase2_part_6.py |
| TC-SEM-2648 | P2 | Weight mapping bloom_filter = 40 | detector=bloom_filter,key=WEIGHT_DETECTOR_AHO,value=40 | weight in range | test_semantic_phase2_part_6.py |
| TC-SEM-2649 | P2 | Weight mapping bloom_filter = 45 | detector=bloom_filter,key=WEIGHT_DETECTOR_AHO,value=45 | weight in range | test_semantic_phase2_part_6.py |
| TC-SEM-2650 | P2 | Weight mapping bloom_filter = 50 | detector=bloom_filter,key=WEIGHT_DETECTOR_AHO,value=50 | weight in range | test_semantic_phase2_part_6.py |
| TC-SEM-2651 | P2 | Category weight political at 0.5 | category=political,similarity=0.5 | boosted | test_semantic_phase2_part_6.py |
| TC-SEM-2652 | P2 | Category weight political at 0.84 | category=political,similarity=0.84 | boosted | test_semantic_phase2_part_6.py |
| TC-SEM-2653 | P2 | Category weight political at 0.86 | category=political,similarity=0.86 | boosted | test_semantic_phase2_part_6.py |
| TC-SEM-2654 | P2 | Category weight political at 0.95 | category=political,similarity=0.95 | boosted | test_semantic_phase2_part_6.py |
| TC-SEM-2655 | P2 | Category weight violence at 0.5 | category=violence,similarity=0.5 | boosted | test_semantic_phase2_part_6.py |
| TC-SEM-2656 | P2 | Category weight violence at 0.84 | category=violence,similarity=0.84 | boosted | test_semantic_phase2_part_6.py |
| TC-SEM-2657 | P2 | Category weight violence at 0.86 | category=violence,similarity=0.86 | boosted | test_semantic_phase2_part_6.py |
| TC-SEM-2658 | P2 | Category weight violence at 0.95 | category=violence,similarity=0.95 | boosted | test_semantic_phase2_part_6.py |
| TC-SEM-2659 | P2 | Category weight sexual at 0.5 | category=sexual,similarity=0.5 | boosted | test_semantic_phase2_part_6.py |
| TC-SEM-2660 | P2 | Category weight sexual at 0.84 | category=sexual,similarity=0.84 | boosted | test_semantic_phase2_part_6.py |
| TC-SEM-2661 | P2 | Category weight sexual at 0.86 | category=sexual,similarity=0.86 | boosted | test_semantic_phase2_part_6.py |
| TC-SEM-2662 | P2 | Category weight sexual at 0.95 | category=sexual,similarity=0.95 | boosted | test_semantic_phase2_part_6.py |
| TC-SEM-2663 | P2 | Category weight hate at 0.5 | category=hate,similarity=0.5 | boosted | test_semantic_phase2_part_6.py |
| TC-SEM-2664 | P2 | Category weight hate at 0.84 | category=hate,similarity=0.84 | boosted | test_semantic_phase2_part_6.py |
| TC-SEM-2665 | P2 | Category weight hate at 0.86 | category=hate,similarity=0.86 | boosted | test_semantic_phase2_part_6.py |
| TC-SEM-2666 | P2 | Category weight hate at 0.95 | category=hate,similarity=0.95 | boosted | test_semantic_phase2_part_6.py |
| TC-SEM-2667 | P2 | Category weight pii at 0.5 | category=pii,similarity=0.5 | boosted | test_semantic_phase2_part_6.py |
| TC-SEM-2668 | P2 | Category weight pii at 0.84 | category=pii,similarity=0.84 | boosted | test_semantic_phase2_part_6.py |
| TC-SEM-2669 | P2 | Category weight pii at 0.86 | category=pii,similarity=0.86 | boosted | test_semantic_phase2_part_6.py |
| TC-SEM-2670 | P2 | Category weight pii at 0.95 | category=pii,similarity=0.95 | boosted | test_semantic_phase2_part_6.py |
| TC-SEM-2671 | P2 | Category weight ads at 0.5 | category=ads,similarity=0.5 | boosted | test_semantic_phase2_part_6.py |
| TC-SEM-2672 | P2 | Category weight ads at 0.84 | category=ads,similarity=0.84 | boosted | test_semantic_phase2_part_6.py |
| TC-SEM-2673 | P2 | Category weight ads at 0.86 | category=ads,similarity=0.86 | boosted | test_semantic_phase2_part_6.py |
| TC-SEM-2674 | P2 | Category weight ads at 0.95 | category=ads,similarity=0.95 | boosted | test_semantic_phase2_part_6.py |
| TC-SEM-2675 | P2 | Category weight other at 0.5 | category=other,similarity=0.5 | boosted | test_semantic_phase2_part_6.py |
| TC-SEM-2676 | P2 | Category weight other at 0.84 | category=other,similarity=0.84 | boosted | test_semantic_phase2_part_6.py |
| TC-SEM-2677 | P2 | Category weight other at 0.86 | category=other,similarity=0.86 | boosted | test_semantic_phase2_part_6.py |
| TC-SEM-2678 | P2 | Category weight other at 0.95 | category=other,similarity=0.95 | boosted | test_semantic_phase2_part_6.py |
| TC-SEM-2679 | P2 | Availability enabled=True top_k=1 | scenario=0,enabled=True,top_k=1 | consistent | test_semantic_phase2_part_6.py |
| TC-SEM-2680 | P2 | Availability enabled=False top_k=1 | scenario=1,enabled=False,top_k=1 | consistent | test_semantic_phase2_part_6.py |
| TC-SEM-2681 | P2 | Availability enabled=True top_k=2 | scenario=2,enabled=True,top_k=2 | consistent | test_semantic_phase2_part_6.py |
| TC-SEM-2682 | P2 | Availability enabled=False top_k=2 | scenario=3,enabled=False,top_k=2 | consistent | test_semantic_phase2_part_6.py |
| TC-SEM-2683 | P2 | Availability enabled=True top_k=3 | scenario=4,enabled=True,top_k=3 | consistent | test_semantic_phase2_part_6.py |
| TC-SEM-2684 | P2 | Availability enabled=False top_k=3 | scenario=5,enabled=False,top_k=3 | consistent | test_semantic_phase2_part_6.py |
| TC-SEM-2685 | P2 | Availability enabled=True top_k=4 | scenario=6,enabled=True,top_k=4 | consistent | test_semantic_phase2_part_6.py |
| TC-SEM-2686 | P2 | Availability enabled=False top_k=4 | scenario=7,enabled=False,top_k=4 | consistent | test_semantic_phase2_part_6.py |
| TC-SEM-2687 | P2 | Availability enabled=True top_k=5 | scenario=8,enabled=True,top_k=5 | consistent | test_semantic_phase2_part_6.py |
| TC-SEM-2688 | P2 | Availability enabled=False top_k=5 | scenario=9,enabled=False,top_k=5 | consistent | test_semantic_phase2_part_6.py |
| TC-SEM-2689 | P2 | Availability enabled=True top_k=6 | scenario=10,enabled=True,top_k=6 | consistent | test_semantic_phase2_part_6.py |
| TC-SEM-2690 | P2 | Availability enabled=False top_k=6 | scenario=11,enabled=False,top_k=6 | consistent | test_semantic_phase2_part_6.py |
| TC-SEM-2691 | P2 | Availability enabled=True top_k=7 | scenario=12,enabled=True,top_k=7 | consistent | test_semantic_phase2_part_6.py |
| TC-SEM-2692 | P2 | Availability enabled=False top_k=7 | scenario=13,enabled=False,top_k=7 | consistent | test_semantic_phase2_part_6.py |
| TC-SEM-2693 | P2 | Availability enabled=True top_k=8 | scenario=14,enabled=True,top_k=8 | consistent | test_semantic_phase2_part_6.py |
| TC-SEM-2694 | P2 | Availability enabled=False top_k=8 | scenario=15,enabled=False,top_k=8 | consistent | test_semantic_phase2_part_6.py |
| TC-SEM-2695 | P2 | Availability enabled=True top_k=9 | scenario=16,enabled=True,top_k=9 | consistent | test_semantic_phase2_part_6.py |
| TC-SEM-2696 | P2 | Availability enabled=False top_k=9 | scenario=17,enabled=False,top_k=9 | consistent | test_semantic_phase2_part_6.py |
| TC-SEM-2697 | P2 | Availability enabled=True top_k=10 | scenario=18,enabled=True,top_k=10 | consistent | test_semantic_phase2_part_6.py |
| TC-SEM-2698 | P2 | Availability enabled=False top_k=10 | scenario=19,enabled=False,top_k=10 | consistent | test_semantic_phase2_part_6.py |
| TC-SEM-2699 | P2 | Availability enabled=True top_k=11 | scenario=20,enabled=True,top_k=11 | consistent | test_semantic_phase2_part_6.py |
| TC-SEM-2700 | P2 | Availability enabled=False top_k=11 | scenario=21,enabled=False,top_k=11 | consistent | test_semantic_phase2_part_6.py |
| TC-SEM-2701 | P2 | Availability enabled=True top_k=12 | scenario=22,enabled=True,top_k=12 | consistent | test_semantic_phase2_part_7.py |
| TC-SEM-2702 | P2 | Availability enabled=False top_k=12 | scenario=23,enabled=False,top_k=12 | consistent | test_semantic_phase2_part_7.py |
| TC-SEM-2703 | P2 | Availability enabled=True top_k=13 | scenario=24,enabled=True,top_k=13 | consistent | test_semantic_phase2_part_7.py |
| TC-SEM-2704 | P2 | Availability enabled=False top_k=13 | scenario=25,enabled=False,top_k=13 | consistent | test_semantic_phase2_part_7.py |
| TC-SEM-2705 | P2 | Availability enabled=True top_k=14 | scenario=26,enabled=True,top_k=14 | consistent | test_semantic_phase2_part_7.py |
| TC-SEM-2706 | P2 | Availability enabled=False top_k=14 | scenario=27,enabled=False,top_k=14 | consistent | test_semantic_phase2_part_7.py |
| TC-SEM-2707 | P2 | Availability enabled=True top_k=15 | scenario=28,enabled=True,top_k=15 | consistent | test_semantic_phase2_part_7.py |
| TC-SEM-2708 | P2 | Availability enabled=False top_k=15 | scenario=29,enabled=False,top_k=15 | consistent | test_semantic_phase2_part_7.py |
| TC-SEM-2709 | P2 | Availability enabled=True top_k=16 | scenario=30,enabled=True,top_k=16 | consistent | test_semantic_phase2_part_7.py |
| TC-SEM-2710 | P2 | Availability enabled=False top_k=16 | scenario=31,enabled=False,top_k=16 | consistent | test_semantic_phase2_part_7.py |
| TC-SEM-2711 | P2 | Availability enabled=True top_k=17 | scenario=32,enabled=True,top_k=17 | consistent | test_semantic_phase2_part_7.py |
| TC-SEM-2712 | P2 | Availability enabled=False top_k=17 | scenario=33,enabled=False,top_k=17 | consistent | test_semantic_phase2_part_7.py |
| TC-SEM-2713 | P2 | Availability enabled=True top_k=18 | scenario=34,enabled=True,top_k=18 | consistent | test_semantic_phase2_part_7.py |
| TC-SEM-2714 | P2 | Availability enabled=False top_k=18 | scenario=35,enabled=False,top_k=18 | consistent | test_semantic_phase2_part_7.py |
| TC-SEM-2715 | P2 | Availability enabled=True top_k=19 | scenario=36,enabled=True,top_k=19 | consistent | test_semantic_phase2_part_7.py |
| TC-SEM-2716 | P2 | Availability enabled=False top_k=19 | scenario=37,enabled=False,top_k=19 | consistent | test_semantic_phase2_part_7.py |
| TC-SEM-2717 | P2 | Availability enabled=True top_k=20 | scenario=38,enabled=True,top_k=20 | consistent | test_semantic_phase2_part_7.py |
| TC-SEM-2718 | P2 | Availability enabled=False top_k=20 | scenario=39,enabled=False,top_k=20 | consistent | test_semantic_phase2_part_7.py |
| TC-SEM-2719 | P2 | Availability enabled=True top_k=21 | scenario=40,enabled=True,top_k=21 | consistent | test_semantic_phase2_part_7.py |
| TC-SEM-2720 | P2 | Availability enabled=False top_k=21 | scenario=41,enabled=False,top_k=21 | consistent | test_semantic_phase2_part_7.py |
| TC-SEM-2721 | P2 | Availability enabled=True top_k=22 | scenario=42,enabled=True,top_k=22 | consistent | test_semantic_phase2_part_7.py |
| TC-SEM-2722 | P2 | Availability enabled=False top_k=22 | scenario=43,enabled=False,top_k=22 | consistent | test_semantic_phase2_part_7.py |
| TC-SEM-2723 | P2 | Availability enabled=True top_k=23 | scenario=44,enabled=True,top_k=23 | consistent | test_semantic_phase2_part_7.py |
| TC-SEM-2724 | P2 | Availability enabled=False top_k=23 | scenario=45,enabled=False,top_k=23 | consistent | test_semantic_phase2_part_7.py |
| TC-SEM-2725 | P2 | Availability enabled=True top_k=24 | scenario=46,enabled=True,top_k=24 | consistent | test_semantic_phase2_part_7.py |
| TC-SEM-2726 | P2 | Availability enabled=False top_k=24 | scenario=47,enabled=False,top_k=24 | consistent | test_semantic_phase2_part_7.py |
| TC-SEM-2727 | P2 | Availability enabled=True top_k=25 | scenario=48,enabled=True,top_k=25 | consistent | test_semantic_phase2_part_7.py |
| TC-SEM-2728 | P2 | Availability enabled=False top_k=25 | scenario=49,enabled=False,top_k=25 | consistent | test_semantic_phase2_part_7.py |
| TC-SEM-2729 | P2 | Availability enabled=True top_k=26 | scenario=50,enabled=True,top_k=26 | consistent | test_semantic_phase2_part_7.py |
| TC-SEM-2730 | P2 | Availability enabled=False top_k=26 | scenario=51,enabled=False,top_k=26 | consistent | test_semantic_phase2_part_7.py |
| TC-SEM-2731 | P2 | Availability enabled=True top_k=27 | scenario=52,enabled=True,top_k=27 | consistent | test_semantic_phase2_part_7.py |
| TC-SEM-2732 | P2 | Availability enabled=False top_k=27 | scenario=53,enabled=False,top_k=27 | consistent | test_semantic_phase2_part_7.py |
| TC-SEM-2733 | P2 | Availability enabled=True top_k=28 | scenario=54,enabled=True,top_k=28 | consistent | test_semantic_phase2_part_7.py |
| TC-SEM-2734 | P2 | Availability enabled=False top_k=28 | scenario=55,enabled=False,top_k=28 | consistent | test_semantic_phase2_part_7.py |
| TC-SEM-2735 | P2 | Availability enabled=True top_k=29 | scenario=56,enabled=True,top_k=29 | consistent | test_semantic_phase2_part_7.py |
| TC-SEM-2736 | P2 | Availability enabled=False top_k=29 | scenario=57,enabled=False,top_k=29 | consistent | test_semantic_phase2_part_7.py |
| TC-SEM-2737 | P2 | Availability enabled=True top_k=30 | scenario=58,enabled=True,top_k=30 | consistent | test_semantic_phase2_part_7.py |
| TC-SEM-2738 | P2 | Availability enabled=False top_k=30 | scenario=59,enabled=False,top_k=30 | consistent | test_semantic_phase2_part_7.py |
| TC-SEM-2739 | P2 | Availability enabled=True top_k=31 | scenario=60,enabled=True,top_k=31 | consistent | test_semantic_phase2_part_7.py |
| TC-SEM-2740 | P2 | Availability enabled=False top_k=31 | scenario=61,enabled=False,top_k=31 | consistent | test_semantic_phase2_part_7.py |
| TC-SEM-2741 | P2 | Availability enabled=True top_k=32 | scenario=62,enabled=True,top_k=32 | consistent | test_semantic_phase2_part_7.py |
| TC-SEM-2742 | P2 | Availability enabled=False top_k=32 | scenario=63,enabled=False,top_k=32 | consistent | test_semantic_phase2_part_7.py |
| TC-SEM-2743 | P2 | Availability enabled=True top_k=33 | scenario=64,enabled=True,top_k=33 | consistent | test_semantic_phase2_part_7.py |
| TC-SEM-2744 | P2 | Availability enabled=False top_k=33 | scenario=65,enabled=False,top_k=33 | consistent | test_semantic_phase2_part_7.py |
| TC-SEM-2745 | P2 | Availability enabled=True top_k=34 | scenario=66,enabled=True,top_k=34 | consistent | test_semantic_phase2_part_7.py |
| TC-SEM-2746 | P2 | Availability enabled=False top_k=34 | scenario=67,enabled=False,top_k=34 | consistent | test_semantic_phase2_part_7.py |
| TC-SEM-2747 | P2 | Availability enabled=True top_k=35 | scenario=68,enabled=True,top_k=35 | consistent | test_semantic_phase2_part_7.py |
| TC-SEM-2748 | P2 | Availability enabled=False top_k=35 | scenario=69,enabled=False,top_k=35 | consistent | test_semantic_phase2_part_7.py |
| TC-SEM-2749 | P2 | Availability enabled=True top_k=36 | scenario=70,enabled=True,top_k=36 | consistent | test_semantic_phase2_part_7.py |
| TC-SEM-2750 | P2 | Availability enabled=False top_k=36 | scenario=71,enabled=False,top_k=36 | consistent | test_semantic_phase2_part_7.py |
| TC-SEM-2751 | P2 | Availability enabled=True top_k=37 | scenario=72,enabled=True,top_k=37 | consistent | test_semantic_phase2_part_7.py |
| TC-SEM-2752 | P2 | Availability enabled=False top_k=37 | scenario=73,enabled=False,top_k=37 | consistent | test_semantic_phase2_part_7.py |
| TC-SEM-2753 | P2 | Availability enabled=True top_k=38 | scenario=74,enabled=True,top_k=38 | consistent | test_semantic_phase2_part_7.py |
| TC-SEM-2754 | P2 | Availability enabled=False top_k=38 | scenario=75,enabled=False,top_k=38 | consistent | test_semantic_phase2_part_7.py |
| TC-SEM-2755 | P2 | Availability enabled=True top_k=39 | scenario=76,enabled=True,top_k=39 | consistent | test_semantic_phase2_part_7.py |
| TC-SEM-2756 | P2 | Availability enabled=False top_k=39 | scenario=77,enabled=False,top_k=39 | consistent | test_semantic_phase2_part_7.py |
| TC-SEM-2757 | P2 | Availability enabled=True top_k=40 | scenario=78,enabled=True,top_k=40 | consistent | test_semantic_phase2_part_7.py |
| TC-SEM-2758 | P2 | Availability enabled=False top_k=40 | scenario=79,enabled=False,top_k=40 | consistent | test_semantic_phase2_part_7.py |
| TC-SEM-2759 | P2 | Availability enabled=True top_k=41 | scenario=80,enabled=True,top_k=41 | consistent | test_semantic_phase2_part_7.py |
| TC-SEM-2760 | P2 | Availability enabled=False top_k=41 | scenario=81,enabled=False,top_k=41 | consistent | test_semantic_phase2_part_7.py |
| TC-SEM-2761 | P2 | Availability enabled=True top_k=42 | scenario=82,enabled=True,top_k=42 | consistent | test_semantic_phase2_part_7.py |
| TC-SEM-2762 | P2 | Availability enabled=False top_k=42 | scenario=83,enabled=False,top_k=42 | consistent | test_semantic_phase2_part_7.py |
| TC-SEM-2763 | P2 | Availability enabled=True top_k=43 | scenario=84,enabled=True,top_k=43 | consistent | test_semantic_phase2_part_7.py |
| TC-SEM-2764 | P2 | Availability enabled=False top_k=43 | scenario=85,enabled=False,top_k=43 | consistent | test_semantic_phase2_part_7.py |
| TC-SEM-2765 | P2 | Availability enabled=True top_k=44 | scenario=86,enabled=True,top_k=44 | consistent | test_semantic_phase2_part_7.py |
| TC-SEM-2766 | P2 | Availability enabled=False top_k=44 | scenario=87,enabled=False,top_k=44 | consistent | test_semantic_phase2_part_7.py |
| TC-SEM-2767 | P2 | Availability enabled=True top_k=45 | scenario=88,enabled=True,top_k=45 | consistent | test_semantic_phase2_part_7.py |
| TC-SEM-2768 | P2 | Availability enabled=False top_k=45 | scenario=89,enabled=False,top_k=45 | consistent | test_semantic_phase2_part_7.py |
| TC-SEM-2769 | P2 | Availability enabled=True top_k=46 | scenario=90,enabled=True,top_k=46 | consistent | test_semantic_phase2_part_7.py |
| TC-SEM-2770 | P2 | Availability enabled=False top_k=46 | scenario=91,enabled=False,top_k=46 | consistent | test_semantic_phase2_part_7.py |
| TC-SEM-2771 | P2 | Availability enabled=True top_k=47 | scenario=92,enabled=True,top_k=47 | consistent | test_semantic_phase2_part_7.py |
| TC-SEM-2772 | P2 | Availability enabled=False top_k=47 | scenario=93,enabled=False,top_k=47 | consistent | test_semantic_phase2_part_7.py |
| TC-SEM-2773 | P2 | Availability enabled=True top_k=48 | scenario=94,enabled=True,top_k=48 | consistent | test_semantic_phase2_part_7.py |
| TC-SEM-2774 | P2 | Availability enabled=False top_k=48 | scenario=95,enabled=False,top_k=48 | consistent | test_semantic_phase2_part_7.py |
| TC-SEM-2775 | P2 | Availability enabled=True top_k=49 | scenario=96,enabled=True,top_k=49 | consistent | test_semantic_phase2_part_7.py |
| TC-SEM-2776 | P2 | Availability enabled=False top_k=49 | scenario=97,enabled=False,top_k=49 | consistent | test_semantic_phase2_part_7.py |
| TC-SEM-2777 | P2 | Availability enabled=True top_k=50 | scenario=98,enabled=True,top_k=50 | consistent | test_semantic_phase2_part_7.py |
| TC-SEM-2778 | P2 | Availability enabled=False top_k=50 | scenario=99,enabled=False,top_k=50 | consistent | test_semantic_phase2_part_7.py |
| TC-SEM-2779 | P2 | Availability enabled=True top_k=51 | scenario=100,enabled=True,top_k=51 | consistent | test_semantic_phase2_part_7.py |
| TC-SEM-2780 | P2 | Availability enabled=False top_k=51 | scenario=101,enabled=False,top_k=51 | consistent | test_semantic_phase2_part_7.py |
| TC-SEM-2781 | P2 | Availability enabled=True top_k=52 | scenario=102,enabled=True,top_k=52 | consistent | test_semantic_phase2_part_7.py |
| TC-SEM-2782 | P2 | Availability enabled=False top_k=52 | scenario=103,enabled=False,top_k=52 | consistent | test_semantic_phase2_part_7.py |
| TC-SEM-2783 | P2 | Availability enabled=True top_k=53 | scenario=104,enabled=True,top_k=53 | consistent | test_semantic_phase2_part_7.py |
| TC-SEM-2784 | P2 | Availability enabled=False top_k=53 | scenario=105,enabled=False,top_k=53 | consistent | test_semantic_phase2_part_7.py |
| TC-SEM-2785 | P2 | Availability enabled=True top_k=54 | scenario=106,enabled=True,top_k=54 | consistent | test_semantic_phase2_part_7.py |
| TC-SEM-2786 | P2 | Availability enabled=False top_k=54 | scenario=107,enabled=False,top_k=54 | consistent | test_semantic_phase2_part_7.py |
| TC-SEM-2787 | P2 | Availability enabled=True top_k=55 | scenario=108,enabled=True,top_k=55 | consistent | test_semantic_phase2_part_7.py |
| TC-SEM-2788 | P2 | Availability enabled=False top_k=55 | scenario=109,enabled=False,top_k=55 | consistent | test_semantic_phase2_part_7.py |
| TC-SEM-2789 | P2 | Availability enabled=True top_k=56 | scenario=110,enabled=True,top_k=56 | consistent | test_semantic_phase2_part_7.py |
| TC-SEM-2790 | P2 | Availability enabled=False top_k=56 | scenario=111,enabled=False,top_k=56 | consistent | test_semantic_phase2_part_7.py |
| TC-SEM-2791 | P2 | Availability enabled=True top_k=57 | scenario=112,enabled=True,top_k=57 | consistent | test_semantic_phase2_part_7.py |
| TC-SEM-2792 | P2 | Availability enabled=False top_k=57 | scenario=113,enabled=False,top_k=57 | consistent | test_semantic_phase2_part_7.py |
| TC-SEM-2793 | P2 | Availability enabled=True top_k=58 | scenario=114,enabled=True,top_k=58 | consistent | test_semantic_phase2_part_7.py |
| TC-SEM-2794 | P2 | Availability enabled=False top_k=58 | scenario=115,enabled=False,top_k=58 | consistent | test_semantic_phase2_part_7.py |
| TC-SEM-2795 | P2 | Availability enabled=True top_k=59 | scenario=116,enabled=True,top_k=59 | consistent | test_semantic_phase2_part_7.py |
| TC-SEM-2796 | P2 | Availability enabled=False top_k=59 | scenario=117,enabled=False,top_k=59 | consistent | test_semantic_phase2_part_7.py |
| TC-SEM-2797 | P2 | Availability enabled=True top_k=60 | scenario=118,enabled=True,top_k=60 | consistent | test_semantic_phase2_part_7.py |
| TC-SEM-2798 | P2 | Availability enabled=False top_k=60 | scenario=119,enabled=False,top_k=60 | consistent | test_semantic_phase2_part_7.py |
| TC-SEM-2799 | P2 | Availability enabled=True top_k=61 | scenario=120,enabled=True,top_k=61 | consistent | test_semantic_phase2_part_7.py |
| TC-SEM-2800 | P2 | Availability enabled=False top_k=61 | scenario=121,enabled=False,top_k=61 | consistent | test_semantic_phase2_part_7.py |

### Phase 3 - 15,000 cases
- Planned sweeps over the full dimension matrix, IDs TC-SEM-0781 onward.

### Phase 4 - 150,000 cases
- Planned high-scale scenarios, IDs TC-SEM-15781 onward.

### Phase 5 - 1,034,220 cases
- Planned exhaustive dimension sweep, IDs TC-SEM-165781 onward.

## Implementation Status
| File | Test Cases | Priority | Status |
| :--- | :--- | :--- | :--- |
| test_semantic_phase2_part_1.py | 2101-2200 | P2 | :white_check_mark: Phase 2 |
| test_semantic_phase2_part_2.py | 2201-2300 | P1 | :white_check_mark: Phase 2 |
| test_semantic_phase2_part_3.py | 2301-2400 | P1 | :white_check_mark: Phase 2 |
| test_semantic_phase2_part_4.py | 2401-2500 | P1 | :white_check_mark: Phase 2 |
| test_semantic_phase2_part_5.py | 2501-2600 | P2 | :white_check_mark: Phase 2 |
| test_semantic_phase2_part_6.py | 2601-2700 | P2 | :white_check_mark: Phase 2 |
| test_semantic_phase2_part_7.py | 2701-2800 | P2 | :white_check_mark: Phase 2 |

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
- Semantic Similarity
- Configuration
