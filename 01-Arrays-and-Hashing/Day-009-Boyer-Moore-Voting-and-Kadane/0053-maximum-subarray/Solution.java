/**
 * LeetCode 53: Maximum Subarray
 * Difficulty: Medium
 * Topic: Arrays & Dynamic Programming
 *
 * Pattern: Kadane's Algorithm
 * Dynamic Programming State:
 *   dp[i] = max(nums[i], dp[i - 1] + nums[i])
 * Optimized to O(1) space by tracking currentMax and globalMax.
 *
 * Time Complexity: O(N) — single linear pass.
 * Space Complexity: O(1) — constant auxiliary space.
 */

public class Solution {

    /**
     * Finds the contiguous subarray with the largest sum.
     *
     * @param nums integer array
     * @return maximum subarray sum
     */
    public int maxSubArray(int[] nums) {
        int currentMax = nums[0];
        int globalMax = nums[0];

        for (int i = 1; i < nums.length; i++) {
            // Either append nums[i] to existing subarray or start anew at nums[i]
            currentMax = Math.max(nums[i], currentMax + nums[i]);
            globalMax = Math.max(globalMax, currentMax);
        }

        return globalMax;
    }

    public static void main(String[] args) {
        Solution solver = new Solution();

        int[] test1 = {-2, 1, -3, 4, -1, 2, 1, -5, 4};
        System.out.println("Test 1: " + solver.maxSubArray(test1)); // Expected: 6

        int[] test2 = {1};
        System.out.println("Test 2: " + solver.maxSubArray(test2)); // Expected: 1

        int[] test3 = {-5, -2, -8, -1, -4};
        System.out.println("Test 3: " + solver.maxSubArray(test3)); // Expected: -1
    }
}
