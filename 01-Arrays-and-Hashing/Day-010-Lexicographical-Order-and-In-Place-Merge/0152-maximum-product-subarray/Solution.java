/**
 * LeetCode 152: Maximum Product Subarray
 * Difficulty: Medium
 * Topic: Arrays & Dynamic Programming
 *
 * Pattern: Dual-Extrema Tracking (Min-Max Product DP)
 * Maintain running maximum and minimum products ending at current position.
 * When encountering a negative number, max and min swap.
 *
 * Time Complexity: O(N)
 * Space Complexity: O(1)
 */

public class Solution {

    public int maxProduct(int[] nums) {
        if (nums == null || nums.length == 0) return 0;

        int maxProd = nums[0];
        int minProd = nums[0];
        int result = nums[0];

        for (int i = 1; i < nums.length; i++) {
            int num = nums[i];

            if (num < 0) {
                int temp = maxProd;
                maxProd = minProd;
                minProd = temp;
            }

            maxProd = Math.max(num, maxProd * num);
            minProd = Math.min(num, minProd * num);

            result = Math.max(result, maxProd);
        }

        return result;
    }

    public static void main(String[] args) {
        Solution solver = new Solution();

        int[] test1 = {2, 3, -2, 4};
        System.out.println("Test 1: " + solver.maxProduct(test1)); // Expected: 6

        int[] test2 = {-2, 0, -1};
        System.out.println("Test 2: " + solver.maxProduct(test2)); // Expected: 0

        int[] test3 = {-2, 3, -4};
        System.out.println("Test 3: " + solver.maxProduct(test3)); // Expected: 24
    }
}
