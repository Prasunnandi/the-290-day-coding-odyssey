"""
LeetCode 179: Largest Number
Difficulty: Medium
Topic: Strings & Custom Sorting / Greedy

Pattern: Total Order Comparison via Concatenation Transitivity
We must arrange string representations of numbers such that their concatenation forms
the largest decimal value.

Comparator Definition:
For two strings A and B:
  - If (A + B) > (B + A): A should appear before B (A is "greater" than B).
  - If (A + B) < (B + A): B should appear before A.
  - If (A + B) == (B + A): A and B are equivalent in order.

Mathematical Soundness (Transitivity Proof):
This pairwise relation forms a strict weak ordering:
  If A + B >= B + A and B + C >= C + B, then A + C >= C + A.
Hence, standard comparison sort (like Timsort) is mathematically guaranteed to find
the globally optimal configuration!

Edge Case:
If the array contains all zeroes (e.g., [0, 0]), after sorting the first element is "0".
We must return "0" rather than "00".

Time Complexity: O(N log N * K) — where N is len(nums) and K is average number of digits (<= 10).
Space Complexity: O(N * K) — to hold string representations.
"""

from functools import cmp_to_key
from typing import List


class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        """
        Arranges numbers to form the largest possible number string.
        
        Args:
            nums: List[int], list of non-negative integers
            
        Returns:
            str, largest formed number
        """
        # Convert all integers to strings
        str_nums = [str(x) for x in nums]
        
        # Custom comparator: return -1 if a should precede b (a + b > b + a)
        def compare(a: str, b: str) -> int:
            if a + b > b + a:
                return -1
            elif a + b < b + a:
                return 1
            else:
                return 0
                
        str_nums.sort(key=cmp_to_key(compare))
        
        # If the largest number is "0", the entire result is "0"
        if str_nums[0] == "0":
            return "0"
            
        return "".join(str_nums)


if __name__ == "__main__":
    solver = Solution()
    
    # Test Case 1: Simple ordering
    print("Test 1 Result:", solver.largestNumber([10, 2]))  # Expected: "210"
    
    # Test Case 2: Multi-digit prefix clash (30 vs 3 vs 34)
    print("Test 2 Result:", solver.largestNumber([3, 30, 34, 5, 9]))  # Expected: "9534330"
    
    # Test Case 3: Multiple zeroes
    print("Test 3 Result:", solver.largestNumber([0, 0]))  # Expected: "0"
    
    # Test Case 4: Single element
    print("Test 4 Result:", solver.largestNumber([1]))  # Expected: "1"
