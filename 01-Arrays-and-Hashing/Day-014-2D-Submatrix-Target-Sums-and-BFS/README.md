# Day 14: 2D Submatrix Target Sums & Multi-Source BFS

## Overview
Day 14 explores advanced matrix geometry, multi-source graph exploration, and 2D-to-1D dimension reduction:
1. **Multi-Source BFS (01 Matrix):** Seeding all distance zeroes simultaneously to achieve global shortest Manhattan paths in $O(M \cdot N)$ time.
2. **Submatrix Sum Target (Number of Submatrices That Sum to Target):** Collapsing vertical columns into 1D row slices to apply hash-map prefix counting in $O(N^2 \cdot M)$ time.
3. **Submatrix Sum Inequality (Max Sum of Rectangle No Larger Than K):** Combining 2D collapse with binary search prefix lookups (TreeSet ceiling) to optimize bounded maximum rectangle sums.

---

## Problems Solved

| Problem | Difficulty | Key Pattern | Time Complexity | Space Complexity | Code Links |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **0542. 01 Matrix** | Medium | Multi-Source BFS Expansion | $O(M \cdot N)$ | $O(M \cdot N)$ | [Python](0542-01-matrix/solution.py) / [Java](0542-01-matrix/Solution.java) |
| **1074. Number of Submatrices That Sum to Target** | Hard | 2D-to-1D Reduction + Prefix Hash Map | $O(N^2 \cdot M)$ | $O(M)$ | [Python](1074-number-of-submatrices-that-sum-to-target/solution.py) / [Java](1074-number-of-submatrices-that-sum-to-target/Solution.java) |
| **0363. Max Sum of Rectangle No Larger Than K** | Hard | 2D Reduction + TreeSet Ceiling Lookup | $O(\min(M, N)^2 \cdot \max(M, N) \log \max(M, N))$ | $O(\max(M, N))$ | [Python](0363-max-sum-of-rectangle-no-larger-than-k/solution.py) / [Java](0363-max-sum-of-rectangle-no-larger-than-k/Solution.java) |

---

## Dimension Reduction Blueprint
Any problem asking for optimal submatrices bounded by $(r_1, c_1)$ and $(r_2, c_2)$ can be flattened:
```
Fix pair of columns (c1, c2)
  Accumulate row slices: slice[r] = sum(matrix[r][c1..c2])
  Apply 1D algorithm on slice[0..m-1]:
    - For exact target sum == K: Hash Map Prefix Counting (O(M))
    - For bounded sum <= K: Binary Search / TreeSet (O(M log M))
```
