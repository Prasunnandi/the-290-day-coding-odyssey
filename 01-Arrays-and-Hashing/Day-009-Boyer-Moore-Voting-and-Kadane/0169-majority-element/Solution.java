/**
 * LeetCode 169: Majority Element
 * Difficulty: Easy
 * Topic: Arrays & Hashing
 *
 * Pattern: Boyer-Moore Voting Algorithm
 * If an element occurs more than n / 2 times, pairings of distinct elements
 * will always leave the majority element standing.
 *
 * Time Complexity: O(N) — single pass.
 * Space Complexity: O(1) — constant extra space.
 */

public class Solution {

    /**
     * Finds the majority element in O(N) time and O(1) space.
     *
     * @param nums integer array of size n
     * @return majority element
     */
    public int majorityElement(int[] nums) {
        int candidate = 0;
        int count = 0;

        for (int num : nums) {
            if (count == 0) {
                candidate = num;
            }
            count += (num == candidate) ? 1 : -1;
        }

        return candidate;
    }

    public static void main(String[] args) {
        Solution solver = new Solution();

        int[] test1 = {3, 2, 3};
        System.out.println("Test 1: " + solver.majorityElement(test1)); // Expected: 3

        int[] test2 = {2, 2, 1, 1, 1, 2, 2};
        System.out.println("Test 2: " + solver.majorityElement(test2)); // Expected: 2
    }
}
