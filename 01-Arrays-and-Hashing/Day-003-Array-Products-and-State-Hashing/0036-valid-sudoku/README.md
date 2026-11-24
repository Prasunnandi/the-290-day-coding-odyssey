# 0036. Valid Sudoku

- **Difficulty:** Medium
- **Topic:** Arrays & Hashing
- **Pattern:** Matrix State Hashing (Row, Column, and Sub-box Set Membership)
- **LeetCode Link:** [Valid Sudoku](https://leetcode.com/problems/valid-sudoku/)

---

## Problem Statement

Determine if a $9 \times 9$ Sudoku board is valid. Only the filled cells need to be validated according to the following rules:
1. Each row must contain the digits `1-9` without repetition.
2. Each column must contain the digits `1-9` without repetition.
3. Each of the nine $3 \times 3$ sub-boxes of the grid must contain the digits `1-9` without repetition.

**Note:** A valid board is not necessarily solvable; only existing entries must satisfy the constraints.

---

## 💡 Intuition & 3x3 Box Coordinate Mapping

The crucial challenge in this problem is indexing the nine $3 \times 3$ sub-boxes cleanly in a single pass.

Dividing the row $r$ and column $c$ by 3 (integer division) collapses the $9 \times 9$ grid into a $3 \times 3$ block grid:

```text
Row block:    r // 3  ∈ {0, 1, 2}
Col block:    c // 3  ∈ {0, 1, 2}

Sub-box Index Formula:
box_idx = (r // 3) * 3 + (c // 3)
```

### Visual Sub-box Layout

```text
       c=0..2     c=3..5     c=6..8
r=0..2 [ Box 0 ]  [ Box 1 ]  [ Box 2 ]
r=3..5 [ Box 3 ]  [ Box 4 ]  [ Box 5 ]
r=6..8 [ Box 6 ]  [ Box 7 ]  [ Box 8 ]
```

---

## 🚀 Implementations

### Python 3 (Hash Sets)
```python
from collections import defaultdict

class Solution:
    def isValidSudoku(self, board: list[list[str]]) -> bool:
        rows = defaultdict(set)
        cols = defaultdict(set)
        boxes = defaultdict(set)

        for r in range(9):
            for c in range(9):
                val = board[r][c]
                if val == ".":
                    continue

                box_key = (r // 3, c // 3)
                if val in rows[r] or val in cols[c] or val in boxes[box_key]:
                    return False

                rows[r].add(val)
                cols[c].add(val)
                boxes[box_key].add(val)

        return True
```

### Java (Boolean Lookup Array — Optimal)
```java
class Solution {
    public boolean isValidSudoku(char[][] board) {
        boolean[][] rows = new boolean[9][9];
        boolean[][] cols = new boolean[9][9];
        boolean[][] boxes = new boolean[9][9];

        for (int r = 0; r < 9; r++) {
            for (int c = 0; c < 9; c++) {
                if (board[r][c] == '.') continue;

                int num = board[r][c] - '1'; // 0-8 indexing
                int boxIdx = (r / 3) * 3 + (c / 3);

                if (rows[r][num] || cols[c][num] || boxes[boxIdx][num]) {
                    return false;
                }

                rows[r][num] = true;
                cols[c][num] = true;
                boxes[boxIdx][num] = true;
            }
        }
        return true;
    }
}
```

---

## 📊 Complexity Analysis

- **Time Complexity:** $O(1)$ — Exactly $9 \times 9 = 81$ cells are inspected, performing $O(1)$ set/array lookups per cell.
- **Space Complexity:** $O(1)$ — The board is strictly fixed at $9 \times 9$. The boolean tables or sets store at most $81$ entries total.
