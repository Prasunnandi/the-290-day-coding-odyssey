/**
 * LeetCode #974: Subarray Sums Divisible by K
 * Difficulty: Medium
 * Topic: Arrays & Hashing
 * Pattern: Prefix Sum + Modulo Arithmetic Congruence
 * Link: https://leetcode.com/problems/subarray-sums-divisible-by-k/
 */

public class Solution {

    // ==========================================
    // Approach: Prefix Sum + Frequency Array of Remainders
    // Because remainders range strictly from 0 to k-1, an int[k] array is faster than HashMap!
    // Negative modulo formula: ((sum % k) + k) % k
    // Time Complexity: O(N)
    // Space Complexity: O(K)
    // ==========================================
    public int subarraysDivByK(int[] nums, int k) {
        int count = 0;
        int currentSum = 0;

        // Array storing frequency of each remainder 0 to k-1
        int[] remainderCounts = new int[k];
        remainderCounts[0] = 1; // Base case for subarray whose sum is directly divisible by k

        for (int num : nums) {
            currentSum += num;
            // Handle negative remainders in Java
            int rem = ((currentSum % k) + k) % k;

            // Prior identical remainders form valid subarrays
            count += remainderCounts[rem];

            remainderCounts[rem]++;
        }

        return count;
    }

    // Local Test Runner
    public static void main(String[] args) {
        Solution solver = new Solution();

        int[] nums1 = {4, 5, 0, -2, -3, 1};
        int k1 = 5;
        int res1 = solver.subarraysDivByK(nums1, k1);
        System.out.println("Test 1 Result: " + res1); // Expected: 7
        assert res1 == 7 : "Test 1 failed";

        int[] nums2 = {5};
        int k2 = 9;
        int res2 = solver.subarraysDivByK(nums2, k2);
        System.out.println("Test 2 Result: " + res2); // Expected: 0
        assert res2 == 0 : "Test 2 failed";

        System.out.println("All Java tests passed for LeetCode #974: Subarray Sums Divisible by K!");
    }
}
