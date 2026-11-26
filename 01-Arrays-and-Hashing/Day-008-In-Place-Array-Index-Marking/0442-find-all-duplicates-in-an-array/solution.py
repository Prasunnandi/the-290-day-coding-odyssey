"""
LeetCode 442: Find All Duplicates in an Array
Difficulty: Medium
Topic: Arrays & Hashing

Pattern: Sign Inversion / In-Place Frequency Flag
Given that every integer is in [1, n] and appears at most twice:
  - Each value x maps directly to index (abs(x) - 1).
  - When encountering value x for the FIRST time:
      nums[abs(x) - 1] is positive -> negate it: nums[abs(x) - 1] = -nums[abs(x) - 1]
  - When encountering value x for the SECOND time:
      nums[abs(x) - 1] is ALREADY negative -> abs(x) is a duplicate!
      append abs(x) to result.

Time Complexity: O(N) — single linear pass over the array.
Space Complexity: O(1) auxiliary space (excluding returned result list).
"""

from typing import List


class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        """
        Identifies all elements appearing twice in O(N) time and O(1) space.
        
        Args:
            nums: List[int], array of length n where 1 <= nums[i] <= n
            
        Returns:
            List[int], list of numbers that appear twice
        """
        duplicates = []
        
        for num in nums:
            val = abs(num)
            target_idx = val - 1
            
            # If the value at target_idx is already negative, val has been seen before
            if nums[target_idx] < 0:
                duplicates.append(val)
            else:
                # Mark as seen by negating the entry
                nums[target_idx] = -nums[target_idx]
                
        # Optional: Restore array to original state
        for i in range(len(nums)):
            nums[i] = abs(nums[i])
            
        return duplicates


if __name__ == "__main__":
    solver = Solution()
    
    # Test Case 1: Standard duplicates
    test1 = [4, 3, 2, 7, 8, 2, 3, 1]
    print("Test 1 Result:", solver.findDuplicates(test1))  # Expected: [2, 3]
    
    # Test Case 2: Array with pair duplicates
    test2 = [1, 1, 2]
    print("Test 2 Result:", solver.findDuplicates(test2))  # Expected: [1]
    
    # Test Case 3: No duplicates
    test3 = [1]
    print("Test 3 Result:", solver.findDuplicates(test3))  # Expected: []
