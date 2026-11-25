"""
LeetCode #54: Spiral Matrix
Difficulty: Medium
Topic: Arrays & Hashing
Pattern: 4-Boundary Shrinking Matrix Simulation (Top, Bottom, Left, Right)
Link: https://leetcode.com/problems/spiral-matrix/

Problem Statement:
Given an m x n matrix, return all elements of the matrix in spiral order.
"""

from typing import List


class Solution:

    # ==========================================
    # Approach: 4 Boundary Pointers Simulation
    # Pointers: top = 0, bottom = m - 1, left = 0, right = n - 1
    # 4 Traversal Steps in each layer:
    # 1. Left -> Right along 'top' row, then top += 1
    # 2. Top -> Bottom along 'right' col, then right -= 1
    # 3. Right -> Left along 'bottom' row (if top <= bottom), then bottom -= 1
    # 4. Bottom -> Top along 'left' col (if left <= right), then left += 1
    # Time Complexity: O(M * N)
    # Space Complexity: O(1) auxiliary (excluding output array)
    # ==========================================
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        result = []
        if not matrix or not matrix[0]:
            return result

        top, bottom = 0, len(matrix) - 1
        left, right = 0, len(matrix[0]) - 1

        while top <= bottom and left <= right:
            # 1. Traverse Right across the top boundary
            for c in range(left, right + 1):
                result.append(matrix[top][c])
            top += 1

            # 2. Traverse Down along the right boundary
            for r in range(top, bottom + 1):
                result.append(matrix[r][right])
            right -= 1

            # 3. Traverse Left across the bottom boundary (check valid bounds)
            if top <= bottom:
                for c in range(right, left - 1, -1):
                    result.append(matrix[bottom][c])
                bottom -= 1

            # 4. Traverse Up along the left boundary (check valid bounds)
            if left <= right:
                for r in range(bottom, top - 1, -1):
                    result.append(matrix[r][left])
                left += 1

        return result


# Local Test Verification
if __name__ == "__main__":
    solver = Solution()

    # Test 1: 3x3
    m1 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    assert solver.spiralOrder(m1) == [1, 2, 3, 6, 9, 8, 7, 4, 5], "Test 1 failed"

    # Test 2: 3x4
    m2 = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]
    assert solver.spiralOrder(m2) == [1, 2, 3, 4, 8, 12, 11, 10, 9, 5, 6, 7], "Test 2 failed"

    print("All tests passed for LeetCode #54: Spiral Matrix!")
