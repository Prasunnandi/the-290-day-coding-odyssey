/**
 * LeetCode 31: Next Permutation
 * Difficulty: Medium
 * Topic: Arrays & Hashing
 *
 * Pattern: Lexicographical Suffix Reversal
 * 1. Find pivot i such that nums[i] < nums[i + 1] scanning right-to-left.
 * 2. If found, find successor j > i such that nums[j] > nums[i].
 * 3. Swap nums[i] and nums[j].
 * 4. Reverse subarray nums[i + 1 .. n - 1].
 *
 * Time Complexity: O(N)
 * Space Complexity: O(1)
 */

import java.util.Arrays;

public class Solution {

    public void nextPermutation(int[] nums) {
        if (nums == null || nums.length <= 1) return;

        int n = nums.length;
        int i = n - 2;

        // Step 1: Find first element decreasing from the right
        while (i >= 0 && nums[i] >= nums[i + 1]) {
            i--;
        }

        if (i >= 0) {
            // Step 2: Find element just larger than nums[i]
            int j = n - 1;
            while (nums[j] <= nums[i]) {
                j--;
            }
            // Step 3: Swap nums[i] and nums[j]
            swap(nums, i, j);
        }

        // Step 4: Reverse the suffix from i + 1 to n - 1
        reverse(nums, i + 1, n - 1);
    }

    private void swap(int[] nums, int i, int j) {
        int temp = nums[i];
        nums[i] = nums[j];
        nums[j] = temp;
    }

    private void reverse(int[] nums, int start, int end) {
        while (start < end) {
            swap(nums, start, end);
            start++;
            end--;
        }
    }

    public static void main(String[] args) {
        Solution solver = new Solution();

        int[] arr1 = {1, 2, 3};
        solver.nextPermutation(arr1);
        System.out.println("Test 1: " + Arrays.toString(arr1)); // [1, 3, 2]

        int[] arr2 = {3, 2, 1};
        solver.nextPermutation(arr2);
        System.out.println("Test 2: " + Arrays.toString(arr2)); // [1, 2, 3]
    }
}
