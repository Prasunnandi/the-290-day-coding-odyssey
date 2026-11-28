# Day 18: Custom Sorting & Quickselect Selection

## Overview
Day 18 explores specialized sorting paradigms, total ordering relations, and sub-logarithmic order statistics:
1. **Constrained Alphabet Counting Sort (Custom Sort String):** Applying linear $O(|order| + |s|)$ frequency counting to reorder strings under explicit sequence constraints.
2. **Concatenation Comparator Transitivity (Largest Number):** Proving strict weak ordering over concatenated pairs ($A + B > B + A$) to maximize compound integers.
3. **Randomized 3-Way Quickselect (Kth Largest Element in an Array):** Reducing search space monotonically to achieve optimal expected $O(N)$ selection in $O(1)$ auxiliary space.

---

## Problems Solved

| Problem | Difficulty | Key Pattern | Time Complexity | Space Complexity | Code Links |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **0791. Custom Sort String** | Medium | Frequency Tabulation & Counting Sort | $O(|order| + |s|)$ | $O(1)$ aux | [Python](0791-custom-sort-string/solution.py) / [Java](0791-custom-sort-string/Solution.java) |
| **0179. Largest Number** | Medium | Transitive Concatenation Comparator | $O(N \log N \cdot K)$ | $O(N \cdot K)$ | [Python](0179-largest-number/solution.py) / [Java](0179-largest-number/Solution.java) |
| **0215. Kth Largest Element in an Array** | Medium | Randomized 3-Way Quickselect | $O(N)$ expected | $O(1)$ aux | [Python](0215-kth-largest-element-in-an-array/solution.py) / [Java](0215-kth-largest-element-in-an-array/Solution.java) |

---

## Sorting Paradigm Comparison
```
+------------------------------------+--------------------------+---------------------------+
| Algorithm                          | Underlying Mechanism     | Target Complexity         |
+------------------------------------+--------------------------+---------------------------+
| Custom Sort String                 | Counting Sort by Table   | O(N) linear time          |
| Largest Number                     | Transitive Total Order   | O(N log N) comparison sort|
| Kth Largest Element                | Hoare's Selection Cut    | O(N) expected time        |
+------------------------------------+--------------------------+---------------------------+
```
