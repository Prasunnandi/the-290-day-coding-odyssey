"""
LeetCode 31: Next Permutation
Difficulty: Medium
Topic: Arrays & Hashing

Pattern: Lexicographical Suffix Reversal
To find the next lexicographically greater permutation:
1. Identify Pivot: Scan backwards to find the first index `i` where nums[i] < nums[i + 1].
   - If no such `i` exists, the sequence is in descending order (highest permutation).
     Simply reverse the entire array and return.
2. Identify Successor: Scan backwards to find the largest index `j > i` where nums[j] > nums[i].
3. Swap: Swap nums[i] and nums[j].
4. Reverse Suffix: Reverse nums[i + 1:] to convert the descending tail into the smallest
   ascending order.

Time Complexity: O(N) — at most two backward scans and one suffix reversal.
Space Complexity: O(1) — strictly in-place modifications.
"""

from typing import List


class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        if n <= 1:
            return
            
        # Step 1: Find first decreasing element from the right
        i = n - 2
        while i >= 0 and nums[i] >= nums[i + 1]:
            i -= 1
            
        if i >= 0:
            # Step 2: Find element just larger than nums[i] from the right
            j = n - 1
            while nums[j] <= nums[i]:
                j -= 1
            # Step 3: Swap nums[i] and nums[j]
            nums[i], nums[j] = nums[j], nums[i]
            
        # Step 4: Reverse the suffix from i + 1 to n - 1
        left, right = i + 1, n - 1
        while left < right:
            nums[left], nums[right] = nums[right], nums[left]
            left += 1
            right -= 1


if __name__ == "__main__":
    solver = Solution()
    
    # Test Case 1: Standard case
    arr1 = [1, 2, 3]
    solver.nextPermutation(arr1)
    print("Test 1 Result:", arr1)  # Expected: [1, 3, 2]
    
    # Test Case 2: Highest permutation (reverse to smallest)
    arr2 = [3, 2, 1]
    solver.nextPermutation(arr2)
    print("Test 2 Result:", arr2)  # Expected: [1, 2, 3]
    
    # Test Case 3: Duplicate elements
    arr3 = [1, 1, 5]
    solver.nextPermutation(arr3)
    print("Test 3 Result:", arr3)  # Expected: [1, 5, 1]
