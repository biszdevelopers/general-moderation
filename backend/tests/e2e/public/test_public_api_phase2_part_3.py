"""Phase 2 public moderation API tests (generated).

Language verdict matrices, batch sizes, validation, unicode edges,
profiling flows and response shapes; see tests/tools/phase2_generator.py."""

# multilingual fixtures use non-ASCII on purpose
from __future__ import annotations

from typing import Any

import pytest

from tests.base_test import BaseTest

_BATCH_SIZE_CASES: tuple[tuple[int, int, int], ...] = (
    (2, 0, 6712,),
    (2, 1, 6713,),
    (2, 2, 6714,),
    (2, 3, 6715,),
    (2, 4, 6716,),
    (2, 5, 6717,),
    (2, 6, 6718,),
    (2, 7, 6719,),
    (2, 8, 6720,),
    (2, 9, 6721,),
    (2, 10, 6722,),
    (2, 11, 6723,),
    (2, 12, 6724,),
    (2, 13, 6725,),
    (2, 14, 6726,),
    (5, 0, 6727,),
    (5, 1, 6728,),
    (5, 2, 6729,),
    (5, 3, 6730,),
    (5, 4, 6731,),
    (5, 5, 6732,),
    (5, 6, 6733,),
    (5, 7, 6734,),
    (5, 8, 6735,),
    (5, 9, 6736,),
    (5, 10, 6737,),
    (5, 11, 6738,),
    (5, 12, 6739,),
    (5, 13, 6740,),
    (5, 14, 6741,),
    (10, 0, 6742,),
    (10, 1, 6743,),
    (10, 2, 6744,),
    (10, 3, 6745,),
    (10, 4, 6746,),
    (10, 5, 6747,),
    (10, 6, 6748,),
    (10, 7, 6749,),
    (10, 8, 6750,),
    (10, 9, 6751,),
    (10, 10, 6752,),
    (10, 11, 6753,),
    (10, 12, 6754,),
    (10, 13, 6755,),
    (10, 14, 6756,),
    (25, 0, 6757,),
    (25, 1, 6758,),
    (25, 2, 6759,),
    (25, 3, 6760,),
    (25, 4, 6761,),
    (25, 5, 6762,),
    (25, 6, 6763,),
    (25, 7, 6764,),
    (25, 8, 6765,),
    (25, 9, 6766,),
    (25, 10, 6767,),
    (25, 11, 6768,),
    (25, 12, 6769,),
    (25, 13, 6770,),
    (25, 14, 6771,),
    (50, 0, 6772,),
    (50, 1, 6773,),
    (50, 2, 6774,),
    (50, 3, 6775,),
    (50, 4, 6776,),
    (50, 5, 6777,),
    (50, 6, 6778,),
    (50, 7, 6779,),
    (50, 8, 6780,),
    (50, 9, 6781,),
    (50, 10, 6782,),
    (50, 11, 6783,),
    (50, 12, 6784,),
    (50, 13, 6785,),
    (50, 14, 6786,),
    (75, 0, 6787,),
    (75, 1, 6788,),
    (75, 2, 6789,),
    (75, 3, 6790,),
    (75, 4, 6791,),
    (75, 5, 6792,),
    (75, 6, 6793,),
    (75, 7, 6794,),
    (75, 8, 6795,),
    (75, 9, 6796,),
    (75, 10, 6797,),
    (75, 11, 6798,),
    (75, 12, 6799,),
    (75, 13, 6800,),
    (75, 14, 6801,),
    (100, 0, 6802,),
    (100, 1, 6803,),
    (100, 2, 6804,),
    (100, 3, 6805,),
    (100, 4, 6806,),
    (100, 5, 6807,),
    (100, 6, 6808,),
    (100, 7, 6809,),
    (100, 8, 6810,),
    (100, 9, 6811,),
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
