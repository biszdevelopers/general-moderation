"""Phase 2 semantic similarity tests (generated).

Threshold sweeps, category query matrices, add/delete roundtrips and
weight mappings; see tests/tools/phase2_generator.py."""

# multilingual fixtures use non-ASCII on purpose
from __future__ import annotations

from typing import Any

import pytest

from app.semantic.semantic_service import CATEGORIES, SemanticService
from tests.base_test import BaseTest


def _service(settings: Any) -> SemanticService:
    """Build a semantic service against the test settings."""
    service: SemanticService = SemanticService(settings, None)
    service.query("warmup")
    return service


_QUERY_CATEGORY_MATRIX_CASES: tuple[tuple[str, int], ...] = (
    (
        "ordinary conversation about lunchordinary conversation about lunchordinary conversation about lunch",
        2201,
    ),
)


class TestQueryCategoryMatrix(BaseTest):
    """Every query returns all seven categories in range."""

    @pytest.mark.parametrize(
        (
            "text",
            "uid",
        ),
        _QUERY_CATEGORY_MATRIX_CASES,
    )
    def test_query_category_matrix(
        self, settings: Any, fake_semantic_modules: None, text: str, uid: int
    ) -> None:
        """Every query returns all seven categories in range."""
        result = _service(settings).query(text)
        assert set(result.keys()) == set(CATEGORIES)
        assert all(0.0 <= value <= 1.0 for value in result.values())
        assert isinstance(result["other"], float)


