"""
LeetCode #1: Two Sum
Difficulty: Easy
Topic: Arrays & Hashing
Pattern: Hash Map (Complement Lookup)
Link: https://leetcode.com/problems/two-sum/

Problem Statement:
Given an array of integers nums and an integer target, return indices of the two
numbers such that they add up to target. You may assume that each input would have
exactly one solution, and you may not use the same element twice.
"""

from typing import List


class Solution:

    # ==========================================
    # Approach 1: Brute Force
    # Time Complexity: O(N^2)
    # Space Complexity: O(1)
    # ==========================================
    def twoSumBruteForce(self, nums: List[int], target: int) -> List[int]:
        n = len(nums)
        # Check every pair (i, j) where i < j
        for i in range(n):
            for j in range(i + 1, n):
                if nums[i] + nums[j] == target:
                    return [i, j]
        return []

    # ==========================================
    # Approach 2: Two-Pass Hash Table
    # Time Complexity: O(N)
    # Space Complexity: O(N)
    # ==========================================
    def twoSumTwoPass(self, nums: List[int], target: int) -> List[int]:
        # Pass 1: Build the hash table
        val_to_index = {num: i for i, num in enumerate(nums)}

        # Pass 2: Search for complement
        for i, num in enumerate(nums):
            complement = target - num
            # Ensure the complement isn't the current element itself
            if complement in val_to_index and val_to_index[complement] != i:
                return [i, val_to_index[complement]]
        return []

    # ==========================================
    # Approach 3: One-Pass Hash Table (Optimal 0ms)
    # Time Complexity: O(N)
    # Space Complexity: O(N)
    # ==========================================
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # Hash map storing: {value -> index}
        seen = {}

        for i, num in enumerate(nums):
            complement = target - num

            # If complement already observed, return pair immediately
            if complement in seen:
                return [seen[complement], i]

            # Otherwise, store current element with its index
            seen[num] = i

        return []


# Local Verification / Test Cases
if __name__ == "__main__":
    solver = Solution()

    # Test Case 1
    nums1 = [2, 7, 11, 15]
    target1 = 9
    assert solver.twoSum(nums1, target1) == [0, 1], f"Test 1 failed: {solver.twoSum(nums1, target1)}"

    # Test Case 2
    nums2 = [3, 2, 4]
    target2 = 6
    assert solver.twoSum(nums2, target2) == [1, 2], f"Test 2 failed: {solver.twoSum(nums2, target2)}"

    # Test Case 3
    nums3 = [3, 3]
    target3 = 6
    assert solver.twoSum(nums3, target3) == [0, 1], f"Test 3 failed: {solver.twoSum(nums3, target3)}"

    print("All tests passed for LeetCode #1: Two Sum (All Approaches)!")
