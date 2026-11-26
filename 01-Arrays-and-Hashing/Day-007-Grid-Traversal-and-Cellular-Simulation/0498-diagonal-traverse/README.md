# 0498. Diagonal Traverse

- **Difficulty:** Medium
- **Topic:** Arrays & Hashing
- **Pattern:** Diagonal Index Invariance ($r + c = d$) & Direction Reflection
- **LeetCode Link:** [Diagonal Traverse](https://leetcode.com/problems/diagonal-traverse/)

---

## Problem Statement

Given an $m \times n$ matrix `mat`, return an array of all the elements of the array in a **diagonal order**.

---

## 💡 Intuition & Anti-Diagonal Invariant

All elements lying along the same upward/downward anti-diagonal share the **identical coordinate sum**:
$$r + c = d \quad \text{where } 0 \le d < m + n - 1$$

### Zigzag Parity
* **Even sum ($d \pmod 2 == 0$):** Traverse upwards (row decreases, column increases).
* **Odd sum ($d \pmod 2 == 1$):** Traverse downwards (row increases, column decreases).

### Boundary Reflection Rules
When moving **Up** ($r-1, c+1$):
* If hitting the right boundary (`c == n - 1`), drop down to next row (`r += 1`) and flip direction (`up = False`).
* If hitting the top boundary (`r == 0`), step right (`c += 1`) and flip direction.

When moving **Down** ($r+1, c-1$):
* If hitting the bottom boundary (`r == m - 1`), step right (`c += 1`) and flip direction (`up = True`).
* If hitting the left boundary (`c == 0`), step down (`r += 1`) and flip direction.

---

## 🚀 Implementations

### Python 3
```python
class Solution:
    def findDiagonalOrder(self, mat: list[list[int]]) -> list[int]:
        if not mat or not mat[0]:
            return []

        m, n = len(mat), len(mat[0])
        result = []
        r, c = 0, 0
        up = True

        for _ in range(m * n):
            result.append(mat[r][c])

            if up:
                if c == n - 1:
                    r += 1
                    up = False
                elif r == 0:
                    c += 1
                    up = False
                else:
                    r -= 1
                    c += 1
            else:
                if r == m - 1:
                    c += 1
                    up = True
                elif c == 0:
                    r += 1
                    up = True
                else:
                    r += 1
                    c -= 1

        return result
```

### Java
```java
class Solution {
    public int[] findDiagonalOrder(int[][] mat) {
        if (mat == null || mat.length == 0) return new int[0];

        int m = mat.length, n = mat[0].length;
        int[] result = new int[m * n];
        int r = 0, c = 0;
        boolean up = true;

        for (int i = 0; i < m * n; i++) {
            result[i] = mat[r][c];

            if (up) {
                if (c == n - 1) {
                    r++;
                    up = false;
                } else if (r == 0) {
                    c++;
                    up = false;
                } else {
                    r--;
                    c++;
                }
            } else {
                if (r == m - 1) {
                    c++;
                    up = true;
                } else if (c == 0) {
                    r++;
                    up = true;
                } else {
                    r++;
                    c--;
                }
            }
        }

        return result;
    }
}
```

---

## 📊 Complexity Analysis

- **Time Complexity:** $O(M \times N)$ — Each element is visited exactly once.
- **Space Complexity:** $O(1)$ auxiliary memory (excluding output array).
