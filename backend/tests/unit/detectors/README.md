# Detector Module Test Documentation

## Overview
- **Total Planned:** 2,100,000
- **Phase 1:** 125 (IDs TC-DET-001 to TC-DET-0125) :white_check_mark: Implemented
- **Phase 2:** 1200 (IDs TC-DET-0126 to TC-DET-1325) :white_check_mark: Implemented
- **Phase 3:** 20,000 (IDs TC-DET-1326 to TC-DET-21325) :hourglass: Planned
- **Phase 4:** 200,000 (IDs TC-DET-21326 to TC-DET-221325) :hourglass: Planned
- **Phase 5:** 1,878,675 (IDs TC-DET-221326 to TC-DET-2100000) :hourglass: Planned

## Dimension Matrix
| Dimension | Values (Phase 2) |
| :--- | :--- |
| Detector | aho, bk-tree, metaphone, multi-language, badwords-py, profanite, glin-profanity, gangajal, safetext, sensitive-word-filter-cn, profanity-filter2, pyprofane |
| Language | en, zh-CN, ru, es, fr, ja, ko, de, it, ar, hi, tr, pt, nl, pl, uk, cs, el, sv, no, da, fi, hu, ro, bg, he, th |
| Length | 1-8192 |
| Content | clean, profanity, hate, violence, ads, pii, mixed, obfuscated, encoded, transliterated |
| Edit distance | 0, 1, 2, 3 |

## Test Case List

### Phase 1 - 125 cases
- 125 cases (basic exact/fuzzy/phonetic matching, 5 languages, standard text lengths).

