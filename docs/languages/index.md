# Language Coverage

The service detects vulgar and politically sensitive content across 20+
languages. Coverage comes from the union of the verified C/C++/Rust/
WebAssembly packages plus custom words.

## Package Matrix

Only packages that install cleanly and run on the supported platforms are
registered in the detector.

| Package | Core tech | Scope |
| :--- | :--- | :--- |
| `profanite` | Rust | Universal |
| `glin-profanity` | C | 25+ languages |
| `gangajal` | WebAssembly | All languages |
| `PyProfane` | C | Universal |

Removed from the pipeline because they do not exist on PyPI, carry broken
dependencies, or are not functional on Python 3.14: `badwords-py`,
`safetext`, `profanity-filter2`, `sensitive-word-filter-cn`,
`sensitive-word-filter`, `scheckbl`, and `valx`.

## Per-Language Pages

- [English](/languages/en)
- [Simplified Chinese](/languages/zh-CN)
- [Traditional Chinese](/languages/zh-TW)
- [Japanese](/languages/ja)
- [Korean](/languages/ko)
- [Russian](/languages/ru)
- [German](/languages/de)
- [Italian](/languages/it)
- [Spanish](/languages/es)
- [French](/languages/fr)
- [Arabic](/languages/ar)
- [Hindi](/languages/hi)
- [Turkish](/languages/tr)
- [Portuguese](/languages/pt)

## How Coverage Works

1. Every installed package runs over the text in priority order.
2. A positive result from any package flags the message.
3. Custom words in that language extend the Aho-Corasick automaton.
4. Level 2 (llama.cpp) provides a language-agnostic final verdict.

The **detector_chain** in every response names the detectors that actually ran,
making it easy to verify which packages contributed to a verdict.