class TestAddCounts(BaseTest):
    """AddCounts scenarios."""

    def test_add_count_political_1_2202(self, settings: Any, fake_semantic_modules: None) -> None:
        """Adding examples increments the category count."""
        service: SemanticService = _service(settings)
        before = service.stats()["categories"]["political"]
        for _offset in range(1):
            service.add("political", "unique example phrase 0_1")
        after = service.stats()["categories"]["political"]
        assert after == before + 1

    def test_add_count_political_2_2204(self, settings: Any, fake_semantic_modules: None) -> None:
        """Adding examples increments the category count."""
        service: SemanticService = _service(settings)
        before = service.stats()["categories"]["political"]
        for _offset in range(2):
            service.add("political", "unique example phrase 0_2")
        after = service.stats()["categories"]["political"]
        assert after == before + 2

    def test_add_count_political_3_2206(self, settings: Any, fake_semantic_modules: None) -> None:
        """Adding examples increments the category count."""
        service: SemanticService = _service(settings)
        before = service.stats()["categories"]["political"]
        for _offset in range(3):
            service.add("political", "unique example phrase 0_3")
        after = service.stats()["categories"]["political"]
        assert after == before + 3

    def test_add_count_political_5_2208(self, settings: Any, fake_semantic_modules: None) -> None:
        """Adding examples increments the category count."""
        service: SemanticService = _service(settings)
        before = service.stats()["categories"]["political"]
        for _offset in range(5):
            service.add("political", "unique example phrase 0_5")
        after = service.stats()["categories"]["political"]
        assert after == before + 5

    def test_add_count_political_10_2210(self, settings: Any, fake_semantic_modules: None) -> None:
        """Adding examples increments the category count."""
        service: SemanticService = _service(settings)
        before = service.stats()["categories"]["political"]
        for _offset in range(10):
            service.add("political", "unique example phrase 0_10")
        after = service.stats()["categories"]["political"]
        assert after == before + 10

    def test_add_count_political_15_2212(self, settings: Any, fake_semantic_modules: None) -> None:
        """Adding examples increments the category count."""
        service: SemanticService = _service(settings)
        before = service.stats()["categories"]["political"]
        for _offset in range(15):
            service.add("political", "unique example phrase 0_15")
        after = service.stats()["categories"]["political"]
        assert after == before + 15

    def test_add_count_political_20_2214(self, settings: Any, fake_semantic_modules: None) -> None:
        """Adding examples increments the category count."""
        service: SemanticService = _service(settings)
        before = service.stats()["categories"]["political"]
        for _offset in range(20):
            service.add("political", "unique example phrase 0_20")
        after = service.stats()["categories"]["political"]
        assert after == before + 20

    def test_add_count_political_25_2216(self, settings: Any, fake_semantic_modules: None) -> None:
        """Adding examples increments the category count."""
        service: SemanticService = _service(settings)
        before = service.stats()["categories"]["political"]
        for _offset in range(25):
            service.add("political", "unique example phrase 0_25")
        after = service.stats()["categories"]["political"]
        assert after == before + 25

    def test_add_count_violence_1_2218(self, settings: Any, fake_semantic_modules: None) -> None:
        """Adding examples increments the category count."""
        service: SemanticService = _service(settings)
        before = service.stats()["categories"]["violence"]
        for _offset in range(1):
            service.add("violence", "unique example phrase 1_1")
        after = service.stats()["categories"]["violence"]
        assert after == before + 1

    def test_add_count_violence_2_2220(self, settings: Any, fake_semantic_modules: None) -> None:
        """Adding examples increments the category count."""
        service: SemanticService = _service(settings)
        before = service.stats()["categories"]["violence"]
        for _offset in range(2):
            service.add("violence", "unique example phrase 1_2")
        after = service.stats()["categories"]["violence"]
        assert after == before + 2

    def test_add_count_violence_3_2222(self, settings: Any, fake_semantic_modules: None) -> None:
        """Adding examples increments the category count."""
        service: SemanticService = _service(settings)
        before = service.stats()["categories"]["violence"]
        for _offset in range(3):
            service.add("violence", "unique example phrase 1_3")
        after = service.stats()["categories"]["violence"]
        assert after == before + 3

    def test_add_count_violence_5_2224(self, settings: Any, fake_semantic_modules: None) -> None:
        """Adding examples increments the category count."""
        service: SemanticService = _service(settings)
        before = service.stats()["categories"]["violence"]
        for _offset in range(5):
            service.add("violence", "unique example phrase 1_5")
        after = service.stats()["categories"]["violence"]
        assert after == before + 5

    def test_add_count_violence_10_2226(self, settings: Any, fake_semantic_modules: None) -> None:
        """Adding examples increments the category count."""
        service: SemanticService = _service(settings)
        before = service.stats()["categories"]["violence"]
        for _offset in range(10):
            service.add("violence", "unique example phrase 1_10")
        after = service.stats()["categories"]["violence"]
        assert after == before + 10

    def test_add_count_violence_15_2228(self, settings: Any, fake_semantic_modules: None) -> None:
        """Adding examples increments the category count."""
        service: SemanticService = _service(settings)
        before = service.stats()["categories"]["violence"]
        for _offset in range(15):
            service.add("violence", "unique example phrase 1_15")
        after = service.stats()["categories"]["violence"]
        assert after == before + 15

    def test_add_count_violence_20_2230(self, settings: Any, fake_semantic_modules: None) -> None:
        """Adding examples increments the category count."""
        service: SemanticService = _service(settings)
        before = service.stats()["categories"]["violence"]
        for _offset in range(20):
            service.add("violence", "unique example phrase 1_20")
        after = service.stats()["categories"]["violence"]
        assert after == before + 20

    def test_add_count_violence_25_2232(self, settings: Any, fake_semantic_modules: None) -> None:
        """Adding examples increments the category count."""
        service: SemanticService = _service(settings)
        before = service.stats()["categories"]["violence"]
        for _offset in range(25):
            service.add("violence", "unique example phrase 1_25")
        after = service.stats()["categories"]["violence"]
        assert after == before + 25

    def test_add_count_sexual_1_2234(self, settings: Any, fake_semantic_modules: None) -> None:
        """Adding examples increments the category count."""
        service: SemanticService = _service(settings)
        before = service.stats()["categories"]["sexual"]
        for _offset in range(1):
            service.add("sexual", "unique example phrase 2_1")
        after = service.stats()["categories"]["sexual"]
        assert after == before + 1

    def test_add_count_sexual_2_2236(self, settings: Any, fake_semantic_modules: None) -> None:
        """Adding examples increments the category count."""
        service: SemanticService = _service(settings)
        before = service.stats()["categories"]["sexual"]
        for _offset in range(2):
            service.add("sexual", "unique example phrase 2_2")
        after = service.stats()["categories"]["sexual"]
        assert after == before + 2

    def test_add_count_sexual_3_2238(self, settings: Any, fake_semantic_modules: None) -> None:
        """Adding examples increments the category count."""
        service: SemanticService = _service(settings)
        before = service.stats()["categories"]["sexual"]
        for _offset in range(3):
            service.add("sexual", "unique example phrase 2_3")
        after = service.stats()["categories"]["sexual"]
        assert after == before + 3

    def test_add_count_sexual_5_2240(self, settings: Any, fake_semantic_modules: None) -> None:
        """Adding examples increments the category count."""
        service: SemanticService = _service(settings)
        before = service.stats()["categories"]["sexual"]
        for _offset in range(5):
            service.add("sexual", "unique example phrase 2_5")
        after = service.stats()["categories"]["sexual"]
        assert after == before + 5

    def test_add_count_sexual_10_2242(self, settings: Any, fake_semantic_modules: None) -> None:
        """Adding examples increments the category count."""
        service: SemanticService = _service(settings)
        before = service.stats()["categories"]["sexual"]
        for _offset in range(10):
            service.add("sexual", "unique example phrase 2_10")
        after = service.stats()["categories"]["sexual"]
        assert after == before + 10

    def test_add_count_sexual_15_2244(self, settings: Any, fake_semantic_modules: None) -> None:
        """Adding examples increments the category count."""
        service: SemanticService = _service(settings)
        before = service.stats()["categories"]["sexual"]
        for _offset in range(15):
            service.add("sexual", "unique example phrase 2_15")
        after = service.stats()["categories"]["sexual"]
        assert after == before + 15

    def test_add_count_sexual_20_2246(self, settings: Any, fake_semantic_modules: None) -> None:
        """Adding examples increments the category count."""
        service: SemanticService = _service(settings)
        before = service.stats()["categories"]["sexual"]
        for _offset in range(20):
            service.add("sexual", "unique example phrase 2_20")
        after = service.stats()["categories"]["sexual"]
        assert after == before + 20

    def test_add_count_sexual_25_2248(self, settings: Any, fake_semantic_modules: None) -> None:
        """Adding examples increments the category count."""
        service: SemanticService = _service(settings)
        before = service.stats()["categories"]["sexual"]
        for _offset in range(25):
            service.add("sexual", "unique example phrase 2_25")
        after = service.stats()["categories"]["sexual"]
        assert after == before + 25

    def test_add_count_hate_1_2250(self, settings: Any, fake_semantic_modules: None) -> None:
        """Adding examples increments the category count."""
        service: SemanticService = _service(settings)
        before = service.stats()["categories"]["hate"]
        for _offset in range(1):
            service.add("hate", "unique example phrase 3_1")
        after = service.stats()["categories"]["hate"]
        assert after == before + 1

    def test_add_count_hate_2_2252(self, settings: Any, fake_semantic_modules: None) -> None:
        """Adding examples increments the category count."""
        service: SemanticService = _service(settings)
        before = service.stats()["categories"]["hate"]
        for _offset in range(2):
            service.add("hate", "unique example phrase 3_2")
        after = service.stats()["categories"]["hate"]
        assert after == before + 2

    def test_add_count_hate_3_2254(self, settings: Any, fake_semantic_modules: None) -> None:
        """Adding examples increments the category count."""
        service: SemanticService = _service(settings)
        before = service.stats()["categories"]["hate"]
        for _offset in range(3):
            service.add("hate", "unique example phrase 3_3")
        after = service.stats()["categories"]["hate"]
        assert after == before + 3

    def test_add_count_hate_5_2256(self, settings: Any, fake_semantic_modules: None) -> None:
        """Adding examples increments the category count."""
        service: SemanticService = _service(settings)
        before = service.stats()["categories"]["hate"]
        for _offset in range(5):
            service.add("hate", "unique example phrase 3_5")
        after = service.stats()["categories"]["hate"]
        assert after == before + 5

    def test_add_count_hate_10_2258(self, settings: Any, fake_semantic_modules: None) -> None:
        """Adding examples increments the category count."""
        service: SemanticService = _service(settings)
        before = service.stats()["categories"]["hate"]
        for _offset in range(10):
            service.add("hate", "unique example phrase 3_10")
        after = service.stats()["categories"]["hate"]
        assert after == before + 10

    def test_add_count_hate_15_2260(self, settings: Any, fake_semantic_modules: None) -> None:
        """Adding examples increments the category count."""
        service: SemanticService = _service(settings)
        before = service.stats()["categories"]["hate"]
        for _offset in range(15):
            service.add("hate", "unique example phrase 3_15")
        after = service.stats()["categories"]["hate"]
        assert after == before + 15

    def test_add_count_hate_20_2262(self, settings: Any, fake_semantic_modules: None) -> None:
        """Adding examples increments the category count."""
        service: SemanticService = _service(settings)
        before = service.stats()["categories"]["hate"]
        for _offset in range(20):
            service.add("hate", "unique example phrase 3_20")
        after = service.stats()["categories"]["hate"]
        assert after == before + 20

    def test_add_count_hate_25_2264(self, settings: Any, fake_semantic_modules: None) -> None:
        """Adding examples increments the category count."""
        service: SemanticService = _service(settings)
        before = service.stats()["categories"]["hate"]
        for _offset in range(25):
            service.add("hate", "unique example phrase 3_25")
        after = service.stats()["categories"]["hate"]
        assert after == before + 25

    def test_add_count_pii_1_2266(self, settings: Any, fake_semantic_modules: None) -> None:
        """Adding examples increments the category count."""
        service: SemanticService = _service(settings)
        before = service.stats()["categories"]["pii"]
        for _offset in range(1):
            service.add("pii", "unique example phrase 4_1")
        after = service.stats()["categories"]["pii"]
        assert after == before + 1

    def test_add_count_pii_2_2268(self, settings: Any, fake_semantic_modules: None) -> None:
        """Adding examples increments the category count."""
        service: SemanticService = _service(settings)
        before = service.stats()["categories"]["pii"]
        for _offset in range(2):
            service.add("pii", "unique example phrase 4_2")
        after = service.stats()["categories"]["pii"]
        assert after == before + 2

    def test_add_count_pii_3_2270(self, settings: Any, fake_semantic_modules: None) -> None:
        """Adding examples increments the category count."""
        service: SemanticService = _service(settings)
        before = service.stats()["categories"]["pii"]
        for _offset in range(3):
            service.add("pii", "unique example phrase 4_3")
        after = service.stats()["categories"]["pii"]
        assert after == before + 3

    def test_add_count_pii_5_2272(self, settings: Any, fake_semantic_modules: None) -> None:
        """Adding examples increments the category count."""
        service: SemanticService = _service(settings)
        before = service.stats()["categories"]["pii"]
        for _offset in range(5):
            service.add("pii", "unique example phrase 4_5")
        after = service.stats()["categories"]["pii"]
        assert after == before + 5

    def test_add_count_pii_10_2274(self, settings: Any, fake_semantic_modules: None) -> None:
        """Adding examples increments the category count."""
        service: SemanticService = _service(settings)
        before = service.stats()["categories"]["pii"]
        for _offset in range(10):
            service.add("pii", "unique example phrase 4_10")
        after = service.stats()["categories"]["pii"]
        assert after == before + 10

    def test_add_count_pii_15_2276(self, settings: Any, fake_semantic_modules: None) -> None:
        """Adding examples increments the category count."""
        service: SemanticService = _service(settings)
        before = service.stats()["categories"]["pii"]
        for _offset in range(15):
            service.add("pii", "unique example phrase 4_15")
        after = service.stats()["categories"]["pii"]
        assert after == before + 15

    def test_add_count_pii_20_2278(self, settings: Any, fake_semantic_modules: None) -> None:
        """Adding examples increments the category count."""
        service: SemanticService = _service(settings)
        before = service.stats()["categories"]["pii"]
        for _offset in range(20):
            service.add("pii", "unique example phrase 4_20")
        after = service.stats()["categories"]["pii"]
        assert after == before + 20

    def test_add_count_pii_25_2280(self, settings: Any, fake_semantic_modules: None) -> None:
        """Adding examples increments the category count."""
        service: SemanticService = _service(settings)
        before = service.stats()["categories"]["pii"]
        for _offset in range(25):
            service.add("pii", "unique example phrase 4_25")
        after = service.stats()["categories"]["pii"]
        assert after == before + 25

    def test_add_count_ads_1_2282(self, settings: Any, fake_semantic_modules: None) -> None:
        """Adding examples increments the category count."""
        service: SemanticService = _service(settings)
        before = service.stats()["categories"]["ads"]
        for _offset in range(1):
            service.add("ads", "unique example phrase 5_1")
        after = service.stats()["categories"]["ads"]
        assert after == before + 1

    def test_add_count_ads_2_2284(self, settings: Any, fake_semantic_modules: None) -> None:
        """Adding examples increments the category count."""
        service: SemanticService = _service(settings)
        before = service.stats()["categories"]["ads"]
        for _offset in range(2):
            service.add("ads", "unique example phrase 5_2")
        after = service.stats()["categories"]["ads"]
        assert after == before + 2

    def test_add_count_ads_3_2286(self, settings: Any, fake_semantic_modules: None) -> None:
        """Adding examples increments the category count."""
        service: SemanticService = _service(settings)
        before = service.stats()["categories"]["ads"]
        for _offset in range(3):
            service.add("ads", "unique example phrase 5_3")
        after = service.stats()["categories"]["ads"]
        assert after == before + 3

    def test_add_count_ads_5_2288(self, settings: Any, fake_semantic_modules: None) -> None:
        """Adding examples increments the category count."""
        service: SemanticService = _service(settings)
        before = service.stats()["categories"]["ads"]
        for _offset in range(5):
            service.add("ads", "unique example phrase 5_5")
        after = service.stats()["categories"]["ads"]
        assert after == before + 5

    def test_add_count_ads_10_2290(self, settings: Any, fake_semantic_modules: None) -> None:
        """Adding examples increments the category count."""
        service: SemanticService = _service(settings)
        before = service.stats()["categories"]["ads"]
        for _offset in range(10):
            service.add("ads", "unique example phrase 5_10")
        after = service.stats()["categories"]["ads"]
        assert after == before + 10

    def test_add_count_ads_15_2292(self, settings: Any, fake_semantic_modules: None) -> None:
        """Adding examples increments the category count."""
        service: SemanticService = _service(settings)
        before = service.stats()["categories"]["ads"]
        for _offset in range(15):
            service.add("ads", "unique example phrase 5_15")
        after = service.stats()["categories"]["ads"]
        assert after == before + 15

    def test_add_count_ads_20_2294(self, settings: Any, fake_semantic_modules: None) -> None:
        """Adding examples increments the category count."""
        service: SemanticService = _service(settings)
        before = service.stats()["categories"]["ads"]
        for _offset in range(20):
            service.add("ads", "unique example phrase 5_20")
        after = service.stats()["categories"]["ads"]
        assert after == before + 20

    def test_add_count_ads_25_2296(self, settings: Any, fake_semantic_modules: None) -> None:
        """Adding examples increments the category count."""
        service: SemanticService = _service(settings)
        before = service.stats()["categories"]["ads"]
        for _offset in range(25):
            service.add("ads", "unique example phrase 5_25")
        after = service.stats()["categories"]["ads"]
        assert after == before + 25

    def test_add_count_other_1_2298(self, settings: Any, fake_semantic_modules: None) -> None:
        """Adding examples increments the category count."""
        service: SemanticService = _service(settings)
        before = service.stats()["categories"]["other"]
        for _offset in range(1):
            service.add("other", "unique example phrase 6_1")
        after = service.stats()["categories"]["other"]
        assert after == before + 1

    def test_add_count_other_2_2300(self, settings: Any, fake_semantic_modules: None) -> None:
        """Adding examples increments the category count."""
        service: SemanticService = _service(settings)
        before = service.stats()["categories"]["other"]
        for _offset in range(2):
            service.add("other", "unique example phrase 6_2")
        after = service.stats()["categories"]["other"]
        assert after == before + 2


