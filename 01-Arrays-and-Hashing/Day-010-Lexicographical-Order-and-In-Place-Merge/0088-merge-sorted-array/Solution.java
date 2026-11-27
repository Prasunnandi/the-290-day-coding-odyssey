/**
 * LeetCode 88: Merge Sorted Array
 * Difficulty: Easy
 * Topic: Arrays & Two Pointers
 *
 * Pattern: Three-Pointer Reverse Placement
 * Merge elements from the back (m + n - 1) backwards to 0
 * to avoid overwriting elements in nums1.
 *
 * Time Complexity: O(m + n)
 * Space Complexity: O(1)
 */

import java.util.Arrays;

public class Solution {

    public void merge(int[] nums1, int m, int[] nums2, int n) {
        int p1 = m - 1;
        int p2 = n - 1;
        int p = m + n - 1;

        while (p2 >= 0) {
            if (p1 >= 0 && nums1[p1] > nums2[p2]) {
                nums1[p] = nums1[p1];
                p1--;
            } else {
                nums1[p] = nums2[p2];
                p2--;
            }
            p--;
        }
    }

    public static void main(String[] args) {
        Solution solver = new Solution();

        int[] nums1_1 = {1, 2, 3, 0, 0, 0};
        int[] nums2_1 = {2, 5, 6};
        solver.merge(nums1_1, 3, nums2_1, 3);
        System.out.println("Test 1: " + Arrays.toString(nums1_1)); // [1, 2, 2, 3, 5, 6]

        int[] nums1_2 = {0};
        int[] nums2_2 = {1};
        solver.merge(nums1_2, 0, nums2_2, 1);
        System.out.println("Test 2: " + Arrays.toString(nums1_2)); // [1]
    }
}
