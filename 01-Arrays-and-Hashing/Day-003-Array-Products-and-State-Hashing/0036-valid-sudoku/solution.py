"""
LeetCode #36: Valid Sudoku
Difficulty: Medium
Topic: Arrays & Hashing
Pattern: Matrix State Hashing (Row, Column, and Sub-box Set Membership)
Link: https://leetcode.com/problems/valid-sudoku/

Problem Statement:
Determine if a 9 x 9 Sudoku board is valid. Only the filled cells need to be validated
according to the following rules:
1. Each row must contain the digits 1-9 without repetition.
2. Each column must contain the digits 1-9 without repetition.
3. Each of the nine 3 x 3 sub-boxes of the grid must contain the digits 1-9 without repetition.

Note:
- A Sudoku board (partially filled) could be valid but is not necessarily solvable.
- Only the filled cells need to be validated according to the mentioned rules.
"""

from collections import defaultdict
from typing import List


class Solution:

    # ==========================================
    # Approach 1: 3 Hash Sets (Rows, Cols, 3x3 Boxes)
    # Box Index Formula: (r // 3) * 3 + (c // 3) or (r // 3, c // 3)
    # Time Complexity: O(1) - fixed 9x9 = 81 cells
    # Space Complexity: O(1) - max 81 elements stored across sets
    # ==========================================
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = defaultdict(set)
        cols = defaultdict(set)
        boxes = defaultdict(set)

        for r in range(9):
            for c in range(9):
                val = board[r][c]
                if val == ".":
                    continue

                # Check if val already seen in current row, column, or 3x3 box
                box_key = (r // 3, c // 3)
                if val in rows[r] or val in cols[c] or val in boxes[box_key]:
                    return False

                rows[r].add(val)
                cols[c].add(val)
                boxes[box_key].add(val)

        return True

    # ==========================================
    # Approach 2: Bitmask Encoding (Zero Allocation O(1) Memory)
    # Uses a single integer's bits (1 << val) as a 9-bit bitmask
    # ==========================================
    def isValidSudokuBitmask(self, board: List[List[str]]) -> bool:
        rows = [0] * 9
        cols = [0] * 9
        boxes = [0] * 9

        for r in range(9):
            for c in range(9):
                val = board[r][c]
                if val == ".":
                    continue

                digit_bit = 1 << int(val)
                box_idx = (r // 3) * 3 + (c // 3)

                # Check if bit already set
                if (rows[r] & digit_bit) or (cols[c] & digit_bit) or (boxes[box_idx] & digit_bit):
                    return False

                rows[r] |= digit_bit
                cols[c] |= digit_bit
                boxes[box_idx] |= digit_bit

        return True


# Local Test Verification
if __name__ == "__main__":
    solver = Solution()

    board1 = [
        ["5","3",".",".","7",".",".",".","."],
        ["6",".",".","1","9","5",".",".","."],
        [".","9","8",".",".",".",".","6","."],
        ["8",".",".",".","6",".",".",".","3"],
        ["4",".",".","8",".","3",".",".","1"],
        ["7",".",".",".","2",".",".",".","6"],
        [".","6",".",".",".",".","2","8","."],
        [".",".",".","4","1","9",".",".","5"],
        [".",".",".",".","8",".",".","7","9"]
    ]
    assert solver.isValidSudoku(board1) is True, "Test 1 failed"

    # Test 2: Invalid duplicate '8' in top-left box
    board2 = [
        ["8","3",".",".","7",".",".",".","."],
        ["6",".",".","1","9","5",".",".","."],
        [".","9","8",".",".",".",".","6","."],
        ["8",".",".",".","6",".",".",".","3"],
        ["4",".",".","8",".","3",".",".","1"],
        ["7",".",".",".","2",".",".",".","6"],
        [".","6",".",".",".",".","2","8","."],
        [".",".",".","4","1","9",".",".","5"],
        [".",".",".",".","8",".",".","7","9"]
    ]
    assert solver.isValidSudoku(board2) is False, "Test 2 failed"

    print("All tests passed for LeetCode #36: Valid Sudoku!")
