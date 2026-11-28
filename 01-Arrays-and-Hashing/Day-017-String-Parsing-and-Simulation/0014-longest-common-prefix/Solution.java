/**
 * LeetCode 14: Longest Common Prefix
 * Difficulty: Easy
 * Topic: Strings & Vertical Scanning
 *
 * Pattern: Vertical Column Scanning
 * Compare characters column by column across all strings.
 *
 * Time Complexity: O(S) where S is sum of all characters.
 * Space Complexity: O(1)
 */

public class Solution {

    public String longestCommonPrefix(String[] strs) {
        if (strs == null || strs.length == 0) return "";

        String firstStr = strs[0];
        for (int col = 0; col < firstStr.length(); col++) {
            char c = firstStr.charAt(col);
            for (int row = 1; row < strs.length; row++) {
                if (col == strs[row].length() || strs[row].charAt(col) != c) {
                    return firstStr.substring(0, col);
                }
            }
        }

        return firstStr;
    }

    public static void main(String[] args) {
        Solution solver = new Solution();

        String[] test1 = {"flower", "flow", "flight"};
        System.out.println("Test 1: " + solver.longestCommonPrefix(test1)); // Expected: "fl"

        String[] test2 = {"dog", "racecar", "car"};
        System.out.println("Test 2: " + solver.longestCommonPrefix(test2)); // Expected: ""
    }
}
