/**
 * LeetCode 566: Reshape the Matrix
 * Difficulty: Easy
 * Topic: Arrays & Matrix
 *
 * Pattern: 1D Index Linear Mapping
 * Flatten an (m x n) matrix conceptually into indices [0, m * n - 1].
 * For each index i:
 *   - Source row: i / n, source col: i % n
 *   - Target row: i / c, target col: i % c
 *
 * Time Complexity: O(m * n)
 * Space Complexity: O(1) auxiliary space (excluding result matrix)
 */

import java.util.Arrays;

public class Solution {

    /**
     * Reshapes an m x n matrix into an r x c matrix if total cells match.
     *
     * @param mat original 2D matrix
     * @param r   target row count
     * @param c   target column count
     * @return reshaped r x c matrix or original mat if invalid
     */
    public int[][] matrixReshape(int[][] mat, int r, int c) {
        int m = mat.length;
        int n = mat[0].length;

        // Dimension mismatch check
        if (m * n != r * c) {
            return mat;
        }

        int[][] result = new int[r][c];
        int totalElements = m * n;

        for (int i = 0; i < totalElements; i++) {
            int origRow = i / n;
            int origCol = i % n;
            int newRow = i / c;
            int newCol = i % c;

            result[newRow][newCol] = mat[origRow][origCol];
        }

        return result;
    }

    public static void main(String[] args) {
        Solution solver = new Solution();

        // Test Case 1: 2x2 -> 1x4
        int[][] mat1 = {{1, 2}, {3, 4}};
        int[][] res1 = solver.matrixReshape(mat1, 1, 4);
        System.out.println("Test 1: " + Arrays.deepToString(res1)); // [[1, 2, 3, 4]]

        // Test Case 2: Illegal 2x2 -> 2x4
        int[][] mat2 = {{1, 2}, {3, 4}};
        int[][] res2 = solver.matrixReshape(mat2, 2, 4);
        System.out.println("Test 2: " + Arrays.deepToString(res2)); // [[1, 2], [3, 4]]
    }
}
