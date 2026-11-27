"""
LeetCode 88: Merge Sorted Array
Difficulty: Easy
Topic: Arrays & Two Pointers

Pattern: Three-Pointer Reverse Placement
We are given nums1 of capacity m + n, where the first m elements are sorted,
and nums2 of length n is sorted.
If we merge from the beginning (index 0), we would overwrite unmerged elements in nums1,
requiring O(m) auxiliary space.

Instead, we merge backwards from index (m + n - 1):
  - p1 points to the end of active elements in nums1 (m - 1)
  - p2 points to the end of nums2 (n - 1)
  - p points to the insertion position (m + n - 1)
  
At each step, we place the larger of nums1[p1] and nums2[p2] at nums1[p],
guaranteeing no unprocessed elements are ever overwritten.

Time Complexity: O(m + n) — linear traversal.
Space Complexity: O(1) — strictly in-place modifications in nums1.
"""

from typing import List


class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        p1 = m - 1
        p2 = n - 1
        p = m + n - 1
        
        # While elements remain in nums2 to be merged
        while p2 >= 0:
            if p1 >= 0 and nums1[p1] > nums2[p2]:
                nums1[p] = nums1[p1]
                p1 -= 1
            else:
                nums1[p] = nums2[p2]
                p2 -= 1
            p -= 1


if __name__ == "__main__":
    solver = Solution()
    
    # Test Case 1: Standard merge
    nums1_1 = [1, 2, 3, 0, 0, 0]
    m1 = 3
    nums2_1 = [2, 5, 6]
    n1 = 3
    solver.merge(nums1_1, m1, nums2_1, n1)
    print("Test 1 Result:", nums1_1)  # Expected: [1, 2, 2, 3, 5, 6]
    
    # Test Case 2: nums1 is empty, nums2 has 1 element
    nums1_2 = [0]
    m2 = 0
    nums2_2 = [1]
    n2 = 1
    solver.merge(nums1_2, m2, nums2_2, n2)
    print("Test 2 Result:", nums1_2)  # Expected: [1]
    
    # Test Case 3: nums2 is empty
    nums1_3 = [1]
    m3 = 1
    nums2_3 = []
    n3 = 0
    solver.merge(nums1_3, m3, nums2_3, n3)
    print("Test 3 Result:", nums1_3)  # Expected: [1]
