"""
LeetCode 215: Kth Largest Element in an Array
Difficulty: Medium
Topic: Arrays & Divide and Conquer / Quickselect

Pattern: Randomized Quickselect (Hoare's Selection Algorithm)
The k-th largest element is located at index target = len(nums) - k in 0-indexed ascending order.

Why Quickselect over Full Sort?
- Quicksort partitions and recurses on BOTH halves: T(N) = 2*T(N/2) + O(N) = O(N log N).
- Quickselect partitions and recurses on ONLY ONE half containing the target index:
    T(N) = T(N/2) + O(N) = O(N * (1 + 1/2 + 1/4 + ...)) = O(N) average time!

3-Way Partitioning (Dutch National Flag Optimization):
To prevent O(N^2) degradation on inputs with heavy duplicate elements, we partition into
three groups around pivot:
  - Elements < pivot
  - Elements == pivot
  - Elements > pivot

Time Complexity: O(N) average, O(N^2) worst-case (mitigated by random pivot selection).
Space Complexity: O(1) auxiliary space (in-place iterative/recursive).
"""

import random
from typing import List


class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        """
        Finds the k-th largest element in O(N) average time using Quickselect.
        
        Args:
            nums: List[int], array of integers
            k: int, 1-based rank from largest
            
        Returns:
            int, k-th largest integer
        """
        target = len(nums) - k  # convert to 0-based k-th smallest index
        
        def quickselect(left: int, right: int) -> int:
            if left == right:
                return nums[left]
                
            # Random pivot selection prevents adversarial worst-case inputs
            pivot_idx = random.randint(left, right)
            pivot = nums[pivot_idx]
            
            # 3-Way Partitioning (Dutch National Flag)
            lt = left       # nums[left .. lt-1] < pivot
            i = left        # nums[lt .. i-1] == pivot
            gt = right      # nums[gt+1 .. right] > pivot
            
            while i <= gt:
                if nums[i] < pivot:
                    nums[lt], nums[i] = nums[i], nums[lt]
                    lt += 1
                    i += 1
                elif nums[i] > pivot:
                    nums[i], nums[gt] = nums[gt], nums[i]
                    gt -= 1
                else:
                    i += 1
                    
            # Pivot group spans [lt, gt]
            if target < lt:
                return quickselect(left, lt - 1)
            elif target > gt:
                return quickselect(gt + 1, right)
            else:
                return nums[target]
                
        return quickselect(0, len(nums) - 1)


if __name__ == "__main__":
    solver = Solution()
    
    # Test Case 1: Standard case
    print("Test 1 Result:", solver.findKthLargest([3, 2, 1, 5, 6, 4], 2))  # Expected: 5
    
    # Test Case 2: Array with duplicates
    print("Test 2 Result:", solver.findKthLargest([3, 2, 3, 1, 2, 4, 5, 5, 6], 4))  # Expected: 4
    
    # Test Case 3: Single element
    print("Test 3 Result:", solver.findKthLargest([1], 1))  # Expected: 1
    
    # Test Case 4: All duplicates
    print("Test 4 Result:", solver.findKthLargest([7, 7, 7, 7], 2))  # Expected: 7
