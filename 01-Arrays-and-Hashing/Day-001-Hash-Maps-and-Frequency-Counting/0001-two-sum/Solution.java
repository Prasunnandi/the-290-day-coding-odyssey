/**
 * LeetCode #1: Two Sum
 * Difficulty: Easy
 * Topic: Arrays & Hashing
 * Pattern: Hash Map (Complement Lookup)
 * Link: https://leetcode.com/problems/two-sum/
 *
 * Problem Statement:
 * Given an array of integers nums and an integer target, return indices of the two
 * numbers such that they add up to target. You may assume that each input would have
 * exactly one solution, and you may not use the same element twice.
 */

import java.util.Arrays;
import java.util.HashMap;
import java.util.Map;

public class Solution {

    // ==========================================
    // Approach 1: Brute Force
    // Time Complexity: O(N^2)
    // Space Complexity: O(1)
    // ==========================================
    public int[] twoSumBruteForce(int[] nums, int target) {
        int n = nums.length;
        // Check every possible pair (i, j) where i < j
        for (int i = 0; i < n; i++) {
            for (int j = i + 1; j < n; j++) {
                if (nums[i] + nums[j] == target) {
                    return new int[]{i, j};
                }
            }
        }
        return new int[]{};
    }

    // ==========================================
    // Approach 2: Two-Pass Hash Table
    // Time Complexity: O(N)
    // Space Complexity: O(N)
    // ==========================================
    public int[] twoSumTwoPass(int[] nums, int target) {
        Map<Integer, Integer> map = new HashMap<>();

        // Pass 1: Add all elements and their indices to hash map
        for (int i = 0; i < nums.length; i++) {
            map.put(nums[i], i);
        }

        // Pass 2: Check if complement exists and is not the current element itself
        for (int i = 0; i < nums.length; i++) {
            int complement = target - nums[i];
            if (map.containsKey(complement) && map.get(complement) != i) {
                return new int[]{i, map.get(complement)};
            }
        }
        return new int[]{};
    }

    // ==========================================
    // Approach 3: One-Pass Hash Table (Optimal 0ms)
    // Time Complexity: O(N)
    // Space Complexity: O(N)
    // ==========================================
    public int[] twoSum(int[] nums, int target) {
        // Hash map storing: {value -> index}
        Map<Integer, Integer> seen = new HashMap<>();

        for (int i = 0; i < nums.length; i++) {
            int complement = target - nums[i];

            // If complement is already encountered, we found our pair
            if (seen.containsKey(complement)) {
                return new int[]{seen.get(complement), i};
            }

            // Otherwise, record the current element and its index
            seen.put(nums[i], i);
        }

        return new int[]{};
    }

    // Local Test Runner
    public static void main(String[] args) {
        Solution solver = new Solution();

        // Test 1
        int[] nums1 = {2, 7, 11, 15};
        int target1 = 9;
        int[] res1 = solver.twoSum(nums1, target1);
        System.out.println("Test 1 Result: " + Arrays.toString(res1)); // Expected: [0, 1]

        // Test 2
        int[] nums2 = {3, 2, 4};
        int target2 = 6;
        int[] res2 = solver.twoSum(nums2, target2);
        System.out.println("Test 2 Result: " + Arrays.toString(res2)); // Expected: [1, 2]

        // Test 3
        int[] nums3 = {3, 3};
        int target3 = 6;
        int[] res3 = solver.twoSum(nums3, target3);
        System.out.println("Test 3 Result: " + Arrays.toString(res3)); // Expected: [0, 1]
    }
}
