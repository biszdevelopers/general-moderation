# Language Coverage

The service detects vulgar and politically sensitive content across 20+
languages. Coverage comes from the union of the verified C/C++/Rust/
WebAssembly packages plus custom words.

## Package Matrix

Only packages that install cleanly and run on the supported platforms are
registered in the detector.

| Package | Core tech | Scope | Status |
| :--- | :--- | :--- | :--- |
| `profanite` | Rust | Universal | Active |
| `glin-profanity` | C | 25+ languages | Active |
| `badwords` | Rust | 26+ languages | Active |
| `gangajal` | WebAssembly | All languages | Active |
| `PyProfane` | C | Universal | Active |
| `safetext` | Python | 13 languages | Guard-wired |
| `sensitive-word-filter-cn` | Python | Chinese | Guard-wired |
| `profanity-filter2` | Python | Universal | Guard-wired |

**Active** packages run on a standard install. **Guard-wired** packages are
import-guarded but no reachable index (pypi.org, Tsinghua, Aliyun) provides an
installable release; they activate only when a working index provides them
(e.g. `uv add safetext==0.3.3`).

Not registered: `scheckbl` and `valx` (their documented APIs do not exist in
the installed versions) and `datasketch` (MinHash semantic similarity is not
a direct profanity detector and needs a pre-built toxic-signature database).

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
