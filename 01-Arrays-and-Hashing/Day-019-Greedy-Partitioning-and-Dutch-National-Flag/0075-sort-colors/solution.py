"""
LeetCode 75: Sort Colors
Difficulty: Medium
Topic: Arrays & Two Pointers / Dutch National Flag

Pattern: Dijkstra's Dutch National Flag (3-Way In-Place Partitioning)
We partition the array into 4 contiguous regions using three pointers (low, mid, high):
  1. nums[0 .. low - 1]:       All 0s (Red)
  2. nums[low .. mid - 1]:     All 1s (White)
  3. nums[mid .. high]:        Unexamined elements
  4. nums[high + 1 .. n - 1]:  All 2s (Blue)

State Transitions:
While mid <= high:
  - If nums[mid] == 0:
      Swap nums[low] and nums[mid].
      low += 1, mid += 1
  - If nums[mid] == 1:
      mid += 1 (element is already in the 1s zone).
  - If nums[mid] == 2:
      Swap nums[mid] and nums[high].
      high -= 1 (do NOT increment mid, because the swapped element from high is uninspected).

Time Complexity: O(N) — each element is examined at most twice in a single pass.
Space Complexity: O(1) — strictly in-place.
"""

from typing import List


class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        low = 0
        mid = 0
        high = len(nums) - 1
        
        while mid <= high:
            if nums[mid] == 0:
                nums[low], nums[mid] = nums[mid], nums[low]
                low += 1
                mid += 1
            elif nums[mid] == 1:
                mid += 1
            else:
                nums[mid], nums[high] = nums[high], nums[mid]
                high -= 1


if __name__ == "__main__":
    solver = Solution()
    
    # Test Case 1: Standard mixed colors
    arr1 = [2, 0, 2, 1, 1, 0]
    solver.sortColors(arr1)
    print("Test 1 Result:", arr1)  # Expected: [0, 0, 1, 1, 2, 2]
    
    # Test Case 2: Array of two colors
    arr2 = [2, 0, 1]
    solver.sortColors(arr2)
    print("Test 2 Result:", arr2)  # Expected: [0, 1, 2]
    
    # Test Case 3: Single element
    arr3 = [0]
    solver.sortColors(arr3)
    print("Test 3 Result:", arr3)  # Expected: [0]
    
    # Test Case 4: Already sorted
    arr4 = [0, 0, 1, 1, 2, 2]
    solver.sortColors(arr4)
    print("Test 4 Result:", arr4)  # Expected: [0, 0, 1, 1, 2, 2]
