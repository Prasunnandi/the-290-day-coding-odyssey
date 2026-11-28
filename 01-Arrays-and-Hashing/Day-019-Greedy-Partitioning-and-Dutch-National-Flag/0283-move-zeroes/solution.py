"""
LeetCode 283: Move Zeroes
Difficulty: Easy
Topic: Arrays & Two Pointers

Pattern: Slow/Fast Pointer In-Place Compaction
Maintain two pointers:
  - slow: Points to the boundary where the next non-zero element should be placed.
  - fast: Explores the array from left to right.

Whenever nums[fast] is non-zero:
  Swap nums[slow] and nums[fast] and increment slow.
  
Properties:
- All non-zero elements preserve their relative order.
- All zeroes are displaced to the tail.
- Achieves optimal number of writes when nums[slow] == nums[fast] (self-swap / no-op).

Time Complexity: O(N) — single pass.
Space Complexity: O(1) — strictly in-place.
"""

from typing import List


class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        slow = 0
        for fast in range(len(nums)):
            if nums[fast] != 0:
                nums[slow], nums[fast] = nums[fast], nums[slow]
                slow += 1


if __name__ == "__main__":
    solver = Solution()
    
    # Test Case 1: Standard mixed array
    arr1 = [0, 1, 0, 3, 12]
    solver.moveZeroes(arr1)
    print("Test 1 Result:", arr1)  # Expected: [1, 3, 12, 0, 0]
    
    # Test Case 2: Single zero
    arr2 = [0]
    solver.moveZeroes(arr2)
    print("Test 2 Result:", arr2)  # Expected: [0]
    
    # Test Case 3: No zeroes
    arr3 = [1, 2, 3]
    solver.moveZeroes(arr3)
    print("Test 3 Result:", arr3)  # Expected: [1, 2, 3]
