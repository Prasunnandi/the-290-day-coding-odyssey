# Day 15: Max Chunks & Disjoint Interval Partitioning

## Overview
Day 15 masters array boundary partitioning where chunks must maintain prefix-suffix ordering invariants:
1. **Permutation Index Matching (Max Chunks To Make Sorted I):** Leveraging the invariant $\max(\text{arr}[0 \dots i]) == i$ for $[0, n - 1]$ permutations.
2. **Prefix Max vs. Suffix Min Invariant (Max Chunks To Make Sorted II):** Validating general cuts where $\max(\text{left}) \le \min(\text{right})$ using a precomputed suffix minimum array.
3. **One-Pass Greedy Horizon Expansion (Partition Array into Disjoint Intervals):** Finding the minimal left partition satisfying $\max(\text{left}) \le \min(\text{right})$ in $O(1)$ auxiliary memory.

---

## Problems Solved

| Problem | Difficulty | Key Pattern | Time Complexity | Space Complexity | Code Links |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **0769. Max Chunks To Make Sorted** | Medium | Permutation Max Value Index Matching | $O(N)$ | $O(1)$ aux | [Python](0769-max-chunks-to-make-sorted/solution.py) / [Java](0769-max-chunks-to-make-sorted/Solution.java) |
| **0768. Max Chunks To Make Sorted II** | Hard | Prefix Max vs. Suffix Min Invariant | $O(N)$ | $O(N)$ aux | [Python](0768-max-chunks-to-make-sorted-ii/solution.py) / [Java](0768-max-chunks-to-make-sorted-ii/Solution.java) |
| **0915. Partition Array into Disjoint Intervals** | Medium | One-Pass Greedy Horizon Expansion | $O(N)$ | $O(1)$ aux | [Python](0915-partition-array-into-disjoint-intervals/solution.py) / [Java](0915-partition-array-into-disjoint-intervals/Solution.java) |

---

## Key Invariant Comparison
```
+------------------------------------+-----------------------------------------------+
| Scenario                           | Invariant Required for Valid Cut at Index i   |
+------------------------------------+-----------------------------------------------+
| Permutation of [0 .. n - 1]        | max(arr[0 .. i]) == i                         |
| Arbitrary array (Max Chunks)       | max(arr[0 .. i]) <= min(arr[i + 1 .. n - 1])  |
| Minimal Left Partition             | Whenever arr[i] < max_left, swallow i into L  |
+------------------------------------+-----------------------------------------------+
```
