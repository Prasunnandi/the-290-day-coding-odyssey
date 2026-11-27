"""
LeetCode 645: Set Mismatch
Difficulty: Easy
Topic: Arrays & Hashing

Pattern: Sign Inversion Index Marking
Given array nums of size n containing numbers in [1, n] with 1 duplicate and 1 missing:
1. Each value x maps directly to index abs(x) - 1.
2. If nums[abs(x) - 1] is already negative, abs(x) is the duplicate!
3. Otherwise, negate nums[abs(x) - 1] to mark it visited.
4. Scan the array: any index i that remains positive was never visited,
   meaning (i + 1) is the missing number!

Time Complexity: O(N) — two linear scans.
Space Complexity: O(1) auxiliary space — modifies input in-place and restores it.
"""

from typing import List


class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        """
        Finds the duplicate and missing numbers in nums.
        
        Args:
            nums: List[int], array of length n with values in [1, n]
            
        Returns:
            List[int], [duplicate, missing]
        """
        duplicate = -1
        missing = -1
        
        # Step 1: Detect duplicate by sign inversion
        for num in nums:
            val = abs(num)
            idx = val - 1
            if nums[idx] < 0:
                duplicate = val
            else:
                nums[idx] = -nums[idx]
                
        # Step 2: Detect missing by remaining positive value
        for i in range(len(nums)):
            if nums[i] > 0:
                missing = i + 1
            else:
                nums[i] = -nums[i]  # restore array
                
        return [duplicate, missing]


if __name__ == "__main__":
    solver = Solution()
    
    # Test Case 1: Standard case
    test1 = [1, 2, 2, 4]
    print("Test 1 Result:", solver.findErrorNums(test1))  # Expected: [2, 3]
    
    # Test Case 2: Pair with 1 missing
    test2 = [1, 1]
    print("Test 2 Result:", solver.findErrorNums(test2))  # Expected: [1, 2]
    
    # Test Case 3: Out of order
    test3 = [3, 2, 3, 4, 6, 5]
    print("Test 3 Result:", solver.findErrorNums(test3))  # Expected: [3, 1]