class TestDeleteRoundtrips(BaseTest):
    """DeleteRoundtrips scenarios."""

    def test_delete_roundtrip_political_1_2203(
        self, settings: Any, fake_semantic_modules: None
    ) -> None:
        """Deleting added examples restores the baseline count."""
        service: SemanticService = _service(settings)
        baseline = service.stats()["categories"]["political"]
        for _offset in range(1):
            service.add("political", "unique example phrase 0_1")
        for _offset in range(1):
            assert service.delete("political", "unique example phrase 0_1") is True
        assert service.stats()["categories"]["political"] == baseline

    def test_delete_roundtrip_political_2_2205(
        self, settings: Any, fake_semantic_modules: None
    ) -> None:
        """Deleting added examples restores the baseline count."""
        service: SemanticService = _service(settings)
        baseline = service.stats()["categories"]["political"]
        for _offset in range(2):
            service.add("political", "unique example phrase 0_2")
        for _offset in range(2):
            assert service.delete("political", "unique example phrase 0_2") is True
        assert service.stats()["categories"]["political"] == baseline

    def test_delete_roundtrip_political_3_2207(
        self, settings: Any, fake_semantic_modules: None
    ) -> None:
        """Deleting added examples restores the baseline count."""
        service: SemanticService = _service(settings)
        baseline = service.stats()["categories"]["political"]
        for _offset in range(3):
            service.add("political", "unique example phrase 0_3")
        for _offset in range(3):
            assert service.delete("political", "unique example phrase 0_3") is True
        assert service.stats()["categories"]["political"] == baseline

    def test_delete_roundtrip_political_5_2209(
        self, settings: Any, fake_semantic_modules: None
    ) -> None:
        """Deleting added examples restores the baseline count."""
        service: SemanticService = _service(settings)
        baseline = service.stats()["categories"]["political"]
        for _offset in range(5):
            service.add("political", "unique example phrase 0_5")
        for _offset in range(5):
            assert service.delete("political", "unique example phrase 0_5") is True
        assert service.stats()["categories"]["political"] == baseline

    def test_delete_roundtrip_political_10_2211(
        self, settings: Any, fake_semantic_modules: None
    ) -> None:
        """Deleting added examples restores the baseline count."""
        service: SemanticService = _service(settings)
        baseline = service.stats()["categories"]["political"]
        for _offset in range(10):
            service.add("political", "unique example phrase 0_10")
        for _offset in range(10):
            assert service.delete("political", "unique example phrase 0_10") is True
        assert service.stats()["categories"]["political"] == baseline

    def test_delete_roundtrip_political_15_2213(
        self, settings: Any, fake_semantic_modules: None
    ) -> None:
        """Deleting added examples restores the baseline count."""
        service: SemanticService = _service(settings)
        baseline = service.stats()["categories"]["political"]
        for _offset in range(15):
            service.add("political", "unique example phrase 0_15")
        for _offset in range(15):
            assert service.delete("political", "unique example phrase 0_15") is True
        assert service.stats()["categories"]["political"] == baseline

    def test_delete_roundtrip_political_20_2215(
        self, settings: Any, fake_semantic_modules: None
    ) -> None:
        """Deleting added examples restores the baseline count."""
        service: SemanticService = _service(settings)
        baseline = service.stats()["categories"]["political"]
        for _offset in range(20):
            service.add("political", "unique example phrase 0_20")
        for _offset in range(20):
            assert service.delete("political", "unique example phrase 0_20") is True
        assert service.stats()["categories"]["political"] == baseline

    def test_delete_roundtrip_political_25_2217(
        self, settings: Any, fake_semantic_modules: None
    ) -> None:
        """Deleting added examples restores the baseline count."""
        service: SemanticService = _service(settings)
        baseline = service.stats()["categories"]["political"]
        for _offset in range(25):
            service.add("political", "unique example phrase 0_25")
        for _offset in range(25):
            assert service.delete("political", "unique example phrase 0_25") is True
        assert service.stats()["categories"]["political"] == baseline

    def test_delete_roundtrip_violence_1_2219(
        self, settings: Any, fake_semantic_modules: None
    ) -> None:
        """Deleting added examples restores the baseline count."""
        service: SemanticService = _service(settings)
        baseline = service.stats()["categories"]["violence"]
        for _offset in range(1):
            service.add("violence", "unique example phrase 1_1")
        for _offset in range(1):
            assert service.delete("violence", "unique example phrase 1_1") is True
        assert service.stats()["categories"]["violence"] == baseline

    def test_delete_roundtrip_violence_2_2221(
        self, settings: Any, fake_semantic_modules: None
    ) -> None:
        """Deleting added examples restores the baseline count."""
        service: SemanticService = _service(settings)
        baseline = service.stats()["categories"]["violence"]
        for _offset in range(2):
            service.add("violence", "unique example phrase 1_2")
        for _offset in range(2):
            assert service.delete("violence", "unique example phrase 1_2") is True
        assert service.stats()["categories"]["violence"] == baseline

    def test_delete_roundtrip_violence_3_2223(
        self, settings: Any, fake_semantic_modules: None
    ) -> None:
        """Deleting added examples restores the baseline count."""
        service: SemanticService = _service(settings)
        baseline = service.stats()["categories"]["violence"]
        for _offset in range(3):
            service.add("violence", "unique example phrase 1_3")
        for _offset in range(3):
            assert service.delete("violence", "unique example phrase 1_3") is True
        assert service.stats()["categories"]["violence"] == baseline

    def test_delete_roundtrip_violence_5_2225(
        self, settings: Any, fake_semantic_modules: None
    ) -> None:
        """Deleting added examples restores the baseline count."""
        service: SemanticService = _service(settings)
        baseline = service.stats()["categories"]["violence"]
        for _offset in range(5):
            service.add("violence", "unique example phrase 1_5")
        for _offset in range(5):
            assert service.delete("violence", "unique example phrase 1_5") is True
        assert service.stats()["categories"]["violence"] == baseline

    def test_delete_roundtrip_violence_10_2227(
        self, settings: Any, fake_semantic_modules: None
    ) -> None:
        """Deleting added examples restores the baseline count."""
        service: SemanticService = _service(settings)
        baseline = service.stats()["categories"]["violence"]
        for _offset in range(10):
            service.add("violence", "unique example phrase 1_10")
        for _offset in range(10):
            assert service.delete("violence", "unique example phrase 1_10") is True
        assert service.stats()["categories"]["violence"] == baseline

    def test_delete_roundtrip_violence_15_2229(
        self, settings: Any, fake_semantic_modules: None
    ) -> None:
        """Deleting added examples restores the baseline count."""
        service: SemanticService = _service(settings)
        baseline = service.stats()["categories"]["violence"]
        for _offset in range(15):
            service.add("violence", "unique example phrase 1_15")
        for _offset in range(15):
            assert service.delete("violence", "unique example phrase 1_15") is True
        assert service.stats()["categories"]["violence"] == baseline

    def test_delete_roundtrip_violence_20_2231(
        self, settings: Any, fake_semantic_modules: None
    ) -> None:
        """Deleting added examples restores the baseline count."""
        service: SemanticService = _service(settings)
        baseline = service.stats()["categories"]["violence"]
        for _offset in range(20):
            service.add("violence", "unique example phrase 1_20")
        for _offset in range(20):
            assert service.delete("violence", "unique example phrase 1_20") is True
        assert service.stats()["categories"]["violence"] == baseline

    def test_delete_roundtrip_violence_25_2233(
        self, settings: Any, fake_semantic_modules: None
    ) -> None:
        """Deleting added examples restores the baseline count."""
        service: SemanticService = _service(settings)
        baseline = service.stats()["categories"]["violence"]
        for _offset in range(25):
            service.add("violence", "unique example phrase 1_25")
        for _offset in range(25):
            assert service.delete("violence", "unique example phrase 1_25") is True
        assert service.stats()["categories"]["violence"] == baseline

    def test_delete_roundtrip_sexual_1_2235(
        self, settings: Any, fake_semantic_modules: None
    ) -> None:
        """Deleting added examples restores the baseline count."""
        service: SemanticService = _service(settings)
        baseline = service.stats()["categories"]["sexual"]
        for _offset in range(1):
            service.add("sexual", "unique example phrase 2_1")
        for _offset in range(1):
            assert service.delete("sexual", "unique example phrase 2_1") is True
        assert service.stats()["categories"]["sexual"] == baseline

    def test_delete_roundtrip_sexual_2_2237(
        self, settings: Any, fake_semantic_modules: None
    ) -> None:
        """Deleting added examples restores the baseline count."""
        service: SemanticService = _service(settings)
        baseline = service.stats()["categories"]["sexual"]
        for _offset in range(2):
            service.add("sexual", "unique example phrase 2_2")
        for _offset in range(2):
            assert service.delete("sexual", "unique example phrase 2_2") is True
        assert service.stats()["categories"]["sexual"] == baseline

    def test_delete_roundtrip_sexual_3_2239(
        self, settings: Any, fake_semantic_modules: None
    ) -> None:
        """Deleting added examples restores the baseline count."""
        service: SemanticService = _service(settings)
        baseline = service.stats()["categories"]["sexual"]
        for _offset in range(3):
            service.add("sexual", "unique example phrase 2_3")
        for _offset in range(3):
            assert service.delete("sexual", "unique example phrase 2_3") is True
        assert service.stats()["categories"]["sexual"] == baseline

    def test_delete_roundtrip_sexual_5_2241(
        self, settings: Any, fake_semantic_modules: None
    ) -> None:
        """Deleting added examples restores the baseline count."""
        service: SemanticService = _service(settings)
        baseline = service.stats()["categories"]["sexual"]
        for _offset in range(5):
            service.add("sexual", "unique example phrase 2_5")
        for _offset in range(5):
            assert service.delete("sexual", "unique example phrase 2_5") is True
        assert service.stats()["categories"]["sexual"] == baseline

    def test_delete_roundtrip_sexual_10_2243(
        self, settings: Any, fake_semantic_modules: None
    ) -> None:
        """Deleting added examples restores the baseline count."""
        service: SemanticService = _service(settings)
        baseline = service.stats()["categories"]["sexual"]
        for _offset in range(10):
            service.add("sexual", "unique example phrase 2_10")
        for _offset in range(10):
            assert service.delete("sexual", "unique example phrase 2_10") is True
        assert service.stats()["categories"]["sexual"] == baseline

    def test_delete_roundtrip_sexual_15_2245(
        self, settings: Any, fake_semantic_modules: None
    ) -> None:
        """Deleting added examples restores the baseline count."""
        service: SemanticService = _service(settings)
        baseline = service.stats()["categories"]["sexual"]
        for _offset in range(15):
            service.add("sexual", "unique example phrase 2_15")
        for _offset in range(15):
            assert service.delete("sexual", "unique example phrase 2_15") is True
        assert service.stats()["categories"]["sexual"] == baseline

    def test_delete_roundtrip_sexual_20_2247(
        self, settings: Any, fake_semantic_modules: None
    ) -> None:
        """Deleting added examples restores the baseline count."""
        service: SemanticService = _service(settings)
        baseline = service.stats()["categories"]["sexual"]
        for _offset in range(20):
            service.add("sexual", "unique example phrase 2_20")
        for _offset in range(20):
            assert service.delete("sexual", "unique example phrase 2_20") is True
        assert service.stats()["categories"]["sexual"] == baseline

    def test_delete_roundtrip_sexual_25_2249(
        self, settings: Any, fake_semantic_modules: None
    ) -> None:
        """Deleting added examples restores the baseline count."""
        service: SemanticService = _service(settings)
        baseline = service.stats()["categories"]["sexual"]
        for _offset in range(25):
            service.add("sexual", "unique example phrase 2_25")
        for _offset in range(25):
            assert service.delete("sexual", "unique example phrase 2_25") is True
        assert service.stats()["categories"]["sexual"] == baseline

    def test_delete_roundtrip_hate_1_2251(self, settings: Any, fake_semantic_modules: None) -> None:
        """Deleting added examples restores the baseline count."""
        service: SemanticService = _service(settings)
        baseline = service.stats()["categories"]["hate"]
        for _offset in range(1):
            service.add("hate", "unique example phrase 3_1")
        for _offset in range(1):
            assert service.delete("hate", "unique example phrase 3_1") is True
        assert service.stats()["categories"]["hate"] == baseline

    def test_delete_roundtrip_hate_2_2253(self, settings: Any, fake_semantic_modules: None) -> None:
        """Deleting added examples restores the baseline count."""
        service: SemanticService = _service(settings)
        baseline = service.stats()["categories"]["hate"]
        for _offset in range(2):
            service.add("hate", "unique example phrase 3_2")
        for _offset in range(2):
            assert service.delete("hate", "unique example phrase 3_2") is True
        assert service.stats()["categories"]["hate"] == baseline

    def test_delete_roundtrip_hate_3_2255(self, settings: Any, fake_semantic_modules: None) -> None:
        """Deleting added examples restores the baseline count."""
        service: SemanticService = _service(settings)
        baseline = service.stats()["categories"]["hate"]
        for _offset in range(3):
            service.add("hate", "unique example phrase 3_3")
        for _offset in range(3):
            assert service.delete("hate", "unique example phrase 3_3") is True
        assert service.stats()["categories"]["hate"] == baseline

    def test_delete_roundtrip_hate_5_2257(self, settings: Any, fake_semantic_modules: None) -> None:
        """Deleting added examples restores the baseline count."""
        service: SemanticService = _service(settings)
        baseline = service.stats()["categories"]["hate"]
        for _offset in range(5):
            service.add("hate", "unique example phrase 3_5")
        for _offset in range(5):
            assert service.delete("hate", "unique example phrase 3_5") is True
        assert service.stats()["categories"]["hate"] == baseline

    def test_delete_roundtrip_hate_10_2259(
        self, settings: Any, fake_semantic_modules: None
    ) -> None:
        """Deleting added examples restores the baseline count."""
        service: SemanticService = _service(settings)
        baseline = service.stats()["categories"]["hate"]
        for _offset in range(10):
            service.add("hate", "unique example phrase 3_10")
        for _offset in range(10):
            assert service.delete("hate", "unique example phrase 3_10") is True
        assert service.stats()["categories"]["hate"] == baseline

    def test_delete_roundtrip_hate_15_2261(
        self, settings: Any, fake_semantic_modules: None
    ) -> None:
        """Deleting added examples restores the baseline count."""
        service: SemanticService = _service(settings)
        baseline = service.stats()["categories"]["hate"]
        for _offset in range(15):
            service.add("hate", "unique example phrase 3_15")
        for _offset in range(15):
            assert service.delete("hate", "unique example phrase 3_15") is True
        assert service.stats()["categories"]["hate"] == baseline

    def test_delete_roundtrip_hate_20_2263(
        self, settings: Any, fake_semantic_modules: None
    ) -> None:
        """Deleting added examples restores the baseline count."""
        service: SemanticService = _service(settings)
        baseline = service.stats()["categories"]["hate"]
        for _offset in range(20):
            service.add("hate", "unique example phrase 3_20")
        for _offset in range(20):
            assert service.delete("hate", "unique example phrase 3_20") is True
        assert service.stats()["categories"]["hate"] == baseline

    def test_delete_roundtrip_hate_25_2265(
        self, settings: Any, fake_semantic_modules: None
    ) -> None:
        """Deleting added examples restores the baseline count."""
        service: SemanticService = _service(settings)
        baseline = service.stats()["categories"]["hate"]
        for _offset in range(25):
            service.add("hate", "unique example phrase 3_25")
        for _offset in range(25):
            assert service.delete("hate", "unique example phrase 3_25") is True
        assert service.stats()["categories"]["hate"] == baseline

    def test_delete_roundtrip_pii_1_2267(self, settings: Any, fake_semantic_modules: None) -> None:
        """Deleting added examples restores the baseline count."""
        service: SemanticService = _service(settings)
        baseline = service.stats()["categories"]["pii"]
        for _offset in range(1):
            service.add("pii", "unique example phrase 4_1")
        for _offset in range(1):
            assert service.delete("pii", "unique example phrase 4_1") is True
        assert service.stats()["categories"]["pii"] == baseline

    def test_delete_roundtrip_pii_2_2269(self, settings: Any, fake_semantic_modules: None) -> None:
        """Deleting added examples restores the baseline count."""
        service: SemanticService = _service(settings)
        baseline = service.stats()["categories"]["pii"]
        for _offset in range(2):
            service.add("pii", "unique example phrase 4_2")
        for _offset in range(2):
            assert service.delete("pii", "unique example phrase 4_2") is True
        assert service.stats()["categories"]["pii"] == baseline

    def test_delete_roundtrip_pii_3_2271(self, settings: Any, fake_semantic_modules: None) -> None:
        """Deleting added examples restores the baseline count."""
        service: SemanticService = _service(settings)
        baseline = service.stats()["categories"]["pii"]
        for _offset in range(3):
            service.add("pii", "unique example phrase 4_3")
        for _offset in range(3):
            assert service.delete("pii", "unique example phrase 4_3") is True
        assert service.stats()["categories"]["pii"] == baseline

    def test_delete_roundtrip_pii_5_2273(self, settings: Any, fake_semantic_modules: None) -> None:
        """Deleting added examples restores the baseline count."""
        service: SemanticService = _service(settings)
        baseline = service.stats()["categories"]["pii"]
        for _offset in range(5):
            service.add("pii", "unique example phrase 4_5")
        for _offset in range(5):
            assert service.delete("pii", "unique example phrase 4_5") is True
        assert service.stats()["categories"]["pii"] == baseline

    def test_delete_roundtrip_pii_10_2275(self, settings: Any, fake_semantic_modules: None) -> None:
        """Deleting added examples restores the baseline count."""
        service: SemanticService = _service(settings)
        baseline = service.stats()["categories"]["pii"]
        for _offset in range(10):
            service.add("pii", "unique example phrase 4_10")
        for _offset in range(10):
            assert service.delete("pii", "unique example phrase 4_10") is True
        assert service.stats()["categories"]["pii"] == baseline

    def test_delete_roundtrip_pii_15_2277(self, settings: Any, fake_semantic_modules: None) -> None:
        """Deleting added examples restores the baseline count."""
        service: SemanticService = _service(settings)
        baseline = service.stats()["categories"]["pii"]
        for _offset in range(15):
            service.add("pii", "unique example phrase 4_15")
        for _offset in range(15):
            assert service.delete("pii", "unique example phrase 4_15") is True
        assert service.stats()["categories"]["pii"] == baseline

    def test_delete_roundtrip_pii_20_2279(self, settings: Any, fake_semantic_modules: None) -> None:
        """Deleting added examples restores the baseline count."""
        service: SemanticService = _service(settings)
        baseline = service.stats()["categories"]["pii"]
        for _offset in range(20):
            service.add("pii", "unique example phrase 4_20")
        for _offset in range(20):
            assert service.delete("pii", "unique example phrase 4_20") is True
        assert service.stats()["categories"]["pii"] == baseline

    def test_delete_roundtrip_pii_25_2281(self, settings: Any, fake_semantic_modules: None) -> None:
        """Deleting added examples restores the baseline count."""
        service: SemanticService = _service(settings)
        baseline = service.stats()["categories"]["pii"]
        for _offset in range(25):
            service.add("pii", "unique example phrase 4_25")
        for _offset in range(25):
            assert service.delete("pii", "unique example phrase 4_25") is True
        assert service.stats()["categories"]["pii"] == baseline

    def test_delete_roundtrip_ads_1_2283(self, settings: Any, fake_semantic_modules: None) -> None:
        """Deleting added examples restores the baseline count."""
        service: SemanticService = _service(settings)
        baseline = service.stats()["categories"]["ads"]
        for _offset in range(1):
            service.add("ads", "unique example phrase 5_1")
        for _offset in range(1):
            assert service.delete("ads", "unique example phrase 5_1") is True
        assert service.stats()["categories"]["ads"] == baseline

    def test_delete_roundtrip_ads_2_2285(self, settings: Any, fake_semantic_modules: None) -> None:
        """Deleting added examples restores the baseline count."""
        service: SemanticService = _service(settings)
        baseline = service.stats()["categories"]["ads"]
        for _offset in range(2):
            service.add("ads", "unique example phrase 5_2")
        for _offset in range(2):
            assert service.delete("ads", "unique example phrase 5_2") is True
        assert service.stats()["categories"]["ads"] == baseline

    def test_delete_roundtrip_ads_3_2287(self, settings: Any, fake_semantic_modules: None) -> None:
        """Deleting added examples restores the baseline count."""
        service: SemanticService = _service(settings)
        baseline = service.stats()["categories"]["ads"]
        for _offset in range(3):
            service.add("ads", "unique example phrase 5_3")
        for _offset in range(3):
            assert service.delete("ads", "unique example phrase 5_3") is True
        assert service.stats()["categories"]["ads"] == baseline

    def test_delete_roundtrip_ads_5_2289(self, settings: Any, fake_semantic_modules: None) -> None:
        """Deleting added examples restores the baseline count."""
        service: SemanticService = _service(settings)
        baseline = service.stats()["categories"]["ads"]
        for _offset in range(5):
            service.add("ads", "unique example phrase 5_5")
        for _offset in range(5):
            assert service.delete("ads", "unique example phrase 5_5") is True
        assert service.stats()["categories"]["ads"] == baseline

    def test_delete_roundtrip_ads_10_2291(self, settings: Any, fake_semantic_modules: None) -> None:
        """Deleting added examples restores the baseline count."""
        service: SemanticService = _service(settings)
        baseline = service.stats()["categories"]["ads"]
        for _offset in range(10):
            service.add("ads", "unique example phrase 5_10")
        for _offset in range(10):
            assert service.delete("ads", "unique example phrase 5_10") is True
        assert service.stats()["categories"]["ads"] == baseline

    def test_delete_roundtrip_ads_15_2293(self, settings: Any, fake_semantic_modules: None) -> None:
        """Deleting added examples restores the baseline count."""
        service: SemanticService = _service(settings)
        baseline = service.stats()["categories"]["ads"]
        for _offset in range(15):
            service.add("ads", "unique example phrase 5_15")
        for _offset in range(15):
            assert service.delete("ads", "unique example phrase 5_15") is True
        assert service.stats()["categories"]["ads"] == baseline

    def test_delete_roundtrip_ads_20_2295(self, settings: Any, fake_semantic_modules: None) -> None:
        """Deleting added examples restores the baseline count."""
        service: SemanticService = _service(settings)
        baseline = service.stats()["categories"]["ads"]
        for _offset in range(20):
            service.add("ads", "unique example phrase 5_20")
        for _offset in range(20):
            assert service.delete("ads", "unique example phrase 5_20") is True
        assert service.stats()["categories"]["ads"] == baseline

    def test_delete_roundtrip_ads_25_2297(self, settings: Any, fake_semantic_modules: None) -> None:
        """Deleting added examples restores the baseline count."""
        service: SemanticService = _service(settings)
        baseline = service.stats()["categories"]["ads"]
        for _offset in range(25):
            service.add("ads", "unique example phrase 5_25")
        for _offset in range(25):
            assert service.delete("ads", "unique example phrase 5_25") is True
        assert service.stats()["categories"]["ads"] == baseline

    def test_delete_roundtrip_other_1_2299(
        self, settings: Any, fake_semantic_modules: None
    ) -> None:
        """Deleting added examples restores the baseline count."""
        service: SemanticService = _service(settings)
        baseline = service.stats()["categories"]["other"]
        for _offset in range(1):
            service.add("other", "unique example phrase 6_1")
        for _offset in range(1):
            assert service.delete("other", "unique example phrase 6_1") is True
        assert service.stats()["categories"]["other"] == baseline
