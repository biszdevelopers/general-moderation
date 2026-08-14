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
    ('explicit sexual content hereexplicit sexual content hereexplicit sexual content here', 2101,),
    ('explicit sexual content hereexplicit sexual content hereexplicit sexual content here', 2102,),
    ('explicit sexual content hereexplicit sexual content hereexplicit sexual content here', 2103,),
    ('explicit sexual content hereexplicit sexual content hereexplicit sexual content here', 2104,),
    ('explicit sexual content hereexplicit sexual content hereexplicit sexual content here', 2105,),
    ('i', 2106,),
    ('i hat', 2107,),
    ('i hate all immigrantsi ha', 2108,),
    ('i hate all immigrantsi hate all immigrantsi hate all immigrants', 2109,),
    ('i hate all immigrantsi hate all immigrantsi hate all immigrants', 2110,),
    ('i hate all immigrantsi hate all immigrantsi hate all immigrants', 2111,),
    ('i hate all immigrantsi hate all immigrantsi hate all immigrants', 2112,),
    ('i hate all immigrantsi hate all immigrantsi hate all immigrants', 2113,),
    ('y', 2114,),
    ('your ', 2115,),
    ('your social security numb', 2116,),
    ('your social security number is 123your social security number is 123your social security number is 1', 2117,),
    ('your social security number is 123your social security number is 123your social security number is 123', 2118,),
    ('your social security number is 123your social security number is 123your social security number is 123', 2119,),
    ('your social security number is 123your social security number is 123your social security number is 123', 2120,),
    ('your social security number is 123your social security number is 123your social security number is 123', 2121,),
    ('b', 2122,),
    ('buy t', 2123,),
    ('buy this product nowbuy t', 2124,),
    ('buy this product nowbuy this product nowbuy this product now', 2125,),
    ('buy this product nowbuy this product nowbuy this product now', 2126,),
    ('buy this product nowbuy this product nowbuy this product now', 2127,),
    ('buy this product nowbuy this product nowbuy this product now', 2128,),
    ('buy this product nowbuy this product nowbuy this product now', 2129,),
    ('t', 2130,),
    ('the w', 2131,),
    ('the weather is pleasantth', 2132,),
    ('the weather is pleasantthe weather is pleasantthe weather is pleasant', 2133,),
    ('the weather is pleasantthe weather is pleasantthe weather is pleasant', 2134,),
    ('the weather is pleasantthe weather is pleasantthe weather is pleasant', 2135,),
    ('the weather is pleasantthe weather is pleasantthe weather is pleasant', 2136,),
    ('the weather is pleasantthe weather is pleasantthe weather is pleasant', 2137,),
    ('p', 2138,),
    ('polit', 2139,),
    ('politicians take bribespo', 2140,),
    ('politicians take bribespoliticians take bribespoliticians take bribes', 2141,),
    ('politicians take bribespoliticians take bribespoliticians take bribes', 2142,),
    ('politicians take bribespoliticians take bribespoliticians take bribes', 2143,),
    ('politicians take bribespoliticians take bribespoliticians take bribes', 2144,),
    ('politicians take bribespoliticians take bribespoliticians take bribes', 2145,),
    ('h', 2146,),
    ('he pu', 2147,),
    ('he punched his brotherhe ', 2148,),
    ('he punched his brotherhe punched his brotherhe punched his brother', 2149,),
    ('he punched his brotherhe punched his brotherhe punched his brother', 2150,),
    ('he punched his brotherhe punched his brotherhe punched his brother', 2151,),
    ('he punched his brotherhe punched his brotherhe punched his brother', 2152,),
    ('he punched his brotherhe punched his brotherhe punched his brother', 2153,),
    ('s', 2154,),
    ('she m', 2155,),
    ('she mailed the parcelshe ', 2156,),
    ('she mailed the parcelshe mailed the parcelshe mailed the parcel', 2157,),
    ('she mailed the parcelshe mailed the parcelshe mailed the parcel', 2158,),
    ('she mailed the parcelshe mailed the parcelshe mailed the parcel', 2159,),
    ('she mailed the parcelshe mailed the parcelshe mailed the parcel', 2160,),
    ('she mailed the parcelshe mailed the parcelshe mailed the parcel', 2161,),
    ('w', 2162,),
    ('watch', 2163,),
    ('watch the news tonightwat', 2164,),
    ('watch the news tonightwatch the news tonightwatch the news tonight', 2165,),
    ('watch the news tonightwatch the news tonightwatch the news tonight', 2166,),
    ('watch the news tonightwatch the news tonightwatch the news tonight', 2167,),
    ('watch the news tonightwatch the news tonightwatch the news tonight', 2168,),
    ('watch the news tonightwatch the news tonightwatch the news tonight', 2169,),
    ('t', 2170,),
    ('the p', 2171,),
    ('the price dropped todayth', 2172,),
    ('the price dropped todaythe price dropped todaythe price dropped today', 2173,),
    ('the price dropped todaythe price dropped todaythe price dropped today', 2174,),
    ('the price dropped todaythe price dropped todaythe price dropped today', 2175,),
    ('the price dropped todaythe price dropped todaythe price dropped today', 2176,),
    ('the price dropped todaythe price dropped todaythe price dropped today', 2177,),
    ('s', 2178,),
    ('secre', 2179,),
    ('secret password exposedse', 2180,),
    ('secret password exposedsecret password exposedsecret password exposed', 2181,),
    ('secret password exposedsecret password exposedsecret password exposed', 2182,),
    ('secret password exposedsecret password exposedsecret password exposed', 2183,),
    ('secret password exposedsecret password exposedsecret password exposed', 2184,),
    ('secret password exposedsecret password exposedsecret password exposed', 2185,),
    ('j', 2186,),
    ('join ', 2187,),
    ('join our mailing listjoin', 2188,),
    ('join our mailing listjoin our mailing listjoin our mailing list', 2189,),
    ('join our mailing listjoin our mailing listjoin our mailing list', 2190,),
    ('join our mailing listjoin our mailing listjoin our mailing list', 2191,),
    ('join our mailing listjoin our mailing listjoin our mailing list', 2192,),
    ('join our mailing listjoin our mailing listjoin our mailing list', 2193,),
    ('o', 2194,),
    ('ordin', 2195,),
    ('ordinary conversation abo', 2196,),
    ('ordinary conversation about lunchordinary conversation about lunchordinary conversation about lunch', 2197,),
    ('ordinary conversation about lunchordinary conversation about lunchordinary conversation about lunch', 2198,),
    ('ordinary conversation about lunchordinary conversation about lunchordinary conversation about lunch', 2199,),
    ('ordinary conversation about lunchordinary conversation about lunchordinary conversation about lunch', 2200,),
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
