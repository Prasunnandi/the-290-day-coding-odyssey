# 0242. Valid Anagram

- **Difficulty:** Easy
- **Topic:** Arrays & Hashing
- **Pattern:** Frequency Counting / Fixed-Size Array
- **LeetCode Link:** [Valid Anagram](https://leetcode.com/problems/valid-anagram/)

---

## Problem Statement

Given two strings `s` and `t`, return `true` if `t` is an anagram of `s`, and `false` otherwise.

An **Anagram** is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

### Examples

**Example 1:**
```text
Input: s = "anagram", t = "nagaram"
Output: true
```

**Example 2:**
```text
Input: s = "rat", t = "car"
Output: false
```

---

## 💡 Intuition

Two strings are anagrams if and only if:
1. They have the identical length.
2. Every character appears with the exact same frequency in both strings.

---

## 🚀 Approach 1: Sorting

Sort both strings alphabetically and compare them character by character.

### Python 3
```python
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return sorted(s) == sorted(t)
```

### Java
```java
import java.util.Arrays;

class Solution {
    public boolean isAnagram(String s, String t) {
        if (s.length() != t.length()) return false;
        char[] sChars = s.toCharArray();
        char[] tChars = t.toCharArray();
        Arrays.sort(sChars);
        Arrays.sort(tChars);
        return Arrays.equals(sChars, tChars);
    }
}
```

### Complexity
- **Time Complexity:** $O(N \log N)$ due to sorting.
- **Space Complexity:** $O(N)$ or $O(1)$ depending on language string mutability.

---

## 🌟 Approach 2: Fixed-Size Frequency Array (Optimal)

Since strings consist only of lowercase English letters, we allocate an array of size 26.
Increment the count for each character in `s` and decrement for each in `t`. All entries must be zero at the end.

### Python 3
```python
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
            
        counts = [0] * 26
        offset = ord('a')
        
        for c1, c2 in zip(s, t):
            counts[ord(c1) - offset] += 1
            counts[ord(c2) - offset] -= 1
            
        return all(c == 0 for c in counts)
```

### Java
```java
class Solution {
    public boolean isAnagram(String s, String t) {
        if (s.length() != t.length()) return false;
        
        int[] counts = new int[26];
        for (int i = 0; i < s.length(); i++) {
            counts[s.charAt(i) - 'a']++;
            counts[t.charAt(i) - 'a']--;
        }
        
        for (int c : counts) {
            if (c != 0) return false;
        }
        return true;
    }
}
```

### Complexity
- **Time Complexity:** $O(N)$ — single simultaneous pass over both strings.
- **Space Complexity:** $O(1)$ auxiliary memory — constant 26-element array.
