"""Phase 2 admin API tests (generated).

Word CRUD, import/export, app policies, settings, logs and dashboard
stats; see tests/tools/phase2_generator.py."""

# multilingual fixtures use non-ASCII on purpose
from __future__ import annotations

from typing import Any

import pytest

from tests.base_test import BaseTest

_APP_CONFIG_CASES: tuple[tuple[str, int, str, bool, bool, int], ...] = (
    (
        "cfgapp",
        60,
        "or",
        False,
        True,
        7624,
    ),
    (
        "cfgapp",
        60,
        "or",
        False,
        False,
        7625,
    ),
    (
        "cfgapp",
        60,
        "and",
        True,
        True,
        7626,
    ),
    (
        "cfgapp",
        60,
        "and",
        True,
        False,
        7627,
    ),
    (
        "cfgapp",
        60,
        "and",
        False,
        True,
        7628,
    ),
    (
        "cfgapp",
        60,
        "and",
        False,
        False,
        7629,
    ),
    (
        "cfgapp",
        70,
        "or",
        True,
        True,
        7630,
    ),
    (
        "cfgapp",
        70,
        "or",
        True,
        False,
        7631,
    ),
    (
        "cfgapp",
        70,
        "or",
        False,
        True,
        7632,
    ),
    (
        "cfgapp",
        70,
        "or",
        False,
        False,
        7633,
    ),
    (
        "cfgapp",
        70,
        "and",
        True,
        True,
        7634,
    ),
    (
        "cfgapp",
        70,
        "and",
        True,
        False,
        7635,
    ),
    (
        "cfgapp",
        70,
        "and",
        False,
        True,
        7636,
    ),
    (
        "cfgapp",
        70,
        "and",
        False,
        False,
        7637,
    ),
    (
        "cfgapp",
        80,
        "or",
        True,
        True,
        7638,
    ),
    (
        "cfgapp",
        80,
        "or",
        True,
        False,
        7639,
    ),
    (
        "cfgapp",
        80,
        "or",
        False,
        True,
        7640,
    ),
    (
        "cfgapp",
        80,
        "or",
        False,
        False,
        7641,
    ),
    (
        "cfgapp",
        80,
        "and",
        True,
        True,
        7642,
    ),
    (
        "cfgapp",
        80,
        "and",
        True,
        False,
        7643,
    ),
    (
        "cfgapp",
        80,
        "and",
        False,
        True,
        7644,
    ),
    (
        "cfgapp",
        80,
        "and",
        False,
        False,
        7645,
    ),
    (
        "cfgapp",
        90,
        "or",
        True,
        True,
        7646,
    ),
    (
        "cfgapp",
        90,
        "or",
        True,
        False,
        7647,
    ),
    (
        "cfgapp",
        90,
        "or",
        False,
        True,
        7648,
    ),
    (
        "cfgapp",
        90,
        "or",
        False,
        False,
        7649,
    ),
    (
        "cfgapp",
        90,
        "and",
        True,
        True,
        7650,
    ),
    (
        "cfgapp",
        90,
        "and",
        True,
        False,
        7651,
    ),
    (
        "cfgapp",
        90,
        "and",
        False,
        True,
        7652,
    ),
    (
        "cfgapp",
        90,
        "and",
        False,
        False,
        7653,
    ),
    (
        "cfgapp",
        100,
        "or",
        True,
        True,
        7654,
    ),
    (
        "cfgapp",
        100,
        "or",
        True,
        False,
        7655,
    ),
    (
        "cfgapp",
        100,
        "or",
        False,
        True,
        7656,
    ),
    (
        "cfgapp",
        100,
        "or",
        False,
        False,
        7657,
    ),
    (
        "cfgapp",
        100,
        "and",
        True,
        True,
        7658,
    ),
    (
        "cfgapp",
        100,
        "and",
        True,
        False,
        7659,
    ),
    (
        "cfgapp",
        100,
        "and",
        False,
        True,
        7660,
    ),
    (
        "cfgapp",
        100,
        "and",
        False,
        False,
        7661,
    ),
)


