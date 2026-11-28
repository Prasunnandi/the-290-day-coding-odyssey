/**
 * LeetCode 75: Sort Colors
 * Difficulty: Medium
 * Topic: Arrays & Dutch National Flag
 *
 * Pattern: Dijkstra's Dutch National Flag (3-Way In-Place Partitioning)
 * Three pointers: low, mid, high.
 *
 * Time Complexity: O(N)
 * Space Complexity: O(1)
 */

import java.util.Arrays;

public class Solution {

    public void sortColors(int[] nums) {
        int low = 0;
        int mid = 0;
        int high = nums.length - 1;

        while (mid <= high) {
            if (nums[mid] == 0) {
                swap(nums, low, mid);
                low++;
                mid++;
            } else if (nums[mid] == 1) {
                mid++;
            } else {
                swap(nums, mid, high);
                high--;
            }
        }
    }

    private void swap(int[] nums, int i, int j) {
        int temp = nums[i];
        nums[i] = nums[j];
        nums[j] = temp;
    }

    public static void main(String[] args) {
        Solution solver = new Solution();

        int[] arr1 = {2, 0, 2, 1, 1, 0};
        solver.sortColors(arr1);
        System.out.println("Test 1: " + Arrays.toString(arr1)); // Expected: [0, 0, 1, 1, 2, 2]

        int[] arr2 = {2, 0, 1};
        solver.sortColors(arr2);
        System.out.println("Test 2: " + Arrays.toString(arr2)); // Expected: [0, 1, 2]
    }
}
