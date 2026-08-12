"""Phase 2 public moderation API tests (generated).

Language verdict matrices, batch sizes, validation, unicode edges,
profiling flows and response shapes; see tests/tools/phase2_generator.py."""

# multilingual fixtures use non-ASCII on purpose
from __future__ import annotations

from typing import Any

from tests.base_test import BaseTest


class TestBatchSizes(BaseTest):
    """BatchSizes scenarios."""

    def test_batch_size_2_0_6712(self, client: Any) -> None:
        """Batches return one ordered result per item."""
        items = [
            {"id": f"i{index}", "text": f"message {index}", "app_name": "a"} for index in range(2)
        ]
        response = client.post("/moderate/batch", json={"items": items})
        assert response.status_code == 200
        results = response.json()["results"]
        assert len(results) == 2
        assert [result["id"] for result in results] == [f"i{index}" for index in range(2)]
        assert response.json()["totalLatencyMs"] >= 0.0

    def test_batch_size_2_1_6713(self, client: Any) -> None:
        """Batches return one ordered result per item."""
        items = [
            {"id": f"i{index}", "text": f"message {index}", "app_name": "a"} for index in range(2)
        ]
        response = client.post("/moderate/batch", json={"items": items})
        assert response.status_code == 200
        results = response.json()["results"]
        assert len(results) == 2
        assert [result["id"] for result in results] == [f"i{index}" for index in range(2)]
        assert response.json()["totalLatencyMs"] >= 0.0

    def test_batch_size_2_2_6714(self, client: Any) -> None:
        """Batches return one ordered result per item."""
        items = [
            {"id": f"i{index}", "text": f"message {index}", "app_name": "a"} for index in range(2)
        ]
        response = client.post("/moderate/batch", json={"items": items})
        assert response.status_code == 200
        results = response.json()["results"]
        assert len(results) == 2
        assert [result["id"] for result in results] == [f"i{index}" for index in range(2)]
        assert response.json()["totalLatencyMs"] >= 0.0

    def test_batch_size_2_3_6715(self, client: Any) -> None:
        """Batches return one ordered result per item."""
        items = [
            {"id": f"i{index}", "text": f"message {index}", "app_name": "a"} for index in range(2)
        ]
        response = client.post("/moderate/batch", json={"items": items})
        assert response.status_code == 200
        results = response.json()["results"]
        assert len(results) == 2
        assert [result["id"] for result in results] == [f"i{index}" for index in range(2)]
        assert response.json()["totalLatencyMs"] >= 0.0

    def test_batch_size_2_4_6716(self, client: Any) -> None:
        """Batches return one ordered result per item."""
        items = [
            {"id": f"i{index}", "text": f"message {index}", "app_name": "a"} for index in range(2)
        ]
        response = client.post("/moderate/batch", json={"items": items})
        assert response.status_code == 200
        results = response.json()["results"]
        assert len(results) == 2
        assert [result["id"] for result in results] == [f"i{index}" for index in range(2)]
        assert response.json()["totalLatencyMs"] >= 0.0

    def test_batch_size_2_5_6717(self, client: Any) -> None:
        """Batches return one ordered result per item."""
        items = [
            {"id": f"i{index}", "text": f"message {index}", "app_name": "a"} for index in range(2)
        ]
        response = client.post("/moderate/batch", json={"items": items})
        assert response.status_code == 200
        results = response.json()["results"]
        assert len(results) == 2
        assert [result["id"] for result in results] == [f"i{index}" for index in range(2)]
        assert response.json()["totalLatencyMs"] >= 0.0

    def test_batch_size_2_6_6718(self, client: Any) -> None:
        """Batches return one ordered result per item."""
        items = [
            {"id": f"i{index}", "text": f"message {index}", "app_name": "a"} for index in range(2)
        ]
        response = client.post("/moderate/batch", json={"items": items})
        assert response.status_code == 200
        results = response.json()["results"]
        assert len(results) == 2
        assert [result["id"] for result in results] == [f"i{index}" for index in range(2)]
        assert response.json()["totalLatencyMs"] >= 0.0

    def test_batch_size_2_7_6719(self, client: Any) -> None:
        """Batches return one ordered result per item."""
        items = [
            {"id": f"i{index}", "text": f"message {index}", "app_name": "a"} for index in range(2)
        ]
        response = client.post("/moderate/batch", json={"items": items})
        assert response.status_code == 200
        results = response.json()["results"]
        assert len(results) == 2
        assert [result["id"] for result in results] == [f"i{index}" for index in range(2)]
        assert response.json()["totalLatencyMs"] >= 0.0

    def test_batch_size_2_8_6720(self, client: Any) -> None:
        """Batches return one ordered result per item."""
        items = [
            {"id": f"i{index}", "text": f"message {index}", "app_name": "a"} for index in range(2)
        ]
        response = client.post("/moderate/batch", json={"items": items})
        assert response.status_code == 200
        results = response.json()["results"]
        assert len(results) == 2
        assert [result["id"] for result in results] == [f"i{index}" for index in range(2)]
        assert response.json()["totalLatencyMs"] >= 0.0

    def test_batch_size_2_9_6721(self, client: Any) -> None:
        """Batches return one ordered result per item."""
        items = [
            {"id": f"i{index}", "text": f"message {index}", "app_name": "a"} for index in range(2)
        ]
        response = client.post("/moderate/batch", json={"items": items})
        assert response.status_code == 200
        results = response.json()["results"]
        assert len(results) == 2
        assert [result["id"] for result in results] == [f"i{index}" for index in range(2)]
        assert response.json()["totalLatencyMs"] >= 0.0

    def test_batch_size_2_10_6722(self, client: Any) -> None:
        """Batches return one ordered result per item."""
        items = [
            {"id": f"i{index}", "text": f"message {index}", "app_name": "a"} for index in range(2)
        ]
        response = client.post("/moderate/batch", json={"items": items})
        assert response.status_code == 200
        results = response.json()["results"]
        assert len(results) == 2
        assert [result["id"] for result in results] == [f"i{index}" for index in range(2)]
        assert response.json()["totalLatencyMs"] >= 0.0

    def test_batch_size_2_11_6723(self, client: Any) -> None:
        """Batches return one ordered result per item."""
        items = [
            {"id": f"i{index}", "text": f"message {index}", "app_name": "a"} for index in range(2)
        ]
        response = client.post("/moderate/batch", json={"items": items})
        assert response.status_code == 200
        results = response.json()["results"]
        assert len(results) == 2
        assert [result["id"] for result in results] == [f"i{index}" for index in range(2)]
        assert response.json()["totalLatencyMs"] >= 0.0

    def test_batch_size_2_12_6724(self, client: Any) -> None:
        """Batches return one ordered result per item."""
        items = [
            {"id": f"i{index}", "text": f"message {index}", "app_name": "a"} for index in range(2)
        ]
        response = client.post("/moderate/batch", json={"items": items})
        assert response.status_code == 200
        results = response.json()["results"]
        assert len(results) == 2
        assert [result["id"] for result in results] == [f"i{index}" for index in range(2)]
        assert response.json()["totalLatencyMs"] >= 0.0

    def test_batch_size_2_13_6725(self, client: Any) -> None:
        """Batches return one ordered result per item."""
        items = [
            {"id": f"i{index}", "text": f"message {index}", "app_name": "a"} for index in range(2)
        ]
        response = client.post("/moderate/batch", json={"items": items})
        assert response.status_code == 200
        results = response.json()["results"]
        assert len(results) == 2
        assert [result["id"] for result in results] == [f"i{index}" for index in range(2)]
        assert response.json()["totalLatencyMs"] >= 0.0

    def test_batch_size_2_14_6726(self, client: Any) -> None:
        """Batches return one ordered result per item."""
        items = [
            {"id": f"i{index}", "text": f"message {index}", "app_name": "a"} for index in range(2)
        ]
        response = client.post("/moderate/batch", json={"items": items})
        assert response.status_code == 200
        results = response.json()["results"]
        assert len(results) == 2
        assert [result["id"] for result in results] == [f"i{index}" for index in range(2)]
        assert response.json()["totalLatencyMs"] >= 0.0

    def test_batch_size_5_0_6727(self, client: Any) -> None:
        """Batches return one ordered result per item."""
        items = [
            {"id": f"i{index}", "text": f"message {index}", "app_name": "a"} for index in range(5)
        ]
        response = client.post("/moderate/batch", json={"items": items})
        assert response.status_code == 200
        results = response.json()["results"]
        assert len(results) == 5
        assert [result["id"] for result in results] == [f"i{index}" for index in range(5)]
        assert response.json()["totalLatencyMs"] >= 0.0

    def test_batch_size_5_1_6728(self, client: Any) -> None:
        """Batches return one ordered result per item."""
        items = [
            {"id": f"i{index}", "text": f"message {index}", "app_name": "a"} for index in range(5)
        ]
        response = client.post("/moderate/batch", json={"items": items})
        assert response.status_code == 200
        results = response.json()["results"]
        assert len(results) == 5
        assert [result["id"] for result in results] == [f"i{index}" for index in range(5)]
        assert response.json()["totalLatencyMs"] >= 0.0

    def test_batch_size_5_2_6729(self, client: Any) -> None:
        """Batches return one ordered result per item."""
        items = [
            {"id": f"i{index}", "text": f"message {index}", "app_name": "a"} for index in range(5)
        ]
        response = client.post("/moderate/batch", json={"items": items})
        assert response.status_code == 200
        results = response.json()["results"]
        assert len(results) == 5
        assert [result["id"] for result in results] == [f"i{index}" for index in range(5)]
        assert response.json()["totalLatencyMs"] >= 0.0

    def test_batch_size_5_3_6730(self, client: Any) -> None:
        """Batches return one ordered result per item."""
        items = [
            {"id": f"i{index}", "text": f"message {index}", "app_name": "a"} for index in range(5)
        ]
        response = client.post("/moderate/batch", json={"items": items})
        assert response.status_code == 200
        results = response.json()["results"]
        assert len(results) == 5
        assert [result["id"] for result in results] == [f"i{index}" for index in range(5)]
        assert response.json()["totalLatencyMs"] >= 0.0

    def test_batch_size_5_4_6731(self, client: Any) -> None:
        """Batches return one ordered result per item."""
        items = [
            {"id": f"i{index}", "text": f"message {index}", "app_name": "a"} for index in range(5)
        ]
        response = client.post("/moderate/batch", json={"items": items})
        assert response.status_code == 200
        results = response.json()["results"]
        assert len(results) == 5
        assert [result["id"] for result in results] == [f"i{index}" for index in range(5)]
        assert response.json()["totalLatencyMs"] >= 0.0

    def test_batch_size_5_5_6732(self, client: Any) -> None:
        """Batches return one ordered result per item."""
        items = [
            {"id": f"i{index}", "text": f"message {index}", "app_name": "a"} for index in range(5)
        ]
        response = client.post("/moderate/batch", json={"items": items})
        assert response.status_code == 200
        results = response.json()["results"]
        assert len(results) == 5
        assert [result["id"] for result in results] == [f"i{index}" for index in range(5)]
        assert response.json()["totalLatencyMs"] >= 0.0

    def test_batch_size_5_6_6733(self, client: Any) -> None:
        """Batches return one ordered result per item."""
        items = [
            {"id": f"i{index}", "text": f"message {index}", "app_name": "a"} for index in range(5)
        ]
        response = client.post("/moderate/batch", json={"items": items})
        assert response.status_code == 200
        results = response.json()["results"]
        assert len(results) == 5
        assert [result["id"] for result in results] == [f"i{index}" for index in range(5)]
        assert response.json()["totalLatencyMs"] >= 0.0

    def test_batch_size_5_7_6734(self, client: Any) -> None:
        """Batches return one ordered result per item."""
        items = [
            {"id": f"i{index}", "text": f"message {index}", "app_name": "a"} for index in range(5)
        ]
        response = client.post("/moderate/batch", json={"items": items})
        assert response.status_code == 200
        results = response.json()["results"]
        assert len(results) == 5
        assert [result["id"] for result in results] == [f"i{index}" for index in range(5)]
        assert response.json()["totalLatencyMs"] >= 0.0

    def test_batch_size_5_8_6735(self, client: Any) -> None:
        """Batches return one ordered result per item."""
        items = [
            {"id": f"i{index}", "text": f"message {index}", "app_name": "a"} for index in range(5)
        ]
        response = client.post("/moderate/batch", json={"items": items})
        assert response.status_code == 200
        results = response.json()["results"]
        assert len(results) == 5
        assert [result["id"] for result in results] == [f"i{index}" for index in range(5)]
        assert response.json()["totalLatencyMs"] >= 0.0

    def test_batch_size_5_9_6736(self, client: Any) -> None:
        """Batches return one ordered result per item."""
        items = [
            {"id": f"i{index}", "text": f"message {index}", "app_name": "a"} for index in range(5)
        ]
        response = client.post("/moderate/batch", json={"items": items})
        assert response.status_code == 200
        results = response.json()["results"]
        assert len(results) == 5
        assert [result["id"] for result in results] == [f"i{index}" for index in range(5)]
        assert response.json()["totalLatencyMs"] >= 0.0

    def test_batch_size_5_10_6737(self, client: Any) -> None:
        """Batches return one ordered result per item."""
        items = [
            {"id": f"i{index}", "text": f"message {index}", "app_name": "a"} for index in range(5)
        ]
        response = client.post("/moderate/batch", json={"items": items})
        assert response.status_code == 200
        results = response.json()["results"]
        assert len(results) == 5
        assert [result["id"] for result in results] == [f"i{index}" for index in range(5)]
        assert response.json()["totalLatencyMs"] >= 0.0

    def test_batch_size_5_11_6738(self, client: Any) -> None:
        """Batches return one ordered result per item."""
        items = [
            {"id": f"i{index}", "text": f"message {index}", "app_name": "a"} for index in range(5)
        ]
        response = client.post("/moderate/batch", json={"items": items})
        assert response.status_code == 200
        results = response.json()["results"]
        assert len(results) == 5
        assert [result["id"] for result in results] == [f"i{index}" for index in range(5)]
        assert response.json()["totalLatencyMs"] >= 0.0

    def test_batch_size_5_12_6739(self, client: Any) -> None:
        """Batches return one ordered result per item."""
        items = [
            {"id": f"i{index}", "text": f"message {index}", "app_name": "a"} for index in range(5)
        ]
        response = client.post("/moderate/batch", json={"items": items})
        assert response.status_code == 200
        results = response.json()["results"]
        assert len(results) == 5
        assert [result["id"] for result in results] == [f"i{index}" for index in range(5)]
        assert response.json()["totalLatencyMs"] >= 0.0

    def test_batch_size_5_13_6740(self, client: Any) -> None:
        """Batches return one ordered result per item."""
        items = [
            {"id": f"i{index}", "text": f"message {index}", "app_name": "a"} for index in range(5)
        ]
        response = client.post("/moderate/batch", json={"items": items})
        assert response.status_code == 200
        results = response.json()["results"]
        assert len(results) == 5
        assert [result["id"] for result in results] == [f"i{index}" for index in range(5)]
        assert response.json()["totalLatencyMs"] >= 0.0

    def test_batch_size_5_14_6741(self, client: Any) -> None:
        """Batches return one ordered result per item."""
        items = [
            {"id": f"i{index}", "text": f"message {index}", "app_name": "a"} for index in range(5)
        ]
        response = client.post("/moderate/batch", json={"items": items})
        assert response.status_code == 200
        results = response.json()["results"]
        assert len(results) == 5
        assert [result["id"] for result in results] == [f"i{index}" for index in range(5)]
        assert response.json()["totalLatencyMs"] >= 0.0

    def test_batch_size_10_0_6742(self, client: Any) -> None:
        """Batches return one ordered result per item."""
        items = [
            {"id": f"i{index}", "text": f"message {index}", "app_name": "a"} for index in range(10)
        ]
        response = client.post("/moderate/batch", json={"items": items})
        assert response.status_code == 200
        results = response.json()["results"]
        assert len(results) == 10
        assert [result["id"] for result in results] == [f"i{index}" for index in range(10)]
        assert response.json()["totalLatencyMs"] >= 0.0

    def test_batch_size_10_1_6743(self, client: Any) -> None:
        """Batches return one ordered result per item."""
        items = [
            {"id": f"i{index}", "text": f"message {index}", "app_name": "a"} for index in range(10)
        ]
        response = client.post("/moderate/batch", json={"items": items})
        assert response.status_code == 200
        results = response.json()["results"]
        assert len(results) == 10
        assert [result["id"] for result in results] == [f"i{index}" for index in range(10)]
        assert response.json()["totalLatencyMs"] >= 0.0

    def test_batch_size_10_2_6744(self, client: Any) -> None:
        """Batches return one ordered result per item."""
        items = [
            {"id": f"i{index}", "text": f"message {index}", "app_name": "a"} for index in range(10)
        ]
        response = client.post("/moderate/batch", json={"items": items})
        assert response.status_code == 200
        results = response.json()["results"]
        assert len(results) == 10
        assert [result["id"] for result in results] == [f"i{index}" for index in range(10)]
        assert response.json()["totalLatencyMs"] >= 0.0

    def test_batch_size_10_3_6745(self, client: Any) -> None:
        """Batches return one ordered result per item."""
        items = [
            {"id": f"i{index}", "text": f"message {index}", "app_name": "a"} for index in range(10)
        ]
        response = client.post("/moderate/batch", json={"items": items})
        assert response.status_code == 200
        results = response.json()["results"]
        assert len(results) == 10
        assert [result["id"] for result in results] == [f"i{index}" for index in range(10)]
        assert response.json()["totalLatencyMs"] >= 0.0

    def test_batch_size_10_4_6746(self, client: Any) -> None:
        """Batches return one ordered result per item."""
        items = [
            {"id": f"i{index}", "text": f"message {index}", "app_name": "a"} for index in range(10)
        ]
        response = client.post("/moderate/batch", json={"items": items})
        assert response.status_code == 200
        results = response.json()["results"]
        assert len(results) == 10
        assert [result["id"] for result in results] == [f"i{index}" for index in range(10)]
        assert response.json()["totalLatencyMs"] >= 0.0

    def test_batch_size_10_5_6747(self, client: Any) -> None:
        """Batches return one ordered result per item."""
        items = [
            {"id": f"i{index}", "text": f"message {index}", "app_name": "a"} for index in range(10)
        ]
        response = client.post("/moderate/batch", json={"items": items})
        assert response.status_code == 200
        results = response.json()["results"]
        assert len(results) == 10
        assert [result["id"] for result in results] == [f"i{index}" for index in range(10)]
        assert response.json()["totalLatencyMs"] >= 0.0

    def test_batch_size_10_6_6748(self, client: Any) -> None:
        """Batches return one ordered result per item."""
        items = [
            {"id": f"i{index}", "text": f"message {index}", "app_name": "a"} for index in range(10)
        ]
        response = client.post("/moderate/batch", json={"items": items})
        assert response.status_code == 200
        results = response.json()["results"]
        assert len(results) == 10
        assert [result["id"] for result in results] == [f"i{index}" for index in range(10)]
        assert response.json()["totalLatencyMs"] >= 0.0

    def test_batch_size_10_7_6749(self, client: Any) -> None:
        """Batches return one ordered result per item."""
        items = [
            {"id": f"i{index}", "text": f"message {index}", "app_name": "a"} for index in range(10)
        ]
        response = client.post("/moderate/batch", json={"items": items})
        assert response.status_code == 200
        results = response.json()["results"]
        assert len(results) == 10
        assert [result["id"] for result in results] == [f"i{index}" for index in range(10)]
        assert response.json()["totalLatencyMs"] >= 0.0

    def test_batch_size_10_8_6750(self, client: Any) -> None:
        """Batches return one ordered result per item."""
        items = [
            {"id": f"i{index}", "text": f"message {index}", "app_name": "a"} for index in range(10)
        ]
        response = client.post("/moderate/batch", json={"items": items})
        assert response.status_code == 200
        results = response.json()["results"]
        assert len(results) == 10
        assert [result["id"] for result in results] == [f"i{index}" for index in range(10)]
        assert response.json()["totalLatencyMs"] >= 0.0

    def test_batch_size_10_9_6751(self, client: Any) -> None:
        """Batches return one ordered result per item."""
        items = [
            {"id": f"i{index}", "text": f"message {index}", "app_name": "a"} for index in range(10)
        ]
        response = client.post("/moderate/batch", json={"items": items})
        assert response.status_code == 200
        results = response.json()["results"]
        assert len(results) == 10
        assert [result["id"] for result in results] == [f"i{index}" for index in range(10)]
        assert response.json()["totalLatencyMs"] >= 0.0

    def test_batch_size_10_10_6752(self, client: Any) -> None:
        """Batches return one ordered result per item."""
        items = [
            {"id": f"i{index}", "text": f"message {index}", "app_name": "a"} for index in range(10)
        ]
        response = client.post("/moderate/batch", json={"items": items})
        assert response.status_code == 200
        results = response.json()["results"]
        assert len(results) == 10
        assert [result["id"] for result in results] == [f"i{index}" for index in range(10)]
        assert response.json()["totalLatencyMs"] >= 0.0

    def test_batch_size_10_11_6753(self, client: Any) -> None:
        """Batches return one ordered result per item."""
        items = [
            {"id": f"i{index}", "text": f"message {index}", "app_name": "a"} for index in range(10)
        ]
        response = client.post("/moderate/batch", json={"items": items})
        assert response.status_code == 200
        results = response.json()["results"]
        assert len(results) == 10
        assert [result["id"] for result in results] == [f"i{index}" for index in range(10)]
        assert response.json()["totalLatencyMs"] >= 0.0

    def test_batch_size_10_12_6754(self, client: Any) -> None:
        """Batches return one ordered result per item."""
        items = [
            {"id": f"i{index}", "text": f"message {index}", "app_name": "a"} for index in range(10)
        ]
        response = client.post("/moderate/batch", json={"items": items})
        assert response.status_code == 200
        results = response.json()["results"]
        assert len(results) == 10
        assert [result["id"] for result in results] == [f"i{index}" for index in range(10)]
        assert response.json()["totalLatencyMs"] >= 0.0

    def test_batch_size_10_13_6755(self, client: Any) -> None:
        """Batches return one ordered result per item."""
        items = [
            {"id": f"i{index}", "text": f"message {index}", "app_name": "a"} for index in range(10)
        ]
        response = client.post("/moderate/batch", json={"items": items})
        assert response.status_code == 200
        results = response.json()["results"]
        assert len(results) == 10
        assert [result["id"] for result in results] == [f"i{index}" for index in range(10)]
        assert response.json()["totalLatencyMs"] >= 0.0

    def test_batch_size_10_14_6756(self, client: Any) -> None:
        """Batches return one ordered result per item."""
        items = [
            {"id": f"i{index}", "text": f"message {index}", "app_name": "a"} for index in range(10)
        ]
        response = client.post("/moderate/batch", json={"items": items})
        assert response.status_code == 200
        results = response.json()["results"]
        assert len(results) == 10
        assert [result["id"] for result in results] == [f"i{index}" for index in range(10)]
        assert response.json()["totalLatencyMs"] >= 0.0

    def test_batch_size_25_0_6757(self, client: Any) -> None:
        """Batches return one ordered result per item."""
        items = [
            {"id": f"i{index}", "text": f"message {index}", "app_name": "a"} for index in range(25)
        ]
        response = client.post("/moderate/batch", json={"items": items})
        assert response.status_code == 200
        results = response.json()["results"]
        assert len(results) == 25
        assert [result["id"] for result in results] == [f"i{index}" for index in range(25)]
        assert response.json()["totalLatencyMs"] >= 0.0

    def test_batch_size_25_1_6758(self, client: Any) -> None:
        """Batches return one ordered result per item."""
        items = [
            {"id": f"i{index}", "text": f"message {index}", "app_name": "a"} for index in range(25)
        ]
        response = client.post("/moderate/batch", json={"items": items})
        assert response.status_code == 200
        results = response.json()["results"]
        assert len(results) == 25
        assert [result["id"] for result in results] == [f"i{index}" for index in range(25)]
        assert response.json()["totalLatencyMs"] >= 0.0

    def test_batch_size_25_2_6759(self, client: Any) -> None:
        """Batches return one ordered result per item."""
        items = [
            {"id": f"i{index}", "text": f"message {index}", "app_name": "a"} for index in range(25)
        ]
        response = client.post("/moderate/batch", json={"items": items})
        assert response.status_code == 200
        results = response.json()["results"]
        assert len(results) == 25
        assert [result["id"] for result in results] == [f"i{index}" for index in range(25)]
        assert response.json()["totalLatencyMs"] >= 0.0

    def test_batch_size_25_3_6760(self, client: Any) -> None:
        """Batches return one ordered result per item."""
        items = [
            {"id": f"i{index}", "text": f"message {index}", "app_name": "a"} for index in range(25)
        ]
        response = client.post("/moderate/batch", json={"items": items})
        assert response.status_code == 200
        results = response.json()["results"]
        assert len(results) == 25
        assert [result["id"] for result in results] == [f"i{index}" for index in range(25)]
        assert response.json()["totalLatencyMs"] >= 0.0

    def test_batch_size_25_4_6761(self, client: Any) -> None:
        """Batches return one ordered result per item."""
        items = [
            {"id": f"i{index}", "text": f"message {index}", "app_name": "a"} for index in range(25)
        ]
        response = client.post("/moderate/batch", json={"items": items})
        assert response.status_code == 200
        results = response.json()["results"]
        assert len(results) == 25
        assert [result["id"] for result in results] == [f"i{index}" for index in range(25)]
        assert response.json()["totalLatencyMs"] >= 0.0

    def test_batch_size_25_5_6762(self, client: Any) -> None:
        """Batches return one ordered result per item."""
        items = [
            {"id": f"i{index}", "text": f"message {index}", "app_name": "a"} for index in range(25)
        ]
        response = client.post("/moderate/batch", json={"items": items})
        assert response.status_code == 200
        results = response.json()["results"]
        assert len(results) == 25
        assert [result["id"] for result in results] == [f"i{index}" for index in range(25)]
        assert response.json()["totalLatencyMs"] >= 0.0

    def test_batch_size_25_6_6763(self, client: Any) -> None:
        """Batches return one ordered result per item."""
        items = [
            {"id": f"i{index}", "text": f"message {index}", "app_name": "a"} for index in range(25)
        ]
        response = client.post("/moderate/batch", json={"items": items})
        assert response.status_code == 200
        results = response.json()["results"]
        assert len(results) == 25
        assert [result["id"] for result in results] == [f"i{index}" for index in range(25)]
        assert response.json()["totalLatencyMs"] >= 0.0

    def test_batch_size_25_7_6764(self, client: Any) -> None:
        """Batches return one ordered result per item."""
        items = [
            {"id": f"i{index}", "text": f"message {index}", "app_name": "a"} for index in range(25)
        ]
        response = client.post("/moderate/batch", json={"items": items})
        assert response.status_code == 200
        results = response.json()["results"]
        assert len(results) == 25
        assert [result["id"] for result in results] == [f"i{index}" for index in range(25)]
        assert response.json()["totalLatencyMs"] >= 0.0

    def test_batch_size_25_8_6765(self, client: Any) -> None:
        """Batches return one ordered result per item."""
        items = [
            {"id": f"i{index}", "text": f"message {index}", "app_name": "a"} for index in range(25)
        ]
        response = client.post("/moderate/batch", json={"items": items})
        assert response.status_code == 200
        results = response.json()["results"]
        assert len(results) == 25
        assert [result["id"] for result in results] == [f"i{index}" for index in range(25)]
        assert response.json()["totalLatencyMs"] >= 0.0

    def test_batch_size_25_9_6766(self, client: Any) -> None:
        """Batches return one ordered result per item."""
        items = [
            {"id": f"i{index}", "text": f"message {index}", "app_name": "a"} for index in range(25)
        ]
        response = client.post("/moderate/batch", json={"items": items})
        assert response.status_code == 200
        results = response.json()["results"]
        assert len(results) == 25
        assert [result["id"] for result in results] == [f"i{index}" for index in range(25)]
        assert response.json()["totalLatencyMs"] >= 0.0

    def test_batch_size_25_10_6767(self, client: Any) -> None:
        """Batches return one ordered result per item."""
        items = [
            {"id": f"i{index}", "text": f"message {index}", "app_name": "a"} for index in range(25)
        ]
        response = client.post("/moderate/batch", json={"items": items})
        assert response.status_code == 200
        results = response.json()["results"]
        assert len(results) == 25
        assert [result["id"] for result in results] == [f"i{index}" for index in range(25)]
        assert response.json()["totalLatencyMs"] >= 0.0

    def test_batch_size_25_11_6768(self, client: Any) -> None:
        """Batches return one ordered result per item."""
        items = [
            {"id": f"i{index}", "text": f"message {index}", "app_name": "a"} for index in range(25)
        ]
        response = client.post("/moderate/batch", json={"items": items})
        assert response.status_code == 200
        results = response.json()["results"]
        assert len(results) == 25
        assert [result["id"] for result in results] == [f"i{index}" for index in range(25)]
        assert response.json()["totalLatencyMs"] >= 0.0

    def test_batch_size_25_12_6769(self, client: Any) -> None:
        """Batches return one ordered result per item."""
        items = [
            {"id": f"i{index}", "text": f"message {index}", "app_name": "a"} for index in range(25)
        ]
        response = client.post("/moderate/batch", json={"items": items})
        assert response.status_code == 200
        results = response.json()["results"]
        assert len(results) == 25
        assert [result["id"] for result in results] == [f"i{index}" for index in range(25)]
        assert response.json()["totalLatencyMs"] >= 0.0

    def test_batch_size_25_13_6770(self, client: Any) -> None:
        """Batches return one ordered result per item."""
        items = [
            {"id": f"i{index}", "text": f"message {index}", "app_name": "a"} for index in range(25)
        ]
        response = client.post("/moderate/batch", json={"items": items})
        assert response.status_code == 200
        results = response.json()["results"]
        assert len(results) == 25
        assert [result["id"] for result in results] == [f"i{index}" for index in range(25)]
        assert response.json()["totalLatencyMs"] >= 0.0

    def test_batch_size_25_14_6771(self, client: Any) -> None:
        """Batches return one ordered result per item."""
        items = [
            {"id": f"i{index}", "text": f"message {index}", "app_name": "a"} for index in range(25)
        ]
        response = client.post("/moderate/batch", json={"items": items})
        assert response.status_code == 200
        results = response.json()["results"]
        assert len(results) == 25
        assert [result["id"] for result in results] == [f"i{index}" for index in range(25)]
        assert response.json()["totalLatencyMs"] >= 0.0

    def test_batch_size_50_0_6772(self, client: Any) -> None:
        """Batches return one ordered result per item."""
        items = [
            {"id": f"i{index}", "text": f"message {index}", "app_name": "a"} for index in range(50)
        ]
        response = client.post("/moderate/batch", json={"items": items})
        assert response.status_code == 200
        results = response.json()["results"]
        assert len(results) == 50
        assert [result["id"] for result in results] == [f"i{index}" for index in range(50)]
        assert response.json()["totalLatencyMs"] >= 0.0

    def test_batch_size_50_1_6773(self, client: Any) -> None:
        """Batches return one ordered result per item."""
        items = [
            {"id": f"i{index}", "text": f"message {index}", "app_name": "a"} for index in range(50)
        ]
        response = client.post("/moderate/batch", json={"items": items})
        assert response.status_code == 200
        results = response.json()["results"]
        assert len(results) == 50
        assert [result["id"] for result in results] == [f"i{index}" for index in range(50)]
        assert response.json()["totalLatencyMs"] >= 0.0

    def test_batch_size_50_2_6774(self, client: Any) -> None:
        """Batches return one ordered result per item."""
        items = [
            {"id": f"i{index}", "text": f"message {index}", "app_name": "a"} for index in range(50)
        ]
        response = client.post("/moderate/batch", json={"items": items})
        assert response.status_code == 200
        results = response.json()["results"]
        assert len(results) == 50
        assert [result["id"] for result in results] == [f"i{index}" for index in range(50)]
        assert response.json()["totalLatencyMs"] >= 0.0

    def test_batch_size_50_3_6775(self, client: Any) -> None:
        """Batches return one ordered result per item."""
        items = [
            {"id": f"i{index}", "text": f"message {index}", "app_name": "a"} for index in range(50)
        ]
        response = client.post("/moderate/batch", json={"items": items})
        assert response.status_code == 200
        results = response.json()["results"]
        assert len(results) == 50
        assert [result["id"] for result in results] == [f"i{index}" for index in range(50)]
        assert response.json()["totalLatencyMs"] >= 0.0

    def test_batch_size_50_4_6776(self, client: Any) -> None:
        """Batches return one ordered result per item."""
        items = [
            {"id": f"i{index}", "text": f"message {index}", "app_name": "a"} for index in range(50)
        ]
        response = client.post("/moderate/batch", json={"items": items})
        assert response.status_code == 200
        results = response.json()["results"]
        assert len(results) == 50
        assert [result["id"] for result in results] == [f"i{index}" for index in range(50)]
        assert response.json()["totalLatencyMs"] >= 0.0

    def test_batch_size_50_5_6777(self, client: Any) -> None:
        """Batches return one ordered result per item."""
        items = [
            {"id": f"i{index}", "text": f"message {index}", "app_name": "a"} for index in range(50)
        ]
        response = client.post("/moderate/batch", json={"items": items})
        assert response.status_code == 200
        results = response.json()["results"]
        assert len(results) == 50
        assert [result["id"] for result in results] == [f"i{index}" for index in range(50)]
        assert response.json()["totalLatencyMs"] >= 0.0

    def test_batch_size_50_6_6778(self, client: Any) -> None:
        """Batches return one ordered result per item."""
        items = [
            {"id": f"i{index}", "text": f"message {index}", "app_name": "a"} for index in range(50)
        ]
        response = client.post("/moderate/batch", json={"items": items})
        assert response.status_code == 200
        results = response.json()["results"]
        assert len(results) == 50
        assert [result["id"] for result in results] == [f"i{index}" for index in range(50)]
        assert response.json()["totalLatencyMs"] >= 0.0

    def test_batch_size_50_7_6779(self, client: Any) -> None:
        """Batches return one ordered result per item."""
        items = [
            {"id": f"i{index}", "text": f"message {index}", "app_name": "a"} for index in range(50)
        ]
        response = client.post("/moderate/batch", json={"items": items})
        assert response.status_code == 200
        results = response.json()["results"]
        assert len(results) == 50
        assert [result["id"] for result in results] == [f"i{index}" for index in range(50)]
        assert response.json()["totalLatencyMs"] >= 0.0

    def test_batch_size_50_8_6780(self, client: Any) -> None:
        """Batches return one ordered result per item."""
        items = [
            {"id": f"i{index}", "text": f"message {index}", "app_name": "a"} for index in range(50)
        ]
        response = client.post("/moderate/batch", json={"items": items})
        assert response.status_code == 200
        results = response.json()["results"]
        assert len(results) == 50
        assert [result["id"] for result in results] == [f"i{index}" for index in range(50)]
        assert response.json()["totalLatencyMs"] >= 0.0

    def test_batch_size_50_9_6781(self, client: Any) -> None:
        """Batches return one ordered result per item."""
        items = [
            {"id": f"i{index}", "text": f"message {index}", "app_name": "a"} for index in range(50)
        ]
        response = client.post("/moderate/batch", json={"items": items})
        assert response.status_code == 200
        results = response.json()["results"]
        assert len(results) == 50
        assert [result["id"] for result in results] == [f"i{index}" for index in range(50)]
        assert response.json()["totalLatencyMs"] >= 0.0

    def test_batch_size_50_10_6782(self, client: Any) -> None:
        """Batches return one ordered result per item."""
        items = [
            {"id": f"i{index}", "text": f"message {index}", "app_name": "a"} for index in range(50)
        ]
        response = client.post("/moderate/batch", json={"items": items})
        assert response.status_code == 200
        results = response.json()["results"]
        assert len(results) == 50
        assert [result["id"] for result in results] == [f"i{index}" for index in range(50)]
        assert response.json()["totalLatencyMs"] >= 0.0

    def test_batch_size_50_11_6783(self, client: Any) -> None:
        """Batches return one ordered result per item."""
        items = [
            {"id": f"i{index}", "text": f"message {index}", "app_name": "a"} for index in range(50)
        ]
        response = client.post("/moderate/batch", json={"items": items})
        assert response.status_code == 200
        results = response.json()["results"]
        assert len(results) == 50
        assert [result["id"] for result in results] == [f"i{index}" for index in range(50)]
        assert response.json()["totalLatencyMs"] >= 0.0

    def test_batch_size_50_12_6784(self, client: Any) -> None:
        """Batches return one ordered result per item."""
        items = [
            {"id": f"i{index}", "text": f"message {index}", "app_name": "a"} for index in range(50)
        ]
        response = client.post("/moderate/batch", json={"items": items})
        assert response.status_code == 200
        results = response.json()["results"]
        assert len(results) == 50
        assert [result["id"] for result in results] == [f"i{index}" for index in range(50)]
        assert response.json()["totalLatencyMs"] >= 0.0

    def test_batch_size_50_13_6785(self, client: Any) -> None:
        """Batches return one ordered result per item."""
        items = [
            {"id": f"i{index}", "text": f"message {index}", "app_name": "a"} for index in range(50)
        ]
        response = client.post("/moderate/batch", json={"items": items})
        assert response.status_code == 200
        results = response.json()["results"]
        assert len(results) == 50
        assert [result["id"] for result in results] == [f"i{index}" for index in range(50)]
        assert response.json()["totalLatencyMs"] >= 0.0

    def test_batch_size_50_14_6786(self, client: Any) -> None:
        """Batches return one ordered result per item."""
        items = [
            {"id": f"i{index}", "text": f"message {index}", "app_name": "a"} for index in range(50)
        ]
        response = client.post("/moderate/batch", json={"items": items})
        assert response.status_code == 200
        results = response.json()["results"]
        assert len(results) == 50
        assert [result["id"] for result in results] == [f"i{index}" for index in range(50)]
        assert response.json()["totalLatencyMs"] >= 0.0

    def test_batch_size_75_0_6787(self, client: Any) -> None:
        """Batches return one ordered result per item."""
        items = [
            {"id": f"i{index}", "text": f"message {index}", "app_name": "a"} for index in range(75)
        ]
        response = client.post("/moderate/batch", json={"items": items})
        assert response.status_code == 200
        results = response.json()["results"]
        assert len(results) == 75
        assert [result["id"] for result in results] == [f"i{index}" for index in range(75)]
        assert response.json()["totalLatencyMs"] >= 0.0

    def test_batch_size_75_1_6788(self, client: Any) -> None:
        """Batches return one ordered result per item."""
        items = [
            {"id": f"i{index}", "text": f"message {index}", "app_name": "a"} for index in range(75)
        ]
        response = client.post("/moderate/batch", json={"items": items})
        assert response.status_code == 200
        results = response.json()["results"]
        assert len(results) == 75
        assert [result["id"] for result in results] == [f"i{index}" for index in range(75)]
        assert response.json()["totalLatencyMs"] >= 0.0

    def test_batch_size_75_2_6789(self, client: Any) -> None:
        """Batches return one ordered result per item."""
        items = [
            {"id": f"i{index}", "text": f"message {index}", "app_name": "a"} for index in range(75)
        ]
        response = client.post("/moderate/batch", json={"items": items})
        assert response.status_code == 200
        results = response.json()["results"]
        assert len(results) == 75
        assert [result["id"] for result in results] == [f"i{index}" for index in range(75)]
        assert response.json()["totalLatencyMs"] >= 0.0

    def test_batch_size_75_3_6790(self, client: Any) -> None:
        """Batches return one ordered result per item."""
        items = [
            {"id": f"i{index}", "text": f"message {index}", "app_name": "a"} for index in range(75)
        ]
        response = client.post("/moderate/batch", json={"items": items})
        assert response.status_code == 200
        results = response.json()["results"]
        assert len(results) == 75
        assert [result["id"] for result in results] == [f"i{index}" for index in range(75)]
        assert response.json()["totalLatencyMs"] >= 0.0

    def test_batch_size_75_4_6791(self, client: Any) -> None:
        """Batches return one ordered result per item."""
        items = [
            {"id": f"i{index}", "text": f"message {index}", "app_name": "a"} for index in range(75)
        ]
        response = client.post("/moderate/batch", json={"items": items})
        assert response.status_code == 200
        results = response.json()["results"]
        assert len(results) == 75
        assert [result["id"] for result in results] == [f"i{index}" for index in range(75)]
        assert response.json()["totalLatencyMs"] >= 0.0

    def test_batch_size_75_5_6792(self, client: Any) -> None:
        """Batches return one ordered result per item."""
        items = [
            {"id": f"i{index}", "text": f"message {index}", "app_name": "a"} for index in range(75)
        ]
        response = client.post("/moderate/batch", json={"items": items})
        assert response.status_code == 200
        results = response.json()["results"]
        assert len(results) == 75
        assert [result["id"] for result in results] == [f"i{index}" for index in range(75)]
        assert response.json()["totalLatencyMs"] >= 0.0

    def test_batch_size_75_6_6793(self, client: Any) -> None:
        """Batches return one ordered result per item."""
        items = [
            {"id": f"i{index}", "text": f"message {index}", "app_name": "a"} for index in range(75)
        ]
        response = client.post("/moderate/batch", json={"items": items})
        assert response.status_code == 200
        results = response.json()["results"]
        assert len(results) == 75
        assert [result["id"] for result in results] == [f"i{index}" for index in range(75)]
        assert response.json()["totalLatencyMs"] >= 0.0

    def test_batch_size_75_7_6794(self, client: Any) -> None:
        """Batches return one ordered result per item."""
        items = [
            {"id": f"i{index}", "text": f"message {index}", "app_name": "a"} for index in range(75)
        ]
        response = client.post("/moderate/batch", json={"items": items})
        assert response.status_code == 200
        results = response.json()["results"]
        assert len(results) == 75
        assert [result["id"] for result in results] == [f"i{index}" for index in range(75)]
        assert response.json()["totalLatencyMs"] >= 0.0

    def test_batch_size_75_8_6795(self, client: Any) -> None:
        """Batches return one ordered result per item."""
        items = [
            {"id": f"i{index}", "text": f"message {index}", "app_name": "a"} for index in range(75)
        ]
        response = client.post("/moderate/batch", json={"items": items})
        assert response.status_code == 200
        results = response.json()["results"]
        assert len(results) == 75
        assert [result["id"] for result in results] == [f"i{index}" for index in range(75)]
        assert response.json()["totalLatencyMs"] >= 0.0

    def test_batch_size_75_9_6796(self, client: Any) -> None:
        """Batches return one ordered result per item."""
        items = [
            {"id": f"i{index}", "text": f"message {index}", "app_name": "a"} for index in range(75)
        ]
        response = client.post("/moderate/batch", json={"items": items})
        assert response.status_code == 200
        results = response.json()["results"]
        assert len(results) == 75
        assert [result["id"] for result in results] == [f"i{index}" for index in range(75)]
        assert response.json()["totalLatencyMs"] >= 0.0

    def test_batch_size_75_10_6797(self, client: Any) -> None:
        """Batches return one ordered result per item."""
        items = [
            {"id": f"i{index}", "text": f"message {index}", "app_name": "a"} for index in range(75)
        ]
        response = client.post("/moderate/batch", json={"items": items})
        assert response.status_code == 200
        results = response.json()["results"]
        assert len(results) == 75
        assert [result["id"] for result in results] == [f"i{index}" for index in range(75)]
        assert response.json()["totalLatencyMs"] >= 0.0

    def test_batch_size_75_11_6798(self, client: Any) -> None:
        """Batches return one ordered result per item."""
        items = [
            {"id": f"i{index}", "text": f"message {index}", "app_name": "a"} for index in range(75)
        ]
        response = client.post("/moderate/batch", json={"items": items})
        assert response.status_code == 200
        results = response.json()["results"]
        assert len(results) == 75
        assert [result["id"] for result in results] == [f"i{index}" for index in range(75)]
        assert response.json()["totalLatencyMs"] >= 0.0

    def test_batch_size_75_12_6799(self, client: Any) -> None:
        """Batches return one ordered result per item."""
        items = [
            {"id": f"i{index}", "text": f"message {index}", "app_name": "a"} for index in range(75)
        ]
        response = client.post("/moderate/batch", json={"items": items})
        assert response.status_code == 200
        results = response.json()["results"]
        assert len(results) == 75
        assert [result["id"] for result in results] == [f"i{index}" for index in range(75)]
        assert response.json()["totalLatencyMs"] >= 0.0

    def test_batch_size_75_13_6800(self, client: Any) -> None:
        """Batches return one ordered result per item."""
        items = [
            {"id": f"i{index}", "text": f"message {index}", "app_name": "a"} for index in range(75)
        ]
        response = client.post("/moderate/batch", json={"items": items})
        assert response.status_code == 200
        results = response.json()["results"]
        assert len(results) == 75
        assert [result["id"] for result in results] == [f"i{index}" for index in range(75)]
        assert response.json()["totalLatencyMs"] >= 0.0

    def test_batch_size_75_14_6801(self, client: Any) -> None:
        """Batches return one ordered result per item."""
        items = [
            {"id": f"i{index}", "text": f"message {index}", "app_name": "a"} for index in range(75)
        ]
        response = client.post("/moderate/batch", json={"items": items})
        assert response.status_code == 200
        results = response.json()["results"]
        assert len(results) == 75
        assert [result["id"] for result in results] == [f"i{index}" for index in range(75)]
        assert response.json()["totalLatencyMs"] >= 0.0

    def test_batch_size_100_0_6802(self, client: Any) -> None:
        """Batches return one ordered result per item."""
        items = [
            {"id": f"i{index}", "text": f"message {index}", "app_name": "a"} for index in range(100)
        ]
        response = client.post("/moderate/batch", json={"items": items})
        assert response.status_code == 200
        results = response.json()["results"]
        assert len(results) == 100
        assert [result["id"] for result in results] == [f"i{index}" for index in range(100)]
        assert response.json()["totalLatencyMs"] >= 0.0

    def test_batch_size_100_1_6803(self, client: Any) -> None:
        """Batches return one ordered result per item."""
        items = [
            {"id": f"i{index}", "text": f"message {index}", "app_name": "a"} for index in range(100)
        ]
        response = client.post("/moderate/batch", json={"items": items})
        assert response.status_code == 200
        results = response.json()["results"]
        assert len(results) == 100
        assert [result["id"] for result in results] == [f"i{index}" for index in range(100)]
        assert response.json()["totalLatencyMs"] >= 0.0

    def test_batch_size_100_2_6804(self, client: Any) -> None:
        """Batches return one ordered result per item."""
        items = [
            {"id": f"i{index}", "text": f"message {index}", "app_name": "a"} for index in range(100)
        ]
        response = client.post("/moderate/batch", json={"items": items})
        assert response.status_code == 200
        results = response.json()["results"]
        assert len(results) == 100
        assert [result["id"] for result in results] == [f"i{index}" for index in range(100)]
        assert response.json()["totalLatencyMs"] >= 0.0

    def test_batch_size_100_3_6805(self, client: Any) -> None:
        """Batches return one ordered result per item."""
        items = [
            {"id": f"i{index}", "text": f"message {index}", "app_name": "a"} for index in range(100)
        ]
        response = client.post("/moderate/batch", json={"items": items})
        assert response.status_code == 200
        results = response.json()["results"]
        assert len(results) == 100
        assert [result["id"] for result in results] == [f"i{index}" for index in range(100)]
        assert response.json()["totalLatencyMs"] >= 0.0

    def test_batch_size_100_4_6806(self, client: Any) -> None:
        """Batches return one ordered result per item."""
        items = [
            {"id": f"i{index}", "text": f"message {index}", "app_name": "a"} for index in range(100)
        ]
        response = client.post("/moderate/batch", json={"items": items})
        assert response.status_code == 200
        results = response.json()["results"]
        assert len(results) == 100
        assert [result["id"] for result in results] == [f"i{index}" for index in range(100)]
        assert response.json()["totalLatencyMs"] >= 0.0

    def test_batch_size_100_5_6807(self, client: Any) -> None:
        """Batches return one ordered result per item."""
        items = [
            {"id": f"i{index}", "text": f"message {index}", "app_name": "a"} for index in range(100)
        ]
        response = client.post("/moderate/batch", json={"items": items})
        assert response.status_code == 200
        results = response.json()["results"]
        assert len(results) == 100
        assert [result["id"] for result in results] == [f"i{index}" for index in range(100)]
        assert response.json()["totalLatencyMs"] >= 0.0

    def test_batch_size_100_6_6808(self, client: Any) -> None:
        """Batches return one ordered result per item."""
        items = [
            {"id": f"i{index}", "text": f"message {index}", "app_name": "a"} for index in range(100)
        ]
        response = client.post("/moderate/batch", json={"items": items})
        assert response.status_code == 200
        results = response.json()["results"]
        assert len(results) == 100
        assert [result["id"] for result in results] == [f"i{index}" for index in range(100)]
        assert response.json()["totalLatencyMs"] >= 0.0

    def test_batch_size_100_7_6809(self, client: Any) -> None:
        """Batches return one ordered result per item."""
        items = [
            {"id": f"i{index}", "text": f"message {index}", "app_name": "a"} for index in range(100)
        ]
        response = client.post("/moderate/batch", json={"items": items})
        assert response.status_code == 200
        results = response.json()["results"]
        assert len(results) == 100
        assert [result["id"] for result in results] == [f"i{index}" for index in range(100)]
        assert response.json()["totalLatencyMs"] >= 0.0

    def test_batch_size_100_8_6810(self, client: Any) -> None:
        """Batches return one ordered result per item."""
        items = [
            {"id": f"i{index}", "text": f"message {index}", "app_name": "a"} for index in range(100)
        ]
        response = client.post("/moderate/batch", json={"items": items})
        assert response.status_code == 200
        results = response.json()["results"]
        assert len(results) == 100
        assert [result["id"] for result in results] == [f"i{index}" for index in range(100)]
        assert response.json()["totalLatencyMs"] >= 0.0

    def test_batch_size_100_9_6811(self, client: Any) -> None:
        """Batches return one ordered result per item."""
        items = [
            {"id": f"i{index}", "text": f"message {index}", "app_name": "a"} for index in range(100)
        ]
        response = client.post("/moderate/batch", json={"items": items})
        assert response.status_code == 200
        results = response.json()["results"]
        assert len(results) == 100
        assert [result["id"] for result in results] == [f"i{index}" for index in range(100)]
        assert response.json()["totalLatencyMs"] >= 0.0
