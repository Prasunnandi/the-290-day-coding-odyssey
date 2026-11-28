/**
 * LeetCode 451: Sort Characters By Frequency
 * Difficulty: Medium
 * Topic: Strings & Bucket Sort
 *
 * Pattern: Bucket Sort by Frequency
 * 1. Count character frequencies using HashMap.
 * 2. Place characters into List<Character>[] buckets where index == frequency.
 * 3. Traverse buckets in reverse order and build the result string.
 *
 * Time Complexity: O(N)
 * Space Complexity: O(N)
 */

import java.util.*;

public class Solution {

    public String frequencySort(String s) {
        if (s == null || s.length() <= 1) return s;

        // Step 1: Count frequency of each character
        Map<Character, Integer> counts = new HashMap<>();
        for (char c : s.toCharArray()) {
            counts.put(c, counts.getOrDefault(c, 0) + 1);
        }

        // Step 2: Create buckets of size N + 1
        int n = s.length();
        @SuppressWarnings("unchecked")
        List<Character>[] buckets = new List[n + 1];

        for (Map.Entry<Character, Integer> entry : counts.entrySet()) {
            int freq = entry.getValue();
            if (buckets[freq] == null) {
                buckets[freq] = new ArrayList<>();
            }
            buckets[freq].add(entry.getKey());
        }

        // Step 3: Traverse buckets backwards from highest frequency
        StringBuilder sb = new StringBuilder();
        for (int freq = n; freq >= 1; freq--) {
            if (buckets[freq] != null) {
                for (char c : buckets[freq]) {
                    for (int i = 0; i < freq; i++) {
                        sb.append(c);
                    }
                }
            }
        }

        return sb.toString();
    }

    public static void main(String[] args) {
        Solution solver = new Solution();

        System.out.println("Test 1: " + solver.frequencySort("tree"));   // eert or eetr
        System.out.println("Test 2: " + solver.frequencySort("cccaaa")); // cccaaa or aaaccc
        System.out.println("Test 3: " + solver.frequencySort("Aabb"));   // bbAa or bbaA
    }
}
