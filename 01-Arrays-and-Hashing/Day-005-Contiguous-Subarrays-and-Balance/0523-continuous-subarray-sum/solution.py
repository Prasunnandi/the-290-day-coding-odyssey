"""
LeetCode #523: Continuous Subarray Sum
Difficulty: Medium
Topic: Arrays & Hashing
Pattern: Prefix Sum Modulo Hash Map (First Occurrence Index Tracking)
Link: https://leetcode.com/problems/continuous-subarray-sum/

Problem Statement:
Given an integer array nums and an integer k, return true if nums has a good subarray or false otherwise.
A good subarray is defined as:
- its length is at least two, and
- the sum of the elements of the subarray is a multiple of k (i.e. sum = n * k where n is an integer).
"""

from typing import List


class Solution:

    # ==========================================
    # Approach: Prefix Sum Modulo with First Occurrence Map
    # Math Principle:
    # If prefix[j] % k == prefix[i] % k, then sum(nums[i+1 ... j]) % k == 0.
    # Constraint: Length must be at least two (j - i >= 2).
    # Critical Rule: We store only the FIRST occurrence of each remainder to maximize (j - i).
    # Base Case: {0: -1} ensures subarrays starting from index 0 of length >= 2 are valid.
    # Time Complexity: O(N)
    # Space Complexity: O(min(N, K))
    # ==========================================
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        # Map: {remainder: first_seen_index}
        remainder_map = {0: -1}
        current_sum = 0

        for i, num in enumerate(nums):
            current_sum += num
            remainder = current_sum % k

            if remainder in remainder_map:
                # Check if subarray length is at least 2
                if i - remainder_map[remainder] >= 2:
                    return True
            else:
                # Only record first occurrence
                remainder_map[remainder] = i

        return False


# Local Test Verification
if __name__ == "__main__":
    solver = Solution()

    # Test 1: Subarray [2, 4] sums to 6
    assert solver.checkSubarraySum([23, 2, 4, 6, 7], 6) is True, "Test 1 failed"

    # Test 2: Subarray [23, 2, 6, 4, 7] sums to 42 (multiple of 6)
    assert solver.checkSubarraySum([23, 2, 6, 4, 7], 6) is True, "Test 2 failed"

    # Test 3: [23, 2, 6, 4, 7], k = 13 -> False
    assert solver.checkSubarraySum([23, 2, 6, 4, 7], 13) is False, "Test 3 failed"

    # Test 4: Edge case: two zeros [0, 0] with any k is divisible by k
    assert solver.checkSubarraySum([0, 0], 1) is True, "Test 4 failed"

    print("All tests passed for LeetCode #523: Continuous Subarray Sum!")
