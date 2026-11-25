/**
 * LeetCode #724: Find Pivot Index
 * Difficulty: Easy
 * Topic: Arrays & Hashing
 * Pattern: Total Sum vs Rolling Left Sum Balance
 * Link: https://leetcode.com/problems/find-pivot-index/
 */

public class Solution {

    // ==========================================
    // Approach: Total Sum & Rolling Left Sum
    // Time Complexity: O(N)
    // Space Complexity: O(1)
    // ==========================================
    public int pivotIndex(int[] nums) {
        int totalSum = 0;
        for (int num : nums) {
            totalSum += num;
        }

        int leftSum = 0;
        for (int i = 0; i < nums.length; i++) {
            // rightSum = totalSum - leftSum - nums[i]
            if (leftSum == totalSum - leftSum - nums[i]) {
                return i;
            }
            leftSum += nums[i];
        }

        return -1;
    }

    // Local Test Runner
    public static void main(String[] args) {
        Solution solver = new Solution();

        int[] nums1 = {1, 7, 3, 6, 5, 6};
        int res1 = solver.pivotIndex(nums1);
        System.out.println("Test 1 Result: " + res1); // Expected: 3
        assert res1 == 3 : "Test 1 failed";

        int[] nums2 = {1, 2, 3};
        int res2 = solver.pivotIndex(nums2);
        System.out.println("Test 2 Result: " + res2); // Expected: -1
        assert res2 == -1 : "Test 2 failed";

        int[] nums3 = {2, 1, -1};
        int res3 = solver.pivotIndex(nums3);
        System.out.println("Test 3 Result: " + res3); // Expected: 0
        assert res3 == 0 : "Test 3 failed";

        System.out.println("All Java tests passed for LeetCode #724: Find Pivot Index!");
    }
}