### Phase 2 (Current) - 1200 cases
| ID | Priority | Description | Dimensions | Expected Outcome | File |
| :--- | :--- | :--- | :--- | :--- | :--- |
| TC-DET-201 | P1 | Aho positive over en | en positive | matched=True | test_detectors_phase2_part_1.py |
| TC-DET-202 | P1 | Aho clean over en | en clean | matched=False | test_detectors_phase2_part_1.py |
| TC-DET-203 | P1 | Aho positive over zh-CN | zh-CN positive | matched=True | test_detectors_phase2_part_1.py |
| TC-DET-204 | P1 | Aho clean over zh-CN | zh-CN clean | matched=False | test_detectors_phase2_part_1.py |
| TC-DET-205 | P1 | Aho positive over ja | ja positive | matched=True | test_detectors_phase2_part_1.py |
| TC-DET-206 | P1 | Aho clean over ja | ja clean | matched=False | test_detectors_phase2_part_1.py |
| TC-DET-207 | P1 | Aho positive over ko | ko positive | matched=True | test_detectors_phase2_part_1.py |
| TC-DET-208 | P1 | Aho clean over ko | ko clean | matched=False | test_detectors_phase2_part_1.py |
| TC-DET-209 | P1 | Aho positive over ru | ru positive | matched=True | test_detectors_phase2_part_1.py |
| TC-DET-210 | P1 | Aho clean over ru | ru clean | matched=False | test_detectors_phase2_part_1.py |
| TC-DET-211 | P1 | Aho positive over es | es positive | matched=True | test_detectors_phase2_part_1.py |
| TC-DET-212 | P1 | Aho clean over es | es clean | matched=False | test_detectors_phase2_part_1.py |
| TC-DET-213 | P1 | Aho positive over fr | fr positive | matched=True | test_detectors_phase2_part_1.py |
| TC-DET-214 | P1 | Aho clean over fr | fr clean | matched=False | test_detectors_phase2_part_1.py |
| TC-DET-215 | P1 | Aho positive over de | de positive | matched=True | test_detectors_phase2_part_1.py |
| TC-DET-216 | P1 | Aho clean over de | de clean | matched=False | test_detectors_phase2_part_1.py |
| TC-DET-217 | P1 | Aho positive over it | it positive | matched=True | test_detectors_phase2_part_1.py |
| TC-DET-218 | P1 | Aho clean over it | it clean | matched=False | test_detectors_phase2_part_1.py |
| TC-DET-219 | P1 | Aho positive over ar | ar positive | matched=True | test_detectors_phase2_part_1.py |
| TC-DET-220 | P1 | Aho clean over ar | ar clean | matched=False | test_detectors_phase2_part_1.py |
| TC-DET-221 | P1 | Aho positive over hi | hi positive | matched=True | test_detectors_phase2_part_1.py |
| TC-DET-222 | P1 | Aho clean over hi | hi clean | matched=False | test_detectors_phase2_part_1.py |
| TC-DET-223 | P1 | Aho positive over tr | tr positive | matched=True | test_detectors_phase2_part_1.py |
| TC-DET-224 | P1 | Aho clean over tr | tr clean | matched=False | test_detectors_phase2_part_1.py |
| TC-DET-225 | P1 | Aho positive over pt | pt positive | matched=True | test_detectors_phase2_part_1.py |
| TC-DET-226 | P1 | Aho clean over pt | pt clean | matched=False | test_detectors_phase2_part_1.py |
| TC-DET-227 | P1 | Aho positive over nl | nl positive | matched=True | test_detectors_phase2_part_1.py |
| TC-DET-228 | P1 | Aho clean over nl | nl clean | matched=False | test_detectors_phase2_part_1.py |
| TC-DET-229 | P1 | Aho positive over pl | pl positive | matched=True | test_detectors_phase2_part_1.py |
| TC-DET-230 | P1 | Aho clean over pl | pl clean | matched=False | test_detectors_phase2_part_1.py |
| TC-DET-231 | P1 | Aho positive over uk | uk positive | matched=True | test_detectors_phase2_part_1.py |
| TC-DET-232 | P1 | Aho clean over uk | uk clean | matched=False | test_detectors_phase2_part_1.py |
| TC-DET-233 | P1 | Aho positive over cs | cs positive | matched=True | test_detectors_phase2_part_1.py |
| TC-DET-234 | P1 | Aho clean over cs | cs clean | matched=False | test_detectors_phase2_part_1.py |
| TC-DET-235 | P1 | Aho positive over el | el positive | matched=True | test_detectors_phase2_part_1.py |
| TC-DET-236 | P1 | Aho clean over el | el clean | matched=False | test_detectors_phase2_part_1.py |
| TC-DET-237 | P1 | Aho positive over sv | sv positive | matched=True | test_detectors_phase2_part_1.py |
| TC-DET-238 | P1 | Aho clean over sv | sv clean | matched=False | test_detectors_phase2_part_1.py |
| TC-DET-239 | P1 | Aho positive over no | no positive | matched=True | test_detectors_phase2_part_1.py |
| TC-DET-240 | P1 | Aho clean over no | no clean | matched=False | test_detectors_phase2_part_1.py |
| TC-DET-241 | P1 | Aho positive over da | da positive | matched=True | test_detectors_phase2_part_1.py |
| TC-DET-242 | P1 | Aho clean over da | da clean | matched=False | test_detectors_phase2_part_1.py |
| TC-DET-243 | P1 | Aho positive over fi | fi positive | matched=True | test_detectors_phase2_part_1.py |
| TC-DET-244 | P1 | Aho clean over fi | fi clean | matched=False | test_detectors_phase2_part_1.py |
| TC-DET-245 | P1 | Aho positive over hu | hu positive | matched=True | test_detectors_phase2_part_1.py |
| TC-DET-246 | P1 | Aho clean over hu | hu clean | matched=False | test_detectors_phase2_part_1.py |
| TC-DET-247 | P1 | Aho positive over ro | ro positive | matched=True | test_detectors_phase2_part_1.py |
| TC-DET-248 | P1 | Aho clean over ro | ro clean | matched=False | test_detectors_phase2_part_1.py |
| TC-DET-249 | P1 | Aho positive over bg | bg positive | matched=True | test_detectors_phase2_part_1.py |
| TC-DET-250 | P1 | Aho clean over bg | bg clean | matched=False | test_detectors_phase2_part_1.py |
| TC-DET-251 | P1 | Aho positive over he | he positive | matched=True | test_detectors_phase2_part_1.py |
| TC-DET-252 | P1 | Aho clean over he | he clean | matched=False | test_detectors_phase2_part_1.py |
| TC-DET-253 | P1 | Aho positive over th | th positive | matched=True | test_detectors_phase2_part_1.py |
| TC-DET-254 | P1 | Aho clean over th | th clean | matched=False | test_detectors_phase2_part_1.py |
| TC-DET-255 | P1 | Aho full-width over en | en fullwidth | matched=True | test_detectors_phase2_part_1.py |
| TC-DET-256 | P1 | Aho full-width over zh-CN | zh-CN fullwidth | matched=True | test_detectors_phase2_part_1.py |
| TC-DET-257 | P1 | Aho full-width over ja | ja fullwidth | matched=True | test_detectors_phase2_part_1.py |
| TC-DET-258 | P1 | Aho full-width over ko | ko fullwidth | matched=True | test_detectors_phase2_part_1.py |
| TC-DET-259 | P1 | Aho full-width over ru | ru fullwidth | matched=True | test_detectors_phase2_part_1.py |
| TC-DET-260 | P1 | Aho full-width over es | es fullwidth | matched=True | test_detectors_phase2_part_1.py |
| TC-DET-261 | P1 | Aho full-width over fr | fr fullwidth | matched=True | test_detectors_phase2_part_1.py |
| TC-DET-262 | P1 | Aho full-width over de | de fullwidth | matched=True | test_detectors_phase2_part_1.py |
| TC-DET-263 | P1 | Aho full-width over it | it fullwidth | matched=True | test_detectors_phase2_part_1.py |
| TC-DET-264 | P1 | Aho full-width over ar | ar fullwidth | matched=True | test_detectors_phase2_part_1.py |
| TC-DET-265 | P1 | Aho full-width over hi | hi fullwidth | matched=True | test_detectors_phase2_part_1.py |
| TC-DET-266 | P1 | Aho full-width over tr | tr fullwidth | matched=True | test_detectors_phase2_part_1.py |
| TC-DET-267 | P1 | Aho full-width over pt | pt fullwidth | matched=True | test_detectors_phase2_part_1.py |
| TC-DET-268 | P1 | Aho full-width over nl | nl fullwidth | matched=True | test_detectors_phase2_part_1.py |
| TC-DET-269 | P1 | Aho full-width over pl | pl fullwidth | matched=True | test_detectors_phase2_part_1.py |
| TC-DET-270 | P1 | Aho full-width over uk | uk fullwidth | matched=True | test_detectors_phase2_part_1.py |
| TC-DET-271 | P1 | Aho full-width over cs | cs fullwidth | matched=True | test_detectors_phase2_part_1.py |
| TC-DET-272 | P1 | Aho full-width over el | el fullwidth | matched=True | test_detectors_phase2_part_1.py |
| TC-DET-273 | P1 | Aho full-width over sv | sv fullwidth | matched=True | test_detectors_phase2_part_1.py |
| TC-DET-274 | P1 | Aho full-width over no | no fullwidth | matched=True | test_detectors_phase2_part_1.py |
| TC-DET-275 | P1 | Aho full-width over da | da fullwidth | matched=True | test_detectors_phase2_part_1.py |
| TC-DET-276 | P1 | Aho full-width over fi | fi fullwidth | matched=True | test_detectors_phase2_part_1.py |
| TC-DET-277 | P1 | Aho full-width over hu | hu fullwidth | matched=True | test_detectors_phase2_part_1.py |
| TC-DET-278 | P1 | Aho full-width over ro | ro fullwidth | matched=True | test_detectors_phase2_part_1.py |
| TC-DET-279 | P1 | Aho full-width over bg | bg fullwidth | matched=True | test_detectors_phase2_part_1.py |
| TC-DET-280 | P1 | Aho full-width over he | he fullwidth | matched=True | test_detectors_phase2_part_1.py |
| TC-DET-281 | P1 | Aho full-width over th | th fullwidth | matched=True | test_detectors_phase2_part_1.py |
| TC-DET-282 | P1 | Aho separator   | separator=  | matched=False | test_detectors_phase2_part_1.py |
| TC-DET-283 | P1 | Aho separator * | separator=* | matched=False | test_detectors_phase2_part_1.py |
| TC-DET-284 | P1 | Aho separator . | separator=. | matched=False | test_detectors_phase2_part_1.py |
| TC-DET-285 | P1 | Aho separator _ | separator=_ | matched=False | test_detectors_phase2_part_1.py |
| TC-DET-286 | P1 | Aho separator - | separator=- | matched=False | test_detectors_phase2_part_1.py |
| TC-DET-287 | P1 | Aho separator + | separator=+ | matched=False | test_detectors_phase2_part_1.py |
| TC-DET-288 | P1 | Aho separator ~ | separator=~ | matched=False | test_detectors_phase2_part_1.py |
| TC-DET-289 | P1 | Aho separator   | separator=  | matched=False | test_detectors_phase2_part_1.py |
| TC-DET-290 | P1 | Aho separator * | separator=* | matched=False | test_detectors_phase2_part_1.py |
| TC-DET-291 | P1 | Aho separator . | separator=. | matched=False | test_detectors_phase2_part_1.py |
| TC-DET-292 | P1 | Aho separator _ | separator=_ | matched=False | test_detectors_phase2_part_1.py |
| TC-DET-293 | P1 | Aho separator - | separator=- | matched=False | test_detectors_phase2_part_1.py |
| TC-DET-294 | P1 | Aho separator + | separator=+ | matched=False | test_detectors_phase2_part_1.py |
| TC-DET-295 | P1 | Aho separator ~ | separator=~ | matched=False | test_detectors_phase2_part_1.py |
| TC-DET-296 | P1 | Aho separator   | separator=  | matched=False | test_detectors_phase2_part_1.py |
| TC-DET-297 | P1 | Aho separator * | separator=* | matched=False | test_detectors_phase2_part_1.py |
| TC-DET-298 | P1 | Aho separator . | separator=. | matched=False | test_detectors_phase2_part_1.py |
| TC-DET-299 | P1 | Aho separator _ | separator=_ | matched=False | test_detectors_phase2_part_1.py |
| TC-DET-300 | P1 | Aho separator - | separator=- | matched=False | test_detectors_phase2_part_1.py |
| TC-DET-301 | P1 | Aho separator + | separator=+ | matched=False | test_detectors_phase2_part_2.py |
| TC-DET-302 | P1 | Aho separator ~ | separator=~ | matched=False | test_detectors_phase2_part_2.py |
| TC-DET-303 | P1 | Aho separator   | separator=  | matched=False | test_detectors_phase2_part_2.py |
| TC-DET-304 | P1 | Aho separator * | separator=* | matched=False | test_detectors_phase2_part_2.py |
| TC-DET-305 | P1 | Aho separator . | separator=. | matched=False | test_detectors_phase2_part_2.py |
| TC-DET-306 | P1 | Aho separator _ | separator=_ | matched=False | test_detectors_phase2_part_2.py |
| TC-DET-307 | P1 | Aho separator - | separator=- | matched=False | test_detectors_phase2_part_2.py |
| TC-DET-308 | P1 | Aho separator + | separator=+ | matched=False | test_detectors_phase2_part_2.py |
| TC-DET-309 | P1 | Aho separator ~ | separator=~ | matched=False | test_detectors_phase2_part_2.py |
| TC-DET-310 | P1 | Aho separator   | separator=  | matched=False | test_detectors_phase2_part_2.py |
| TC-DET-311 | P1 | Aho separator * | separator=* | matched=False | test_detectors_phase2_part_2.py |
| TC-DET-312 | P1 | Aho separator . | separator=. | matched=False | test_detectors_phase2_part_2.py |
| TC-DET-313 | P1 | Aho separator _ | separator=_ | matched=False | test_detectors_phase2_part_2.py |
| TC-DET-314 | P1 | Aho separator - | separator=- | matched=False | test_detectors_phase2_part_2.py |
| TC-DET-315 | P1 | Aho separator + | separator=+ | matched=False | test_detectors_phase2_part_2.py |
| TC-DET-316 | P1 | Aho separator ~ | separator=~ | matched=False | test_detectors_phase2_part_2.py |
| TC-DET-317 | P1 | Aho separator   | separator=  | matched=False | test_detectors_phase2_part_2.py |
| TC-DET-318 | P1 | Aho separator * | separator=* | matched=False | test_detectors_phase2_part_2.py |
| TC-DET-319 | P1 | Aho separator . | separator=. | matched=False | test_detectors_phase2_part_2.py |
| TC-DET-320 | P1 | Aho separator _ | separator=_ | matched=False | test_detectors_phase2_part_2.py |
| TC-DET-321 | P1 | Aho separator - | separator=- | matched=False | test_detectors_phase2_part_2.py |
| TC-DET-322 | P1 | Aho separator + | separator=+ | matched=False | test_detectors_phase2_part_2.py |
| TC-DET-323 | P1 | Aho separator ~ | separator=~ | matched=False | test_detectors_phase2_part_2.py |
| TC-DET-324 | P2 | Aho long text 200 | length=200 | matched=True | test_detectors_phase2_part_2.py |
| TC-DET-325 | P2 | Aho long text 500 | length=500 | matched=True | test_detectors_phase2_part_2.py |
| TC-DET-326 | P2 | Aho long text 1000 | length=1000 | matched=True | test_detectors_phase2_part_2.py |
| TC-DET-327 | P2 | Aho long text 2000 | length=2000 | matched=True | test_detectors_phase2_part_2.py |
| TC-DET-328 | P2 | Aho long text 5000 | length=5000 | matched=True | test_detectors_phase2_part_2.py |
| TC-DET-329 | P2 | Aho long text 200 | length=200 | matched=True | test_detectors_phase2_part_2.py |
| TC-DET-330 | P2 | Aho long text 500 | length=500 | matched=True | test_detectors_phase2_part_2.py |
| TC-DET-331 | P2 | Aho long text 1000 | length=1000 | matched=True | test_detectors_phase2_part_2.py |
| TC-DET-332 | P2 | Aho long text 2000 | length=2000 | matched=True | test_detectors_phase2_part_2.py |
| TC-DET-333 | P2 | Aho long text 5000 | length=5000 | matched=True | test_detectors_phase2_part_2.py |
| TC-DET-334 | P2 | Aho long text 200 | length=200 | matched=True | test_detectors_phase2_part_2.py |
| TC-DET-335 | P2 | Aho long text 500 | length=500 | matched=True | test_detectors_phase2_part_2.py |
| TC-DET-336 | P2 | Aho long text 1000 | length=1000 | matched=True | test_detectors_phase2_part_2.py |
| TC-DET-337 | P2 | Aho long text 2000 | length=2000 | matched=True | test_detectors_phase2_part_2.py |
| TC-DET-338 | P2 | Aho long text 5000 | length=5000 | matched=True | test_detectors_phase2_part_2.py |
| TC-DET-339 | P2 | Aho long text 200 | length=200 | matched=True | test_detectors_phase2_part_2.py |
| TC-DET-340 | P2 | Aho long text 500 | length=500 | matched=True | test_detectors_phase2_part_2.py |
| TC-DET-341 | P2 | Aho long text 1000 | length=1000 | matched=True | test_detectors_phase2_part_2.py |
| TC-DET-342 | P2 | Aho long text 2000 | length=2000 | matched=True | test_detectors_phase2_part_2.py |
| TC-DET-343 | P2 | Aho long text 5000 | length=5000 | matched=True | test_detectors_phase2_part_2.py |
| TC-DET-344 | P2 | Aho long text 200 | length=200 | matched=True | test_detectors_phase2_part_2.py |
| TC-DET-345 | P2 | Aho long text 500 | length=500 | matched=True | test_detectors_phase2_part_2.py |
| TC-DET-346 | P2 | Aho long text 1000 | length=1000 | matched=True | test_detectors_phase2_part_2.py |
| TC-DET-347 | P2 | Aho long text 2000 | length=2000 | matched=True | test_detectors_phase2_part_2.py |
| TC-DET-348 | P2 | Aho long text 5000 | length=5000 | matched=True | test_detectors_phase2_part_2.py |
| TC-DET-349 | P2 | Aho long text 200 | length=200 | matched=True | test_detectors_phase2_part_2.py |
| TC-DET-350 | P2 | Aho long text 500 | length=500 | matched=True | test_detectors_phase2_part_2.py |
| TC-DET-351 | P2 | Aho long text 1000 | length=1000 | matched=True | test_detectors_phase2_part_2.py |
| TC-DET-352 | P2 | Aho long text 2000 | length=2000 | matched=True | test_detectors_phase2_part_2.py |
| TC-DET-353 | P2 | Aho long text 5000 | length=5000 | matched=True | test_detectors_phase2_part_2.py |
| TC-DET-354 | P2 | Aho long text 200 | length=200 | matched=True | test_detectors_phase2_part_2.py |
| TC-DET-355 | P2 | Aho long text 500 | length=500 | matched=True | test_detectors_phase2_part_2.py |
| TC-DET-356 | P2 | Aho long text 1000 | length=1000 | matched=True | test_detectors_phase2_part_2.py |
| TC-DET-357 | P2 | Aho long text 2000 | length=2000 | matched=True | test_detectors_phase2_part_2.py |
| TC-DET-358 | P2 | Aho long text 5000 | length=5000 | matched=True | test_detectors_phase2_part_2.py |
| TC-DET-359 | P2 | Aho long text 200 | length=200 | matched=True | test_detectors_phase2_part_2.py |
| TC-DET-360 | P2 | Aho long text 500 | length=500 | matched=True | test_detectors_phase2_part_2.py |
| TC-DET-361 | P2 | Aho long text 1000 | length=1000 | matched=True | test_detectors_phase2_part_2.py |
| TC-DET-362 | P2 | Aho long text 2000 | length=2000 | matched=True | test_detectors_phase2_part_2.py |
| TC-DET-363 | P2 | Aho long text 5000 | length=5000 | matched=True | test_detectors_phase2_part_2.py |
| TC-DET-364 | P2 | Aho long text 200 | length=200 | matched=True | test_detectors_phase2_part_2.py |
| TC-DET-365 | P2 | Aho long text 500 | length=500 | matched=True | test_detectors_phase2_part_2.py |
| TC-DET-366 | P2 | Aho long text 1000 | length=1000 | matched=True | test_detectors_phase2_part_2.py |
| TC-DET-367 | P2 | Aho long text 2000 | length=2000 | matched=True | test_detectors_phase2_part_2.py |
| TC-DET-368 | P2 | Aho long text 5000 | length=5000 | matched=True | test_detectors_phase2_part_2.py |
| TC-DET-369 | P2 | Aho long text 200 | length=200 | matched=True | test_detectors_phase2_part_2.py |
| TC-DET-370 | P2 | Aho long text 500 | length=500 | matched=True | test_detectors_phase2_part_2.py |
| TC-DET-371 | P2 | Aho long text 1000 | length=1000 | matched=True | test_detectors_phase2_part_2.py |
| TC-DET-372 | P2 | Aho long text 2000 | length=2000 | matched=True | test_detectors_phase2_part_2.py |
| TC-DET-373 | P2 | Aho long text 5000 | length=5000 | matched=True | test_detectors_phase2_part_2.py |
| TC-DET-374 | P2 | Aho mixed content over en | en mixed | matched=True | test_detectors_phase2_part_2.py |
| TC-DET-375 | P2 | Aho mixed content over zh-CN | zh-CN mixed | matched=True | test_detectors_phase2_part_2.py |
| TC-DET-376 | P2 | Aho mixed content over ja | ja mixed | matched=True | test_detectors_phase2_part_2.py |
| TC-DET-377 | P2 | Aho mixed content over ko | ko mixed | matched=True | test_detectors_phase2_part_2.py |
| TC-DET-378 | P2 | Aho mixed content over ru | ru mixed | matched=True | test_detectors_phase2_part_2.py |
| TC-DET-379 | P2 | Aho mixed content over es | es mixed | matched=True | test_detectors_phase2_part_2.py |
| TC-DET-380 | P2 | Aho mixed content over fr | fr mixed | matched=True | test_detectors_phase2_part_2.py |
| TC-DET-381 | P2 | Aho mixed content over de | de mixed | matched=True | test_detectors_phase2_part_2.py |
| TC-DET-382 | P2 | Aho mixed content over it | it mixed | matched=True | test_detectors_phase2_part_2.py |
| TC-DET-383 | P2 | Aho mixed content over ar | ar mixed | matched=True | test_detectors_phase2_part_2.py |
| TC-DET-384 | P2 | Aho mixed content over hi | hi mixed | matched=True | test_detectors_phase2_part_2.py |
| TC-DET-385 | P2 | Aho mixed content over tr | tr mixed | matched=True | test_detectors_phase2_part_2.py |
| TC-DET-386 | P2 | Aho mixed content over pt | pt mixed | matched=True | test_detectors_phase2_part_2.py |
| TC-DET-387 | P2 | Aho mixed content over nl | nl mixed | matched=True | test_detectors_phase2_part_2.py |
| TC-DET-388 | P2 | Aho mixed content over pl | pl mixed | matched=True | test_detectors_phase2_part_2.py |
| TC-DET-389 | P2 | Aho mixed content over uk | uk mixed | matched=True | test_detectors_phase2_part_2.py |
| TC-DET-390 | P2 | Aho mixed content over cs | cs mixed | matched=True | test_detectors_phase2_part_2.py |
| TC-DET-391 | P2 | Aho mixed content over el | el mixed | matched=True | test_detectors_phase2_part_2.py |
| TC-DET-392 | P2 | Aho mixed content over sv | sv mixed | matched=True | test_detectors_phase2_part_2.py |
| TC-DET-393 | P2 | Aho mixed content over no | no mixed | matched=True | test_detectors_phase2_part_2.py |
| TC-DET-394 | P2 | Aho mixed content over da | da mixed | matched=True | test_detectors_phase2_part_2.py |
| TC-DET-395 | P2 | Aho mixed content over fi | fi mixed | matched=True | test_detectors_phase2_part_2.py |
| TC-DET-396 | P2 | Aho mixed content over hu | hu mixed | matched=True | test_detectors_phase2_part_2.py |
| TC-DET-397 | P2 | Aho mixed content over ro | ro mixed | matched=True | test_detectors_phase2_part_2.py |
| TC-DET-398 | P2 | Aho mixed content over bg | bg mixed | matched=True | test_detectors_phase2_part_2.py |
| TC-DET-399 | P2 | Aho mixed content over he | he mixed | matched=True | test_detectors_phase2_part_2.py |
| TC-DET-400 | P2 | Aho mixed content over th | th mixed | matched=True | test_detectors_phase2_part_2.py |
| TC-DET-401 | P1 | BK mutation dist=1 | dist=1 | matched=True | test_detectors_phase2_part_3.py |
| TC-DET-402 | P1 | BK mutation dist=2 | dist=2 | matched=True | test_detectors_phase2_part_3.py |
| TC-DET-403 | P1 | BK mutation dist=3 | dist=3 | matched=True | test_detectors_phase2_part_3.py |
| TC-DET-404 | P1 | BK mutation dist=1 | dist=1 | matched=True | test_detectors_phase2_part_3.py |
| TC-DET-405 | P1 | BK mutation dist=2 | dist=2 | matched=True | test_detectors_phase2_part_3.py |
| TC-DET-406 | P1 | BK mutation dist=3 | dist=3 | matched=True | test_detectors_phase2_part_3.py |
| TC-DET-407 | P1 | BK mutation dist=1 | dist=1 | matched=True | test_detectors_phase2_part_3.py |
| TC-DET-408 | P1 | BK mutation dist=2 | dist=2 | matched=True | test_detectors_phase2_part_3.py |
| TC-DET-409 | P1 | BK mutation dist=3 | dist=3 | matched=True | test_detectors_phase2_part_3.py |
| TC-DET-410 | P1 | BK mutation dist=1 | dist=1 | matched=True | test_detectors_phase2_part_3.py |
| TC-DET-411 | P1 | BK mutation dist=2 | dist=2 | matched=True | test_detectors_phase2_part_3.py |
| TC-DET-412 | P1 | BK mutation dist=3 | dist=3 | matched=True | test_detectors_phase2_part_3.py |
| TC-DET-413 | P1 | BK mutation dist=1 | dist=1 | matched=True | test_detectors_phase2_part_3.py |
| TC-DET-414 | P1 | BK mutation dist=2 | dist=2 | matched=True | test_detectors_phase2_part_3.py |
| TC-DET-415 | P1 | BK mutation dist=3 | dist=3 | matched=True | test_detectors_phase2_part_3.py |
| TC-DET-416 | P1 | BK mutation dist=1 | dist=1 | matched=True | test_detectors_phase2_part_3.py |
| TC-DET-417 | P1 | BK mutation dist=2 | dist=2 | matched=True | test_detectors_phase2_part_3.py |
| TC-DET-418 | P1 | BK mutation dist=3 | dist=3 | matched=True | test_detectors_phase2_part_3.py |
| TC-DET-419 | P1 | BK mutation dist=1 | dist=1 | matched=True | test_detectors_phase2_part_3.py |
| TC-DET-420 | P1 | BK mutation dist=2 | dist=2 | matched=True | test_detectors_phase2_part_3.py |
| TC-DET-421 | P1 | BK mutation dist=3 | dist=3 | matched=True | test_detectors_phase2_part_3.py |
| TC-DET-422 | P1 | BK mutation dist=1 | dist=1 | matched=True | test_detectors_phase2_part_3.py |
| TC-DET-423 | P1 | BK mutation dist=2 | dist=2 | matched=True | test_detectors_phase2_part_3.py |
| TC-DET-424 | P1 | BK mutation dist=3 | dist=3 | matched=True | test_detectors_phase2_part_3.py |
| TC-DET-425 | P1 | BK mutation dist=1 | dist=1 | matched=True | test_detectors_phase2_part_3.py |
| TC-DET-426 | P1 | BK mutation dist=2 | dist=2 | matched=True | test_detectors_phase2_part_3.py |
| TC-DET-427 | P1 | BK mutation dist=3 | dist=3 | matched=True | test_detectors_phase2_part_3.py |
| TC-DET-428 | P1 | BK mutation dist=1 | dist=1 | matched=True | test_detectors_phase2_part_3.py |
| TC-DET-429 | P1 | BK mutation dist=2 | dist=2 | matched=True | test_detectors_phase2_part_3.py |
| TC-DET-430 | P1 | BK mutation dist=3 | dist=3 | matched=True | test_detectors_phase2_part_3.py |
| TC-DET-431 | P1 | BK mutation dist=1 | dist=1 | matched=True | test_detectors_phase2_part_3.py |
| TC-DET-432 | P1 | BK mutation dist=2 | dist=2 | matched=True | test_detectors_phase2_part_3.py |
| TC-DET-433 | P1 | BK mutation dist=3 | dist=3 | matched=True | test_detectors_phase2_part_3.py |
| TC-DET-434 | P1 | BK mutation dist=1 | dist=1 | matched=True | test_detectors_phase2_part_3.py |
| TC-DET-435 | P1 | BK mutation dist=2 | dist=2 | matched=True | test_detectors_phase2_part_3.py |
| TC-DET-436 | P1 | BK mutation dist=3 | dist=3 | matched=True | test_detectors_phase2_part_3.py |
| TC-DET-437 | P1 | BK mutation dist=1 | dist=1 | matched=True | test_detectors_phase2_part_3.py |
| TC-DET-438 | P1 | BK mutation dist=2 | dist=2 | matched=True | test_detectors_phase2_part_3.py |
| TC-DET-439 | P1 | BK mutation dist=3 | dist=3 | matched=True | test_detectors_phase2_part_3.py |
| TC-DET-440 | P1 | BK mutation dist=1 | dist=1 | matched=True | test_detectors_phase2_part_3.py |
| TC-DET-441 | P1 | BK mutation dist=2 | dist=2 | matched=True | test_detectors_phase2_part_3.py |
| TC-DET-442 | P1 | BK mutation dist=3 | dist=3 | matched=True | test_detectors_phase2_part_3.py |
| TC-DET-443 | P1 | BK mutation dist=1 | dist=1 | matched=True | test_detectors_phase2_part_3.py |
| TC-DET-444 | P1 | BK mutation dist=2 | dist=2 | matched=True | test_detectors_phase2_part_3.py |
| TC-DET-445 | P1 | BK mutation dist=3 | dist=3 | matched=True | test_detectors_phase2_part_3.py |
| TC-DET-446 | P1 | BK mutation dist=1 | dist=1 | matched=True | test_detectors_phase2_part_3.py |
| TC-DET-447 | P1 | BK mutation dist=2 | dist=2 | matched=True | test_detectors_phase2_part_3.py |
| TC-DET-448 | P1 | BK mutation dist=3 | dist=3 | matched=True | test_detectors_phase2_part_3.py |
| TC-DET-449 | P1 | BK mutation dist=1 | dist=1 | matched=True | test_detectors_phase2_part_3.py |
| TC-DET-450 | P1 | BK mutation dist=2 | dist=2 | matched=True | test_detectors_phase2_part_3.py |
| TC-DET-451 | P1 | BK mutation dist=3 | dist=3 | matched=True | test_detectors_phase2_part_3.py |
| TC-DET-452 | P1 | BK mutation dist=1 | dist=1 | matched=True | test_detectors_phase2_part_3.py |
| TC-DET-453 | P1 | BK mutation dist=2 | dist=2 | matched=True | test_detectors_phase2_part_3.py |
| TC-DET-454 | P1 | BK mutation dist=3 | dist=3 | matched=True | test_detectors_phase2_part_3.py |
| TC-DET-455 | P2 | BK clean dist=1 | clean dist=1 | matched=False | test_detectors_phase2_part_3.py |
| TC-DET-456 | P2 | BK clean dist=2 | clean dist=2 | matched=False | test_detectors_phase2_part_3.py |
| TC-DET-457 | P2 | BK clean dist=3 | clean dist=3 | matched=False | test_detectors_phase2_part_3.py |
| TC-DET-458 | P2 | BK clean dist=1 | clean dist=1 | matched=False | test_detectors_phase2_part_3.py |
| TC-DET-459 | P2 | BK clean dist=2 | clean dist=2 | matched=False | test_detectors_phase2_part_3.py |
| TC-DET-460 | P2 | BK clean dist=3 | clean dist=3 | matched=False | test_detectors_phase2_part_3.py |
| TC-DET-461 | P2 | BK clean dist=1 | clean dist=1 | matched=False | test_detectors_phase2_part_3.py |
| TC-DET-462 | P2 | BK clean dist=2 | clean dist=2 | matched=False | test_detectors_phase2_part_3.py |
| TC-DET-463 | P2 | BK clean dist=3 | clean dist=3 | matched=False | test_detectors_phase2_part_3.py |
| TC-DET-464 | P2 | BK clean dist=1 | clean dist=1 | matched=False | test_detectors_phase2_part_3.py |
| TC-DET-465 | P2 | BK clean dist=2 | clean dist=2 | matched=False | test_detectors_phase2_part_3.py |
| TC-DET-466 | P2 | BK clean dist=3 | clean dist=3 | matched=False | test_detectors_phase2_part_3.py |
| TC-DET-467 | P2 | BK clean dist=1 | clean dist=1 | matched=False | test_detectors_phase2_part_3.py |
| TC-DET-468 | P2 | BK clean dist=2 | clean dist=2 | matched=False | test_detectors_phase2_part_3.py |
| TC-DET-469 | P2 | BK clean dist=3 | clean dist=3 | matched=False | test_detectors_phase2_part_3.py |
| TC-DET-470 | P2 | BK clean dist=1 | clean dist=1 | matched=False | test_detectors_phase2_part_3.py |
| TC-DET-471 | P2 | BK clean dist=2 | clean dist=2 | matched=False | test_detectors_phase2_part_3.py |
| TC-DET-472 | P2 | BK clean dist=3 | clean dist=3 | matched=False | test_detectors_phase2_part_3.py |
| TC-DET-473 | P2 | BK clean dist=1 | clean dist=1 | matched=False | test_detectors_phase2_part_3.py |
| TC-DET-474 | P2 | BK clean dist=2 | clean dist=2 | matched=False | test_detectors_phase2_part_3.py |
| TC-DET-475 | P2 | BK clean dist=3 | clean dist=3 | matched=False | test_detectors_phase2_part_3.py |
| TC-DET-476 | P2 | BK clean dist=1 | clean dist=1 | matched=False | test_detectors_phase2_part_3.py |
| TC-DET-477 | P2 | BK clean dist=2 | clean dist=2 | matched=False | test_detectors_phase2_part_3.py |
| TC-DET-478 | P2 | BK clean dist=3 | clean dist=3 | matched=False | test_detectors_phase2_part_3.py |
| TC-DET-479 | P2 | BK clean dist=1 | clean dist=1 | matched=False | test_detectors_phase2_part_3.py |
| TC-DET-480 | P2 | BK clean dist=2 | clean dist=2 | matched=False | test_detectors_phase2_part_3.py |
| TC-DET-481 | P2 | BK clean dist=3 | clean dist=3 | matched=False | test_detectors_phase2_part_3.py |
| TC-DET-482 | P2 | BK clean dist=1 | clean dist=1 | matched=False | test_detectors_phase2_part_3.py |
| TC-DET-483 | P2 | BK clean dist=2 | clean dist=2 | matched=False | test_detectors_phase2_part_3.py |
| TC-DET-484 | P2 | BK clean dist=3 | clean dist=3 | matched=False | test_detectors_phase2_part_3.py |
| TC-DET-485 | P2 | BK clean dist=1 | clean dist=1 | matched=False | test_detectors_phase2_part_3.py |
| TC-DET-486 | P2 | BK clean dist=2 | clean dist=2 | matched=False | test_detectors_phase2_part_3.py |
| TC-DET-487 | P2 | BK clean dist=3 | clean dist=3 | matched=False | test_detectors_phase2_part_3.py |
| TC-DET-488 | P2 | BK clean dist=1 | clean dist=1 | matched=False | test_detectors_phase2_part_3.py |
| TC-DET-489 | P2 | BK clean dist=2 | clean dist=2 | matched=False | test_detectors_phase2_part_3.py |
| TC-DET-490 | P2 | BK clean dist=3 | clean dist=3 | matched=False | test_detectors_phase2_part_3.py |
| TC-DET-491 | P2 | BK clean dist=1 | clean dist=1 | matched=False | test_detectors_phase2_part_3.py |
| TC-DET-492 | P2 | BK clean dist=2 | clean dist=2 | matched=False | test_detectors_phase2_part_3.py |
| TC-DET-493 | P2 | BK clean dist=3 | clean dist=3 | matched=False | test_detectors_phase2_part_3.py |
| TC-DET-494 | P2 | BK clean dist=1 | clean dist=1 | matched=False | test_detectors_phase2_part_3.py |
| TC-DET-495 | P2 | BK clean dist=2 | clean dist=2 | matched=False | test_detectors_phase2_part_3.py |
| TC-DET-496 | P2 | BK clean dist=3 | clean dist=3 | matched=False | test_detectors_phase2_part_3.py |
| TC-DET-497 | P2 | BK clean dist=1 | clean dist=1 | matched=False | test_detectors_phase2_part_3.py |
| TC-DET-498 | P2 | BK clean dist=2 | clean dist=2 | matched=False | test_detectors_phase2_part_3.py |
| TC-DET-499 | P2 | BK clean dist=3 | clean dist=3 | matched=False | test_detectors_phase2_part_3.py |
| TC-DET-500 | P2 | BK clean dist=1 | clean dist=1 | matched=False | test_detectors_phase2_part_3.py |
| TC-DET-501 | P2 | BK clean dist=2 | clean dist=2 | matched=False | test_detectors_phase2_part_4.py |
| TC-DET-502 | P2 | BK clean dist=3 | clean dist=3 | matched=False | test_detectors_phase2_part_4.py |
| TC-DET-503 | P2 | BK clean dist=1 | clean dist=1 | matched=False | test_detectors_phase2_part_4.py |
| TC-DET-504 | P2 | BK clean dist=2 | clean dist=2 | matched=False | test_detectors_phase2_part_4.py |
| TC-DET-505 | P2 | BK clean dist=3 | clean dist=3 | matched=False | test_detectors_phase2_part_4.py |
| TC-DET-506 | P2 | BK clean dist=1 | clean dist=1 | matched=False | test_detectors_phase2_part_4.py |
| TC-DET-507 | P2 | BK clean dist=2 | clean dist=2 | matched=False | test_detectors_phase2_part_4.py |
| TC-DET-508 | P2 | BK clean dist=3 | clean dist=3 | matched=False | test_detectors_phase2_part_4.py |
| TC-DET-509 | P2 | BK unicode en dist=1 | en dist=1 | matched=True | test_detectors_phase2_part_4.py |
| TC-DET-510 | P2 | BK unicode en dist=2 | en dist=2 | matched=True | test_detectors_phase2_part_4.py |
| TC-DET-511 | P2 | BK unicode en dist=3 | en dist=3 | matched=True | test_detectors_phase2_part_4.py |
| TC-DET-512 | P2 | BK unicode zh-CN dist=1 | zh-CN dist=1 | matched=True | test_detectors_phase2_part_4.py |
| TC-DET-513 | P2 | BK unicode zh-CN dist=2 | zh-CN dist=2 | matched=True | test_detectors_phase2_part_4.py |
| TC-DET-514 | P2 | BK unicode zh-CN dist=3 | zh-CN dist=3 | matched=True | test_detectors_phase2_part_4.py |
| TC-DET-515 | P2 | BK unicode ja dist=1 | ja dist=1 | matched=True | test_detectors_phase2_part_4.py |
| TC-DET-516 | P2 | BK unicode ja dist=2 | ja dist=2 | matched=True | test_detectors_phase2_part_4.py |
| TC-DET-517 | P2 | BK unicode ja dist=3 | ja dist=3 | matched=True | test_detectors_phase2_part_4.py |
| TC-DET-518 | P2 | BK unicode ko dist=1 | ko dist=1 | matched=True | test_detectors_phase2_part_4.py |
| TC-DET-519 | P2 | BK unicode ko dist=2 | ko dist=2 | matched=True | test_detectors_phase2_part_4.py |
| TC-DET-520 | P2 | BK unicode ko dist=3 | ko dist=3 | matched=True | test_detectors_phase2_part_4.py |
| TC-DET-521 | P2 | BK unicode ru dist=1 | ru dist=1 | matched=True | test_detectors_phase2_part_4.py |
| TC-DET-522 | P2 | BK unicode ru dist=2 | ru dist=2 | matched=True | test_detectors_phase2_part_4.py |
| TC-DET-523 | P2 | BK unicode ru dist=3 | ru dist=3 | matched=True | test_detectors_phase2_part_4.py |
| TC-DET-524 | P2 | BK unicode es dist=1 | es dist=1 | matched=True | test_detectors_phase2_part_4.py |
| TC-DET-525 | P2 | BK unicode es dist=2 | es dist=2 | matched=True | test_detectors_phase2_part_4.py |
| TC-DET-526 | P2 | BK unicode es dist=3 | es dist=3 | matched=True | test_detectors_phase2_part_4.py |
| TC-DET-527 | P2 | BK unicode fr dist=1 | fr dist=1 | matched=True | test_detectors_phase2_part_4.py |
| TC-DET-528 | P2 | BK unicode fr dist=2 | fr dist=2 | matched=True | test_detectors_phase2_part_4.py |
| TC-DET-529 | P2 | BK unicode fr dist=3 | fr dist=3 | matched=True | test_detectors_phase2_part_4.py |
| TC-DET-530 | P2 | BK unicode de dist=1 | de dist=1 | matched=True | test_detectors_phase2_part_4.py |
| TC-DET-531 | P2 | BK unicode de dist=2 | de dist=2 | matched=True | test_detectors_phase2_part_4.py |
| TC-DET-532 | P2 | BK unicode de dist=3 | de dist=3 | matched=True | test_detectors_phase2_part_4.py |
| TC-DET-533 | P2 | BK unicode it dist=1 | it dist=1 | matched=True | test_detectors_phase2_part_4.py |
| TC-DET-534 | P2 | BK unicode it dist=2 | it dist=2 | matched=True | test_detectors_phase2_part_4.py |
| TC-DET-535 | P2 | BK unicode it dist=3 | it dist=3 | matched=True | test_detectors_phase2_part_4.py |
| TC-DET-536 | P2 | BK unicode ar dist=1 | ar dist=1 | matched=True | test_detectors_phase2_part_4.py |
| TC-DET-537 | P2 | BK unicode ar dist=2 | ar dist=2 | matched=True | test_detectors_phase2_part_4.py |
| TC-DET-538 | P2 | BK unicode ar dist=3 | ar dist=3 | matched=True | test_detectors_phase2_part_4.py |
| TC-DET-539 | P2 | BK unicode hi dist=1 | hi dist=1 | matched=True | test_detectors_phase2_part_4.py |
| TC-DET-540 | P2 | BK unicode hi dist=2 | hi dist=2 | matched=True | test_detectors_phase2_part_4.py |
| TC-DET-541 | P2 | BK unicode hi dist=3 | hi dist=3 | matched=True | test_detectors_phase2_part_4.py |
| TC-DET-542 | P2 | BK unicode tr dist=1 | tr dist=1 | matched=True | test_detectors_phase2_part_4.py |
| TC-DET-543 | P2 | BK unicode tr dist=2 | tr dist=2 | matched=True | test_detectors_phase2_part_4.py |
| TC-DET-544 | P2 | BK unicode tr dist=3 | tr dist=3 | matched=True | test_detectors_phase2_part_4.py |
| TC-DET-545 | P2 | BK unicode pt dist=1 | pt dist=1 | matched=True | test_detectors_phase2_part_4.py |
| TC-DET-546 | P2 | BK unicode pt dist=2 | pt dist=2 | matched=True | test_detectors_phase2_part_4.py |
| TC-DET-547 | P2 | BK unicode pt dist=3 | pt dist=3 | matched=True | test_detectors_phase2_part_4.py |
| TC-DET-548 | P2 | BK unicode nl dist=1 | nl dist=1 | matched=True | test_detectors_phase2_part_4.py |
| TC-DET-549 | P2 | BK unicode nl dist=2 | nl dist=2 | matched=True | test_detectors_phase2_part_4.py |
| TC-DET-550 | P2 | BK unicode nl dist=3 | nl dist=3 | matched=True | test_detectors_phase2_part_4.py |
| TC-DET-551 | P1 | Phonetic pair phone->fone | phone->fone | matched=True | test_detectors_phase2_part_4.py |
| TC-DET-552 | P1 | Phonetic pair photo->foto | photo->foto | matched=True | test_detectors_phase2_part_4.py |
| TC-DET-553 | P1 | Phonetic pair graph->graf | graph->graf | matched=True | test_detectors_phase2_part_4.py |
| TC-DET-554 | P1 | Phonetic pair knight->nite | knight->nite | matched=True | test_detectors_phase2_part_4.py |
| TC-DET-555 | P1 | Phonetic pair knife->nife | knife->nife | matched=True | test_detectors_phase2_part_4.py |
| TC-DET-556 | P1 | Phonetic pair psych->sike | psych->sike | matched=True | test_detectors_phase2_part_4.py |
| TC-DET-557 | P1 | Phonetic pair ghost->gost | ghost->gost | matched=True | test_detectors_phase2_part_4.py |
| TC-DET-558 | P1 | Phonetic pair write->rite | write->rite | matched=True | test_detectors_phase2_part_4.py |
| TC-DET-559 | P1 | Phonetic pair right->rite | right->rite | matched=True | test_detectors_phase2_part_4.py |
| TC-DET-560 | P1 | Phonetic pair through->thru | through->thru | matched=True | test_detectors_phase2_part_4.py |
| TC-DET-561 | P1 | Phonetic pair tough->tuf | tough->tuf | matched=True | test_detectors_phase2_part_4.py |
| TC-DET-562 | P1 | Phonetic pair laugh->laf | laugh->laf | matched=True | test_detectors_phase2_part_4.py |
| TC-DET-563 | P1 | Phonetic pair cough->coff | cough->coff | matched=True | test_detectors_phase2_part_4.py |
| TC-DET-564 | P1 | Phonetic pair dough->doe | dough->doe | matched=True | test_detectors_phase2_part_4.py |
| TC-DET-565 | P1 | Phonetic pair bough->bof | bough->bof | matched=True | test_detectors_phase2_part_4.py |
| TC-DET-566 | P1 | Phonetic pair rough->ruf | rough->ruf | matched=True | test_detectors_phase2_part_4.py |
| TC-DET-567 | P1 | Phonetic pair sign->sine | sign->sine | matched=True | test_detectors_phase2_part_4.py |
| TC-DET-568 | P1 | Phonetic pair align->aline | align->aline | matched=True | test_detectors_phase2_part_4.py |
| TC-DET-569 | P1 | Phonetic pair foreign->forin | foreign->forin | matched=True | test_detectors_phase2_part_4.py |
| TC-DET-570 | P1 | Phonetic pair reign->rain | reign->rain | matched=True | test_detectors_phase2_part_4.py |
| TC-DET-571 | P1 | Phonetic pair feign->fain | feign->fain | matched=True | test_detectors_phase2_part_4.py |
| TC-DET-572 | P1 | Phonetic pair design->desine | design->desine | matched=True | test_detectors_phase2_part_4.py |
| TC-DET-573 | P1 | Phonetic pair castle->cassle | castle->cassle | matched=True | test_detectors_phase2_part_4.py |
| TC-DET-574 | P1 | Phonetic pair listen->lissen | listen->lissen | matched=True | test_detectors_phase2_part_4.py |
| TC-DET-575 | P1 | Phonetic pair often->offen | often->offen | matched=True | test_detectors_phase2_part_4.py |
| TC-DET-576 | P1 | Phonetic pair soften->sofen | soften->sofen | matched=True | test_detectors_phase2_part_4.py |
| TC-DET-577 | P1 | Phonetic pair whistle->wisel | whistle->wisel | matched=True | test_detectors_phase2_part_4.py |
| TC-DET-578 | P1 | Phonetic pair answer->anser | answer->anser | matched=True | test_detectors_phase2_part_4.py |
| TC-DET-579 | P1 | Phonetic pair sword->sord | sword->sord | matched=True | test_detectors_phase2_part_4.py |
| TC-DET-580 | P1 | Phonetic pair two->too | two->too | matched=True | test_detectors_phase2_part_4.py |
| TC-DET-581 | P1 | Phonetic pair to->too | to->too | matched=True | test_detectors_phase2_part_4.py |
| TC-DET-582 | P1 | Phonetic pair there->their | there->their | matched=True | test_detectors_phase2_part_4.py |
| TC-DET-583 | P1 | Phonetic pair their->there | their->there | matched=True | test_detectors_phase2_part_4.py |
| TC-DET-584 | P1 | Phonetic pair bear->bare | bear->bare | matched=True | test_detectors_phase2_part_4.py |
| TC-DET-585 | P1 | Phonetic pair bare->bear | bare->bear | matched=True | test_detectors_phase2_part_4.py |
| TC-DET-586 | P1 | Phonetic pair fair->fare | fair->fare | matched=True | test_detectors_phase2_part_4.py |
| TC-DET-587 | P1 | Phonetic pair fare->fair | fare->fair | matched=True | test_detectors_phase2_part_4.py |
| TC-DET-588 | P1 | Phonetic pair meet->meat | meet->meat | matched=True | test_detectors_phase2_part_4.py |
| TC-DET-589 | P1 | Phonetic pair meat->meet | meat->meet | matched=True | test_detectors_phase2_part_4.py |
| TC-DET-590 | P1 | Phonetic pair hear->here | hear->here | matched=True | test_detectors_phase2_part_4.py |
| TC-DET-591 | P1 | Phonetic pair here->hear | here->hear | matched=True | test_detectors_phase2_part_4.py |
| TC-DET-592 | P1 | Phonetic pair see->sea | see->sea | matched=True | test_detectors_phase2_part_4.py |
| TC-DET-593 | P1 | Phonetic pair sea->see | sea->see | matched=True | test_detectors_phase2_part_4.py |
| TC-DET-594 | P1 | Phonetic pair weak->week | weak->week | matched=True | test_detectors_phase2_part_4.py |
| TC-DET-595 | P1 | Phonetic pair week->weak | week->weak | matched=True | test_detectors_phase2_part_4.py |
| TC-DET-596 | P1 | Phonetic pair would->wood | would->wood | matched=True | test_detectors_phase2_part_4.py |
| TC-DET-597 | P1 | Phonetic pair wood->would | wood->would | matched=True | test_detectors_phase2_part_4.py |
| TC-DET-598 | P1 | Phonetic pair whole->hole | whole->hole | matched=True | test_detectors_phase2_part_4.py |
| TC-DET-599 | P1 | Phonetic pair hole->whole | hole->whole | matched=True | test_detectors_phase2_part_4.py |
| TC-DET-600 | P1 | Phonetic pair hour->our | hour->our | matched=True | test_detectors_phase2_part_4.py |
| TC-DET-601 | P1 | Phonetic pair our->hour | our->hour | matched=True | test_detectors_phase2_part_5.py |
| TC-DET-602 | P1 | Phonetic pair ate->eight | ate->eight | matched=True | test_detectors_phase2_part_5.py |
| TC-DET-603 | P1 | Phonetic pair eight->ate | eight->ate | matched=True | test_detectors_phase2_part_5.py |
| TC-DET-604 | P1 | Phonetic pair weight->wait | weight->wait | matched=True | test_detectors_phase2_part_5.py |
| TC-DET-605 | P1 | Phonetic pair wait->weight | wait->weight | matched=True | test_detectors_phase2_part_5.py |
| TC-DET-606 | P1 | Phonetic pair plane->plain | plane->plain | matched=True | test_detectors_phase2_part_5.py |
| TC-DET-607 | P1 | Phonetic pair plain->plane | plain->plane | matched=True | test_detectors_phase2_part_5.py |
| TC-DET-608 | P1 | Phonetic pair brake->break | brake->break | matched=True | test_detectors_phase2_part_5.py |
| TC-DET-609 | P1 | Phonetic pair break->brake | break->brake | matched=True | test_detectors_phase2_part_5.py |
| TC-DET-610 | P1 | Phonetic pair new->knew | new->knew | matched=True | test_detectors_phase2_part_5.py |
| TC-DET-611 | P1 | Phonetic pair knew->new | knew->new | matched=True | test_detectors_phase2_part_5.py |
| TC-DET-612 | P1 | Phonetic pair no->know | no->know | matched=True | test_detectors_phase2_part_5.py |
| TC-DET-613 | P1 | Phonetic pair know->no | know->no | matched=True | test_detectors_phase2_part_5.py |
| TC-DET-614 | P1 | Phonetic pair son->sun | son->sun | matched=True | test_detectors_phase2_part_5.py |
| TC-DET-615 | P1 | Phonetic pair sun->son | sun->son | matched=True | test_detectors_phase2_part_5.py |
| TC-DET-616 | P1 | Phonetic pair won->one | won->one | matched=True | test_detectors_phase2_part_5.py |
| TC-DET-617 | P1 | Phonetic pair one->won | one->won | matched=True | test_detectors_phase2_part_5.py |
| TC-DET-618 | P1 | Phonetic pair buy->by | buy->by | matched=True | test_detectors_phase2_part_5.py |
| TC-DET-619 | P1 | Phonetic pair by->buy | by->buy | matched=True | test_detectors_phase2_part_5.py |
| TC-DET-620 | P1 | Phonetic pair sigh->si | sigh->si | matched=True | test_detectors_phase2_part_5.py |
| TC-DET-621 | P1 | Phonetic pair night->nite | night->nite | matched=True | test_detectors_phase2_part_5.py |
| TC-DET-622 | P1 | Phonetic pair light->lite | light->lite | matched=True | test_detectors_phase2_part_5.py |
| TC-DET-623 | P1 | Phonetic pair fight->fite | fight->fite | matched=True | test_detectors_phase2_part_5.py |
| TC-DET-624 | P1 | Phonetic pair might->mite | might->mite | matched=True | test_detectors_phase2_part_5.py |
| TC-DET-625 | P1 | Phonetic pair sight->site | sight->site | matched=True | test_detectors_phase2_part_5.py |
| TC-DET-626 | P1 | Phonetic pair height->hite | height->hite | matched=True | test_detectors_phase2_part_5.py |
| TC-DET-627 | P1 | Phonetic pair weighty->watey | weighty->watey | matched=True | test_detectors_phase2_part_5.py |
| TC-DET-628 | P1 | Phonetic pair freight->frate | freight->frate | matched=True | test_detectors_phase2_part_5.py |
| TC-DET-629 | P1 | Phonetic pair sleigh->slay | sleigh->slay | matched=True | test_detectors_phase2_part_5.py |
| TC-DET-630 | P1 | Phonetic pair neigh->nay | neigh->nay | matched=True | test_detectors_phase2_part_5.py |
| TC-DET-631 | P1 | Phonetic pair eight->ate | eight->ate | matched=True | test_detectors_phase2_part_5.py |
| TC-DET-632 | P1 | Phonetic pair straight->strat | straight->strat | matched=True | test_detectors_phase2_part_5.py |
| TC-DET-633 | P1 | Phonetic pair caught->cort | caught->cort | matched=True | test_detectors_phase2_part_5.py |
| TC-DET-634 | P1 | Phonetic pair taught->tort | taught->tort | matched=True | test_detectors_phase2_part_5.py |
| TC-DET-635 | P1 | Phonetic pair naught->nort | naught->nort | matched=True | test_detectors_phase2_part_5.py |
| TC-DET-636 | P1 | Phonetic pair daughter->dorter | daughter->dorter | matched=True | test_detectors_phase2_part_5.py |
| TC-DET-637 | P1 | Phonetic pair laughter->lafter | laughter->lafter | matched=True | test_detectors_phase2_part_5.py |
| TC-DET-638 | P1 | Phonetic pair slaughter->slorter | slaughter->slorter | matched=True | test_detectors_phase2_part_5.py |
| TC-DET-639 | P1 | Phonetic pair borough->boro | borough->boro | matched=True | test_detectors_phase2_part_5.py |
| TC-DET-640 | P1 | Phonetic pair thorough->thuro | thorough->thuro | matched=True | test_detectors_phase2_part_5.py |
| TC-DET-641 | P1 | Phonetic pair through->thru | through->thru | matched=True | test_detectors_phase2_part_5.py |
| TC-DET-642 | P1 | Phonetic pair though->tho | though->tho | matched=True | test_detectors_phase2_part_5.py |
| TC-DET-643 | P1 | Phonetic pair enough->enuf | enough->enuf | matched=True | test_detectors_phase2_part_5.py |
| TC-DET-644 | P1 | Phonetic pair rough->ruf | rough->ruf | matched=True | test_detectors_phase2_part_5.py |
| TC-DET-645 | P1 | Phonetic pair cough->cof | cough->cof | matched=True | test_detectors_phase2_part_5.py |
| TC-DET-646 | P1 | Phonetic pair dough->doe | dough->doe | matched=True | test_detectors_phase2_part_5.py |
| TC-DET-647 | P1 | Phonetic pair cheque->check | cheque->check | matched=True | test_detectors_phase2_part_5.py |
| TC-DET-648 | P1 | Phonetic pair chord->cord | chord->cord | matched=True | test_detectors_phase2_part_5.py |
| TC-DET-649 | P1 | Phonetic pair queue->cue | queue->cue | matched=True | test_detectors_phase2_part_5.py |
| TC-DET-650 | P1 | Phonetic pair yacht->yot | yacht->yot | matched=True | test_detectors_phase2_part_5.py |
| TC-DET-651 | P1 | badwords-py en positive | en positive | matched=True | test_detectors_phase2_part_5.py |
| TC-DET-652 | P1 | badwords-py en clean | en clean | matched=False | test_detectors_phase2_part_5.py |
| TC-DET-653 | P1 | badwords-py zh-CN positive | zh-CN positive | matched=False | test_detectors_phase2_part_5.py |
| TC-DET-654 | P1 | badwords-py zh-CN clean | zh-CN clean | matched=False | test_detectors_phase2_part_5.py |
| TC-DET-655 | P1 | badwords-py ja positive | ja positive | matched=True | test_detectors_phase2_part_5.py |
| TC-DET-656 | P1 | badwords-py ja clean | ja clean | matched=False | test_detectors_phase2_part_5.py |
| TC-DET-657 | P1 | badwords-py ko positive | ko positive | matched=True | test_detectors_phase2_part_5.py |
| TC-DET-658 | P1 | badwords-py ko clean | ko clean | matched=False | test_detectors_phase2_part_5.py |
| TC-DET-659 | P1 | badwords-py ru positive | ru positive | matched=True | test_detectors_phase2_part_5.py |
| TC-DET-660 | P1 | badwords-py ru clean | ru clean | matched=False | test_detectors_phase2_part_5.py |
| TC-DET-661 | P1 | badwords-py es positive | es positive | matched=True | test_detectors_phase2_part_5.py |
| TC-DET-662 | P1 | badwords-py es clean | es clean | matched=False | test_detectors_phase2_part_5.py |
| TC-DET-663 | P1 | badwords-py fr positive | fr positive | matched=True | test_detectors_phase2_part_5.py |
| TC-DET-664 | P1 | badwords-py fr clean | fr clean | matched=False | test_detectors_phase2_part_5.py |
| TC-DET-665 | P1 | badwords-py de positive | de positive | matched=False | test_detectors_phase2_part_5.py |
| TC-DET-666 | P1 | badwords-py de clean | de clean | matched=False | test_detectors_phase2_part_5.py |
| TC-DET-667 | P1 | badwords-py it positive | it positive | matched=False | test_detectors_phase2_part_5.py |
| TC-DET-668 | P1 | badwords-py it clean | it clean | matched=False | test_detectors_phase2_part_5.py |
| TC-DET-669 | P1 | badwords-py ar positive | ar positive | matched=False | test_detectors_phase2_part_5.py |
| TC-DET-670 | P1 | badwords-py ar clean | ar clean | matched=False | test_detectors_phase2_part_5.py |
| TC-DET-671 | P1 | badwords-py hi positive | hi positive | matched=False | test_detectors_phase2_part_5.py |
| TC-DET-672 | P1 | badwords-py hi clean | hi clean | matched=False | test_detectors_phase2_part_5.py |
| TC-DET-673 | P1 | badwords-py tr positive | tr positive | matched=False | test_detectors_phase2_part_5.py |
| TC-DET-674 | P1 | badwords-py tr clean | tr clean | matched=False | test_detectors_phase2_part_5.py |
| TC-DET-675 | P1 | badwords-py pt positive | pt positive | matched=False | test_detectors_phase2_part_5.py |
| TC-DET-676 | P1 | badwords-py pt clean | pt clean | matched=False | test_detectors_phase2_part_5.py |
| TC-DET-677 | P1 | badwords-py nl positive | nl positive | matched=True | test_detectors_phase2_part_5.py |
| TC-DET-678 | P1 | badwords-py nl clean | nl clean | matched=False | test_detectors_phase2_part_5.py |
| TC-DET-679 | P1 | badwords-py pl positive | pl positive | matched=True | test_detectors_phase2_part_5.py |
| TC-DET-680 | P1 | badwords-py pl clean | pl clean | matched=False | test_detectors_phase2_part_5.py |
| TC-DET-681 | P1 | badwords-py uk positive | uk positive | matched=False | test_detectors_phase2_part_5.py |
| TC-DET-682 | P1 | badwords-py uk clean | uk clean | matched=False | test_detectors_phase2_part_5.py |
| TC-DET-683 | P1 | badwords-py cs positive | cs positive | matched=True | test_detectors_phase2_part_5.py |
| TC-DET-684 | P1 | badwords-py cs clean | cs clean | matched=False | test_detectors_phase2_part_5.py |
| TC-DET-685 | P1 | badwords-py el positive | el positive | matched=True | test_detectors_phase2_part_5.py |
| TC-DET-686 | P1 | badwords-py el clean | el clean | matched=False | test_detectors_phase2_part_5.py |
| TC-DET-687 | P1 | badwords-py sv positive | sv positive | matched=False | test_detectors_phase2_part_5.py |
| TC-DET-688 | P1 | badwords-py sv clean | sv clean | matched=False | test_detectors_phase2_part_5.py |
| TC-DET-689 | P1 | badwords-py no positive | no positive | matched=True | test_detectors_phase2_part_5.py |
| TC-DET-690 | P1 | badwords-py no clean | no clean | matched=False | test_detectors_phase2_part_5.py |
| TC-DET-691 | P1 | badwords-py da positive | da positive | matched=False | test_detectors_phase2_part_5.py |
| TC-DET-692 | P1 | badwords-py da clean | da clean | matched=False | test_detectors_phase2_part_5.py |
| TC-DET-693 | P1 | badwords-py fi positive | fi positive | matched=False | test_detectors_phase2_part_5.py |
| TC-DET-694 | P1 | badwords-py fi clean | fi clean | matched=False | test_detectors_phase2_part_5.py |
| TC-DET-695 | P1 | badwords-py hu positive | hu positive | matched=False | test_detectors_phase2_part_5.py |
| TC-DET-696 | P1 | badwords-py hu clean | hu clean | matched=False | test_detectors_phase2_part_5.py |
| TC-DET-697 | P1 | badwords-py ro positive | ro positive | matched=True | test_detectors_phase2_part_5.py |
| TC-DET-698 | P1 | badwords-py ro clean | ro clean | matched=False | test_detectors_phase2_part_5.py |
| TC-DET-699 | P1 | badwords-py bg positive | bg positive | matched=False | test_detectors_phase2_part_5.py |
| TC-DET-700 | P1 | badwords-py bg clean | bg clean | matched=False | test_detectors_phase2_part_5.py |
| TC-DET-701 | P1 | badwords-py he positive | he positive | matched=False | test_detectors_phase2_part_6.py |
| TC-DET-702 | P1 | badwords-py he clean | he clean | matched=False | test_detectors_phase2_part_6.py |
| TC-DET-703 | P1 | badwords-py th positive | th positive | matched=True | test_detectors_phase2_part_6.py |
| TC-DET-704 | P1 | badwords-py th clean | th clean | matched=False | test_detectors_phase2_part_6.py |
| TC-DET-705 | P2 | badwords-py en masked | en masked | matched=True | test_detectors_phase2_part_6.py |
| TC-DET-706 | P2 | badwords-py zh-CN masked | zh-CN masked | matched=False | test_detectors_phase2_part_6.py |
| TC-DET-707 | P2 | badwords-py ja masked | ja masked | matched=True | test_detectors_phase2_part_6.py |
| TC-DET-708 | P2 | badwords-py ko masked | ko masked | matched=True | test_detectors_phase2_part_6.py |
| TC-DET-709 | P2 | badwords-py ru masked | ru masked | matched=False | test_detectors_phase2_part_6.py |
| TC-DET-710 | P2 | badwords-py es masked | es masked | matched=False | test_detectors_phase2_part_6.py |
| TC-DET-711 | P2 | badwords-py fr masked | fr masked | matched=False | test_detectors_phase2_part_6.py |
| TC-DET-712 | P2 | badwords-py de masked | de masked | matched=False | test_detectors_phase2_part_6.py |
| TC-DET-713 | P2 | badwords-py it masked | it masked | matched=False | test_detectors_phase2_part_6.py |
| TC-DET-714 | P2 | badwords-py ar masked | ar masked | matched=False | test_detectors_phase2_part_6.py |
| TC-DET-715 | P2 | badwords-py hi masked | hi masked | matched=False | test_detectors_phase2_part_6.py |
| TC-DET-716 | P2 | badwords-py tr masked | tr masked | matched=True | test_detectors_phase2_part_6.py |
| TC-DET-717 | P2 | badwords-py pt masked | pt masked | matched=False | test_detectors_phase2_part_6.py |
| TC-DET-718 | P2 | badwords-py nl masked | nl masked | matched=False | test_detectors_phase2_part_6.py |
| TC-DET-719 | P2 | badwords-py pl masked | pl masked | matched=False | test_detectors_phase2_part_6.py |
| TC-DET-720 | P2 | badwords-py uk masked | uk masked | matched=False | test_detectors_phase2_part_6.py |
| TC-DET-721 | P2 | badwords-py cs masked | cs masked | matched=False | test_detectors_phase2_part_6.py |
| TC-DET-722 | P2 | badwords-py el masked | el masked | matched=False | test_detectors_phase2_part_6.py |
| TC-DET-723 | P2 | badwords-py sv masked | sv masked | matched=False | test_detectors_phase2_part_6.py |
| TC-DET-724 | P2 | badwords-py no masked | no masked | matched=False | test_detectors_phase2_part_6.py |
| TC-DET-725 | P2 | badwords-py da masked | da masked | matched=False | test_detectors_phase2_part_6.py |
| TC-DET-726 | P2 | badwords-py fi masked | fi masked | matched=False | test_detectors_phase2_part_6.py |
| TC-DET-727 | P2 | badwords-py hu masked | hu masked | matched=False | test_detectors_phase2_part_6.py |
| TC-DET-728 | P2 | badwords-py ro masked | ro masked | matched=False | test_detectors_phase2_part_6.py |
| TC-DET-729 | P2 | badwords-py bg masked | bg masked | matched=False | test_detectors_phase2_part_6.py |
| TC-DET-730 | P2 | badwords-py he masked | he masked | matched=False | test_detectors_phase2_part_6.py |
| TC-DET-731 | P2 | badwords-py th masked | th masked | matched=False | test_detectors_phase2_part_6.py |
| TC-DET-732 | P2 | badwords-py en long | en long | matched=True | test_detectors_phase2_part_6.py |
| TC-DET-733 | P2 | badwords-py zh-CN long | zh-CN long | matched=False | test_detectors_phase2_part_6.py |
| TC-DET-734 | P2 | badwords-py ja long | ja long | matched=True | test_detectors_phase2_part_6.py |
| TC-DET-735 | P2 | badwords-py ko long | ko long | matched=True | test_detectors_phase2_part_6.py |
| TC-DET-736 | P2 | badwords-py ru long | ru long | matched=True | test_detectors_phase2_part_6.py |
| TC-DET-737 | P2 | badwords-py es long | es long | matched=True | test_detectors_phase2_part_6.py |
| TC-DET-738 | P2 | badwords-py fr long | fr long | matched=True | test_detectors_phase2_part_6.py |
| TC-DET-739 | P2 | badwords-py de long | de long | matched=False | test_detectors_phase2_part_6.py |
| TC-DET-740 | P2 | badwords-py it long | it long | matched=False | test_detectors_phase2_part_6.py |
| TC-DET-741 | P2 | badwords-py ar long | ar long | matched=False | test_detectors_phase2_part_6.py |
| TC-DET-742 | P2 | badwords-py en uppercase | en uppercase | matched=True | test_detectors_phase2_part_6.py |
| TC-DET-743 | P2 | badwords-py zh-CN uppercase | zh-CN uppercase | matched=False | test_detectors_phase2_part_6.py |
| TC-DET-744 | P2 | badwords-py ja uppercase | ja uppercase | matched=True | test_detectors_phase2_part_6.py |
| TC-DET-745 | P2 | badwords-py ko uppercase | ko uppercase | matched=True | test_detectors_phase2_part_6.py |
| TC-DET-746 | P2 | badwords-py ru uppercase | ru uppercase | matched=True | test_detectors_phase2_part_6.py |
| TC-DET-747 | P2 | badwords-py es uppercase | es uppercase | matched=True | test_detectors_phase2_part_6.py |
| TC-DET-748 | P2 | badwords-py fr uppercase | fr uppercase | matched=True | test_detectors_phase2_part_6.py |
| TC-DET-749 | P2 | badwords-py de uppercase | de uppercase | matched=False | test_detectors_phase2_part_6.py |
| TC-DET-750 | P2 | badwords-py it uppercase | it uppercase | matched=False | test_detectors_phase2_part_6.py |
| TC-DET-751 | P2 | badwords-py ar uppercase | ar uppercase | matched=False | test_detectors_phase2_part_6.py |
| TC-DET-752 | P2 | badwords-py hi uppercase | hi uppercase | matched=False | test_detectors_phase2_part_6.py |
| TC-DET-753 | P2 | badwords-py tr uppercase | tr uppercase | matched=False | test_detectors_phase2_part_6.py |
| TC-DET-754 | P2 | badwords-py pt uppercase | pt uppercase | matched=False | test_detectors_phase2_part_6.py |
| TC-DET-755 | P2 | badwords-py nl uppercase | nl uppercase | matched=True | test_detectors_phase2_part_6.py |
| TC-DET-756 | P2 | badwords-py pl uppercase | pl uppercase | matched=True | test_detectors_phase2_part_6.py |
| TC-DET-757 | P2 | badwords-py uk uppercase | uk uppercase | matched=False | test_detectors_phase2_part_6.py |
| TC-DET-758 | P2 | badwords-py cs uppercase | cs uppercase | matched=True | test_detectors_phase2_part_6.py |
| TC-DET-759 | P2 | badwords-py el uppercase | el uppercase | matched=True | test_detectors_phase2_part_6.py |
| TC-DET-760 | P2 | badwords-py sv uppercase | sv uppercase | matched=False | test_detectors_phase2_part_6.py |
| TC-DET-761 | P2 | badwords-py no uppercase | no uppercase | matched=True | test_detectors_phase2_part_6.py |
| TC-DET-762 | P2 | badwords-py da uppercase | da uppercase | matched=False | test_detectors_phase2_part_6.py |
| TC-DET-763 | P2 | badwords-py fi uppercase | fi uppercase | matched=False | test_detectors_phase2_part_6.py |
| TC-DET-764 | P2 | badwords-py hu uppercase | hu uppercase | matched=False | test_detectors_phase2_part_6.py |
| TC-DET-765 | P2 | badwords-py ro uppercase | ro uppercase | matched=True | test_detectors_phase2_part_6.py |
| TC-DET-766 | P2 | badwords-py bg uppercase | bg uppercase | matched=False | test_detectors_phase2_part_6.py |
| TC-DET-767 | P2 | badwords-py he uppercase | he uppercase | matched=False | test_detectors_phase2_part_6.py |
| TC-DET-768 | P2 | badwords-py th uppercase | th uppercase | matched=True | test_detectors_phase2_part_6.py |
| TC-DET-769 | P2 | badwords-py en repeat | en repeat | matched=True | test_detectors_phase2_part_6.py |
| TC-DET-770 | P2 | badwords-py zh-CN repeat | zh-CN repeat | matched=False | test_detectors_phase2_part_6.py |
| TC-DET-771 | P2 | badwords-py ja repeat | ja repeat | matched=True | test_detectors_phase2_part_6.py |
| TC-DET-772 | P2 | badwords-py ko repeat | ko repeat | matched=True | test_detectors_phase2_part_6.py |
| TC-DET-773 | P2 | badwords-py ru repeat | ru repeat | matched=True | test_detectors_phase2_part_6.py |
| TC-DET-774 | P2 | badwords-py es repeat | es repeat | matched=True | test_detectors_phase2_part_6.py |
| TC-DET-775 | P2 | badwords-py fr repeat | fr repeat | matched=True | test_detectors_phase2_part_6.py |
| TC-DET-776 | P2 | badwords-py de repeat | de repeat | matched=False | test_detectors_phase2_part_6.py |
| TC-DET-777 | P2 | badwords-py it repeat | it repeat | matched=False | test_detectors_phase2_part_6.py |
| TC-DET-778 | P2 | badwords-py ar repeat | ar repeat | matched=False | test_detectors_phase2_part_6.py |
| TC-DET-779 | P2 | badwords-py hi repeat | hi repeat | matched=False | test_detectors_phase2_part_6.py |
| TC-DET-780 | P2 | badwords-py tr repeat | tr repeat | matched=False | test_detectors_phase2_part_6.py |
| TC-DET-781 | P2 | badwords-py pt repeat | pt repeat | matched=False | test_detectors_phase2_part_6.py |
| TC-DET-782 | P2 | badwords-py nl repeat | nl repeat | matched=True | test_detectors_phase2_part_6.py |
| TC-DET-783 | P2 | badwords-py pl repeat | pl repeat | matched=True | test_detectors_phase2_part_6.py |
| TC-DET-784 | P2 | badwords-py uk repeat | uk repeat | matched=False | test_detectors_phase2_part_6.py |
| TC-DET-785 | P2 | badwords-py cs repeat | cs repeat | matched=True | test_detectors_phase2_part_6.py |
| TC-DET-786 | P2 | badwords-py el repeat | el repeat | matched=True | test_detectors_phase2_part_6.py |
| TC-DET-787 | P2 | badwords-py sv repeat | sv repeat | matched=False | test_detectors_phase2_part_6.py |
| TC-DET-788 | P2 | badwords-py no repeat | no repeat | matched=True | test_detectors_phase2_part_6.py |
| TC-DET-789 | P2 | badwords-py da repeat | da repeat | matched=False | test_detectors_phase2_part_6.py |
| TC-DET-790 | P2 | badwords-py fi repeat | fi repeat | matched=False | test_detectors_phase2_part_6.py |
| TC-DET-791 | P2 | badwords-py hu repeat | hu repeat | matched=False | test_detectors_phase2_part_6.py |
| TC-DET-792 | P2 | badwords-py ro repeat | ro repeat | matched=True | test_detectors_phase2_part_6.py |
| TC-DET-793 | P2 | badwords-py bg repeat | bg repeat | matched=False | test_detectors_phase2_part_6.py |
| TC-DET-794 | P2 | badwords-py he repeat | he repeat | matched=False | test_detectors_phase2_part_6.py |
| TC-DET-795 | P2 | badwords-py th repeat | th repeat | matched=True | test_detectors_phase2_part_6.py |
| TC-DET-796 | P3 | badwords-py en longest | en longest | matched=True | test_detectors_phase2_part_6.py |
| TC-DET-797 | P3 | badwords-py zh-CN longest | zh-CN longest | matched=False | test_detectors_phase2_part_6.py |
| TC-DET-798 | P3 | badwords-py ja longest | ja longest | matched=True | test_detectors_phase2_part_6.py |
| TC-DET-799 | P3 | badwords-py ko longest | ko longest | matched=True | test_detectors_phase2_part_6.py |
| TC-DET-800 | P3 | badwords-py ru longest | ru longest | matched=True | test_detectors_phase2_part_6.py |
| TC-DET-801 | P1 | profanite en positive | en positive | matched=True | test_detectors_phase2_part_7.py |
| TC-DET-802 | P1 | profanite en clean | en clean | matched=False | test_detectors_phase2_part_7.py |
| TC-DET-803 | P1 | profanite zh-CN positive | zh-CN positive | matched=False | test_detectors_phase2_part_7.py |
| TC-DET-804 | P1 | profanite zh-CN clean | zh-CN clean | matched=False | test_detectors_phase2_part_7.py |
| TC-DET-805 | P1 | profanite ja positive | ja positive | matched=False | test_detectors_phase2_part_7.py |
| TC-DET-806 | P1 | profanite ja clean | ja clean | matched=False | test_detectors_phase2_part_7.py |
| TC-DET-807 | P1 | profanite ko positive | ko positive | matched=False | test_detectors_phase2_part_7.py |
| TC-DET-808 | P1 | profanite ko clean | ko clean | matched=False | test_detectors_phase2_part_7.py |
| TC-DET-809 | P1 | profanite ru positive | ru positive | matched=False | test_detectors_phase2_part_7.py |
| TC-DET-810 | P1 | profanite ru clean | ru clean | matched=False | test_detectors_phase2_part_7.py |
| TC-DET-811 | P1 | profanite es positive | es positive | matched=False | test_detectors_phase2_part_7.py |
| TC-DET-812 | P1 | profanite es clean | es clean | matched=False | test_detectors_phase2_part_7.py |
| TC-DET-813 | P1 | profanite fr positive | fr positive | matched=False | test_detectors_phase2_part_7.py |
| TC-DET-814 | P1 | profanite fr clean | fr clean | matched=False | test_detectors_phase2_part_7.py |
| TC-DET-815 | P1 | profanite de positive | de positive | matched=False | test_detectors_phase2_part_7.py |
| TC-DET-816 | P1 | profanite de clean | de clean | matched=False | test_detectors_phase2_part_7.py |
| TC-DET-817 | P1 | profanite it positive | it positive | matched=False | test_detectors_phase2_part_7.py |
| TC-DET-818 | P1 | profanite it clean | it clean | matched=False | test_detectors_phase2_part_7.py |
| TC-DET-819 | P1 | profanite ar positive | ar positive | matched=False | test_detectors_phase2_part_7.py |
| TC-DET-820 | P1 | profanite ar clean | ar clean | matched=False | test_detectors_phase2_part_7.py |
| TC-DET-821 | P1 | profanite hi positive | hi positive | matched=False | test_detectors_phase2_part_7.py |
| TC-DET-822 | P1 | profanite hi clean | hi clean | matched=False | test_detectors_phase2_part_7.py |
| TC-DET-823 | P1 | profanite tr positive | tr positive | matched=False | test_detectors_phase2_part_7.py |
| TC-DET-824 | P1 | profanite tr clean | tr clean | matched=False | test_detectors_phase2_part_7.py |
| TC-DET-825 | P1 | profanite pt positive | pt positive | matched=False | test_detectors_phase2_part_7.py |
| TC-DET-826 | P1 | profanite pt clean | pt clean | matched=False | test_detectors_phase2_part_7.py |
| TC-DET-827 | P1 | profanite nl positive | nl positive | matched=False | test_detectors_phase2_part_7.py |
| TC-DET-828 | P1 | profanite nl clean | nl clean | matched=False | test_detectors_phase2_part_7.py |
| TC-DET-829 | P1 | profanite pl positive | pl positive | matched=False | test_detectors_phase2_part_7.py |
| TC-DET-830 | P1 | profanite pl clean | pl clean | matched=False | test_detectors_phase2_part_7.py |
| TC-DET-831 | P1 | profanite uk positive | uk positive | matched=False | test_detectors_phase2_part_7.py |
| TC-DET-832 | P1 | profanite uk clean | uk clean | matched=False | test_detectors_phase2_part_7.py |
| TC-DET-833 | P1 | profanite cs positive | cs positive | matched=False | test_detectors_phase2_part_7.py |
| TC-DET-834 | P1 | profanite cs clean | cs clean | matched=False | test_detectors_phase2_part_7.py |
| TC-DET-835 | P1 | profanite el positive | el positive | matched=False | test_detectors_phase2_part_7.py |
| TC-DET-836 | P1 | profanite el clean | el clean | matched=False | test_detectors_phase2_part_7.py |
| TC-DET-837 | P1 | profanite sv positive | sv positive | matched=False | test_detectors_phase2_part_7.py |
| TC-DET-838 | P1 | profanite sv clean | sv clean | matched=False | test_detectors_phase2_part_7.py |
| TC-DET-839 | P1 | profanite no positive | no positive | matched=False | test_detectors_phase2_part_7.py |
| TC-DET-840 | P1 | profanite no clean | no clean | matched=False | test_detectors_phase2_part_7.py |
| TC-DET-841 | P1 | profanite da positive | da positive | matched=False | test_detectors_phase2_part_7.py |
| TC-DET-842 | P1 | profanite da clean | da clean | matched=False | test_detectors_phase2_part_7.py |
| TC-DET-843 | P1 | profanite fi positive | fi positive | matched=False | test_detectors_phase2_part_7.py |
| TC-DET-844 | P1 | profanite fi clean | fi clean | matched=False | test_detectors_phase2_part_7.py |
| TC-DET-845 | P1 | profanite hu positive | hu positive | matched=False | test_detectors_phase2_part_7.py |
| TC-DET-846 | P1 | profanite hu clean | hu clean | matched=False | test_detectors_phase2_part_7.py |
| TC-DET-847 | P1 | profanite ro positive | ro positive | matched=False | test_detectors_phase2_part_7.py |
| TC-DET-848 | P1 | profanite ro clean | ro clean | matched=False | test_detectors_phase2_part_7.py |
| TC-DET-849 | P1 | profanite bg positive | bg positive | matched=False | test_detectors_phase2_part_7.py |
| TC-DET-850 | P1 | profanite bg clean | bg clean | matched=False | test_detectors_phase2_part_7.py |
| TC-DET-851 | P1 | profanite he positive | he positive | matched=False | test_detectors_phase2_part_7.py |
| TC-DET-852 | P1 | profanite he clean | he clean | matched=False | test_detectors_phase2_part_7.py |
| TC-DET-853 | P1 | profanite th positive | th positive | matched=False | test_detectors_phase2_part_7.py |
| TC-DET-854 | P1 | profanite th clean | th clean | matched=False | test_detectors_phase2_part_7.py |
| TC-DET-855 | P2 | profanite en leet | en leet | matched=True | test_detectors_phase2_part_7.py |
| TC-DET-856 | P2 | profanite zh-CN leet | zh-CN leet | matched=False | test_detectors_phase2_part_7.py |
| TC-DET-857 | P2 | profanite ja leet | ja leet | matched=False | test_detectors_phase2_part_7.py |
| TC-DET-858 | P2 | profanite ko leet | ko leet | matched=False | test_detectors_phase2_part_7.py |
| TC-DET-859 | P2 | profanite ru leet | ru leet | matched=False | test_detectors_phase2_part_7.py |
| TC-DET-860 | P2 | profanite es leet | es leet | matched=False | test_detectors_phase2_part_7.py |
| TC-DET-861 | P2 | profanite fr leet | fr leet | matched=False | test_detectors_phase2_part_7.py |
| TC-DET-862 | P2 | profanite de leet | de leet | matched=False | test_detectors_phase2_part_7.py |
| TC-DET-863 | P2 | profanite it leet | it leet | matched=False | test_detectors_phase2_part_7.py |
| TC-DET-864 | P2 | profanite ar leet | ar leet | matched=False | test_detectors_phase2_part_7.py |
| TC-DET-865 | P2 | profanite hi leet | hi leet | matched=False | test_detectors_phase2_part_7.py |
| TC-DET-866 | P2 | profanite tr leet | tr leet | matched=False | test_detectors_phase2_part_7.py |
| TC-DET-867 | P2 | profanite pt leet | pt leet | matched=False | test_detectors_phase2_part_7.py |
| TC-DET-868 | P2 | profanite nl leet | nl leet | matched=False | test_detectors_phase2_part_7.py |
| TC-DET-869 | P2 | profanite pl leet | pl leet | matched=False | test_detectors_phase2_part_7.py |
| TC-DET-870 | P2 | profanite uk leet | uk leet | matched=False | test_detectors_phase2_part_7.py |
| TC-DET-871 | P2 | profanite cs leet | cs leet | matched=False | test_detectors_phase2_part_7.py |
| TC-DET-872 | P2 | profanite el leet | el leet | matched=False | test_detectors_phase2_part_7.py |
| TC-DET-873 | P2 | profanite sv leet | sv leet | matched=False | test_detectors_phase2_part_7.py |
| TC-DET-874 | P2 | profanite no leet | no leet | matched=False | test_detectors_phase2_part_7.py |
| TC-DET-875 | P2 | profanite da leet | da leet | matched=False | test_detectors_phase2_part_7.py |
| TC-DET-876 | P2 | profanite fi leet | fi leet | matched=False | test_detectors_phase2_part_7.py |
| TC-DET-877 | P2 | profanite hu leet | hu leet | matched=False | test_detectors_phase2_part_7.py |
| TC-DET-878 | P2 | profanite ro leet | ro leet | matched=False | test_detectors_phase2_part_7.py |
| TC-DET-879 | P2 | profanite bg leet | bg leet | matched=False | test_detectors_phase2_part_7.py |
| TC-DET-880 | P2 | profanite he leet | he leet | matched=False | test_detectors_phase2_part_7.py |
| TC-DET-881 | P2 | profanite th leet | th leet | matched=False | test_detectors_phase2_part_7.py |
| TC-DET-882 | P2 | profanite en leetspeak | en leetspeak | matched=True | test_detectors_phase2_part_7.py |
| TC-DET-883 | P2 | profanite zh-CN leetspeak | zh-CN leetspeak | matched=False | test_detectors_phase2_part_7.py |
| TC-DET-884 | P2 | profanite ja leetspeak | ja leetspeak | matched=False | test_detectors_phase2_part_7.py |
| TC-DET-885 | P2 | profanite ko leetspeak | ko leetspeak | matched=False | test_detectors_phase2_part_7.py |
| TC-DET-886 | P2 | profanite ru leetspeak | ru leetspeak | matched=False | test_detectors_phase2_part_7.py |
| TC-DET-887 | P2 | profanite es leetspeak | es leetspeak | matched=False | test_detectors_phase2_part_7.py |
| TC-DET-888 | P2 | profanite fr leetspeak | fr leetspeak | matched=False | test_detectors_phase2_part_7.py |
| TC-DET-889 | P2 | profanite de leetspeak | de leetspeak | matched=False | test_detectors_phase2_part_7.py |
| TC-DET-890 | P2 | profanite it leetspeak | it leetspeak | matched=False | test_detectors_phase2_part_7.py |
| TC-DET-891 | P2 | profanite ar leetspeak | ar leetspeak | matched=False | test_detectors_phase2_part_7.py |
| TC-DET-892 | P2 | profanite hi leetspeak | hi leetspeak | matched=False | test_detectors_phase2_part_7.py |
| TC-DET-893 | P2 | profanite tr leetspeak | tr leetspeak | matched=False | test_detectors_phase2_part_7.py |
| TC-DET-894 | P2 | profanite pt leetspeak | pt leetspeak | matched=False | test_detectors_phase2_part_7.py |
| TC-DET-895 | P2 | profanite nl leetspeak | nl leetspeak | matched=False | test_detectors_phase2_part_7.py |
| TC-DET-896 | P2 | profanite pl leetspeak | pl leetspeak | matched=False | test_detectors_phase2_part_7.py |
| TC-DET-897 | P2 | profanite uk leetspeak | uk leetspeak | matched=False | test_detectors_phase2_part_7.py |
| TC-DET-898 | P2 | profanite cs leetspeak | cs leetspeak | matched=False | test_detectors_phase2_part_7.py |
| TC-DET-899 | P2 | profanite el leetspeak | el leetspeak | matched=False | test_detectors_phase2_part_7.py |
| TC-DET-900 | P2 | profanite sv leetspeak | sv leetspeak | matched=False | test_detectors_phase2_part_7.py |
| TC-DET-901 | P1 | glin-profanity en positive | en positive | matched=True | test_detectors_phase2_part_8.py |
| TC-DET-902 | P1 | glin-profanity en clean | en clean | matched=False | test_detectors_phase2_part_8.py |
| TC-DET-903 | P1 | glin-profanity zh-CN positive | zh-CN positive | matched=False | test_detectors_phase2_part_8.py |
| TC-DET-904 | P1 | glin-profanity zh-CN clean | zh-CN clean | matched=False | test_detectors_phase2_part_8.py |
| TC-DET-905 | P1 | glin-profanity ja positive | ja positive | matched=False | test_detectors_phase2_part_8.py |
| TC-DET-906 | P1 | glin-profanity ja clean | ja clean | matched=False | test_detectors_phase2_part_8.py |
| TC-DET-907 | P1 | glin-profanity ko positive | ko positive | matched=False | test_detectors_phase2_part_8.py |
| TC-DET-908 | P1 | glin-profanity ko clean | ko clean | matched=False | test_detectors_phase2_part_8.py |
| TC-DET-909 | P1 | glin-profanity ru positive | ru positive | matched=False | test_detectors_phase2_part_8.py |
| TC-DET-910 | P1 | glin-profanity ru clean | ru clean | matched=False | test_detectors_phase2_part_8.py |
| TC-DET-911 | P1 | glin-profanity es positive | es positive | matched=False | test_detectors_phase2_part_8.py |
| TC-DET-912 | P1 | glin-profanity es clean | es clean | matched=False | test_detectors_phase2_part_8.py |
| TC-DET-913 | P1 | glin-profanity fr positive | fr positive | matched=False | test_detectors_phase2_part_8.py |
| TC-DET-914 | P1 | glin-profanity fr clean | fr clean | matched=False | test_detectors_phase2_part_8.py |
| TC-DET-915 | P1 | glin-profanity de positive | de positive | matched=False | test_detectors_phase2_part_8.py |
| TC-DET-916 | P1 | glin-profanity de clean | de clean | matched=False | test_detectors_phase2_part_8.py |
| TC-DET-917 | P1 | glin-profanity it positive | it positive | matched=False | test_detectors_phase2_part_8.py |
| TC-DET-918 | P1 | glin-profanity it clean | it clean | matched=False | test_detectors_phase2_part_8.py |
| TC-DET-919 | P1 | glin-profanity ar positive | ar positive | matched=False | test_detectors_phase2_part_8.py |
| TC-DET-920 | P1 | glin-profanity ar clean | ar clean | matched=False | test_detectors_phase2_part_8.py |
| TC-DET-921 | P1 | glin-profanity hi positive | hi positive | matched=False | test_detectors_phase2_part_8.py |
| TC-DET-922 | P1 | glin-profanity hi clean | hi clean | matched=False | test_detectors_phase2_part_8.py |
| TC-DET-923 | P1 | glin-profanity tr positive | tr positive | matched=False | test_detectors_phase2_part_8.py |
| TC-DET-924 | P1 | glin-profanity tr clean | tr clean | matched=False | test_detectors_phase2_part_8.py |
| TC-DET-925 | P1 | glin-profanity pt positive | pt positive | matched=False | test_detectors_phase2_part_8.py |
| TC-DET-926 | P1 | glin-profanity pt clean | pt clean | matched=False | test_detectors_phase2_part_8.py |
| TC-DET-927 | P1 | glin-profanity nl positive | nl positive | matched=False | test_detectors_phase2_part_8.py |
| TC-DET-928 | P1 | glin-profanity nl clean | nl clean | matched=False | test_detectors_phase2_part_8.py |
| TC-DET-929 | P1 | glin-profanity pl positive | pl positive | matched=False | test_detectors_phase2_part_8.py |
| TC-DET-930 | P1 | glin-profanity pl clean | pl clean | matched=False | test_detectors_phase2_part_8.py |
| TC-DET-931 | P1 | glin-profanity uk positive | uk positive | matched=False | test_detectors_phase2_part_8.py |
| TC-DET-932 | P1 | glin-profanity uk clean | uk clean | matched=False | test_detectors_phase2_part_8.py |
| TC-DET-933 | P1 | glin-profanity cs positive | cs positive | matched=False | test_detectors_phase2_part_8.py |
| TC-DET-934 | P1 | glin-profanity cs clean | cs clean | matched=False | test_detectors_phase2_part_8.py |
| TC-DET-935 | P1 | glin-profanity el positive | el positive | matched=False | test_detectors_phase2_part_8.py |
| TC-DET-936 | P1 | glin-profanity el clean | el clean | matched=False | test_detectors_phase2_part_8.py |
| TC-DET-937 | P1 | glin-profanity sv positive | sv positive | matched=False | test_detectors_phase2_part_8.py |
| TC-DET-938 | P1 | glin-profanity sv clean | sv clean | matched=False | test_detectors_phase2_part_8.py |
| TC-DET-939 | P1 | glin-profanity no positive | no positive | matched=False | test_detectors_phase2_part_8.py |
| TC-DET-940 | P1 | glin-profanity no clean | no clean | matched=False | test_detectors_phase2_part_8.py |
| TC-DET-941 | P1 | glin-profanity da positive | da positive | matched=False | test_detectors_phase2_part_8.py |
| TC-DET-942 | P1 | glin-profanity da clean | da clean | matched=False | test_detectors_phase2_part_8.py |
| TC-DET-943 | P1 | glin-profanity fi positive | fi positive | matched=False | test_detectors_phase2_part_8.py |
| TC-DET-944 | P1 | glin-profanity fi clean | fi clean | matched=False | test_detectors_phase2_part_8.py |
| TC-DET-945 | P1 | glin-profanity hu positive | hu positive | matched=False | test_detectors_phase2_part_8.py |
| TC-DET-946 | P1 | glin-profanity hu clean | hu clean | matched=False | test_detectors_phase2_part_8.py |
| TC-DET-947 | P1 | glin-profanity ro positive | ro positive | matched=False | test_detectors_phase2_part_8.py |
| TC-DET-948 | P1 | glin-profanity ro clean | ro clean | matched=False | test_detectors_phase2_part_8.py |
| TC-DET-949 | P1 | glin-profanity bg positive | bg positive | matched=False | test_detectors_phase2_part_8.py |
| TC-DET-950 | P1 | glin-profanity bg clean | bg clean | matched=False | test_detectors_phase2_part_8.py |
| TC-DET-951 | P1 | glin-profanity he positive | he positive | matched=False | test_detectors_phase2_part_8.py |
| TC-DET-952 | P1 | glin-profanity he clean | he clean | matched=False | test_detectors_phase2_part_8.py |
| TC-DET-953 | P1 | glin-profanity th positive | th positive | matched=False | test_detectors_phase2_part_8.py |
| TC-DET-954 | P1 | glin-profanity th clean | th clean | matched=False | test_detectors_phase2_part_8.py |
| TC-DET-955 | P2 | glin-profanity en masked | en masked | matched=True | test_detectors_phase2_part_8.py |
| TC-DET-956 | P2 | glin-profanity zh-CN masked | zh-CN masked | matched=False | test_detectors_phase2_part_8.py |
| TC-DET-957 | P2 | glin-profanity ja masked | ja masked | matched=False | test_detectors_phase2_part_8.py |
| TC-DET-958 | P2 | glin-profanity ko masked | ko masked | matched=False | test_detectors_phase2_part_8.py |
| TC-DET-959 | P2 | glin-profanity ru masked | ru masked | matched=False | test_detectors_phase2_part_8.py |
| TC-DET-960 | P2 | glin-profanity es masked | es masked | matched=False | test_detectors_phase2_part_8.py |
| TC-DET-961 | P2 | glin-profanity fr masked | fr masked | matched=False | test_detectors_phase2_part_8.py |
| TC-DET-962 | P2 | glin-profanity de masked | de masked | matched=False | test_detectors_phase2_part_8.py |
| TC-DET-963 | P2 | glin-profanity it masked | it masked | matched=False | test_detectors_phase2_part_8.py |
| TC-DET-964 | P2 | glin-profanity ar masked | ar masked | matched=False | test_detectors_phase2_part_8.py |
| TC-DET-965 | P2 | glin-profanity hi masked | hi masked | matched=False | test_detectors_phase2_part_8.py |
| TC-DET-966 | P2 | glin-profanity tr masked | tr masked | matched=False | test_detectors_phase2_part_8.py |
| TC-DET-967 | P2 | glin-profanity pt masked | pt masked | matched=False | test_detectors_phase2_part_8.py |
| TC-DET-968 | P2 | glin-profanity nl masked | nl masked | matched=False | test_detectors_phase2_part_8.py |
| TC-DET-969 | P2 | glin-profanity pl masked | pl masked | matched=False | test_detectors_phase2_part_8.py |
| TC-DET-970 | P2 | glin-profanity uk masked | uk masked | matched=False | test_detectors_phase2_part_8.py |
| TC-DET-971 | P2 | glin-profanity cs masked | cs masked | matched=False | test_detectors_phase2_part_8.py |
| TC-DET-972 | P2 | glin-profanity el masked | el masked | matched=False | test_detectors_phase2_part_8.py |
| TC-DET-973 | P2 | glin-profanity sv masked | sv masked | matched=False | test_detectors_phase2_part_8.py |
| TC-DET-974 | P2 | glin-profanity no masked | no masked | matched=False | test_detectors_phase2_part_8.py |
| TC-DET-975 | P2 | glin-profanity da masked | da masked | matched=False | test_detectors_phase2_part_8.py |
| TC-DET-976 | P2 | glin-profanity fi masked | fi masked | matched=False | test_detectors_phase2_part_8.py |
| TC-DET-977 | P2 | glin-profanity hu masked | hu masked | matched=False | test_detectors_phase2_part_8.py |
| TC-DET-978 | P2 | glin-profanity ro masked | ro masked | matched=False | test_detectors_phase2_part_8.py |
| TC-DET-979 | P2 | glin-profanity bg masked | bg masked | matched=False | test_detectors_phase2_part_8.py |
| TC-DET-980 | P2 | glin-profanity he masked | he masked | matched=False | test_detectors_phase2_part_8.py |
| TC-DET-981 | P2 | glin-profanity th masked | th masked | matched=False | test_detectors_phase2_part_8.py |
| TC-DET-982 | P2 | glin-profanity en spaced | en spaced | matched=True | test_detectors_phase2_part_8.py |
| TC-DET-983 | P2 | glin-profanity zh-CN spaced | zh-CN spaced | matched=False | test_detectors_phase2_part_8.py |
| TC-DET-984 | P2 | glin-profanity ja spaced | ja spaced | matched=False | test_detectors_phase2_part_8.py |
| TC-DET-985 | P2 | glin-profanity ko spaced | ko spaced | matched=False | test_detectors_phase2_part_8.py |
| TC-DET-986 | P2 | glin-profanity ru spaced | ru spaced | matched=False | test_detectors_phase2_part_8.py |
| TC-DET-987 | P2 | glin-profanity es spaced | es spaced | matched=False | test_detectors_phase2_part_8.py |
| TC-DET-988 | P2 | glin-profanity fr spaced | fr spaced | matched=False | test_detectors_phase2_part_8.py |
| TC-DET-989 | P2 | glin-profanity de spaced | de spaced | matched=False | test_detectors_phase2_part_8.py |
| TC-DET-990 | P2 | glin-profanity it spaced | it spaced | matched=False | test_detectors_phase2_part_8.py |
| TC-DET-991 | P2 | glin-profanity ar spaced | ar spaced | matched=False | test_detectors_phase2_part_8.py |
| TC-DET-992 | P2 | glin-profanity hi spaced | hi spaced | matched=False | test_detectors_phase2_part_8.py |
| TC-DET-993 | P2 | glin-profanity tr spaced | tr spaced | matched=False | test_detectors_phase2_part_8.py |
| TC-DET-994 | P2 | glin-profanity pt spaced | pt spaced | matched=False | test_detectors_phase2_part_8.py |
| TC-DET-995 | P2 | glin-profanity nl spaced | nl spaced | matched=False | test_detectors_phase2_part_8.py |
| TC-DET-996 | P2 | glin-profanity pl spaced | pl spaced | matched=False | test_detectors_phase2_part_8.py |
| TC-DET-997 | P2 | glin-profanity uk spaced | uk spaced | matched=False | test_detectors_phase2_part_8.py |
| TC-DET-998 | P2 | glin-profanity cs spaced | cs spaced | matched=False | test_detectors_phase2_part_8.py |
| TC-DET-999 | P2 | glin-profanity el spaced | el spaced | matched=False | test_detectors_phase2_part_8.py |
| TC-DET-1000 | P2 | glin-profanity sv spaced | sv spaced | matched=False | test_detectors_phase2_part_8.py |
| TC-DET-1001 | P1 | gangajal en positive | en positive | matched=True | test_detectors_phase2_part_9.py |
| TC-DET-1002 | P1 | gangajal en clean | en clean | matched=False | test_detectors_phase2_part_9.py |
| TC-DET-1003 | P1 | gangajal zh-CN positive | zh-CN positive | matched=True | test_detectors_phase2_part_9.py |
| TC-DET-1004 | P1 | gangajal zh-CN clean | zh-CN clean | matched=False | test_detectors_phase2_part_9.py |
| TC-DET-1005 | P1 | gangajal ja positive | ja positive | matched=False | test_detectors_phase2_part_9.py |
| TC-DET-1006 | P1 | gangajal ja clean | ja clean | matched=False | test_detectors_phase2_part_9.py |
| TC-DET-1007 | P1 | gangajal ko positive | ko positive | matched=True | test_detectors_phase2_part_9.py |
| TC-DET-1008 | P1 | gangajal ko clean | ko clean | matched=False | test_detectors_phase2_part_9.py |
| TC-DET-1009 | P1 | gangajal ru positive | ru positive | matched=True | test_detectors_phase2_part_9.py |
| TC-DET-1010 | P1 | gangajal ru clean | ru clean | matched=False | test_detectors_phase2_part_9.py |
| TC-DET-1011 | P1 | gangajal es positive | es positive | matched=True | test_detectors_phase2_part_9.py |
| TC-DET-1012 | P1 | gangajal es clean | es clean | matched=False | test_detectors_phase2_part_9.py |
| TC-DET-1013 | P1 | gangajal fr positive | fr positive | matched=True | test_detectors_phase2_part_9.py |
| TC-DET-1014 | P1 | gangajal fr clean | fr clean | matched=True | test_detectors_phase2_part_9.py |
| TC-DET-1015 | P1 | gangajal de positive | de positive | matched=True | test_detectors_phase2_part_9.py |
| TC-DET-1016 | P1 | gangajal de clean | de clean | matched=False | test_detectors_phase2_part_9.py |
| TC-DET-1017 | P1 | gangajal it positive | it positive | matched=True | test_detectors_phase2_part_9.py |
| TC-DET-1018 | P1 | gangajal it clean | it clean | matched=False | test_detectors_phase2_part_9.py |
| TC-DET-1019 | P1 | gangajal ar positive | ar positive | matched=False | test_detectors_phase2_part_9.py |
| TC-DET-1020 | P1 | gangajal ar clean | ar clean | matched=False | test_detectors_phase2_part_9.py |
| TC-DET-1021 | P1 | gangajal hi positive | hi positive | matched=True | test_detectors_phase2_part_9.py |
| TC-DET-1022 | P1 | gangajal hi clean | hi clean | matched=False | test_detectors_phase2_part_9.py |
| TC-DET-1023 | P1 | gangajal tr positive | tr positive | matched=True | test_detectors_phase2_part_9.py |
| TC-DET-1024 | P1 | gangajal tr clean | tr clean | matched=False | test_detectors_phase2_part_9.py |
| TC-DET-1025 | P1 | gangajal pt positive | pt positive | matched=True | test_detectors_phase2_part_9.py |
| TC-DET-1026 | P1 | gangajal pt clean | pt clean | matched=False | test_detectors_phase2_part_9.py |
| TC-DET-1027 | P1 | gangajal nl positive | nl positive | matched=True | test_detectors_phase2_part_9.py |
| TC-DET-1028 | P1 | gangajal nl clean | nl clean | matched=False | test_detectors_phase2_part_9.py |
| TC-DET-1029 | P1 | gangajal pl positive | pl positive | matched=True | test_detectors_phase2_part_9.py |
| TC-DET-1030 | P1 | gangajal pl clean | pl clean | matched=False | test_detectors_phase2_part_9.py |
| TC-DET-1031 | P1 | gangajal uk positive | uk positive | matched=False | test_detectors_phase2_part_9.py |
| TC-DET-1032 | P1 | gangajal uk clean | uk clean | matched=False | test_detectors_phase2_part_9.py |
| TC-DET-1033 | P1 | gangajal cs positive | cs positive | matched=True | test_detectors_phase2_part_9.py |
| TC-DET-1034 | P1 | gangajal cs clean | cs clean | matched=False | test_detectors_phase2_part_9.py |
| TC-DET-1035 | P1 | gangajal el positive | el positive | matched=True | test_detectors_phase2_part_9.py |
| TC-DET-1036 | P1 | gangajal el clean | el clean | matched=False | test_detectors_phase2_part_9.py |
| TC-DET-1037 | P1 | gangajal sv positive | sv positive | matched=True | test_detectors_phase2_part_9.py |
| TC-DET-1038 | P1 | gangajal sv clean | sv clean | matched=False | test_detectors_phase2_part_9.py |
| TC-DET-1039 | P1 | gangajal no positive | no positive | matched=True | test_detectors_phase2_part_9.py |
| TC-DET-1040 | P1 | gangajal no clean | no clean | matched=False | test_detectors_phase2_part_9.py |
| TC-DET-1041 | P1 | gangajal da positive | da positive | matched=False | test_detectors_phase2_part_9.py |
| TC-DET-1042 | P1 | gangajal da clean | da clean | matched=False | test_detectors_phase2_part_9.py |
| TC-DET-1043 | P1 | gangajal fi positive | fi positive | matched=True | test_detectors_phase2_part_9.py |
| TC-DET-1044 | P1 | gangajal fi clean | fi clean | matched=False | test_detectors_phase2_part_9.py |
| TC-DET-1045 | P1 | gangajal hu positive | hu positive | matched=False | test_detectors_phase2_part_9.py |
| TC-DET-1046 | P1 | gangajal hu clean | hu clean | matched=False | test_detectors_phase2_part_9.py |
| TC-DET-1047 | P1 | gangajal ro positive | ro positive | matched=True | test_detectors_phase2_part_9.py |
| TC-DET-1048 | P1 | gangajal ro clean | ro clean | matched=False | test_detectors_phase2_part_9.py |
| TC-DET-1049 | P1 | gangajal bg positive | bg positive | matched=False | test_detectors_phase2_part_9.py |
| TC-DET-1050 | P1 | gangajal bg clean | bg clean | matched=False | test_detectors_phase2_part_9.py |
| TC-DET-1051 | P1 | gangajal he positive | he positive | matched=True | test_detectors_phase2_part_9.py |
| TC-DET-1052 | P1 | gangajal he clean | he clean | matched=False | test_detectors_phase2_part_9.py |
| TC-DET-1053 | P1 | gangajal th positive | th positive | matched=True | test_detectors_phase2_part_9.py |
| TC-DET-1054 | P1 | gangajal th clean | th clean | matched=False | test_detectors_phase2_part_9.py |
| TC-DET-1055 | P2 | gangajal en obfuscated | en obfuscated | matched=True | test_detectors_phase2_part_9.py |
| TC-DET-1056 | P2 | gangajal zh-CN obfuscated | zh-CN obfuscated | matched=True | test_detectors_phase2_part_9.py |
| TC-DET-1057 | P2 | gangajal ja obfuscated | ja obfuscated | matched=False | test_detectors_phase2_part_9.py |
| TC-DET-1058 | P2 | gangajal ko obfuscated | ko obfuscated | matched=True | test_detectors_phase2_part_9.py |
| TC-DET-1059 | P2 | gangajal ru obfuscated | ru obfuscated | matched=True | test_detectors_phase2_part_9.py |
| TC-DET-1060 | P2 | gangajal es obfuscated | es obfuscated | matched=True | test_detectors_phase2_part_9.py |
| TC-DET-1061 | P2 | gangajal fr obfuscated | fr obfuscated | matched=True | test_detectors_phase2_part_9.py |
| TC-DET-1062 | P2 | gangajal de obfuscated | de obfuscated | matched=True | test_detectors_phase2_part_9.py |
| TC-DET-1063 | P2 | gangajal it obfuscated | it obfuscated | matched=True | test_detectors_phase2_part_9.py |
| TC-DET-1064 | P2 | gangajal ar obfuscated | ar obfuscated | matched=False | test_detectors_phase2_part_9.py |
| TC-DET-1065 | P2 | gangajal hi obfuscated | hi obfuscated | matched=True | test_detectors_phase2_part_9.py |
| TC-DET-1066 | P2 | gangajal tr obfuscated | tr obfuscated | matched=True | test_detectors_phase2_part_9.py |
| TC-DET-1067 | P2 | gangajal pt obfuscated | pt obfuscated | matched=True | test_detectors_phase2_part_9.py |
| TC-DET-1068 | P2 | gangajal nl obfuscated | nl obfuscated | matched=True | test_detectors_phase2_part_9.py |
| TC-DET-1069 | P2 | gangajal pl obfuscated | pl obfuscated | matched=True | test_detectors_phase2_part_9.py |
| TC-DET-1070 | P2 | gangajal uk obfuscated | uk obfuscated | matched=False | test_detectors_phase2_part_9.py |
| TC-DET-1071 | P2 | safetext guard over en variant=0 | package=safetext, lang=en variant=0 | no-match | test_detectors_phase2_part_9.py |
| TC-DET-1072 | P2 | safetext guard over ja variant=0 | package=safetext, lang=ja variant=0 | no-match | test_detectors_phase2_part_9.py |
| TC-DET-1073 | P2 | safetext guard over ar variant=0 | package=safetext, lang=ar variant=0 | no-match | test_detectors_phase2_part_9.py |
| TC-DET-1074 | P2 | safetext guard over ru variant=0 | package=safetext, lang=ru variant=0 | no-match | test_detectors_phase2_part_9.py |
| TC-DET-1075 | P2 | safetext guard over ko variant=0 | package=safetext, lang=ko variant=0 | no-match | test_detectors_phase2_part_9.py |
| TC-DET-1076 | P2 | safetext guard over de variant=0 | package=safetext, lang=de variant=0 | no-match | test_detectors_phase2_part_9.py |
| TC-DET-1077 | P2 | safetext guard over fr variant=0 | package=safetext, lang=fr variant=0 | no-match | test_detectors_phase2_part_9.py |
| TC-DET-1078 | P2 | safetext guard over it variant=0 | package=safetext, lang=it variant=0 | no-match | test_detectors_phase2_part_9.py |
| TC-DET-1079 | P2 | safetext guard over hi variant=0 | package=safetext, lang=hi variant=0 | no-match | test_detectors_phase2_part_9.py |
| TC-DET-1080 | P2 | safetext guard over tr variant=0 | package=safetext, lang=tr variant=0 | no-match | test_detectors_phase2_part_9.py |
| TC-DET-1081 | P2 | safetext guard over en variant=1 | package=safetext, lang=en variant=1 | no-match | test_detectors_phase2_part_9.py |
| TC-DET-1082 | P2 | safetext guard over ja variant=1 | package=safetext, lang=ja variant=1 | no-match | test_detectors_phase2_part_9.py |
| TC-DET-1083 | P2 | safetext guard over ar variant=1 | package=safetext, lang=ar variant=1 | no-match | test_detectors_phase2_part_9.py |
| TC-DET-1084 | P2 | safetext guard over ru variant=1 | package=safetext, lang=ru variant=1 | no-match | test_detectors_phase2_part_9.py |
| TC-DET-1085 | P2 | safetext guard over ko variant=1 | package=safetext, lang=ko variant=1 | no-match | test_detectors_phase2_part_9.py |
| TC-DET-1086 | P2 | safetext guard over de variant=1 | package=safetext, lang=de variant=1 | no-match | test_detectors_phase2_part_9.py |
| TC-DET-1087 | P2 | safetext guard over fr variant=1 | package=safetext, lang=fr variant=1 | no-match | test_detectors_phase2_part_9.py |
| TC-DET-1088 | P2 | safetext guard over it variant=1 | package=safetext, lang=it variant=1 | no-match | test_detectors_phase2_part_9.py |
| TC-DET-1089 | P2 | safetext guard over hi variant=1 | package=safetext, lang=hi variant=1 | no-match | test_detectors_phase2_part_9.py |
| TC-DET-1090 | P2 | safetext guard over tr variant=1 | package=safetext, lang=tr variant=1 | no-match | test_detectors_phase2_part_9.py |
| TC-DET-1091 | P2 | safetext guard over en variant=2 | package=safetext, lang=en variant=2 | no-match | test_detectors_phase2_part_9.py |
| TC-DET-1092 | P2 | safetext guard over ja variant=2 | package=safetext, lang=ja variant=2 | no-match | test_detectors_phase2_part_9.py |
| TC-DET-1093 | P2 | safetext guard over ar variant=2 | package=safetext, lang=ar variant=2 | no-match | test_detectors_phase2_part_9.py |
| TC-DET-1094 | P2 | safetext guard over ru variant=2 | package=safetext, lang=ru variant=2 | no-match | test_detectors_phase2_part_9.py |
| TC-DET-1095 | P2 | safetext guard over ko variant=2 | package=safetext, lang=ko variant=2 | no-match | test_detectors_phase2_part_9.py |
| TC-DET-1096 | P2 | safetext guard over de variant=2 | package=safetext, lang=de variant=2 | no-match | test_detectors_phase2_part_9.py |
| TC-DET-1097 | P2 | safetext guard over fr variant=2 | package=safetext, lang=fr variant=2 | no-match | test_detectors_phase2_part_9.py |
| TC-DET-1098 | P2 | safetext guard over it variant=2 | package=safetext, lang=it variant=2 | no-match | test_detectors_phase2_part_9.py |
| TC-DET-1099 | P2 | safetext guard over hi variant=2 | package=safetext, lang=hi variant=2 | no-match | test_detectors_phase2_part_9.py |
| TC-DET-1100 | P2 | safetext guard over tr variant=2 | package=safetext, lang=tr variant=2 | no-match | test_detectors_phase2_part_9.py |
| TC-DET-1101 | P2 | safetext guard over en variant=3 | package=safetext, lang=en variant=3 | no-match | test_detectors_phase2_part_10.py |
| TC-DET-1102 | P2 | safetext guard over ja variant=3 | package=safetext, lang=ja variant=3 | no-match | test_detectors_phase2_part_10.py |
| TC-DET-1103 | P2 | safetext guard over ar variant=3 | package=safetext, lang=ar variant=3 | no-match | test_detectors_phase2_part_10.py |
| TC-DET-1104 | P2 | safetext guard over ru variant=3 | package=safetext, lang=ru variant=3 | no-match | test_detectors_phase2_part_10.py |
| TC-DET-1105 | P2 | safetext guard over ko variant=3 | package=safetext, lang=ko variant=3 | no-match | test_detectors_phase2_part_10.py |
| TC-DET-1106 | P2 | safetext guard over de variant=3 | package=safetext, lang=de variant=3 | no-match | test_detectors_phase2_part_10.py |
| TC-DET-1107 | P2 | safetext guard over fr variant=3 | package=safetext, lang=fr variant=3 | no-match | test_detectors_phase2_part_10.py |
| TC-DET-1108 | P2 | safetext guard over it variant=3 | package=safetext, lang=it variant=3 | no-match | test_detectors_phase2_part_10.py |
| TC-DET-1109 | P2 | safetext guard over hi variant=3 | package=safetext, lang=hi variant=3 | no-match | test_detectors_phase2_part_10.py |
| TC-DET-1110 | P2 | safetext guard over tr variant=3 | package=safetext, lang=tr variant=3 | no-match | test_detectors_phase2_part_10.py |
| TC-DET-1111 | P2 | safetext guard over en variant=4 | package=safetext, lang=en variant=4 | no-match | test_detectors_phase2_part_10.py |
| TC-DET-1112 | P2 | safetext guard over ja variant=4 | package=safetext, lang=ja variant=4 | no-match | test_detectors_phase2_part_10.py |
| TC-DET-1113 | P2 | safetext guard over ar variant=4 | package=safetext, lang=ar variant=4 | no-match | test_detectors_phase2_part_10.py |
| TC-DET-1114 | P2 | safetext guard over ru variant=4 | package=safetext, lang=ru variant=4 | no-match | test_detectors_phase2_part_10.py |
| TC-DET-1115 | P2 | safetext guard over ko variant=4 | package=safetext, lang=ko variant=4 | no-match | test_detectors_phase2_part_10.py |
| TC-DET-1116 | P2 | safetext guard over de variant=4 | package=safetext, lang=de variant=4 | no-match | test_detectors_phase2_part_10.py |
| TC-DET-1117 | P2 | safetext guard over fr variant=4 | package=safetext, lang=fr variant=4 | no-match | test_detectors_phase2_part_10.py |
| TC-DET-1118 | P2 | safetext guard over it variant=4 | package=safetext, lang=it variant=4 | no-match | test_detectors_phase2_part_10.py |
| TC-DET-1119 | P2 | safetext guard over hi variant=4 | package=safetext, lang=hi variant=4 | no-match | test_detectors_phase2_part_10.py |
| TC-DET-1120 | P2 | safetext guard over tr variant=4 | package=safetext, lang=tr variant=4 | no-match | test_detectors_phase2_part_10.py |
| TC-DET-1121 | P2 | safetext guard over en variant=5 | package=safetext, lang=en variant=5 | no-match | test_detectors_phase2_part_10.py |
| TC-DET-1122 | P2 | safetext guard over ja variant=5 | package=safetext, lang=ja variant=5 | no-match | test_detectors_phase2_part_10.py |
| TC-DET-1123 | P2 | safetext guard over ar variant=5 | package=safetext, lang=ar variant=5 | no-match | test_detectors_phase2_part_10.py |
| TC-DET-1124 | P2 | safetext guard over ru variant=5 | package=safetext, lang=ru variant=5 | no-match | test_detectors_phase2_part_10.py |
| TC-DET-1125 | P2 | safetext guard over ko variant=5 | package=safetext, lang=ko variant=5 | no-match | test_detectors_phase2_part_10.py |
| TC-DET-1126 | P2 | safetext guard over de variant=5 | package=safetext, lang=de variant=5 | no-match | test_detectors_phase2_part_10.py |
| TC-DET-1127 | P2 | safetext guard over fr variant=5 | package=safetext, lang=fr variant=5 | no-match | test_detectors_phase2_part_10.py |
| TC-DET-1128 | P2 | safetext guard over it variant=5 | package=safetext, lang=it variant=5 | no-match | test_detectors_phase2_part_10.py |
| TC-DET-1129 | P2 | safetext guard over hi variant=5 | package=safetext, lang=hi variant=5 | no-match | test_detectors_phase2_part_10.py |
| TC-DET-1130 | P2 | safetext guard over tr variant=5 | package=safetext, lang=tr variant=5 | no-match | test_detectors_phase2_part_10.py |
| TC-DET-1131 | P2 | safetext guard over en variant=6 | package=safetext, lang=en variant=6 | no-match | test_detectors_phase2_part_10.py |
| TC-DET-1132 | P2 | safetext guard over ja variant=6 | package=safetext, lang=ja variant=6 | no-match | test_detectors_phase2_part_10.py |
| TC-DET-1133 | P2 | safetext guard over ar variant=6 | package=safetext, lang=ar variant=6 | no-match | test_detectors_phase2_part_10.py |
| TC-DET-1134 | P2 | safetext guard over ru variant=6 | package=safetext, lang=ru variant=6 | no-match | test_detectors_phase2_part_10.py |
| TC-DET-1135 | P2 | safetext guard over ko variant=6 | package=safetext, lang=ko variant=6 | no-match | test_detectors_phase2_part_10.py |
| TC-DET-1136 | P2 | safetext guard over de variant=6 | package=safetext, lang=de variant=6 | no-match | test_detectors_phase2_part_10.py |
| TC-DET-1137 | P2 | safetext guard over fr variant=6 | package=safetext, lang=fr variant=6 | no-match | test_detectors_phase2_part_10.py |
| TC-DET-1138 | P2 | safetext guard over it variant=6 | package=safetext, lang=it variant=6 | no-match | test_detectors_phase2_part_10.py |
| TC-DET-1139 | P2 | safetext guard over hi variant=6 | package=safetext, lang=hi variant=6 | no-match | test_detectors_phase2_part_10.py |
| TC-DET-1140 | P2 | safetext guard over tr variant=6 | package=safetext, lang=tr variant=6 | no-match | test_detectors_phase2_part_10.py |
| TC-DET-1141 | P2 | safetext guard over en variant=7 | package=safetext, lang=en variant=7 | no-match | test_detectors_phase2_part_10.py |
| TC-DET-1142 | P2 | safetext guard over ja variant=7 | package=safetext, lang=ja variant=7 | no-match | test_detectors_phase2_part_10.py |
| TC-DET-1143 | P2 | safetext guard over ar variant=7 | package=safetext, lang=ar variant=7 | no-match | test_detectors_phase2_part_10.py |
| TC-DET-1144 | P2 | safetext guard over ru variant=7 | package=safetext, lang=ru variant=7 | no-match | test_detectors_phase2_part_10.py |
| TC-DET-1145 | P2 | safetext guard over ko variant=7 | package=safetext, lang=ko variant=7 | no-match | test_detectors_phase2_part_10.py |
| TC-DET-1146 | P2 | safetext guard over de variant=7 | package=safetext, lang=de variant=7 | no-match | test_detectors_phase2_part_10.py |
| TC-DET-1147 | P2 | safetext guard over fr variant=7 | package=safetext, lang=fr variant=7 | no-match | test_detectors_phase2_part_10.py |
| TC-DET-1148 | P2 | safetext guard over it variant=7 | package=safetext, lang=it variant=7 | no-match | test_detectors_phase2_part_10.py |
| TC-DET-1149 | P2 | safetext guard over hi variant=7 | package=safetext, lang=hi variant=7 | no-match | test_detectors_phase2_part_10.py |
| TC-DET-1150 | P2 | safetext guard over tr variant=7 | package=safetext, lang=tr variant=7 | no-match | test_detectors_phase2_part_10.py |
| TC-DET-1151 | P2 | safetext guard over en variant=8 | package=safetext, lang=en variant=8 | no-match | test_detectors_phase2_part_10.py |
| TC-DET-1152 | P2 | safetext guard over ja variant=8 | package=safetext, lang=ja variant=8 | no-match | test_detectors_phase2_part_10.py |
| TC-DET-1153 | P2 | safetext guard over ar variant=8 | package=safetext, lang=ar variant=8 | no-match | test_detectors_phase2_part_10.py |
| TC-DET-1154 | P2 | safetext guard over ru variant=8 | package=safetext, lang=ru variant=8 | no-match | test_detectors_phase2_part_10.py |
| TC-DET-1155 | P2 | safetext guard over ko variant=8 | package=safetext, lang=ko variant=8 | no-match | test_detectors_phase2_part_10.py |
| TC-DET-1156 | P2 | safetext guard over de variant=8 | package=safetext, lang=de variant=8 | no-match | test_detectors_phase2_part_10.py |
| TC-DET-1157 | P2 | safetext guard over fr variant=8 | package=safetext, lang=fr variant=8 | no-match | test_detectors_phase2_part_10.py |
| TC-DET-1158 | P2 | safetext guard over it variant=8 | package=safetext, lang=it variant=8 | no-match | test_detectors_phase2_part_10.py |
| TC-DET-1159 | P2 | safetext guard over hi variant=8 | package=safetext, lang=hi variant=8 | no-match | test_detectors_phase2_part_10.py |
| TC-DET-1160 | P2 | safetext guard over tr variant=8 | package=safetext, lang=tr variant=8 | no-match | test_detectors_phase2_part_10.py |
| TC-DET-1161 | P2 | safetext guard over en variant=9 | package=safetext, lang=en variant=9 | no-match | test_detectors_phase2_part_10.py |
| TC-DET-1162 | P2 | safetext guard over ja variant=9 | package=safetext, lang=ja variant=9 | no-match | test_detectors_phase2_part_10.py |
| TC-DET-1163 | P2 | safetext guard over ar variant=9 | package=safetext, lang=ar variant=9 | no-match | test_detectors_phase2_part_10.py |
| TC-DET-1164 | P2 | safetext guard over ru variant=9 | package=safetext, lang=ru variant=9 | no-match | test_detectors_phase2_part_10.py |
| TC-DET-1165 | P2 | safetext guard over ko variant=9 | package=safetext, lang=ko variant=9 | no-match | test_detectors_phase2_part_10.py |
| TC-DET-1166 | P2 | safetext guard over de variant=9 | package=safetext, lang=de variant=9 | no-match | test_detectors_phase2_part_10.py |
| TC-DET-1167 | P2 | safetext guard over fr variant=9 | package=safetext, lang=fr variant=9 | no-match | test_detectors_phase2_part_10.py |
| TC-DET-1168 | P2 | safetext guard over it variant=9 | package=safetext, lang=it variant=9 | no-match | test_detectors_phase2_part_10.py |
| TC-DET-1169 | P2 | safetext guard over hi variant=9 | package=safetext, lang=hi variant=9 | no-match | test_detectors_phase2_part_10.py |
| TC-DET-1170 | P2 | safetext guard over tr variant=9 | package=safetext, lang=tr variant=9 | no-match | test_detectors_phase2_part_10.py |
| TC-DET-1171 | P2 | sensitive-word-filter-cn guard over zh variant=0 | package=sensitive-word-filter-cn, lang=zh variant=0 | no-match | test_detectors_phase2_part_10.py |
| TC-DET-1172 | P2 | sensitive-word-filter-cn guard over zh variant=1 | package=sensitive-word-filter-cn, lang=zh variant=1 | no-match | test_detectors_phase2_part_10.py |
| TC-DET-1173 | P2 | sensitive-word-filter-cn guard over zh variant=2 | package=sensitive-word-filter-cn, lang=zh variant=2 | no-match | test_detectors_phase2_part_10.py |
| TC-DET-1174 | P2 | sensitive-word-filter-cn guard over zh variant=3 | package=sensitive-word-filter-cn, lang=zh variant=3 | no-match | test_detectors_phase2_part_10.py |
| TC-DET-1175 | P2 | sensitive-word-filter-cn guard over zh variant=4 | package=sensitive-word-filter-cn, lang=zh variant=4 | no-match | test_detectors_phase2_part_10.py |
| TC-DET-1176 | P2 | sensitive-word-filter-cn guard over zh variant=5 | package=sensitive-word-filter-cn, lang=zh variant=5 | no-match | test_detectors_phase2_part_10.py |
| TC-DET-1177 | P2 | sensitive-word-filter-cn guard over zh variant=6 | package=sensitive-word-filter-cn, lang=zh variant=6 | no-match | test_detectors_phase2_part_10.py |
| TC-DET-1178 | P2 | sensitive-word-filter-cn guard over zh variant=7 | package=sensitive-word-filter-cn, lang=zh variant=7 | no-match | test_detectors_phase2_part_10.py |
| TC-DET-1179 | P2 | sensitive-word-filter-cn guard over zh variant=8 | package=sensitive-word-filter-cn, lang=zh variant=8 | no-match | test_detectors_phase2_part_10.py |
| TC-DET-1180 | P2 | sensitive-word-filter-cn guard over zh variant=9 | package=sensitive-word-filter-cn, lang=zh variant=9 | no-match | test_detectors_phase2_part_10.py |
| TC-DET-1181 | P2 | sensitive-word-filter-cn guard over zh variant=10 | package=sensitive-word-filter-cn, lang=zh variant=10 | no-match | test_detectors_phase2_part_10.py |
| TC-DET-1182 | P2 | sensitive-word-filter-cn guard over zh variant=11 | package=sensitive-word-filter-cn, lang=zh variant=11 | no-match | test_detectors_phase2_part_10.py |
| TC-DET-1183 | P2 | sensitive-word-filter-cn guard over zh variant=12 | package=sensitive-word-filter-cn, lang=zh variant=12 | no-match | test_detectors_phase2_part_10.py |
| TC-DET-1184 | P2 | sensitive-word-filter-cn guard over zh variant=13 | package=sensitive-word-filter-cn, lang=zh variant=13 | no-match | test_detectors_phase2_part_10.py |
| TC-DET-1185 | P2 | sensitive-word-filter-cn guard over zh variant=14 | package=sensitive-word-filter-cn, lang=zh variant=14 | no-match | test_detectors_phase2_part_10.py |
| TC-DET-1186 | P2 | sensitive-word-filter-cn guard over zh variant=15 | package=sensitive-word-filter-cn, lang=zh variant=15 | no-match | test_detectors_phase2_part_10.py |
| TC-DET-1187 | P2 | sensitive-word-filter-cn guard over zh variant=16 | package=sensitive-word-filter-cn, lang=zh variant=16 | no-match | test_detectors_phase2_part_10.py |
| TC-DET-1188 | P2 | sensitive-word-filter-cn guard over zh variant=17 | package=sensitive-word-filter-cn, lang=zh variant=17 | no-match | test_detectors_phase2_part_10.py |
| TC-DET-1189 | P2 | sensitive-word-filter-cn guard over zh variant=18 | package=sensitive-word-filter-cn, lang=zh variant=18 | no-match | test_detectors_phase2_part_10.py |
| TC-DET-1190 | P2 | sensitive-word-filter-cn guard over zh variant=19 | package=sensitive-word-filter-cn, lang=zh variant=19 | no-match | test_detectors_phase2_part_10.py |
| TC-DET-1191 | P2 | sensitive-word-filter-cn guard over zh variant=20 | package=sensitive-word-filter-cn, lang=zh variant=20 | no-match | test_detectors_phase2_part_10.py |
| TC-DET-1192 | P2 | sensitive-word-filter-cn guard over zh variant=21 | package=sensitive-word-filter-cn, lang=zh variant=21 | no-match | test_detectors_phase2_part_10.py |
| TC-DET-1193 | P2 | sensitive-word-filter-cn guard over zh variant=22 | package=sensitive-word-filter-cn, lang=zh variant=22 | no-match | test_detectors_phase2_part_10.py |
| TC-DET-1194 | P2 | sensitive-word-filter-cn guard over zh variant=23 | package=sensitive-word-filter-cn, lang=zh variant=23 | no-match | test_detectors_phase2_part_10.py |
| TC-DET-1195 | P2 | sensitive-word-filter-cn guard over zh variant=24 | package=sensitive-word-filter-cn, lang=zh variant=24 | no-match | test_detectors_phase2_part_10.py |
| TC-DET-1196 | P2 | sensitive-word-filter-cn guard over zh variant=25 | package=sensitive-word-filter-cn, lang=zh variant=25 | no-match | test_detectors_phase2_part_10.py |
| TC-DET-1197 | P2 | sensitive-word-filter-cn guard over zh variant=26 | package=sensitive-word-filter-cn, lang=zh variant=26 | no-match | test_detectors_phase2_part_10.py |
| TC-DET-1198 | P2 | sensitive-word-filter-cn guard over zh variant=27 | package=sensitive-word-filter-cn, lang=zh variant=27 | no-match | test_detectors_phase2_part_10.py |
| TC-DET-1199 | P2 | sensitive-word-filter-cn guard over zh variant=28 | package=sensitive-word-filter-cn, lang=zh variant=28 | no-match | test_detectors_phase2_part_10.py |
| TC-DET-1200 | P2 | sensitive-word-filter-cn guard over zh variant=29 | package=sensitive-word-filter-cn, lang=zh variant=29 | no-match | test_detectors_phase2_part_10.py |
| TC-DET-1201 | P2 | sensitive-word-filter-cn guard over zh variant=30 | package=sensitive-word-filter-cn, lang=zh variant=30 | no-match | test_detectors_phase2_part_11.py |
| TC-DET-1202 | P2 | sensitive-word-filter-cn guard over zh variant=31 | package=sensitive-word-filter-cn, lang=zh variant=31 | no-match | test_detectors_phase2_part_11.py |
| TC-DET-1203 | P2 | sensitive-word-filter-cn guard over zh variant=32 | package=sensitive-word-filter-cn, lang=zh variant=32 | no-match | test_detectors_phase2_part_11.py |
| TC-DET-1204 | P2 | sensitive-word-filter-cn guard over zh variant=33 | package=sensitive-word-filter-cn, lang=zh variant=33 | no-match | test_detectors_phase2_part_11.py |
| TC-DET-1205 | P2 | sensitive-word-filter-cn guard over zh variant=34 | package=sensitive-word-filter-cn, lang=zh variant=34 | no-match | test_detectors_phase2_part_11.py |
| TC-DET-1206 | P2 | sensitive-word-filter-cn guard over zh variant=35 | package=sensitive-word-filter-cn, lang=zh variant=35 | no-match | test_detectors_phase2_part_11.py |
| TC-DET-1207 | P2 | sensitive-word-filter-cn guard over zh variant=36 | package=sensitive-word-filter-cn, lang=zh variant=36 | no-match | test_detectors_phase2_part_11.py |
| TC-DET-1208 | P2 | sensitive-word-filter-cn guard over zh variant=37 | package=sensitive-word-filter-cn, lang=zh variant=37 | no-match | test_detectors_phase2_part_11.py |
| TC-DET-1209 | P2 | sensitive-word-filter-cn guard over zh variant=38 | package=sensitive-word-filter-cn, lang=zh variant=38 | no-match | test_detectors_phase2_part_11.py |
| TC-DET-1210 | P2 | sensitive-word-filter-cn guard over zh variant=39 | package=sensitive-word-filter-cn, lang=zh variant=39 | no-match | test_detectors_phase2_part_11.py |
| TC-DET-1211 | P2 | sensitive-word-filter-cn guard over zh variant=40 | package=sensitive-word-filter-cn, lang=zh variant=40 | no-match | test_detectors_phase2_part_11.py |
| TC-DET-1212 | P2 | sensitive-word-filter-cn guard over zh variant=41 | package=sensitive-word-filter-cn, lang=zh variant=41 | no-match | test_detectors_phase2_part_11.py |
| TC-DET-1213 | P2 | sensitive-word-filter-cn guard over zh variant=42 | package=sensitive-word-filter-cn, lang=zh variant=42 | no-match | test_detectors_phase2_part_11.py |
| TC-DET-1214 | P2 | sensitive-word-filter-cn guard over zh variant=43 | package=sensitive-word-filter-cn, lang=zh variant=43 | no-match | test_detectors_phase2_part_11.py |
| TC-DET-1215 | P2 | sensitive-word-filter-cn guard over zh variant=44 | package=sensitive-word-filter-cn, lang=zh variant=44 | no-match | test_detectors_phase2_part_11.py |
| TC-DET-1216 | P2 | sensitive-word-filter-cn guard over zh variant=45 | package=sensitive-word-filter-cn, lang=zh variant=45 | no-match | test_detectors_phase2_part_11.py |
| TC-DET-1217 | P2 | sensitive-word-filter-cn guard over zh variant=46 | package=sensitive-word-filter-cn, lang=zh variant=46 | no-match | test_detectors_phase2_part_11.py |
| TC-DET-1218 | P2 | sensitive-word-filter-cn guard over zh variant=47 | package=sensitive-word-filter-cn, lang=zh variant=47 | no-match | test_detectors_phase2_part_11.py |
| TC-DET-1219 | P2 | sensitive-word-filter-cn guard over zh variant=48 | package=sensitive-word-filter-cn, lang=zh variant=48 | no-match | test_detectors_phase2_part_11.py |
| TC-DET-1220 | P2 | sensitive-word-filter-cn guard over zh variant=49 | package=sensitive-word-filter-cn, lang=zh variant=49 | no-match | test_detectors_phase2_part_11.py |
| TC-DET-1221 | P2 | sensitive-word-filter-cn guard over zh variant=50 | package=sensitive-word-filter-cn, lang=zh variant=50 | no-match | test_detectors_phase2_part_11.py |
| TC-DET-1222 | P2 | sensitive-word-filter-cn guard over zh variant=51 | package=sensitive-word-filter-cn, lang=zh variant=51 | no-match | test_detectors_phase2_part_11.py |
| TC-DET-1223 | P2 | sensitive-word-filter-cn guard over zh variant=52 | package=sensitive-word-filter-cn, lang=zh variant=52 | no-match | test_detectors_phase2_part_11.py |
| TC-DET-1224 | P2 | sensitive-word-filter-cn guard over zh variant=53 | package=sensitive-word-filter-cn, lang=zh variant=53 | no-match | test_detectors_phase2_part_11.py |
| TC-DET-1225 | P2 | sensitive-word-filter-cn guard over zh variant=54 | package=sensitive-word-filter-cn, lang=zh variant=54 | no-match | test_detectors_phase2_part_11.py |
| TC-DET-1226 | P2 | sensitive-word-filter-cn guard over zh variant=55 | package=sensitive-word-filter-cn, lang=zh variant=55 | no-match | test_detectors_phase2_part_11.py |
| TC-DET-1227 | P2 | sensitive-word-filter-cn guard over zh variant=56 | package=sensitive-word-filter-cn, lang=zh variant=56 | no-match | test_detectors_phase2_part_11.py |
| TC-DET-1228 | P2 | sensitive-word-filter-cn guard over zh variant=57 | package=sensitive-word-filter-cn, lang=zh variant=57 | no-match | test_detectors_phase2_part_11.py |
| TC-DET-1229 | P2 | sensitive-word-filter-cn guard over zh variant=58 | package=sensitive-word-filter-cn, lang=zh variant=58 | no-match | test_detectors_phase2_part_11.py |
| TC-DET-1230 | P2 | sensitive-word-filter-cn guard over zh variant=59 | package=sensitive-word-filter-cn, lang=zh variant=59 | no-match | test_detectors_phase2_part_11.py |
| TC-DET-1231 | P2 | sensitive-word-filter-cn guard over zh variant=60 | package=sensitive-word-filter-cn, lang=zh variant=60 | no-match | test_detectors_phase2_part_11.py |
| TC-DET-1232 | P2 | sensitive-word-filter-cn guard over zh variant=61 | package=sensitive-word-filter-cn, lang=zh variant=61 | no-match | test_detectors_phase2_part_11.py |
| TC-DET-1233 | P2 | sensitive-word-filter-cn guard over zh variant=62 | package=sensitive-word-filter-cn, lang=zh variant=62 | no-match | test_detectors_phase2_part_11.py |
| TC-DET-1234 | P2 | sensitive-word-filter-cn guard over zh variant=63 | package=sensitive-word-filter-cn, lang=zh variant=63 | no-match | test_detectors_phase2_part_11.py |
| TC-DET-1235 | P2 | sensitive-word-filter-cn guard over zh variant=64 | package=sensitive-word-filter-cn, lang=zh variant=64 | no-match | test_detectors_phase2_part_11.py |
| TC-DET-1236 | P2 | sensitive-word-filter-cn guard over zh variant=65 | package=sensitive-word-filter-cn, lang=zh variant=65 | no-match | test_detectors_phase2_part_11.py |
| TC-DET-1237 | P2 | sensitive-word-filter-cn guard over zh variant=66 | package=sensitive-word-filter-cn, lang=zh variant=66 | no-match | test_detectors_phase2_part_11.py |
| TC-DET-1238 | P2 | sensitive-word-filter-cn guard over zh variant=67 | package=sensitive-word-filter-cn, lang=zh variant=67 | no-match | test_detectors_phase2_part_11.py |
| TC-DET-1239 | P2 | sensitive-word-filter-cn guard over zh variant=68 | package=sensitive-word-filter-cn, lang=zh variant=68 | no-match | test_detectors_phase2_part_11.py |
| TC-DET-1240 | P2 | sensitive-word-filter-cn guard over zh variant=69 | package=sensitive-word-filter-cn, lang=zh variant=69 | no-match | test_detectors_phase2_part_11.py |
| TC-DET-1241 | P2 | sensitive-word-filter-cn guard over zh variant=70 | package=sensitive-word-filter-cn, lang=zh variant=70 | no-match | test_detectors_phase2_part_11.py |
| TC-DET-1242 | P2 | sensitive-word-filter-cn guard over zh variant=71 | package=sensitive-word-filter-cn, lang=zh variant=71 | no-match | test_detectors_phase2_part_11.py |
| TC-DET-1243 | P2 | sensitive-word-filter-cn guard over zh variant=72 | package=sensitive-word-filter-cn, lang=zh variant=72 | no-match | test_detectors_phase2_part_11.py |
| TC-DET-1244 | P2 | sensitive-word-filter-cn guard over zh variant=73 | package=sensitive-word-filter-cn, lang=zh variant=73 | no-match | test_detectors_phase2_part_11.py |
| TC-DET-1245 | P2 | sensitive-word-filter-cn guard over zh variant=74 | package=sensitive-word-filter-cn, lang=zh variant=74 | no-match | test_detectors_phase2_part_11.py |
| TC-DET-1246 | P2 | sensitive-word-filter-cn guard over zh variant=75 | package=sensitive-word-filter-cn, lang=zh variant=75 | no-match | test_detectors_phase2_part_11.py |
| TC-DET-1247 | P2 | sensitive-word-filter-cn guard over zh variant=76 | package=sensitive-word-filter-cn, lang=zh variant=76 | no-match | test_detectors_phase2_part_11.py |
| TC-DET-1248 | P2 | sensitive-word-filter-cn guard over zh variant=77 | package=sensitive-word-filter-cn, lang=zh variant=77 | no-match | test_detectors_phase2_part_11.py |
| TC-DET-1249 | P2 | sensitive-word-filter-cn guard over zh variant=78 | package=sensitive-word-filter-cn, lang=zh variant=78 | no-match | test_detectors_phase2_part_11.py |
| TC-DET-1250 | P2 | sensitive-word-filter-cn guard over zh variant=79 | package=sensitive-word-filter-cn, lang=zh variant=79 | no-match | test_detectors_phase2_part_11.py |
| TC-DET-1251 | P2 | profanity-filter2 guard over en variant=0 | package=profanity-filter2, lang=en variant=0 | no-match | test_detectors_phase2_part_11.py |
| TC-DET-1252 | P2 | profanity-filter2 guard over en variant=1 | package=profanity-filter2, lang=en variant=1 | no-match | test_detectors_phase2_part_11.py |
| TC-DET-1253 | P2 | profanity-filter2 guard over en variant=2 | package=profanity-filter2, lang=en variant=2 | no-match | test_detectors_phase2_part_11.py |
| TC-DET-1254 | P2 | profanity-filter2 guard over en variant=3 | package=profanity-filter2, lang=en variant=3 | no-match | test_detectors_phase2_part_11.py |
| TC-DET-1255 | P2 | profanity-filter2 guard over en variant=4 | package=profanity-filter2, lang=en variant=4 | no-match | test_detectors_phase2_part_11.py |
| TC-DET-1256 | P2 | profanity-filter2 guard over en variant=5 | package=profanity-filter2, lang=en variant=5 | no-match | test_detectors_phase2_part_11.py |
| TC-DET-1257 | P2 | profanity-filter2 guard over en variant=6 | package=profanity-filter2, lang=en variant=6 | no-match | test_detectors_phase2_part_11.py |
| TC-DET-1258 | P2 | profanity-filter2 guard over en variant=7 | package=profanity-filter2, lang=en variant=7 | no-match | test_detectors_phase2_part_11.py |
| TC-DET-1259 | P2 | profanity-filter2 guard over en variant=8 | package=profanity-filter2, lang=en variant=8 | no-match | test_detectors_phase2_part_11.py |
| TC-DET-1260 | P2 | profanity-filter2 guard over en variant=9 | package=profanity-filter2, lang=en variant=9 | no-match | test_detectors_phase2_part_11.py |
| TC-DET-1261 | P2 | profanity-filter2 guard over en variant=10 | package=profanity-filter2, lang=en variant=10 | no-match | test_detectors_phase2_part_11.py |
| TC-DET-1262 | P2 | profanity-filter2 guard over en variant=11 | package=profanity-filter2, lang=en variant=11 | no-match | test_detectors_phase2_part_11.py |
| TC-DET-1263 | P2 | profanity-filter2 guard over en variant=12 | package=profanity-filter2, lang=en variant=12 | no-match | test_detectors_phase2_part_11.py |
| TC-DET-1264 | P2 | profanity-filter2 guard over en variant=13 | package=profanity-filter2, lang=en variant=13 | no-match | test_detectors_phase2_part_11.py |
| TC-DET-1265 | P2 | profanity-filter2 guard over en variant=14 | package=profanity-filter2, lang=en variant=14 | no-match | test_detectors_phase2_part_11.py |
| TC-DET-1266 | P2 | profanity-filter2 guard over en variant=15 | package=profanity-filter2, lang=en variant=15 | no-match | test_detectors_phase2_part_11.py |
| TC-DET-1267 | P2 | profanity-filter2 guard over en variant=16 | package=profanity-filter2, lang=en variant=16 | no-match | test_detectors_phase2_part_11.py |
| TC-DET-1268 | P2 | profanity-filter2 guard over en variant=17 | package=profanity-filter2, lang=en variant=17 | no-match | test_detectors_phase2_part_11.py |
| TC-DET-1269 | P2 | profanity-filter2 guard over en variant=18 | package=profanity-filter2, lang=en variant=18 | no-match | test_detectors_phase2_part_11.py |
| TC-DET-1270 | P2 | profanity-filter2 guard over en variant=19 | package=profanity-filter2, lang=en variant=19 | no-match | test_detectors_phase2_part_11.py |
| TC-DET-1271 | P2 | profanity-filter2 guard over en variant=20 | package=profanity-filter2, lang=en variant=20 | no-match | test_detectors_phase2_part_11.py |
| TC-DET-1272 | P2 | profanity-filter2 guard over en variant=21 | package=profanity-filter2, lang=en variant=21 | no-match | test_detectors_phase2_part_11.py |
| TC-DET-1273 | P2 | profanity-filter2 guard over en variant=22 | package=profanity-filter2, lang=en variant=22 | no-match | test_detectors_phase2_part_11.py |
| TC-DET-1274 | P2 | profanity-filter2 guard over en variant=23 | package=profanity-filter2, lang=en variant=23 | no-match | test_detectors_phase2_part_11.py |
| TC-DET-1275 | P2 | profanity-filter2 guard over en variant=24 | package=profanity-filter2, lang=en variant=24 | no-match | test_detectors_phase2_part_11.py |
| TC-DET-1276 | P2 | profanity-filter2 guard over en variant=25 | package=profanity-filter2, lang=en variant=25 | no-match | test_detectors_phase2_part_11.py |
| TC-DET-1277 | P2 | profanity-filter2 guard over en variant=26 | package=profanity-filter2, lang=en variant=26 | no-match | test_detectors_phase2_part_11.py |
| TC-DET-1278 | P2 | profanity-filter2 guard over en variant=27 | package=profanity-filter2, lang=en variant=27 | no-match | test_detectors_phase2_part_11.py |
| TC-DET-1279 | P2 | profanity-filter2 guard over en variant=28 | package=profanity-filter2, lang=en variant=28 | no-match | test_detectors_phase2_part_11.py |
| TC-DET-1280 | P2 | profanity-filter2 guard over en variant=29 | package=profanity-filter2, lang=en variant=29 | no-match | test_detectors_phase2_part_11.py |
| TC-DET-1281 | P2 | profanity-filter2 guard over en variant=30 | package=profanity-filter2, lang=en variant=30 | no-match | test_detectors_phase2_part_11.py |
| TC-DET-1282 | P2 | profanity-filter2 guard over en variant=31 | package=profanity-filter2, lang=en variant=31 | no-match | test_detectors_phase2_part_11.py |
| TC-DET-1283 | P2 | profanity-filter2 guard over en variant=32 | package=profanity-filter2, lang=en variant=32 | no-match | test_detectors_phase2_part_11.py |
| TC-DET-1284 | P2 | profanity-filter2 guard over en variant=33 | package=profanity-filter2, lang=en variant=33 | no-match | test_detectors_phase2_part_11.py |
| TC-DET-1285 | P2 | profanity-filter2 guard over en variant=34 | package=profanity-filter2, lang=en variant=34 | no-match | test_detectors_phase2_part_11.py |
| TC-DET-1286 | P2 | profanity-filter2 guard over en variant=35 | package=profanity-filter2, lang=en variant=35 | no-match | test_detectors_phase2_part_11.py |
| TC-DET-1287 | P2 | profanity-filter2 guard over en variant=36 | package=profanity-filter2, lang=en variant=36 | no-match | test_detectors_phase2_part_11.py |
| TC-DET-1288 | P2 | profanity-filter2 guard over en variant=37 | package=profanity-filter2, lang=en variant=37 | no-match | test_detectors_phase2_part_11.py |
| TC-DET-1289 | P2 | profanity-filter2 guard over en variant=38 | package=profanity-filter2, lang=en variant=38 | no-match | test_detectors_phase2_part_11.py |
| TC-DET-1290 | P2 | profanity-filter2 guard over en variant=39 | package=profanity-filter2, lang=en variant=39 | no-match | test_detectors_phase2_part_11.py |
| TC-DET-1291 | P2 | profanity-filter2 guard over en variant=40 | package=profanity-filter2, lang=en variant=40 | no-match | test_detectors_phase2_part_11.py |
| TC-DET-1292 | P2 | profanity-filter2 guard over en variant=41 | package=profanity-filter2, lang=en variant=41 | no-match | test_detectors_phase2_part_11.py |
| TC-DET-1293 | P2 | profanity-filter2 guard over en variant=42 | package=profanity-filter2, lang=en variant=42 | no-match | test_detectors_phase2_part_11.py |
| TC-DET-1294 | P2 | profanity-filter2 guard over en variant=43 | package=profanity-filter2, lang=en variant=43 | no-match | test_detectors_phase2_part_11.py |
| TC-DET-1295 | P2 | profanity-filter2 guard over en variant=44 | package=profanity-filter2, lang=en variant=44 | no-match | test_detectors_phase2_part_11.py |
| TC-DET-1296 | P2 | profanity-filter2 guard over en variant=45 | package=profanity-filter2, lang=en variant=45 | no-match | test_detectors_phase2_part_11.py |
| TC-DET-1297 | P2 | profanity-filter2 guard over en variant=46 | package=profanity-filter2, lang=en variant=46 | no-match | test_detectors_phase2_part_11.py |
| TC-DET-1298 | P2 | profanity-filter2 guard over en variant=47 | package=profanity-filter2, lang=en variant=47 | no-match | test_detectors_phase2_part_11.py |
| TC-DET-1299 | P2 | profanity-filter2 guard over en variant=48 | package=profanity-filter2, lang=en variant=48 | no-match | test_detectors_phase2_part_11.py |
| TC-DET-1300 | P2 | profanity-filter2 guard over en variant=49 | package=profanity-filter2, lang=en variant=49 | no-match | test_detectors_phase2_part_11.py |
| TC-DET-1301 | P2 | profanity-filter2 guard over en variant=50 | package=profanity-filter2, lang=en variant=50 | no-match | test_detectors_phase2_part_12.py |
| TC-DET-1302 | P2 | profanity-filter2 guard over en variant=51 | package=profanity-filter2, lang=en variant=51 | no-match | test_detectors_phase2_part_12.py |
| TC-DET-1303 | P2 | profanity-filter2 guard over en variant=52 | package=profanity-filter2, lang=en variant=52 | no-match | test_detectors_phase2_part_12.py |
| TC-DET-1304 | P2 | profanity-filter2 guard over en variant=53 | package=profanity-filter2, lang=en variant=53 | no-match | test_detectors_phase2_part_12.py |
| TC-DET-1305 | P2 | profanity-filter2 guard over en variant=54 | package=profanity-filter2, lang=en variant=54 | no-match | test_detectors_phase2_part_12.py |
| TC-DET-1306 | P2 | profanity-filter2 guard over en variant=55 | package=profanity-filter2, lang=en variant=55 | no-match | test_detectors_phase2_part_12.py |
| TC-DET-1307 | P2 | profanity-filter2 guard over en variant=56 | package=profanity-filter2, lang=en variant=56 | no-match | test_detectors_phase2_part_12.py |
| TC-DET-1308 | P2 | profanity-filter2 guard over en variant=57 | package=profanity-filter2, lang=en variant=57 | no-match | test_detectors_phase2_part_12.py |
| TC-DET-1309 | P2 | profanity-filter2 guard over en variant=58 | package=profanity-filter2, lang=en variant=58 | no-match | test_detectors_phase2_part_12.py |
| TC-DET-1310 | P2 | profanity-filter2 guard over en variant=59 | package=profanity-filter2, lang=en variant=59 | no-match | test_detectors_phase2_part_12.py |
| TC-DET-1311 | P2 | profanity-filter2 guard over en variant=60 | package=profanity-filter2, lang=en variant=60 | no-match | test_detectors_phase2_part_12.py |
| TC-DET-1312 | P2 | profanity-filter2 guard over en variant=61 | package=profanity-filter2, lang=en variant=61 | no-match | test_detectors_phase2_part_12.py |
| TC-DET-1313 | P2 | profanity-filter2 guard over en variant=62 | package=profanity-filter2, lang=en variant=62 | no-match | test_detectors_phase2_part_12.py |
| TC-DET-1314 | P2 | profanity-filter2 guard over en variant=63 | package=profanity-filter2, lang=en variant=63 | no-match | test_detectors_phase2_part_12.py |
| TC-DET-1315 | P2 | profanity-filter2 guard over en variant=64 | package=profanity-filter2, lang=en variant=64 | no-match | test_detectors_phase2_part_12.py |
| TC-DET-1316 | P2 | profanity-filter2 guard over en variant=65 | package=profanity-filter2, lang=en variant=65 | no-match | test_detectors_phase2_part_12.py |
| TC-DET-1317 | P2 | profanity-filter2 guard over en variant=66 | package=profanity-filter2, lang=en variant=66 | no-match | test_detectors_phase2_part_12.py |
| TC-DET-1318 | P2 | profanity-filter2 guard over en variant=67 | package=profanity-filter2, lang=en variant=67 | no-match | test_detectors_phase2_part_12.py |
| TC-DET-1319 | P2 | profanity-filter2 guard over en variant=68 | package=profanity-filter2, lang=en variant=68 | no-match | test_detectors_phase2_part_12.py |
| TC-DET-1320 | P2 | profanity-filter2 guard over en variant=69 | package=profanity-filter2, lang=en variant=69 | no-match | test_detectors_phase2_part_12.py |
| TC-DET-1321 | P2 | profanity-filter2 guard over en variant=70 | package=profanity-filter2, lang=en variant=70 | no-match | test_detectors_phase2_part_12.py |
| TC-DET-1322 | P2 | profanity-filter2 guard over en variant=71 | package=profanity-filter2, lang=en variant=71 | no-match | test_detectors_phase2_part_12.py |
| TC-DET-1323 | P2 | profanity-filter2 guard over en variant=72 | package=profanity-filter2, lang=en variant=72 | no-match | test_detectors_phase2_part_12.py |
| TC-DET-1324 | P2 | profanity-filter2 guard over en variant=73 | package=profanity-filter2, lang=en variant=73 | no-match | test_detectors_phase2_part_12.py |
| TC-DET-1325 | P2 | profanity-filter2 guard over en variant=74 | package=profanity-filter2, lang=en variant=74 | no-match | test_detectors_phase2_part_12.py |
| TC-DET-1326 | P2 | profanity-filter2 guard over en variant=75 | package=profanity-filter2, lang=en variant=75 | no-match | test_detectors_phase2_part_12.py |
| TC-DET-1327 | P2 | profanity-filter2 guard over en variant=76 | package=profanity-filter2, lang=en variant=76 | no-match | test_detectors_phase2_part_12.py |
| TC-DET-1328 | P2 | profanity-filter2 guard over en variant=77 | package=profanity-filter2, lang=en variant=77 | no-match | test_detectors_phase2_part_12.py |
| TC-DET-1329 | P2 | profanity-filter2 guard over en variant=78 | package=profanity-filter2, lang=en variant=78 | no-match | test_detectors_phase2_part_12.py |
| TC-DET-1330 | P2 | profanity-filter2 guard over en variant=79 | package=profanity-filter2, lang=en variant=79 | no-match | test_detectors_phase2_part_12.py |
| TC-DET-1331 | P2 | pyprofane guard over en variant=0 | package=pyprofane, lang=en variant=0 | no-match | test_detectors_phase2_part_12.py |
| TC-DET-1332 | P2 | pyprofane guard over en variant=1 | package=pyprofane, lang=en variant=1 | no-match | test_detectors_phase2_part_12.py |
| TC-DET-1333 | P2 | pyprofane guard over en variant=2 | package=pyprofane, lang=en variant=2 | no-match | test_detectors_phase2_part_12.py |
| TC-DET-1334 | P2 | pyprofane guard over en variant=3 | package=pyprofane, lang=en variant=3 | no-match | test_detectors_phase2_part_12.py |
| TC-DET-1335 | P2 | pyprofane guard over en variant=4 | package=pyprofane, lang=en variant=4 | no-match | test_detectors_phase2_part_12.py |
| TC-DET-1336 | P2 | pyprofane guard over en variant=5 | package=pyprofane, lang=en variant=5 | no-match | test_detectors_phase2_part_12.py |
| TC-DET-1337 | P2 | pyprofane guard over en variant=6 | package=pyprofane, lang=en variant=6 | no-match | test_detectors_phase2_part_12.py |
| TC-DET-1338 | P2 | pyprofane guard over en variant=7 | package=pyprofane, lang=en variant=7 | no-match | test_detectors_phase2_part_12.py |
| TC-DET-1339 | P2 | pyprofane guard over en variant=8 | package=pyprofane, lang=en variant=8 | no-match | test_detectors_phase2_part_12.py |
| TC-DET-1340 | P2 | pyprofane guard over en variant=9 | package=pyprofane, lang=en variant=9 | no-match | test_detectors_phase2_part_12.py |
| TC-DET-1341 | P2 | pyprofane guard over en variant=10 | package=pyprofane, lang=en variant=10 | no-match | test_detectors_phase2_part_12.py |
| TC-DET-1342 | P2 | pyprofane guard over en variant=11 | package=pyprofane, lang=en variant=11 | no-match | test_detectors_phase2_part_12.py |
| TC-DET-1343 | P2 | pyprofane guard over en variant=12 | package=pyprofane, lang=en variant=12 | no-match | test_detectors_phase2_part_12.py |
| TC-DET-1344 | P2 | pyprofane guard over en variant=13 | package=pyprofane, lang=en variant=13 | no-match | test_detectors_phase2_part_12.py |
| TC-DET-1345 | P2 | pyprofane guard over en variant=14 | package=pyprofane, lang=en variant=14 | no-match | test_detectors_phase2_part_12.py |
| TC-DET-1346 | P2 | pyprofane guard over en variant=15 | package=pyprofane, lang=en variant=15 | no-match | test_detectors_phase2_part_12.py |
| TC-DET-1347 | P2 | pyprofane guard over en variant=16 | package=pyprofane, lang=en variant=16 | no-match | test_detectors_phase2_part_12.py |
| TC-DET-1348 | P2 | pyprofane guard over en variant=17 | package=pyprofane, lang=en variant=17 | no-match | test_detectors_phase2_part_12.py |
| TC-DET-1349 | P2 | pyprofane guard over en variant=18 | package=pyprofane, lang=en variant=18 | no-match | test_detectors_phase2_part_12.py |
| TC-DET-1350 | P2 | pyprofane guard over en variant=19 | package=pyprofane, lang=en variant=19 | no-match | test_detectors_phase2_part_12.py |
| TC-DET-1351 | P2 | pyprofane guard over en variant=20 | package=pyprofane, lang=en variant=20 | no-match | test_detectors_phase2_part_12.py |
| TC-DET-1352 | P2 | pyprofane guard over en variant=21 | package=pyprofane, lang=en variant=21 | no-match | test_detectors_phase2_part_12.py |
| TC-DET-1353 | P2 | pyprofane guard over en variant=22 | package=pyprofane, lang=en variant=22 | no-match | test_detectors_phase2_part_12.py |
| TC-DET-1354 | P2 | pyprofane guard over en variant=23 | package=pyprofane, lang=en variant=23 | no-match | test_detectors_phase2_part_12.py |
| TC-DET-1355 | P2 | pyprofane guard over en variant=24 | package=pyprofane, lang=en variant=24 | no-match | test_detectors_phase2_part_12.py |
| TC-DET-1356 | P2 | pyprofane guard over en variant=25 | package=pyprofane, lang=en variant=25 | no-match | test_detectors_phase2_part_12.py |
| TC-DET-1357 | P2 | pyprofane guard over en variant=26 | package=pyprofane, lang=en variant=26 | no-match | test_detectors_phase2_part_12.py |
| TC-DET-1358 | P2 | pyprofane guard over en variant=27 | package=pyprofane, lang=en variant=27 | no-match | test_detectors_phase2_part_12.py |
| TC-DET-1359 | P2 | pyprofane guard over en variant=28 | package=pyprofane, lang=en variant=28 | no-match | test_detectors_phase2_part_12.py |
| TC-DET-1360 | P2 | pyprofane guard over en variant=29 | package=pyprofane, lang=en variant=29 | no-match | test_detectors_phase2_part_12.py |
| TC-DET-1361 | P2 | pyprofane guard over en variant=30 | package=pyprofane, lang=en variant=30 | no-match | test_detectors_phase2_part_12.py |
| TC-DET-1362 | P2 | pyprofane guard over en variant=31 | package=pyprofane, lang=en variant=31 | no-match | test_detectors_phase2_part_12.py |
| TC-DET-1363 | P2 | pyprofane guard over en variant=32 | package=pyprofane, lang=en variant=32 | no-match | test_detectors_phase2_part_12.py |
| TC-DET-1364 | P2 | pyprofane guard over en variant=33 | package=pyprofane, lang=en variant=33 | no-match | test_detectors_phase2_part_12.py |
| TC-DET-1365 | P2 | pyprofane guard over en variant=34 | package=pyprofane, lang=en variant=34 | no-match | test_detectors_phase2_part_12.py |
| TC-DET-1366 | P2 | pyprofane guard over en variant=35 | package=pyprofane, lang=en variant=35 | no-match | test_detectors_phase2_part_12.py |
| TC-DET-1367 | P2 | pyprofane guard over en variant=36 | package=pyprofane, lang=en variant=36 | no-match | test_detectors_phase2_part_12.py |
| TC-DET-1368 | P2 | pyprofane guard over en variant=37 | package=pyprofane, lang=en variant=37 | no-match | test_detectors_phase2_part_12.py |
| TC-DET-1369 | P2 | pyprofane guard over en variant=38 | package=pyprofane, lang=en variant=38 | no-match | test_detectors_phase2_part_12.py |
| TC-DET-1370 | P2 | pyprofane guard over en variant=39 | package=pyprofane, lang=en variant=39 | no-match | test_detectors_phase2_part_12.py |
| TC-DET-1371 | P2 | pyprofane guard over en variant=40 | package=pyprofane, lang=en variant=40 | no-match | test_detectors_phase2_part_12.py |
| TC-DET-1372 | P2 | pyprofane guard over en variant=41 | package=pyprofane, lang=en variant=41 | no-match | test_detectors_phase2_part_12.py |
| TC-DET-1373 | P2 | pyprofane guard over en variant=42 | package=pyprofane, lang=en variant=42 | no-match | test_detectors_phase2_part_12.py |
| TC-DET-1374 | P2 | pyprofane guard over en variant=43 | package=pyprofane, lang=en variant=43 | no-match | test_detectors_phase2_part_12.py |
| TC-DET-1375 | P2 | pyprofane guard over en variant=44 | package=pyprofane, lang=en variant=44 | no-match | test_detectors_phase2_part_12.py |
| TC-DET-1376 | P2 | pyprofane guard over en variant=45 | package=pyprofane, lang=en variant=45 | no-match | test_detectors_phase2_part_12.py |
| TC-DET-1377 | P2 | pyprofane guard over en variant=46 | package=pyprofane, lang=en variant=46 | no-match | test_detectors_phase2_part_12.py |
| TC-DET-1378 | P2 | pyprofane guard over en variant=47 | package=pyprofane, lang=en variant=47 | no-match | test_detectors_phase2_part_12.py |
| TC-DET-1379 | P2 | pyprofane guard over en variant=48 | package=pyprofane, lang=en variant=48 | no-match | test_detectors_phase2_part_12.py |
| TC-DET-1380 | P2 | pyprofane guard over en variant=49 | package=pyprofane, lang=en variant=49 | no-match | test_detectors_phase2_part_12.py |
| TC-DET-1381 | P2 | pyprofane guard over en variant=50 | package=pyprofane, lang=en variant=50 | no-match | test_detectors_phase2_part_12.py |
| TC-DET-1382 | P2 | pyprofane guard over en variant=51 | package=pyprofane, lang=en variant=51 | no-match | test_detectors_phase2_part_12.py |
| TC-DET-1383 | P2 | pyprofane guard over en variant=52 | package=pyprofane, lang=en variant=52 | no-match | test_detectors_phase2_part_12.py |
| TC-DET-1384 | P2 | pyprofane guard over en variant=53 | package=pyprofane, lang=en variant=53 | no-match | test_detectors_phase2_part_12.py |
| TC-DET-1385 | P2 | pyprofane guard over en variant=54 | package=pyprofane, lang=en variant=54 | no-match | test_detectors_phase2_part_12.py |
| TC-DET-1386 | P2 | pyprofane guard over en variant=55 | package=pyprofane, lang=en variant=55 | no-match | test_detectors_phase2_part_12.py |
| TC-DET-1387 | P2 | pyprofane guard over en variant=56 | package=pyprofane, lang=en variant=56 | no-match | test_detectors_phase2_part_12.py |
| TC-DET-1388 | P2 | pyprofane guard over en variant=57 | package=pyprofane, lang=en variant=57 | no-match | test_detectors_phase2_part_12.py |
| TC-DET-1389 | P2 | pyprofane guard over en variant=58 | package=pyprofane, lang=en variant=58 | no-match | test_detectors_phase2_part_12.py |
| TC-DET-1390 | P2 | pyprofane guard over en variant=59 | package=pyprofane, lang=en variant=59 | no-match | test_detectors_phase2_part_12.py |
| TC-DET-1391 | P2 | pyprofane guard over en variant=60 | package=pyprofane, lang=en variant=60 | no-match | test_detectors_phase2_part_12.py |
| TC-DET-1392 | P2 | pyprofane guard over en variant=61 | package=pyprofane, lang=en variant=61 | no-match | test_detectors_phase2_part_12.py |
| TC-DET-1393 | P2 | pyprofane guard over en variant=62 | package=pyprofane, lang=en variant=62 | no-match | test_detectors_phase2_part_12.py |
| TC-DET-1394 | P2 | pyprofane guard over en variant=63 | package=pyprofane, lang=en variant=63 | no-match | test_detectors_phase2_part_12.py |
| TC-DET-1395 | P2 | pyprofane guard over en variant=64 | package=pyprofane, lang=en variant=64 | no-match | test_detectors_phase2_part_12.py |
| TC-DET-1396 | P2 | pyprofane guard over en variant=65 | package=pyprofane, lang=en variant=65 | no-match | test_detectors_phase2_part_12.py |
| TC-DET-1397 | P2 | pyprofane guard over en variant=66 | package=pyprofane, lang=en variant=66 | no-match | test_detectors_phase2_part_12.py |
| TC-DET-1398 | P2 | pyprofane guard over en variant=67 | package=pyprofane, lang=en variant=67 | no-match | test_detectors_phase2_part_12.py |
| TC-DET-1399 | P2 | pyprofane guard over en variant=68 | package=pyprofane, lang=en variant=68 | no-match | test_detectors_phase2_part_12.py |
| TC-DET-1400 | P2 | pyprofane guard over en variant=69 | package=pyprofane, lang=en variant=69 | no-match | test_detectors_phase2_part_12.py |

