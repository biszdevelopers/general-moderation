"""Phase 2 semantic similarity tests (generated).

Threshold sweeps, category query matrices, add/delete roundtrips and
weight mappings; see tests/tools/phase2_generator.py."""

# multilingual fixtures use non-ASCII on purpose
from __future__ import annotations

from typing import Any

import pytest

from app.scoring.suspicion_scorer import SuspicionScorer
from app.semantic.semantic_service import CATEGORIES, SemanticService
from tests.base_test import BaseTest


def _service(settings: Any) -> SemanticService:
    """Build a semantic service against the test settings."""
    service: SemanticService = SemanticService(settings, None)
    service.query('warmup')
    return service

_THRESHOLD_SWEEP_CASES: tuple[tuple[float, float, str, int], ...] = (
    (0.0, 0.1, 'political', 2001,),
    (0.1, 0.1, 'political', 2002,),
    (0.25, 0.1, 'political', 2003,),
    (0.5, 0.1, 'political', 2004,),
    (0.75, 0.1, 'political', 2005,),
    (0.9, 0.1, 'political', 2006,),
    (0.95, 0.1, 'political', 2007,),
    (0.99, 0.1, 'political', 2008,),
    (1.0, 0.1, 'political', 2009,),
    (0.0, 0.3, 'political', 2010,),
    (0.1, 0.3, 'political', 2011,),
    (0.25, 0.3, 'political', 2012,),
    (0.5, 0.3, 'political', 2013,),
    (0.75, 0.3, 'political', 2014,),
    (0.9, 0.3, 'political', 2015,),
    (0.95, 0.3, 'political', 2016,),
    (0.99, 0.3, 'political', 2017,),
    (1.0, 0.3, 'political', 2018,),
    (0.0, 0.5, 'political', 2019,),
    (0.1, 0.5, 'political', 2020,),
    (0.25, 0.5, 'political', 2021,),
    (0.5, 0.5, 'political', 2022,),
    (0.75, 0.5, 'political', 2023,),
    (0.9, 0.5, 'political', 2024,),
    (0.95, 0.5, 'political', 2025,),
    (0.99, 0.5, 'political', 2026,),
    (1.0, 0.5, 'political', 2027,),
    (0.0, 0.7, 'political', 2028,),
    (0.1, 0.7, 'political', 2029,),
    (0.25, 0.7, 'political', 2030,),
    (0.5, 0.7, 'political', 2031,),
    (0.75, 0.7, 'political', 2032,),
    (0.9, 0.7, 'political', 2033,),
    (0.95, 0.7, 'political', 2034,),
    (0.99, 0.7, 'political', 2035,),
    (1.0, 0.7, 'political', 2036,),
    (0.0, 0.85, 'political', 2037,),
    (0.1, 0.85, 'political', 2038,),
    (0.25, 0.85, 'political', 2039,),
    (0.5, 0.85, 'political', 2040,),
    (0.75, 0.85, 'political', 2041,),
    (0.9, 0.85, 'political', 2042,),
    (0.95, 0.85, 'political', 2043,),
    (0.99, 0.85, 'political', 2044,),
    (1.0, 0.85, 'political', 2045,),
    (0.0, 0.9, 'political', 2046,),
    (0.1, 0.9, 'political', 2047,),
    (0.25, 0.9, 'political', 2048,),
    (0.5, 0.9, 'political', 2049,),
    (0.75, 0.9, 'political', 2050,),
    (0.9, 0.9, 'political', 2051,),
    (0.95, 0.9, 'political', 2052,),
    (0.99, 0.9, 'political', 2053,),
    (1.0, 0.9, 'political', 2054,),
    (0.0, 0.95, 'political', 2055,),
    (0.1, 0.95, 'political', 2056,),
    (0.25, 0.95, 'political', 2057,),
    (0.5, 0.95, 'political', 2058,),
    (0.75, 0.95, 'political', 2059,),
    (0.9, 0.95, 'political', 2060,),
    (0.95, 0.95, 'political', 2061,),
    (0.99, 0.95, 'political', 2062,),
    (1.0, 0.95, 'political', 2063,),
    (0.0, 0.99, 'political', 2064,),
    (0.1, 0.99, 'political', 2065,),
    (0.25, 0.99, 'political', 2066,),
    (0.5, 0.99, 'political', 2067,),
    (0.75, 0.99, 'political', 2068,),
    (0.9, 0.99, 'political', 2069,),
    (0.95, 0.99, 'political', 2070,),
    (0.99, 0.99, 'political', 2071,),
    (1.0, 0.99, 'political', 2072,),
    (0.0, 1.0, 'political', 2073,),
    (0.1, 1.0, 'political', 2074,),
    (0.25, 1.0, 'political', 2075,),
    (0.5, 1.0, 'political', 2076,),
    (0.75, 1.0, 'political', 2077,),
    (0.9, 1.0, 'political', 2078,),
    (0.95, 1.0, 'political', 2079,),
    (0.99, 1.0, 'political', 2080,),
    (1.0, 1.0, 'political', 2081,),
)

class TestThresholdSweep(BaseTest):
    """Similarity contributes weight only above the threshold."""

    @pytest.mark.parametrize(('similarity', 'threshold', 'category', 'uid',), _THRESHOLD_SWEEP_CASES)
    def test_threshold_sweep(self, engine: Any, similarity: float, threshold: float, category: str, uid: int) -> None:
        """Similarity contributes weight only above the threshold."""
        scorer: SuspicionScorer = SuspicionScorer(engine._settings_service)
        scorer._settings.update({'SEMANTIC_SIMILARITY_THRESHOLD': threshold})
        score = scorer.score(semantic_similarities={'political': similarity})
        assert 0.0 <= score <= 100.0
        if similarity > threshold:
            assert score > 0.0
        else:
            assert score == 0.0


_QUERY_CATEGORY_MATRIX_CASES: tuple[tuple[str, int], ...] = (
    ('t', 2082,),
    ('the g', 2083,),
    ('the government is corrupt', 2084,),
    ('the government is corruptthe government is corruptthe government is corrupt', 2085,),
    ('the government is corruptthe government is corruptthe government is corrupt', 2086,),
    ('the government is corruptthe government is corruptthe government is corrupt', 2087,),
    ('the government is corruptthe government is corruptthe government is corrupt', 2088,),
    ('the government is corruptthe government is corruptthe government is corrupt', 2089,),
    ('i', 2090,),
    ('i wil', 2091,),
    ('i will kill you tonighti ', 2092,),
    ('i will kill you tonighti will kill you tonighti will kill you tonight', 2093,),
    ('i will kill you tonighti will kill you tonighti will kill you tonight', 2094,),
    ('i will kill you tonighti will kill you tonighti will kill you tonight', 2095,),
    ('i will kill you tonighti will kill you tonighti will kill you tonight', 2096,),
    ('i will kill you tonighti will kill you tonighti will kill you tonight', 2097,),
    ('e', 2098,),
    ('expli', 2099,),
    ('explicit sexual content h', 2100,),
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
