/**
 * LeetCode 542: 01 Matrix
 * Difficulty: Medium
 * Topic: Matrix & Breadth-First Search (BFS)
 *
 * Pattern: Multi-Source BFS
 * Seed queue with all 0-cells at distance 0.
 * Expand outward in 4 cardinal directions.
 *
 * Time Complexity: O(M * N)
 * Space Complexity: O(M * N)
 */

import java.util.ArrayDeque;
import java.util.Arrays;
import java.util.Queue;

public class Solution {

    public int[][] updateMatrix(int[][] mat) {
        int m = mat.length;
        int n = mat[0].length;
        int[][] dist = new int[m][n];
        Queue<int[]> queue = new ArrayDeque<>();

        for (int r = 0; r < m; r++) {
            for (int c = 0; c < n; c++) {
                if (mat[r][c] == 0) {
                    dist[r][c] = 0;
                    queue.offer(new int[]{r, c});
                } else {
                    dist[r][c] = -1; // unvisited marker
                }
            }
        }

        int[][] directions = {{-1, 0}, {1, 0}, {0, -1}, {0, 1}};

        while (!queue.isEmpty()) {
            int[] cell = queue.poll();
            int r = cell[0];
            int c = cell[1];

            for (int[] dir : directions) {
                int nr = r + dir[0];
                int nc = c + dir[1];

                if (nr >= 0 && nr < m && nc >= 0 && nc < n && dist[nr][nc] == -1) {
                    dist[nr][nc] = dist[r][c] + 1;
                    queue.offer(new int[]{nr, nc});
                }
            }
        }

        return dist;
    }

    public static void main(String[] args) {
        Solution solver = new Solution();

        int[][] mat1 = {
            {0, 0, 0},
            {0, 1, 0},
            {0, 0, 0}
        };
        System.out.println("Test 1: " + Arrays.deepToString(solver.updateMatrix(mat1)));

        int[][] mat2 = {
            {0, 0, 0},
            {0, 1, 0},
            {1, 1, 1}
        };
        System.out.println("Test 2: " + Arrays.deepToString(solver.updateMatrix(mat2)));
    }
}
