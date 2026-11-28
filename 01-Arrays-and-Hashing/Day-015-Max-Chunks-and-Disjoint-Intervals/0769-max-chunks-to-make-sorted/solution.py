"""
LeetCode 769: Max Chunks To Make Sorted
Difficulty: Medium
Topic: Arrays & Greedy / Prefix Extrema

Pattern: Permutation Index Invariant
Given an array representing a permutation of numbers [0, n - 1]:
For any valid chunk ending at index i:
  - When sorted, the elements in arr[0..i] must form the set {0, 1, ..., i}.
  - This set contains values <= i if and only if the maximum value encountered so far
    is equal to the current index i:
      max(arr[0..i]) == i

Algorithm:
1. Maintain running max_val = 0.
2. Iterate i from 0 to n - 1:
   - max_val = max(max_val, arr[i])
   - If max_val == i, all elements {0..i} are confined to arr[0..i].
     Increment chunks count.
3. Return chunks.

Time Complexity: O(N) — single pass.
Space Complexity: O(1) — constant auxiliary space.
"""

from typing import List


class Solution:
    def maxChunksToSorted(self, arr: List[int]) -> int:
        """
        Calculates the maximum chunks to make permutation sorted.
        
        Args:
            arr: List[int], permutation of [0, n - 1]
            
        Returns:
            int, maximum number of chunks
        """
        max_val = 0
        chunks = 0
        
        for i, val in enumerate(arr):
            max_val = max(max_val, val)
            if max_val == i:
                chunks += 1
                
        return chunks


if __name__ == "__main__":
    solver = Solution()
    
    # Test Case 1: Reversed prefix
    test1 = [4, 3, 2, 1, 0]
    print("Test 1 Result:", solver.maxChunksToSorted(test1))  # Expected: 1
    
    # Test Case 2: Multiple chunks
    test2 = [1, 0, 2, 3, 4]
    print("Test 2 Result:", solver.maxChunksToSorted(test2))  # Expected: 4 ([1, 0], [2], [3], [4])
    
    # Test Case 3: Already sorted
    test3 = [0, 1, 2, 3]
    print("Test 3 Result:", solver.maxChunksToSorted(test3))  # Expected: 4