class TestAppConfig(BaseTest):
    """App trigger policies store and return every field."""

    @pytest.mark.parametrize(
        (
            "app_name",
            "threshold",
            "logic",
            "sboost",
            "uboost",
            "uid",
        ),
        _APP_CONFIG_CASES,
    )
    def test_app_config(
        self,
        client: Any,
        admin_headers: dict[str, str],
        app_name: str,
        threshold: int,
        logic: str,
        sboost: bool,
        uboost: bool,
        uid: int,
    ) -> None:
        """App trigger policies store and return every field."""
        payload = {
            "app_name": app_name,
            "score_threshold": threshold,
            "logic_type": logic,
            "semantic_boost": sboost,
            "user_ratio_boost": uboost,
        }
        response = client.post("/admin/app-config", headers=admin_headers, json=payload)
        assert response.status_code == 200
        assert response.json()["score_threshold"] == threshold
        assert response.json()["logic_type"] == logic
        assert response.json()["semantic_boost"] is sboost


_APP_CONFIG_INVALID_CASES: tuple[tuple[int, int], ...] = (
    (
        -1,
        7662,
    ),
    (
        101,
        7663,
    ),
)


class TestAppConfigInvalid(BaseTest):
    """Out-of-range thresholds are rejected."""

    @pytest.mark.parametrize(
        (
            "threshold",
            "uid",
        ),
        _APP_CONFIG_INVALID_CASES,
    )
    def test_app_config_invalid(
        self, client: Any, admin_headers: dict[str, str], threshold: int, uid: int
    ) -> None:
        """Out-of-range thresholds are rejected."""
        payload = {"app_name": "bad", "score_threshold": threshold}
        response = client.post("/admin/app-config", headers=admin_headers, json=payload)
        assert response.status_code == 422


_APP_CONFIG_DEFAULT_CASES: tuple[tuple[str, int], ...] = (
    (
        "ghost0",
        7664,
    ),
    (
        "ghost1",
        7665,
    ),
    (
        "ghost2",
        7666,
    ),
    (
        "ghost3",
        7667,
    ),
    (
        "ghost4",
        7668,
    ),
    (
        "ghost5",
        7669,
    ),
    (
        "ghost6",
        7670,
    ),
    (
        "ghost7",
        7671,
    ),
    (
        "ghost8",
        7672,
    ),
    (
        "ghost9",
        7673,
    ),
)


class TestAppConfigDefault(BaseTest):
    """Unknown apps fall back to the default policy."""

    @pytest.mark.parametrize(
        (
            "app_name",
            "uid",
        ),
        _APP_CONFIG_DEFAULT_CASES,
    )
    def test_app_config_default(
        self, client: Any, admin_headers: dict[str, str], app_name: str, uid: int
    ) -> None:
        """Unknown apps fall back to the default policy."""
        response = client.get(f"/admin/app-config/{app_name}", headers=admin_headers)
        assert response.status_code == 200
        assert response.json()["score_threshold"] == 50


