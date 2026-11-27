/**
 * LeetCode 645: Set Mismatch
 * Difficulty: Easy
 * Topic: Arrays & Hashing
 *
 * Pattern: Sign Inversion Index Marking
 * Negate nums[abs(x) - 1] to detect duplicate (already negative)
 * and missing (remains positive).
 *
 * Time Complexity: O(N)
 * Space Complexity: O(1)
 */

import java.util.Arrays;

public class Solution {

    public int[] findErrorNums(int[] nums) {
        int duplicate = -1;
        int missing = -1;

        for (int i = 0; i < nums.length; i++) {
            int val = Math.abs(nums[i]);
            int idx = val - 1;

            if (nums[idx] < 0) {
                duplicate = val;
            } else {
                nums[idx] = -nums[idx];
            }
        }

        for (int i = 0; i < nums.length; i++) {
            if (nums[i] > 0) {
                missing = i + 1;
            } else {
                nums[i] = -nums[i]; // restore original values
            }
        }

        return new int[]{duplicate, missing};
    }

    public static void main(String[] args) {
        Solution solver = new Solution();

        int[] test1 = {1, 2, 2, 4};
        System.out.println("Test 1: " + Arrays.toString(solver.findErrorNums(test1))); // Expected: [2, 3]

        int[] test2 = {1, 1};
        System.out.println("Test 2: " + Arrays.toString(solver.findErrorNums(test2))); // Expected: [1, 2]
    }
}
