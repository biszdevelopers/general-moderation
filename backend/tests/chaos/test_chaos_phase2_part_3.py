"""Phase 2 chaos and resilience tests (generated).

Hash storms, malformed databases, package adapter failures, engine
recovery and API bursts."""

# multilingual fixtures use non-ASCII on purpose
from __future__ import annotations

import pytest

from tests.base_test import BaseTest

_ADAPTER_FAILURE_CASES: tuple[tuple[str, str, int], ...] = (
    ('profanite', 'harmless text profanite 0', 9502,),
    ('profanite', 'harmless text profanite 1', 9503,),
    ('profanite', 'harmless text profanite 2', 9504,),
    ('profanite', 'harmless text profanite 3', 9505,),
    ('profanite', 'harmless text profanite 4', 9506,),
    ('profanite', 'harmless text profanite 5', 9507,),
    ('profanite', 'harmless text profanite 6', 9508,),
    ('profanite', 'harmless text profanite 7', 9509,),
    ('profanite', 'harmless text profanite 8', 9510,),
    ('profanite', 'harmless text profanite 9', 9511,),
    ('profanite', 'harmless text profanite 10', 9512,),
    ('profanite', 'harmless text profanite 11', 9513,),
    ('profanite', 'harmless text profanite 12', 9514,),
    ('badwords_py', 'harmless text badwords_py 0', 9515,),
    ('badwords_py', 'harmless text badwords_py 1', 9516,),
    ('badwords_py', 'harmless text badwords_py 2', 9517,),
    ('badwords_py', 'harmless text badwords_py 3', 9518,),
    ('badwords_py', 'harmless text badwords_py 4', 9519,),
    ('badwords_py', 'harmless text badwords_py 5', 9520,),
    ('badwords_py', 'harmless text badwords_py 6', 9521,),
    ('badwords_py', 'harmless text badwords_py 7', 9522,),
    ('badwords_py', 'harmless text badwords_py 8', 9523,),
    ('badwords_py', 'harmless text badwords_py 9', 9524,),
    ('badwords_py', 'harmless text badwords_py 10', 9525,),
    ('badwords_py', 'harmless text badwords_py 11', 9526,),
    ('badwords_py', 'harmless text badwords_py 12', 9527,),
    ('glin_profanity', 'harmless text glin_profanity 0', 9528,),
    ('glin_profanity', 'harmless text glin_profanity 1', 9529,),
    ('glin_profanity', 'harmless text glin_profanity 2', 9530,),
    ('glin_profanity', 'harmless text glin_profanity 3', 9531,),
    ('glin_profanity', 'harmless text glin_profanity 4', 9532,),
    ('glin_profanity', 'harmless text glin_profanity 5', 9533,),
    ('glin_profanity', 'harmless text glin_profanity 6', 9534,),
    ('glin_profanity', 'harmless text glin_profanity 7', 9535,),
    ('glin_profanity', 'harmless text glin_profanity 8', 9536,),
    ('glin_profanity', 'harmless text glin_profanity 9', 9537,),
    ('glin_profanity', 'harmless text glin_profanity 10', 9538,),
    ('glin_profanity', 'harmless text glin_profanity 11', 9539,),
    ('glin_profanity', 'harmless text glin_profanity 12', 9540,),
    ('gangajal', 'harmless text gangajal 0', 9541,),
    ('gangajal', 'harmless text gangajal 1', 9542,),
    ('gangajal', 'harmless text gangajal 2', 9543,),
    ('gangajal', 'harmless text gangajal 3', 9544,),
    ('gangajal', 'harmless text gangajal 4', 9545,),
    ('gangajal', 'harmless text gangajal 5', 9546,),
    ('gangajal', 'harmless text gangajal 6', 9547,),
    ('gangajal', 'harmless text gangajal 7', 9548,),
    ('gangajal', 'harmless text gangajal 8', 9549,),
    ('gangajal', 'harmless text gangajal 9', 9550,),
    ('gangajal', 'harmless text gangajal 10', 9551,),
    ('gangajal', 'harmless text gangajal 11', 9552,),
    ('gangajal', 'harmless text gangajal 12', 9553,),
    ('safetext', 'harmless text safetext 0', 9554,),
    ('safetext', 'harmless text safetext 1', 9555,),
    ('safetext', 'harmless text safetext 2', 9556,),
    ('safetext', 'harmless text safetext 3', 9557,),
    ('safetext', 'harmless text safetext 4', 9558,),
    ('safetext', 'harmless text safetext 5', 9559,),
    ('safetext', 'harmless text safetext 6', 9560,),
    ('safetext', 'harmless text safetext 7', 9561,),
    ('safetext', 'harmless text safetext 8', 9562,),
    ('safetext', 'harmless text safetext 9', 9563,),
    ('safetext', 'harmless text safetext 10', 9564,),
    ('safetext', 'harmless text safetext 11', 9565,),
    ('safetext', 'harmless text safetext 12', 9566,),
    ('pyprofane', 'harmless text pyprofane 0', 9567,),
    ('pyprofane', 'harmless text pyprofane 1', 9568,),
    ('pyprofane', 'harmless text pyprofane 2', 9569,),
    ('pyprofane', 'harmless text pyprofane 3', 9570,),
    ('pyprofane', 'harmless text pyprofane 4', 9571,),
    ('pyprofane', 'harmless text pyprofane 5', 9572,),
    ('pyprofane', 'harmless text pyprofane 6', 9573,),
    ('pyprofane', 'harmless text pyprofane 7', 9574,),
    ('pyprofane', 'harmless text pyprofane 8', 9575,),
    ('pyprofane', 'harmless text pyprofane 9', 9576,),
    ('pyprofane', 'harmless text pyprofane 10', 9577,),
    ('pyprofane', 'harmless text pyprofane 11', 9578,),
    ('pyprofane', 'harmless text pyprofane 12', 9579,),
    ('sensitive_word_filter_cn', 'harmless text sensitive_word_filter_cn 0', 9580,),
    ('sensitive_word_filter_cn', 'harmless text sensitive_word_filter_cn 1', 9581,),
    ('sensitive_word_filter_cn', 'harmless text sensitive_word_filter_cn 2', 9582,),
    ('sensitive_word_filter_cn', 'harmless text sensitive_word_filter_cn 3', 9583,),
    ('sensitive_word_filter_cn', 'harmless text sensitive_word_filter_cn 4', 9584,),
    ('sensitive_word_filter_cn', 'harmless text sensitive_word_filter_cn 5', 9585,),
    ('sensitive_word_filter_cn', 'harmless text sensitive_word_filter_cn 6', 9586,),
    ('sensitive_word_filter_cn', 'harmless text sensitive_word_filter_cn 7', 9587,),
    ('sensitive_word_filter_cn', 'harmless text sensitive_word_filter_cn 8', 9588,),
    ('sensitive_word_filter_cn', 'harmless text sensitive_word_filter_cn 9', 9589,),
    ('sensitive_word_filter_cn', 'harmless text sensitive_word_filter_cn 10', 9590,),
    ('sensitive_word_filter_cn', 'harmless text sensitive_word_filter_cn 11', 9591,),
    ('sensitive_word_filter_cn', 'harmless text sensitive_word_filter_cn 12', 9592,),
    ('profanity_filter', 'harmless text profanity_filter 0', 9593,),
    ('profanity_filter', 'harmless text profanity_filter 1', 9594,),
    ('profanity_filter', 'harmless text profanity_filter 2', 9595,),
    ('profanity_filter', 'harmless text profanity_filter 3', 9596,),
    ('profanity_filter', 'harmless text profanity_filter 4', 9597,),
    ('profanity_filter', 'harmless text profanity_filter 5', 9598,),
    ('profanity_filter', 'harmless text profanity_filter 6', 9599,),
    ('profanity_filter', 'harmless text profanity_filter 7', 9600,),
    ('profanity_filter', 'harmless text profanity_filter 8', 9601,),
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
