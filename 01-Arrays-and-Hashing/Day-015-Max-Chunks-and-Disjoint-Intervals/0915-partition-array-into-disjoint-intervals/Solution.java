/**
 * LeetCode 915: Partition Array into Disjoint Intervals
 * Difficulty: Medium
 * Topic: Arrays & Greedy
 *
 * Pattern: One-Pass Greedy Horizon Expansion
 * Track maxLeft and currMax. If nums[i] < maxLeft, expand partition to i.
 *
 * Time Complexity: O(N)
 * Space Complexity: O(1)
 */

public class Solution {

    public int partitionDisjoint(int[] nums) {
        int maxLeft = nums[0];
        int currMax = nums[0];
        int partitionIdx = 0;

        for (int i = 1; i < nums.length; i++) {
            currMax = Math.max(currMax, nums[i]);
            if (nums[i] < maxLeft) {
                partitionIdx = i;
                maxLeft = currMax;
            }
        }

        return partitionIdx + 1;
    }

    public static void main(String[] args) {
        Solution solver = new Solution();

        int[] test1 = {5, 0, 3, 8, 6};
        System.out.println("Test 1: " + solver.partitionDisjoint(test1)); // Expected: 3

        int[] test2 = {1, 1, 1, 0, 6, 12};
        System.out.println("Test 2: " + solver.partitionDisjoint(test2)); // Expected: 4
    }
}
