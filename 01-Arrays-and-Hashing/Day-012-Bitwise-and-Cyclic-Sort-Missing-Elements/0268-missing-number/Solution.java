/**
 * LeetCode 268: Missing Number
 * Difficulty: Easy
 * Topic: Arrays & Bit Manipulation
 *
 * Pattern: Bitwise XOR Cancellation
 * XOR all indices 0..n with all values in nums.
 * Duplicates cancel to 0; missing number remains.
 *
 * Time Complexity: O(N)
 * Space Complexity: O(1)
 */

public class Solution {

    public int missingNumber(int[] nums) {
        int n = nums.length;
        int missing = n;

        for (int i = 0; i < n; i++) {
            missing ^= (i ^ nums[i]);
        }

        return missing;
    }

    public static void main(String[] args) {
        Solution solver = new Solution();

        int[] test1 = {3, 0, 1};
        System.out.println("Test 1: " + solver.missingNumber(test1)); // Expected: 2

        int[] test2 = {0, 1};
        System.out.println("Test 2: " + solver.missingNumber(test2)); // Expected: 2

        int[] test3 = {9, 6, 4, 2, 3, 5, 7, 0, 1};
        System.out.println("Test 3: " + solver.missingNumber(test3)); // Expected: 8
    }
}
