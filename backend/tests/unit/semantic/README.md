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
| TC-SEM-2101 | P2 | Unavailable path scenario 0 | scenario=0 | unavailable | test_semantic_phase2_part_1.py |
| TC-SEM-2102 | P2 | Unavailable path scenario 1 | scenario=1 | unavailable | test_semantic_phase2_part_1.py |
| TC-SEM-2103 | P2 | Unavailable path scenario 2 | scenario=2 | unavailable | test_semantic_phase2_part_1.py |
| TC-SEM-2104 | P2 | Unavailable path scenario 3 | scenario=3 | unavailable | test_semantic_phase2_part_1.py |
| TC-SEM-2105 | P2 | Unavailable path scenario 4 | scenario=4 | unavailable | test_semantic_phase2_part_1.py |
| TC-SEM-2106 | P2 | Unavailable path scenario 5 | scenario=5 | unavailable | test_semantic_phase2_part_1.py |
| TC-SEM-2107 | P2 | Unavailable path scenario 6 | scenario=6 | unavailable | test_semantic_phase2_part_1.py |
| TC-SEM-2108 | P2 | Unavailable path scenario 7 | scenario=7 | unavailable | test_semantic_phase2_part_1.py |
| TC-SEM-2109 | P2 | Unavailable path scenario 8 | scenario=8 | unavailable | test_semantic_phase2_part_1.py |
| TC-SEM-2110 | P2 | Unavailable path scenario 9 | scenario=9 | unavailable | test_semantic_phase2_part_1.py |
| TC-SEM-2111 | P2 | Unavailable path scenario 10 | scenario=10 | unavailable | test_semantic_phase2_part_1.py |
| TC-SEM-2112 | P2 | Unavailable path scenario 11 | scenario=11 | unavailable | test_semantic_phase2_part_1.py |
| TC-SEM-2113 | P2 | Unavailable path scenario 12 | scenario=12 | unavailable | test_semantic_phase2_part_1.py |
| TC-SEM-2114 | P2 | Unavailable path scenario 13 | scenario=13 | unavailable | test_semantic_phase2_part_1.py |
| TC-SEM-2115 | P2 | Unavailable path scenario 14 | scenario=14 | unavailable | test_semantic_phase2_part_1.py |
| TC-SEM-2116 | P2 | Unavailable path scenario 15 | scenario=15 | unavailable | test_semantic_phase2_part_1.py |
| TC-SEM-2117 | P2 | Unavailable path scenario 16 | scenario=16 | unavailable | test_semantic_phase2_part_1.py |
| TC-SEM-2118 | P2 | Unavailable path scenario 17 | scenario=17 | unavailable | test_semantic_phase2_part_1.py |
| TC-SEM-2119 | P2 | Unavailable path scenario 18 | scenario=18 | unavailable | test_semantic_phase2_part_1.py |
| TC-SEM-2120 | P2 | Unavailable path scenario 19 | scenario=19 | unavailable | test_semantic_phase2_part_1.py |
| TC-SEM-2121 | P2 | Unavailable path scenario 20 | scenario=20 | unavailable | test_semantic_phase2_part_1.py |
| TC-SEM-2122 | P2 | Unavailable path scenario 21 | scenario=21 | unavailable | test_semantic_phase2_part_1.py |
| TC-SEM-2123 | P2 | Unavailable path scenario 22 | scenario=22 | unavailable | test_semantic_phase2_part_1.py |
| TC-SEM-2124 | P2 | Unavailable path scenario 23 | scenario=23 | unavailable | test_semantic_phase2_part_1.py |
| TC-SEM-2125 | P2 | Unavailable path scenario 24 | scenario=24 | unavailable | test_semantic_phase2_part_1.py |
| TC-SEM-2126 | P2 | Unavailable path scenario 25 | scenario=25 | unavailable | test_semantic_phase2_part_1.py |
| TC-SEM-2127 | P2 | Unavailable path scenario 26 | scenario=26 | unavailable | test_semantic_phase2_part_1.py |
| TC-SEM-2128 | P2 | Unavailable path scenario 27 | scenario=27 | unavailable | test_semantic_phase2_part_1.py |
| TC-SEM-2129 | P2 | Unavailable path scenario 28 | scenario=28 | unavailable | test_semantic_phase2_part_1.py |
| TC-SEM-2130 | P2 | Unavailable path scenario 29 | scenario=29 | unavailable | test_semantic_phase2_part_1.py |
| TC-SEM-2131 | P2 | Unavailable path scenario 30 | scenario=30 | unavailable | test_semantic_phase2_part_1.py |
| TC-SEM-2132 | P2 | Unavailable path scenario 31 | scenario=31 | unavailable | test_semantic_phase2_part_1.py |
| TC-SEM-2133 | P2 | Unavailable path scenario 32 | scenario=32 | unavailable | test_semantic_phase2_part_1.py |
| TC-SEM-2134 | P2 | Unavailable path scenario 33 | scenario=33 | unavailable | test_semantic_phase2_part_1.py |
| TC-SEM-2135 | P2 | Unavailable path scenario 34 | scenario=34 | unavailable | test_semantic_phase2_part_1.py |
| TC-SEM-2136 | P2 | Unavailable path scenario 35 | scenario=35 | unavailable | test_semantic_phase2_part_1.py |
| TC-SEM-2137 | P2 | Unavailable path scenario 36 | scenario=36 | unavailable | test_semantic_phase2_part_1.py |
| TC-SEM-2138 | P2 | Unavailable path scenario 37 | scenario=37 | unavailable | test_semantic_phase2_part_1.py |
| TC-SEM-2139 | P2 | Unavailable path scenario 38 | scenario=38 | unavailable | test_semantic_phase2_part_1.py |
| TC-SEM-2140 | P2 | Unavailable path scenario 39 | scenario=39 | unavailable | test_semantic_phase2_part_1.py |
| TC-SEM-2141 | P2 | Unavailable path scenario 40 | scenario=40 | unavailable | test_semantic_phase2_part_1.py |
| TC-SEM-2142 | P2 | Unavailable path scenario 41 | scenario=41 | unavailable | test_semantic_phase2_part_1.py |
| TC-SEM-2143 | P2 | Unavailable path scenario 42 | scenario=42 | unavailable | test_semantic_phase2_part_1.py |
| TC-SEM-2144 | P2 | Unavailable path scenario 43 | scenario=43 | unavailable | test_semantic_phase2_part_1.py |
| TC-SEM-2145 | P2 | Unavailable path scenario 44 | scenario=44 | unavailable | test_semantic_phase2_part_1.py |
| TC-SEM-2146 | P2 | Unavailable path scenario 45 | scenario=45 | unavailable | test_semantic_phase2_part_1.py |
| TC-SEM-2147 | P2 | Unavailable path scenario 46 | scenario=46 | unavailable | test_semantic_phase2_part_1.py |
| TC-SEM-2148 | P2 | Unavailable path scenario 47 | scenario=47 | unavailable | test_semantic_phase2_part_1.py |
| TC-SEM-2149 | P2 | Unavailable path scenario 48 | scenario=48 | unavailable | test_semantic_phase2_part_1.py |
| TC-SEM-2150 | P2 | Unavailable path scenario 49 | scenario=49 | unavailable | test_semantic_phase2_part_1.py |
| TC-SEM-2151 | P2 | Unavailable path scenario 50 | scenario=50 | unavailable | test_semantic_phase2_part_1.py |
| TC-SEM-2152 | P2 | Unavailable path scenario 51 | scenario=51 | unavailable | test_semantic_phase2_part_1.py |
| TC-SEM-2153 | P2 | Unavailable path scenario 52 | scenario=52 | unavailable | test_semantic_phase2_part_1.py |
| TC-SEM-2154 | P2 | Unavailable path scenario 53 | scenario=53 | unavailable | test_semantic_phase2_part_1.py |
| TC-SEM-2155 | P2 | Unavailable path scenario 54 | scenario=54 | unavailable | test_semantic_phase2_part_1.py |
| TC-SEM-2156 | P2 | Unavailable path scenario 55 | scenario=55 | unavailable | test_semantic_phase2_part_1.py |
| TC-SEM-2157 | P2 | Unavailable path scenario 56 | scenario=56 | unavailable | test_semantic_phase2_part_1.py |
| TC-SEM-2158 | P2 | Unavailable path scenario 57 | scenario=57 | unavailable | test_semantic_phase2_part_1.py |
| TC-SEM-2159 | P2 | Unavailable path scenario 58 | scenario=58 | unavailable | test_semantic_phase2_part_1.py |
| TC-SEM-2160 | P2 | Unavailable path scenario 59 | scenario=59 | unavailable | test_semantic_phase2_part_1.py |
| TC-SEM-2161 | P2 | Unavailable path scenario 60 | scenario=60 | unavailable | test_semantic_phase2_part_1.py |
| TC-SEM-2162 | P2 | Unavailable path scenario 61 | scenario=61 | unavailable | test_semantic_phase2_part_1.py |
| TC-SEM-2163 | P2 | Unavailable path scenario 62 | scenario=62 | unavailable | test_semantic_phase2_part_1.py |
| TC-SEM-2164 | P2 | Unavailable path scenario 63 | scenario=63 | unavailable | test_semantic_phase2_part_1.py |
| TC-SEM-2165 | P2 | Unavailable path scenario 64 | scenario=64 | unavailable | test_semantic_phase2_part_1.py |
| TC-SEM-2166 | P2 | Unavailable path scenario 65 | scenario=65 | unavailable | test_semantic_phase2_part_1.py |
| TC-SEM-2167 | P2 | Unavailable path scenario 66 | scenario=66 | unavailable | test_semantic_phase2_part_1.py |
| TC-SEM-2168 | P2 | Unavailable path scenario 67 | scenario=67 | unavailable | test_semantic_phase2_part_1.py |
| TC-SEM-2169 | P2 | Unavailable path scenario 68 | scenario=68 | unavailable | test_semantic_phase2_part_1.py |
| TC-SEM-2170 | P2 | Unavailable path scenario 69 | scenario=69 | unavailable | test_semantic_phase2_part_1.py |
| TC-SEM-2171 | P2 | Unavailable path scenario 70 | scenario=70 | unavailable | test_semantic_phase2_part_1.py |
| TC-SEM-2172 | P2 | Unavailable path scenario 71 | scenario=71 | unavailable | test_semantic_phase2_part_1.py |
| TC-SEM-2173 | P2 | Unavailable path scenario 72 | scenario=72 | unavailable | test_semantic_phase2_part_1.py |
| TC-SEM-2174 | P2 | Unavailable path scenario 73 | scenario=73 | unavailable | test_semantic_phase2_part_1.py |
| TC-SEM-2175 | P2 | Unavailable path scenario 74 | scenario=74 | unavailable | test_semantic_phase2_part_1.py |
| TC-SEM-2176 | P2 | Unavailable path scenario 75 | scenario=75 | unavailable | test_semantic_phase2_part_1.py |
| TC-SEM-2177 | P2 | Unavailable path scenario 76 | scenario=76 | unavailable | test_semantic_phase2_part_1.py |
| TC-SEM-2178 | P2 | Unavailable path scenario 77 | scenario=77 | unavailable | test_semantic_phase2_part_1.py |
| TC-SEM-2179 | P2 | Unavailable path scenario 78 | scenario=78 | unavailable | test_semantic_phase2_part_1.py |
| TC-SEM-2180 | P2 | Unavailable path scenario 79 | scenario=79 | unavailable | test_semantic_phase2_part_1.py |
| TC-SEM-2181 | P2 | Unavailable path scenario 80 | scenario=80 | unavailable | test_semantic_phase2_part_1.py |
| TC-SEM-2182 | P2 | Unavailable path scenario 81 | scenario=81 | unavailable | test_semantic_phase2_part_1.py |
| TC-SEM-2183 | P2 | Unavailable path scenario 82 | scenario=82 | unavailable | test_semantic_phase2_part_1.py |
| TC-SEM-2184 | P2 | Unavailable path scenario 83 | scenario=83 | unavailable | test_semantic_phase2_part_1.py |
| TC-SEM-2185 | P2 | Unavailable path scenario 84 | scenario=84 | unavailable | test_semantic_phase2_part_1.py |
| TC-SEM-2186 | P2 | Unavailable path scenario 85 | scenario=85 | unavailable | test_semantic_phase2_part_1.py |
| TC-SEM-2187 | P2 | Unavailable path scenario 86 | scenario=86 | unavailable | test_semantic_phase2_part_1.py |
| TC-SEM-2188 | P2 | Unavailable path scenario 87 | scenario=87 | unavailable | test_semantic_phase2_part_1.py |
| TC-SEM-2189 | P2 | Unavailable path scenario 88 | scenario=88 | unavailable | test_semantic_phase2_part_1.py |
| TC-SEM-2190 | P2 | Unavailable path scenario 89 | scenario=89 | unavailable | test_semantic_phase2_part_1.py |
| TC-SEM-2191 | P2 | Unavailable path scenario 90 | scenario=90 | unavailable | test_semantic_phase2_part_1.py |
| TC-SEM-2192 | P2 | Unavailable path scenario 91 | scenario=91 | unavailable | test_semantic_phase2_part_1.py |
| TC-SEM-2193 | P2 | Unavailable path scenario 92 | scenario=92 | unavailable | test_semantic_phase2_part_1.py |
| TC-SEM-2194 | P2 | Unavailable path scenario 93 | scenario=93 | unavailable | test_semantic_phase2_part_1.py |
| TC-SEM-2195 | P2 | Unavailable path scenario 94 | scenario=94 | unavailable | test_semantic_phase2_part_1.py |
| TC-SEM-2196 | P2 | Unavailable path scenario 95 | scenario=95 | unavailable | test_semantic_phase2_part_1.py |
| TC-SEM-2197 | P2 | Unavailable path scenario 96 | scenario=96 | unavailable | test_semantic_phase2_part_1.py |
| TC-SEM-2198 | P2 | Unavailable path scenario 97 | scenario=97 | unavailable | test_semantic_phase2_part_1.py |
| TC-SEM-2199 | P2 | Unavailable path scenario 98 | scenario=98 | unavailable | test_semantic_phase2_part_1.py |
| TC-SEM-2200 | P2 | Unavailable path scenario 99 | scenario=99 | unavailable | test_semantic_phase2_part_1.py |
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
| TC-SEM-2514 | P2 | Stats field for political (verify) | category=political,query=verify | stats valid | test_semantic_phase2_part_5.py |
| TC-SEM-2515 | P2 | Stats field for political (sample) | category=political,query=sample | stats valid | test_semantic_phase2_part_5.py |
| TC-SEM-2516 | P2 | Stats field for political (count) | category=political,query=count | stats valid | test_semantic_phase2_part_5.py |
| TC-SEM-2517 | P2 | Stats field for political (shape) | category=political,query=shape | stats valid | test_semantic_phase2_part_5.py |
| TC-SEM-2518 | P2 | Stats field for violence (verify) | category=violence,query=verify | stats valid | test_semantic_phase2_part_5.py |
| TC-SEM-2519 | P2 | Stats field for violence (sample) | category=violence,query=sample | stats valid | test_semantic_phase2_part_5.py |
| TC-SEM-2520 | P2 | Stats field for violence (count) | category=violence,query=count | stats valid | test_semantic_phase2_part_5.py |
| TC-SEM-2521 | P2 | Stats field for violence (shape) | category=violence,query=shape | stats valid | test_semantic_phase2_part_5.py |
| TC-SEM-2522 | P2 | Stats field for sexual (verify) | category=sexual,query=verify | stats valid | test_semantic_phase2_part_5.py |
| TC-SEM-2523 | P2 | Stats field for sexual (sample) | category=sexual,query=sample | stats valid | test_semantic_phase2_part_5.py |
| TC-SEM-2524 | P2 | Stats field for sexual (count) | category=sexual,query=count | stats valid | test_semantic_phase2_part_5.py |
| TC-SEM-2525 | P2 | Stats field for sexual (shape) | category=sexual,query=shape | stats valid | test_semantic_phase2_part_5.py |
| TC-SEM-2526 | P2 | Stats field for hate (verify) | category=hate,query=verify | stats valid | test_semantic_phase2_part_5.py |
| TC-SEM-2527 | P2 | Stats field for hate (sample) | category=hate,query=sample | stats valid | test_semantic_phase2_part_5.py |
| TC-SEM-2528 | P2 | Stats field for hate (count) | category=hate,query=count | stats valid | test_semantic_phase2_part_5.py |
| TC-SEM-2529 | P2 | Stats field for hate (shape) | category=hate,query=shape | stats valid | test_semantic_phase2_part_5.py |
| TC-SEM-2530 | P2 | Stats field for pii (verify) | category=pii,query=verify | stats valid | test_semantic_phase2_part_5.py |
| TC-SEM-2531 | P2 | Stats field for pii (sample) | category=pii,query=sample | stats valid | test_semantic_phase2_part_5.py |
| TC-SEM-2532 | P2 | Stats field for pii (count) | category=pii,query=count | stats valid | test_semantic_phase2_part_5.py |
| TC-SEM-2533 | P2 | Stats field for pii (shape) | category=pii,query=shape | stats valid | test_semantic_phase2_part_5.py |
| TC-SEM-2534 | P2 | Stats field for ads (verify) | category=ads,query=verify | stats valid | test_semantic_phase2_part_5.py |
| TC-SEM-2535 | P2 | Stats field for ads (sample) | category=ads,query=sample | stats valid | test_semantic_phase2_part_5.py |
| TC-SEM-2536 | P2 | Stats field for ads (count) | category=ads,query=count | stats valid | test_semantic_phase2_part_5.py |
| TC-SEM-2537 | P2 | Stats field for ads (shape) | category=ads,query=shape | stats valid | test_semantic_phase2_part_5.py |
| TC-SEM-2538 | P2 | Stats field for other (verify) | category=other,query=verify | stats valid | test_semantic_phase2_part_5.py |
| TC-SEM-2539 | P2 | Stats field for other (sample) | category=other,query=sample | stats valid | test_semantic_phase2_part_5.py |
| TC-SEM-2540 | P2 | Stats field for other (count) | category=other,query=count | stats valid | test_semantic_phase2_part_5.py |
| TC-SEM-2541 | P2 | Stats field for other (shape) | category=other,query=shape | stats valid | test_semantic_phase2_part_5.py |
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
| TC-SEM-2555 | P2 | Weight mapping badwords #0 | detector=badwords,key=WEIGHT_DETECTOR_BADWORDS | weight in range | test_semantic_phase2_part_5.py |
| TC-SEM-2556 | P2 | Weight mapping badwords #1 | detector=badwords,key=WEIGHT_DETECTOR_BADWORDS | weight in range | test_semantic_phase2_part_5.py |
| TC-SEM-2557 | P2 | Weight mapping badwords #2 | detector=badwords,key=WEIGHT_DETECTOR_BADWORDS | weight in range | test_semantic_phase2_part_5.py |
| TC-SEM-2558 | P2 | Weight mapping badwords #3 | detector=badwords,key=WEIGHT_DETECTOR_BADWORDS | weight in range | test_semantic_phase2_part_5.py |
| TC-SEM-2559 | P2 | Weight mapping badwords #4 | detector=badwords,key=WEIGHT_DETECTOR_BADWORDS | weight in range | test_semantic_phase2_part_5.py |
| TC-SEM-2560 | P2 | Weight mapping badwords #5 | detector=badwords,key=WEIGHT_DETECTOR_BADWORDS | weight in range | test_semantic_phase2_part_5.py |
| TC-SEM-2561 | P2 | Weight mapping badwords #6 | detector=badwords,key=WEIGHT_DETECTOR_BADWORDS | weight in range | test_semantic_phase2_part_5.py |
| TC-SEM-2562 | P2 | Weight mapping badwords #7 | detector=badwords,key=WEIGHT_DETECTOR_BADWORDS | weight in range | test_semantic_phase2_part_5.py |
| TC-SEM-2563 | P2 | Weight mapping badwords #8 | detector=badwords,key=WEIGHT_DETECTOR_BADWORDS | weight in range | test_semantic_phase2_part_5.py |
| TC-SEM-2564 | P2 | Weight mapping badwords #9 | detector=badwords,key=WEIGHT_DETECTOR_BADWORDS | weight in range | test_semantic_phase2_part_5.py |
| TC-SEM-2565 | P2 | Weight mapping badwords #10 | detector=badwords,key=WEIGHT_DETECTOR_BADWORDS | weight in range | test_semantic_phase2_part_5.py |
| TC-SEM-2566 | P2 | Weight mapping badwords #11 | detector=badwords,key=WEIGHT_DETECTOR_BADWORDS | weight in range | test_semantic_phase2_part_5.py |
| TC-SEM-2567 | P2 | Weight mapping profanite #0 | detector=profanite,key=WEIGHT_DETECTOR_PROFANITE | weight in range | test_semantic_phase2_part_5.py |
| TC-SEM-2568 | P2 | Weight mapping profanite #1 | detector=profanite,key=WEIGHT_DETECTOR_PROFANITE | weight in range | test_semantic_phase2_part_5.py |
| TC-SEM-2569 | P2 | Weight mapping profanite #2 | detector=profanite,key=WEIGHT_DETECTOR_PROFANITE | weight in range | test_semantic_phase2_part_5.py |
| TC-SEM-2570 | P2 | Weight mapping profanite #3 | detector=profanite,key=WEIGHT_DETECTOR_PROFANITE | weight in range | test_semantic_phase2_part_5.py |
| TC-SEM-2571 | P2 | Weight mapping profanite #4 | detector=profanite,key=WEIGHT_DETECTOR_PROFANITE | weight in range | test_semantic_phase2_part_5.py |
| TC-SEM-2572 | P2 | Weight mapping profanite #5 | detector=profanite,key=WEIGHT_DETECTOR_PROFANITE | weight in range | test_semantic_phase2_part_5.py |
| TC-SEM-2573 | P2 | Weight mapping profanite #6 | detector=profanite,key=WEIGHT_DETECTOR_PROFANITE | weight in range | test_semantic_phase2_part_5.py |
| TC-SEM-2574 | P2 | Weight mapping profanite #7 | detector=profanite,key=WEIGHT_DETECTOR_PROFANITE | weight in range | test_semantic_phase2_part_5.py |
| TC-SEM-2575 | P2 | Weight mapping profanite #8 | detector=profanite,key=WEIGHT_DETECTOR_PROFANITE | weight in range | test_semantic_phase2_part_5.py |
| TC-SEM-2576 | P2 | Weight mapping profanite #9 | detector=profanite,key=WEIGHT_DETECTOR_PROFANITE | weight in range | test_semantic_phase2_part_5.py |
| TC-SEM-2577 | P2 | Weight mapping profanite #10 | detector=profanite,key=WEIGHT_DETECTOR_PROFANITE | weight in range | test_semantic_phase2_part_5.py |
| TC-SEM-2578 | P2 | Weight mapping profanite #11 | detector=profanite,key=WEIGHT_DETECTOR_PROFANITE | weight in range | test_semantic_phase2_part_5.py |
| TC-SEM-2579 | P2 | Weight mapping glin-profanity #0 | detector=glin-profanity,key=WEIGHT_DETECTOR_GLIN | weight in range | test_semantic_phase2_part_5.py |
| TC-SEM-2580 | P2 | Weight mapping glin-profanity #1 | detector=glin-profanity,key=WEIGHT_DETECTOR_GLIN | weight in range | test_semantic_phase2_part_5.py |
| TC-SEM-2581 | P2 | Weight mapping glin-profanity #2 | detector=glin-profanity,key=WEIGHT_DETECTOR_GLIN | weight in range | test_semantic_phase2_part_5.py |
| TC-SEM-2582 | P2 | Weight mapping glin-profanity #3 | detector=glin-profanity,key=WEIGHT_DETECTOR_GLIN | weight in range | test_semantic_phase2_part_5.py |
| TC-SEM-2583 | P2 | Weight mapping glin-profanity #4 | detector=glin-profanity,key=WEIGHT_DETECTOR_GLIN | weight in range | test_semantic_phase2_part_5.py |
| TC-SEM-2584 | P2 | Weight mapping glin-profanity #5 | detector=glin-profanity,key=WEIGHT_DETECTOR_GLIN | weight in range | test_semantic_phase2_part_5.py |
| TC-SEM-2585 | P2 | Weight mapping glin-profanity #6 | detector=glin-profanity,key=WEIGHT_DETECTOR_GLIN | weight in range | test_semantic_phase2_part_5.py |
| TC-SEM-2586 | P2 | Weight mapping glin-profanity #7 | detector=glin-profanity,key=WEIGHT_DETECTOR_GLIN | weight in range | test_semantic_phase2_part_5.py |
| TC-SEM-2587 | P2 | Weight mapping glin-profanity #8 | detector=glin-profanity,key=WEIGHT_DETECTOR_GLIN | weight in range | test_semantic_phase2_part_5.py |
| TC-SEM-2588 | P2 | Weight mapping glin-profanity #9 | detector=glin-profanity,key=WEIGHT_DETECTOR_GLIN | weight in range | test_semantic_phase2_part_5.py |
| TC-SEM-2589 | P2 | Weight mapping glin-profanity #10 | detector=glin-profanity,key=WEIGHT_DETECTOR_GLIN | weight in range | test_semantic_phase2_part_5.py |
| TC-SEM-2590 | P2 | Weight mapping glin-profanity #11 | detector=glin-profanity,key=WEIGHT_DETECTOR_GLIN | weight in range | test_semantic_phase2_part_5.py |
| TC-SEM-2591 | P2 | Weight mapping bk_tree #0 | detector=bk_tree,key=WEIGHT_DETECTOR_BKTREE | weight in range | test_semantic_phase2_part_5.py |
| TC-SEM-2592 | P2 | Weight mapping bk_tree #1 | detector=bk_tree,key=WEIGHT_DETECTOR_BKTREE | weight in range | test_semantic_phase2_part_5.py |
| TC-SEM-2593 | P2 | Weight mapping bk_tree #2 | detector=bk_tree,key=WEIGHT_DETECTOR_BKTREE | weight in range | test_semantic_phase2_part_5.py |
| TC-SEM-2594 | P2 | Weight mapping bk_tree #3 | detector=bk_tree,key=WEIGHT_DETECTOR_BKTREE | weight in range | test_semantic_phase2_part_5.py |
| TC-SEM-2595 | P2 | Weight mapping bk_tree #4 | detector=bk_tree,key=WEIGHT_DETECTOR_BKTREE | weight in range | test_semantic_phase2_part_5.py |
| TC-SEM-2596 | P2 | Weight mapping bk_tree #5 | detector=bk_tree,key=WEIGHT_DETECTOR_BKTREE | weight in range | test_semantic_phase2_part_5.py |
| TC-SEM-2597 | P2 | Weight mapping bk_tree #6 | detector=bk_tree,key=WEIGHT_DETECTOR_BKTREE | weight in range | test_semantic_phase2_part_5.py |
| TC-SEM-2598 | P2 | Weight mapping bk_tree #7 | detector=bk_tree,key=WEIGHT_DETECTOR_BKTREE | weight in range | test_semantic_phase2_part_5.py |
| TC-SEM-2599 | P2 | Weight mapping bk_tree #8 | detector=bk_tree,key=WEIGHT_DETECTOR_BKTREE | weight in range | test_semantic_phase2_part_5.py |
| TC-SEM-2600 | P2 | Weight mapping bk_tree #9 | detector=bk_tree,key=WEIGHT_DETECTOR_BKTREE | weight in range | test_semantic_phase2_part_5.py |
| TC-SEM-2601 | P2 | Weight mapping bk_tree #10 | detector=bk_tree,key=WEIGHT_DETECTOR_BKTREE | weight in range | test_semantic_phase2_part_6.py |
| TC-SEM-2602 | P2 | Weight mapping bk_tree #11 | detector=bk_tree,key=WEIGHT_DETECTOR_BKTREE | weight in range | test_semantic_phase2_part_6.py |
| TC-SEM-2603 | P2 | Weight mapping double_metaphone #0 | detector=double_metaphone,key=WEIGHT_DETECTOR_METAPHONE | weight in range | test_semantic_phase2_part_6.py |
| TC-SEM-2604 | P2 | Weight mapping double_metaphone #1 | detector=double_metaphone,key=WEIGHT_DETECTOR_METAPHONE | weight in range | test_semantic_phase2_part_6.py |
| TC-SEM-2605 | P2 | Weight mapping double_metaphone #2 | detector=double_metaphone,key=WEIGHT_DETECTOR_METAPHONE | weight in range | test_semantic_phase2_part_6.py |
| TC-SEM-2606 | P2 | Weight mapping double_metaphone #3 | detector=double_metaphone,key=WEIGHT_DETECTOR_METAPHONE | weight in range | test_semantic_phase2_part_6.py |
| TC-SEM-2607 | P2 | Weight mapping double_metaphone #4 | detector=double_metaphone,key=WEIGHT_DETECTOR_METAPHONE | weight in range | test_semantic_phase2_part_6.py |
| TC-SEM-2608 | P2 | Weight mapping double_metaphone #5 | detector=double_metaphone,key=WEIGHT_DETECTOR_METAPHONE | weight in range | test_semantic_phase2_part_6.py |
| TC-SEM-2609 | P2 | Weight mapping double_metaphone #6 | detector=double_metaphone,key=WEIGHT_DETECTOR_METAPHONE | weight in range | test_semantic_phase2_part_6.py |
| TC-SEM-2610 | P2 | Weight mapping double_metaphone #7 | detector=double_metaphone,key=WEIGHT_DETECTOR_METAPHONE | weight in range | test_semantic_phase2_part_6.py |
| TC-SEM-2611 | P2 | Weight mapping double_metaphone #8 | detector=double_metaphone,key=WEIGHT_DETECTOR_METAPHONE | weight in range | test_semantic_phase2_part_6.py |
| TC-SEM-2612 | P2 | Weight mapping double_metaphone #9 | detector=double_metaphone,key=WEIGHT_DETECTOR_METAPHONE | weight in range | test_semantic_phase2_part_6.py |
| TC-SEM-2613 | P2 | Weight mapping double_metaphone #10 | detector=double_metaphone,key=WEIGHT_DETECTOR_METAPHONE | weight in range | test_semantic_phase2_part_6.py |
| TC-SEM-2614 | P2 | Weight mapping double_metaphone #11 | detector=double_metaphone,key=WEIGHT_DETECTOR_METAPHONE | weight in range | test_semantic_phase2_part_6.py |
| TC-SEM-2615 | P2 | Weight mapping multi_language #0 | detector=multi_language,key=WEIGHT_DETECTOR_BADWORDS | weight in range | test_semantic_phase2_part_6.py |
| TC-SEM-2616 | P2 | Weight mapping multi_language #1 | detector=multi_language,key=WEIGHT_DETECTOR_BADWORDS | weight in range | test_semantic_phase2_part_6.py |
| TC-SEM-2617 | P2 | Weight mapping multi_language #2 | detector=multi_language,key=WEIGHT_DETECTOR_BADWORDS | weight in range | test_semantic_phase2_part_6.py |
| TC-SEM-2618 | P2 | Weight mapping multi_language #3 | detector=multi_language,key=WEIGHT_DETECTOR_BADWORDS | weight in range | test_semantic_phase2_part_6.py |
| TC-SEM-2619 | P2 | Weight mapping multi_language #4 | detector=multi_language,key=WEIGHT_DETECTOR_BADWORDS | weight in range | test_semantic_phase2_part_6.py |
| TC-SEM-2620 | P2 | Weight mapping multi_language #5 | detector=multi_language,key=WEIGHT_DETECTOR_BADWORDS | weight in range | test_semantic_phase2_part_6.py |
| TC-SEM-2621 | P2 | Weight mapping multi_language #6 | detector=multi_language,key=WEIGHT_DETECTOR_BADWORDS | weight in range | test_semantic_phase2_part_6.py |
| TC-SEM-2622 | P2 | Weight mapping multi_language #7 | detector=multi_language,key=WEIGHT_DETECTOR_BADWORDS | weight in range | test_semantic_phase2_part_6.py |
| TC-SEM-2623 | P2 | Weight mapping multi_language #8 | detector=multi_language,key=WEIGHT_DETECTOR_BADWORDS | weight in range | test_semantic_phase2_part_6.py |
| TC-SEM-2624 | P2 | Weight mapping multi_language #9 | detector=multi_language,key=WEIGHT_DETECTOR_BADWORDS | weight in range | test_semantic_phase2_part_6.py |
| TC-SEM-2625 | P2 | Weight mapping multi_language #10 | detector=multi_language,key=WEIGHT_DETECTOR_BADWORDS | weight in range | test_semantic_phase2_part_6.py |
| TC-SEM-2626 | P2 | Weight mapping multi_language #11 | detector=multi_language,key=WEIGHT_DETECTOR_BADWORDS | weight in range | test_semantic_phase2_part_6.py |
| TC-SEM-2627 | P2 | Weight mapping rolling_hash #0 | detector=rolling_hash,key=WEIGHT_DETECTOR_AHO | weight in range | test_semantic_phase2_part_6.py |
| TC-SEM-2628 | P2 | Weight mapping rolling_hash #1 | detector=rolling_hash,key=WEIGHT_DETECTOR_AHO | weight in range | test_semantic_phase2_part_6.py |
| TC-SEM-2629 | P2 | Weight mapping rolling_hash #2 | detector=rolling_hash,key=WEIGHT_DETECTOR_AHO | weight in range | test_semantic_phase2_part_6.py |
| TC-SEM-2630 | P2 | Weight mapping rolling_hash #3 | detector=rolling_hash,key=WEIGHT_DETECTOR_AHO | weight in range | test_semantic_phase2_part_6.py |
| TC-SEM-2631 | P2 | Weight mapping rolling_hash #4 | detector=rolling_hash,key=WEIGHT_DETECTOR_AHO | weight in range | test_semantic_phase2_part_6.py |
| TC-SEM-2632 | P2 | Weight mapping rolling_hash #5 | detector=rolling_hash,key=WEIGHT_DETECTOR_AHO | weight in range | test_semantic_phase2_part_6.py |
| TC-SEM-2633 | P2 | Weight mapping rolling_hash #6 | detector=rolling_hash,key=WEIGHT_DETECTOR_AHO | weight in range | test_semantic_phase2_part_6.py |
| TC-SEM-2634 | P2 | Weight mapping rolling_hash #7 | detector=rolling_hash,key=WEIGHT_DETECTOR_AHO | weight in range | test_semantic_phase2_part_6.py |
| TC-SEM-2635 | P2 | Weight mapping rolling_hash #8 | detector=rolling_hash,key=WEIGHT_DETECTOR_AHO | weight in range | test_semantic_phase2_part_6.py |
| TC-SEM-2636 | P2 | Weight mapping rolling_hash #9 | detector=rolling_hash,key=WEIGHT_DETECTOR_AHO | weight in range | test_semantic_phase2_part_6.py |
| TC-SEM-2637 | P2 | Weight mapping rolling_hash #10 | detector=rolling_hash,key=WEIGHT_DETECTOR_AHO | weight in range | test_semantic_phase2_part_6.py |
| TC-SEM-2638 | P2 | Weight mapping rolling_hash #11 | detector=rolling_hash,key=WEIGHT_DETECTOR_AHO | weight in range | test_semantic_phase2_part_6.py |
| TC-SEM-2639 | P2 | Weight mapping bloom_filter #0 | detector=bloom_filter,key=WEIGHT_DETECTOR_AHO | weight in range | test_semantic_phase2_part_6.py |
| TC-SEM-2640 | P2 | Weight mapping bloom_filter #1 | detector=bloom_filter,key=WEIGHT_DETECTOR_AHO | weight in range | test_semantic_phase2_part_6.py |
| TC-SEM-2641 | P2 | Weight mapping bloom_filter #2 | detector=bloom_filter,key=WEIGHT_DETECTOR_AHO | weight in range | test_semantic_phase2_part_6.py |
| TC-SEM-2642 | P2 | Weight mapping bloom_filter #3 | detector=bloom_filter,key=WEIGHT_DETECTOR_AHO | weight in range | test_semantic_phase2_part_6.py |
| TC-SEM-2643 | P2 | Weight mapping bloom_filter #4 | detector=bloom_filter,key=WEIGHT_DETECTOR_AHO | weight in range | test_semantic_phase2_part_6.py |
| TC-SEM-2644 | P2 | Weight mapping bloom_filter #5 | detector=bloom_filter,key=WEIGHT_DETECTOR_AHO | weight in range | test_semantic_phase2_part_6.py |
| TC-SEM-2645 | P2 | Weight mapping bloom_filter #6 | detector=bloom_filter,key=WEIGHT_DETECTOR_AHO | weight in range | test_semantic_phase2_part_6.py |
| TC-SEM-2646 | P2 | Weight mapping bloom_filter #7 | detector=bloom_filter,key=WEIGHT_DETECTOR_AHO | weight in range | test_semantic_phase2_part_6.py |
| TC-SEM-2647 | P2 | Weight mapping bloom_filter #8 | detector=bloom_filter,key=WEIGHT_DETECTOR_AHO | weight in range | test_semantic_phase2_part_6.py |
| TC-SEM-2648 | P2 | Weight mapping bloom_filter #9 | detector=bloom_filter,key=WEIGHT_DETECTOR_AHO | weight in range | test_semantic_phase2_part_6.py |
| TC-SEM-2649 | P2 | Weight mapping bloom_filter #10 | detector=bloom_filter,key=WEIGHT_DETECTOR_AHO | weight in range | test_semantic_phase2_part_6.py |
| TC-SEM-2650 | P2 | Weight mapping bloom_filter #11 | detector=bloom_filter,key=WEIGHT_DETECTOR_AHO | weight in range | test_semantic_phase2_part_6.py |
| TC-SEM-2651 | P2 | Category weight political #0 | category=political | boosted | test_semantic_phase2_part_6.py |
| TC-SEM-2652 | P2 | Category weight political #1 | category=political | boosted | test_semantic_phase2_part_6.py |
| TC-SEM-2653 | P2 | Category weight political #2 | category=political | boosted | test_semantic_phase2_part_6.py |
| TC-SEM-2654 | P2 | Category weight political #3 | category=political | boosted | test_semantic_phase2_part_6.py |
| TC-SEM-2655 | P2 | Category weight violence #0 | category=violence | boosted | test_semantic_phase2_part_6.py |
| TC-SEM-2656 | P2 | Category weight violence #1 | category=violence | boosted | test_semantic_phase2_part_6.py |
| TC-SEM-2657 | P2 | Category weight violence #2 | category=violence | boosted | test_semantic_phase2_part_6.py |
| TC-SEM-2658 | P2 | Category weight violence #3 | category=violence | boosted | test_semantic_phase2_part_6.py |
| TC-SEM-2659 | P2 | Category weight sexual #0 | category=sexual | boosted | test_semantic_phase2_part_6.py |
| TC-SEM-2660 | P2 | Category weight sexual #1 | category=sexual | boosted | test_semantic_phase2_part_6.py |
| TC-SEM-2661 | P2 | Category weight sexual #2 | category=sexual | boosted | test_semantic_phase2_part_6.py |
| TC-SEM-2662 | P2 | Category weight sexual #3 | category=sexual | boosted | test_semantic_phase2_part_6.py |
| TC-SEM-2663 | P2 | Category weight hate #0 | category=hate | boosted | test_semantic_phase2_part_6.py |
| TC-SEM-2664 | P2 | Category weight hate #1 | category=hate | boosted | test_semantic_phase2_part_6.py |
| TC-SEM-2665 | P2 | Category weight hate #2 | category=hate | boosted | test_semantic_phase2_part_6.py |
| TC-SEM-2666 | P2 | Category weight hate #3 | category=hate | boosted | test_semantic_phase2_part_6.py |
| TC-SEM-2667 | P2 | Category weight pii #0 | category=pii | boosted | test_semantic_phase2_part_6.py |
| TC-SEM-2668 | P2 | Category weight pii #1 | category=pii | boosted | test_semantic_phase2_part_6.py |
| TC-SEM-2669 | P2 | Category weight pii #2 | category=pii | boosted | test_semantic_phase2_part_6.py |
| TC-SEM-2670 | P2 | Category weight pii #3 | category=pii | boosted | test_semantic_phase2_part_6.py |
| TC-SEM-2671 | P2 | Category weight ads #0 | category=ads | boosted | test_semantic_phase2_part_6.py |
| TC-SEM-2672 | P2 | Category weight ads #1 | category=ads | boosted | test_semantic_phase2_part_6.py |
| TC-SEM-2673 | P2 | Category weight ads #2 | category=ads | boosted | test_semantic_phase2_part_6.py |
| TC-SEM-2674 | P2 | Category weight ads #3 | category=ads | boosted | test_semantic_phase2_part_6.py |
| TC-SEM-2675 | P2 | Category weight other #0 | category=other | boosted | test_semantic_phase2_part_6.py |
| TC-SEM-2676 | P2 | Category weight other #1 | category=other | boosted | test_semantic_phase2_part_6.py |
| TC-SEM-2677 | P2 | Category weight other #2 | category=other | boosted | test_semantic_phase2_part_6.py |
| TC-SEM-2678 | P2 | Category weight other #3 | category=other | boosted | test_semantic_phase2_part_6.py |
| TC-SEM-2679 | P2 | Availability toggle scenario 0 | scenario=0,enabled=True | consistent | test_semantic_phase2_part_6.py |
| TC-SEM-2680 | P2 | Availability toggle scenario 1 | scenario=1,enabled=False | consistent | test_semantic_phase2_part_6.py |
| TC-SEM-2681 | P2 | Availability toggle scenario 2 | scenario=2,enabled=True | consistent | test_semantic_phase2_part_6.py |
| TC-SEM-2682 | P2 | Availability toggle scenario 3 | scenario=3,enabled=False | consistent | test_semantic_phase2_part_6.py |
| TC-SEM-2683 | P2 | Availability toggle scenario 4 | scenario=4,enabled=True | consistent | test_semantic_phase2_part_6.py |
| TC-SEM-2684 | P2 | Availability toggle scenario 5 | scenario=5,enabled=False | consistent | test_semantic_phase2_part_6.py |
| TC-SEM-2685 | P2 | Availability toggle scenario 6 | scenario=6,enabled=True | consistent | test_semantic_phase2_part_6.py |
| TC-SEM-2686 | P2 | Availability toggle scenario 7 | scenario=7,enabled=False | consistent | test_semantic_phase2_part_6.py |
| TC-SEM-2687 | P2 | Availability toggle scenario 8 | scenario=8,enabled=True | consistent | test_semantic_phase2_part_6.py |
| TC-SEM-2688 | P2 | Availability toggle scenario 9 | scenario=9,enabled=False | consistent | test_semantic_phase2_part_6.py |
| TC-SEM-2689 | P2 | Availability toggle scenario 10 | scenario=10,enabled=True | consistent | test_semantic_phase2_part_6.py |
| TC-SEM-2690 | P2 | Availability toggle scenario 11 | scenario=11,enabled=False | consistent | test_semantic_phase2_part_6.py |
| TC-SEM-2691 | P2 | Availability toggle scenario 12 | scenario=12,enabled=True | consistent | test_semantic_phase2_part_6.py |
| TC-SEM-2692 | P2 | Availability toggle scenario 13 | scenario=13,enabled=False | consistent | test_semantic_phase2_part_6.py |
| TC-SEM-2693 | P2 | Availability toggle scenario 14 | scenario=14,enabled=True | consistent | test_semantic_phase2_part_6.py |
| TC-SEM-2694 | P2 | Availability toggle scenario 15 | scenario=15,enabled=False | consistent | test_semantic_phase2_part_6.py |
| TC-SEM-2695 | P2 | Availability toggle scenario 16 | scenario=16,enabled=True | consistent | test_semantic_phase2_part_6.py |
| TC-SEM-2696 | P2 | Availability toggle scenario 17 | scenario=17,enabled=False | consistent | test_semantic_phase2_part_6.py |
| TC-SEM-2697 | P2 | Availability toggle scenario 18 | scenario=18,enabled=True | consistent | test_semantic_phase2_part_6.py |
| TC-SEM-2698 | P2 | Availability toggle scenario 19 | scenario=19,enabled=False | consistent | test_semantic_phase2_part_6.py |
| TC-SEM-2699 | P2 | Availability toggle scenario 20 | scenario=20,enabled=True | consistent | test_semantic_phase2_part_6.py |
| TC-SEM-2700 | P2 | Availability toggle scenario 21 | scenario=21,enabled=False | consistent | test_semantic_phase2_part_6.py |
| TC-SEM-2701 | P2 | Availability toggle scenario 22 | scenario=22,enabled=True | consistent | test_semantic_phase2_part_7.py |
| TC-SEM-2702 | P2 | Availability toggle scenario 23 | scenario=23,enabled=False | consistent | test_semantic_phase2_part_7.py |
| TC-SEM-2703 | P2 | Availability toggle scenario 24 | scenario=24,enabled=True | consistent | test_semantic_phase2_part_7.py |
| TC-SEM-2704 | P2 | Availability toggle scenario 25 | scenario=25,enabled=False | consistent | test_semantic_phase2_part_7.py |
| TC-SEM-2705 | P2 | Availability toggle scenario 26 | scenario=26,enabled=True | consistent | test_semantic_phase2_part_7.py |
| TC-SEM-2706 | P2 | Availability toggle scenario 27 | scenario=27,enabled=False | consistent | test_semantic_phase2_part_7.py |
| TC-SEM-2707 | P2 | Availability toggle scenario 28 | scenario=28,enabled=True | consistent | test_semantic_phase2_part_7.py |
| TC-SEM-2708 | P2 | Availability toggle scenario 29 | scenario=29,enabled=False | consistent | test_semantic_phase2_part_7.py |
| TC-SEM-2709 | P2 | Availability toggle scenario 30 | scenario=30,enabled=True | consistent | test_semantic_phase2_part_7.py |
| TC-SEM-2710 | P2 | Availability toggle scenario 31 | scenario=31,enabled=False | consistent | test_semantic_phase2_part_7.py |
| TC-SEM-2711 | P2 | Availability toggle scenario 32 | scenario=32,enabled=True | consistent | test_semantic_phase2_part_7.py |
| TC-SEM-2712 | P2 | Availability toggle scenario 33 | scenario=33,enabled=False | consistent | test_semantic_phase2_part_7.py |
| TC-SEM-2713 | P2 | Availability toggle scenario 34 | scenario=34,enabled=True | consistent | test_semantic_phase2_part_7.py |
| TC-SEM-2714 | P2 | Availability toggle scenario 35 | scenario=35,enabled=False | consistent | test_semantic_phase2_part_7.py |
| TC-SEM-2715 | P2 | Availability toggle scenario 36 | scenario=36,enabled=True | consistent | test_semantic_phase2_part_7.py |
| TC-SEM-2716 | P2 | Availability toggle scenario 37 | scenario=37,enabled=False | consistent | test_semantic_phase2_part_7.py |
| TC-SEM-2717 | P2 | Availability toggle scenario 38 | scenario=38,enabled=True | consistent | test_semantic_phase2_part_7.py |
| TC-SEM-2718 | P2 | Availability toggle scenario 39 | scenario=39,enabled=False | consistent | test_semantic_phase2_part_7.py |
| TC-SEM-2719 | P2 | Availability toggle scenario 40 | scenario=40,enabled=True | consistent | test_semantic_phase2_part_7.py |
| TC-SEM-2720 | P2 | Availability toggle scenario 41 | scenario=41,enabled=False | consistent | test_semantic_phase2_part_7.py |
| TC-SEM-2721 | P2 | Availability toggle scenario 42 | scenario=42,enabled=True | consistent | test_semantic_phase2_part_7.py |
| TC-SEM-2722 | P2 | Availability toggle scenario 43 | scenario=43,enabled=False | consistent | test_semantic_phase2_part_7.py |
| TC-SEM-2723 | P2 | Availability toggle scenario 44 | scenario=44,enabled=True | consistent | test_semantic_phase2_part_7.py |
| TC-SEM-2724 | P2 | Availability toggle scenario 45 | scenario=45,enabled=False | consistent | test_semantic_phase2_part_7.py |
| TC-SEM-2725 | P2 | Availability toggle scenario 46 | scenario=46,enabled=True | consistent | test_semantic_phase2_part_7.py |
| TC-SEM-2726 | P2 | Availability toggle scenario 47 | scenario=47,enabled=False | consistent | test_semantic_phase2_part_7.py |
| TC-SEM-2727 | P2 | Availability toggle scenario 48 | scenario=48,enabled=True | consistent | test_semantic_phase2_part_7.py |
| TC-SEM-2728 | P2 | Availability toggle scenario 49 | scenario=49,enabled=False | consistent | test_semantic_phase2_part_7.py |
| TC-SEM-2729 | P2 | Availability toggle scenario 50 | scenario=50,enabled=True | consistent | test_semantic_phase2_part_7.py |
| TC-SEM-2730 | P2 | Availability toggle scenario 51 | scenario=51,enabled=False | consistent | test_semantic_phase2_part_7.py |
| TC-SEM-2731 | P2 | Availability toggle scenario 52 | scenario=52,enabled=True | consistent | test_semantic_phase2_part_7.py |
| TC-SEM-2732 | P2 | Availability toggle scenario 53 | scenario=53,enabled=False | consistent | test_semantic_phase2_part_7.py |
| TC-SEM-2733 | P2 | Availability toggle scenario 54 | scenario=54,enabled=True | consistent | test_semantic_phase2_part_7.py |
| TC-SEM-2734 | P2 | Availability toggle scenario 55 | scenario=55,enabled=False | consistent | test_semantic_phase2_part_7.py |
| TC-SEM-2735 | P2 | Availability toggle scenario 56 | scenario=56,enabled=True | consistent | test_semantic_phase2_part_7.py |
| TC-SEM-2736 | P2 | Availability toggle scenario 57 | scenario=57,enabled=False | consistent | test_semantic_phase2_part_7.py |
| TC-SEM-2737 | P2 | Availability toggle scenario 58 | scenario=58,enabled=True | consistent | test_semantic_phase2_part_7.py |
| TC-SEM-2738 | P2 | Availability toggle scenario 59 | scenario=59,enabled=False | consistent | test_semantic_phase2_part_7.py |
| TC-SEM-2739 | P2 | Availability toggle scenario 60 | scenario=60,enabled=True | consistent | test_semantic_phase2_part_7.py |
| TC-SEM-2740 | P2 | Availability toggle scenario 61 | scenario=61,enabled=False | consistent | test_semantic_phase2_part_7.py |
| TC-SEM-2741 | P2 | Availability toggle scenario 62 | scenario=62,enabled=True | consistent | test_semantic_phase2_part_7.py |
| TC-SEM-2742 | P2 | Availability toggle scenario 63 | scenario=63,enabled=False | consistent | test_semantic_phase2_part_7.py |
| TC-SEM-2743 | P2 | Availability toggle scenario 64 | scenario=64,enabled=True | consistent | test_semantic_phase2_part_7.py |
| TC-SEM-2744 | P2 | Availability toggle scenario 65 | scenario=65,enabled=False | consistent | test_semantic_phase2_part_7.py |
| TC-SEM-2745 | P2 | Availability toggle scenario 66 | scenario=66,enabled=True | consistent | test_semantic_phase2_part_7.py |
| TC-SEM-2746 | P2 | Availability toggle scenario 67 | scenario=67,enabled=False | consistent | test_semantic_phase2_part_7.py |
| TC-SEM-2747 | P2 | Availability toggle scenario 68 | scenario=68,enabled=True | consistent | test_semantic_phase2_part_7.py |
| TC-SEM-2748 | P2 | Availability toggle scenario 69 | scenario=69,enabled=False | consistent | test_semantic_phase2_part_7.py |
| TC-SEM-2749 | P2 | Availability toggle scenario 70 | scenario=70,enabled=True | consistent | test_semantic_phase2_part_7.py |
| TC-SEM-2750 | P2 | Availability toggle scenario 71 | scenario=71,enabled=False | consistent | test_semantic_phase2_part_7.py |
| TC-SEM-2751 | P2 | Availability toggle scenario 72 | scenario=72,enabled=True | consistent | test_semantic_phase2_part_7.py |
| TC-SEM-2752 | P2 | Availability toggle scenario 73 | scenario=73,enabled=False | consistent | test_semantic_phase2_part_7.py |
| TC-SEM-2753 | P2 | Availability toggle scenario 74 | scenario=74,enabled=True | consistent | test_semantic_phase2_part_7.py |
| TC-SEM-2754 | P2 | Availability toggle scenario 75 | scenario=75,enabled=False | consistent | test_semantic_phase2_part_7.py |
| TC-SEM-2755 | P2 | Availability toggle scenario 76 | scenario=76,enabled=True | consistent | test_semantic_phase2_part_7.py |
| TC-SEM-2756 | P2 | Availability toggle scenario 77 | scenario=77,enabled=False | consistent | test_semantic_phase2_part_7.py |
| TC-SEM-2757 | P2 | Availability toggle scenario 78 | scenario=78,enabled=True | consistent | test_semantic_phase2_part_7.py |
| TC-SEM-2758 | P2 | Availability toggle scenario 79 | scenario=79,enabled=False | consistent | test_semantic_phase2_part_7.py |
| TC-SEM-2759 | P2 | Availability toggle scenario 80 | scenario=80,enabled=True | consistent | test_semantic_phase2_part_7.py |
| TC-SEM-2760 | P2 | Availability toggle scenario 81 | scenario=81,enabled=False | consistent | test_semantic_phase2_part_7.py |
| TC-SEM-2761 | P2 | Availability toggle scenario 82 | scenario=82,enabled=True | consistent | test_semantic_phase2_part_7.py |
| TC-SEM-2762 | P2 | Availability toggle scenario 83 | scenario=83,enabled=False | consistent | test_semantic_phase2_part_7.py |
| TC-SEM-2763 | P2 | Availability toggle scenario 84 | scenario=84,enabled=True | consistent | test_semantic_phase2_part_7.py |
| TC-SEM-2764 | P2 | Availability toggle scenario 85 | scenario=85,enabled=False | consistent | test_semantic_phase2_part_7.py |
| TC-SEM-2765 | P2 | Availability toggle scenario 86 | scenario=86,enabled=True | consistent | test_semantic_phase2_part_7.py |
| TC-SEM-2766 | P2 | Availability toggle scenario 87 | scenario=87,enabled=False | consistent | test_semantic_phase2_part_7.py |
| TC-SEM-2767 | P2 | Availability toggle scenario 88 | scenario=88,enabled=True | consistent | test_semantic_phase2_part_7.py |
| TC-SEM-2768 | P2 | Availability toggle scenario 89 | scenario=89,enabled=False | consistent | test_semantic_phase2_part_7.py |
| TC-SEM-2769 | P2 | Availability toggle scenario 90 | scenario=90,enabled=True | consistent | test_semantic_phase2_part_7.py |
| TC-SEM-2770 | P2 | Availability toggle scenario 91 | scenario=91,enabled=False | consistent | test_semantic_phase2_part_7.py |
| TC-SEM-2771 | P2 | Availability toggle scenario 92 | scenario=92,enabled=True | consistent | test_semantic_phase2_part_7.py |
| TC-SEM-2772 | P2 | Availability toggle scenario 93 | scenario=93,enabled=False | consistent | test_semantic_phase2_part_7.py |
| TC-SEM-2773 | P2 | Availability toggle scenario 94 | scenario=94,enabled=True | consistent | test_semantic_phase2_part_7.py |
| TC-SEM-2774 | P2 | Availability toggle scenario 95 | scenario=95,enabled=False | consistent | test_semantic_phase2_part_7.py |
| TC-SEM-2775 | P2 | Availability toggle scenario 96 | scenario=96,enabled=True | consistent | test_semantic_phase2_part_7.py |
| TC-SEM-2776 | P2 | Availability toggle scenario 97 | scenario=97,enabled=False | consistent | test_semantic_phase2_part_7.py |
| TC-SEM-2777 | P2 | Availability toggle scenario 98 | scenario=98,enabled=True | consistent | test_semantic_phase2_part_7.py |
| TC-SEM-2778 | P2 | Availability toggle scenario 99 | scenario=99,enabled=False | consistent | test_semantic_phase2_part_7.py |
| TC-SEM-2779 | P2 | Availability toggle scenario 100 | scenario=100,enabled=True | consistent | test_semantic_phase2_part_7.py |
| TC-SEM-2780 | P2 | Availability toggle scenario 101 | scenario=101,enabled=False | consistent | test_semantic_phase2_part_7.py |
| TC-SEM-2781 | P2 | Availability toggle scenario 102 | scenario=102,enabled=True | consistent | test_semantic_phase2_part_7.py |
| TC-SEM-2782 | P2 | Availability toggle scenario 103 | scenario=103,enabled=False | consistent | test_semantic_phase2_part_7.py |
| TC-SEM-2783 | P2 | Availability toggle scenario 104 | scenario=104,enabled=True | consistent | test_semantic_phase2_part_7.py |
| TC-SEM-2784 | P2 | Availability toggle scenario 105 | scenario=105,enabled=False | consistent | test_semantic_phase2_part_7.py |
| TC-SEM-2785 | P2 | Availability toggle scenario 106 | scenario=106,enabled=True | consistent | test_semantic_phase2_part_7.py |
| TC-SEM-2786 | P2 | Availability toggle scenario 107 | scenario=107,enabled=False | consistent | test_semantic_phase2_part_7.py |
| TC-SEM-2787 | P2 | Availability toggle scenario 108 | scenario=108,enabled=True | consistent | test_semantic_phase2_part_7.py |
| TC-SEM-2788 | P2 | Availability toggle scenario 109 | scenario=109,enabled=False | consistent | test_semantic_phase2_part_7.py |
| TC-SEM-2789 | P2 | Availability toggle scenario 110 | scenario=110,enabled=True | consistent | test_semantic_phase2_part_7.py |
| TC-SEM-2790 | P2 | Availability toggle scenario 111 | scenario=111,enabled=False | consistent | test_semantic_phase2_part_7.py |
| TC-SEM-2791 | P2 | Availability toggle scenario 112 | scenario=112,enabled=True | consistent | test_semantic_phase2_part_7.py |
| TC-SEM-2792 | P2 | Availability toggle scenario 113 | scenario=113,enabled=False | consistent | test_semantic_phase2_part_7.py |
| TC-SEM-2793 | P2 | Availability toggle scenario 114 | scenario=114,enabled=True | consistent | test_semantic_phase2_part_7.py |
| TC-SEM-2794 | P2 | Availability toggle scenario 115 | scenario=115,enabled=False | consistent | test_semantic_phase2_part_7.py |
| TC-SEM-2795 | P2 | Availability toggle scenario 116 | scenario=116,enabled=True | consistent | test_semantic_phase2_part_7.py |
| TC-SEM-2796 | P2 | Availability toggle scenario 117 | scenario=117,enabled=False | consistent | test_semantic_phase2_part_7.py |
| TC-SEM-2797 | P2 | Availability toggle scenario 118 | scenario=118,enabled=True | consistent | test_semantic_phase2_part_7.py |
| TC-SEM-2798 | P2 | Availability toggle scenario 119 | scenario=119,enabled=False | consistent | test_semantic_phase2_part_7.py |
| TC-SEM-2799 | P2 | Availability toggle scenario 120 | scenario=120,enabled=True | consistent | test_semantic_phase2_part_7.py |
| TC-SEM-2800 | P2 | Availability toggle scenario 121 | scenario=121,enabled=False | consistent | test_semantic_phase2_part_7.py |

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
