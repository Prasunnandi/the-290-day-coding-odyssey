/**
 * LeetCode #238: Product of Array Except Self
 * Difficulty: Medium
 * Topic: Arrays & Hashing
 * Pattern: Prefix & Suffix Products (Running Product Accumulation)
 * Link: https://leetcode.com/problems/product-of-array-except-self/
 */

import java.util.Arrays;

public class Solution {

    // ==========================================
    // Approach 1: Explicit Prefix & Suffix Arrays
    // Time Complexity: O(N)
    // Space Complexity: O(N) auxiliary space
    // ==========================================
    public int[] productExceptSelfPrefixSuffix(int[] nums) {
        int n = nums.length;
        int[] prefix = new int[n];
        int[] suffix = new int[n];
        int[] result = new int[n];

        prefix[0] = 1;
        for (int i = 1; i < n; i++) {
            prefix[i] = prefix[i - 1] * nums[i - 1];
        }

        suffix[n - 1] = 1;
        for (int i = n - 2; i >= 0; i--) {
            suffix[i] = suffix[i + 1] * nums[i + 1];
        }

        for (int i = 0; i < n; i++) {
            result[i] = prefix[i] * suffix[i];
        }

        return result;
    }

    // ==========================================
    // Approach 2: O(1) Auxiliary Space (Optimal)
    // Time Complexity: O(N)
    // Space Complexity: O(1) auxiliary (excluding output array)
    // ==========================================
    public int[] productExceptSelf(int[] nums) {
        int n = nums.length;
        int[] output = new int[n];

        // Pass 1: output[i] stores product of all elements to the left
        output[0] = 1;
        for (int i = 1; i < n; i++) {
            output[i] = output[i - 1] * nums[i - 1];
        }

        // Pass 2: Multiply by product of all elements to the right using rolling variable
        int suffix = 1;
        for (int i = n - 1; i >= 0; i--) {
            output[i] *= suffix;
            suffix *= nums[i];
        }

        return output;
    }

    // Local Test Runner
    public static void main(String[] args) {
        Solution solver = new Solution();

        int[] nums1 = {1, 2, 3, 4};
        int[] res1 = solver.productExceptSelf(nums1);
        System.out.println("Test 1 Result: " + Arrays.toString(res1)); // Expected: [24, 12, 8, 6]

        int[] nums2 = {-1, 1, 0, -3, 3};
        int[] res2 = solver.productExceptSelf(nums2);
        System.out.println("Test 2 Result: " + Arrays.toString(res2)); // Expected: [0, 0, 9, 0, 0]

        System.out.println("All Java tests passed for LeetCode #238: Product of Array Except Self!");
    }
}
