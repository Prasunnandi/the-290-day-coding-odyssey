/**
 * LeetCode 363: Max Sum of Rectangle No Larger Than K
 * Difficulty: Hard
 * Topic: Matrix & Binary Search / TreeSet
 *
 * Pattern: 2D-to-1D Dimension Reduction with TreeSet Ceiling Search
 * Fix pairs of smaller dimension, accumulate slices, and use TreeSet.ceiling(curr - k)
 * to find the minimal prefix sum that satisfies P[i] >= P[j] - k in O(log N).
 *
 * Time Complexity: O(min(M, N)^2 * max(M, N) * log(max(M, N)))
 * Space Complexity: O(max(M, N))
 */

import java.util.TreeSet;

public class Solution {

    public int maxSumSubmatrix(int[][] matrix, int k) {
        int m = matrix.length;
        int n = matrix[0].length;
        int maxSum = Integer.MIN_VALUE;

        if (m > n) {
            // More rows than cols: iterate over column pairs (c1, c2)
            for (int c1 = 0; c1 < n; c1++) {
                int[] rowSums = new int[m];
                for (int c2 = c1; c2 < n; c2++) {
                    for (int r = 0; r < m; r++) {
                        rowSums[r] += matrix[r][c2];
                    }
                    int currMax = maxSubArrayNoLargerThanK(rowSums, k);
                    maxSum = Math.max(maxSum, currMax);
                    if (maxSum == k) return k;
                }
            }
        } else {
            // More cols than rows: iterate over row pairs (r1, r2)
            for (int r1 = 0; r1 < m; r1++) {
                int[] colSums = new int[n];
                for (int r2 = r1; r2 < m; r2++) {
                    for (int c = 0; c < n; c++) {
                        colSums[c] += matrix[r2][c];
                    }
                    int currMax = maxSubArrayNoLargerThanK(colSums, k);
                    maxSum = Math.max(maxSum, currMax);
                    if (maxSum == k) return k;
                }
            }
        }

        return maxSum;
    }

    private int maxSubArrayNoLargerThanK(int[] arr, int k) {
        TreeSet<Integer> set = new TreeSet<>();
        set.add(0);
        int curr = 0;
        int best = Integer.MIN_VALUE;

        for (int val : arr) {
            curr += val;
            // Find smallest prefix >= curr - k
            Integer ceil = set.ceiling(curr - k);
            if (ceil != null) {
                best = Math.max(best, curr - ceil);
                if (best == k) return k;
            }
            set.add(curr);
        }

        return best;
    }

    public static void main(String[] args) {
        Solution solver = new Solution();

        int[][] mat1 = {
            {1, 0, 1},
            {0, -2, 3}
        };
        System.out.println("Test 1: " + solver.maxSumSubmatrix(mat1, 2)); // Expected: 2

        int[][] mat2 = {
            {2, 2, -1}
        };
        System.out.println("Test 2: " + solver.maxSumSubmatrix(mat2, 3)); // Expected: 3
    }
}
