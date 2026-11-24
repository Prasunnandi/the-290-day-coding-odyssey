/**
 * LeetCode #560: Subarray Sum Equals K
 * Difficulty: Medium
 * Topic: Arrays & Hashing
 * Pattern: Prefix Sum + Hash Map (Target Complement Counting)
 * Link: https://leetcode.com/problems/subarray-sum-equals-k/
 */

import java.util.HashMap;
import java.util.Map;

public class Solution {

    // ==========================================
    // Approach: Prefix Sum + Frequency Hash Map
    // Time Complexity: O(N)
    // Space Complexity: O(N)
    // ==========================================
    public int subarraySum(int[] nums, int k) {
        int count = 0;
        int currentSum = 0;

        // Map stores: {prefixSum -> frequency}
        Map<Integer, Integer> prefixCounts = new HashMap<>();
        prefixCounts.put(0, 1); // Base case for subarray starting at index 0

        for (int num : nums) {
            currentSum += num;
            int complement = currentSum - k;

            // If (currentSum - k) exists, add its occurrences to total count
            if (prefixCounts.containsKey(complement)) {
                count += prefixCounts.get(complement);
            }

            prefixCounts.put(currentSum, prefixCounts.getOrDefault(currentSum, 0) + 1);
        }

        return count;
    }

    // Local Test Runner
    public static void main(String[] args) {
        Solution solver = new Solution();

        int[] nums1 = {1, 1, 1};
        int k1 = 2;
        int res1 = solver.subarraySum(nums1, k1);
        System.out.println("Test 1 Result: " + res1); // Expected: 2
        assert res1 == 2 : "Test 1 failed";

        int[] nums2 = {1, -1, 0};
        int k2 = 0;
        int res2 = solver.subarraySum(nums2, k2);
        System.out.println("Test 2 Result: " + res2); // Expected: 3
        assert res2 == 3 : "Test 2 failed";

        System.out.println("All Java tests passed for LeetCode #560: Subarray Sum Equals K!");
    }
}
