/**
 * LeetCode 229: Majority Element II
 * Difficulty: Medium
 * Topic: Arrays & Hashing
 *
 * Pattern: Extended Boyer-Moore Voting Algorithm (n / 3 threshold)
 * At most 2 elements can each appear > n / 3 times.
 * Candidate selection maintains 2 candidates and drops triples of 3 distinct values.
 * Second pass verifies candidates against threshold floor(n / 3).
 *
 * Time Complexity: O(N) — two sequential passes.
 * Space Complexity: O(1) auxiliary space (excluding returned List).
 */

import java.util.ArrayList;
import java.util.List;

public class Solution {

    /**
     * Finds all elements that appear more than n / 3 times.
     *
     * @param nums integer array
     * @return list containing up to 2 majority elements
     */
    public List<Integer> majorityElement(int[] nums) {
        List<Integer> result = new ArrayList<>();
        if (nums == null || nums.length == 0) {
            return result;
        }

        Integer cand1 = null;
        Integer cand2 = null;
        int count1 = 0;
        int count2 = 0;

        // Step 1: Boyer-Moore Candidate Selection
        for (int num : nums) {
            if (cand1 != null && num == cand1) {
                count1++;
            } else if (cand2 != null && num == cand2) {
                count2++;
            } else if (count1 == 0) {
                cand1 = num;
                count1 = 1;
            } else if (count2 == 0) {
                cand2 = num;
                count2 = 1;
            } else {
                count1--;
                count2--;
            }
        }

        // Step 2: Verification Pass
        int threshold = nums.length / 3;
        int freq1 = 0;
        int freq2 = 0;

        for (int num : nums) {
            if (cand1 != null && num == cand1) {
                freq1++;
            }
            if (cand2 != null && num == cand2) {
                freq2++;
            }
        }

        if (cand1 != null && freq1 > threshold) {
            result.add(cand1);
        }
        if (cand2 != null && !cand2.equals(cand1) && freq2 > threshold) {
            result.add(cand2);
        }

        return result;
    }

    public static void main(String[] args) {
        Solution solver = new Solution();

        int[] test1 = {3, 2, 3};
        System.out.println("Test 1: " + solver.majorityElement(test1)); // Expected: [3]

        int[] test2 = {1, 2};
        System.out.println("Test 2: " + solver.majorityElement(test2)); // Expected: [1, 2]
    }
}
