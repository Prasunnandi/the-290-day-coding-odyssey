/**
 * LeetCode #271: Encode and Decode Strings
 * Difficulty: Medium
 * Topic: Arrays & Hashing
 * Pattern: Length-Prefixed String Chunking / Protocol Serialization
 * Link: https://leetcode.com/problems/encode-and-decode-strings/
 *
 * Problem Statement:
 * Design an algorithm to encode a list of strings to a string, and decode it back.
 * Strings can contain any of the 256 valid ASCII characters.
 */

import java.util.*;

public class Solution {

    public static class Codec {

        // ==========================================
        // Optimal Protocol: Length Prefix + Delimiter '#'
        // Format: [length]#[content]
        // Time Complexity: O(Total Characters)
        // Space Complexity: O(1) auxiliary
        // ==========================================

        // Encodes a list of strings to a single string.
        public String encode(List<String> strs) {
            StringBuilder sb = new StringBuilder();
            for (String s : strs) {
                sb.append(s.length()).append('#').append(s);
            }
            return sb.toString();
        }

        // Decodes a single string to a list of strings.
        public List<String> decode(String s) {
            List<String> result = new ArrayList<>();
            int i = 0;
            int n = s.length();

            while (i < n) {
                // Locate delimiter '#'
                int j = i;
                while (s.charAt(j) != '#') {
                    j++;
                }

                // Parse length
                int length = Integer.parseInt(s.substring(i, j));

                // Slice the content string of exact length
                int start = j + 1;
                int end = start + length;
                result.add(s.substring(start, end));

                // Advance pointer past the extracted word
                i = end;
            }

            return result;
        }
    }

    // Local Test Runner
    public static void main(String[] args) {
        Codec codec = new Codec();

        // Test 1
        List<String> input1 = Arrays.asList("lint", "code", "love", "you");
        String encoded1 = codec.encode(input1);
        System.out.println("Encoded 1: " + encoded1);
        assert codec.decode(encoded1).equals(input1) : "Test 1 failed";

        // Test 2: Delimiters and numbers inside content
        List<String> input2 = Arrays.asList("4#hello", "world#2", "", "#");
        String encoded2 = codec.encode(input2);
        System.out.println("Encoded 2: " + encoded2);
        assert codec.decode(encoded2).equals(input2) : "Test 2 failed";

        System.out.println("All Java tests passed for LeetCode #271: Encode and Decode Strings!");
    }
}
