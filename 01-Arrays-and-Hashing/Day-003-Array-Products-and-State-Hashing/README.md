# 📅 Day 003: Arrays & Hashing — Products, Board Hashing & Sequence Starts

- **Phase:** Phase 1: Arrays & Hashing
- **Focus Pattern:** Prefix & Suffix Products, Grid Hashing & Sequence Start Detection
- **Target Difficulty:** 3 Medium Problems

---

## 🎯 Day 3 Overview & Key Algorithmic Patterns

1. **Prefix and Suffix Multiplication ($O(1)$ Extra Space):** By accumulating left-hand products in the output array and using a rolling variable for right-hand products, we achieve division-free $O(N)$ products without allocating auxiliary buffers.
2. **Matrix State Hashing with Integer Coordinates:** Mapping 2D Sudoku cell coordinates $(r, c)$ into sub-box blocks $(r // 3) \times 3 + (c // 3)$ to validate multiple constraints in a single traversal.
3. **Intelligent Sequence Starting ($O(N)$ vs $O(N^2)$):** Filtering candidates with `if num - 1 not in set` to ensure each contiguous sequence on the number line is only scanned from its exact starting boundary.

---

## 📚 Problems Solved Today

| # | LeetCode ID | Problem Title | Difficulty | Pattern | Python Solution | Java Solution | Time | Space | Status |
| :---: | :---: | :--- | :---: | :--- | :---: | :---: | :---: | :---: | :---: |
| 1 | 0238 | [Product of Array Except Self](https://leetcode.com/problems/product-of-array-except-self/) | Medium | Prefix/Suffix Multiplication | [Python](./0238-product-of-array-except-self/solution.py) | [Java](./0238-product-of-array-except-self/Solution.java) | $O(N)$ | $O(1)$ | ✅ Solved |
| 2 | 0036 | [Valid Sudoku](https://leetcode.com/problems/valid-sudoku/) | Medium | Matrix Coordinate State Hashing | [Python](./0036-valid-sudoku/solution.py) | [Java](./0036-valid-sudoku/Solution.java) | $O(1)$ | $O(1)$ | ✅ Solved |
| 3 | 0128 | [Longest Consecutive Sequence](https://leetcode.com/problems/longest-consecutive-sequence/) | Medium | Sequence Start Set Optimization | [Python](./0128-longest-consecutive-sequence/solution.py) | [Java](./0128-longest-consecutive-sequence/Solution.java) | $O(N)$ | $O(N)$ | ✅ Solved |

---

## 💡 Key Takeaways & Cheat Sheet

```text
Pattern: Product of all except self (no division)
-> output[i] = prefix_product_left
-> rolling_suffix_right accumulated backwards

Pattern: Sudoku 3x3 box indexing
-> box_idx = (r // 3) * 3 + (c // 3)

Pattern: Longest consecutive numbers in unsorted array in O(N)
-> Only scan forward IF (num - 1) is NOT in hash_set
```
