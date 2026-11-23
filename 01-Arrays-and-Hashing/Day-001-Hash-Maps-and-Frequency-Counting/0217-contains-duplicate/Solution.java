/**
 * LeetCode #217: Contains Duplicate
 * Difficulty: Easy
 * Topic: Arrays & Hashing
 * Pattern: Hash Set (Membership Testing with Early Exit)
 * Link: https://leetcode.com/problems/contains-duplicate/
 *
 * Problem Statement:
 * Given an integer array nums, return true if any value appears at least twice in
 * the array, and return false if every element is distinct.
 */

import java.util.Arrays;
import java.util.HashSet;
import java.util.Set;

public class Solution {

    // ==========================================
    // Approach 1: Sorting
    // Time Complexity: O(N log N)
    // Space Complexity: O(1) or O(log N) depending on sort
    // ==========================================
    public boolean containsDuplicateSorting(int[] nums) {
        Arrays.sort(nums);
        for (int i = 1; i < nums.length; i++) {
            if (nums[i] == nums[i - 1]) {
                return true;
            }
        }
        return false;
    }

    // ==========================================
    // Approach 2: Hash Set with Early Exit (Optimal)
    // Time Complexity: O(N)
    // Space Complexity: O(N)
    // ==========================================
    public boolean containsDuplicate(int[] nums) {
        Set<Integer> seen = new HashSet<>();

        for (int num : nums) {
            // Set.add returns false if the item was already in the set
            if (!seen.add(num)) {
                return true;
            }
        }

        return false;
    }

    // Local Test Runner
    public static void main(String[] args) {
        Solution solver = new Solution();

        // Test 1
        int[] nums1 = {1, 2, 3, 1};
        assert solver.containsDuplicate(nums1) : "Test 1 failed";
        System.out.println("Test 1 Passed: {1, 2, 3, 1} -> true");

        // Test 2
        int[] nums2 = {1, 2, 3, 4};
        assert !solver.containsDuplicate(nums2) : "Test 2 failed";
        System.out.println("Test 2 Passed: {1, 2, 3, 4} -> false");

        // Test 3
        int[] nums3 = {1, 1, 1, 3, 3, 4, 3, 2, 4, 2};
        assert solver.containsDuplicate(nums3) : "Test 3 failed";
        System.out.println("Test 3 Passed: {1, 1, 1, 3, ...} -> true");
    }
}
