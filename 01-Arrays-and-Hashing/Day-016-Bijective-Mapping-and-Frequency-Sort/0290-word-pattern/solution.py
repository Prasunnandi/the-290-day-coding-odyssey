"""
LeetCode 290: Word Pattern
Difficulty: Easy
Topic: Strings & Hash Table

Pattern: Character-to-Token Bijective Mapping
Identical in mathematical structure to LeetCode 205 (Isomorphic Strings), but the codomain
consists of whitespace-delimited words instead of single characters.

Bijections Required:
  1. pattern[i] -> words[i] (char_to_word)
  2. words[i] -> pattern[i] (word_to_char)

Time Complexity: O(N + M) — where N is length of pattern and M is total character length of s.
Space Complexity: O(W) — where W is number of distinct words in s.
"""

class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        """
        Determines if pattern matches word sequence s bijectively.
        
        Args:
            pattern: str, pattern of letters
            s: str, space-delimited words
            
        Returns:
            bool, True if pattern matches s, False otherwise
        """
        words = s.split(" ")
        if len(pattern) != len(words):
            return False
            
        char_to_word = {}
        word_to_char = {}
        
        for ch, word in zip(pattern, words):
            # Check forward mapping
            if ch in char_to_word and char_to_word[ch] != word:
                return False
            # Check reverse mapping
            if word in word_to_char and word_to_char[word] != ch:
                return False
                
            char_to_word[ch] = word
            word_to_char[word] = ch
            
        return True


if __name__ == "__main__":
    solver = Solution()
    
    # Test Case 1: Valid pattern
    print("Test 1 Result:", solver.wordPattern("abba", "dog cat cat dog"))  # Expected: True
    
    # Test Case 2: Mismatched word at the end
    print("Test 2 Result:", solver.wordPattern("abba", "dog cat cat fish"))  # Expected: False
    
    # Test Case 3: Multiple chars mapping to same word
    print("Test 3 Result:", solver.wordPattern("abba", "dog dog dog dog"))  # Expected: False
    
    # Test Case 4: Length mismatch
    print("Test 4 Result:", solver.wordPattern("aaa", "aa aa aa aa"))  # Expected: False
