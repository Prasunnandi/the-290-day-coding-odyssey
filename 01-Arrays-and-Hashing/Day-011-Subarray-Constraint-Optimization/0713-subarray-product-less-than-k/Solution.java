/**
 * LeetCode 713: Subarray Product Less Than K
 * Difficulty: Medium
 * Topic: Arrays & Sliding Window
 *
 * Pattern: Sliding Window Subarray Counting
 * Count of new subarrays introduced by expanding right: (right - left + 1).
 *
 * Time Complexity: O(N)
 * Space Complexity: O(1)
 */

public class Solution {

    public int numSubarrayProductLessThanK(int[] nums, int k) {
        if (k <= 1) return 0;

        int left = 0;
        int prod = 1;
        int count = 0;

        for (int right = 0; right < nums.length; right++) {
            prod *= nums[right];

            while (prod >= k && left <= right) {
                prod /= nums[left];
                left++;
            }

            count += (right - left + 1);
        }

        return count;
    }

    public static void main(String[] args) {
        Solution solver = new Solution();

        int[] nums1 = {10, 5, 2, 6};
        System.out.println("Test 1: " + solver.numSubarrayProductLessThanK(nums1, 100)); // Expected: 8

        int[] nums2 = {1, 2, 3};
        System.out.println("Test 2: " + solver.numSubarrayProductLessThanK(nums2, 0)); // Expected: 0
    }
}
