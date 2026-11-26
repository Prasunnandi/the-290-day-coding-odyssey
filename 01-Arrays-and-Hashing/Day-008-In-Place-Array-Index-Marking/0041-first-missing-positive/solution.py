"""
LeetCode 41: First Missing Positive
Difficulty: Hard
Topic: Arrays & Hashing

Pattern: Cyclic Sort / In-Place Index Mapping
Given an array of length n, the first missing positive integer MUST be in the range [1, n + 1].
- If numbers 1 through n are all present, the answer is n + 1.
- Otherwise, at least one number in [1, n] is missing.

Algorithm (Cyclic Sort):
1. Traverse the array. For each element x = nums[i]:
   If 1 <= x <= n and nums[x - 1] != x:
       swap(nums[i], nums[x - 1])
   Repeat until nums[i] is at the correct index, out of bounds, or a duplicate.
2. Scan from index 0 to n - 1:
   The first index i where nums[i] != i + 1 corresponds to missing integer i + 1.
3. If all indices match, return n + 1.

Time Complexity: O(N) — each number is swapped into its correct place at most once.
Space Complexity: O(1) — strictly in-place modifications without auxiliary data structures.
"""

from typing import List


class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        """
        Finds the smallest missing positive integer in O(N) time and O(1) auxiliary space.
        
        Args:
            nums: List[int], unsorted list of integers
            
        Returns:
            int, the smallest missing positive integer
        """
        n = len(nums)
        
        # Step 1: Place each number in its target index (x belongs at index x - 1)
        for i in range(n):
            while 1 <= nums[i] <= n and nums[nums[i] - 1] != nums[i]:
                # Swap nums[i] with nums[target_idx]
                target_idx = nums[i] - 1
                nums[i], nums[target_idx] = nums[target_idx], nums[i]
                
        # Step 2: Identify the first index where nums[i] != i + 1
        for i in range(n):
            if nums[i] != i + 1:
                return i + 1
                
        # If 1 to n are all present
        return n + 1


if __name__ == "__main__":
    solver = Solution()
    
    # Test Case 1: Standard out-of-order positive numbers
    test1 = [1, 2, 0]
    print("Test 1 Result:", solver.firstMissingPositive(test1))  # Expected: 3
    
    # Test Case 2: Array with gaps and duplicates
    test2 = [3, 4, -1, 1]
    print("Test 2 Result:", solver.firstMissingPositive(test2))  # Expected: 2
    
    # Test Case 3: Complete contiguous sequence from 1 to n
    test3 = [7, 8, 9, 11, 12]
    print("Test 3 Result:", solver.firstMissingPositive(test3))  # Expected: 1
    
    # Test Case 4: Complete sequence 1..4
    test4 = [1, 2, 3, 4]
    print("Test 4 Result:", solver.firstMissingPositive(test4))  # Expected: 5
