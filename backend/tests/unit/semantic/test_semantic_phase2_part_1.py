"""Phase 2 semantic similarity tests (generated).

Threshold sweeps, category query matrices, add/delete roundtrips and
weight mappings; see tests/tools/phase2_generator.py."""

# multilingual fixtures use non-ASCII on purpose
from __future__ import annotations

from typing import Any

import pytest

from app.semantic.semantic_service import SemanticService
from tests.base_test import BaseTest


def _service(settings: Any) -> SemanticService:
    """Build a semantic service against the test settings."""
    service: SemanticService = SemanticService(settings, None)
    service.query('warmup')
    return service

_UNAVAILABLE_CASES: tuple[tuple[int, int], ...] = (
    (1, 1901,),
    (2, 1902,),
    (3, 1903,),
    (4, 1904,),
    (5, 1905,),
    (6, 1906,),
    (7, 1907,),
    (8, 1908,),
    (9, 1909,),
    (10, 1910,),
    (11, 1911,),
    (12, 1912,),
    (13, 1913,),
    (14, 1914,),
    (15, 1915,),
    (16, 1916,),
    (17, 1917,),
    (18, 1918,),
    (19, 1919,),
    (20, 1920,),
    (21, 1921,),
    (22, 1922,),
    (23, 1923,),
    (24, 1924,),
    (25, 1925,),
    (26, 1926,),
    (27, 1927,),
    (28, 1928,),
    (29, 1929,),
    (30, 1930,),
    (31, 1931,),
    (32, 1932,),
    (33, 1933,),
    (34, 1934,),
    (35, 1935,),
    (36, 1936,),
    (37, 1937,),
    (38, 1938,),
    (39, 1939,),
    (40, 1940,),
    (41, 1941,),
    (42, 1942,),
    (43, 1943,),
    (44, 1944,),
    (45, 1945,),
    (46, 1946,),
    (47, 1947,),
    (48, 1948,),
    (49, 1949,),
    (50, 1950,),
    (51, 1951,),
    (52, 1952,),
    (53, 1953,),
    (54, 1954,),
    (55, 1955,),
    (56, 1956,),
    (57, 1957,),
    (58, 1958,),
    (59, 1959,),
    (60, 1960,),
    (61, 1961,),
    (62, 1962,),
    (63, 1963,),
    (64, 1964,),
    (65, 1965,),
    (66, 1966,),
    (67, 1967,),
    (68, 1968,),
    (69, 1969,),
    (70, 1970,),
    (71, 1971,),
    (72, 1972,),
    (73, 1973,),
    (74, 1974,),
    (75, 1975,),
    (76, 1976,),
    (77, 1977,),
    (78, 1978,),
    (79, 1979,),
    (80, 1980,),
    (81, 1981,),
    (82, 1982,),
    (83, 1983,),
    (84, 1984,),
    (85, 1985,),
    (86, 1986,),
    (87, 1987,),
    (88, 1988,),
    (89, 1989,),
    (90, 1990,),
    (91, 1991,),
    (92, 1992,),
    (93, 1993,),
    (94, 1994,),
    (95, 1995,),
    (96, 1996,),
    (97, 1997,),
    (98, 1998,),
    (99, 1999,),
    (100, 2000,),
)

class TestUnavailable(BaseTest):
    """Without the heavy dependencies the service reports unavailable."""

    @pytest.mark.parametrize(('top_k', 'uid',), _UNAVAILABLE_CASES)
    def test_unavailable(self, settings: Any, top_k: int, uid: int) -> None:
        """Without the heavy dependencies the service reports unavailable."""
        settings.semantic_top_k = top_k
        service: SemanticService = SemanticService(settings, None)
        assert service.is_available() is False
        assert service.query('anything') == {}
        stats = service.stats()
        assert stats['available'] is False
