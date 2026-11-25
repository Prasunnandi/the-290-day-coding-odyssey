/**
 * LeetCode #48: Rotate Image
 * Difficulty: Medium
 * Topic: Arrays & Hashing
 * Pattern: Matrix Transposition & Symmetry Reversal
 * Link: https://leetcode.com/problems/rotate-image/
 */

import java.util.Arrays;

public class Solution {

    // ==========================================
    // Approach: Transpose + Reverse Each Row
    // Time Complexity: O(N^2)
    // Space Complexity: O(1) in-place
    // ==========================================
    public void rotate(int[][] matrix) {
        int n = matrix.length;

        // Step 1: Transpose matrix along the main diagonal
        for (int r = 0; r < n; r++) {
            for (int c = r + 1; c < n; c++) {
                int temp = matrix[r][c];
                matrix[r][c] = matrix[c][r];
                matrix[c][r] = temp;
            }
        }

        // Step 2: Reverse each row using two pointers
        for (int r = 0; r < n; r++) {
            int left = 0;
            int right = n - 1;
            while (left < right) {
                int temp = matrix[r][left];
                matrix[r][left] = matrix[r][right];
                matrix[r][right] = temp;
                left++;
                right--;
            }
        }
    }

    // Local Test Runner
    public static void main(String[] args) {
        Solution solver = new Solution();

        int[][] m1 = {
            {1, 2, 3},
            {4, 5, 6},
            {7, 8, 9}
        };
        solver.rotate(m1);
        System.out.println("Test 1 Result: " + Arrays.deepToString(m1));
        int[][] expected = {
            {7, 4, 1},
            {8, 5, 2},
            {9, 6, 3}
        };
        assert Arrays.deepEquals(m1, expected) : "Test 1 failed";

        System.out.println("All Java tests passed for LeetCode #48: Rotate Image!");
    }
}
