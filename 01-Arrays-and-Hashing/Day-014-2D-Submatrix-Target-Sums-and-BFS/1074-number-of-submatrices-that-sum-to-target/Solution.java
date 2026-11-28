/**
 * LeetCode 1074: Number of Submatrices That Sum to Target
 * Difficulty: Hard
 * Topic: Matrix & Prefix Sums (Hash Map)
 *
 * Pattern: 2D-to-1D Dimension Reduction
 * Fix pairs of column boundaries (c1, c2), compute slice sums for each row,
 * and apply LeetCode 560 (Subarray Sum Equals Target) in O(M) time.
 *
 * Time Complexity: O(N^2 * M)
 * Space Complexity: O(M)
 */

import java.util.HashMap;
import java.util.Map;

public class Solution {

    public int numSubmatrixSumTarget(int[][] matrix, int target) {
        int m = matrix.length;
        int n = matrix[0].length;

        // Step 1: Compute horizontal row prefix sums
        for (int r = 0; r < m; r++) {
            for (int c = 1; c < n; c++) {
                matrix[r][c] += matrix[r][c - 1];
            }
        }

        int count = 0;

        // Step 2: Iterate over all column pairs (c1, c2)
        for (int c1 = 0; c1 < n; c1++) {
            for (int c2 = c1; c2 < n; c2++) {
                Map<Integer, Integer> prefixMap = new HashMap<>();
                prefixMap.put(0, 1);
                int currSum = 0;

                for (int r = 0; r < m; r++) {
                    int rowSum = matrix[r][c2] - (c1 > 0 ? matrix[r][c1 - 1] : 0);
                    currSum += rowSum;

                    count += prefixMap.getOrDefault(currSum - target, 0);
                    prefixMap.put(currSum, prefixMap.getOrDefault(currSum, 0) + 1);
                }
            }
        }

        return count;
    }

    public static void main(String[] args) {
        Solution solver = new Solution();

        int[][] mat1 = {
            {0, 1, 0},
            {1, 1, 1},
            {0, 1, 0}
        };
        System.out.println("Test 1: " + solver.numSubmatrixSumTarget(mat1, 0)); // Expected: 4

        int[][] mat2 = {
            {1, -1},
            {-1, 1}
        };
        System.out.println("Test 2: " + solver.numSubmatrixSumTarget(mat2, 0)); // Expected: 5
    }
}
