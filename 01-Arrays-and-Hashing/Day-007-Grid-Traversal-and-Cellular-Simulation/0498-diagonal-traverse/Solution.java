/**
 * LeetCode #498: Diagonal Traverse
 * Difficulty: Medium
 * Topic: Arrays & Hashing
 * Pattern: Diagonal Index Invariance (r + c = d) & Zigzag Parity
 * Link: https://leetcode.com/problems/diagonal-traverse/
 */

import java.util.Arrays;

public class Solution {

    // ==========================================
    // Approach: Direct Simulation with Direction Reflection
    // Time Complexity: O(M * N)
    // Space Complexity: O(1) auxiliary (excluding return array)
    // ==========================================
    public int[] findDiagonalOrder(int[][] mat) {
        if (mat == null || mat.length == 0) {
            return new int[0];
        }

        int m = mat.length;
        int n = mat[0].length;
        int[] result = new int[m * n];

        int r = 0, c = 0;
        boolean up = true;

        for (int i = 0; i < m * n; i++) {
            result[i] = mat[r][c];

            if (up) {
                if (c == n - 1) {
                    r++;
                    up = false;
                } else if (r == 0) {
                    c++;
                    up = false;
                } else {
                    r--;
                    c++;
                }
            } else {
                if (r == m - 1) {
                    c++;
                    up = true;
                } else if (c == 0) {
                    r++;
                    up = true;
                } else {
                    r++;
                    c--;
                }
            }
        }

        return result;
    }

    // Local Test Runner
    public static void main(String[] args) {
        Solution solver = new Solution();

        int[][] mat1 = {
            {1, 2, 3},
            {4, 5, 6},
            {7, 8, 9}
        };
        int[] res1 = solver.findDiagonalOrder(mat1);
        int[] expected1 = {1, 2, 4, 7, 5, 3, 6, 8, 9};
        System.out.println("Test 1 Result: " + Arrays.toString(res1));
        assert Arrays.equals(res1, expected1) : "Test 1 failed";

        System.out.println("All Java tests passed for LeetCode #498: Diagonal Traverse!");
    }
}
