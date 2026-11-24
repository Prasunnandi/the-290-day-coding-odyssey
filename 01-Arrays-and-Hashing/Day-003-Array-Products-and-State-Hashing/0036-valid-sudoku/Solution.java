/**
 * LeetCode #36: Valid Sudoku
 * Difficulty: Medium
 * Topic: Arrays & Hashing
 * Pattern: Matrix State Hashing (Row, Column, and Sub-box Set Membership)
 * Link: https://leetcode.com/problems/valid-sudoku/
 */

import java.util.HashSet;
import java.util.Set;

public class Solution {

    // ==========================================
    // Approach 1: Boolean Array Lookup
    // Time Complexity: O(1) - exactly 81 cells checked
    // Space Complexity: O(1) - fixed 9x9 boolean tables
    // ==========================================
    public boolean isValidSudoku(char[][] board) {
        boolean[][] rows = new boolean[9][9];
        boolean[][] cols = new boolean[9][9];
        boolean[][] boxes = new boolean[9][9];

        for (int r = 0; r < 9; r++) {
            for (int c = 0; c < 9; c++) {
                if (board[r][c] == '.') {
                    continue;
                }

                int num = board[r][c] - '1'; // 0-indexed for 1-9
                int boxIdx = (r / 3) * 3 + (c / 3);

                if (rows[r][num] || cols[c][num] || boxes[boxIdx][num]) {
                    return false;
                }

                rows[r][num] = true;
                cols[c][num] = true;
                boxes[boxIdx][num] = true;
            }
        }

        return true;
    }

    // ==========================================
    // Approach 2: Bitmask Encoding
    // Uses integer bits (1 << num) for instant verification
    // ==========================================
    public boolean isValidSudokuBitmask(char[][] board) {
        int[] rows = new int[9];
        int[] cols = new int[9];
        int[] boxes = new int[9];

        for (int r = 0; r < 9; r++) {
            for (int c = 0; c < 9; c++) {
                if (board[r][c] == '.') {
                    continue;
                }

                int digitBit = 1 << (board[r][c] - '0');
                int boxIdx = (r / 3) * 3 + (c / 3);

                if ((rows[r] & digitBit) != 0 || (cols[c] & digitBit) != 0 || (boxes[boxIdx] & digitBit) != 0) {
                    return false;
                }

                rows[r] |= digitBit;
                cols[c] |= digitBit;
                boxes[boxIdx] |= digitBit;
            }
        }

        return true;
    }

    // Local Test Runner
    public static void main(String[] args) {
        Solution solver = new Solution();

        char[][] board = {
            {'5','3','.','.','7','.','.','.','.'},
            {'6','.','.','1','9','5','.','.','.'},
            {'.','9','8','.','.','.','.','6','.'},
            {'8','.','.','.','6','.','.','.','3'},
            {'4','.','.','8','.','3','.','.','1'},
            {'7','.','.','.','2','.','.','.','6'},
            {'.','6','.','.','.','.','2','8','.'},
            {'.','.','.','4','1','9','.','.','5'},
            {'.','.','.','.','8','.','.','7','9'}
        };

        boolean result = solver.isValidSudoku(board);
        System.out.println("Test 1 Result: " + result); // Expected: true
        assert result : "Test 1 failed";

        System.out.println("All Java tests passed for LeetCode #36: Valid Sudoku!");
    }
}
