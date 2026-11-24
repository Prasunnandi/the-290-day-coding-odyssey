/**
 * LeetCode #128: Longest Consecutive Sequence
 * Difficulty: Medium
 * Topic: Arrays & Hashing
 * Pattern: Hash Set Intelligent Sequence Start Check
 * Link: https://leetcode.com/problems/longest-consecutive-sequence/
 */

import java.util.HashSet;
import java.util.Set;

public class Solution {

    // ==========================================
    // Approach: Hash Set with Sequence Start Optimization
    // Time Complexity: O(N) - each element visited at most twice
    // Space Complexity: O(N)
    // ==========================================
    public int longestConsecutive(int[] nums) {
        if (nums == null || nums.length == 0) {
            return 0;
        }

        Set<Integer> numSet = new HashSet<>();
        for (int num : nums) {
            numSet.add(num);
        }

        int longestStreak = 0;

        for (int num : numSet) {
            // Only initiate a streak if 'num' is the FIRST element of a sequence
            if (!numSet.contains(num - 1)) {
                int currentNum = num;
                int currentStreak = 1;

                while (numSet.contains(currentNum + 1)) {
                    currentNum++;
                    currentStreak++;
                }

                longestStreak = Math.max(longestStreak, currentStreak);
            }
        }

        return longestStreak;
    }

    // Local Test Runner
    public static void main(String[] args) {
        Solution solver = new Solution();

        int[] nums1 = {100, 4, 200, 1, 3, 2};
        int res1 = solver.longestConsecutive(nums1);
        System.out.println("Test 1 Result: " + res1); // Expected: 4
        assert res1 == 4 : "Test 1 failed";

        int[] nums2 = {0, 3, 7, 2, 5, 8, 4, 6, 0, 1};
        int res2 = solver.longestConsecutive(nums2);
        System.out.println("Test 2 Result: " + res2); // Expected: 9
        assert res2 == 9 : "Test 2 failed";

        System.out.println("All Java tests passed for LeetCode #128: Longest Consecutive Sequence!");
    }
}
