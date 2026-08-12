# Performance Test Documentation

## Overview
- **Total Planned:** 1,500,000
- **Phase 1:** 0 (README only; Phase-1 sanity covered inside module suites)
- **Phase 2:** 1,500 (IDs TC-PERF-201 to TC-PERF-1,700)
- **Phase 3:** 15,000 (IDs TC-PERF-1,701 to TC-PERF-16,700)
- **Phase 4:** 150,000 (IDs TC-PERF-16,701 to TC-PERF-166,700)
- **Phase 5:** 1,333,300 (IDs TC-PERF-166,701 to TC-PERF-1,500,000)

## Dimension Matrix
| Dimension | Values | Phase 2 | Phase 3 |
| :--- | :--- | :--- | :--- |
| Concurrency | 1, 50, 200 | 50 | 200 |
| Latency target | <1ms, <50ms, <200ms | all | all |
| Throughput | 100, 1000, 10000 req/s | 1000 | 10000 |
| Cache hit rate | 0-100% | 50% | all |
| Payload size | 1-8192 | 1000 | all |

## Planned Benchmarks
- Fast path <1ms, semantic <50ms, full pipeline <200ms.
- P95 latency under 50/200 concurrent load.
- Memory stability over 1-hour soak.

## Adding New Tests
Create `test_performance_part_1.py` with `pytest-benchmark`-style timing
assertions. Commit tag: `TEST-PERF`.

## Related Documentation
- [Performance Targets](../../docs/guide/)
