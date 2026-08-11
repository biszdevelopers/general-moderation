# Algorithms

The service relies on a small set of well-understood algorithms, each
documented here with its mathematical formulation, complexity analysis, a
flowchart, and pseudocode.

| Algorithm | Purpose | Complexity |
| :--- | :--- | :--- |
| [Aho-Corasick](/algorithms/aho-corasick) | Exact multi-pattern matching | O(n + m + z) build/search |
| [BK-tree](/algorithms/bk-tree) | Fuzzy matching, Levenshtein <= 2 | O(log n) query |
| [Double Metaphone](/algorithms/metaphone) | Phonetic variant matching | O(n) |
| [Semantic Similarity](/algorithms/semantic-similarity) | Paraphrase detection with SentenceTransformer + Faiss | O(n) encode, O(log N) search |
| [Suspicion Score](/algorithms/suspicion-score) | Weighted signal aggregation | O(d + c) |
| [User Profiling](/algorithms/user-profiling) | 91-day rolling window with cycle summaries | O(91 + s) per read |
| [Weight Tuning](/algorithms/weight-tuning) | Precision-driven daily adjustments | O(f + w) |
