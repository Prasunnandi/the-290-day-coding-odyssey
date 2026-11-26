"""
LeetCode #289: Game of Life
Difficulty: Medium
Topic: Arrays & Hashing
Pattern: Cellular Automata In-Place State Encoding (2-Bit Transition Modeling)
Link: https://leetcode.com/problems/game-of-life/

Problem Statement:
According to Conway's Game of Life:
1. Any live cell with fewer than two live neighbors dies (under-population).
2. Any live cell with two or three live neighbors lives on to the next generation.
3. Any live cell with more than three live neighbors dies (over-population).
4. Any dead cell with exactly three live neighbors becomes a live cell (reproduction).

The next state is created by applying the above rules simultaneously to every cell.
Follow-up: Could you solve it in-place without creating a copy of the board?
"""

from typing import List


class Solution:

    # ==========================================
    # Approach: In-Place State Transition Encoding
    # In-place 2-state mapping:
    # 0 -> 0 (dead stays dead)     : encode as 0
    # 1 -> 1 (live stays live)     : encode as 1
    # 1 -> 0 (live dies)           : encode as -1
    # 0 -> 1 (dead becomes live)   : encode as 2
    #
    # Original state checking:
    # A cell was originally LIVE if abs(board[r][c]) == 1 (i.e. 1 or -1).
    # In final pass: cells with value > 0 become 1; cells <= 0 become 0.
    # Time Complexity: O(M * N)
    # Space Complexity: O(1) in-place
    # ==========================================
    def gameOfLife(self, board: List[List[int]]) -> None:
        """Do not return anything, modify board in-place instead."""
        m, n = len(board), len(board[0])
        directions = [(-1,-1), (-1,0), (-1,1), (0,-1), (0,1), (1,-1), (1,0), (1,1)]

        # Pass 1: Encode state transitions
        for r in range(m):
            for c in range(n):
                live_neighbors = 0
                for dr, dc in directions:
                    nr, nc = r + dr, c + dc
                    if 0 <= nr < m and 0 <= nc < n:
                        # Check original state: abs(value) == 1 means originally alive
                        if abs(board[nr][nc]) == 1:
                            live_neighbors += 1

                # Rule 1 & 3: Live cell dies
                if board[r][c] == 1 and (live_neighbors < 2 or live_neighbors > 3):
                    board[r][c] = -1
                # Rule 4: Dead cell becomes alive
                elif board[r][c] == 0 and live_neighbors == 3:
                    board[r][c] = 2

        # Pass 2: Finalize to binary states (0 or 1)
        for r in range(m):
            for c in range(n):
                board[r][c] = 1 if board[r][c] > 0 else 0


# Local Test Verification
if __name__ == "__main__":
    solver = Solution()

    b1 = [[0,1,0],[0,0,1],[1,1,1],[0,0,0]]
    solver.gameOfLife(b1)
    expected1 = [[0,0,0],[1,0,1],[0,1,1],[0,1,0]]
    assert b1 == expected1, f"Test 1 failed: {b1}"

    print("All tests passed for LeetCode #289: Game of Life!")
