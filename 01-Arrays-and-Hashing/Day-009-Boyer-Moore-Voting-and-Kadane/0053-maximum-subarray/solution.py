"""
LeetCode 53: Maximum Subarray
Difficulty: Medium
Topic: Arrays & Dynamic Programming

Pattern: Kadane's Algorithm / Running Local Optimum
At each index i, we make a local decision:
  Should we extend the previous contiguous subarray, or start a fresh subarray at nums[i]?
  current_max = max(nums[i], current_max + nums[i])
  global_max = max(global_max, current_max)

Invariants:
- If current_max drops below 0, any subsequent element is better off starting a new subarray on its own.
- Correctly handles arrays containing entirely negative numbers.

Time Complexity: O(N) — single pass.
Space Complexity: O(1) — constant extra space.
"""

from typing import List


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        """
        Finds the maximum subarray sum using Kadane's Algorithm.
        
        Args:
            nums: List[int], list of integers
            
        Returns:
            int, maximum contiguous subarray sum
        """
        current_max = nums[0]
        global_max = nums[0]
        
        for num in nums[1:]:
            # Extend subarray or restart at current number
            current_max = max(num, current_max + num)
            global_max = max(global_max, current_max)
            
        return global_max


if __name__ == "__main__":
    solver = Solution()
    
    # Test Case 1: Standard mixed array
    test1 = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
    print("Test 1 Result:", solver.maxSubArray(test1))  # Expected: 6 ([4, -1, 2, 1])
    
    # Test Case 2: Single element
    test2 = [1]
    print("Test 2 Result:", solver.maxSubArray(test2))  # Expected: 1
    
    # Test Case 3: All negative elements
    test3 = [-5, -2, -8, -1, -4]
    print("Test 3 Result:", solver.maxSubArray(test3))  # Expected: -1 ([-1])
    
    # Test Case 4: All positive elements
    test4 = [5, 4, 1, 7, 8]
    print("Test 4 Result:", solver.maxSubArray(test4))  # Expected: 25
