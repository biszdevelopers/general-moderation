---
layout: home

hero:
    name: Moderation Service
    text: Multi-language content moderation microservice
    tagline: Sub-millisecond rule-based detection over 20+ languages, backed by C/C++/Rust libraries and an optional llama.cpp inference engine.
    actions:
        - theme: brand
          text: Getting Started
          link: /guide/getting-started
        - theme: alt
          text: API Reference
          link: /api/index

features:
    - icon: ⚡
      title: Sub-millisecond Level 1
      details: Bloom filters, Aho-Corasick, MurmurHash3, and C edit distance keep exact matching below a millisecond.
    - icon: 🌐
      title: 20+ Languages
      details: Eleven C/C++/Rust/WebAssembly packages combine base dictionaries across the world's major languages.
    - icon: 🔒
      title: C/C++ First Security
      details: Cryptography, hashing, TLS, rate limiting, and authentication all delegate to compiled libraries.
    - icon: 🧠
      title: AI Final Verdict
      details: Level 2 llama.cpp resolves borderline cases with a locally hosted GGUF model.
---
