/**
 * LeetCode #289: Game of Life
 * Difficulty: Medium
 * Topic: Arrays & Hashing
 * Pattern: Cellular Automata In-Place State Encoding (2-Bit Transition Modeling)
 * Link: https://leetcode.com/problems/game-of-life/
 */

import java.util.Arrays;

public class Solution {

    // ==========================================
    // Approach: In-Place State Transition Encoding
    // 0 -> 0: 0
    // 1 -> 1: 1
    // 1 -> 0: -1
    // 0 -> 1: 2
    // Time Complexity: O(M * N)
    // Space Complexity: O(1) in-place
    // ==========================================
    public void gameOfLife(int[][] board) {
        int m = board.length;
        int n = board[0].length;
        int[][] directions = {
            {-1, -1}, {-1, 0}, {-1, 1},
            {0, -1},           {0, 1},
            {1, -1},  {1, 0},  {1, 1}
        };

        // Pass 1: Encode state transitions
        for (int r = 0; r < m; r++) {
            for (int c = 0; c < n; c++) {
                int liveNeighbors = 0;
                for (int[] d : directions) {
                    int nr = r + d[0];
                    int nc = c + d[1];
                    if (nr >= 0 && nr < m && nc >= 0 && nc < n) {
                        // Math.abs(board[nr][nc]) == 1 means originally alive (1 or -1)
                        if (Math.abs(board[nr][nc]) == 1) {
                            liveNeighbors++;
                        }
                    }
                }

                // Rule 1 & 3: Live cell dies
                if (board[r][c] == 1 && (liveNeighbors < 2 || liveNeighbors > 3)) {
                    board[r][c] = -1;
                }
                // Rule 4: Dead cell becomes alive
                else if (board[r][c] == 0 && liveNeighbors == 3) {
                    board[r][c] = 2;
                }
            }
        }

        // Pass 2: Finalize values to binary states
        for (int r = 0; r < m; r++) {
            for (int c = 0; c < n; c++) {
                board[r][c] = board[r][c] > 0 ? 1 : 0;
            }
        }
    }

    // Local Test Runner
    public static void main(String[] args) {
        Solution solver = new Solution();

        int[][] b1 = {
            {0, 1, 0},
            {0, 0, 1},
            {1, 1, 1},
            {0, 0, 0}
        };
        solver.gameOfLife(b1);
        int[][] expected1 = {
            {0, 0, 0},
            {1, 0, 1},
            {0, 1, 1},
            {0, 1, 0}
        };
        assert Arrays.deepEquals(b1, expected1) : "Test 1 failed";
        System.out.println("Test 1 Result: " + Arrays.deepToString(b1));

        System.out.println("All Java tests passed for LeetCode #289: Game of Life!");
    }
}
