/**
 * LeetCode 304: Range Sum Query 2D - Immutable
 * Difficulty: Medium
 * Topic: Arrays & 2D Prefix Sums
 *
 * Pattern: 2D Inclusion-Exclusion Principle
 * Precompute 2D prefix sums P of size (m + 1) x (n + 1).
 * Queries run in O(1) time.
 *
 * Time Complexity: O(M * N) build, O(1) query.
 * Space Complexity: O(M * N)
 */

class NumMatrix {

    private final int[][] P;

    public NumMatrix(int[][] matrix) {
        if (matrix == null || matrix.length == 0 || matrix[0].length == 0) {
            P = new int[0][0];
            return;
        }

        int m = matrix.length;
        int n = matrix[0].length;
        P = new int[m + 1][n + 1];

        for (int r = 0; r < m; r++) {
            for (int c = 0; c < n; c++) {
                P[r + 1][c + 1] = matrix[r][c] + P[r][c + 1] + P[r + 1][c] - P[r][c];
            }
        }
    }

    public int sumRegion(int row1, int col1, int row2, int col2) {
        return P[row2 + 1][col2 + 1]
                - P[row1][col2 + 1]
                - P[row2 + 1][col1]
                + P[row1][col1];
    }

    public static void main(String[] args) {
        int[][] mat = {
            {3, 0, 1, 4, 2},
            {5, 6, 3, 2, 1},
            {1, 2, 0, 1, 5},
            {4, 1, 0, 1, 7},
            {1, 0, 3, 0, 5}
        };

        NumMatrix nm = new NumMatrix(mat);
        System.out.println("Test 1: " + nm.sumRegion(2, 1, 4, 3)); // Expected: 8
        System.out.println("Test 2: " + nm.sumRegion(1, 1, 2, 2)); // Expected: 11
        System.out.println("Test 3: " + nm.sumRegion(1, 2, 2, 4)); // Expected: 12
    }
}
