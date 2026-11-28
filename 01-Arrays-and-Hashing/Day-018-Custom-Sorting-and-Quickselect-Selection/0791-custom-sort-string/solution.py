"""
LeetCode 791: Custom Sort String
Difficulty: Medium
Topic: Strings & Hash Table / Counting Sort

Pattern: Frequency Hashing & Constrained Sequence Placement
Instead of full comparison-based sorting (O(N log N)), we use Counting Sort (O(N)):
1. Build a frequency table of all characters in s: O(|s|).
2. Iterate through order:
   - For each character c in order:
     If c appears in our frequency table, append c * count[c] to our result builder.
     Remove c from the frequency table.
3. Append all remaining characters (characters in s that did not appear in order):
   - Their relative order does not matter as long as they appear after the ordered characters.

Time Complexity: O(|order| + |s|) — purely linear.
Space Complexity: O(1) auxiliary space — character count table bounded by lowercase English alphabet (<= 26).
"""

from collections import Counter


class Solution:
    def customSortString(self, order: str, s: str) -> str:
        """
        Permutes s so that characters follow the order specified in order.
        
        Args:
            order: str, unique custom character sequence
            s: str, string to be permuted
            
        Returns:
            str, permuted string
        """
        counts = Counter(s)
        result = []
        
        # 1. Place characters in the sequence defined by order
        for ch in order:
            if ch in counts:
                result.append(ch * counts[ch])
                del counts[ch]
                
        # 2. Append all remaining characters not present in order
        for ch, count in counts.items():
            result.append(ch * count)
            
        return "".join(result)


if __name__ == "__main__":
    solver = Solution()
    
    # Test Case 1: Standard case
    print("Test 1 Result:", solver.customSortString("cba", "abcd"))  # Expected: "cbad"
    
    # Test Case 2: Duplicate letters in s
    print("Test 2 Result:", solver.customSortString("bcafg", "abcd"))  # Expected: "bcad"
    
    # Test Case 3: Empty order overlap
    print("Test 3 Result:", solver.customSortString("xyz", "abc"))  # Expected: "abc"
