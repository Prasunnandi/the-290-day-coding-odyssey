"""
LeetCode 1004: Max Consecutive Ones III
Difficulty: Medium
Topic: Arrays & Sliding Window

Pattern: Sliding Window with Resource Budget (Flip Quota)
The problem is equivalent to:
  "Find the longest contiguous subarray containing AT MOST k zeroes."

Algorithm:
1. Maintain window [left, right] and a counter zero_count.
2. Advance right pointer:
   - If nums[right] == 0, increment zero_count.
3. If zero_count > k, contract left pointer until zero_count <= k:
   - If nums[left] == 0, decrement zero_count.
   - Advance left.
4. Track max window size: max_len = max(max_len, right - left + 1).

Time Complexity: O(N) — each element is entered and exited at most once.
Space Complexity: O(1) — constant extra space.
"""

from typing import List


class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        """
        Returns the maximum consecutive 1s achievable with at most k flips.
        
        Args:
            nums: List[int], binary array
            k: int, maximum zeroes allowed to flip
            
        Returns:
            int, length of longest consecutive 1s subarray
        """
        left = 0
        zero_count = 0
        max_len = 0
        
        for right in range(len(nums)):
            if nums[right] == 0:
                zero_count += 1
                
            # If zeroes exceed budget k, shrink window from left
            while zero_count > k:
                if nums[left] == 0:
                    zero_count -= 1
                left += 1
                
            max_len = max(max_len, right - left + 1)
            
        return max_len


if __name__ == "__main__":
    solver = Solution()
    
    # Test Case 1: Standard case
    test1 = [1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 0]
    print("Test 1 Result:", solver.longestOnes(test1, 2))  # Expected: 6
    
    # Test Case 2: Larger array with more flips
    test2 = [0, 0, 1, 1, 0, 0, 1, 1, 1, 0, 1, 1, 0, 0, 0, 1, 1, 1, 1]
    print("Test 2 Result:", solver.longestOnes(test2, 3))  # Expected: 10
    
    # Test Case 3: Zero flips allowed
    test3 = [1, 1, 0, 1, 1, 1]
    print("Test 3 Result:", solver.longestOnes(test3, 0))  # Expected: 3
