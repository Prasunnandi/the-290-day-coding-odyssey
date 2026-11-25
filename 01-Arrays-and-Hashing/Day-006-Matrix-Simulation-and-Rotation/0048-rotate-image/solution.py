"""
LeetCode #48: Rotate Image
Difficulty: Medium
Topic: Arrays & Hashing
Pattern: Matrix Transposition & Symmetry Reversal
Link: https://leetcode.com/problems/rotate-image/

Problem Statement:
You are given an n x n 2D matrix representing an image, rotate the image by 90 degrees (clockwise).
You have to rotate the image in-place, which means you have to modify the input 2D matrix directly.
DO NOT allocate another 2D matrix and do the rotation.
"""

from typing import List


class Solution:

    # ==========================================
    # Approach: Transpose + Reverse Each Row (Optimal O(1) Space)
    # Linear Algebra Invariant:
    # Rotating 90 degrees clockwise is equivalent to:
    # 1. Transposing the matrix (swap matrix[r][c] with matrix[c][r])
    # 2. Reversing each row horizontally
    # Time Complexity: O(N^2)
    # Space Complexity: O(1) in-place
    # ==========================================
    def rotate(self, matrix: List[List[int]]) -> None:
        """Do not return anything, modify matrix in-place instead."""
        n = len(matrix)

        # Step 1: Transpose the matrix across main diagonal
        for r in range(n):
            for c in range(r + 1, n):
                matrix[r][c], matrix[c][r] = matrix[c][r], matrix[r][c]

        # Step 2: Reverse each row horizontally
        for r in range(n):
            matrix[r].reverse()


# Local Test Verification
if __name__ == "__main__":
    solver = Solution()

    # Test 1: 3x3
    m1 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    solver.rotate(m1)
    assert m1 == [[7, 4, 1], [8, 5, 2], [9, 6, 3]], f"Test 1 failed: {m1}"

    # Test 2: 4x4
    m2 = [[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]]
    solver.rotate(m2)
    assert m2 == [[15,13,2,5],[14,3,4,1],[12,6,8,9],[16,7,10,11]], f"Test 2 failed: {m2}"

    print("All tests passed for LeetCode #48: Rotate Image!")
