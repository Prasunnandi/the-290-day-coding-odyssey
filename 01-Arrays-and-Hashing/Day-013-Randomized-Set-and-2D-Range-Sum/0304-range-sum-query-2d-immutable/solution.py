"""
LeetCode 304: Range Sum Query 2D - Immutable
Difficulty: Medium
Topic: Arrays & 2D Prefix Sums

Pattern: Inclusion-Exclusion Principle (2D Prefix Sums)
We precompute a prefix sum matrix P of size (m + 1) x (n + 1), where:
  P[r + 1][c + 1] = sum of elements in rectangle from (0, 0) to (r, c).

Recurrence for Construction:
  P[r + 1][c + 1] = matrix[r][c] + P[r][c + 1] + P[r + 1][c] - P[r][c]

Recurrence for O(1) Region Sum Query:
Given top-left (r1, c1) and bottom-right (r2, c2):
  Total = P[r2 + 1][c2 + 1]
        - P[r1][c2 + 1]       (subtract region above)
        - P[r2 + 1][c1]       (subtract region to the left)
        + P[r1][c1]           (add back double-subtracted top-left overlap)

Time Complexity:
  - Construction: O(M * N)
  - Query: O(1)
Space Complexity: O(M * N) for the prefix table.
"""

from typing import List


class NumMatrix:
    def __init__(self, matrix: List[List[int]]):
        """
        Initializes 2D prefix sum table with 1-based indexing padding.
        """
        if not matrix or not matrix[0]:
            return
            
        m, n = len(matrix), len(matrix[0])
        self.P = [[0] * (n + 1) for _ in range(m + 1)]
        
        for r in range(m):
            for c in range(n):
                self.P[r + 1][c + 1] = (
                    matrix[r][c]
                    + self.P[r][c + 1]
                    + self.P[r + 1][c]
                    - self.P[r][c]
                )

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        """
        Returns the rectangle sum in O(1) time using inclusion-exclusion.
        """
        return (
            self.P[row2 + 1][col2 + 1]
            - self.P[row1][col2 + 1]
            - self.P[row2 + 1][col1]
            + self.P[row1][col1]
        )


if __name__ == "__main__":
    mat = [
        [3, 0, 1, 4, 2],
        [5, 6, 3, 2, 1],
        [1, 2, 0, 1, 5],
        [4, 1, 0, 1, 7],
        [1, 0, 3, 0, 5]
    ]
    nm = NumMatrix(mat)
    print("Test 1 Result:", nm.sumRegion(2, 1, 4, 3))  # Expected: 8
    print("Test 2 Result:", nm.sumRegion(1, 1, 2, 2))  # Expected: 11
    print("Test 3 Result:", nm.sumRegion(1, 2, 2, 4))  # Expected: 12
