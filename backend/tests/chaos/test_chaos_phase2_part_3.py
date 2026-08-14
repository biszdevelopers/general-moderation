"""Phase 2 chaos and resilience tests (generated).

Hash storms, malformed databases, package adapter failures, engine
recovery and API bursts."""

# multilingual fixtures use non-ASCII on purpose
from __future__ import annotations

import pytest

from tests.base_test import BaseTest

_ADAPTER_FAILURE_CASES: tuple[tuple[str, str, int], ...] = (
    ('profanite', 'harmless text profanite 0', 9661,),
    ('profanite', 'harmless text profanite 1', 9662,),
    ('profanite', 'harmless text profanite 2', 9663,),
    ('profanite', 'harmless text profanite 3', 9664,),
    ('profanite', 'harmless text profanite 4', 9665,),
    ('profanite', 'harmless text profanite 5', 9666,),
    ('profanite', 'harmless text profanite 6', 9667,),
    ('profanite', 'harmless text profanite 7', 9668,),
    ('profanite', 'harmless text profanite 8', 9669,),
    ('profanite', 'harmless text profanite 9', 9670,),
    ('profanite', 'harmless text profanite 10', 9671,),
    ('profanite', 'harmless text profanite 11', 9672,),
    ('profanite', 'harmless text profanite 12', 9673,),
    ('badwords_py', 'harmless text badwords_py 0', 9674,),
    ('badwords_py', 'harmless text badwords_py 1', 9675,),
    ('badwords_py', 'harmless text badwords_py 2', 9676,),
    ('badwords_py', 'harmless text badwords_py 3', 9677,),
    ('badwords_py', 'harmless text badwords_py 4', 9678,),
    ('badwords_py', 'harmless text badwords_py 5', 9679,),
    ('badwords_py', 'harmless text badwords_py 6', 9680,),
    ('badwords_py', 'harmless text badwords_py 7', 9681,),
    ('badwords_py', 'harmless text badwords_py 8', 9682,),
    ('badwords_py', 'harmless text badwords_py 9', 9683,),
    ('badwords_py', 'harmless text badwords_py 10', 9684,),
    ('badwords_py', 'harmless text badwords_py 11', 9685,),
    ('badwords_py', 'harmless text badwords_py 12', 9686,),
    ('glin_profanity', 'harmless text glin_profanity 0', 9687,),
    ('glin_profanity', 'harmless text glin_profanity 1', 9688,),
    ('glin_profanity', 'harmless text glin_profanity 2', 9689,),
    ('glin_profanity', 'harmless text glin_profanity 3', 9690,),
    ('glin_profanity', 'harmless text glin_profanity 4', 9691,),
    ('glin_profanity', 'harmless text glin_profanity 5', 9692,),
    ('glin_profanity', 'harmless text glin_profanity 6', 9693,),
    ('glin_profanity', 'harmless text glin_profanity 7', 9694,),
    ('glin_profanity', 'harmless text glin_profanity 8', 9695,),
    ('glin_profanity', 'harmless text glin_profanity 9', 9696,),
    ('glin_profanity', 'harmless text glin_profanity 10', 9697,),
    ('glin_profanity', 'harmless text glin_profanity 11', 9698,),
    ('glin_profanity', 'harmless text glin_profanity 12', 9699,),
    ('gangajal', 'harmless text gangajal 0', 9700,),
    ('gangajal', 'harmless text gangajal 1', 9701,),
    ('gangajal', 'harmless text gangajal 2', 9702,),
    ('gangajal', 'harmless text gangajal 3', 9703,),
    ('gangajal', 'harmless text gangajal 4', 9704,),
    ('gangajal', 'harmless text gangajal 5', 9705,),
    ('gangajal', 'harmless text gangajal 6', 9706,),
    ('gangajal', 'harmless text gangajal 7', 9707,),
    ('gangajal', 'harmless text gangajal 8', 9708,),
    ('gangajal', 'harmless text gangajal 9', 9709,),
    ('gangajal', 'harmless text gangajal 10', 9710,),
    ('gangajal', 'harmless text gangajal 11', 9711,),
    ('gangajal', 'harmless text gangajal 12', 9712,),
    ('safetext', 'harmless text safetext 0', 9713,),
    ('safetext', 'harmless text safetext 1', 9714,),
    ('safetext', 'harmless text safetext 2', 9715,),
    ('safetext', 'harmless text safetext 3', 9716,),
    ('safetext', 'harmless text safetext 4', 9717,),
    ('safetext', 'harmless text safetext 5', 9718,),
    ('safetext', 'harmless text safetext 6', 9719,),
    ('safetext', 'harmless text safetext 7', 9720,),
    ('safetext', 'harmless text safetext 8', 9721,),
    ('safetext', 'harmless text safetext 9', 9722,),
    ('safetext', 'harmless text safetext 10', 9723,),
    ('safetext', 'harmless text safetext 11', 9724,),
    ('safetext', 'harmless text safetext 12', 9725,),
    ('pyprofane', 'harmless text pyprofane 0', 9726,),
    ('pyprofane', 'harmless text pyprofane 1', 9727,),
    ('pyprofane', 'harmless text pyprofane 2', 9728,),
    ('pyprofane', 'harmless text pyprofane 3', 9729,),
    ('pyprofane', 'harmless text pyprofane 4', 9730,),
    ('pyprofane', 'harmless text pyprofane 5', 9731,),
    ('pyprofane', 'harmless text pyprofane 6', 9732,),
    ('pyprofane', 'harmless text pyprofane 7', 9733,),
    ('pyprofane', 'harmless text pyprofane 8', 9734,),
    ('pyprofane', 'harmless text pyprofane 9', 9735,),
    ('pyprofane', 'harmless text pyprofane 10', 9736,),
    ('pyprofane', 'harmless text pyprofane 11', 9737,),
    ('pyprofane', 'harmless text pyprofane 12', 9738,),
    ('sensitive_word_filter_cn', 'harmless text sensitive_word_filter_cn 0', 9739,),
    ('sensitive_word_filter_cn', 'harmless text sensitive_word_filter_cn 1', 9740,),
    ('sensitive_word_filter_cn', 'harmless text sensitive_word_filter_cn 2', 9741,),
    ('sensitive_word_filter_cn', 'harmless text sensitive_word_filter_cn 3', 9742,),
    ('sensitive_word_filter_cn', 'harmless text sensitive_word_filter_cn 4', 9743,),
    ('sensitive_word_filter_cn', 'harmless text sensitive_word_filter_cn 5', 9744,),
    ('sensitive_word_filter_cn', 'harmless text sensitive_word_filter_cn 6', 9745,),
    ('sensitive_word_filter_cn', 'harmless text sensitive_word_filter_cn 7', 9746,),
    ('sensitive_word_filter_cn', 'harmless text sensitive_word_filter_cn 8', 9747,),
    ('sensitive_word_filter_cn', 'harmless text sensitive_word_filter_cn 9', 9748,),
    ('sensitive_word_filter_cn', 'harmless text sensitive_word_filter_cn 10', 9749,),
    ('sensitive_word_filter_cn', 'harmless text sensitive_word_filter_cn 11', 9750,),
    ('sensitive_word_filter_cn', 'harmless text sensitive_word_filter_cn 12', 9751,),
    ('profanity_filter', 'harmless text profanity_filter 0', 9752,),
    ('profanity_filter', 'harmless text profanity_filter 1', 9753,),
    ('profanity_filter', 'harmless text profanity_filter 2', 9754,),
    ('profanity_filter', 'harmless text profanity_filter 3', 9755,),
    ('profanity_filter', 'harmless text profanity_filter 4', 9756,),
    ('profanity_filter', 'harmless text profanity_filter 5', 9757,),
    ('profanity_filter', 'harmless text profanity_filter 6', 9758,),
    ('profanity_filter', 'harmless text profanity_filter 7', 9759,),
    ('profanity_filter', 'harmless text profanity_filter 8', 9760,),
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
