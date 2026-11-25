# 📅 Day 006: Arrays & Hashing — Matrix Simulation & In-Place Rotations

- **Phase:** Phase 1: Arrays & Hashing
- **Focus Pattern:** Matrix In-Place Markers, Boundary Shrinking & Linear Algebra Rotations
- **Target Difficulty:** 3 Medium Problems

---

## 🎯 Day 6 Overview & In-Place Matrix Principles

1. **Repurposing First Row/Col as Marker Arrays ($O(1)$ Space):** Storing zero state directly in `matrix[r][0]` and `matrix[0][c]` avoids allocating $O(M + N)$ auxiliary memory. A single boolean variable solves the overlap conflict at `matrix[0][0]`.
2. **4-Boundary Moving Walls (Spiral Traversal):** Replacing complex angle checks with four simple boundary pointers (`top`, `bottom`, `left`, `right`) that shrink inward layer by layer, guarded by boundary checks to prevent double-processing.
3. **Linear Algebra Matrix Decomposition:** Rotating a 2D matrix by $90^\circ$ clockwise decomposes into two in-place symmetric operations: **Transpose + Horizontal Row Reversal**.

---

## 📚 Problems Solved Today

| # | LeetCode ID | Problem Title | Difficulty | Pattern | Python Solution | Java Solution | Time | Space | Status |
| :---: | :---: | :--- | :---: | :--- | :---: | :---: | :---: | :---: | :---: |
| 1 | 0073 | [Set Matrix Zeroes](https://leetcode.com/problems/set-matrix-zeroes/) | Medium | In-Place Row/Col Markers | [Python](./0073-set-matrix-zeroes/solution.py) | [Java](./0073-set-matrix-zeroes/Solution.java) | $O(M \cdot N)$ | $O(1)$ | ✅ Solved |
| 2 | 0054 | [Spiral Matrix](https://leetcode.com/problems/spiral-matrix/) | Medium | 4-Boundary Moving Walls | [Python](./0054-spiral-matrix/solution.py) | [Java](./0054-spiral-matrix/Solution.java) | $O(M \cdot N)$ | $O(1)$ | ✅ Solved |
| 3 | 0048 | [Rotate Image](https://leetcode.com/problems/rotate-image/) | Medium | Transpose + Row Reversal | [Python](./0048-rotate-image/solution.py) | [Java](./0048-rotate-image/Solution.java) | $O(N^2)$ | $O(1)$ | ✅ Solved |

---

## 💡 Key Takeaways & Cheat Sheet

```text
Pattern: In-place matrix zeroing with O(1) space
-> matrix[r][0] and matrix[0][c] act as marker flags
-> Use first_col_zero boolean for cell [0][0] ambiguity

Pattern: Spiral order traversal
-> Maintain: top, bottom, left, right
-> Guard checks: top <= bottom (moving left) & left <= right (moving up)

Pattern: Rotate matrix 90 degrees clockwise in-place
-> Transpose: swap matrix[r][c] with matrix[c][r] for c > r
-> Reverse: row.reverse() for each row
```
