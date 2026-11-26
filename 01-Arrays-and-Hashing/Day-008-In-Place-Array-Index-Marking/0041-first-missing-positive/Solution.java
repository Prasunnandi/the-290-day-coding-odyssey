/**
 * LeetCode 41: First Missing Positive
 * Difficulty: Hard
 * Topic: Arrays & Hashing
 *
 * Pattern: Cyclic Sort / In-Place Index Mapping
 * The smallest missing positive integer must fall in range [1, n + 1].
 * By swapping every element x where 1 <= x <= n to its bucket index (x - 1),
 * we establish the invariant nums[i] == i + 1 for all valid numbers present.
 *
 * Time Complexity: O(N) — each swap places at least one element into its correct slot.
 * Space Complexity: O(1) — purely in-place array element swaps.
 */

public class Solution {

    /**
     * Returns the smallest missing positive integer in O(N) time and O(1) space.
     *
     * @param nums unsorted integer array
     * @return smallest missing positive integer
     */
    public int firstMissingPositive(int[] nums) {
        int n = nums.length;

        // Step 1: Cyclic Sort into target positions (nums[i] belongs at nums[i] - 1)
        for (int i = 0; i < n; i++) {
            while (nums[i] >= 1 && nums[i] <= n && nums[nums[i] - 1] != nums[i]) {
                int targetIndex = nums[i] - 1;
                // Swap nums[i] and nums[targetIndex]
                int temp = nums[i];
                nums[i] = nums[targetIndex];
                nums[targetIndex] = temp;
            }
        }

        // Step 2: Identify the first discrepancy
        for (int i = 0; i < n; i++) {
            if (nums[i] != i + 1) {
                return i + 1;
            }
        }

        // All numbers 1 to n are present
        return n + 1;
    }

    public static void main(String[] args) {
        Solution solver = new Solution();

        int[] test1 = {1, 2, 0};
        System.out.println("Test 1: " + solver.firstMissingPositive(test1)); // Expected: 3

        int[] test2 = {3, 4, -1, 1};
        System.out.println("Test 2: " + solver.firstMissingPositive(test2)); // Expected: 2

        int[] test3 = {7, 8, 9, 11, 12};
        System.out.println("Test 3: " + solver.firstMissingPositive(test3)); // Expected: 1
    }
}
