"""
LeetCode #303: Range Sum Query - Immutable
Difficulty: Easy
Topic: Arrays & Hashing
Pattern: 1D Prefix Sum Array
Link: https://leetcode.com/problems/range-sum-query-immutable/

Problem Statement:
Given an integer array nums, handle multiple queries of the following type:
Calculate the sum of the elements of nums between indices left and right inclusive where left <= right.

Implement the NumArray class:
- NumArray(int[] nums) Initializes the object with the integer array nums.
- int sumRange(int left, int right) Returns the sum of the elements of nums between indices left and right inclusive
  (i.e. nums[left] + nums[left + 1] + ... + nums[right]).
"""

from typing import List


class NumArray:

    # ==========================================
    # Approach: Prefix Sum Array with Offset 1
    # prefix[k] = sum(nums[0 ... k-1])
    # sumRange(left, right) = prefix[right + 1] - prefix[left]
    # Initialization: O(N) Time, O(N) Space
    # Query: O(1) Time, O(1) Space
    # ==========================================
    def __init__(self, nums: List[int]):
        # prefix array of size len(nums) + 1 simplifies 0-based boundary handling
        self.prefix = [0] * (len(nums) + 1)
        for i, num in enumerate(nums):
            self.prefix[i + 1] = self.prefix[i] + num

    def sumRange(self, left: int, right: int) -> int:
        return self.prefix[right + 1] - self.prefix[left]


# Local Test Verification
if __name__ == "__main__":
    obj = NumArray([-2, 0, 3, -5, 2, -1])
    assert obj.sumRange(0, 2) == 1, "Test 1 failed (-2 + 0 + 3 = 1)"
    assert obj.sumRange(2, 5) == -1, "Test 2 failed (3 + -5 + 2 + -1 = -1)"
    assert obj.sumRange(0, 5) == -3, "Test 3 failed (total sum = -3)"
    print("All tests passed for LeetCode #303: Range Sum Query - Immutable!")
