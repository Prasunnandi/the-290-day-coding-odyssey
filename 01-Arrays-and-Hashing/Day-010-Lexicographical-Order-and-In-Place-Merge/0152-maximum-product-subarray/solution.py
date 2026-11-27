"""
LeetCode 152: Maximum Product Subarray
Difficulty: Medium
Topic: Arrays & Dynamic Programming

Pattern: Dual-Extrema Tracking (Min-Max Product DP)
Unlike maximum sum (Kadane's), multiplying by a negative number reverses the polarity:
  - A very large positive number becomes a very small negative number.
  - A very small negative number becomes a very large positive number.

Therefore, at each position i, we maintain BOTH:
  1. max_prod: Maximum contiguous product ending at index i
  2. min_prod: Minimum contiguous product ending at index i

When nums[i] < 0, max_prod and min_prod swap roles before computation.

Time Complexity: O(N) — single linear pass.
Space Complexity: O(1) — constant auxiliary variables.
"""

from typing import List


class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        """
        Finds the contiguous subarray with the largest product.
        
        Args:
            nums: List[int], array of integers
            
        Returns:
            int, maximum product
        """
        if not nums:
            return 0
            
        max_prod = nums[0]
        min_prod = nums[0]
        result = nums[0]
        
        for num in nums[1:]:
            # If current number is negative, swapping max and min handles polarity inversion
            if num < 0:
                max_prod, min_prod = min_prod, max_prod
                
            # Choice: extend previous subarray or start fresh at num
            max_prod = max(num, max_prod * num)
            min_prod = min(num, min_prod * num)
            
            result = max(result, max_prod)
            
        return result


if __name__ == "__main__":
    solver = Solution()
    
    # Test Case 1: Standard positive product subarray
    test1 = [2, 3, -2, 4]
    print("Test 1 Result:", solver.maxProduct(test1))  # Expected: 6 ([2, 3])
    
    # Test Case 2: Negative product turns positive
    test2 = [-2, 0, -1]
    print("Test 2 Result:", solver.maxProduct(test2))  # Expected: 0
    
    # Test Case 3: Double negative amplification
    test3 = [-2, 3, -4]
    print("Test 3 Result:", solver.maxProduct(test3))  # Expected: 24 ([-2, 3, -4])
    
    # Test Case 4: Single negative number
    test4 = [-2]
    print("Test 4 Result:", solver.maxProduct(test4))  # Expected: -2
