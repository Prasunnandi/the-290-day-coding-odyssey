# Day 10: Lexicographical Order & In-Place Merge

## Overview
Day 10 concludes fundamental array permutation and sorting manipulations:
1. **Lexicographical Suffix Reversal (Next Permutation):** Identifying the inflection point and reversing descending suffixes in $O(N)$ time.
2. **Dual-Extrema Dynamic Programming (Maximum Product Subarray):** Tracking paired min-max variables across sign inversions.
3. **Reverse Pointer Placement (Merge Sorted Array):** Right-to-left three-pointer merge guaranteeing non-destructive $O(1)$ memory usage.

---

## Problems Solved

| Problem | Difficulty | Key Pattern | Time Complexity | Space Complexity | Code Links |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **0031. Next Permutation** | Medium | Pivot Finding + Suffix Inversion | $O(N)$ | $O(1)$ aux | [Python](0031-next-permutation/solution.py) / [Java](0031-next-permutation/Solution.java) |
| **0152. Maximum Product Subarray** | Medium | Dual-Extrema Tracking (Min/Max DP) | $O(N)$ | $O(1)$ aux | [Python](0152-maximum-product-subarray/solution.py) / [Java](0152-maximum-product-subarray/Solution.java) |
| **0088. Merge Sorted Array** | Easy | Three-Pointer Reverse In-Place Merge | $O(M + N)$ | $O(1)$ aux | [Python](0088-merge-sorted-array/solution.py) / [Java](0088-merge-sorted-array/Solution.java) |

---

## Key Takeaways
- When rearranging arrays lexicographically, descending suffixes represent the maximal local order; reversing them yields the minimal local order.
- In product maximization, negative numbers swap minimum and maximum states — maintaining both bounds is essential.
- Merging into an array that has reserved capacity at the tail is always cleanest when processed from back to front.
