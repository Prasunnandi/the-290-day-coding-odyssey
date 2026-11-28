"""
LeetCode 14: Longest Common Prefix
Difficulty: Easy
Topic: Strings & Vertical Scanning

Pattern: Vertical Column Scanning
Instead of horizontal pairwise reductions (which examine all characters of every string even
when the prefix fails on the first letter), vertical scanning inspects the characters column by column:
1. For character index col in range [0, len(strs[0]) - 1]:
   - Let char = strs[0][col].
   - Compare char against strs[row][col] for all row in [1, len(strs) - 1].
   - If col reaches len(strs[row]) or strs[row][col] != char:
     We immediately terminate and return strs[0][:col].
2. If all columns pass, return strs[0].

Time Complexity: O(S) worst case (where S is the total number of characters across all strings).
                 In practice, vertical scanning stops at the first mismatch.
Space Complexity: O(1) auxiliary space.
"""

from typing import List


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        """
        Finds the longest common prefix among an array of strings.
        
        Args:
            strs: List[str], list of strings
            
        Returns:
            str, longest common prefix
        """
        if not strs:
            return ""
            
        first_str = strs[0]
        for col in range(len(first_str)):
            char = first_str[col]
            for row in range(1, len(strs)):
                # If column exceeds length of current string or characters mismatch
                if col == len(strs[row]) or strs[row][col] != char:
                    return first_str[:col]
                    
        return first_str


if __name__ == "__main__":
    solver = Solution()
    
    # Test Case 1: Standard prefix
    print("Test 1 Result:", solver.longestCommonPrefix(["flower", "flow", "flight"]))  # Expected: "fl"
    
    # Test Case 2: No common prefix
    print("Test 2 Result:", solver.longestCommonPrefix(["dog", "racecar", "car"]))  # Expected: ""
    
    # Test Case 3: Identical strings
    print("Test 3 Result:", solver.longestCommonPrefix(["interspecies", "interstellar", "interstate"]))  # Expected: "inters"
    
    # Test Case 4: Single string
    print("Test 4 Result:", solver.longestCommonPrefix(["alone"]))  # Expected: "alone"
