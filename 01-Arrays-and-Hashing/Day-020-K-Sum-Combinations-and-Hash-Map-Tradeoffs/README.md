# Day 20: K-Sum Combinations & Hash Map Tradeoffs

## Overview
Day 20 unifies the family of $K$-Sum and target-sum problems:
1. **Generalized K-Sum Reduction (4Sum):** Recursive dimension reduction from $K$ down to the $K = 2$ base case using two pointers and early pruning in $O(N^{K - 1})$ time.
2. **Meet-in-the-Middle Partitioning (4Sum II):** Trading space for time by precomputing pairwise sums in $O(N^2)$ time and $O(N^2)$ space across 4 independent arrays.
3. **Monotonic Two-Pointer Gap Minimization (3Sum Closest):** Directing two-pointer convergence to track closest proximity to a target sum in $O(N^2)$ time and $O(1)$ auxiliary space.

---

## Problems Solved

| Problem | Difficulty | Key Pattern | Time Complexity | Space Complexity | Code Links |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **0018. 4Sum** | Medium | General K-Sum Recursion & Two Pointers | $O(N^3)$ | $O(N)$ aux | [Python](0018-4sum/solution.py) / [Java](0018-4sum/Solution.java) |
| **0454. 4Sum II** | Medium | Meet-in-the-Middle Hash Map Tradeoff | $O(N^2)$ | $O(N^2)$ aux | [Python](0454-4sum-ii/solution.py) / [Java](0454-4sum-ii/Solution.java) |
| **0016. 3Sum Closest** | Medium | Sorted Two-Pointer Convergent Scan | $O(N^2)$ | $O(1)$ aux | [Python](0016-3sum-closest/solution.py) / [Java](0016-3sum-closest/Solution.java) |

---

## 4Sum vs. 4Sum II Architectural Comparison
```
+------------------------------------+--------------------------+---------------------------+
| Feature                            | LeetCode 18 (4Sum)       | LeetCode 454 (4Sum II)    |
+------------------------------------+--------------------------+---------------------------+
| Input Source                       | Single array nums        | 4 distinct arrays         |
| Uniqueness Requirement             | Distinct quadruplets     | Distinct index tuples     |
| Optimal Approach                   | Sorting + Two Pointers   | Meet-in-the-Middle Hashing|
| Time Complexity                    | O(N^3)                   | O(N^2)                    |
| Space Complexity                   | O(1) auxiliary           | O(N^2) auxiliary          |
+------------------------------------+--------------------------+---------------------------+
```
