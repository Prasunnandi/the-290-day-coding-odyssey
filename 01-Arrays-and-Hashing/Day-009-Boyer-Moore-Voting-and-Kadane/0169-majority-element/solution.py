"""
LeetCode 169: Majority Element
Difficulty: Easy
Topic: Arrays & Hashing

Pattern: Boyer-Moore Voting Algorithm
The majority element appears strictly more than floor(n / 2) times.
Even if all other distinct elements combine their votes to cancel out the majority element,
the majority element will still retain a positive surplus vote count.

Algorithm:
1. Initialize candidate = None, count = 0.
2. For each num in nums:
   - If count == 0: candidate = num
   - count += 1 if num == candidate else -1
3. Return candidate.

Time Complexity: O(N) — single pass.
Space Complexity: O(1) — constant extra space.
"""

from typing import List


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        """
        Finds the element appearing > floor(n / 2) times using Boyer-Moore Voting.
        
        Args:
            nums: List[int], array of numbers
            
        Returns:
            int, the majority element
        """
        candidate = 0
        count = 0
        
        for num in nums:
            if count == 0:
                candidate = num
            count += (1 if num == candidate else -1)
            
        return candidate


if __name__ == "__main__":
    solver = Solution()
    
    # Test Case 1: Standard majority
    test1 = [3, 2, 3]
    print("Test 1 Result:", solver.majorityElement(test1))  # Expected: 3
    
    # Test Case 2: Even-odd distribution
    test2 = [2, 2, 1, 1, 1, 2, 2]
    print("Test 2 Result:", solver.majorityElement(test2))  # Expected: 2
    
    # Test Case 3: Single element
    test3 = [1]
    print("Test 3 Result:", solver.majorityElement(test3))  # Expected: 1
