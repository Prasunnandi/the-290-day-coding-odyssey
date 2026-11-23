"""
LeetCode #271: Encode and Decode Strings
Difficulty: Medium
Topic: Arrays & Hashing
Pattern: Length-Prefixed String Chunking / Protocol Serialization
Link: https://leetcode.com/problems/encode-and-decode-strings/
(Also available on LintCode #659 / NeetCode 150)

Problem Statement:
Design an algorithm to encode a list of strings to a string. The encoded string is
then sent over the network and is decoded back to the original list of strings.

Please implement encode and decode methods.
Strings may contain any possible characters out of 256 valid ASCII characters (including delimiters!).
"""

from typing import List


class Codec:

    # ==========================================
    # Optimal Protocol: Length Prefix + Delimiter '#'
    # Format: [length]#[content]
    # Example: ["lint", "code", "love", "you"] -> "4#lint4#code4#love3#you"
    # Even if content contains '#' or numbers, length prevents false splitting!
    # ==========================================

    def encode(self, strs: List[str]) -> str:
        """Encodes a list of strings to a single string."""
        encoded = []
        for s in strs:
            encoded.append(f"{len(s)}#{s}")
        return "".join(encoded)

    def decode(self, s: str) -> List[str]:
        """Decodes a single string to a list of strings."""
        result = []
        i = 0
        n = len(s)

        while i < n:
            # Find the delimiter '#' starting from pointer i
            j = i
            while s[j] != '#':
                j += 1

            # Length of the string chunk
            length = int(s[i:j])

            # Content starts right after '#' and extends for 'length' characters
            start = j + 1
            end = start + length
            result.append(s[start:end])

            # Move pointer past the current decoded string
            i = end

        return result


# Local Test Verification
if __name__ == "__main__":
    codec = Codec()

    # Test 1: Standard words
    test1 = ["lint", "code", "love", "you"]
    encoded1 = codec.encode(test1)
    print("Encoded 1:", encoded1)
    assert codec.decode(encoded1) == test1, "Test 1 failed"

    # Test 2: Edge case with delimiter '#' and numbers in content
    test2 = ["we#and", "4#code", "", "#", "123#456"]
    encoded2 = codec.encode(test2)
    print("Encoded 2:", encoded2)
    assert codec.decode(encoded2) == test2, "Test 2 failed"

    # Test 3: Empty string list
    test3 = [""]
    assert codec.decode(codec.encode(test3)) == test3, "Test 3 failed"

    print("All tests passed for LeetCode #271: Encode and Decode Strings!")
