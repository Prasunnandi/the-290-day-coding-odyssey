"""
LeetCode 713: Subarray Product Less Than K
Difficulty: Medium
Topic: Arrays & Sliding Window

Pattern: Dynamic Sliding Window (Contiguous Subarray Counting)
Since all numbers in nums are strictly positive (nums[i] >= 1):
  - Expanding the right pointer monotonically increases the window product.
  - Shrinking the left pointer monotonically decreases the window product.

Counting Invariant:
For a valid window [left, right] where product < k:
The number of valid subarrays ending at `right` is exactly:
  (right - left + 1)
These correspond to: nums[right], nums[right-1..right], ..., nums[left..right].

Edge Case:
If k <= 1, no positive product can be strictly less than k -> return 0.

Time Complexity: O(N) — left and right pointers traverse the array at most once.
Space Complexity: O(1) — constant auxiliary space.
"""

from typing import List


class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        """
        Calculates the number of contiguous subarrays with product strictly less than k.
        
        Args:
            nums: List[int], positive integer array
            k: int, product upper bound
            
        Returns:
            int, total count of valid subarrays
        """
        if k <= 1:
            return 0
            
        prod = 1
        left = 0
        total_subarrays = 0
        
        for right in range(len(nums)):
            prod *= nums[right]
            
            # Shrink window until prod < k
            while prod >= k and left <= right:
                prod /= nums[left]
                left += 1
                
            # Number of subarrays ending at right is (right - left + 1)
            total_subarrays += (right - left + 1)
            
        return total_subarrays


if __name__ == "__main__":
    solver = Solution()
    
    # Test Case 1: Standard case
    test1_nums = [10, 5, 2, 6]
    test1_k = 100
    print("Test 1 Result:", solver.numSubarrayProductLessThanK(test1_nums, test1_k))  # Expected: 8
    
    # Test Case 2: Boundary k <= 1
    test2_nums = [1, 2, 3]
    test2_k = 0
    print("Test 2 Result:", solver.numSubarrayProductLessThanK(test2_nums, test2_k))  # Expected: 0
    
    # Test Case 3: All elements larger than k
    test3_nums = [5, 6, 7]
    test3_k = 2
    print("Test 3 Result:", solver.numSubarrayProductLessThanK(test3_nums, test3_k))  # Expected: 0
