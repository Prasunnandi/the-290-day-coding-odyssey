"""
LeetCode #242: Valid Anagram
Difficulty: Easy
Topic: Arrays & Hashing
Pattern: Frequency Counting / Fixed-Size Array
Link: https://leetcode.com/problems/valid-anagram/

Problem Statement:
Given two strings s and t, return true if t is an anagram of s, and false otherwise.
An Anagram is a word or phrase formed by rearranging the letters of a different word
or phrase, typically using all the original letters exactly once.
"""


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # If lengths differ, they cannot be anagrams
        if len(s) != len(t):
            return False

        # Frequency count array for 26 lowercase English letters
        counts = [0] * 26
        offset = ord('a')

        for char_s, char_t in zip(s, t):
            counts[ord(char_s) - offset] += 1
            counts[ord(char_t) - offset] -= 1

        # Check if all counts balanced out to 0
        return all(count == 0 for count in counts)


# Local Verification / Test Cases
if __name__ == "__main__":
    solver = Solution()

    # Test Case 1
    assert solver.isAnagram("anagram", "nagaram") is True, "Test 1 failed"

    # Test Case 2
    assert solver.isAnagram("rat", "car") is False, "Test 2 failed"

    # Test Case 3 (different lengths)
    assert solver.isAnagram("a", "ab") is False, "Test 3 failed"

    print("All tests passed for LeetCode #242: Valid Anagram!")
