# Day 13: Randomized Data Structures & 2D Prefix Sums

## Overview
Day 13 covers hybrid collection engineering and multidimensional prefix sums:
1. **Swap-and-Pop Deletion (Insert Delete GetRandom O(1)):** Combining dynamic array random indexing with hash map $O(1)$ coordinate lookup.
2. **Multiset Index Tracking (Insert Delete GetRandom O(1) - Duplicates):** Maintaining hash sets of indices per value to preserve probability proportional to frequency.
3. **2D Inclusion-Exclusion (Range Sum Query 2D - Immutable):** Generalizing 1D prefix sums to 2D matrices for true $O(1)$ arbitrary rectangular region queries.

---

## Problems Solved

| Problem | Difficulty | Key Pattern | Time Complexity | Space Complexity | Code Links |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **0380. Insert Delete GetRandom O(1)** | Medium | Dynamic Array + Hash Map (Swap-and-Pop) | $O(1)$ avg | $O(N)$ | [Python](0380-insert-delete-getrandom-o1/solution.py) / [Java](0380-insert-delete-getrandom-o1/Solution.java) |
| **0381. Insert Delete GetRandom O(1) - Duplicates** | Hard | Dynamic Array + Hash Map of Index Sets | $O(1)$ avg | $O(N)$ | [Python](0381-insert-delete-getrandom-o1-duplicates-allowed/solution.py) / [Java](0381-insert-delete-getrandom-o1-duplicates-allowed/Solution.java) |
| **0304. Range Sum Query 2D - Immutable** | Medium | 2D Inclusion-Exclusion Prefix Table | $O(1)$ query | $O(M \cdot N)$ | [Python](0304-range-sum-query-2d-immutable/solution.py) / [Java](0304-range-sum-query-2d-immutable/Solution.java) |

---

## Key Algorithmic Insights
- **Why Swap-and-Pop?** Array deletions at the tail are $O(1)$. Overwriting the target index with the tail element turns an arbitrary internal deletion into a tail pop without shifting elements.
- **Multidimensional Prefix Sum:** To compute subgrid sums in $O(1)$, remember to add back the double-subtracted top-left overlap:
  $$\text{Area} = P[r_2+1][c_2+1] - P[r_1][c_2+1] - P[r_2+1][c_1] + P[r_1][c_1]$$
