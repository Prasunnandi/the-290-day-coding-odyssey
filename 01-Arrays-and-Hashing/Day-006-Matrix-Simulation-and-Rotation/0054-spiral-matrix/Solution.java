/**
 * LeetCode #54: Spiral Matrix
 * Difficulty: Medium
 * Topic: Arrays & Hashing
 * Pattern: 4-Boundary Shrinking Matrix Simulation (Top, Bottom, Left, Right)
 * Link: https://leetcode.com/problems/spiral-matrix/
 */

import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

public class Solution {

    // ==========================================
    // Approach: 4 Boundary Pointers Simulation
    // Time Complexity: O(M * N)
    // Space Complexity: O(1) auxiliary (excluding return list)
    // ==========================================
    public List<Integer> spiralOrder(int[][] matrix) {
        List<Integer> result = new ArrayList<>();
        if (matrix == null || matrix.length == 0) {
            return result;
        }

        int top = 0;
        int bottom = matrix.length - 1;
        int left = 0;
        int right = matrix[0].length - 1;

        while (top <= bottom && left <= right) {
            // 1. Move Right across the top row
            for (int c = left; c <= right; c++) {
                result.add(matrix[top][c]);
            }
            top++;

            // 2. Move Down along the right column
            for (int r = top; r <= bottom; r++) {
                result.add(matrix[r][right]);
            }
            right--;

            // 3. Move Left across the bottom row (boundary check required)
            if (top <= bottom) {
                for (int c = right; c >= left; c--) {
                    result.add(matrix[bottom][c]);
                }
                bottom--;
            }

            // 4. Move Up along the left column (boundary check required)
            if (left <= right) {
                for (int r = bottom; r >= top; r--) {
                    result.add(matrix[r][left]);
                }
                left++;
            }
        }

        return result;
    }

    // Local Test Runner
    public static void main(String[] args) {
        Solution solver = new Solution();

        int[][] m1 = {
            {1, 2, 3},
            {4, 5, 6},
            {7, 8, 9}
        };
        List<Integer> res1 = solver.spiralOrder(m1);
        System.out.println("Test 1 Result: " + res1); // Expected: [1, 2, 3, 6, 9, 8, 7, 4, 5]
        assert res1.equals(Arrays.asList(1, 2, 3, 6, 9, 8, 7, 4, 5)) : "Test 1 failed";

        System.out.println("All Java tests passed for LeetCode #54: Spiral Matrix!");
    }
}
