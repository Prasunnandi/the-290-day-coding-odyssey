# 0054. Spiral Matrix

- **Difficulty:** Medium
- **Topic:** Arrays & Hashing
- **Pattern:** 4-Boundary Shrinking Matrix Simulation (Top, Bottom, Left, Right)
- **LeetCode Link:** [Spiral Matrix](https://leetcode.com/problems/spiral-matrix/)

---

## Problem Statement

Given an $m \times n$ matrix, return all elements of the `matrix` in **spiral order**.

### Examples

**Example 1:**
```text
Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]
Output: [1,2,3,6,9,8,7,4,5]
```

**Example 2:**
```text
Input: matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
Output: [1,2,3,4,8,12,11,10,9,5,6,7]
```

---

## 💡 Intuition & 4-Boundary Shrinking Frame

Instead of tracking angle directions and visited matrices, maintain **4 moving boundary walls**:
* `top = 0`, `bottom = m - 1`
* `left = 0`, `right = n - 1`

In each iteration of the outer while-loop, traverse in 4 distinct directions and shrink the respective wall inward:

```text
       left                               right
 top   [ →   →   →   →   →   →   →   →   ↓ ]  (top increments after)
       [ ↑                               ↓ ]
       [ ↑                               ↓ ]
bottom [ ↑   ←   ←   ←   ←   ←   ←   ←   ← ]  (bottom decrements after)
```

### Critical Boundary Guards
After traversing Right and Down:
1. `top` has moved down. Verify `top <= bottom` before traversing Left!
2. `right` has moved left. Verify `left <= right` before traversing Up!
Without these checks, non-square matrices (e.g., $1 \times 4$ or $3 \times 1$) will duplicate middle elements.

---

## 🚀 Implementations

### Python 3
```python
class Solution:
    def spiralOrder(self, matrix: list[list[int]]) -> list[int]:
        result = []
        if not matrix or not matrix[0]:
            return result

        top, bottom = 0, len(matrix) - 1
        left, right = 0, len(matrix[0]) - 1

        while top <= bottom and left <= right:
            # 1. Traverse Right
            for c in range(left, right + 1):
                result.append(matrix[top][c])
            top += 1

            # 2. Traverse Down
            for r in range(top, bottom + 1):
                result.append(matrix[r][right])
            right -= 1

            # 3. Traverse Left
            if top <= bottom:
                for c in range(right, left - 1, -1):
                    result.append(matrix[bottom][c])
                bottom -= 1

            # 4. Traverse Up
            if left <= right:
                for r in range(bottom, top - 1, -1):
                    result.append(matrix[r][left])
                left += 1

        return result
```

### Java
```java
import java.util.ArrayList;
import java.util.List;

class Solution {
    public List<Integer> spiralOrder(int[][] matrix) {
        List<Integer> result = new ArrayList<>();
        if (matrix == null || matrix.length == 0) return result;

        int top = 0, bottom = matrix.length - 1;
        int left = 0, right = matrix[0].length - 1;

        while (top <= bottom && left <= right) {
            for (int c = left; c <= right; c++) result.add(matrix[top][c]);
            top++;

            for (int r = top; r <= bottom; r++) result.add(matrix[r][right]);
            right--;

            if (top <= bottom) {
                for (int c = right; c >= left; c--) result.add(matrix[bottom][c]);
                bottom--;
            }

            if (left <= right) {
                for (int r = bottom; r >= top; r--) result.add(matrix[r][left]);
                left++;
            }
        }
        return result;
    }
}
```

---

## 📊 Complexity Analysis

- **Time Complexity:** $O(M \times N)$ — Each cell of the matrix is visited exactly once.
- **Space Complexity:** $O(1)$ auxiliary memory — Beyond the returned array, only the 4 scalar boundary pointers are allocated.
