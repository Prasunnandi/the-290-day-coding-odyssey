"""
LeetCode 205: Isomorphic Strings
Difficulty: Easy
Topic: Strings & Hash Table

Pattern: Bijective Mapping (Two-Way Bijection)
Two strings s and t are isomorphic if:
  1. Forward mapping: Each character in s maps to exactly one character in t (Injective from s to t).
  2. Backward mapping: Each character in t maps to exactly one character in s (Injective from t to s).

Algorithm:
Maintain two hash tables or fixed-size arrays:
  - s_to_t: maps char in s -> char in t
  - t_to_s: maps char in t -> char in s

For each pair (c1, c2) in zip(s, t):
  - If c1 in s_to_t and s_to_t[c1] != c2: return False
  - If c2 in t_to_s and t_to_s[c2] != c1: return False
  - Set s_to_t[c1] = c2 and t_to_s[c2] = c1

Time Complexity: O(N) — single linear pass over strings of length N.
Space Complexity: O(1) — alphabet size is at most 256 ASCII characters.
"""

class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        """
        Determines if two strings s and t are isomorphic.
        
        Args:
            s: str, first string
            t: str, second string
            
        Returns:
            bool, True if isomorphic, False otherwise
        """
        if len(s) != len(t):
            return False
            
        s_to_t = {}
        t_to_s = {}
        
        for c1, c2 in zip(s, t):
            # Check forward mapping consistency
            if c1 in s_to_t and s_to_t[c1] != c2:
                return False
            # Check reverse mapping consistency
            if c2 in t_to_s and t_to_s[c2] != c1:
                return False
                
            s_to_t[c1] = c2
            t_to_s[c2] = c1
            
        return True


if __name__ == "__main__":
    solver = Solution()
    
    # Test Case 1: Valid isomorphism
    print("Test 1 Result:", solver.isIsomorphic("egg", "add"))  # Expected: True
    
    # Test Case 2: Injective collision
    print("Test 2 Result:", solver.isIsomorphic("foo", "bar"))  # Expected: False
    
    # Test Case 3: Reverse injective collision
    print("Test 3 Result:", solver.isIsomorphic("paper", "title"))  # Expected: True
    
    # Test Case 4: Two chars in s mapping to same char in t
    print("Test 4 Result:", solver.isIsomorphic("badc", "baba"))  # Expected: False
