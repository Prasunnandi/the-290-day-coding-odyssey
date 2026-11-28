/**
 * LeetCode 791: Custom Sort String
 * Difficulty: Medium
 * Topic: Strings & Counting Sort
 *
 * Pattern: Frequency Hashing & Constrained Sequence Placement
 * Count character frequencies in s and append characters following order.
 *
 * Time Complexity: O(|order| + |s|)
 * Space Complexity: O(1) auxiliary (26 lowercase English letters)
 */

public class Solution {

    public String customSortString(String order, String s) {
        int[] counts = new int[26];
        for (char c : s.toCharArray()) {
            counts[c - 'a']++;
        }

        StringBuilder sb = new StringBuilder();

        // 1. Append characters specified by order
        for (char c : order.toCharArray()) {
            while (counts[c - 'a'] > 0) {
                sb.append(c);
                counts[c - 'a']--;
            }
        }

        // 2. Append remaining characters
        for (int i = 0; i < 26; i++) {
            while (counts[i] > 0) {
                sb.append((char) ('a' + i));
                counts[i]--;
            }
        }

        return sb.toString();
    }

    public static void main(String[] args) {
        Solution solver = new Solution();

        System.out.println("Test 1: " + solver.customSortString("cba", "abcd"));  // "cbad"
        System.out.println("Test 2: " + solver.customSortString("bcafg", "abcd")); // "bcad"
    }
}
