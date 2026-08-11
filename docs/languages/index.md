# Language Coverage

The service detects vulgar and politically sensitive content across 20+
languages. Coverage comes from the union of eleven C/C++/Rust/WebAssembly
packages plus custom words.

## Package Matrix

| Package | Core tech | Scope |
| :--- | :--- | :--- |
| `badwords-py` | Rust | 26+ languages |
| `profanite` | Rust | Universal |
| `glin-profanity` | C | 25+ languages |
| `safetext` | C | 13 languages |
| `sensitive-word-filter-cn` | C (DFA) | Chinese |
| `profanity-filter2` | C | Universal |
| `gangajal` | WebAssembly | All languages |
| `scheckbl` | C | Universal |
| `valx` | C + AI | Universal |
| `sensitive-word-filter` | C | Chinese (political) |
| `pyprofane` | C | Universal |

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
