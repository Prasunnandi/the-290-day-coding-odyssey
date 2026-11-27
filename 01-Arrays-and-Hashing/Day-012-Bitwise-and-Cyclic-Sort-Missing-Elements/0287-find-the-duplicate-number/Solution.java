/**
 * LeetCode 287: Find the Duplicate Number
 * Difficulty: Medium
 * Topic: Arrays & Two Pointers
 *
 * Pattern: Floyd's Cycle Detection (Tortoise and Hare)
 * Maps indices to values: i -> nums[i].
 * Detects the cycle entrance node which corresponds to the duplicate.
 * Strictly O(1) space and does NOT modify nums.
 *
 * Time Complexity: O(N)
 * Space Complexity: O(1)
 */

public class Solution {

    public int findDuplicate(int[] nums) {
        // Phase 1: Detect cycle
        int slow = nums[0];
        int fast = nums[0];

        do {
            slow = nums[slow];
            fast = nums[nums[fast]];
        } while (slow != fast);

        // Phase 2: Find entrance to the cycle
        int slow2 = nums[0];
        while (slow != slow2) {
            slow = nums[slow];
            slow2 = nums[slow2];
        }

        return slow;
    }

    public static void main(String[] args) {
        Solution solver = new Solution();

        int[] test1 = {1, 3, 4, 2, 2};
        System.out.println("Test 1: " + solver.findDuplicate(test1)); // Expected: 2

        int[] test2 = {3, 1, 3, 4, 2};
        System.out.println("Test 2: " + solver.findDuplicate(test2)); // Expected: 3
    }
}