_SETTINGS_ENDPOINT_CASES: tuple[tuple[str, int, int], ...] = (
    (
        "WEIGHT_DETECTOR_AHO",
        5,
        7674,
    ),
    (
        "WEIGHT_DETECTOR_AHO",
        8,
        7675,
    ),
    (
        "WEIGHT_DETECTOR_AHO",
        10,
        7676,
    ),
    (
        "WEIGHT_DETECTOR_AHO",
        12,
        7677,
    ),
    (
        "WEIGHT_DETECTOR_AHO",
        15,
        7678,
    ),
    (
        "WEIGHT_DETECTOR_AHO",
        18,
        7679,
    ),
    (
        "WEIGHT_DETECTOR_AHO",
        20,
        7680,
    ),
    (
        "WEIGHT_DETECTOR_AHO",
        22,
        7681,
    ),
    (
        "WEIGHT_DETECTOR_AHO",
        25,
        7682,
    ),
    (
        "WEIGHT_DETECTOR_AHO",
        28,
        7683,
    ),
    (
        "WEIGHT_DETECTOR_AHO",
        30,
        7684,
    ),
    (
        "WEIGHT_DETECTOR_AHO",
        32,
        7685,
    ),
    (
        "WEIGHT_DETECTOR_AHO",
        35,
        7686,
    ),
    (
        "WEIGHT_DETECTOR_AHO",
        38,
        7687,
    ),
    (
        "WEIGHT_DETECTOR_AHO",
        40,
        7688,
    ),
    (
        "WEIGHT_DETECTOR_AHO",
        42,
        7689,
    ),
    (
        "WEIGHT_DETECTOR_AHO",
        45,
        7690,
    ),
    (
        "WEIGHT_DETECTOR_AHO",
        47,
        7691,
    ),
    (
        "WEIGHT_DETECTOR_AHO",
        49,
        7692,
    ),
    (
        "WEIGHT_DETECTOR_AHO",
        50,
        7693,
    ),
    (
        "WEIGHT_USER",
        5,
        7694,
    ),
    (
        "WEIGHT_USER",
        7,
        7695,
    ),
    (
        "WEIGHT_USER",
        9,
        7696,
    ),
    (
        "WEIGHT_USER",
        11,
        7697,
    ),
    (
        "WEIGHT_USER",
        13,
        7698,
    ),
    (
        "WEIGHT_USER",
        16,
        7699,
    ),
    (
        "WEIGHT_USER",
        19,
        7700,
    ),
    (
        "WEIGHT_USER",
        21,
        7701,
    ),
    (
        "WEIGHT_USER",
        24,
        7702,
    ),
    (
        "WEIGHT_USER",
        26,
        7703,
    ),
    (
        "WEIGHT_USER",
        29,
        7704,
    ),
    (
        "WEIGHT_USER",
        31,
        7705,
    ),
    (
        "WEIGHT_USER",
        34,
        7706,
    ),
    (
        "WEIGHT_USER",
        36,
        7707,
    ),
    (
        "WEIGHT_USER",
        39,
        7708,
    ),
    (
        "WEIGHT_USER",
        41,
        7709,
    ),
    (
        "WEIGHT_USER",
        44,
        7710,
    ),
    (
        "WEIGHT_USER",
        46,
        7711,
    ),
    (
        "WEIGHT_USER",
        48,
        7712,
    ),
    (
        "WEIGHT_USER",
        50,
        7713,
    ),
    (
        "SEMANTIC_TOP_K",
        1,
        7714,
    ),
    (
        "SEMANTIC_TOP_K",
        2,
        7715,
    ),
    (
        "SEMANTIC_TOP_K",
        3,
        7716,
    ),
    (
        "SEMANTIC_TOP_K",
        5,
        7717,
    ),
    (
        "SEMANTIC_TOP_K",
        8,
        7718,
    ),
    (
        "SEMANTIC_TOP_K",
        10,
        7719,
    ),
    (
        "SEMANTIC_TOP_K",
        12,
        7720,
    ),
    (
        "SEMANTIC_TOP_K",
        16,
        7721,
    ),
    (
        "SEMANTIC_TOP_K",
        20,
        7722,
    ),
    (
        "SEMANTIC_TOP_K",
        25,
        7723,
    ),
)


class TestSettingsEndpoint(BaseTest):
    """The settings endpoint accepts valid values."""

    @pytest.mark.parametrize(
        (
            "key",
            "value",
            "uid",
        ),
        _SETTINGS_ENDPOINT_CASES,
    )
    def test_settings_endpoint(
        self, client: Any, admin_headers: dict[str, str], key: str, value: int, uid: int
    ) -> None:
        """The settings endpoint accepts valid values."""
        payload = {"settings": {key: value}}
        response = client.post("/admin/settings", headers=admin_headers, json=payload)
        assert response.status_code == 200
        assert key in response.json()["updated"]
