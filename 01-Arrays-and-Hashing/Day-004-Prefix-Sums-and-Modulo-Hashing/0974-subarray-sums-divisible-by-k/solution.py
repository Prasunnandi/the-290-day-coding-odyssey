"""
LeetCode #974: Subarray Sums Divisible by K
Difficulty: Medium
Topic: Arrays & Hashing
Pattern: Prefix Sum + Modulo Arithmetic Congruence
Link: https://leetcode.com/problems/subarray-sums-divisible-by-k/

Problem Statement:
Given an integer array nums and an integer k, return the number of non-empty subarrays
that have a sum divisible by k.
A subarray is a contiguous part of an array.
"""

from collections import defaultdict
from typing import List


class Solution:

    # ==========================================
    # Approach: Prefix Sum with Modulo Arithmetic
    # Math Principle:
    # If (prefix[j] - prefix[i]) % k == 0
    # Then prefix[j] % k == prefix[i] % k
    # Two prefix sums with the identical remainder modulo k form a subarray divisible by k!
    #
    # Handing Negative Remainders:
    # In Python, -1 % 5 == 4 automatically.
    # In other languages (Java/C++): (rem % k + k) % k ensures non-negative remainder.
    # ==========================================
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        count = 0
        current_sum = 0
        remainder_counts = defaultdict(int)
        remainder_counts[0] = 1 # Remainder 0 base case

        for num in nums:
            current_sum += num
            remainder = current_sum % k

            # If remainder has been seen before, each prior occurrence forms a valid subarray
            if remainder in remainder_counts:
                count += remainder_counts[remainder]

            remainder_counts[remainder] += 1

        return count


# Local Test Verification
if __name__ == "__main__":
    solver = Solution()

    # Test 1
    nums1 = [4, 5, 0, -2, -3, 1]
    k1 = 5
    assert solver.subarraysDivByK(nums1, k1) == 7, f"Test 1 failed: {solver.subarraysDivByK(nums1, k1)}"

    # Test 2
    nums2 = [5]
    k2 = 9
    assert solver.subarraysDivByK(nums2, k2) == 0, "Test 2 failed"

    print("All tests passed for LeetCode #974: Subarray Sums Divisible by K!")
