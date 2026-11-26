/**
 * LeetCode 448: Find All Numbers Disappeared in an Array
 * Difficulty: Easy
 * Topic: Arrays & Hashing
 *
 * Pattern: Sign Inversion / In-Place Index Marking
 * For each number val in nums, we negate nums[Math.abs(val) - 1] to mark
 * index (Math.abs(val) - 1) as visited.
 * Any index i that remains positive after the scan indicates (i + 1) was absent.
 *
 * Time Complexity: O(N) — two sequential linear passes.
 * Space Complexity: O(1) auxiliary space (excluding returned List).
 */

import java.util.ArrayList;
import java.util.List;

public class Solution {

    /**
     * Finds all integers in the range [1, n] that do not appear in nums.
     *
     * @param nums integer array where 1 <= nums[i] <= n
     * @return list of missing integers
     */
    public List<Integer> findDisappearedNumbers(int[] nums) {
        int n = nums.length;

        // Step 1: Invert sign of numbers at index abs(val) - 1
        for (int i = 0; i < n; i++) {
            int targetIndex = Math.abs(nums[i]) - 1;
            if (nums[targetIndex] > 0) {
                nums[targetIndex] = -nums[targetIndex];
            }
        }

        // Step 2: Positive value at index i means (i + 1) is missing
        List<Integer> result = new ArrayList<>();
        for (int i = 0; i < n; i++) {
            if (nums[i] > 0) {
                result.add(i + 1);
            } else {
                // Restore original positive value
                nums[i] = -nums[i];
            }
        }

        return result;
    }

    public static void main(String[] args) {
        Solution solver = new Solution();

        int[] test1 = {4, 3, 2, 7, 8, 2, 3, 1};
        System.out.println("Test 1: " + solver.findDisappearedNumbers(test1)); // Expected: [5, 6]

        int[] test2 = {1, 1};
        System.out.println("Test 2: " + solver.findDisappearedNumbers(test2)); // Expected: [2]
    }
}
