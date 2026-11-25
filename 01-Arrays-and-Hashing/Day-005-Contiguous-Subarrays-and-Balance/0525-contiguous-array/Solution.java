/**
 * LeetCode #525: Contiguous Array
 * Difficulty: Medium
 * Topic: Arrays & Hashing
 * Pattern: Prefix Sum with Value Transformation (0 -> -1 Balance Counter)
 * Link: https://leetcode.com/problems/contiguous-array/
 */

import java.util.HashMap;
import java.util.Map;

public class Solution {

    // ==========================================
    // Approach: Value Transformation (0 -> -1) & Prefix Sum Map
    // Time Complexity: O(N)
    // Space Complexity: O(N)
    // ==========================================
    public int findMaxLength(int[] nums) {
        Map<Integer, Integer> prefixMap = new HashMap<>();
        prefixMap.put(0, -1); // Base case: prefix sum 0 occurs before the array starts

        int maxLength = 0;
        int currentSum = 0;

        for (int i = 0; i < nums.length; i++) {
            // Transform 0 into -1, keep 1 as +1
            currentSum += (nums[i] == 1) ? 1 : -1;

            if (prefixMap.containsKey(currentSum)) {
                int previousIndex = prefixMap.get(currentSum);
                maxLength = Math.max(maxLength, i - previousIndex);
            } else {
                // Record only the first appearance of currentSum
                prefixMap.put(currentSum, i);
            }
        }

        return maxLength;
    }

    // Local Test Runner
    public static void main(String[] args) {
        Solution solver = new Solution();

        int[] nums1 = {0, 1};
        assert solver.findMaxLength(nums1) == 2 : "Test 1 failed";
        System.out.println("Test 1 Result: " + solver.findMaxLength(nums1)); // Expected: 2

        int[] nums2 = {0, 1, 0};
        assert solver.findMaxLength(nums2) == 2 : "Test 2 failed";
        System.out.println("Test 2 Result: " + solver.findMaxLength(nums2)); // Expected: 2

        int[] nums3 = {0, 0, 1, 0, 0, 0, 1, 1};
        assert solver.findMaxLength(nums3) == 6 : "Test 3 failed";
        System.out.println("Test 3 Result: " + solver.findMaxLength(nums3)); // Expected: 6

        System.out.println("All Java tests passed for LeetCode #525: Contiguous Array!");
    }
}
