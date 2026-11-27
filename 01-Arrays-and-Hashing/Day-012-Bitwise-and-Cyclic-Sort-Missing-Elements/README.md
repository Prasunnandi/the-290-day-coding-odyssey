# Day 12: Bitwise & Cyclic Sort Missing Elements

## Overview
Day 12 addresses the family of bounded-range element detection problems:
1. **Floyd's Tortoise and Hare Cycle Detection (Find the Duplicate Number):** Interpreting arrays as functional graphs to locate cycles in $O(N)$ time with strictly read-only $O(1)$ space.
2. **Bitwise XOR Involutive Cancellation (Missing Number):** Eliminating matched pairs via $x \oplus x = 0$ with zero overflow risk.
3. **Sign Inversion Dual Detection (Set Mismatch):** Identifying both duplicate and missing values simultaneously using array indices as direct-address hash buckets.

---

## Problems Solved

| Problem | Difficulty | Key Pattern | Time Complexity | Space Complexity | Code Links |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **0287. Find the Duplicate Number** | Medium | Floyd's Cycle Detection / Functional Graph | $O(N)$ | $O(1)$ aux (read-only) | [Python](0287-find-the-duplicate-number/solution.py) / [Java](0287-find-the-duplicate-number/Solution.java) |
| **0268. Missing Number** | Easy | Bitwise XOR Cancellation | $O(N)$ | $O(1)$ aux | [Python](0268-missing-number/solution.py) / [Java](0268-missing-number/Solution.java) |
| **0645. Set Mismatch** | Easy | Sign Inversion Direct Addressing | $O(N)$ | $O(1)$ aux | [Python](0645-set-mismatch/solution.py) / [Java](0645-set-mismatch/Solution.java) |

---

## Comparative Matrix

```
+------------------------------------+--------------------------+---------------------------+
| Problem Feature                    | Primary Constraint       | Optimal Paradigm          |
+------------------------------------+--------------------------+---------------------------+
| Read-only array, single duplicate  | Cannot modify nums, O(1) | Floyd's Tortoise & Hare   |
| Continuous range [0..n], 1 missing | O(N) time, O(1) space    | Bitwise XOR Invariant     |
| 1 duplicate AND 1 missing in [1..n]| O(N) time, O(1) space    | Sign Inversion Marking    |
+------------------------------------+--------------------------+---------------------------+
```
