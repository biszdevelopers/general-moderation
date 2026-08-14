"""Phase 2 public moderation API tests (generated).

Language verdict matrices, batch sizes, validation, unicode edges,
profiling flows and response shapes; see tests/tools/phase2_generator.py."""

# multilingual fixtures use non-ASCII on purpose
from __future__ import annotations

from typing import Any

import pytest

from tests.base_test import BaseTest

_BATCH_SIZE_CASES: tuple[tuple[int, int, int], ...] = (
    (2, 0, 6871,),
    (2, 1, 6872,),
    (2, 2, 6873,),
    (2, 3, 6874,),
    (2, 4, 6875,),
    (2, 5, 6876,),
    (2, 6, 6877,),
    (2, 7, 6878,),
    (2, 8, 6879,),
    (2, 9, 6880,),
    (2, 10, 6881,),
    (2, 11, 6882,),
    (2, 12, 6883,),
    (2, 13, 6884,),
    (2, 14, 6885,),
    (5, 0, 6886,),
    (5, 1, 6887,),
    (5, 2, 6888,),
    (5, 3, 6889,),
    (5, 4, 6890,),
    (5, 5, 6891,),
    (5, 6, 6892,),
    (5, 7, 6893,),
    (5, 8, 6894,),
    (5, 9, 6895,),
    (5, 10, 6896,),
    (5, 11, 6897,),
    (5, 12, 6898,),
    (5, 13, 6899,),
    (5, 14, 6900,),
    (10, 0, 6901,),
    (10, 1, 6902,),
    (10, 2, 6903,),
    (10, 3, 6904,),
    (10, 4, 6905,),
    (10, 5, 6906,),
    (10, 6, 6907,),
    (10, 7, 6908,),
    (10, 8, 6909,),
    (10, 9, 6910,),
    (10, 10, 6911,),
    (10, 11, 6912,),
    (10, 12, 6913,),
    (10, 13, 6914,),
    (10, 14, 6915,),
    (25, 0, 6916,),
    (25, 1, 6917,),
    (25, 2, 6918,),
    (25, 3, 6919,),
    (25, 4, 6920,),
    (25, 5, 6921,),
    (25, 6, 6922,),
    (25, 7, 6923,),
    (25, 8, 6924,),
    (25, 9, 6925,),
    (25, 10, 6926,),
    (25, 11, 6927,),
    (25, 12, 6928,),
    (25, 13, 6929,),
    (25, 14, 6930,),
    (50, 0, 6931,),
    (50, 1, 6932,),
    (50, 2, 6933,),
    (50, 3, 6934,),
    (50, 4, 6935,),
    (50, 5, 6936,),
    (50, 6, 6937,),
    (50, 7, 6938,),
    (50, 8, 6939,),
    (50, 9, 6940,),
    (50, 10, 6941,),
    (50, 11, 6942,),
    (50, 12, 6943,),
    (50, 13, 6944,),
    (50, 14, 6945,),
    (75, 0, 6946,),
    (75, 1, 6947,),
    (75, 2, 6948,),
    (75, 3, 6949,),
    (75, 4, 6950,),
    (75, 5, 6951,),
    (75, 6, 6952,),
    (75, 7, 6953,),
    (75, 8, 6954,),
    (75, 9, 6955,),
    (75, 10, 6956,),
    (75, 11, 6957,),
    (75, 12, 6958,),
    (75, 13, 6959,),
    (75, 14, 6960,),
    (100, 0, 6961,),
    (100, 1, 6962,),
    (100, 2, 6963,),
    (100, 3, 6964,),
    (100, 4, 6965,),
    (100, 5, 6966,),
    (100, 6, 6967,),
    (100, 7, 6968,),
    (100, 8, 6969,),
    (100, 9, 6970,),
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
