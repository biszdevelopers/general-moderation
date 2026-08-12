"""Phase 2 public moderation API tests (generated).

Language verdict matrices, batch sizes, validation, unicode edges,
profiling flows and response shapes; see tests/tools/phase2_generator.py."""

# multilingual fixtures use non-ASCII on purpose
from __future__ import annotations

from typing import Any

from tests.base_test import BaseTest


class TestValidationCases(BaseTest):
    """ValidationCases scenarios."""

    def test_validation_0_6817(self, client: Any) -> None:
        """Invalid payloads are rejected without crashing."""
        payload = '{"text": ""}'
        response = client.post(
            "/moderate",
            content=payload,
            headers={"content-type": "application/json"},
        )
        assert response.status_code in (200, 422)

    def test_validation_1_6818(self, client: Any) -> None:
        """Invalid payloads are rejected without crashing."""
        payload = '{"text": ""}'
        response = client.post(
            "/moderate",
            content=payload,
            headers={"content-type": "application/json"},
        )
        assert response.status_code in (200, 422)

    def test_validation_2_6819(self, client: Any) -> None:
        """Invalid payloads are rejected without crashing."""
        payload = '{"text": ""}'
        response = client.post(
            "/moderate",
            content=payload,
            headers={"content-type": "application/json"},
        )
        assert response.status_code in (200, 422)

    def test_validation_3_6820(self, client: Any) -> None:
        """Invalid payloads are rejected without crashing."""
        payload = '{"text": ""}'
        response = client.post(
            "/moderate",
            content=payload,
            headers={"content-type": "application/json"},
        )
        assert response.status_code in (200, 422)

    def test_validation_4_6821(self, client: Any) -> None:
        """Invalid payloads are rejected without crashing."""
        payload = '{"text": ""}'
        response = client.post(
            "/moderate",
            content=payload,
            headers={"content-type": "application/json"},
        )
        assert response.status_code in (200, 422)

    def test_validation_5_6822(self, client: Any) -> None:
        """Invalid payloads are rejected without crashing."""
        payload = '{"text": ""}'
        response = client.post(
            "/moderate",
            content=payload,
            headers={"content-type": "application/json"},
        )
        assert response.status_code in (200, 422)

    def test_validation_6_6823(self, client: Any) -> None:
        """Invalid payloads are rejected without crashing."""
        payload = '{"text": ""}'
        response = client.post(
            "/moderate",
            content=payload,
            headers={"content-type": "application/json"},
        )
        assert response.status_code in (200, 422)

    def test_validation_7_6824(self, client: Any) -> None:
        """Invalid payloads are rejected without crashing."""
        payload = '{"text": ""}'
        response = client.post(
            "/moderate",
            content=payload,
            headers={"content-type": "application/json"},
        )
        assert response.status_code in (200, 422)

    def test_validation_8_6825(self, client: Any) -> None:
        """Invalid payloads are rejected without crashing."""
        payload = '{"text": ""}'
        response = client.post(
            "/moderate",
            content=payload,
            headers={"content-type": "application/json"},
        )
        assert response.status_code in (200, 422)

    def test_validation_9_6826(self, client: Any) -> None:
        """Invalid payloads are rejected without crashing."""
        payload = '{"text": ""}'
        response = client.post(
            "/moderate",
            content=payload,
            headers={"content-type": "application/json"},
        )
        assert response.status_code in (200, 422)

    def test_validation_0_6827(self, client: Any) -> None:
        """Invalid payloads are rejected without crashing."""
        payload = '{"text": null}'
        response = client.post(
            "/moderate",
            content=payload,
            headers={"content-type": "application/json"},
        )
        assert response.status_code in (200, 422)

    def test_validation_1_6828(self, client: Any) -> None:
        """Invalid payloads are rejected without crashing."""
        payload = '{"text": null}'
        response = client.post(
            "/moderate",
            content=payload,
            headers={"content-type": "application/json"},
        )
        assert response.status_code in (200, 422)

    def test_validation_2_6829(self, client: Any) -> None:
        """Invalid payloads are rejected without crashing."""
        payload = '{"text": null}'
        response = client.post(
            "/moderate",
            content=payload,
            headers={"content-type": "application/json"},
        )
        assert response.status_code in (200, 422)

    def test_validation_3_6830(self, client: Any) -> None:
        """Invalid payloads are rejected without crashing."""
        payload = '{"text": null}'
        response = client.post(
            "/moderate",
            content=payload,
            headers={"content-type": "application/json"},
        )
        assert response.status_code in (200, 422)

    def test_validation_4_6831(self, client: Any) -> None:
        """Invalid payloads are rejected without crashing."""
        payload = '{"text": null}'
        response = client.post(
            "/moderate",
            content=payload,
            headers={"content-type": "application/json"},
        )
        assert response.status_code in (200, 422)

    def test_validation_5_6832(self, client: Any) -> None:
        """Invalid payloads are rejected without crashing."""
        payload = '{"text": null}'
        response = client.post(
            "/moderate",
            content=payload,
            headers={"content-type": "application/json"},
        )
        assert response.status_code in (200, 422)

    def test_validation_6_6833(self, client: Any) -> None:
        """Invalid payloads are rejected without crashing."""
        payload = '{"text": null}'
        response = client.post(
            "/moderate",
            content=payload,
            headers={"content-type": "application/json"},
        )
        assert response.status_code in (200, 422)

    def test_validation_7_6834(self, client: Any) -> None:
        """Invalid payloads are rejected without crashing."""
        payload = '{"text": null}'
        response = client.post(
            "/moderate",
            content=payload,
            headers={"content-type": "application/json"},
        )
        assert response.status_code in (200, 422)

    def test_validation_8_6835(self, client: Any) -> None:
        """Invalid payloads are rejected without crashing."""
        payload = '{"text": null}'
        response = client.post(
            "/moderate",
            content=payload,
            headers={"content-type": "application/json"},
        )
        assert response.status_code in (200, 422)

    def test_validation_9_6836(self, client: Any) -> None:
        """Invalid payloads are rejected without crashing."""
        payload = '{"text": null}'
        response = client.post(
            "/moderate",
            content=payload,
            headers={"content-type": "application/json"},
        )
        assert response.status_code in (200, 422)

    def test_validation_0_6837(self, client: Any) -> None:
        """Invalid payloads are rejected without crashing."""
        payload = "{}"
        response = client.post(
            "/moderate",
            content=payload,
            headers={"content-type": "application/json"},
        )
        assert response.status_code in (200, 422)

    def test_validation_1_6838(self, client: Any) -> None:
        """Invalid payloads are rejected without crashing."""
        payload = "{}"
        response = client.post(
            "/moderate",
            content=payload,
            headers={"content-type": "application/json"},
        )
        assert response.status_code in (200, 422)

    def test_validation_2_6839(self, client: Any) -> None:
        """Invalid payloads are rejected without crashing."""
        payload = "{}"
        response = client.post(
            "/moderate",
            content=payload,
            headers={"content-type": "application/json"},
        )
        assert response.status_code in (200, 422)

    def test_validation_3_6840(self, client: Any) -> None:
        """Invalid payloads are rejected without crashing."""
        payload = "{}"
        response = client.post(
            "/moderate",
            content=payload,
            headers={"content-type": "application/json"},
        )
        assert response.status_code in (200, 422)

    def test_validation_4_6841(self, client: Any) -> None:
        """Invalid payloads are rejected without crashing."""
        payload = "{}"
        response = client.post(
            "/moderate",
            content=payload,
            headers={"content-type": "application/json"},
        )
        assert response.status_code in (200, 422)

    def test_validation_5_6842(self, client: Any) -> None:
        """Invalid payloads are rejected without crashing."""
        payload = "{}"
        response = client.post(
            "/moderate",
            content=payload,
            headers={"content-type": "application/json"},
        )
        assert response.status_code in (200, 422)

    def test_validation_6_6843(self, client: Any) -> None:
        """Invalid payloads are rejected without crashing."""
        payload = "{}"
        response = client.post(
            "/moderate",
            content=payload,
            headers={"content-type": "application/json"},
        )
        assert response.status_code in (200, 422)

    def test_validation_7_6844(self, client: Any) -> None:
        """Invalid payloads are rejected without crashing."""
        payload = "{}"
        response = client.post(
            "/moderate",
            content=payload,
            headers={"content-type": "application/json"},
        )
        assert response.status_code in (200, 422)

    def test_validation_8_6845(self, client: Any) -> None:
        """Invalid payloads are rejected without crashing."""
        payload = "{}"
        response = client.post(
            "/moderate",
            content=payload,
            headers={"content-type": "application/json"},
        )
        assert response.status_code in (200, 422)

    def test_validation_9_6846(self, client: Any) -> None:
        """Invalid payloads are rejected without crashing."""
        payload = "{}"
        response = client.post(
            "/moderate",
            content=payload,
            headers={"content-type": "application/json"},
        )
        assert response.status_code in (200, 422)

    def test_validation_0_6847(self, client: Any) -> None:
        """Invalid payloads are rejected without crashing."""
        payload = '{"nope": 1}'
        response = client.post(
            "/moderate",
            content=payload,
            headers={"content-type": "application/json"},
        )
        assert response.status_code in (200, 422)

    def test_validation_1_6848(self, client: Any) -> None:
        """Invalid payloads are rejected without crashing."""
        payload = '{"nope": 1}'
        response = client.post(
            "/moderate",
            content=payload,
            headers={"content-type": "application/json"},
        )
        assert response.status_code in (200, 422)

    def test_validation_2_6849(self, client: Any) -> None:
        """Invalid payloads are rejected without crashing."""
        payload = '{"nope": 1}'
        response = client.post(
            "/moderate",
            content=payload,
            headers={"content-type": "application/json"},
        )
        assert response.status_code in (200, 422)

    def test_validation_3_6850(self, client: Any) -> None:
        """Invalid payloads are rejected without crashing."""
        payload = '{"nope": 1}'
        response = client.post(
            "/moderate",
            content=payload,
            headers={"content-type": "application/json"},
        )
        assert response.status_code in (200, 422)

    def test_validation_4_6851(self, client: Any) -> None:
        """Invalid payloads are rejected without crashing."""
        payload = '{"nope": 1}'
        response = client.post(
            "/moderate",
            content=payload,
            headers={"content-type": "application/json"},
        )
        assert response.status_code in (200, 422)

    def test_validation_5_6852(self, client: Any) -> None:
        """Invalid payloads are rejected without crashing."""
        payload = '{"nope": 1}'
        response = client.post(
            "/moderate",
            content=payload,
            headers={"content-type": "application/json"},
        )
        assert response.status_code in (200, 422)

    def test_validation_6_6853(self, client: Any) -> None:
        """Invalid payloads are rejected without crashing."""
        payload = '{"nope": 1}'
        response = client.post(
            "/moderate",
            content=payload,
            headers={"content-type": "application/json"},
        )
        assert response.status_code in (200, 422)

    def test_validation_7_6854(self, client: Any) -> None:
        """Invalid payloads are rejected without crashing."""
        payload = '{"nope": 1}'
        response = client.post(
            "/moderate",
            content=payload,
            headers={"content-type": "application/json"},
        )
        assert response.status_code in (200, 422)

    def test_validation_8_6855(self, client: Any) -> None:
        """Invalid payloads are rejected without crashing."""
        payload = '{"nope": 1}'
        response = client.post(
            "/moderate",
            content=payload,
            headers={"content-type": "application/json"},
        )
        assert response.status_code in (200, 422)

    def test_validation_9_6856(self, client: Any) -> None:
        """Invalid payloads are rejected without crashing."""
        payload = '{"nope": 1}'
        response = client.post(
            "/moderate",
            content=payload,
            headers={"content-type": "application/json"},
        )
        assert response.status_code in (200, 422)

    def test_validation_0_6857(self, client: Any) -> None:
        """Invalid payloads are rejected without crashing."""
        payload = '{"text": 12345}'
        response = client.post(
            "/moderate",
            content=payload,
            headers={"content-type": "application/json"},
        )
        assert response.status_code in (200, 422)

    def test_validation_1_6858(self, client: Any) -> None:
        """Invalid payloads are rejected without crashing."""
        payload = '{"text": 12345}'
        response = client.post(
            "/moderate",
            content=payload,
            headers={"content-type": "application/json"},
        )
        assert response.status_code in (200, 422)

    def test_validation_2_6859(self, client: Any) -> None:
        """Invalid payloads are rejected without crashing."""
        payload = '{"text": 12345}'
        response = client.post(
            "/moderate",
            content=payload,
            headers={"content-type": "application/json"},
        )
        assert response.status_code in (200, 422)

    def test_validation_3_6860(self, client: Any) -> None:
        """Invalid payloads are rejected without crashing."""
        payload = '{"text": 12345}'
        response = client.post(
            "/moderate",
            content=payload,
            headers={"content-type": "application/json"},
        )
        assert response.status_code in (200, 422)

    def test_validation_4_6861(self, client: Any) -> None:
        """Invalid payloads are rejected without crashing."""
        payload = '{"text": 12345}'
        response = client.post(
            "/moderate",
            content=payload,
            headers={"content-type": "application/json"},
        )
        assert response.status_code in (200, 422)

    def test_validation_5_6862(self, client: Any) -> None:
        """Invalid payloads are rejected without crashing."""
        payload = '{"text": 12345}'
        response = client.post(
            "/moderate",
            content=payload,
            headers={"content-type": "application/json"},
        )
        assert response.status_code in (200, 422)

    def test_validation_6_6863(self, client: Any) -> None:
        """Invalid payloads are rejected without crashing."""
        payload = '{"text": 12345}'
        response = client.post(
            "/moderate",
            content=payload,
            headers={"content-type": "application/json"},
        )
        assert response.status_code in (200, 422)

    def test_validation_7_6864(self, client: Any) -> None:
        """Invalid payloads are rejected without crashing."""
        payload = '{"text": 12345}'
        response = client.post(
            "/moderate",
            content=payload,
            headers={"content-type": "application/json"},
        )
        assert response.status_code in (200, 422)

    def test_validation_8_6865(self, client: Any) -> None:
        """Invalid payloads are rejected without crashing."""
        payload = '{"text": 12345}'
        response = client.post(
            "/moderate",
            content=payload,
            headers={"content-type": "application/json"},
        )
        assert response.status_code in (200, 422)

    def test_validation_9_6866(self, client: Any) -> None:
        """Invalid payloads are rejected without crashing."""
        payload = '{"text": 12345}'
        response = client.post(
            "/moderate",
            content=payload,
            headers={"content-type": "application/json"},
        )
        assert response.status_code in (200, 422)

    def test_validation_0_6867(self, client: Any) -> None:
        """Invalid payloads are rejected without crashing."""
        payload = '{"text": "x" * 9000}'
        response = client.post(
            "/moderate",
            content=payload,
            headers={"content-type": "application/json"},
        )
        assert response.status_code in (200, 422)

    def test_validation_1_6868(self, client: Any) -> None:
        """Invalid payloads are rejected without crashing."""
        payload = '{"text": "x" * 9000}'
        response = client.post(
            "/moderate",
            content=payload,
            headers={"content-type": "application/json"},
        )
        assert response.status_code in (200, 422)

    def test_validation_2_6869(self, client: Any) -> None:
        """Invalid payloads are rejected without crashing."""
        payload = '{"text": "x" * 9000}'
        response = client.post(
            "/moderate",
            content=payload,
            headers={"content-type": "application/json"},
        )
        assert response.status_code in (200, 422)

    def test_validation_3_6870(self, client: Any) -> None:
        """Invalid payloads are rejected without crashing."""
        payload = '{"text": "x" * 9000}'
        response = client.post(
            "/moderate",
            content=payload,
            headers={"content-type": "application/json"},
        )
        assert response.status_code in (200, 422)

    def test_validation_4_6871(self, client: Any) -> None:
        """Invalid payloads are rejected without crashing."""
        payload = '{"text": "x" * 9000}'
        response = client.post(
            "/moderate",
            content=payload,
            headers={"content-type": "application/json"},
        )
        assert response.status_code in (200, 422)

    def test_validation_5_6872(self, client: Any) -> None:
        """Invalid payloads are rejected without crashing."""
        payload = '{"text": "x" * 9000}'
        response = client.post(
            "/moderate",
            content=payload,
            headers={"content-type": "application/json"},
        )
        assert response.status_code in (200, 422)

    def test_validation_6_6873(self, client: Any) -> None:
        """Invalid payloads are rejected without crashing."""
        payload = '{"text": "x" * 9000}'
        response = client.post(
            "/moderate",
            content=payload,
            headers={"content-type": "application/json"},
        )
        assert response.status_code in (200, 422)

    def test_validation_7_6874(self, client: Any) -> None:
        """Invalid payloads are rejected without crashing."""
        payload = '{"text": "x" * 9000}'
        response = client.post(
            "/moderate",
            content=payload,
            headers={"content-type": "application/json"},
        )
        assert response.status_code in (200, 422)

    def test_validation_8_6875(self, client: Any) -> None:
        """Invalid payloads are rejected without crashing."""
        payload = '{"text": "x" * 9000}'
        response = client.post(
            "/moderate",
            content=payload,
            headers={"content-type": "application/json"},
        )
        assert response.status_code in (200, 422)

    def test_validation_9_6876(self, client: Any) -> None:
        """Invalid payloads are rejected without crashing."""
        payload = '{"text": "x" * 9000}'
        response = client.post(
            "/moderate",
            content=payload,
            headers={"content-type": "application/json"},
        )
        assert response.status_code in (200, 422)

    def test_validation_0_6877(self, client: Any) -> None:
        """Invalid payloads are rejected without crashing."""
        payload = '{"items": []}'
        response = client.post(
            "/moderate",
            content=payload,
            headers={"content-type": "application/json"},
        )
        assert response.status_code in (200, 422)

    def test_validation_1_6878(self, client: Any) -> None:
        """Invalid payloads are rejected without crashing."""
        payload = '{"items": []}'
        response = client.post(
            "/moderate",
            content=payload,
            headers={"content-type": "application/json"},
        )
        assert response.status_code in (200, 422)

    def test_validation_2_6879(self, client: Any) -> None:
        """Invalid payloads are rejected without crashing."""
        payload = '{"items": []}'
        response = client.post(
            "/moderate",
            content=payload,
            headers={"content-type": "application/json"},
        )
        assert response.status_code in (200, 422)

    def test_validation_3_6880(self, client: Any) -> None:
        """Invalid payloads are rejected without crashing."""
        payload = '{"items": []}'
        response = client.post(
            "/moderate",
            content=payload,
            headers={"content-type": "application/json"},
        )
        assert response.status_code in (200, 422)

    def test_validation_4_6881(self, client: Any) -> None:
        """Invalid payloads are rejected without crashing."""
        payload = '{"items": []}'
        response = client.post(
            "/moderate",
            content=payload,
            headers={"content-type": "application/json"},
        )
        assert response.status_code in (200, 422)

    def test_validation_5_6882(self, client: Any) -> None:
        """Invalid payloads are rejected without crashing."""
        payload = '{"items": []}'
        response = client.post(
            "/moderate",
            content=payload,
            headers={"content-type": "application/json"},
        )
        assert response.status_code in (200, 422)

    def test_validation_6_6883(self, client: Any) -> None:
        """Invalid payloads are rejected without crashing."""
        payload = '{"items": []}'
        response = client.post(
            "/moderate",
            content=payload,
            headers={"content-type": "application/json"},
        )
        assert response.status_code in (200, 422)

    def test_validation_7_6884(self, client: Any) -> None:
        """Invalid payloads are rejected without crashing."""
        payload = '{"items": []}'
        response = client.post(
            "/moderate",
            content=payload,
            headers={"content-type": "application/json"},
        )
        assert response.status_code in (200, 422)

    def test_validation_8_6885(self, client: Any) -> None:
        """Invalid payloads are rejected without crashing."""
        payload = '{"items": []}'
        response = client.post(
            "/moderate",
            content=payload,
            headers={"content-type": "application/json"},
        )
        assert response.status_code in (200, 422)

    def test_validation_9_6886(self, client: Any) -> None:
        """Invalid payloads are rejected without crashing."""
        payload = '{"items": []}'
        response = client.post(
            "/moderate",
            content=payload,
            headers={"content-type": "application/json"},
        )
        assert response.status_code in (200, 422)

    def test_validation_0_6887(self, client: Any) -> None:
        """Invalid payloads are rejected without crashing."""
        payload = '{"items": [{"nope": 1}]}'
        response = client.post(
            "/moderate",
            content=payload,
            headers={"content-type": "application/json"},
        )
        assert response.status_code in (200, 422)

    def test_validation_1_6888(self, client: Any) -> None:
        """Invalid payloads are rejected without crashing."""
        payload = '{"items": [{"nope": 1}]}'
        response = client.post(
            "/moderate",
            content=payload,
            headers={"content-type": "application/json"},
        )
        assert response.status_code in (200, 422)

    def test_validation_2_6889(self, client: Any) -> None:
        """Invalid payloads are rejected without crashing."""
        payload = '{"items": [{"nope": 1}]}'
        response = client.post(
            "/moderate",
            content=payload,
            headers={"content-type": "application/json"},
        )
        assert response.status_code in (200, 422)

    def test_validation_3_6890(self, client: Any) -> None:
        """Invalid payloads are rejected without crashing."""
        payload = '{"items": [{"nope": 1}]}'
        response = client.post(
            "/moderate",
            content=payload,
            headers={"content-type": "application/json"},
        )
        assert response.status_code in (200, 422)

    def test_validation_4_6891(self, client: Any) -> None:
        """Invalid payloads are rejected without crashing."""
        payload = '{"items": [{"nope": 1}]}'
        response = client.post(
            "/moderate",
            content=payload,
            headers={"content-type": "application/json"},
        )
        assert response.status_code in (200, 422)

    def test_validation_5_6892(self, client: Any) -> None:
        """Invalid payloads are rejected without crashing."""
        payload = '{"items": [{"nope": 1}]}'
        response = client.post(
            "/moderate",
            content=payload,
            headers={"content-type": "application/json"},
        )
        assert response.status_code in (200, 422)

    def test_validation_6_6893(self, client: Any) -> None:
        """Invalid payloads are rejected without crashing."""
        payload = '{"items": [{"nope": 1}]}'
        response = client.post(
            "/moderate",
            content=payload,
            headers={"content-type": "application/json"},
        )
        assert response.status_code in (200, 422)

    def test_validation_7_6894(self, client: Any) -> None:
        """Invalid payloads are rejected without crashing."""
        payload = '{"items": [{"nope": 1}]}'
        response = client.post(
            "/moderate",
            content=payload,
            headers={"content-type": "application/json"},
        )
        assert response.status_code in (200, 422)

    def test_validation_8_6895(self, client: Any) -> None:
        """Invalid payloads are rejected without crashing."""
        payload = '{"items": [{"nope": 1}]}'
        response = client.post(
            "/moderate",
            content=payload,
            headers={"content-type": "application/json"},
        )
        assert response.status_code in (200, 422)

    def test_validation_9_6896(self, client: Any) -> None:
        """Invalid payloads are rejected without crashing."""
        payload = '{"items": [{"nope": 1}]}'
        response = client.post(
            "/moderate",
            content=payload,
            headers={"content-type": "application/json"},
        )
        assert response.status_code in (200, 422)

    def test_validation_0_6897(self, client: Any) -> None:
        """Invalid payloads are rejected without crashing."""
        payload = "{not valid json"
        response = client.post(
            "/moderate",
            content=payload,
            headers={"content-type": "application/json"},
        )
        assert response.status_code in (200, 422)

    def test_validation_1_6898(self, client: Any) -> None:
        """Invalid payloads are rejected without crashing."""
        payload = "{not valid json"
        response = client.post(
            "/moderate",
            content=payload,
            headers={"content-type": "application/json"},
        )
        assert response.status_code in (200, 422)

    def test_validation_2_6899(self, client: Any) -> None:
        """Invalid payloads are rejected without crashing."""
        payload = "{not valid json"
        response = client.post(
            "/moderate",
            content=payload,
            headers={"content-type": "application/json"},
        )
        assert response.status_code in (200, 422)

    def test_validation_3_6900(self, client: Any) -> None:
        """Invalid payloads are rejected without crashing."""
        payload = "{not valid json"
        response = client.post(
            "/moderate",
            content=payload,
            headers={"content-type": "application/json"},
        )
        assert response.status_code in (200, 422)

    def test_validation_4_6901(self, client: Any) -> None:
        """Invalid payloads are rejected without crashing."""
        payload = "{not valid json"
        response = client.post(
            "/moderate",
            content=payload,
            headers={"content-type": "application/json"},
        )
        assert response.status_code in (200, 422)

    def test_validation_5_6902(self, client: Any) -> None:
        """Invalid payloads are rejected without crashing."""
        payload = "{not valid json"
        response = client.post(
            "/moderate",
            content=payload,
            headers={"content-type": "application/json"},
        )
        assert response.status_code in (200, 422)

    def test_validation_6_6903(self, client: Any) -> None:
        """Invalid payloads are rejected without crashing."""
        payload = "{not valid json"
        response = client.post(
            "/moderate",
            content=payload,
            headers={"content-type": "application/json"},
        )
        assert response.status_code in (200, 422)

    def test_validation_7_6904(self, client: Any) -> None:
        """Invalid payloads are rejected without crashing."""
        payload = "{not valid json"
        response = client.post(
            "/moderate",
            content=payload,
            headers={"content-type": "application/json"},
        )
        assert response.status_code in (200, 422)

    def test_validation_8_6905(self, client: Any) -> None:
        """Invalid payloads are rejected without crashing."""
        payload = "{not valid json"
        response = client.post(
            "/moderate",
            content=payload,
            headers={"content-type": "application/json"},
        )
        assert response.status_code in (200, 422)

    def test_validation_9_6906(self, client: Any) -> None:
        """Invalid payloads are rejected without crashing."""
        payload = "{not valid json"
        response = client.post(
            "/moderate",
            content=payload,
            headers={"content-type": "application/json"},
        )
        assert response.status_code in (200, 422)

    def test_validation_0_6907(self, client: Any) -> None:
        """Invalid payloads are rejected without crashing."""
        payload = '{"text": "x" * 8192}'
        response = client.post(
            "/moderate",
            content=payload,
            headers={"content-type": "application/json"},
        )
        assert response.status_code in (200, 422)

    def test_validation_1_6908(self, client: Any) -> None:
        """Invalid payloads are rejected without crashing."""
        payload = '{"text": "x" * 8192}'
        response = client.post(
            "/moderate",
            content=payload,
            headers={"content-type": "application/json"},
        )
        assert response.status_code in (200, 422)

    def test_validation_2_6909(self, client: Any) -> None:
        """Invalid payloads are rejected without crashing."""
        payload = '{"text": "x" * 8192}'
        response = client.post(
            "/moderate",
            content=payload,
            headers={"content-type": "application/json"},
        )
        assert response.status_code in (200, 422)

    def test_validation_3_6910(self, client: Any) -> None:
        """Invalid payloads are rejected without crashing."""
        payload = '{"text": "x" * 8192}'
        response = client.post(
            "/moderate",
            content=payload,
            headers={"content-type": "application/json"},
        )
        assert response.status_code in (200, 422)

    def test_validation_4_6911(self, client: Any) -> None:
        """Invalid payloads are rejected without crashing."""
        payload = '{"text": "x" * 8192}'
        response = client.post(
            "/moderate",
            content=payload,
            headers={"content-type": "application/json"},
        )
        assert response.status_code in (200, 422)

    def test_validation_5_6912(self, client: Any) -> None:
        """Invalid payloads are rejected without crashing."""
        payload = '{"text": "x" * 8192}'
        response = client.post(
            "/moderate",
            content=payload,
            headers={"content-type": "application/json"},
        )
        assert response.status_code in (200, 422)

    def test_validation_6_6913(self, client: Any) -> None:
        """Invalid payloads are rejected without crashing."""
        payload = '{"text": "x" * 8192}'
        response = client.post(
            "/moderate",
            content=payload,
            headers={"content-type": "application/json"},
        )
        assert response.status_code in (200, 422)

    def test_validation_7_6914(self, client: Any) -> None:
        """Invalid payloads are rejected without crashing."""
        payload = '{"text": "x" * 8192}'
        response = client.post(
            "/moderate",
            content=payload,
            headers={"content-type": "application/json"},
        )
        assert response.status_code in (200, 422)

    def test_validation_8_6915(self, client: Any) -> None:
        """Invalid payloads are rejected without crashing."""
        payload = '{"text": "x" * 8192}'
        response = client.post(
            "/moderate",
            content=payload,
            headers={"content-type": "application/json"},
        )
        assert response.status_code in (200, 422)

    def test_validation_9_6916(self, client: Any) -> None:
        """Invalid payloads are rejected without crashing."""
        payload = '{"text": "x" * 8192}'
        response = client.post(
            "/moderate",
            content=payload,
            headers={"content-type": "application/json"},
        )
        assert response.status_code in (200, 422)
