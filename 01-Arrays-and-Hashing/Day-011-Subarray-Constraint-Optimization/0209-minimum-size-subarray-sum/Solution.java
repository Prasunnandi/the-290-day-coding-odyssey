/**
 * LeetCode 209: Minimum Size Subarray Sum
 * Difficulty: Medium
 * Topic: Arrays & Sliding Window
 *
 * Pattern: Shrinking Sliding Window
 * Expand right pointer to reach target, contract left pointer to minimize window.
 *
 * Time Complexity: O(N)
 * Space Complexity: O(1)
 */

public class Solution {

    public int minSubArrayLen(int target, int[] nums) {
        int n = nums.length;
        int left = 0;
        int currentSum = 0;
        int minLen = Integer.MAX_VALUE;

        for (int right = 0; right < n; right++) {
            currentSum += nums[right];

            while (currentSum >= target) {
                minLen = Math.min(minLen, right - left + 1);
                currentSum -= nums[left];
                left++;
            }
        }

        return (minLen == Integer.MAX_VALUE) ? 0 : minLen;
    }

    public static void main(String[] args) {
        Solution solver = new Solution();

        int[] nums1 = {2, 3, 1, 2, 4, 3};
        System.out.println("Test 1: " + solver.minSubArrayLen(7, nums1)); // Expected: 2

        int[] nums2 = {1, 4, 4};
        System.out.println("Test 2: " + solver.minSubArrayLen(4, nums2)); // Expected: 1

        int[] nums3 = {1, 1, 1, 1, 1, 1, 1, 1};
        System.out.println("Test 3: " + solver.minSubArrayLen(11, nums3)); // Expected: 0
    }
}
