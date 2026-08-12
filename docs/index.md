---
layout: home

hero:
    name: General Moderation
    text: Multi-language content moderation service
    tagline: A three-stage pipeline that pre-filters content before human review — fast-path rules, semantic similarity, user profiling, and a local LLM.
    actions:
        - theme: brand
          text: Getting Started
          link: /guide/
        - theme: alt
          text: Architecture
          link: /architecture/

features:
    - icon: ⚡
      title: 3-Stage Pipeline
      details: Safe-word fast path, parallel rule detectors with suspicion scoring, and a conditional LLM final verdict.
    - icon: 🌐
      title: 26+ Languages
      details: Eleven C/C++/Rust/WebAssembly packages combine base dictionaries across the world's major languages.
    - icon: 🧠
      title: Semantic Similarity
      details: Multilingual SentenceTransformer embeddings searched against per-category Faiss indexes.
    - icon: 📊
      title: User Profiling
      details: A 91-day rolling window with archived, linked cycle summaries keeps long-term history with bounded storage.
    - icon: 🔁
      title: Active Learning
      details: Administrator feedback tunes weights and thresholds daily through the auto-tuning batch.
    - icon: 📦
      title: Full Export
      details: One ZIP archive of every database, CSV, log, config snapshot, and semantic index.
---
