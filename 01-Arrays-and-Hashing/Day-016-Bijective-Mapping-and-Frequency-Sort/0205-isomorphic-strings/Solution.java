/**
 * LeetCode 205: Isomorphic Strings
 * Difficulty: Easy
 * Topic: Strings & Hash Table
 *
 * Pattern: Bijective Mapping (Two-Way Bijection)
 * Verify character bijection using two fixed ASCII arrays.
 *
 * Time Complexity: O(N)
 * Space Complexity: O(1)
 */

public class Solution {

    public boolean isIsomorphic(String s, String t) {
        if (s.length() != t.length()) return false;

        int[] mapST = new int[256];
        int[] mapTS = new int[256];

        for (int i = 0; i < s.length(); i++) {
            char c1 = s.charAt(i);
            char c2 = t.charAt(i);

            // Using 1-based indexing to distinguish from default 0
            if (mapST[c1] != 0 && mapST[c1] != c2) return false;
            if (mapTS[c2] != 0 && mapTS[c2] != c1) return false;

            mapST[c1] = c2;
            mapTS[c2] = c1;
        }

        return true;
    }

    public static void main(String[] args) {
        Solution solver = new Solution();

        System.out.println("Test 1: " + solver.isIsomorphic("egg", "add"));     // Expected: true
        System.out.println("Test 2: " + solver.isIsomorphic("foo", "bar"));     // Expected: false
        System.out.println("Test 3: " + solver.isIsomorphic("paper", "title")); // Expected: true
    }
}
