"""
LeetCode 454: 4Sum II
Difficulty: Medium
Topic: Arrays & Hash Table / Meet-in-the-Middle

Pattern: Meet-in-the-Middle Hash Map Tradeoff
In LeetCode 18, all 4 numbers came from the same array and unique index combinations were required,
necessitating O(N^3) time and O(1) space.

Here, the 4 numbers come from 4 independent arrays nums1, nums2, nums3, nums4.
We can split the 4-way sum into two 2-way sums (Meet-in-the-Middle):
  nums1[i] + nums2[j] = -(nums3[k] + nums4[l])

Algorithm:
1. Map all pairwise sums of (nums1, nums2) into a frequency hash map:
   sum12[a + b] += 1
2. For each pair (c, d) in nums3 x nums4:
   Look up -(c + d) in sum12 and add its frequency to total count.

Time Complexity: O(N^2) — two separate N x N double loops instead of one N^4 loop.
Space Complexity: O(N^2) — to store at most N^2 unique pairwise sums in the hash map.
"""

from collections import Counter
from typing import List


class Solution:
    def fourSumCount(self, nums1: List[int], nums2: List[int], nums3: List[int], nums4: List[int]) -> int:
        """
        Returns the count of tuples (i, j, k, l) such that nums1[i] + nums2[j] + nums3[k] + nums4[l] == 0.
        
        Args:
            nums1, nums2, nums3, nums4: List[int], four integer arrays of size n
            
        Returns:
            int, number of tuples summing to 0
        """
        # Step 1: Precompute frequency of all sums from nums1 and nums2
        sum12 = Counter(a + b for a in nums1 for b in nums2)
        
        # Step 2: Query complementary sums from nums3 and nums4
        count = 0
        for c in nums3:
            for d in nums4:
                target = -(c + d)
                count += sum12[target]
                
        return count


if __name__ == "__main__":
    solver = Solution()
    
    # Test Case 1: Standard case
    n1 = [1, 2]
    n2 = [-2, -1]
    n3 = [-1, 2]
    n4 = [0, 2]
    print("Test 1 Result:", solver.fourSumCount(n1, n2, n3, n4))  # Expected: 2
    
    # Test Case 2: All zeroes
    print("Test 2 Result:", solver.fourSumCount([0], [0], [0], [0]))  # Expected: 1
    
    # Test Case 3: No zero sum
    print("Test 3 Result:", solver.fourSumCount([1], [1], [1], [1]))  # Expected: 0
