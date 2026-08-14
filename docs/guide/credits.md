# Credits

General Moderation relies on a number of open-source projects. This page
credits everything used by the service — word data, detector packages,
algorithm libraries, frameworks, and tooling.

## Chinese sensitive-word lists

These subrepos live under `backend/data/` and are consumed as **raw word
data** through this service's own matching algorithms (Aho-Corasick, BK-tree,
Bloom). They ship no Python bindings, so none of their code runs here — only
the word lists are read at load time. Fetch them with
`git submodule update --init`.

| Source | Repository | License | Used for |
| :--- | :--- | :--- | :--- |
| sensitive-stop-words | [fwwdn/sensitive-stop-words](https://github.com/fwwdn/sensitive-stop-words) | Apache-2.0 | Per-category blocking lists (political, porn, gun, ad, url) |
| sensitive | [importcjj/sensitive](https://github.com/importcjj/sensitive) | MIT | `dict/dict.txt` — Chinese sensitive-word list |
| sensitive-lexicon | [konsheng/Sensitive-lexicon](https://github.com/konsheng/Sensitive-lexicon) | MIT | `Vocabulary/` — political, porn, gun, URL, and other category lists |
| sensitive-word-data | [houbb/sensitive-word-data](https://github.com/houbb/sensitive-word-data) | Apache-2.0 | `sensitive_word_dict.txt` — Chinese sensitive-word dictionary |

## Detection packages

The multi-language detector guard-wires installed packages. The ones that
activate on a standard install are listed here; several more are wired behind
import guards and activate only when a working index provides them.

| Package | Language/Engine | Purpose |
| :--- | :--- | :--- |
| [badwords-py](https://pypi.org/project/badwords-py/) | Rust | Fast word-level profanity |
| [profanite](https://pypi.org/project/profanite/) | Rust | Anti-obfuscation profanity |
| [glin-profanity](https://pypi.org/project/glin-profanity/) | C | Context-aware profanity |
| [gangajal](https://pypi.org/project/gangajal/) | WebAssembly | Sandboxed profanity detection |
| [PyProfane](https://pypi.org/project/pyprofane/) | C | Soundex-based profanity |

## Algorithm and native libraries

| Library | Purpose |
| :--- | :--- |
| [ahocorasick-rs](https://pypi.org/project/ahocorasick-rs/) | Rust Aho-Corasick multi-pattern matching (primary engine for the Chinese sensitive-word lists) |
| [pyahocorasick](https://pypi.org/project/pyahocorasick/) | Aho-Corasick exact multi-pattern matching (word bank + fallback) |
| [pybktree](https://pypi.org/project/pybktree/) | BK-tree fuzzy matching |
| [python-Levenshtein](https://pypi.org/project/python-Levenshtein/) | Edit-distance computation |
| [metaphone](https://pypi.org/project/metaphone/) | Double Metaphone phonetic matching |
| [pybloom-live](https://pypi.org/project/pybloom-live/) | Bloom filter fast-negative rejection |
| [mmh3](https://pypi.org/project/mmh3/) | MurmurHash3 fingerprinting |
| [regex](https://pypi.org/project/regex/) | Onigmo-backed regex engine |
| [llama-cpp-python](https://pypi.org/project/llama-cpp-python/) | Local LLM inference (optional `ai` extra) |
| [sentence-transformers](https://pypi.org/project/sentence-transformers/) + [faiss-cpu](https://pypi.org/project/faiss-cpu/) | Semantic similarity (optional `semantic` extra) |

## Framework and infrastructure

- [FastAPI](https://fastapi.tiangolo.com/) + [uvicorn](https://www.uvicorn.org/) —
  HTTP framework and ASGI server
- [Pydantic](https://docs.pydantic.dev/) / pydantic-settings — request models and configuration
- [SQLite](https://www.sqlite.org/) — persistence for settings, feedback, profiling, phrases
- [llama.cpp](https://github.com/ggml-org/llama.cpp) — local GGUF inference backend
- [VitePress](https://vitepress.dev/) — this documentation site

## Tooling

- [uv](https://astral.sh/uv/) — Python dependency management
- [ruff](https://docs.astral.sh/ruff/) — linting and formatting
- [pytest](https://docs.pytest.org/) — testing framework

If you believe a dependency is missing from this page, please open an issue.
