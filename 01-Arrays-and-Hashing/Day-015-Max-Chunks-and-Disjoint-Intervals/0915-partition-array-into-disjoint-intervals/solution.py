"""
LeetCode 915: Partition Array into Disjoint Intervals
Difficulty: Medium
Topic: Arrays & Greedy

Pattern: One-Pass Greedy Horizon Expansion
We need to partition nums into [left] and [right] such that:
  max(left) <= min(right), with len(left) minimized.

One-Pass State Tracking:
1. max_left: The maximum element in the currently confirmed left partition (starts at nums[0]).
2. curr_max: The global maximum seen up to the current pointer i.
3. partition_idx: The ending index of the confirmed left partition (starts at 0).

Greedy Transition:
Iterate i from 1 to n - 1:
  - If nums[i] < max_left:
    An element smaller than max(left) has appeared. By the problem definition,
    this element CANNOT reside in the right partition.
    Therefore, the left partition MUST expand up to index i:
      partition_idx = i
      max_left = curr_max  (absorb all intermediate elements into left)
  - Else:
    nums[i] >= max_left, so nums[i] could potentially belong to the right partition.

Return partition_idx + 1 (the length of left).

Time Complexity: O(N) — single pass.
Space Complexity: O(1) — constant auxiliary variables.
"""

from typing import List


class Solution:
    def partitionDisjoint(self, nums: List[int]) -> int:
        """
        Finds the minimum length of left partition where max(left) <= min(right).
        
        Args:
            nums: List[int], array of integers
            
        Returns:
            int, minimum length of left
        """
        max_left = nums[0]
        curr_max = nums[0]
        partition_idx = 0
        
        for i in range(1, len(nums)):
            curr_max = max(curr_max, nums[i])
            if nums[i] < max_left:
                partition_idx = i
                max_left = curr_max
                
        return partition_idx + 1


if __name__ == "__main__":
    solver = Solution()
    
    # Test Case 1: Standard case
    test1 = [5, 0, 3, 8, 6]
    print("Test 1 Result:", solver.partitionDisjoint(test1))  # Expected: 3 ([5, 0, 3] and [8, 6])
    
    # Test Case 2: Minimal left of length 1
    test2 = [1, 1, 1, 0, 6, 12]
    print("Test 2 Result:", solver.partitionDisjoint(test2))  # Expected: 4 ([1, 1, 1, 0] and [6, 12])
    
    # Test Case 3: Strictly ascending
    test3 = [1, 2, 3, 4]
    print("Test 3 Result:", solver.partitionDisjoint(test3))  # Expected: 1 ([1] and [2, 3, 4])
