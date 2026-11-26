# Day 8: In-Place Array Index Marking & Cyclic Sort

## Overview
Day 8 focuses on the **Index-as-Hash-Key** pattern for arrays containing values within bounded ranges $[1, n]$. Rather than spending $O(n)$ extra memory on `HashSet` or `HashMap`, we encode state directly into the array itself:
1. **Cyclic Sort Swapping:** Reorganizing numbers into their canonical bucket positions ($x$ at index $x - 1$).
2. **Sign Inversion as Visited Flag:** Negating the value at index $(|x| - 1)$ to mark number $x$ as present.
3. **Duplicate Detection:** Checking if index $(|x| - 1)$ is already negative upon inspection.

---

## Problems Solved

| Problem | Difficulty | Key Pattern | Time Complexity | Space Complexity | Code Links |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **0041. First Missing Positive** | Hard | Cyclic Sort / In-Place Swapping | $O(N)$ | $O(1)$ aux | [Python](0041-first-missing-positive/solution.py) / [Java](0041-first-missing-positive/Solution.java) |
| **0448. Find All Numbers Disappeared** | Easy | Sign Inversion (Negation Marking) | $O(N)$ | $O(1)$ aux | [Python](0448-find-all-numbers-disappeared-in-an-array/solution.py) / [Java](0448-find-all-numbers-disappeared-in-an-array/Solution.java) |
| **0442. Find All Duplicates in an Array** | Medium | Sign Inversion (Duplicate Catch) | $O(N)$ | $O(1)$ aux | [Python](0442-find-all-duplicates-in-an-array/solution.py) / [Java](0442-find-all-duplicates-in-an-array/Solution.java) |

---

## Pattern Comparison

```
+-----------------------------------+-----------------------------------------------+
| Approach                          | Best Suited For                               |
+-----------------------------------+-----------------------------------------------+
| Cyclic Sort Swapping              | Finding missing/corrupted elements where      |
|                                   | values can be permuted arbitrarily            |
+-----------------------------------+-----------------------------------------------+
| Sign Negation Marking             | Read-only duplicate or missing queries where  |
|                                   | original magnitudes must be preserved         |
+-----------------------------------+-----------------------------------------------+
```
