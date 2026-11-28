/**
 * LeetCode 16: 3Sum Closest
 * Difficulty: Medium
 * Topic: Arrays & Two Pointers
 *
 * Pattern: Two-Pointer Convergent Gap Minimization
 * Sort array, fix element i, and converge left/right pointers.
 *
 * Time Complexity: O(N^2)
 * Space Complexity: O(1)
 */

import java.util.Arrays;

public class Solution {

    public int threeSumClosest(int[] nums, int target) {
        Arrays.sort(nums);
        int n = nums.length;
        int closestSum = nums[0] + nums[1] + nums[2];

        for (int i = 0; i < n - 2; i++) {
            if (i > 0 && nums[i] == nums[i - 1]) continue;

            int left = i + 1;
            int right = n - 1;

            while (left < right) {
                int currSum = nums[i] + nums[left] + nums[right];

                if (Math.abs(currSum - target) < Math.abs(closestSum - target)) {
                    closestSum = currSum;
                }

                if (currSum < target) {
                    left++;
                } else if (currSum > target) {
                    right--;
                } else {
                    return target;
                }
            }
        }

        return closestSum;
    }

    public static void main(String[] args) {
        Solution solver = new Solution();

        int[] test1 = {-1, 2, 1, -4};
        System.out.println("Test 1: " + solver.threeSumClosest(test1, 1)); // Expected: 2

        int[] test2 = {0, 0, 0};
        System.out.println("Test 2: " + solver.threeSumClosest(test2, 1)); // Expected: 0
    }
}
