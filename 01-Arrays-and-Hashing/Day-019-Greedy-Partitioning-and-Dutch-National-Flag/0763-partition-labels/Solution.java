/**
 * LeetCode 763: Partition Labels
 * Difficulty: Medium
 * Topic: Strings & Greedy
 *
 * Pattern: Furthest Right Boundary Tracking
 * Track last occurrence of each character; partition cut when i == end.
 *
 * Time Complexity: O(N)
 * Space Complexity: O(1) auxiliary (26 English characters)
 */

import java.util.ArrayList;
import java.util.List;

public class Solution {

    public List<Integer> partitionLabels(String s) {
        int[] last = new int[26];
        for (int i = 0; i < s.length(); i++) {
            last[s.charAt(i) - 'a'] = i;
        }

        List<Integer> result = new ArrayList<>();
        int start = 0;
        int end = 0;

        for (int i = 0; i < s.length(); i++) {
            end = Math.max(end, last[s.charAt(i) - 'a']);
            if (i == end) {
                result.add(end - start + 1);
                start = i + 1;
            }
        }

        return result;
    }

    public static void main(String[] args) {
        Solution solver = new Solution();

        System.out.println("Test 1: " + solver.partitionLabels("ababcbacadefegdehijhklij")); // Expected: [9, 7, 8]
        System.out.println("Test 2: " + solver.partitionLabels("eccbbbbdec"));                 // Expected: [10]
    }
}
