"""
LeetCode #724: Find Pivot Index
Difficulty: Easy
Topic: Arrays & Hashing
Pattern: Total Sum vs Rolling Left Sum Balance
Link: https://leetcode.com/problems/find-pivot-index/
(Also identical to LeetCode #1991: Find the Middle Index in Array)

Problem Statement:
Given an array of integers nums, calculate the pivot index of this array.
The pivot index is the index where the sum of all the numbers strictly to the left
of the index is equal to the sum of all the numbers strictly to the index's right.
If the index is on the left edge of the array, then the left sum is 0.
Return the leftmost pivot index. If no such index exists, return -1.
"""

from typing import List


class Solution:

    # ==========================================
    # Approach: Total Sum & Rolling Left Sum (Optimal O(1) Space)
    # Math Principle:
    # total_sum = left_sum + nums[i] + right_sum
    # Therefore: right_sum = total_sum - left_sum - nums[i]
    # Pivot condition: left_sum == right_sum
    # Time Complexity: O(N)
    # Space Complexity: O(1)
    # ==========================================
    def pivotIndex(self, nums: List[int]) -> int:
        total_sum = sum(nums)
        left_sum = 0

        for i, num in enumerate(nums):
            # right_sum is what remains after subtracting left_sum and current num
            right_sum = total_sum - left_sum - num
            if left_sum == right_sum:
                return i
            left_sum += num

        return -1


# Local Test Verification
if __name__ == "__main__":
    solver = Solution()

    # Test 1: Pivot at index 3: left = 1+7+3 = 11, right = 5+6 = 11
    assert solver.pivotIndex([1, 7, 3, 6, 5, 6]) == 3, "Test 1 failed"

    # Test 2: No pivot exists
    assert solver.pivotIndex([1, 2, 3]) == -1, "Test 2 failed"

    # Test 3: Pivot at index 0: left = 0, right = 1 - 1 = 0
    assert solver.pivotIndex([2, 1, -1]) == 0, "Test 3 failed"

    print("All tests passed for LeetCode #724: Find Pivot Index!")
