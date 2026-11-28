"""
LeetCode 768: Max Chunks To Make Sorted II
Difficulty: Hard
Topic: Arrays & Greedy / Prefix-Suffix Extrema

Pattern: Prefix Max <= Suffix Min Partition Invariant
Unlike Problem 769, elements are arbitrary and may contain duplicates.
A partition cut between index i and index i + 1 is valid if and only if:
  Every element in the left chunk is <= every element in the right chunk:
    max(arr[0..i]) <= min(arr[i + 1..n - 1])

Algorithm:
1. Precompute suffix minimums:
   min_right[i] = min(arr[i..n-1])
2. Scan left-to-right maintaining prefix maximum max_left:
   For i from 0 to n - 2:
     max_left = max(max_left, arr[i])
     If max_left <= min_right[i + 1]:
       chunks += 1
3. Total chunks = chunks + 1 (accounting for the final segment).

Time Complexity: O(N) — two linear scans.
Space Complexity: O(N) — suffix minimum array.
"""

from typing import List


class Solution:
    def maxChunksToSorted(self, arr: List[int]) -> int:
        """
        Calculates maximum chunks to sort an arbitrary array with duplicates.
        
        Args:
            arr: List[int], array of arbitrary integers
            
        Returns:
            int, maximum number of chunks
        """
        n = len(arr)
        if n <= 1:
            return n
            
        # Step 1: Precompute suffix minimums
        min_right = [0] * n
        min_right[-1] = arr[-1]
        for i in range(n - 2, -1, -1):
            min_right[i] = min(arr[i], min_right[i + 1])
            
        # Step 2: Compare running prefix max against suffix min
        chunks = 0
        max_left = float("-inf")
        
        for i in range(n - 1):
            max_left = max(max_left, arr[i])
            if max_left <= min_right[i + 1]:
                chunks += 1
                
        return chunks + 1


if __name__ == "__main__":
    solver = Solution()
    
    # Test Case 1: Standard case
    test1 = [5, 4, 3, 2, 1]
    print("Test 1 Result:", solver.maxChunksToSorted(test1))  # Expected: 1
    
    # Test Case 2: Array with duplicates
    test2 = [2, 1, 3, 4, 4]
    print("Test 2 Result:", solver.maxChunksToSorted(test2))  # Expected: 4 ([2, 1], [3], [4], [4])
    
    # Test Case 3: Plateau elements
    test3 = [1, 1, 1, 1]
    print("Test 3 Result:", solver.maxChunksToSorted(test3))  # Expected: 4
