"""Phase 2 security tests (generated).

Header parity, CORS, auth bypass, injection, traversal, method
restrictions and encoded payloads; see tests/tools/phase2_generator.py."""

# multilingual fixtures use non-ASCII on purpose
from __future__ import annotations

from typing import Any

import pytest

from tests.base_test import BaseTest

_AUTH_REJECTED_CASES: tuple[tuple[str, int], ...] = (
    (
        "",
        8772,
    ),
    (
        "",
        8773,
    ),
    (
        "",
        8774,
    ),
    (
        "",
        8775,
    ),
    (
        "",
        8776,
    ),
    (
        "",
        8777,
    ),
    (
        "",
        8778,
    ),
    (
        "",
        8779,
    ),
    (
        "",
        8780,
    ),
    (
        "",
        8781,
    ),
    (
        " ",
        8782,
    ),
    (
        " ",
        8783,
    ),
    (
        " ",
        8784,
    ),
    (
        " ",
        8785,
    ),
    (
        " ",
        8786,
    ),
    (
        " ",
        8787,
    ),
    (
        " ",
        8788,
    ),
    (
        " ",
        8789,
    ),
    (
        " ",
        8790,
    ),
    (
        " ",
        8791,
    ),
    (
        "null",
        8792,
    ),
    (
        "null",
        8793,
    ),
    (
        "null",
        8794,
    ),
    (
        "null",
        8795,
    ),
    (
        "null",
        8796,
    ),
    (
        "null",
        8797,
    ),
    (
        "null",
        8798,
    ),
    (
        "null",
        8799,
    ),
    (
        "null",
        8800,
    ),
    (
        "null",
        8801,
    ),
    (
        "None",
        8802,
    ),
    (
        "None",
        8803,
    ),
    (
        "None",
        8804,
    ),
    (
        "None",
        8805,
    ),
    (
        "None",
        8806,
    ),
    (
        "None",
        8807,
    ),
    (
        "None",
        8808,
    ),
    (
        "None",
        8809,
    ),
    (
        "None",
        8810,
    ),
    (
        "None",
        8811,
    ),
    (
        "CHANGE_ME",
        8812,
    ),
    (
        "CHANGE_ME",
        8813,
    ),
    (
        "CHANGE_ME",
        8814,
    ),
    (
        "CHANGE_ME",
        8815,
    ),
    (
        "CHANGE_ME",
        8816,
    ),
    (
        "CHANGE_ME",
        8817,
    ),
    (
        "CHANGE_ME",
        8818,
    ),
    (
        "CHANGE_ME",
        8819,
    ),
    (
        "CHANGE_ME",
        8820,
    ),
    (
        "CHANGE_ME",
        8821,
    ),
    (
        "wrong-key",
        8822,
    ),
    (
        "wrong-key",
        8823,
    ),
    (
        "wrong-key",
        8824,
    ),
    (
        "wrong-key",
        8825,
    ),
    (
        "wrong-key",
        8826,
    ),
    (
        "wrong-key",
        8827,
    ),
    (
        "wrong-key",
        8828,
    ),
    (
        "wrong-key",
        8829,
    ),
    (
        "wrong-key",
        8830,
    ),
    (
        "wrong-key",
        8831,
    ),
    (
        "test-admin-key ",
        8832,
    ),
    (
        "test-admin-key ",
        8833,
    ),
    (
        "test-admin-key ",
        8834,
    ),
    (
        "test-admin-key ",
        8835,
    ),
    (
        "test-admin-key ",
        8836,
    ),
    (
        "test-admin-key ",
        8837,
    ),
    (
        "test-admin-key ",
        8838,
    ),
    (
        "test-admin-key ",
        8839,
    ),
    (
        "test-admin-key ",
        8840,
    ),
    (
        "test-admin-key ",
        8841,
    ),
    (
        "TEST-ADMIN-KEY",
        8842,
    ),
    (
        "TEST-ADMIN-KEY",
        8843,
    ),
    (
        "TEST-ADMIN-KEY",
        8844,
    ),
    (
        "TEST-ADMIN-KEY",
        8845,
    ),
    (
        "TEST-ADMIN-KEY",
        8846,
    ),
    (
        "TEST-ADMIN-KEY",
        8847,
    ),
    (
        "TEST-ADMIN-KEY",
        8848,
    ),
    (
        "TEST-ADMIN-KEY",
        8849,
    ),
    (
        "TEST-ADMIN-KEY",
        8850,
    ),
    (
        "TEST-ADMIN-KEY",
        8851,
    ),
    (
        "bearer-token",
        8852,
    ),
    (
        "bearer-token",
        8853,
    ),
    (
        "bearer-token",
        8854,
    ),
    (
        "bearer-token",
        8855,
    ),
    (
        "bearer-token",
        8856,
    ),
    (
        "bearer-token",
        8857,
    ),
    (
        "bearer-token",
        8858,
    ),
    (
        "bearer-token",
        8859,
    ),
    (
        "bearer-token",
        8860,
    ),
    (
        "bearer-token",
        8861,
    ),
    (
        "leaked-secret",
        8862,
    ),
    (
        "leaked-secret",
        8863,
    ),
    (
        "leaked-secret",
        8864,
    ),
    (
        "leaked-secret",
        8865,
    ),
    (
        "leaked-secret",
        8866,
    ),
    (
        "leaked-secret",
        8867,
    ),
    (
        "leaked-secret",
        8868,
    ),
    (
        "leaked-secret",
        8869,
    ),
    (
        "leaked-secret",
        8870,
    ),
    (
        "leaked-secret",
        8871,
    ),
)


class TestAuthRejected(BaseTest):
    """Invalid credentials are rejected on admin endpoints."""

    @pytest.mark.parametrize(
        (
            "key",
            "uid",
        ),
        _AUTH_REJECTED_CASES,
    )
    def test_auth_rejected(self, client: Any, key: str, uid: int) -> None:
        """Invalid credentials are rejected on admin endpoints."""
        response = client.get("/admin/wordbank/stats", headers={"X-API-Key": key})
        assert response.status_code == 401
        bearer = client.get("/admin/wordbank/stats", headers={"Authorization": f"Bearer {key}"})
        assert bearer.status_code == 401
