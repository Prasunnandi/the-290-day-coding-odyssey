"""
LeetCode #49: Group Anagrams
Difficulty: Medium
Topic: Arrays & Hashing
Pattern: Hash Map Grouping (Categorization by Canonical Signature)
Link: https://leetcode.com/problems/group-anagrams/

Problem Statement:
Given an array of strings strs, group the anagrams together. You can return the answer in any order.
An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase,
typically using all the original letters exactly once.
"""

from collections import defaultdict
from typing import List


class Solution:

    # ==========================================
    # Approach 1: Sorted String as Key
    # Time Complexity: O(N * K log K) where N = len(strs), K = max string length
    # Space Complexity: O(N * K)
    # ==========================================
    def groupAnagramsSorting(self, strs: List[str]) -> List[List[str]]:
        groups = defaultdict(list)

        for s in strs:
            # Sort characters to form canonical key: e.g. "eat" -> "aet"
            canonical_key = "".join(sorted(s))
            groups[canonical_key].append(s)

        return list(groups.values())

    # ==========================================
    # Approach 2: 26-Character Frequency Tuple as Key (Optimal)
    # Time Complexity: O(N * K) - Linear in total number of characters
    # Space Complexity: O(N * K)
    # ==========================================
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = defaultdict(list)
        offset = ord('a')

        for s in strs:
            # 26-element tuple representing frequency of each character 'a' through 'z'
            count = [0] * 26
            for char in s:
                count[ord(char) - offset] += 1

            # Tuples are immutable and hashable in Python (usable as dict keys)
            groups[tuple(count)].append(s)

        return list(groups.values())


# Local Test Verification
if __name__ == "__main__":
    solver = Solution()

    # Test 1
    input1 = ["eat", "tea", "tan", "ate", "nat", "bat"]
    res1 = solver.groupAnagrams(input1)
    # Sort inner and outer for order-agnostic comparison
    sorted_res1 = sorted([sorted(g) for g in res1])
    expected1 = sorted([["bat"], ["nat", "tan"], ["ate", "eat", "tea"]])
    assert sorted_res1 == expected1, f"Test 1 failed: {res1}"

    # Test 2
    input2 = [""]
    assert solver.groupAnagrams(input2) == [[""]], "Test 2 failed"

    # Test 3
    input3 = ["a"]
    assert solver.groupAnagrams(input3) == [["a"]], "Test 3 failed"

    print("All tests passed for LeetCode #49: Group Anagrams!")
