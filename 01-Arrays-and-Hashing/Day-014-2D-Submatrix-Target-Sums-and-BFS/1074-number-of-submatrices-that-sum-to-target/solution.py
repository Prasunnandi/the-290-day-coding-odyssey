"""
LeetCode 1074: Number of Submatrices That Sum to Target
Difficulty: Hard
Topic: Matrix & Prefix Sums (Hash Map)

Pattern: 2D-to-1D Dimension Reduction (Subarray Sum Equals K Extension)
A naive brute force over all 4 boundaries (r1, c1, r2, c2) takes O(M^2 * N^2).

Dimension Reduction:
1. Compute horizontal prefix sums across each row:
   row_prefix[r][c] = sum of elements in matrix[r][0..c]
2. Fix column boundaries c1 and c2 where 0 <= c1 <= c2 < n:
   For any row r, the sum of elements between column c1 and c2 is:
     row_slice_sum(r) = matrix[r][c2] - (matrix[r][c1 - 1] if c1 > 0 else 0)
3. For fixed (c1, c2), the problem reduces identically to 1D LeetCode 560:
   Find the number of contiguous row segments summing to target using a prefix sum frequency hash map!

Time Complexity: O(N^2 * M) — where N is columns, M is rows.
Space Complexity: O(M) auxiliary space for the prefix frequency map.
"""

from collections import defaultdict
from typing import List


class Solution:
    def numSubmatrixSumTarget(self, matrix: List[List[int]], target: int) -> int:
        """
        Returns the number of non-empty submatrices summing to target.
        
        Args:
            matrix: List[List[int]], 2D integer matrix
            target: int, target sum
            
        Returns:
            int, count of matching submatrices
        """
        m, n = len(matrix), len(matrix[0])
        
        # Step 1: In-place row prefix sums
        for r in range(m):
            for c in range(1, n):
                matrix[r][c] += matrix[r][c - 1]
                
        count = 0
        
        # Step 2: Iterate over all pairs of column boundaries (c1, c2)
        for c1 in range(n):
            for c2 in range(c1, n):
                # 1D Subarray Sum Equals Target on collapsed column slices
                prefix_map = defaultdict(int)
                prefix_map[0] = 1
                curr_sum = 0
                
                for r in range(m):
                    # Sum of matrix[r][c1..c2]
                    row_sum = matrix[r][c2] - (matrix[r][c1 - 1] if c1 > 0 else 0)
                    curr_sum += row_sum
                    
                    # If (curr_sum - target) exists in prefix_map, matching submatrix exists
                    count += prefix_map[curr_sum - target]
                    prefix_map[curr_sum] += 1
                    
        return count


if __name__ == "__main__":
    solver = Solution()
    
    # Test Case 1: Simple 3x3 matrix
    mat1 = [
        [0, 1, 0],
        [1, 1, 1],
        [0, 1, 0]
    ]
    print("Test 1 Result:", solver.numSubmatrixSumTarget(mat1, 0))  # Expected: 4
    
    # Test Case 2: Uniform 2x2
    mat2 = [
        [1, -1],
        [-1, 1]
    ]
    print("Test 2 Result:", solver.numSubmatrixSumTarget(mat2, 0))  # Expected: 5
    
    # Test Case 3: Single element target match
    mat3 = [[904]]
    print("Test 3 Result:", solver.numSubmatrixSumTarget(mat3, 0))  # Expected: 0
