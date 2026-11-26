# Day 9: Boyer-Moore Voting & Kadane's Algorithm

## Overview
Day 9 covers linear-time cancellation and greedy accumulation paradigms:
1. **Boyer-Moore Voting ($> n/2$):** Majority element identification in $O(N)$ time and $O(1)$ space using pairwise cancellation.
2. **Extended Boyer-Moore ($> n/3$):** Dual-candidate tracking with triplet cancellation and confirmation pass.
3. **Kadane's Algorithm:** Optimal subarray sum via local vs. global dynamic programming decision states.

---

## Problems Solved

| Problem | Difficulty | Key Pattern | Time Complexity | Space Complexity | Code Links |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **0169. Majority Element** | Easy | Boyer-Moore Pairwise Voting | $O(N)$ | $O(1)$ aux | [Python](0169-majority-element/solution.py) / [Java](0169-majority-element/Solution.java) |
| **0229. Majority Element II** | Medium | Triplet Cancellation Voting | $O(N)$ | $O(1)$ aux | [Python](0229-majority-element-ii/solution.py) / [Java](0229-majority-element-ii/Solution.java) |
| **0053. Maximum Subarray** | Medium | Kadane's DP / Running Optimum | $O(N)$ | $O(1)$ aux | [Python](0053-maximum-subarray/solution.py) / [Java](0053-maximum-subarray/Solution.java) |

---

## Pattern Comparison: Elimination vs. Accumulation

```
+---------------------------+-------------------------------+-----------------------------------+
| Pattern                   | Governing Principle           | Core Invariant                    |
+---------------------------+-------------------------------+-----------------------------------+
| Boyer-Moore (k = 2)       | Pairwise Cancellation         | Dominant element survives         |
|                           |                               | against all others combined       |
+---------------------------+-------------------------------+-----------------------------------+
| Boyer-Moore (k = 3)       | Triplet Cancellation          | At most 2 elements can satisfy    |
|                           |                               | frequency > floor(n / 3)          |
+---------------------------+-------------------------------+-----------------------------------+
| Kadane's Algorithm        | Prefix Reset if Negative      | Never propagate negative prefix   |
|                           |                               | sum into future subarrays         |
+---------------------------+-------------------------------+-----------------------------------+
```
