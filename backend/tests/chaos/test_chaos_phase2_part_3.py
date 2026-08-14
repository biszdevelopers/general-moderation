"""Phase 2 chaos and resilience tests (generated).

Hash storms, malformed databases, package adapter failures, engine
recovery and API bursts."""

# multilingual fixtures use non-ASCII on purpose
from __future__ import annotations

import pytest

from tests.base_test import BaseTest

_ADAPTER_FAILURE_CASES: tuple[tuple[str, str, int], ...] = (
    ('profanite', 'harmless text profanite 0', 9701,),
    ('profanite', 'harmless text profanite 1', 9702,),
    ('profanite', 'harmless text profanite 2', 9703,),
    ('profanite', 'harmless text profanite 3', 9704,),
    ('profanite', 'harmless text profanite 4', 9705,),
    ('profanite', 'harmless text profanite 5', 9706,),
    ('profanite', 'harmless text profanite 6', 9707,),
    ('profanite', 'harmless text profanite 7', 9708,),
    ('profanite', 'harmless text profanite 8', 9709,),
    ('profanite', 'harmless text profanite 9', 9710,),
    ('profanite', 'harmless text profanite 10', 9711,),
    ('profanite', 'harmless text profanite 11', 9712,),
    ('profanite', 'harmless text profanite 12', 9713,),
    ('badwords_py', 'harmless text badwords_py 0', 9714,),
    ('badwords_py', 'harmless text badwords_py 1', 9715,),
    ('badwords_py', 'harmless text badwords_py 2', 9716,),
    ('badwords_py', 'harmless text badwords_py 3', 9717,),
    ('badwords_py', 'harmless text badwords_py 4', 9718,),
    ('badwords_py', 'harmless text badwords_py 5', 9719,),
    ('badwords_py', 'harmless text badwords_py 6', 9720,),
    ('badwords_py', 'harmless text badwords_py 7', 9721,),
    ('badwords_py', 'harmless text badwords_py 8', 9722,),
    ('badwords_py', 'harmless text badwords_py 9', 9723,),
    ('badwords_py', 'harmless text badwords_py 10', 9724,),
    ('badwords_py', 'harmless text badwords_py 11', 9725,),
    ('badwords_py', 'harmless text badwords_py 12', 9726,),
    ('glin_profanity', 'harmless text glin_profanity 0', 9727,),
    ('glin_profanity', 'harmless text glin_profanity 1', 9728,),
    ('glin_profanity', 'harmless text glin_profanity 2', 9729,),
    ('glin_profanity', 'harmless text glin_profanity 3', 9730,),
    ('glin_profanity', 'harmless text glin_profanity 4', 9731,),
    ('glin_profanity', 'harmless text glin_profanity 5', 9732,),
    ('glin_profanity', 'harmless text glin_profanity 6', 9733,),
    ('glin_profanity', 'harmless text glin_profanity 7', 9734,),
    ('glin_profanity', 'harmless text glin_profanity 8', 9735,),
    ('glin_profanity', 'harmless text glin_profanity 9', 9736,),
    ('glin_profanity', 'harmless text glin_profanity 10', 9737,),
    ('glin_profanity', 'harmless text glin_profanity 11', 9738,),
    ('glin_profanity', 'harmless text glin_profanity 12', 9739,),
    ('gangajal', 'harmless text gangajal 0', 9740,),
    ('gangajal', 'harmless text gangajal 1', 9741,),
    ('gangajal', 'harmless text gangajal 2', 9742,),
    ('gangajal', 'harmless text gangajal 3', 9743,),
    ('gangajal', 'harmless text gangajal 4', 9744,),
    ('gangajal', 'harmless text gangajal 5', 9745,),
    ('gangajal', 'harmless text gangajal 6', 9746,),
    ('gangajal', 'harmless text gangajal 7', 9747,),
    ('gangajal', 'harmless text gangajal 8', 9748,),
    ('gangajal', 'harmless text gangajal 9', 9749,),
    ('gangajal', 'harmless text gangajal 10', 9750,),
    ('gangajal', 'harmless text gangajal 11', 9751,),
    ('gangajal', 'harmless text gangajal 12', 9752,),
    ('safetext', 'harmless text safetext 0', 9753,),
    ('safetext', 'harmless text safetext 1', 9754,),
    ('safetext', 'harmless text safetext 2', 9755,),
    ('safetext', 'harmless text safetext 3', 9756,),
    ('safetext', 'harmless text safetext 4', 9757,),
    ('safetext', 'harmless text safetext 5', 9758,),
    ('safetext', 'harmless text safetext 6', 9759,),
    ('safetext', 'harmless text safetext 7', 9760,),
    ('safetext', 'harmless text safetext 8', 9761,),
    ('safetext', 'harmless text safetext 9', 9762,),
    ('safetext', 'harmless text safetext 10', 9763,),
    ('safetext', 'harmless text safetext 11', 9764,),
    ('safetext', 'harmless text safetext 12', 9765,),
    ('pyprofane', 'harmless text pyprofane 0', 9766,),
    ('pyprofane', 'harmless text pyprofane 1', 9767,),
    ('pyprofane', 'harmless text pyprofane 2', 9768,),
    ('pyprofane', 'harmless text pyprofane 3', 9769,),
    ('pyprofane', 'harmless text pyprofane 4', 9770,),
    ('pyprofane', 'harmless text pyprofane 5', 9771,),
    ('pyprofane', 'harmless text pyprofane 6', 9772,),
    ('pyprofane', 'harmless text pyprofane 7', 9773,),
    ('pyprofane', 'harmless text pyprofane 8', 9774,),
    ('pyprofane', 'harmless text pyprofane 9', 9775,),
    ('pyprofane', 'harmless text pyprofane 10', 9776,),
    ('pyprofane', 'harmless text pyprofane 11', 9777,),
    ('pyprofane', 'harmless text pyprofane 12', 9778,),
    ('sensitive_word_filter_cn', 'harmless text sensitive_word_filter_cn 0', 9779,),
    ('sensitive_word_filter_cn', 'harmless text sensitive_word_filter_cn 1', 9780,),
    ('sensitive_word_filter_cn', 'harmless text sensitive_word_filter_cn 2', 9781,),
    ('sensitive_word_filter_cn', 'harmless text sensitive_word_filter_cn 3', 9782,),
    ('sensitive_word_filter_cn', 'harmless text sensitive_word_filter_cn 4', 9783,),
    ('sensitive_word_filter_cn', 'harmless text sensitive_word_filter_cn 5', 9784,),
    ('sensitive_word_filter_cn', 'harmless text sensitive_word_filter_cn 6', 9785,),
    ('sensitive_word_filter_cn', 'harmless text sensitive_word_filter_cn 7', 9786,),
    ('sensitive_word_filter_cn', 'harmless text sensitive_word_filter_cn 8', 9787,),
    ('sensitive_word_filter_cn', 'harmless text sensitive_word_filter_cn 9', 9788,),
    ('sensitive_word_filter_cn', 'harmless text sensitive_word_filter_cn 10', 9789,),
    ('sensitive_word_filter_cn', 'harmless text sensitive_word_filter_cn 11', 9790,),
    ('sensitive_word_filter_cn', 'harmless text sensitive_word_filter_cn 12', 9791,),
    ('profanity_filter', 'harmless text profanity_filter 0', 9792,),
    ('profanity_filter', 'harmless text profanity_filter 1', 9793,),
    ('profanity_filter', 'harmless text profanity_filter 2', 9794,),
    ('profanity_filter', 'harmless text profanity_filter 3', 9795,),
    ('profanity_filter', 'harmless text profanity_filter 4', 9796,),
    ('profanity_filter', 'harmless text profanity_filter 5', 9797,),
    ('profanity_filter', 'harmless text profanity_filter 6', 9798,),
    ('profanity_filter', 'harmless text profanity_filter 7', 9799,),
    ('profanity_filter', 'harmless text profanity_filter 8', 9800,),
)

class TestAdapterFailure(BaseTest):
    """Broken package adapters degrade to a non-match."""

    @pytest.mark.parametrize(('package', 'text', 'uid',), _ADAPTER_FAILURE_CASES)
    def test_adapter_failure(self, monkeypatch: pytest.MonkeyPatch, package: str, text: str, uid: int) -> None:
        """Broken package adapters degrade to a non-match."""
        import importlib

        from app.detectors.multi_language_detector import _PackageAdapter
        real_import = importlib.import_module
        def _broken_import(name, *args, **kwargs):
            if name == package:
                raise ImportError('simulated missing package')
            return real_import(name, *args, **kwargs)
        monkeypatch.setattr(importlib, 'import_module', _broken_import)
        adapter: _PackageAdapter = _PackageAdapter(package, 'any', 'truthy')
        assert adapter.available is False
        assert adapter.detect(text).matched is False
