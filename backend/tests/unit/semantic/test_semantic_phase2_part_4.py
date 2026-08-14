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
    service.query('warmup')
    return service

_QUERY_CATEGORY_MATRIX_CASES: tuple[tuple[str, int], ...] = (
    ('ordinary conversation about lunchordinary conversation about lunchordinary conversation about lunch', 2201,),
)

class TestQueryCategoryMatrix(BaseTest):
    """Every query returns all seven categories in range."""

    @pytest.mark.parametrize(('text', 'uid',), _QUERY_CATEGORY_MATRIX_CASES)
    def test_query_category_matrix(self, settings: Any, fake_semantic_modules: None, text: str, uid: int) -> None:
        """Every query returns all seven categories in range."""
        result = _service(settings).query(text)
        assert set(result.keys()) == set(CATEGORIES)
        assert all(0.0 <= value <= 1.0 for value in result.values())
        assert isinstance(result['other'], float)


_ADD_COUNT_CASES: tuple[tuple[str, int, int], ...] = (
    ('political', 1, 2202,),
    ('political', 2, 2204,),
    ('political', 3, 2206,),
    ('political', 5, 2208,),
    ('political', 10, 2210,),
    ('political', 15, 2212,),
    ('political', 20, 2214,),
    ('political', 25, 2216,),
    ('violence', 1, 2218,),
    ('violence', 2, 2220,),
    ('violence', 3, 2222,),
    ('violence', 5, 2224,),
    ('violence', 10, 2226,),
    ('violence', 15, 2228,),
    ('violence', 20, 2230,),
    ('violence', 25, 2232,),
    ('sexual', 1, 2234,),
    ('sexual', 2, 2236,),
    ('sexual', 3, 2238,),
    ('sexual', 5, 2240,),
    ('sexual', 10, 2242,),
    ('sexual', 15, 2244,),
    ('sexual', 20, 2246,),
    ('sexual', 25, 2248,),
    ('hate', 1, 2250,),
    ('hate', 2, 2252,),
    ('hate', 3, 2254,),
    ('hate', 5, 2256,),
    ('hate', 10, 2258,),
    ('hate', 15, 2260,),
    ('hate', 20, 2262,),
    ('hate', 25, 2264,),
    ('pii', 1, 2266,),
    ('pii', 2, 2268,),
    ('pii', 3, 2270,),
    ('pii', 5, 2272,),
    ('pii', 10, 2274,),
    ('pii', 15, 2276,),
    ('pii', 20, 2278,),
    ('pii', 25, 2280,),
    ('ads', 1, 2282,),
    ('ads', 2, 2284,),
    ('ads', 3, 2286,),
    ('ads', 5, 2288,),
    ('ads', 10, 2290,),
    ('ads', 15, 2292,),
    ('ads', 20, 2294,),
    ('ads', 25, 2296,),
    ('other', 1, 2298,),
    ('other', 2, 2300,),
)

class TestAddCount(BaseTest):
    """Adding examples increments the category count."""

    @pytest.mark.parametrize(('category', 'count', 'uid',), _ADD_COUNT_CASES)
    def test_add_count(self, settings: Any, fake_semantic_modules: None, category: str, count: int, uid: int) -> None:
        """Adding examples increments the category count."""
        service: SemanticService = _service(settings)
        before = service.stats()['categories'][category]
        example = f'unique example phrase {category}_{count}'
        for _offset in range(count):
            service.add(category, example)
        after = service.stats()['categories'][category]
        assert after == before + count


_DELETE_ROUNDTRIP_CASES: tuple[tuple[str, int, int], ...] = (
    ('political', 1, 2203,),
    ('political', 2, 2205,),
    ('political', 3, 2207,),
    ('political', 5, 2209,),
    ('political', 10, 2211,),
    ('political', 15, 2213,),
    ('political', 20, 2215,),
    ('political', 25, 2217,),
    ('violence', 1, 2219,),
    ('violence', 2, 2221,),
    ('violence', 3, 2223,),
    ('violence', 5, 2225,),
    ('violence', 10, 2227,),
    ('violence', 15, 2229,),
    ('violence', 20, 2231,),
    ('violence', 25, 2233,),
    ('sexual', 1, 2235,),
    ('sexual', 2, 2237,),
    ('sexual', 3, 2239,),
    ('sexual', 5, 2241,),
    ('sexual', 10, 2243,),
    ('sexual', 15, 2245,),
    ('sexual', 20, 2247,),
    ('sexual', 25, 2249,),
    ('hate', 1, 2251,),
    ('hate', 2, 2253,),
    ('hate', 3, 2255,),
    ('hate', 5, 2257,),
    ('hate', 10, 2259,),
    ('hate', 15, 2261,),
    ('hate', 20, 2263,),
    ('hate', 25, 2265,),
    ('pii', 1, 2267,),
    ('pii', 2, 2269,),
    ('pii', 3, 2271,),
    ('pii', 5, 2273,),
    ('pii', 10, 2275,),
    ('pii', 15, 2277,),
    ('pii', 20, 2279,),
    ('pii', 25, 2281,),
    ('ads', 1, 2283,),
    ('ads', 2, 2285,),
    ('ads', 3, 2287,),
    ('ads', 5, 2289,),
    ('ads', 10, 2291,),
    ('ads', 15, 2293,),
    ('ads', 20, 2295,),
    ('ads', 25, 2297,),
    ('other', 1, 2299,),
)

class TestDeleteRoundtrip(BaseTest):
    """Deleting added examples restores the baseline count."""

    @pytest.mark.parametrize(('category', 'count', 'uid',), _DELETE_ROUNDTRIP_CASES)
    def test_delete_roundtrip(self, settings: Any, fake_semantic_modules: None, category: str, count: int, uid: int) -> None:
        """Deleting added examples restores the baseline count."""
        service: SemanticService = _service(settings)
        baseline = service.stats()['categories'][category]
        example = f'unique example phrase {category}_{count}'
        for _offset in range(count):
            service.add(category, example)
        for _offset in range(count):
            assert service.delete(category, example) is True
        assert service.stats()['categories'][category] == baseline
