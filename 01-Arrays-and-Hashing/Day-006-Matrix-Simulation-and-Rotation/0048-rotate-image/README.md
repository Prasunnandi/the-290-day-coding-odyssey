# 0048. Rotate Image

- **Difficulty:** Medium
- **Topic:** Arrays & Hashing
- **Pattern:** Matrix Transposition & Symmetry Reversal
- **LeetCode Link:** [Rotate Image](https://leetcode.com/problems/rotate-image/)

---

## Problem Statement

You are given an $n \times n$ 2D `matrix` representing an image, rotate the image by **90 degrees (clockwise)**.

You have to rotate the image **in place**, which means you have to modify the input 2D matrix directly. **DO NOT** allocate another 2D matrix and do the rotation.

---

## 💡 The Linear Algebra Property

A $90^\circ$ clockwise rotation is mathematically identical to a two-step geometric reflection:
$$\text{Rotate } 90^\circ \text{ Clockwise} = \text{Transpose} + \text{Horizontal Reflection (Reverse Each Row)}$$

### Step 1: Transpose along the Main Diagonal
Swap `matrix[r][c]` with `matrix[c][r]` for all $c > r$:
```text
[ 1, 2, 3 ]         [ 1, 4, 7 ]
[ 4, 5, 6 ]   -->   [ 2, 5, 8 ]
[ 7, 8, 9 ]         [ 3, 6, 9 ]
```

### Step 2: Reverse Each Row Horizontally
Reverse elements from left to right:
```text
[ 1, 4, 7 ]         [ 7, 4, 1 ]
[ 2, 5, 8 ]   -->   [ 8, 5, 2 ]
[ 3, 6, 9 ]         [ 9, 6, 3 ]   <-- Rotated 90° clockwise!
```

---

## 🚀 Implementations

### Python 3
```python
class Solution:
    def rotate(self, matrix: list[list[int]]) -> None:
        n = len(matrix)

        # 1. Transpose in-place
        for r in range(n):
            for c in range(r + 1, n):
                matrix[r][c], matrix[c][r] = matrix[c][r], matrix[r][c]

        # 2. Reverse each row
        for r in range(n):
            matrix[r].reverse()
```

### Java
```java
class Solution {
    public void rotate(int[][] matrix) {
        int n = matrix.length;

        // 1. Transpose in-place
        for (int r = 0; r < n; r++) {
            for (int c = r + 1; c < n; c++) {
                int temp = matrix[r][c];
                matrix[r][c] = matrix[c][r];
                matrix[c][r] = temp;
            }
        }

        // 2. Reverse each row
        for (int r = 0; r < n; r++) {
            int left = 0, right = n - 1;
            while (left < right) {
                int temp = matrix[r][left];
                matrix[r][left] = matrix[r][right];
                matrix[r][right] = temp;
                left++;
                right--;
            }
        }
    }
}
```

---

## 📊 Complexity Analysis

- **Time Complexity:** $O(N^2)$ — Transposition takes $O(N^2 / 2)$ operations, and reversing each of the $N$ rows takes $O(N^2 / 2)$ operations. Total operations $\approx N^2$.
- **Space Complexity:** $O(1)$ in-place — No extra arrays or memory are allocated.
