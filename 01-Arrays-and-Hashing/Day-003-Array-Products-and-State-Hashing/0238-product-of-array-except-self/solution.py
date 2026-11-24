"""
LeetCode #238: Product of Array Except Self
Difficulty: Medium
Topic: Arrays & Hashing
Pattern: Prefix & Suffix Products (Running Product Accumulation)
Link: https://leetcode.com/problems/product-of-array-except-self/

Problem Statement:
Given an integer array nums, return an array answer such that answer[i] is equal to
the product of all the elements of nums except nums[i].
The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.
You must write an algorithm that runs in O(n) time and without using the division operation.
Follow-up: Can you solve the problem in O(1) extra space complexity? (The output array does not count as extra space).
"""

from typing import List


class Solution:

    # ==========================================
    # Approach 1: Explicit Prefix and Suffix Arrays
    # Time Complexity: O(N)
    # Space Complexity: O(N) auxiliary space
    # ==========================================
    def productExceptSelfPrefixSuffix(self, nums: List[int]) -> List[int]:
        n = len(nums)
        prefix = [1] * n
        suffix = [1] * n

        # Build prefix products: prefix[i] = nums[0] * ... * nums[i-1]
        for i in range(1, n):
            prefix[i] = prefix[i - 1] * nums[i - 1]

        # Build suffix products: suffix[i] = nums[i+1] * ... * nums[n-1]
        for i in range(n - 2, -1, -1):
            suffix[i] = suffix[i + 1] * nums[i + 1]

        # Combine prefix and suffix
        return [prefix[i] * suffix[i] for i in range(n)]

    # ==========================================
    # Approach 2: O(1) Extra Space (Prefix in Output + Rolling Suffix)
    # Time Complexity: O(N)
    # Space Complexity: O(1) auxiliary (output array excluded)
    # ==========================================
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        output = [1] * n

        # Pass 1: Compute prefix products directly in output
        prefix = 1
        for i in range(n):
            output[i] = prefix
            prefix *= nums[i]

        # Pass 2: Multiply by suffix product using a single rolling variable
        suffix = 1
        for i in range(n - 1, -1, -1):
            output[i] *= suffix
            suffix *= nums[i]

        return output


# Local Test Verification
if __name__ == "__main__":
    solver = Solution()

    # Test 1
    nums1 = [1, 2, 3, 4]
    assert solver.productExceptSelf(nums1) == [24, 12, 8, 6], f"Test 1 failed: {solver.productExceptSelf(nums1)}"

    # Test 2: Contains Zeros
    nums2 = [-1, 1, 0, -3, 3]
    assert solver.productExceptSelf(nums2) == [0, 0, 9, 0, 0], f"Test 2 failed: {solver.productExceptSelf(nums2)}"

    print("All tests passed for LeetCode #238: Product of Array Except Self!")
