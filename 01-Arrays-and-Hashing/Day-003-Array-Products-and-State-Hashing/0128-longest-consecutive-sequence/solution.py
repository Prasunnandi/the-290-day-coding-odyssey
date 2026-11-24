"""
LeetCode #128: Longest Consecutive Sequence
Difficulty: Medium
Topic: Arrays & Hashing
Pattern: Hash Set Intelligent Sequence Start Check
Link: https://leetcode.com/problems/longest-consecutive-sequence/

Problem Statement:
Given an unsorted array of integers nums, return the length of the longest consecutive elements sequence.
You must write an algorithm that runs in O(n) time.
"""

from typing import List


class Solution:

    # ==========================================
    # Approach 1: Sorting
    # Time Complexity: O(N log N)
    # Space Complexity: O(1) or O(N)
    # ==========================================
    def longestConsecutiveSorting(self, nums: List[int]) -> int:
        if not nums:
            return 0

        nums.sort()
        longest = 1
        current_streak = 1

        for i in range(1, len(nums)):
            # Skip duplicates
            if nums[i] == nums[i - 1]:
                continue
            if nums[i] == nums[i - 1] + 1:
                current_streak += 1
            else:
                longest = max(longest, current_streak)
                current_streak = 1

        return max(longest, current_streak)

    # ==========================================
    # Approach 2: Hash Set (Optimal O(N) Linear Time)
    # Only start counting if (num - 1) is NOT in the set!
    # This guarantees each consecutive streak is traversed only ONCE!
    # ==========================================
    def longestConsecutive(self, nums: List[int]) -> int:
        num_set = set(nums)
        longest = 0

        for num in num_set:
            # Check if num is the beginning of a sequence
            if (num - 1) not in num_set:
                current_num = num
                current_streak = 1

                # Expand sequence forward
                while (current_num + 1) in num_set:
                    current_num += 1
                    current_streak += 1

                longest = max(longest, current_streak)

        return longest


# Local Test Verification
if __name__ == "__main__":
    solver = Solution()

    # Test 1
    nums1 = [100, 4, 200, 1, 3, 2]
    assert solver.longestConsecutive(nums1) == 4, f"Test 1 failed: {solver.longestConsecutive(nums1)}" # Sequence: [1, 2, 3, 4]

    # Test 2
    nums2 = [0, 3, 7, 2, 5, 8, 4, 6, 0, 1]
    assert solver.longestConsecutive(nums2) == 9, f"Test 2 failed: {solver.longestConsecutive(nums2)}" # Sequence: [0, 1, 2, 3, 4, 5, 6, 7, 8]

    # Test 3: Empty Array
    nums3 = []
    assert solver.longestConsecutive(nums3) == 0, "Test 3 failed"

    print("All tests passed for LeetCode #128: Longest Consecutive Sequence!")
