/**
 * LeetCode 769: Max Chunks To Make Sorted
 * Difficulty: Medium
 * Topic: Arrays & Greedy
 *
 * Pattern: Permutation Index Invariant
 * A chunk boundary can be placed at index i if max(arr[0..i]) == i.
 *
 * Time Complexity: O(N)
 * Space Complexity: O(1)
 */

public class Solution {

    public int maxChunksToSorted(int[] arr) {
        int maxVal = 0;
        int chunks = 0;

        for (int i = 0; i < arr.length; i++) {
            maxVal = Math.max(maxVal, arr[i]);
            if (maxVal == i) {
                chunks++;
            }
        }

        return chunks;
    }

    public static void main(String[] args) {
        Solution solver = new Solution();

        int[] test1 = {4, 3, 2, 1, 0};
        System.out.println("Test 1: " + solver.maxChunksToSorted(test1)); // Expected: 1

        int[] test2 = {1, 0, 2, 3, 4};
        System.out.println("Test 2: " + solver.maxChunksToSorted(test2)); // Expected: 4
    }
}
