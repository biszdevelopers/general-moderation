# BK-Tree

The Burkhard-Keller tree (BK-tree) indexes the word bank by Levenshtein
distance so that fuzzy matches within a small edit distance can be found
without scanning the entire dictionary.

## Mathematical Formulation

Let \(d(x, y)\) be the Levenshtein edit distance. A BK-tree node stores a word
\(w\). Each child edge is labeled with a distance \(k\), and every word in the
subtree rooted at that child satisfies \(d(w, \text{word}) = k\). Searching
for words within distance \(t\) of a query \(q\) visits only the children
whose edge label lies in \([d(q, w) - t,\ d(q, w) + t]\), pruning the rest.

\[
\text{candidates}(q, t) = \{ p \in \text{tree} \mid d(q, p) \le t \}
\]

## Complexity

- **Build**: \(O(n \cdot d)\) expected, where \(d\) is the average distance
  computation cost.
- **Query**: \(O(\log n)\) in the average case; the worst case is \(O(n)\).

## Flowchart

```mermaid
flowchart TD
    A[Root word] --> B{Child edge k near d(q,w)?}
    B -->|yes| C[Recurse into subtree]
    B -->|no| D[Prune subtree]
    C --> E{Levenshtein(q, node) <= t?}
    E -->|yes| F[Emit node as candidate]
    E -->|no| G[Skip]
```

## Pseudocode

```text
class BKNode:
    word
    children = {}   # distance -> BKNode

insert(node, word):
    dist = levenshtein(node.word, word)
    if dist in node.children:
        insert(node.children[dist], word)
    else:
        node.children[dist] = BKNode(word)

search(node, query, t, results):
    dist = levenshtein(node.word, query)
    if dist <= t:
        results.add(node.word)
    for edge, child in node.children:
        if abs(dist - edge) <= t:
            search(child, query, t, results)
```

## References

- Burkhard, W. A. and Keller, R. M., "Some Approaches to Best-Match File
  Searching," Communications of the ACM, 1973.
- `pybktree` — https://github.com/benhoyt/pybktree
