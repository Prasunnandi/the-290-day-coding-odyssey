/**
 * LeetCode 215: Kth Largest Element in an Array
 * Difficulty: Medium
 * Topic: Arrays & Quickselect
 *
 * Pattern: Randomized 3-Way Quickselect (Hoare's Selection)
 * Target index is (nums.length - k) in ascending order.
 *
 * Time Complexity: O(N) average, O(N^2) worst-case
 * Space Complexity: O(1) auxiliary
 */

import java.util.Random;

public class Solution {

    private final Random rand = new Random();

    public int findKthLargest(int[] nums, int k) {
        int target = nums.length - k;
        return quickselect(nums, 0, nums.length - 1, target);
    }

    private int quickselect(int[] nums, int left, int right, int target) {
        if (left == right) {
            return nums[left];
        }

        // Random pivot to avoid worst-case O(N^2)
        int pivotIdx = left + rand.nextInt(right - left + 1);
        int pivot = nums[pivotIdx];

        // 3-Way Partitioning (Dutch National Flag)
        int lt = left;
        int i = left;
        int gt = right;

        while (i <= gt) {
            if (nums[i] < pivot) {
                swap(nums, lt++, i++);
            } else if (nums[i] > pivot) {
                swap(nums, i, gt--);
            } else {
                i++;
            }
        }

        if (target < lt) {
            return quickselect(nums, left, lt - 1, target);
        } else if (target > gt) {
            return quickselect(nums, gt + 1, right, target);
        } else {
            return nums[target];
        }
    }

    private void swap(int[] nums, int i, int j) {
        int temp = nums[i];
        nums[i] = nums[j];
        nums[j] = temp;
    }

    public static void main(String[] args) {
        Solution solver = new Solution();

        int[] test1 = {3, 2, 1, 5, 6, 4};
        System.out.println("Test 1: " + solver.findKthLargest(test1, 2)); // Expected: 5

        int[] test2 = {3, 2, 3, 1, 2, 4, 5, 5, 6};
        System.out.println("Test 2: " + solver.findKthLargest(test2, 4)); // Expected: 4
    }
}
