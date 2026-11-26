"""
LeetCode 566: Reshape the Matrix
Difficulty: Easy
Topic: Arrays & Matrix

Pattern: 1D Index Linear Mapping
Any 2D matrix of dimensions (m x n) can be conceptually flattened to a 1D sequence of length (m * n).
For any 1D index i in [0, m * n - 1]:
  - Original 2D coordinates: row = i // n, col = i % n
  - Reshaped 2D coordinates (r x c): new_row = i // c, new_col = i % c

Time Complexity: O(m * n)
Space Complexity: O(1) auxiliary space (excluding result matrix)
"""

from typing import List


class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        """
        Reshapes an m x n matrix into an r x c matrix if total elements match.
        
        Args:
            mat: List[List[int]], original 2D matrix
            r: int, target row count
            c: int, target column count
            
        Returns:
            List[List[int]], reshaped matrix or original mat if invalid dimensions
        """
        m, n = len(mat), len(mat[0])
        
        # Check legality: total number of cells must be identical
        if m * n != r * c:
            return mat
        
        # Initialize target matrix of size r x c
        result = [[0] * c for _ in range(r)]
        
        total_elements = m * n
        for i in range(total_elements):
            orig_row, orig_col = i // n, i % n
            new_row, new_col = i // c, i % c
            result[new_row][new_col] = mat[orig_row][orig_col]
            
        return result


if __name__ == "__main__":
    solver = Solution()
    
    # Test Case 1: Standard legal reshape (2x2 -> 1x4)
    mat1 = [[1, 2], [3, 4]]
    r1, c1 = 1, 4
    print("Test 1 Result:", solver.matrixReshape(mat1, r1, c1))  # Expected: [[1, 2, 3, 4]]
    
    # Test Case 2: Illegal reshape (2x2 -> 2x4)
    mat2 = [[1, 2], [3, 4]]
    r2, c2 = 2, 4
    print("Test 2 Result:", solver.matrixReshape(mat2, r2, c2))  # Expected: [[1, 2], [3, 4]]
    
    # Test Case 3: Identity reshape
    mat3 = [[1, 2, 3], [4, 5, 6]]
    r3, c3 = 3, 2
    print("Test 3 Result:", solver.matrixReshape(mat3, r3, c3))  # Expected: [[1, 2], [3, 4], [5, 6]]
