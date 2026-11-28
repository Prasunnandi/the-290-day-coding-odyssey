/**
 * LeetCode 8: String to Integer (atoi)
 * Difficulty: Medium
 * Topic: Strings & State Machine / Parsing
 *
 * Pattern: Deterministic String Parsing & 32-Bit Clamping
 * Parse sign, read digits, and check for overflow against Integer.MAX_VALUE / 10.
 *
 * Time Complexity: O(N)
 * Space Complexity: O(1)
 */

public class Solution {

    public int myAtoi(String s) {
        if (s == null) return 0;

        int n = s.length();
        int i = 0;

        // 1. Skip leading whitespace
        while (i < n && s.charAt(i) == ' ') {
            i++;
        }

        if (i == n) return 0;

        // 2. Check sign
        int sign = 1;
        if (s.charAt(i) == '-') {
            sign = -1;
            i++;
        } else if (s.charAt(i) == '+') {
            i++;
        }

        // 3. Process digits with overflow protection
        int res = 0;
        int maxDiv10 = Integer.MAX_VALUE / 10;

        while (i < n && Character.isDigit(s.charAt(i))) {
            int digit = s.charAt(i) - '0';

            // Check overflow before computing res * 10 + digit
            if (res > maxDiv10 || (res == maxDiv10 && digit > 7)) {
                return (sign == 1) ? Integer.MAX_VALUE : Integer.MIN_VALUE;
            }

            res = res * 10 + digit;
            i++;
        }

        return sign * res;
    }

    public static void main(String[] args) {
        Solution solver = new Solution();

        System.out.println("Test 1: " + solver.myAtoi("42"));           // Expected: 42
        System.out.println("Test 2: " + solver.myAtoi("   -042"));       // Expected: -42
        System.out.println("Test 3: " + solver.myAtoi("1337c0d3"));      // Expected: 1337
        System.out.println("Test 4: " + solver.myAtoi("words and 987")); // Expected: 0
        System.out.println("Test 5: " + solver.myAtoi("-91283472332"));  // Expected: -2147483648
    }
}
