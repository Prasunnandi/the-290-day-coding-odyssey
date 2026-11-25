/**
 * LeetCode #73: Set Matrix Zeroes
 * Difficulty: Medium
 * Topic: Arrays & Hashing
 * Pattern: In-Place Matrix State Marking (Using 1st Row and 1st Column as Markers)
 * Link: https://leetcode.com/problems/set-matrix-zeroes/
 */

import java.util.Arrays;

public class Solution {

    // ==========================================
    // Optimal Approach: O(1) Auxiliary Space
    // Time Complexity: O(M * N)
    // Space Complexity: O(1)
    // ==========================================
    public void setZeroes(int[][] matrix) {
        int m = matrix.length;
        int n = matrix[0].length;
        boolean firstColZero = false;

        // Step 1: Scan and record zeros in the first row & column
        for (int r = 0; r < m; r++) {
            if (matrix[r][0] == 0) {
                firstColZero = true;
            }
            for (int c = 1; c < n; c++) {
                if (matrix[r][c] == 0) {
                    matrix[r][0] = 0;
                    matrix[0][c] = 0;
                }
            }
        }

        // Step 2: Iterate inner cells and zero out based on markers
        for (int r = 1; r < m; r++) {
            for (int c = 1; c < n; c++) {
                if (matrix[r][0] == 0 || matrix[0][c] == 0) {
                    matrix[r][c] = 0;
                }
            }
        }

        // Step 3: Zero out the first row if matrix[0][0] is 0
        if (matrix[0][0] == 0) {
            for (int c = 0; c < n; c++) {
                matrix[0][c] = 0;
            }
        }

        // Step 4: Zero out the first column if firstColZero is true
        if (firstColZero) {
            for (int r = 0; r < m; r++) {
                matrix[r][0] = 0;
            }
        }
    }

    // Local Test Runner
    public static void main(String[] args) {
        Solution solver = new Solution();

        int[][] m1 = {
            {1, 1, 1},
            {1, 0, 1},
            {1, 1, 1}
        };
        solver.setZeroes(m1);
        System.out.println("Test 1 Result: " + Arrays.deepToString(m1));
        assert Arrays.deepEquals(m1, new int[][]{{1,0,1},{0,0,0},{1,0,1}}) : "Test 1 failed";

        System.out.println("All Java tests passed for LeetCode #73: Set Matrix Zeroes!");
    }
}
