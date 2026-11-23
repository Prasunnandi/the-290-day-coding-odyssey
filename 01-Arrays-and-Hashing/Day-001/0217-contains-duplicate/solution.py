"""
LeetCode #217: Contains Duplicate
Difficulty: Easy
Topic: Arrays & Hashing
Pattern: Hash Set (Membership Testing with Early Exit)
Link: https://leetcode.com/problems/contains-duplicate/

Problem Statement:
Given an integer array nums, return true if any value appears at least twice in
the array, and return false if every element is distinct.
"""

from typing import List


class Solution:

    # ==========================================
    # Approach 1: Sorting
    # Time Complexity: O(N log N)
    # Space Complexity: O(1) or O(N) depending on Timsort
    # ==========================================
    def containsDuplicateSorting(self, nums: List[int]) -> bool:
        nums.sort()
        for i in range(1, len(nums)):
            if nums[i] == nums[i - 1]:
                return True
        return False

    # ==========================================
    # Approach 2: Hash Set with Early Exit (Optimal)
    # Time Complexity: O(N)
    # Space Complexity: O(N)
    # ==========================================
    def containsDuplicate(self, nums: List[int]) -> bool:
        seen = set()
        for num in nums:
            # If element already present, duplicate found
            if num in seen:
                return True
            seen.add(num)
        return False

    # ==========================================
    # Approach 3: Pythonic Length Comparison
    # Time Complexity: O(N)
    # Space Complexity: O(N)
    # ==========================================
    def containsDuplicateSetLength(self, nums: List[int]) -> bool:
        return len(nums) != len(set(nums))


# Local Verification / Test Cases
if __name__ == "__main__":
    solver = Solution()

    # Test 1
    assert solver.containsDuplicate([1, 2, 3, 1]) is True, "Test 1 failed"

    # Test 2
    assert solver.containsDuplicate([1, 2, 3, 4]) is False, "Test 2 failed"

    # Test 3
    assert solver.containsDuplicate([1, 1, 1, 3, 3, 4, 3, 2, 4, 2]) is True, "Test 3 failed"

    print("All tests passed for LeetCode #217: Contains Duplicate!")
