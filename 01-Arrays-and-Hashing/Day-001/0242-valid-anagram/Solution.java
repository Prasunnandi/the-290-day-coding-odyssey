/**
 * LeetCode #242: Valid Anagram
 * Difficulty: Easy
 * Topic: Arrays & Hashing
 * Pattern: Frequency Counting / Fixed-Size Array
 * Link: https://leetcode.com/problems/valid-anagram/
 *
 * Problem Statement:
 * Given two strings s and t, return true if t is an anagram of s, and false otherwise.
 * An Anagram is a word or phrase formed by rearranging the letters of a different
 * word or phrase, typically using all the original letters exactly once.
 */

import java.util.Arrays;

public class Solution {

    // ==========================================
    // Approach 1: Sorting
    // Time Complexity: O(N log N)
    // Space Complexity: O(N) or O(1) depending on language
    // ==========================================
    public boolean isAnagramSorting(String s, String t) {
        if (s.length() != t.length()) {
            return false;
        }

        char[] sChars = s.toCharArray();
        char[] tChars = t.toCharArray();

        Arrays.sort(sChars);
        Arrays.sort(tChars);

        return Arrays.equals(sChars, tChars);
    }

    // ==========================================
    // Approach 2: Fixed-Size Frequency Array (Optimal)
    // Time Complexity: O(N)
    // Space Complexity: O(1) [fixed 26 lowercase English letters]
    // ==========================================
    public boolean isAnagram(String s, String t) {
        // If lengths differ, they cannot be anagrams
        if (s.length() != t.length()) {
            return false;
        }

        // 26 counters for 'a' through 'z'
        int[] counts = new int[26];

        for (int i = 0; i < s.length(); i++) {
            counts[s.charAt(i) - 'a']++;
            counts[t.charAt(i) - 'a']--;
        }

        // Check if all counts canceled out to zero
        for (int count : counts) {
            if (count != 0) {
                return false;
            }
        }

        return true;
    }

    // Local Test Runner
    public static void main(String[] args) {
        Solution solver = new Solution();

        // Test 1: Anagrams
        assert solver.isAnagram("anagram", "nagaram") : "Test 1 failed";
        System.out.println("Test 1 Passed: anagram & nagaram -> " + solver.isAnagram("anagram", "nagaram"));

        // Test 2: Not Anagrams
        assert !solver.isAnagram("rat", "car") : "Test 2 failed";
        System.out.println("Test 2 Passed: rat & car -> " + solver.isAnagram("rat", "car"));

        // Test 3: Length Mismatch
        assert !solver.isAnagram("ab", "a") : "Test 3 failed";
        System.out.println("Test 3 Passed: ab & a -> " + solver.isAnagram("ab", "a"));
    }
}