### Phase 3 - 20,000 cases
- Planned sweeps over the full dimension matrix, IDs TC-DET-1326 onward.

### Phase 4 - 200,000 cases
- Planned high-scale scenarios, IDs TC-DET-21326 onward.

### Phase 5 - 1,878,675 cases
- Planned exhaustive dimension sweep, IDs TC-DET-221326 onward.

## Implementation Status
| File | Test Cases | Priority | Status |
| :--- | :--- | :--- | :--- |
| test_detectors_phase2_part_1.py | 201-300 | P1 | :white_check_mark: Phase 2 |
| test_detectors_phase2_part_2.py | 301-400 | P1 | :white_check_mark: Phase 2 |
| test_detectors_phase2_part_3.py | 401-500 | P1 | :white_check_mark: Phase 2 |
| test_detectors_phase2_part_4.py | 501-600 | P2 | :white_check_mark: Phase 2 |
| test_detectors_phase2_part_5.py | 601-700 | P1 | :white_check_mark: Phase 2 |
| test_detectors_phase2_part_6.py | 701-800 | P1 | :white_check_mark: Phase 2 |
| test_detectors_phase2_part_7.py | 801-900 | P1 | :white_check_mark: Phase 2 |
| test_detectors_phase2_part_8.py | 901-1000 | P1 | :white_check_mark: Phase 2 |
| test_detectors_phase2_part_9.py | 1001-1100 | P1 | :white_check_mark: Phase 2 |
| test_detectors_phase2_part_10.py | 1101-1200 | P2 | :white_check_mark: Phase 2 |
| test_detectors_phase2_part_11.py | 1201-1300 | P2 | :white_check_mark: Phase 2 |
| test_detectors_phase2_part_12.py | 1301-1400 | P2 | :white_check_mark: Phase 2 |

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
- Detector Architecture
- Algorithm Formulations
