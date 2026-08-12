"""Phase 2 security tests (generated).

Header parity, CORS, auth bypass, injection, traversal, method
restrictions and encoded payloads; see tests/tools/phase2_generator.py."""

# multilingual fixtures use non-ASCII on purpose
from __future__ import annotations

from typing import Any

from tests.base_test import BaseTest


class TestEncodedPayloads(BaseTest):
    """EncodedPayloads scenarios."""

    def test_encoded_0_9242(self, client: Any) -> None:
        """Encoded payloads never crash the moderator."""
        payloads = [
            "%3Cscript%3E",
            "\\u003cscript\\u003e",
            "\\x3cscript\\x3e",
            "&#60;script&#62;",
            "\\u202eoverride",
        ]
        for payload in payloads:
            response = client.post("/moderate", json={"text": payload, "app_name": "a"})
            assert response.status_code == 200

    def test_encoded_1_9243(self, client: Any) -> None:
        """Encoded payloads never crash the moderator."""
        payloads = [
            "%3Cscript%3E",
            "\\u003cscript\\u003e",
            "\\x3cscript\\x3e",
            "&#60;script&#62;",
            "\\u202eoverride",
        ]
        for payload in payloads:
            response = client.post("/moderate", json={"text": payload, "app_name": "a"})
            assert response.status_code == 200

    def test_encoded_2_9244(self, client: Any) -> None:
        """Encoded payloads never crash the moderator."""
        payloads = [
            "%3Cscript%3E",
            "\\u003cscript\\u003e",
            "\\x3cscript\\x3e",
            "&#60;script&#62;",
            "\\u202eoverride",
        ]
        for payload in payloads:
            response = client.post("/moderate", json={"text": payload, "app_name": "a"})
            assert response.status_code == 200

    def test_encoded_3_9245(self, client: Any) -> None:
        """Encoded payloads never crash the moderator."""
        payloads = [
            "%3Cscript%3E",
            "\\u003cscript\\u003e",
            "\\x3cscript\\x3e",
            "&#60;script&#62;",
            "\\u202eoverride",
        ]
        for payload in payloads:
            response = client.post("/moderate", json={"text": payload, "app_name": "a"})
            assert response.status_code == 200

    def test_encoded_4_9246(self, client: Any) -> None:
        """Encoded payloads never crash the moderator."""
        payloads = [
            "%3Cscript%3E",
            "\\u003cscript\\u003e",
            "\\x3cscript\\x3e",
            "&#60;script&#62;",
            "\\u202eoverride",
        ]
        for payload in payloads:
            response = client.post("/moderate", json={"text": payload, "app_name": "a"})
            assert response.status_code == 200

    def test_encoded_5_9247(self, client: Any) -> None:
        """Encoded payloads never crash the moderator."""
        payloads = [
            "%3Cscript%3E",
            "\\u003cscript\\u003e",
            "\\x3cscript\\x3e",
            "&#60;script&#62;",
            "\\u202eoverride",
        ]
        for payload in payloads:
            response = client.post("/moderate", json={"text": payload, "app_name": "a"})
            assert response.status_code == 200

    def test_encoded_6_9248(self, client: Any) -> None:
        """Encoded payloads never crash the moderator."""
        payloads = [
            "%3Cscript%3E",
            "\\u003cscript\\u003e",
            "\\x3cscript\\x3e",
            "&#60;script&#62;",
            "\\u202eoverride",
        ]
        for payload in payloads:
            response = client.post("/moderate", json={"text": payload, "app_name": "a"})
            assert response.status_code == 200

    def test_encoded_7_9249(self, client: Any) -> None:
        """Encoded payloads never crash the moderator."""
        payloads = [
            "%3Cscript%3E",
            "\\u003cscript\\u003e",
            "\\x3cscript\\x3e",
            "&#60;script&#62;",
            "\\u202eoverride",
        ]
        for payload in payloads:
            response = client.post("/moderate", json={"text": payload, "app_name": "a"})
            assert response.status_code == 200

    def test_encoded_8_9250(self, client: Any) -> None:
        """Encoded payloads never crash the moderator."""
        payloads = [
            "%3Cscript%3E",
            "\\u003cscript\\u003e",
            "\\x3cscript\\x3e",
            "&#60;script&#62;",
            "\\u202eoverride",
        ]
        for payload in payloads:
            response = client.post("/moderate", json={"text": payload, "app_name": "a"})
            assert response.status_code == 200

    def test_encoded_9_9251(self, client: Any) -> None:
        """Encoded payloads never crash the moderator."""
        payloads = [
            "%3Cscript%3E",
            "\\u003cscript\\u003e",
            "\\x3cscript\\x3e",
            "&#60;script&#62;",
            "\\u202eoverride",
        ]
        for payload in payloads:
            response = client.post("/moderate", json={"text": payload, "app_name": "a"})
            assert response.status_code == 200

    def test_encoded_10_9252(self, client: Any) -> None:
        """Encoded payloads never crash the moderator."""
        payloads = [
            "%3Cscript%3E",
            "\\u003cscript\\u003e",
            "\\x3cscript\\x3e",
            "&#60;script&#62;",
            "\\u202eoverride",
        ]
        for payload in payloads:
            response = client.post("/moderate", json={"text": payload, "app_name": "a"})
            assert response.status_code == 200

    def test_encoded_11_9253(self, client: Any) -> None:
        """Encoded payloads never crash the moderator."""
        payloads = [
            "%3Cscript%3E",
            "\\u003cscript\\u003e",
            "\\x3cscript\\x3e",
            "&#60;script&#62;",
            "\\u202eoverride",
        ]
        for payload in payloads:
            response = client.post("/moderate", json={"text": payload, "app_name": "a"})
            assert response.status_code == 200

    def test_encoded_12_9254(self, client: Any) -> None:
        """Encoded payloads never crash the moderator."""
        payloads = [
            "%3Cscript%3E",
            "\\u003cscript\\u003e",
            "\\x3cscript\\x3e",
            "&#60;script&#62;",
            "\\u202eoverride",
        ]
        for payload in payloads:
            response = client.post("/moderate", json={"text": payload, "app_name": "a"})
            assert response.status_code == 200

    def test_encoded_13_9255(self, client: Any) -> None:
        """Encoded payloads never crash the moderator."""
        payloads = [
            "%3Cscript%3E",
            "\\u003cscript\\u003e",
            "\\x3cscript\\x3e",
            "&#60;script&#62;",
            "\\u202eoverride",
        ]
        for payload in payloads:
            response = client.post("/moderate", json={"text": payload, "app_name": "a"})
            assert response.status_code == 200

    def test_encoded_14_9256(self, client: Any) -> None:
        """Encoded payloads never crash the moderator."""
        payloads = [
            "%3Cscript%3E",
            "\\u003cscript\\u003e",
            "\\x3cscript\\x3e",
            "&#60;script&#62;",
            "\\u202eoverride",
        ]
        for payload in payloads:
            response = client.post("/moderate", json={"text": payload, "app_name": "a"})
            assert response.status_code == 200

    def test_encoded_15_9257(self, client: Any) -> None:
        """Encoded payloads never crash the moderator."""
        payloads = [
            "%3Cscript%3E",
            "\\u003cscript\\u003e",
            "\\x3cscript\\x3e",
            "&#60;script&#62;",
            "\\u202eoverride",
        ]
        for payload in payloads:
            response = client.post("/moderate", json={"text": payload, "app_name": "a"})
            assert response.status_code == 200

    def test_encoded_16_9258(self, client: Any) -> None:
        """Encoded payloads never crash the moderator."""
        payloads = [
            "%3Cscript%3E",
            "\\u003cscript\\u003e",
            "\\x3cscript\\x3e",
            "&#60;script&#62;",
            "\\u202eoverride",
        ]
        for payload in payloads:
            response = client.post("/moderate", json={"text": payload, "app_name": "a"})
            assert response.status_code == 200

    def test_encoded_17_9259(self, client: Any) -> None:
        """Encoded payloads never crash the moderator."""
        payloads = [
            "%3Cscript%3E",
            "\\u003cscript\\u003e",
            "\\x3cscript\\x3e",
            "&#60;script&#62;",
            "\\u202eoverride",
        ]
        for payload in payloads:
            response = client.post("/moderate", json={"text": payload, "app_name": "a"})
            assert response.status_code == 200

    def test_encoded_18_9260(self, client: Any) -> None:
        """Encoded payloads never crash the moderator."""
        payloads = [
            "%3Cscript%3E",
            "\\u003cscript\\u003e",
            "\\x3cscript\\x3e",
            "&#60;script&#62;",
            "\\u202eoverride",
        ]
        for payload in payloads:
            response = client.post("/moderate", json={"text": payload, "app_name": "a"})
            assert response.status_code == 200

    def test_encoded_19_9261(self, client: Any) -> None:
        """Encoded payloads never crash the moderator."""
        payloads = [
            "%3Cscript%3E",
            "\\u003cscript\\u003e",
            "\\x3cscript\\x3e",
            "&#60;script&#62;",
            "\\u202eoverride",
        ]
        for payload in payloads:
            response = client.post("/moderate", json={"text": payload, "app_name": "a"})
            assert response.status_code == 200

    def test_encoded_20_9262(self, client: Any) -> None:
        """Encoded payloads never crash the moderator."""
        payloads = [
            "%3Cscript%3E",
            "\\u003cscript\\u003e",
            "\\x3cscript\\x3e",
            "&#60;script&#62;",
            "\\u202eoverride",
        ]
        for payload in payloads:
            response = client.post("/moderate", json={"text": payload, "app_name": "a"})
            assert response.status_code == 200

    def test_encoded_21_9263(self, client: Any) -> None:
        """Encoded payloads never crash the moderator."""
        payloads = [
            "%3Cscript%3E",
            "\\u003cscript\\u003e",
            "\\x3cscript\\x3e",
            "&#60;script&#62;",
            "\\u202eoverride",
        ]
        for payload in payloads:
            response = client.post("/moderate", json={"text": payload, "app_name": "a"})
            assert response.status_code == 200

    def test_encoded_22_9264(self, client: Any) -> None:
        """Encoded payloads never crash the moderator."""
        payloads = [
            "%3Cscript%3E",
            "\\u003cscript\\u003e",
            "\\x3cscript\\x3e",
            "&#60;script&#62;",
            "\\u202eoverride",
        ]
        for payload in payloads:
            response = client.post("/moderate", json={"text": payload, "app_name": "a"})
            assert response.status_code == 200

    def test_encoded_23_9265(self, client: Any) -> None:
        """Encoded payloads never crash the moderator."""
        payloads = [
            "%3Cscript%3E",
            "\\u003cscript\\u003e",
            "\\x3cscript\\x3e",
            "&#60;script&#62;",
            "\\u202eoverride",
        ]
        for payload in payloads:
            response = client.post("/moderate", json={"text": payload, "app_name": "a"})
            assert response.status_code == 200

    def test_encoded_24_9266(self, client: Any) -> None:
        """Encoded payloads never crash the moderator."""
        payloads = [
            "%3Cscript%3E",
            "\\u003cscript\\u003e",
            "\\x3cscript\\x3e",
            "&#60;script&#62;",
            "\\u202eoverride",
        ]
        for payload in payloads:
            response = client.post("/moderate", json={"text": payload, "app_name": "a"})
            assert response.status_code == 200

    def test_encoded_25_9267(self, client: Any) -> None:
        """Encoded payloads never crash the moderator."""
        payloads = [
            "%3Cscript%3E",
            "\\u003cscript\\u003e",
            "\\x3cscript\\x3e",
            "&#60;script&#62;",
            "\\u202eoverride",
        ]
        for payload in payloads:
            response = client.post("/moderate", json={"text": payload, "app_name": "a"})
            assert response.status_code == 200

    def test_encoded_26_9268(self, client: Any) -> None:
        """Encoded payloads never crash the moderator."""
        payloads = [
            "%3Cscript%3E",
            "\\u003cscript\\u003e",
            "\\x3cscript\\x3e",
            "&#60;script&#62;",
            "\\u202eoverride",
        ]
        for payload in payloads:
            response = client.post("/moderate", json={"text": payload, "app_name": "a"})
            assert response.status_code == 200

    def test_encoded_27_9269(self, client: Any) -> None:
        """Encoded payloads never crash the moderator."""
        payloads = [
            "%3Cscript%3E",
            "\\u003cscript\\u003e",
            "\\x3cscript\\x3e",
            "&#60;script&#62;",
            "\\u202eoverride",
        ]
        for payload in payloads:
            response = client.post("/moderate", json={"text": payload, "app_name": "a"})
            assert response.status_code == 200

    def test_encoded_28_9270(self, client: Any) -> None:
        """Encoded payloads never crash the moderator."""
        payloads = [
            "%3Cscript%3E",
            "\\u003cscript\\u003e",
            "\\x3cscript\\x3e",
            "&#60;script&#62;",
            "\\u202eoverride",
        ]
        for payload in payloads:
            response = client.post("/moderate", json={"text": payload, "app_name": "a"})
            assert response.status_code == 200

    def test_encoded_29_9271(self, client: Any) -> None:
        """Encoded payloads never crash the moderator."""
        payloads = [
            "%3Cscript%3E",
            "\\u003cscript\\u003e",
            "\\x3cscript\\x3e",
            "&#60;script&#62;",
            "\\u202eoverride",
        ]
        for payload in payloads:
            response = client.post("/moderate", json={"text": payload, "app_name": "a"})
            assert response.status_code == 200

    def test_encoded_30_9272(self, client: Any) -> None:
        """Encoded payloads never crash the moderator."""
        payloads = [
            "%3Cscript%3E",
            "\\u003cscript\\u003e",
            "\\x3cscript\\x3e",
            "&#60;script&#62;",
            "\\u202eoverride",
        ]
        for payload in payloads:
            response = client.post("/moderate", json={"text": payload, "app_name": "a"})
            assert response.status_code == 200

    def test_encoded_31_9273(self, client: Any) -> None:
        """Encoded payloads never crash the moderator."""
        payloads = [
            "%3Cscript%3E",
            "\\u003cscript\\u003e",
            "\\x3cscript\\x3e",
            "&#60;script&#62;",
            "\\u202eoverride",
        ]
        for payload in payloads:
            response = client.post("/moderate", json={"text": payload, "app_name": "a"})
            assert response.status_code == 200

    def test_encoded_32_9274(self, client: Any) -> None:
        """Encoded payloads never crash the moderator."""
        payloads = [
            "%3Cscript%3E",
            "\\u003cscript\\u003e",
            "\\x3cscript\\x3e",
            "&#60;script&#62;",
            "\\u202eoverride",
        ]
        for payload in payloads:
            response = client.post("/moderate", json={"text": payload, "app_name": "a"})
            assert response.status_code == 200

    def test_encoded_33_9275(self, client: Any) -> None:
        """Encoded payloads never crash the moderator."""
        payloads = [
            "%3Cscript%3E",
            "\\u003cscript\\u003e",
            "\\x3cscript\\x3e",
            "&#60;script&#62;",
            "\\u202eoverride",
        ]
        for payload in payloads:
            response = client.post("/moderate", json={"text": payload, "app_name": "a"})
            assert response.status_code == 200

    def test_encoded_34_9276(self, client: Any) -> None:
        """Encoded payloads never crash the moderator."""
        payloads = [
            "%3Cscript%3E",
            "\\u003cscript\\u003e",
            "\\x3cscript\\x3e",
            "&#60;script&#62;",
            "\\u202eoverride",
        ]
        for payload in payloads:
            response = client.post("/moderate", json={"text": payload, "app_name": "a"})
            assert response.status_code == 200

    def test_encoded_35_9277(self, client: Any) -> None:
        """Encoded payloads never crash the moderator."""
        payloads = [
            "%3Cscript%3E",
            "\\u003cscript\\u003e",
            "\\x3cscript\\x3e",
            "&#60;script&#62;",
            "\\u202eoverride",
        ]
        for payload in payloads:
            response = client.post("/moderate", json={"text": payload, "app_name": "a"})
            assert response.status_code == 200

    def test_encoded_36_9278(self, client: Any) -> None:
        """Encoded payloads never crash the moderator."""
        payloads = [
            "%3Cscript%3E",
            "\\u003cscript\\u003e",
            "\\x3cscript\\x3e",
            "&#60;script&#62;",
            "\\u202eoverride",
        ]
        for payload in payloads:
            response = client.post("/moderate", json={"text": payload, "app_name": "a"})
            assert response.status_code == 200

    def test_encoded_37_9279(self, client: Any) -> None:
        """Encoded payloads never crash the moderator."""
        payloads = [
            "%3Cscript%3E",
            "\\u003cscript\\u003e",
            "\\x3cscript\\x3e",
            "&#60;script&#62;",
            "\\u202eoverride",
        ]
        for payload in payloads:
            response = client.post("/moderate", json={"text": payload, "app_name": "a"})
            assert response.status_code == 200

    def test_encoded_38_9280(self, client: Any) -> None:
        """Encoded payloads never crash the moderator."""
        payloads = [
            "%3Cscript%3E",
            "\\u003cscript\\u003e",
            "\\x3cscript\\x3e",
            "&#60;script&#62;",
            "\\u202eoverride",
        ]
        for payload in payloads:
            response = client.post("/moderate", json={"text": payload, "app_name": "a"})
            assert response.status_code == 200

    def test_encoded_39_9281(self, client: Any) -> None:
        """Encoded payloads never crash the moderator."""
        payloads = [
            "%3Cscript%3E",
            "\\u003cscript\\u003e",
            "\\x3cscript\\x3e",
            "&#60;script&#62;",
            "\\u202eoverride",
        ]
        for payload in payloads:
            response = client.post("/moderate", json={"text": payload, "app_name": "a"})
            assert response.status_code == 200

    def test_encoded_40_9282(self, client: Any) -> None:
        """Encoded payloads never crash the moderator."""
        payloads = [
            "%3Cscript%3E",
            "\\u003cscript\\u003e",
            "\\x3cscript\\x3e",
            "&#60;script&#62;",
            "\\u202eoverride",
        ]
        for payload in payloads:
            response = client.post("/moderate", json={"text": payload, "app_name": "a"})
            assert response.status_code == 200

    def test_encoded_41_9283(self, client: Any) -> None:
        """Encoded payloads never crash the moderator."""
        payloads = [
            "%3Cscript%3E",
            "\\u003cscript\\u003e",
            "\\x3cscript\\x3e",
            "&#60;script&#62;",
            "\\u202eoverride",
        ]
        for payload in payloads:
            response = client.post("/moderate", json={"text": payload, "app_name": "a"})
            assert response.status_code == 200

    def test_encoded_42_9284(self, client: Any) -> None:
        """Encoded payloads never crash the moderator."""
        payloads = [
            "%3Cscript%3E",
            "\\u003cscript\\u003e",
            "\\x3cscript\\x3e",
            "&#60;script&#62;",
            "\\u202eoverride",
        ]
        for payload in payloads:
            response = client.post("/moderate", json={"text": payload, "app_name": "a"})
            assert response.status_code == 200

    def test_encoded_43_9285(self, client: Any) -> None:
        """Encoded payloads never crash the moderator."""
        payloads = [
            "%3Cscript%3E",
            "\\u003cscript\\u003e",
            "\\x3cscript\\x3e",
            "&#60;script&#62;",
            "\\u202eoverride",
        ]
        for payload in payloads:
            response = client.post("/moderate", json={"text": payload, "app_name": "a"})
            assert response.status_code == 200

    def test_encoded_44_9286(self, client: Any) -> None:
        """Encoded payloads never crash the moderator."""
        payloads = [
            "%3Cscript%3E",
            "\\u003cscript\\u003e",
            "\\x3cscript\\x3e",
            "&#60;script&#62;",
            "\\u202eoverride",
        ]
        for payload in payloads:
            response = client.post("/moderate", json={"text": payload, "app_name": "a"})
            assert response.status_code == 200

    def test_encoded_45_9287(self, client: Any) -> None:
        """Encoded payloads never crash the moderator."""
        payloads = [
            "%3Cscript%3E",
            "\\u003cscript\\u003e",
            "\\x3cscript\\x3e",
            "&#60;script&#62;",
            "\\u202eoverride",
        ]
        for payload in payloads:
            response = client.post("/moderate", json={"text": payload, "app_name": "a"})
            assert response.status_code == 200

    def test_encoded_46_9288(self, client: Any) -> None:
        """Encoded payloads never crash the moderator."""
        payloads = [
            "%3Cscript%3E",
            "\\u003cscript\\u003e",
            "\\x3cscript\\x3e",
            "&#60;script&#62;",
            "\\u202eoverride",
        ]
        for payload in payloads:
            response = client.post("/moderate", json={"text": payload, "app_name": "a"})
            assert response.status_code == 200

    def test_encoded_47_9289(self, client: Any) -> None:
        """Encoded payloads never crash the moderator."""
        payloads = [
            "%3Cscript%3E",
            "\\u003cscript\\u003e",
            "\\x3cscript\\x3e",
            "&#60;script&#62;",
            "\\u202eoverride",
        ]
        for payload in payloads:
            response = client.post("/moderate", json={"text": payload, "app_name": "a"})
            assert response.status_code == 200

    def test_encoded_48_9290(self, client: Any) -> None:
        """Encoded payloads never crash the moderator."""
        payloads = [
            "%3Cscript%3E",
            "\\u003cscript\\u003e",
            "\\x3cscript\\x3e",
            "&#60;script&#62;",
            "\\u202eoverride",
        ]
        for payload in payloads:
            response = client.post("/moderate", json={"text": payload, "app_name": "a"})
            assert response.status_code == 200

    def test_encoded_49_9291(self, client: Any) -> None:
        """Encoded payloads never crash the moderator."""
        payloads = [
            "%3Cscript%3E",
            "\\u003cscript\\u003e",
            "\\x3cscript\\x3e",
            "&#60;script&#62;",
            "\\u202eoverride",
        ]
        for payload in payloads:
            response = client.post("/moderate", json={"text": payload, "app_name": "a"})
            assert response.status_code == 200

    def test_encoded_50_9292(self, client: Any) -> None:
        """Encoded payloads never crash the moderator."""
        payloads = [
            "%3Cscript%3E",
            "\\u003cscript\\u003e",
            "\\x3cscript\\x3e",
            "&#60;script&#62;",
            "\\u202eoverride",
        ]
        for payload in payloads:
            response = client.post("/moderate", json={"text": payload, "app_name": "a"})
            assert response.status_code == 200

    def test_encoded_51_9293(self, client: Any) -> None:
        """Encoded payloads never crash the moderator."""
        payloads = [
            "%3Cscript%3E",
            "\\u003cscript\\u003e",
            "\\x3cscript\\x3e",
            "&#60;script&#62;",
            "\\u202eoverride",
        ]
        for payload in payloads:
            response = client.post("/moderate", json={"text": payload, "app_name": "a"})
            assert response.status_code == 200

    def test_encoded_52_9294(self, client: Any) -> None:
        """Encoded payloads never crash the moderator."""
        payloads = [
            "%3Cscript%3E",
            "\\u003cscript\\u003e",
            "\\x3cscript\\x3e",
            "&#60;script&#62;",
            "\\u202eoverride",
        ]
        for payload in payloads:
            response = client.post("/moderate", json={"text": payload, "app_name": "a"})
            assert response.status_code == 200

    def test_encoded_53_9295(self, client: Any) -> None:
        """Encoded payloads never crash the moderator."""
        payloads = [
            "%3Cscript%3E",
            "\\u003cscript\\u003e",
            "\\x3cscript\\x3e",
            "&#60;script&#62;",
            "\\u202eoverride",
        ]
        for payload in payloads:
            response = client.post("/moderate", json={"text": payload, "app_name": "a"})
            assert response.status_code == 200

    def test_encoded_54_9296(self, client: Any) -> None:
        """Encoded payloads never crash the moderator."""
        payloads = [
            "%3Cscript%3E",
            "\\u003cscript\\u003e",
            "\\x3cscript\\x3e",
            "&#60;script&#62;",
            "\\u202eoverride",
        ]
        for payload in payloads:
            response = client.post("/moderate", json={"text": payload, "app_name": "a"})
            assert response.status_code == 200

    def test_encoded_55_9297(self, client: Any) -> None:
        """Encoded payloads never crash the moderator."""
        payloads = [
            "%3Cscript%3E",
            "\\u003cscript\\u003e",
            "\\x3cscript\\x3e",
            "&#60;script&#62;",
            "\\u202eoverride",
        ]
        for payload in payloads:
            response = client.post("/moderate", json={"text": payload, "app_name": "a"})
            assert response.status_code == 200

    def test_encoded_56_9298(self, client: Any) -> None:
        """Encoded payloads never crash the moderator."""
        payloads = [
            "%3Cscript%3E",
            "\\u003cscript\\u003e",
            "\\x3cscript\\x3e",
            "&#60;script&#62;",
            "\\u202eoverride",
        ]
        for payload in payloads:
            response = client.post("/moderate", json={"text": payload, "app_name": "a"})
            assert response.status_code == 200

    def test_encoded_57_9299(self, client: Any) -> None:
        """Encoded payloads never crash the moderator."""
        payloads = [
            "%3Cscript%3E",
            "\\u003cscript\\u003e",
            "\\x3cscript\\x3e",
            "&#60;script&#62;",
            "\\u202eoverride",
        ]
        for payload in payloads:
            response = client.post("/moderate", json={"text": payload, "app_name": "a"})
            assert response.status_code == 200

    def test_encoded_58_9300(self, client: Any) -> None:
        """Encoded payloads never crash the moderator."""
        payloads = [
            "%3Cscript%3E",
            "\\u003cscript\\u003e",
            "\\x3cscript\\x3e",
            "&#60;script&#62;",
            "\\u202eoverride",
        ]
        for payload in payloads:
            response = client.post("/moderate", json={"text": payload, "app_name": "a"})
            assert response.status_code == 200

    def test_encoded_59_9301(self, client: Any) -> None:
        """Encoded payloads never crash the moderator."""
        payloads = [
            "%3Cscript%3E",
            "\\u003cscript\\u003e",
            "\\x3cscript\\x3e",
            "&#60;script&#62;",
            "\\u202eoverride",
        ]
        for payload in payloads:
            response = client.post("/moderate", json={"text": payload, "app_name": "a"})
            assert response.status_code == 200

    def test_encoded_60_9302(self, client: Any) -> None:
        """Encoded payloads never crash the moderator."""
        payloads = [
            "%3Cscript%3E",
            "\\u003cscript\\u003e",
            "\\x3cscript\\x3e",
            "&#60;script&#62;",
            "\\u202eoverride",
        ]
        for payload in payloads:
            response = client.post("/moderate", json={"text": payload, "app_name": "a"})
            assert response.status_code == 200

    def test_encoded_61_9303(self, client: Any) -> None:
        """Encoded payloads never crash the moderator."""
        payloads = [
            "%3Cscript%3E",
            "\\u003cscript\\u003e",
            "\\x3cscript\\x3e",
            "&#60;script&#62;",
            "\\u202eoverride",
        ]
        for payload in payloads:
            response = client.post("/moderate", json={"text": payload, "app_name": "a"})
            assert response.status_code == 200

    def test_encoded_62_9304(self, client: Any) -> None:
        """Encoded payloads never crash the moderator."""
        payloads = [
            "%3Cscript%3E",
            "\\u003cscript\\u003e",
            "\\x3cscript\\x3e",
            "&#60;script&#62;",
            "\\u202eoverride",
        ]
        for payload in payloads:
            response = client.post("/moderate", json={"text": payload, "app_name": "a"})
            assert response.status_code == 200

    def test_encoded_63_9305(self, client: Any) -> None:
        """Encoded payloads never crash the moderator."""
        payloads = [
            "%3Cscript%3E",
            "\\u003cscript\\u003e",
            "\\x3cscript\\x3e",
            "&#60;script&#62;",
            "\\u202eoverride",
        ]
        for payload in payloads:
            response = client.post("/moderate", json={"text": payload, "app_name": "a"})
            assert response.status_code == 200

    def test_encoded_64_9306(self, client: Any) -> None:
        """Encoded payloads never crash the moderator."""
        payloads = [
            "%3Cscript%3E",
            "\\u003cscript\\u003e",
            "\\x3cscript\\x3e",
            "&#60;script&#62;",
            "\\u202eoverride",
        ]
        for payload in payloads:
            response = client.post("/moderate", json={"text": payload, "app_name": "a"})
            assert response.status_code == 200

    def test_encoded_65_9307(self, client: Any) -> None:
        """Encoded payloads never crash the moderator."""
        payloads = [
            "%3Cscript%3E",
            "\\u003cscript\\u003e",
            "\\x3cscript\\x3e",
            "&#60;script&#62;",
            "\\u202eoverride",
        ]
        for payload in payloads:
            response = client.post("/moderate", json={"text": payload, "app_name": "a"})
            assert response.status_code == 200

    def test_encoded_66_9308(self, client: Any) -> None:
        """Encoded payloads never crash the moderator."""
        payloads = [
            "%3Cscript%3E",
            "\\u003cscript\\u003e",
            "\\x3cscript\\x3e",
            "&#60;script&#62;",
            "\\u202eoverride",
        ]
        for payload in payloads:
            response = client.post("/moderate", json={"text": payload, "app_name": "a"})
            assert response.status_code == 200

    def test_encoded_67_9309(self, client: Any) -> None:
        """Encoded payloads never crash the moderator."""
        payloads = [
            "%3Cscript%3E",
            "\\u003cscript\\u003e",
            "\\x3cscript\\x3e",
            "&#60;script&#62;",
            "\\u202eoverride",
        ]
        for payload in payloads:
            response = client.post("/moderate", json={"text": payload, "app_name": "a"})
            assert response.status_code == 200

    def test_encoded_68_9310(self, client: Any) -> None:
        """Encoded payloads never crash the moderator."""
        payloads = [
            "%3Cscript%3E",
            "\\u003cscript\\u003e",
            "\\x3cscript\\x3e",
            "&#60;script&#62;",
            "\\u202eoverride",
        ]
        for payload in payloads:
            response = client.post("/moderate", json={"text": payload, "app_name": "a"})
            assert response.status_code == 200

    def test_encoded_69_9311(self, client: Any) -> None:
        """Encoded payloads never crash the moderator."""
        payloads = [
            "%3Cscript%3E",
            "\\u003cscript\\u003e",
            "\\x3cscript\\x3e",
            "&#60;script&#62;",
            "\\u202eoverride",
        ]
        for payload in payloads:
            response = client.post("/moderate", json={"text": payload, "app_name": "a"})
            assert response.status_code == 200

    def test_encoded_70_9312(self, client: Any) -> None:
        """Encoded payloads never crash the moderator."""
        payloads = [
            "%3Cscript%3E",
            "\\u003cscript\\u003e",
            "\\x3cscript\\x3e",
            "&#60;script&#62;",
            "\\u202eoverride",
        ]
        for payload in payloads:
            response = client.post("/moderate", json={"text": payload, "app_name": "a"})
            assert response.status_code == 200

    def test_encoded_71_9313(self, client: Any) -> None:
        """Encoded payloads never crash the moderator."""
        payloads = [
            "%3Cscript%3E",
            "\\u003cscript\\u003e",
            "\\x3cscript\\x3e",
            "&#60;script&#62;",
            "\\u202eoverride",
        ]
        for payload in payloads:
            response = client.post("/moderate", json={"text": payload, "app_name": "a"})
            assert response.status_code == 200

    def test_encoded_72_9314(self, client: Any) -> None:
        """Encoded payloads never crash the moderator."""
        payloads = [
            "%3Cscript%3E",
            "\\u003cscript\\u003e",
            "\\x3cscript\\x3e",
            "&#60;script&#62;",
            "\\u202eoverride",
        ]
        for payload in payloads:
            response = client.post("/moderate", json={"text": payload, "app_name": "a"})
            assert response.status_code == 200

    def test_encoded_73_9315(self, client: Any) -> None:
        """Encoded payloads never crash the moderator."""
        payloads = [
            "%3Cscript%3E",
            "\\u003cscript\\u003e",
            "\\x3cscript\\x3e",
            "&#60;script&#62;",
            "\\u202eoverride",
        ]
        for payload in payloads:
            response = client.post("/moderate", json={"text": payload, "app_name": "a"})
            assert response.status_code == 200

    def test_encoded_74_9316(self, client: Any) -> None:
        """Encoded payloads never crash the moderator."""
        payloads = [
            "%3Cscript%3E",
            "\\u003cscript\\u003e",
            "\\x3cscript\\x3e",
            "&#60;script&#62;",
            "\\u202eoverride",
        ]
        for payload in payloads:
            response = client.post("/moderate", json={"text": payload, "app_name": "a"})
            assert response.status_code == 200

    def test_encoded_75_9317(self, client: Any) -> None:
        """Encoded payloads never crash the moderator."""
        payloads = [
            "%3Cscript%3E",
            "\\u003cscript\\u003e",
            "\\x3cscript\\x3e",
            "&#60;script&#62;",
            "\\u202eoverride",
        ]
        for payload in payloads:
            response = client.post("/moderate", json={"text": payload, "app_name": "a"})
            assert response.status_code == 200

    def test_encoded_76_9318(self, client: Any) -> None:
        """Encoded payloads never crash the moderator."""
        payloads = [
            "%3Cscript%3E",
            "\\u003cscript\\u003e",
            "\\x3cscript\\x3e",
            "&#60;script&#62;",
            "\\u202eoverride",
        ]
        for payload in payloads:
            response = client.post("/moderate", json={"text": payload, "app_name": "a"})
            assert response.status_code == 200

    def test_encoded_77_9319(self, client: Any) -> None:
        """Encoded payloads never crash the moderator."""
        payloads = [
            "%3Cscript%3E",
            "\\u003cscript\\u003e",
            "\\x3cscript\\x3e",
            "&#60;script&#62;",
            "\\u202eoverride",
        ]
        for payload in payloads:
            response = client.post("/moderate", json={"text": payload, "app_name": "a"})
            assert response.status_code == 200

    def test_encoded_78_9320(self, client: Any) -> None:
        """Encoded payloads never crash the moderator."""
        payloads = [
            "%3Cscript%3E",
            "\\u003cscript\\u003e",
            "\\x3cscript\\x3e",
            "&#60;script&#62;",
            "\\u202eoverride",
        ]
        for payload in payloads:
            response = client.post("/moderate", json={"text": payload, "app_name": "a"})
            assert response.status_code == 200

    def test_encoded_79_9321(self, client: Any) -> None:
        """Encoded payloads never crash the moderator."""
        payloads = [
            "%3Cscript%3E",
            "\\u003cscript\\u003e",
            "\\x3cscript\\x3e",
            "&#60;script&#62;",
            "\\u202eoverride",
        ]
        for payload in payloads:
            response = client.post("/moderate", json={"text": payload, "app_name": "a"})
            assert response.status_code == 200

    def test_encoded_80_9322(self, client: Any) -> None:
        """Encoded payloads never crash the moderator."""
        payloads = [
            "%3Cscript%3E",
            "\\u003cscript\\u003e",
            "\\x3cscript\\x3e",
            "&#60;script&#62;",
            "\\u202eoverride",
        ]
        for payload in payloads:
            response = client.post("/moderate", json={"text": payload, "app_name": "a"})
            assert response.status_code == 200

    def test_encoded_81_9323(self, client: Any) -> None:
        """Encoded payloads never crash the moderator."""
        payloads = [
            "%3Cscript%3E",
            "\\u003cscript\\u003e",
            "\\x3cscript\\x3e",
            "&#60;script&#62;",
            "\\u202eoverride",
        ]
        for payload in payloads:
            response = client.post("/moderate", json={"text": payload, "app_name": "a"})
            assert response.status_code == 200

    def test_encoded_82_9324(self, client: Any) -> None:
        """Encoded payloads never crash the moderator."""
        payloads = [
            "%3Cscript%3E",
            "\\u003cscript\\u003e",
            "\\x3cscript\\x3e",
            "&#60;script&#62;",
            "\\u202eoverride",
        ]
        for payload in payloads:
            response = client.post("/moderate", json={"text": payload, "app_name": "a"})
            assert response.status_code == 200

    def test_encoded_83_9325(self, client: Any) -> None:
        """Encoded payloads never crash the moderator."""
        payloads = [
            "%3Cscript%3E",
            "\\u003cscript\\u003e",
            "\\x3cscript\\x3e",
            "&#60;script&#62;",
            "\\u202eoverride",
        ]
        for payload in payloads:
            response = client.post("/moderate", json={"text": payload, "app_name": "a"})
            assert response.status_code == 200

    def test_encoded_84_9326(self, client: Any) -> None:
        """Encoded payloads never crash the moderator."""
        payloads = [
            "%3Cscript%3E",
            "\\u003cscript\\u003e",
            "\\x3cscript\\x3e",
            "&#60;script&#62;",
            "\\u202eoverride",
        ]
        for payload in payloads:
            response = client.post("/moderate", json={"text": payload, "app_name": "a"})
            assert response.status_code == 200

    def test_encoded_85_9327(self, client: Any) -> None:
        """Encoded payloads never crash the moderator."""
        payloads = [
            "%3Cscript%3E",
            "\\u003cscript\\u003e",
            "\\x3cscript\\x3e",
            "&#60;script&#62;",
            "\\u202eoverride",
        ]
        for payload in payloads:
            response = client.post("/moderate", json={"text": payload, "app_name": "a"})
            assert response.status_code == 200

    def test_encoded_86_9328(self, client: Any) -> None:
        """Encoded payloads never crash the moderator."""
        payloads = [
            "%3Cscript%3E",
            "\\u003cscript\\u003e",
            "\\x3cscript\\x3e",
            "&#60;script&#62;",
            "\\u202eoverride",
        ]
        for payload in payloads:
            response = client.post("/moderate", json={"text": payload, "app_name": "a"})
            assert response.status_code == 200

    def test_encoded_87_9329(self, client: Any) -> None:
        """Encoded payloads never crash the moderator."""
        payloads = [
            "%3Cscript%3E",
            "\\u003cscript\\u003e",
            "\\x3cscript\\x3e",
            "&#60;script&#62;",
            "\\u202eoverride",
        ]
        for payload in payloads:
            response = client.post("/moderate", json={"text": payload, "app_name": "a"})
            assert response.status_code == 200

    def test_encoded_88_9330(self, client: Any) -> None:
        """Encoded payloads never crash the moderator."""
        payloads = [
            "%3Cscript%3E",
            "\\u003cscript\\u003e",
            "\\x3cscript\\x3e",
            "&#60;script&#62;",
            "\\u202eoverride",
        ]
        for payload in payloads:
            response = client.post("/moderate", json={"text": payload, "app_name": "a"})
            assert response.status_code == 200

    def test_encoded_89_9331(self, client: Any) -> None:
        """Encoded payloads never crash the moderator."""
        payloads = [
            "%3Cscript%3E",
            "\\u003cscript\\u003e",
            "\\x3cscript\\x3e",
            "&#60;script&#62;",
            "\\u202eoverride",
        ]
        for payload in payloads:
            response = client.post("/moderate", json={"text": payload, "app_name": "a"})
            assert response.status_code == 200

    def test_encoded_90_9332(self, client: Any) -> None:
        """Encoded payloads never crash the moderator."""
        payloads = [
            "%3Cscript%3E",
            "\\u003cscript\\u003e",
            "\\x3cscript\\x3e",
            "&#60;script&#62;",
            "\\u202eoverride",
        ]
        for payload in payloads:
            response = client.post("/moderate", json={"text": payload, "app_name": "a"})
            assert response.status_code == 200

    def test_encoded_91_9333(self, client: Any) -> None:
        """Encoded payloads never crash the moderator."""
        payloads = [
            "%3Cscript%3E",
            "\\u003cscript\\u003e",
            "\\x3cscript\\x3e",
            "&#60;script&#62;",
            "\\u202eoverride",
        ]
        for payload in payloads:
            response = client.post("/moderate", json={"text": payload, "app_name": "a"})
            assert response.status_code == 200

    def test_encoded_92_9334(self, client: Any) -> None:
        """Encoded payloads never crash the moderator."""
        payloads = [
            "%3Cscript%3E",
            "\\u003cscript\\u003e",
            "\\x3cscript\\x3e",
            "&#60;script&#62;",
            "\\u202eoverride",
        ]
        for payload in payloads:
            response = client.post("/moderate", json={"text": payload, "app_name": "a"})
            assert response.status_code == 200

    def test_encoded_93_9335(self, client: Any) -> None:
        """Encoded payloads never crash the moderator."""
        payloads = [
            "%3Cscript%3E",
            "\\u003cscript\\u003e",
            "\\x3cscript\\x3e",
            "&#60;script&#62;",
            "\\u202eoverride",
        ]
        for payload in payloads:
            response = client.post("/moderate", json={"text": payload, "app_name": "a"})
            assert response.status_code == 200

    def test_encoded_94_9336(self, client: Any) -> None:
        """Encoded payloads never crash the moderator."""
        payloads = [
            "%3Cscript%3E",
            "\\u003cscript\\u003e",
            "\\x3cscript\\x3e",
            "&#60;script&#62;",
            "\\u202eoverride",
        ]
        for payload in payloads:
            response = client.post("/moderate", json={"text": payload, "app_name": "a"})
            assert response.status_code == 200

    def test_encoded_95_9337(self, client: Any) -> None:
        """Encoded payloads never crash the moderator."""
        payloads = [
            "%3Cscript%3E",
            "\\u003cscript\\u003e",
            "\\x3cscript\\x3e",
            "&#60;script&#62;",
            "\\u202eoverride",
        ]
        for payload in payloads:
            response = client.post("/moderate", json={"text": payload, "app_name": "a"})
            assert response.status_code == 200

    def test_encoded_96_9338(self, client: Any) -> None:
        """Encoded payloads never crash the moderator."""
        payloads = [
            "%3Cscript%3E",
            "\\u003cscript\\u003e",
            "\\x3cscript\\x3e",
            "&#60;script&#62;",
            "\\u202eoverride",
        ]
        for payload in payloads:
            response = client.post("/moderate", json={"text": payload, "app_name": "a"})
            assert response.status_code == 200

    def test_encoded_97_9339(self, client: Any) -> None:
        """Encoded payloads never crash the moderator."""
        payloads = [
            "%3Cscript%3E",
            "\\u003cscript\\u003e",
            "\\x3cscript\\x3e",
            "&#60;script&#62;",
            "\\u202eoverride",
        ]
        for payload in payloads:
            response = client.post("/moderate", json={"text": payload, "app_name": "a"})
            assert response.status_code == 200

    def test_encoded_98_9340(self, client: Any) -> None:
        """Encoded payloads never crash the moderator."""
        payloads = [
            "%3Cscript%3E",
            "\\u003cscript\\u003e",
            "\\x3cscript\\x3e",
            "&#60;script&#62;",
            "\\u202eoverride",
        ]
        for payload in payloads:
            response = client.post("/moderate", json={"text": payload, "app_name": "a"})
            assert response.status_code == 200

    def test_encoded_99_9341(self, client: Any) -> None:
        """Encoded payloads never crash the moderator."""
        payloads = [
            "%3Cscript%3E",
            "\\u003cscript\\u003e",
            "\\x3cscript\\x3e",
            "&#60;script&#62;",
            "\\u202eoverride",
        ]
        for payload in payloads:
            response = client.post("/moderate", json={"text": payload, "app_name": "a"})
            assert response.status_code == 200
