"""
LeetCode 448: Find All Numbers Disappeared in an Array
Difficulty: Easy
Topic: Arrays & Hashing

Pattern: Sign Inversion / In-Place Index Marking
Since all numbers are in the range [1, n], each value x corresponds to an index (x - 1).
We can use the sign of the value at nums[abs(x) - 1] as a presence flag:
  - When encountering value x, mark index (abs(x) - 1) as visited by setting nums[abs(x) - 1] to negative.
  - In a second pass, any index i where nums[i] remains positive was never visited.
  - Thus, (i + 1) is a disappeared number.

Time Complexity: O(N) — two linear passes over nums.
Space Complexity: O(1) auxiliary space — modifies input array in-place.
"""

from typing import List


class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        """
        Finds all numbers in range [1, n] absent from nums.
        
        Args:
            nums: List[int], array of length n with values in [1, n]
            
        Returns:
            List[int], list of missing integers
        """
        n = len(nums)
        
        # Step 1: Mark visited indices by negating values at index abs(val) - 1
        for num in nums:
            target_idx = abs(num) - 1
            if nums[target_idx] > 0:
                nums[target_idx] = -nums[target_idx]
                
        # Step 2: Any positive value at index i implies (i + 1) was never encountered
        result = []
        for i in range(n):
            if nums[i] > 0:
                result.append(i + 1)
            else:
                # Optional: Restore original array state
                nums[i] = -nums[i]
                
        return result


if __name__ == "__main__":
    solver = Solution()
    
    # Test Case 1: Multiple missing numbers
    test1 = [4, 3, 2, 7, 8, 2, 3, 1]
    print("Test 1 Result:", solver.findDisappearedNumbers(test1))  # Expected: [5, 6]
    
    # Test Case 2: Array of duplicates
    test2 = [1, 1]
    print("Test 2 Result:", solver.findDisappearedNumbers(test2))  # Expected: [2]
    
    # Test Case 3: Complete array with no missing elements
    test3 = [1, 2, 3, 4]
    print("Test 3 Result:", solver.findDisappearedNumbers(test3))  # Expected: []
