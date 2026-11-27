"""
LeetCode 209: Minimum Size Subarray Sum
Difficulty: Medium
Topic: Arrays & Sliding Window

Pattern: Shrinking Sliding Window
All elements are strictly positive (nums[i] >= 1):
  - Adding nums[right] strictly increases the window sum.
  - Subtracting nums[left] strictly decreases the window sum.

Algorithm:
1. Expand right boundary until current_sum >= target.
2. While current_sum >= target:
   - Record current window length: right - left + 1
   - Shrink window from the left to find minimal valid length.
3. If no subarray reaches target, return 0.

Time Complexity: O(N) — each pointer advances at most N steps.
Space Complexity: O(1) — constant extra space.
"""

from typing import List


class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        """
        Finds the minimal length of a contiguous subarray with sum >= target.
        
        Args:
            target: int, threshold sum
            nums: List[int], array of positive integers
            
        Returns:
            int, minimal length or 0 if unreachable
        """
        n = len(nums)
        left = 0
        current_sum = 0
        min_len = float("inf")
        
        for right in range(n):
            current_sum += nums[right]
            
            # Contract window from the left while condition is satisfied
            while current_sum >= target:
                min_len = min(min_len, right - left + 1)
                current_sum -= nums[left]
                left += 1
                
        return min_len if min_len != float("inf") else 0


if __name__ == "__main__":
    solver = Solution()
    
    # Test Case 1: Standard case
    print("Test 1 Result:", solver.minSubArrayLen(7, [2, 3, 1, 2, 4, 3]))  # Expected: 2 ([4, 3])
    
    # Test Case 2: Exact match with single element
    print("Test 2 Result:", solver.minSubArrayLen(4, [1, 4, 4]))  # Expected: 1 ([4])
    
    # Test Case 3: Target unreachable
    print("Test 3 Result:", solver.minSubArrayLen(11, [1, 1, 1, 1, 1, 1, 1, 1]))  # Expected: 0
