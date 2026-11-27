/**
 * LeetCode 1004: Max Consecutive Ones III
 * Difficulty: Medium
 * Topic: Arrays & Sliding Window
 *
 * Pattern: Sliding Window with Zero Budget
 * Longest subarray with at most k zeroes.
 *
 * Time Complexity: O(N)
 * Space Complexity: O(1)
 */

public class Solution {

    public int longestOnes(int[] nums, int k) {
        int left = 0;
        int zeroCount = 0;
        int maxLen = 0;

        for (int right = 0; right < nums.length; right++) {
            if (nums[right] == 0) {
                zeroCount++;
            }

            while (zeroCount > k) {
                if (nums[left] == 0) {
                    zeroCount--;
                }
                left++;
            }

            maxLen = Math.max(maxLen, right - left + 1);
        }

        return maxLen;
    }

    public static void main(String[] args) {
        Solution solver = new Solution();

        int[] test1 = {1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 0};
        System.out.println("Test 1: " + solver.longestOnes(test1, 2)); // Expected: 6

        int[] test2 = {0, 0, 1, 1, 0, 0, 1, 1, 1, 0, 1, 1, 0, 0, 0, 1, 1, 1, 1};
        System.out.println("Test 2: " + solver.longestOnes(test2, 3)); // Expected: 10
    }
}
