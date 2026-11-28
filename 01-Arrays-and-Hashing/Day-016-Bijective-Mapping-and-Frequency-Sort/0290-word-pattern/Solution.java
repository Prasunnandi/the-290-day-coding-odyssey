/**
 * LeetCode 290: Word Pattern
 * Difficulty: Easy
 * Topic: Strings & Hash Table
 *
 * Pattern: Character-to-Token Bijective Mapping
 * Uses two HashMaps to enforce strict 1-to-1 bijection between chars and words.
 *
 * Time Complexity: O(N + M)
 * Space Complexity: O(W)
 */

import java.util.HashMap;
import java.util.Map;

public class Solution {

    public boolean wordPattern(String pattern, String s) {
        String[] words = s.split(" ");
        if (pattern.length() != words.length) return false;

        Map<Character, String> charToWord = new HashMap<>();
        Map<String, Character> wordToChar = new HashMap<>();

        for (int i = 0; i < pattern.length(); i++) {
            char c = pattern.charAt(i);
            String w = words[i];

            if (charToWord.containsKey(c) && !charToWord.get(c).equals(w)) {
                return false;
            }
            if (wordToChar.containsKey(w) && wordToChar.get(w) != c) {
                return false;
            }

            charToWord.put(c, w);
            wordToChar.put(w, c);
        }

        return true;
    }

    public static void main(String[] args) {
        Solution solver = new Solution();

        System.out.println("Test 1: " + solver.wordPattern("abba", "dog cat cat dog"));  // Expected: true
        System.out.println("Test 2: " + solver.wordPattern("abba", "dog cat cat fish")); // Expected: false
        System.out.println("Test 3: " + solver.wordPattern("aaaa", "dog cat cat dog"));  // Expected: false
    }
}
