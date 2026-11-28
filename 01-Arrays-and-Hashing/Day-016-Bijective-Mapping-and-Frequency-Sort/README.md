# Day 16: Bijective Mapping & Frequency-Based Bucket Sorting

## Overview
Day 16 focuses on hash-table relational invariants and non-comparison sorting:
1. **Character-to-Character Bijection (Isomorphic Strings):** Enforcing bidirectional 1-to-1 character mappings across strings using twin hash arrays.
2. **Character-to-Token Bijection (Word Pattern):** Generalizing isomorphic mappings to whitespace-delimited word sequences.
3. **Linear-Time Frequency Sorting (Sort Characters By Frequency):** Utilizing bucket sort indexed by frequency to sort strings in optimal $O(N)$ time.

---

## Problems Solved

| Problem | Difficulty | Key Pattern | Time Complexity | Space Complexity | Code Links |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **0205. Isomorphic Strings** | Easy | Two-Way Character Bijection | $O(N)$ | $O(1)$ aux | [Python](0205-isomorphic-strings/solution.py) / [Java](0205-isomorphic-strings/Solution.java) |
| **0290. Word Pattern** | Easy | Tokenized Two-Way Bijection | $O(N + M)$ | $O(W)$ aux | [Python](0290-word-pattern/solution.py) / [Java](0290-word-pattern/Solution.java) |
| **0451. Sort Characters By Frequency** | Medium | Linear-Time Frequency Bucket Sort | $O(N)$ | $O(N)$ aux | [Python](0451-sort-characters-by-frequency/solution.py) / [Java](0451-sort-characters-by-frequency/Solution.java) |

---

## Key Algorithmic Insights
- **Why Two Hash Maps for Bijection?** A single forward mapping checks only that one input maps to one output (function property), but does NOT guarantee that two different inputs do not collide onto the same output (injective property). A reverse mapping is required to guarantee strict bijection.
- **Why Bucket Sort for Frequencies?** The frequency of any element in an array of size $N$ is integer-bounded in $[1, N]$. Using frequency directly as an array index eliminates $O(K \log K)$ sorting comparisons completely.
