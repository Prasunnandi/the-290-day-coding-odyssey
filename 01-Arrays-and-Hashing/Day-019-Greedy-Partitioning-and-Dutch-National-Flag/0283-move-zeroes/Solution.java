/**
 * LeetCode 283: Move Zeroes
 * Difficulty: Easy
 * Topic: Arrays & Two Pointers
 *
 * Pattern: Two Pointers In-Place Compaction
 * Slow write pointer and fast read pointer swap non-zeroes to the front.
 *
 * Time Complexity: O(N)
 * Space Complexity: O(1)
 */

import java.util.Arrays;

public class Solution {

    public void moveZeroes(int[] nums) {
        int slow = 0;
        for (int fast = 0; fast < nums.length; fast++) {
            if (nums[fast] != 0) {
                int temp = nums[slow];
                nums[slow] = nums[fast];
                nums[fast] = temp;
                slow++;
            }
        }
    }

    public static void main(String[] args) {
        Solution solver = new Solution();

        int[] arr1 = {0, 1, 0, 3, 12};
        solver.moveZeroes(arr1);
        System.out.println("Test 1: " + Arrays.toString(arr1)); // Expected: [1, 3, 12, 0, 0]

        int[] arr2 = {0};
        solver.moveZeroes(arr2);
        System.out.println("Test 2: " + Arrays.toString(arr2)); // Expected: [0]
    }
}
