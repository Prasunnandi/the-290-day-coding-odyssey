"""
LeetCode #560: Subarray Sum Equals K
Difficulty: Medium
Topic: Arrays & Hashing
Pattern: Prefix Sum + Hash Map (Target Complement Counting)
Link: https://leetcode.com/problems/subarray-sum-equals-k/

Problem Statement:
Given an array of integers nums and an integer k, return the total number of subarrays whose sum equals to k.
A subarray is a contiguous non-empty sequence of elements within an array.
Note: Numbers can be negative, so Sliding Window does NOT work!
"""

from collections import defaultdict
from typing import List


class Solution:

    # ==========================================
    # Approach 1: Prefix Sum + Hash Map (Optimal O(N))
    # Mathematical Invariant:
    # If prefix[j] - prefix[i] == k, then sum(nums[i+1 ... j]) == k.
    # Therefore, prefix[i] = prefix[j] - k.
    # We count how many times (current_sum - k) has occurred so far!
    # Base Case: {0: 1} to count subarrays that start from index 0.
    # ==========================================
    def subarraySum(self, nums: List[int], k: int) -> int:
        count = 0
        current_sum = 0
        # Hash map: {prefix_sum: frequency}
        prefix_counts = defaultdict(int)
        prefix_counts[0] = 1 # Essential for subarrays starting at index 0

        for num in nums:
            current_sum += num
            complement = current_sum - k

            # Add count of previously observed prefix sums that yield target k
            if complement in prefix_counts:
                count += prefix_counts[complement]

            # Record current cumulative prefix sum
            prefix_counts[current_sum] += 1

        return count


# Local Test Verification
if __name__ == "__main__":
    solver = Solution()

    # Test 1
    assert solver.subarraySum([1, 1, 1], 2) == 2, "Test 1 failed" # [1,1] at [0..1] and [1..2]

    # Test 2
    assert solver.subarraySum([1, 2, 3], 3) == 2, "Test 2 failed" # [1,2] and [3]

    # Test 3: Negative numbers
    assert solver.subarraySum([1, -1, 0], 0) == 3, "Test 3 failed" # [1, -1], [0], [1, -1, 0]

    print("All tests passed for LeetCode #560: Subarray Sum Equals K!")
