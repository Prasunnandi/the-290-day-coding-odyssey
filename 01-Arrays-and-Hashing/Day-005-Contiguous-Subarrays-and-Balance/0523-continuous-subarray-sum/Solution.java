/**
 * LeetCode #523: Continuous Subarray Sum
 * Difficulty: Medium
 * Topic: Arrays & Hashing
 * Pattern: Prefix Sum Modulo Hash Map (First Occurrence Index Tracking)
 * Link: https://leetcode.com/problems/continuous-subarray-sum/
 */

import java.util.HashMap;
import java.util.Map;

public class Solution {

    // ==========================================
    // Approach: Prefix Sum Modulo with First Occurrence Map
    // Time Complexity: O(N)
    // Space Complexity: O(min(N, K))
    // ==========================================
    public boolean checkSubarraySum(int[] nums, int k) {
        // Map: remainder -> first seen index
        Map<Integer, Integer> remainderMap = new HashMap<>();
        remainderMap.put(0, -1); // Base case for subarray starting at index 0

        int currentSum = 0;

        for (int i = 0; i < nums.length; i++) {
            currentSum += nums[i];
            int remainder = currentSum % k;

            if (remainderMap.containsKey(remainder)) {
                // Verify length is at least 2
                if (i - remainderMap.get(remainder) >= 2) {
                    return true;
                }
            } else {
                // Crucial: Only store the first occurrence to maximize subarray length
                remainderMap.put(remainder, i);
            }
        }

        return false;
    }

    // Local Test Runner
    public static void main(String[] args) {
        Solution solver = new Solution();

        int[] nums1 = {23, 2, 4, 6, 7};
        int k1 = 6;
        assert solver.checkSubarraySum(nums1, k1) : "Test 1 failed";
        System.out.println("Test 1 Result: " + solver.checkSubarraySum(nums1, k1)); // Expected: true

        int[] nums2 = {23, 2, 6, 4, 7};
        int k2 = 13;
        assert !solver.checkSubarraySum(nums2, k2) : "Test 2 failed";
        System.out.println("Test 2 Result: " + solver.checkSubarraySum(nums2, k2)); // Expected: false

        int[] nums3 = {0, 0};
        int k3 = 1;
        assert solver.checkSubarraySum(nums3, k3) : "Test 3 failed";
        System.out.println("Test 3 Result: " + solver.checkSubarraySum(nums3, k3)); // Expected: true

        System.out.println("All Java tests passed for LeetCode #523: Continuous Subarray Sum!");
    }
}
