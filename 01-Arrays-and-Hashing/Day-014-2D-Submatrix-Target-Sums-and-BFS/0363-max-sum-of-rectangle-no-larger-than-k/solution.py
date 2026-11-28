"""
LeetCode 363: Max Sum of Rectangle No Larger Than K
Difficulty: Hard
Topic: Matrix & Binary Search / Sorted List

Pattern: 2D-to-1D Dimension Reduction with Binary Search Prefix Matching
To find max submatrix sum <= k:
1. Orient matrix so the outer loop iterates over the smaller dimension:
   - If rows < cols, fix row pairs (r1, r2) and search along columns.
   - Else, fix column pairs (c1, c2) and search along rows.
2. In the collapsed 1D array of slice sums:
   - Let P be running prefix sum.
   - For a subarray sum P[j] - P[i] <= k:
       P[i] >= P[j] - k
   - To maximize (P[j] - P[i]), we must MINIMIZE P[i].
   - Thus, we query the smallest prefix sum >= (P[j] - k) using binary search (bisect_left).

Time Complexity: O(min(M, N)^2 * max(M, N) * log(max(M, N)))
Space Complexity: O(max(M, N))
"""

import bisect
from typing import List


class Solution:
    def maxSumSubmatrix(self, matrix: List[List[int]], k: int) -> int:
        """
        Finds the maximum sum of a rectangle no larger than k.
        
        Args:
            matrix: List[List[int]], 2D integer matrix
            k: int, upper bound sum
            
        Returns:
            int, maximal sum <= k
        """
        m, n = len(matrix), len(matrix[0])
        max_sum = float("-inf")
        
        # Optimize orientation: ensure outer pair loop iterates over fewer elements
        if m > n:
            # More rows than cols: fix column pairs c1, c2
            for c1 in range(n):
                row_sums = [0] * m
                for c2 in range(c1, n):
                    for r in range(m):
                        row_sums[r] += matrix[r][c2]
                        
                    # 1D Best Subarray Sum <= k
                    curr_max = self._maxSubArrayNoLargerThanK(row_sums, k)
                    max_sum = max(max_sum, curr_max)
                    if max_sum == k:
                        return k
        else:
            # More cols than rows: fix row pairs r1, r2
            for r1 in range(m):
                col_sums = [0] * n
                for r2 in range(r1, m):
                    for c in range(n):
                        col_sums[c] += matrix[r2][c]
                        
                    curr_max = self._maxSubArrayNoLargerThanK(col_sums, k)
                    max_sum = max(max_sum, curr_max)
                    if max_sum == k:
                        return k
                        
        return max_sum

    def _maxSubArrayNoLargerThanK(self, arr: List[int], k: int) -> int:
        """
        1D Helper: finds maximum contiguous subarray sum <= k using bisect.
        """
        seen_prefix = [0]
        curr = 0
        best = float("-inf")
        
        for val in arr:
            curr += val
            # Find smallest prefix in seen_prefix >= curr - k
            target = curr - k
            idx = bisect.bisect_left(seen_prefix, target)
            
            if idx < len(seen_prefix):
                best = max(best, curr - seen_prefix[idx])
                if best == k:
                    return k
                    
            bisect.insort(seen_prefix, curr)
            
        return best


if __name__ == "__main__":
    solver = Solution()
    
    # Test Case 1: Standard rectangle
    mat1 = [[1, 0, 1], [0, -2, 3]]
    k1 = 2
    print("Test 1 Result:", solver.maxSumSubmatrix(mat1, k1))  # Expected: 2
    
    # Test Case 2: Negative target
    mat2 = [[2, 2, -1]]
    k2 = 3
    print("Test 2 Result:", solver.maxSumSubmatrix(mat2, k2))  # Expected: 3
    
    # Test Case 3: Exact match
    mat3 = [[2, 2, -1]]
    k3 = 0
    print("Test 3 Result:", solver.maxSumSubmatrix(mat3, k3))  # Expected: -1
