/**
 * LeetCode 454: 4Sum II
 * Difficulty: Medium
 * Topic: Arrays & Hash Table / Meet-in-the-Middle
 *
 * Pattern: Meet-in-the-Middle Hash Map Tradeoff
 * Precompute pairwise sums of nums1 and nums2 in HashMap,
 * then match against -(nums3[k] + nums4[l]).
 *
 * Time Complexity: O(N^2)
 * Space Complexity: O(N^2)
 */

import java.util.HashMap;
import java.util.Map;

public class Solution {

    public int fourSumCount(int[] nums1, int[] nums2, int[] nums3, int[] nums4) {
        Map<Integer, Integer> sum12 = new HashMap<>();

        // Step 1: Precompute all pairs from nums1 and nums2
        for (int a : nums1) {
            for (int b : nums2) {
                int sum = a + b;
                sum12.put(sum, sum12.getOrDefault(sum, 0) + 1);
            }
        }

        // Step 2: Look up complementary negative sums from nums3 and nums4
        int count = 0;
        for (int c : nums3) {
            for (int d : nums4) {
                int target = -(c + d);
                count += sum12.getOrDefault(target, 0);
            }
        }

        return count;
    }

    public static void main(String[] args) {
        Solution solver = new Solution();

        int[] n1 = {1, 2};
        int[] n2 = {-2, -1};
        int[] n3 = {-1, 2};
        int[] n4 = {0, 2};
        System.out.println("Test 1: " + solver.fourSumCount(n1, n2, n3, n4)); // Expected: 2
    }
}
