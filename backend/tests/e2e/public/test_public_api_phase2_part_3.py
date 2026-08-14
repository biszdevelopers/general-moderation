"""Phase 2 public moderation API tests (generated).

Language verdict matrices, batch sizes, validation, unicode edges,
profiling flows and response shapes; see tests/tools/phase2_generator.py."""

# multilingual fixtures use non-ASCII on purpose
from __future__ import annotations

from typing import Any

import pytest

from tests.base_test import BaseTest

_BATCH_SIZE_CASES: tuple[tuple[int, int, int], ...] = (
    (2, 0, 6911,),
    (2, 1, 6912,),
    (2, 2, 6913,),
    (2, 3, 6914,),
    (2, 4, 6915,),
    (2, 5, 6916,),
    (2, 6, 6917,),
    (2, 7, 6918,),
    (2, 8, 6919,),
    (2, 9, 6920,),
    (2, 10, 6921,),
    (2, 11, 6922,),
    (2, 12, 6923,),
    (2, 13, 6924,),
    (2, 14, 6925,),
    (5, 0, 6926,),
    (5, 1, 6927,),
    (5, 2, 6928,),
    (5, 3, 6929,),
    (5, 4, 6930,),
    (5, 5, 6931,),
    (5, 6, 6932,),
    (5, 7, 6933,),
    (5, 8, 6934,),
    (5, 9, 6935,),
    (5, 10, 6936,),
    (5, 11, 6937,),
    (5, 12, 6938,),
    (5, 13, 6939,),
    (5, 14, 6940,),
    (10, 0, 6941,),
    (10, 1, 6942,),
    (10, 2, 6943,),
    (10, 3, 6944,),
    (10, 4, 6945,),
    (10, 5, 6946,),
    (10, 6, 6947,),
    (10, 7, 6948,),
    (10, 8, 6949,),
    (10, 9, 6950,),
    (10, 10, 6951,),
    (10, 11, 6952,),
    (10, 12, 6953,),
    (10, 13, 6954,),
    (10, 14, 6955,),
    (25, 0, 6956,),
    (25, 1, 6957,),
    (25, 2, 6958,),
    (25, 3, 6959,),
    (25, 4, 6960,),
    (25, 5, 6961,),
    (25, 6, 6962,),
    (25, 7, 6963,),
    (25, 8, 6964,),
    (25, 9, 6965,),
    (25, 10, 6966,),
    (25, 11, 6967,),
    (25, 12, 6968,),
    (25, 13, 6969,),
    (25, 14, 6970,),
    (50, 0, 6971,),
    (50, 1, 6972,),
    (50, 2, 6973,),
    (50, 3, 6974,),
    (50, 4, 6975,),
    (50, 5, 6976,),
    (50, 6, 6977,),
    (50, 7, 6978,),
    (50, 8, 6979,),
    (50, 9, 6980,),
    (50, 10, 6981,),
    (50, 11, 6982,),
    (50, 12, 6983,),
    (50, 13, 6984,),
    (50, 14, 6985,),
    (75, 0, 6986,),
    (75, 1, 6987,),
    (75, 2, 6988,),
    (75, 3, 6989,),
    (75, 4, 6990,),
    (75, 5, 6991,),
    (75, 6, 6992,),
    (75, 7, 6993,),
    (75, 8, 6994,),
    (75, 9, 6995,),
    (75, 10, 6996,),
    (75, 11, 6997,),
    (75, 12, 6998,),
    (75, 13, 6999,),
    (75, 14, 7000,),
    (100, 0, 7001,),
    (100, 1, 7002,),
    (100, 2, 7003,),
    (100, 3, 7004,),
    (100, 4, 7005,),
    (100, 5, 7006,),
    (100, 6, 7007,),
    (100, 7, 7008,),
    (100, 8, 7009,),
    (100, 9, 7010,),
)

class TestBatchSize(BaseTest):
    """Batches return one ordered result per item."""

    @pytest.mark.parametrize(('size', 'scenario', 'uid',), _BATCH_SIZE_CASES)
    def test_batch_size(self, client: Any, size: int, scenario: int, uid: int) -> None:
        """Batches return one ordered result per item."""
        items = [{'id': f'i{index}', 'text': f'message {index} v{scenario}', 'app_name': 'a'} for index in range(size)]
        response = client.post('/moderate/batch', json={'items': items})
        assert response.status_code == 200
        results = response.json()['results']
        assert len(results) == size
        assert [result['id'] for result in results] == [f'i{index}' for index in range(size)]
        assert response.json()['totalLatencyMs'] >= 0.0
