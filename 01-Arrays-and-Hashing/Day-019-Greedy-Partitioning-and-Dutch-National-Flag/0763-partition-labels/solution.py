"""
LeetCode 763: Partition Labels
Difficulty: Medium
Topic: Strings & Greedy / Two Pointers

Pattern: Greedy Furthest Right Boundary Tracking
Requirement:
Each letter can appear in AT MOST one partition.
Therefore, if a partition contains character c, it MUST extend at least up to the
LAST occurrence of c in string s.

Algorithm:
1. Pass 1 (Record Last Sightings):
   Store the rightmost index for each character:
     last[c] = rightmost index of c in s
2. Pass 2 (Greedy Partitioning):
   Maintain the boundary of the current partition:
     start = 0, end = 0
   Iterate i from 0 to n - 1:
     end = max(end, last[s[i]])
     If i == end:
       We have safely enclosed all occurrences of every character encountered so far!
       Record partition size: end - start + 1
       Advance start = i + 1

Time Complexity: O(N) — two linear passes over string s.
Space Complexity: O(1) auxiliary space — table bounded by 26 lowercase English letters.
"""

from typing import List


class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        """
        Partitions s into the maximum number of parts so that each character appears in at most one part.
        
        Args:
            s: str, input string
            
        Returns:
            List[int], lengths of the partitions
        """
        # Step 1: Record rightmost index of each character
        last = {c: i for i, c in enumerate(s)}
        
        # Step 2: Greedily expand partition horizon
        result = []
        start = 0
        end = 0
        
        for i, c in enumerate(s):
            end = max(end, last[c])
            if i == end:
                result.append(end - start + 1)
                start = i + 1
                
        return result


if __name__ == "__main__":
    solver = Solution()
    
    # Test Case 1: Standard case
    test1 = "ababcbacadefegdehijhklij"
    print("Test 1 Result:", solver.partitionLabels(test1))  # Expected: [9, 7, 8]
    
    # Test Case 2: Monolithic string
    test2 = "eccbbbbdec"
    print("Test 2 Result:", solver.partitionLabels(test2))  # Expected: [10]
    
    # Test Case 3: All distinct characters
    test3 = "abcdef"
    print("Test 3 Result:", solver.partitionLabels(test3))  # Expected: [1, 1, 1, 1, 1, 1]
