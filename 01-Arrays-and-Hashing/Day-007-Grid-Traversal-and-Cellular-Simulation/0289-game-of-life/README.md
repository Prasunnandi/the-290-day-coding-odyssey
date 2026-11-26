# 0289. Game of Life

- **Difficulty:** Medium
- **Topic:** Arrays & Hashing
- **Pattern:** Cellular Automata In-Place State Encoding (2-Bit Transition Modeling)
- **LeetCode Link:** [Game of Life](https://leetcode.com/problems/game-of-life/)

---

## Problem Statement

According to Conway's Game of Life, the board is an $m \times n$ grid of cells where each cell is either `0` (dead) or `1` (alive):
1. **Under-population:** Any live cell with fewer than two live neighbors dies.
2. **Survival:** Any live cell with two or three live neighbors lives on.
3. **Over-population:** Any live cell with more than three live neighbors dies.
4. **Reproduction:** Any dead cell with exactly three live neighbors becomes a live cell.

The next state is created by applying the above rules **simultaneously** to every cell.

### Follow-up
Could you solve it **in-place** without creating an $O(M \times N)$ auxiliary copy of the board?

---

## 💡 In-Place 2-State Encoding

When updating sequentially, cell modifications would corrupt neighbor counts for subsequent cells. To do this in-place without auxiliary memory, encode **both the past and future states** into each integer:

| Old State | New State | Encoded Value | Condition |
| :---: | :---: | :---: | :--- |
| `0` (dead) | `0` (dead) | `0` | Default |
| `1` (live) | `1` (live) | `1` | 2 or 3 live neighbors |
| `1` (live) | `0` (dead) | `-1` | $< 2$ or $> 3$ live neighbors |
| `0` (dead) | `1` (live) | `2` | Exactly 3 live neighbors |

### Two-Pass Execution
1. **Pass 1 (Counting Neighbors):**
   * A neighbor was originally live if `abs(board[nr][nc]) == 1` (both `1` and `-1` represent past live cells).
   * Update the cell to `-1` or `2` if a state transition occurs.
2. **Pass 2 (Resolution):**
   * Map `board[r][c] > 0` to `1` (covers both `1` and `2`).
   * Map `board[r][c] <= 0` to `0` (covers both `0` and `-1`).

---

## 🚀 Implementations

### Python 3
```python
class Solution:
    def gameOfLife(self, board: list[list[int]]) -> None:
        m, n = len(board), len(board[0])
        directions = [(-1,-1), (-1,0), (-1,1), (0,-1), (0,1), (1,-1), (1,0), (1,1)]

        for r in range(m):
            for c in range(n):
                live_neighbors = 0
                for dr, dc in directions:
                    nr, nc = r + dr, c + dc
                    if 0 <= nr < m and 0 <= nc < n and abs(board[nr][nc]) == 1:
                        live_neighbors += 1

                if board[r][c] == 1 and (live_neighbors < 2 or live_neighbors > 3):
                    board[r][c] = -1
                elif board[r][c] == 0 and live_neighbors == 3:
                    board[r][c] = 2

        for r in range(m):
            for c in range(n):
                board[r][c] = 1 if board[r][c] > 0 else 0
```

### Java
```java
class Solution {
    public void gameOfLife(int[][] board) {
        int m = board.length, n = board[0].length;
        int[][] dirs = {{-1,-1},{-1,0},{-1,1},{0,-1},{0,1},{1,-1},{1,0},{1,1}};

        for (int r = 0; r < m; r++) {
            for (int c = 0; c < n; c++) {
                int liveNeighbors = 0;
                for (int[] d : dirs) {
                    int nr = r + d[0], nc = c + d[1];
                    if (nr >= 0 && nr < m && nc >= 0 && nc < n && Math.abs(board[nr][nc]) == 1) {
                        liveNeighbors++;
                    }
                }

                if (board[r][c] == 1 && (liveNeighbors < 2 || liveNeighbors > 3)) board[r][c] = -1;
                else if (board[r][c] == 0 && liveNeighbors == 3) board[r][c] = 2;
            }
        }

        for (int r = 0; r < m; r++) {
            for (int c = 0; c < n; c++) {
                board[r][c] = board[r][c] > 0 ? 1 : 0;
            }
        }
    }
}
```

---

## 📊 Complexity Analysis

- **Time Complexity:** $O(M \times N)$ — Fixed 8 neighbor lookups per cell across two passes.
- **Space Complexity:** $O(1)$ in-place — No extra arrays allocated.
