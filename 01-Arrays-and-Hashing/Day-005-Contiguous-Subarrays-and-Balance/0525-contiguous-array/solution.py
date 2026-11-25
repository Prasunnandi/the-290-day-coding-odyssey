"""
LeetCode #525: Contiguous Array
Difficulty: Medium
Topic: Arrays & Hashing
Pattern: Prefix Sum with Value Transformation (0 -> -1 Balance Counter)
Link: https://leetcode.com/problems/contiguous-array/

Problem Statement:
Given a binary array nums, return the maximum length of a contiguous subarray with an equal number of 0 and 1.
"""

from typing import List


class Solution:

    # ==========================================
    # Approach: Value Transformation (0 -> -1) & Prefix Sum Tracking
    # Concept:
    # Treat 0 as -1 and 1 as +1.
    # An equal number of 0s and 1s means the cumulative sum change is exactly 0.
    # If prefix[j] == prefix[i], then sum(nums[i+1 ... j]) == 0,
    # meaning the subarray from i+1 to j has equal 0s and 1s!
    # Subarray length: j - i.
    # To maximize length, record only the EARLIEST (first) index for each prefix sum.
    # Base Case: {0: -1} accounts for valid balanced subarrays starting at index 0.
    # Time Complexity: O(N)
    # Space Complexity: O(N)
    # ==========================================
    def findMaxLength(self, nums: List[int]) -> int:
        prefix_map = {0: -1}
        max_length = 0
        current_sum = 0

        for i, num in enumerate(nums):
            # Treat 0 as -1 and 1 as +1
            current_sum += 1 if num == 1 else -1

            if current_sum in prefix_map:
                max_length = max(max_length, i - prefix_map[current_sum])
            else:
                # Only record earliest index to maximize subsequent lengths
                prefix_map[current_sum] = i

        return max_length


# Local Test Verification
if __name__ == "__main__":
    solver = Solution()

    # Test 1: [0, 1] -> length 2
    assert solver.findMaxLength([0, 1]) == 2, "Test 1 failed"

    # Test 2: [0, 1, 0] -> length 2 ([0, 1] or [1, 0])
    assert solver.findMaxLength([0, 1, 0]) == 2, "Test 2 failed"

    # Test 3: [0, 1, 1, 0, 1, 1, 1, 0] -> length 4
    assert solver.findMaxLength([0, 1, 1, 0, 1, 1, 1, 0]) == 4, "Test 3 failed"

    print("All tests passed for LeetCode #525: Contiguous Array!")
