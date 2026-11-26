/**
 * LeetCode 442: Find All Duplicates in an Array
 * Difficulty: Medium
 * Topic: Arrays & Hashing
 *
 * Pattern: Sign Inversion / In-Place Frequency Flag
 * Iterate through the array. For each value val:
 * - Map to index idx = Math.abs(val) - 1.
 * - If nums[idx] < 0, then val is encountered for the 2nd time -> add to result.
 * - Otherwise, negate nums[idx] to register the 1st encounter.
 *
 * Time Complexity: O(N) — single pass.
 * Space Complexity: O(1) auxiliary space (excluding returned List).
 */

import java.util.ArrayList;
import java.util.List;

public class Solution {

    /**
     * Finds all integers that appear twice in the array.
     *
     * @param nums array of length n where 1 <= nums[i] <= n
     * @return list of duplicate integers
     */
    public List<Integer> findDuplicates(int[] nums) {
        List<Integer> duplicates = new ArrayList<>();
        int n = nums.length;

        for (int i = 0; i < n; i++) {
            int val = Math.abs(nums[i]);
            int targetIndex = val - 1;

            if (nums[targetIndex] < 0) {
                // Already negated => visited previously => duplicate
                duplicates.add(val);
            } else {
                // First visit => mark visited by negating
                nums[targetIndex] = -nums[targetIndex];
            }
        }

        // Optional: restore array to original positive values
        for (int i = 0; i < n; i++) {
            nums[i] = Math.abs(nums[i]);
        }

        return duplicates;
    }

    public static void main(String[] args) {
        Solution solver = new Solution();

        int[] test1 = {4, 3, 2, 7, 8, 2, 3, 1};
        System.out.println("Test 1: " + solver.findDuplicates(test1)); // Expected: [2, 3]

        int[] test2 = {1, 1, 2};
        System.out.println("Test 2: " + solver.findDuplicates(test2)); // Expected: [1]
    }
}
