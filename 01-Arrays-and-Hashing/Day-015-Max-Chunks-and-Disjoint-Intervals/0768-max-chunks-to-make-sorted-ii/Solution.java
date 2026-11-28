/**
 * LeetCode 768: Max Chunks To Make Sorted II
 * Difficulty: Hard
 * Topic: Arrays & Prefix-Suffix Extrema
 *
 * Pattern: Prefix Max <= Suffix Min Partition Invariant
 * Cut is valid at index i if max(arr[0..i]) <= min(arr[i+1..n-1]).
 *
 * Time Complexity: O(N)
 * Space Complexity: O(N)
 */

public class Solution {

    public int maxChunksToSorted(int[] arr) {
        int n = arr.length;
        if (n <= 1) return n;

        int[] minRight = new int[n];
        minRight[n - 1] = arr[n - 1];

        for (int i = n - 2; i >= 0; i--) {
            minRight[i] = Math.min(arr[i], minRight[i + 1]);
        }

        int chunks = 0;
        int maxLeft = Integer.MIN_VALUE;

        for (int i = 0; i < n - 1; i++) {
            maxLeft = Math.max(maxLeft, arr[i]);
            if (maxLeft <= minRight[i + 1]) {
                chunks++;
            }
        }

        return chunks + 1;
    }

    public static void main(String[] args) {
        Solution solver = new Solution();

        int[] test1 = {5, 4, 3, 2, 1};
        System.out.println("Test 1: " + solver.maxChunksToSorted(test1)); // Expected: 1

        int[] test2 = {2, 1, 3, 4, 4};
        System.out.println("Test 2: " + solver.maxChunksToSorted(test2)); // Expected: 4
    }
}
