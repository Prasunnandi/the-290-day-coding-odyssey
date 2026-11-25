"""
LeetCode #73: Set Matrix Zeroes
Difficulty: Medium
Topic: Arrays & Hashing
Pattern: In-Place Matrix State Marking (Using 1st Row and 1st Column as Markers)
Link: https://leetcode.com/problems/set-matrix-zeroes/

Problem Statement:
Given an m x n integer matrix matrix, if an element is 0, set its entire row and column to 0's.
You must do it in place.
Follow up: Could you devise a constant space solution?
"""

from typing import List


class Solution:

    # ==========================================
    # Approach 1: O(M + N) Space using separate marker sets/arrays
    # Time Complexity: O(M * N)
    # Space Complexity: O(M + N)
    # ==========================================
    def setZeroesExtraSpace(self, matrix: List[List[int]]) -> None:
        m, n = len(matrix), len(matrix[0])
        zero_rows = set()
        zero_cols = set()

        for r in range(m):
            for c in range(n):
                if matrix[r][c] == 0:
                    zero_rows.add(r)
                    zero_cols.add(c)

        for r in range(m):
            for c in range(n):
                if r in zero_rows or c in zero_cols:
                    matrix[r][c] = 0

    # ==========================================
    # Approach 2: O(1) Extra Space In-Place Markers
    # Use matrix[r][0] and matrix[0][c] as markers!
    # Because matrix[0][0] overlaps, use a single boolean 'first_col_zero' for col 0.
    # Time Complexity: O(M * N)
    # Space Complexity: O(1)
    # ==========================================
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """Do not return anything, modify matrix in-place instead."""
        m, n = len(matrix), len(matrix[0])
        first_col_zero = False

        # Step 1: Mark rows and columns in the first row/col
        for r in range(m):
            if matrix[r][0] == 0:
                first_col_zero = True
            for c in range(1, n):
                if matrix[r][c] == 0:
                    matrix[r][0] = 0
                    matrix[0][c] = 0

        # Step 2: Use markers to set inner cells (from bottom-right or 1..m, 1..n)
        for r in range(1, m):
            for c in range(1, n):
                if matrix[r][0] == 0 or matrix[0][c] == 0:
                    matrix[r][c] = 0

        # Step 3: Handle first row if matrix[0][0] was marked
        if matrix[0][0] == 0:
            for c in range(n):
                matrix[0][c] = 0

        # Step 4: Handle first column if first_col_zero was set
        if first_col_zero:
            for r in range(m):
                matrix[r][0] = 0


# Local Test Verification
if __name__ == "__main__":
    solver = Solution()

    # Test 1
    m1 = [[1,1,1],[1,0,1],[1,1,1]]
    solver.setZeroes(m1)
    assert m1 == [[1,0,1],[0,0,0],[1,0,1]], f"Test 1 failed: {m1}"

    # Test 2
    m2 = [[0,1,2,0],[3,4,5,2],[1,3,1,5]]
    solver.setZeroes(m2)
    assert m2 == [[0,0,0,0],[0,4,5,0],[0,3,1,0]], f"Test 2 failed: {m2}"

    print("All tests passed for LeetCode #73: Set Matrix Zeroes!")
