"""
LeetCode 287: Find the Duplicate Number
Difficulty: Medium
Topic: Arrays & Two Pointers

Pattern: Floyd's Tortoise and Hare (Cycle Detection in Functional Graph)
Constraints:
- You must NOT modify the array nums.
- You must use only constant O(1) auxiliary space.

Mathematical Formulation:
Since nums contains n + 1 integers in range [1, n]:
Consider a directed graph where an edge exists from index i to nums[i]:
  f(i) = nums[i]
Because nums[i] in [1, n], 0 has no incoming edges (it is the entry point).
By Pigeonhole Principle, at least two distinct indices map to the same value (the duplicate).
This creates a directed cycle in the functional graph!
The duplicate number is the entry point (node with in-degree >= 2) into the cycle.

Algorithm:
1. Phase 1 (Intersection):
   slow = nums[0], fast = nums[0]
   Advance slow by 1 step (nums[slow]), fast by 2 steps (nums[nums[fast]]).
   Repeat until slow == fast.
2. Phase 2 (Cycle Entrance):
   Reset slow2 = nums[0].
   Advance slow and slow2 by 1 step each until they meet.
   The meeting point is the duplicate number!

Time Complexity: O(N)
Space Complexity: O(1) auxiliary space (read-only, does not modify nums).
"""

from typing import List


class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        """
        Finds the duplicate number in nums without modifying the array.
        
        Args:
            nums: List[int], array of n + 1 integers in [1, n]
            
        Returns:
            int, the duplicate integer
        """
        # Phase 1: Detect cycle using slow and fast pointers
        slow = nums[0]
        fast = nums[0]
        
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast:
                break
                
        # Phase 2: Find the entry point of the cycle
        slow2 = nums[0]
        while slow != slow2:
            slow = nums[slow]
            slow2 = nums[slow2]
            
        return slow


if __name__ == "__main__":
    solver = Solution()
    
    # Test Case 1: Standard duplicate
    test1 = [1, 3, 4, 2, 2]
    print("Test 1 Result:", solver.findDuplicate(test1))  # Expected: 2
    
    # Test Case 2: Duplicate appears multiple times
    test2 = [3, 1, 3, 4, 2]
    print("Test 2 Result:", solver.findDuplicate(test2))  # Expected: 3
    
    # Test Case 3: All elements identical
    test3 = [3, 3, 3, 3, 3]
    print("Test 3 Result:", solver.findDuplicate(test3))  # Expected: 3
