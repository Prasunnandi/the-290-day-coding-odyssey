/**
 * LeetCode #49: Group Anagrams
 * Difficulty: Medium
 * Topic: Arrays & Hashing
 * Pattern: Hash Map Grouping (Categorization by Canonical Signature)
 * Link: https://leetcode.com/problems/group-anagrams/
 *
 * Problem Statement:
 * Given an array of strings strs, group the anagrams together. You can return the answer in any order.
 */

import java.util.*;

public class Solution {

    // ==========================================
    // Approach 1: Sorted String as Key
    // Time Complexity: O(N * K log K) where N = len(strs), K = max length of a string
    // Space Complexity: O(N * K)
    // ==========================================
    public List<List<String>> groupAnagramsSorting(String[] strs) {
        if (strs == null || strs.length == 0) {
            return new ArrayList<>();
        }

        Map<String, List<String>> map = new HashMap<>();

        for (String s : strs) {
            char[] chars = s.toCharArray();
            Arrays.sort(chars);
            String sortedKey = new String(chars);

            map.computeIfAbsent(sortedKey, k -> new ArrayList<>()).add(s);
        }

        return new ArrayList<>(map.values());
    }

    // ==========================================
    // Approach 2: Frequency Signature as Key (Optimal)
    // Time Complexity: O(N * K) - Linear time without sorting
    // Space Complexity: O(N * K)
    // ==========================================
    public List<List<String>> groupAnagrams(String[] strs) {
        if (strs == null || strs.length == 0) {
            return new ArrayList<>();
        }

        Map<String, List<String>> map = new HashMap<>();

        for (String s : strs) {
            // Count array for 26 lowercase English letters
            int[] counts = new int[26];
            for (char c : s.toCharArray()) {
                counts[c - 'a']++;
            }

            // Build delimiter-separated frequency signature (e.g. #1#0#0...#1)
            StringBuilder sb = new StringBuilder();
            for (int count : counts) {
                sb.append('#').append(count);
            }
            String signature = sb.toString();

            map.computeIfAbsent(signature, k -> new ArrayList<>()).add(s);
        }

        return new ArrayList<>(map.values());
    }

    // Local Test Runner
    public static void main(String[] args) {
        Solution solver = new Solution();

        String[] input1 = {"eat", "tea", "tan", "ate", "nat", "bat"};
        List<List<String>> res1 = solver.groupAnagrams(input1);
        System.out.println("Test 1 Result: " + res1);
        assert res1.size() == 3 : "Test 1 failed";

        String[] input2 = {""};
        List<List<String>> res2 = solver.groupAnagrams(input2);
        System.out.println("Test 2 Result: " + res2);
        assert res2.size() == 1 : "Test 2 failed";

        System.out.println("All Java tests passed for LeetCode #49: Group Anagrams!");
    }
}
