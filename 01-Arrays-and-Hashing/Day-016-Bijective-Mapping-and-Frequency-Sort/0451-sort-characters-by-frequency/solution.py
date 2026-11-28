"""
LeetCode 451: Sort Characters By Frequency
Difficulty: Medium
Topic: Strings & Hash Table / Bucket Sort

Pattern: Frequency Bucket Sort (Linear-Time Sorting)
While sorting unique characters by frequency using comparison sort takes O(K log K)
(where K <= 62 is distinct characters), Bucket Sort runs in guaranteed O(N) time:
1. Count character frequencies using a Hash Map: O(N).
2. The frequency of any character is bounded in [1, N].
   Create an array of buckets of size N + 1 where bucket[f] stores characters with frequency f.
3. Traverse the buckets in reverse order from N down to 1:
   For each character in bucket[f], append char * f to the output builder.

Time Complexity: O(N) — where N is the length of string s.
Space Complexity: O(N) — bucket array and character frequency table.
"""

from collections import Counter


class Solution:
    def frequencySort(self, s: str) -> str:
        """
        Sorts characters of s in decreasing order of frequency.
        
        Args:
            s: str, input string
            
        Returns:
            str, frequency-sorted string
        """
        # Step 1: Count frequency of each character
        counts = Counter(s)
        n = len(s)
        
        # Step 2: Bucket sort where index is the frequency
        buckets = [[] for _ in range(n + 1)]
        for char, freq in counts.items():
            buckets[freq].append(char)
            
        # Step 3: Reconstruct string from highest frequency to lowest
        result = []
        for freq in range(n, 0, -1):
            for char in buckets[freq]:
                result.append(char * freq)
                
        return "".join(result)


if __name__ == "__main__":
    solver = Solution()
    
    # Test Case 1: Multiple frequencies
    print("Test 1 Result:", solver.frequencySort("tree"))  # Expected: 'eert' or 'eetr'
    
    # Test Case 2: Uniform case-sensitive frequencies
    print("Test 2 Result:", solver.frequencySort("cccaaa"))  # Expected: 'cccaaa' or 'aaaccc'
    
    # Test Case 3: Case-sensitive distinction
    print("Test 3 Result:", solver.frequencySort("Aabb"))  # Expected: 'bbAa' or 'bbaA'
