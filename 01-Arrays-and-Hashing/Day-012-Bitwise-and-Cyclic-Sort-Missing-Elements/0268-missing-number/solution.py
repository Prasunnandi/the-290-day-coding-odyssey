"""
LeetCode 268: Missing Number
Difficulty: Easy
Topic: Arrays & Bit Manipulation

Pattern: Bitwise XOR Elimination / Gauss Summation
Given n distinct numbers in range [0, n]:
Approach 1: XOR Property (Zero Overflow Risk)
  - x ^ x = 0 (self-cancellation)
  - x ^ 0 = x (identity)
  By XOR-ing all expected numbers [0..n] and all observed elements in nums:
  Every present number appears twice and cancels out to 0;
  The single missing number appears once and remains!
  missing = n ^ (XOR_{i=0}^{n-1} (i ^ nums[i]))

Approach 2: Mathematical Sum
  expected = n * (n + 1) // 2
  return expected - sum(nums)

Time Complexity: O(N) — single pass.
Space Complexity: O(1) — constant extra space.
"""

from typing import List


class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        """
        Finds the missing number in [0, n] using Bitwise XOR.
        
        Args:
            nums: List[int], array of n distinct integers from [0, n]
            
        Returns:
            int, the missing integer
        """
        n = len(nums)
        missing = n
        
        for i, num in enumerate(nums):
            missing ^= (i ^ num)
            
        return missing

    def missingNumberMath(self, nums: List[int]) -> int:
        """
        Alternative: Gauss summation formula.
        """
        n = len(nums)
        expected_sum = n * (n + 1) // 2
        return expected_sum - sum(nums)


if __name__ == "__main__":
    solver = Solution()
    
    # Test Case 1: Standard case
    test1 = [3, 0, 1]
    print("Test 1 Result (XOR):", solver.missingNumber(test1))  # Expected: 2
    
    # Test Case 2: Missing middle element
    test2 = [0, 1]
    print("Test 2 Result (XOR):", solver.missingNumber(test2))  # Expected: 2
    
    # Test Case 3: Missing 8
    test3 = [9, 6, 4, 2, 3, 5, 7, 0, 1]
    print("Test 3 Result (XOR):", solver.missingNumber(test3))  # Expected: 8
