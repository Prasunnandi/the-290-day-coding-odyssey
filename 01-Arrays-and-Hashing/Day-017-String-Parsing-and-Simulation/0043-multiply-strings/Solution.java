/**
 * LeetCode 43: Multiply Strings
 * Difficulty: Medium
 * Topic: Strings & Simulation
 *
 * Pattern: Column-wise Elementary Grade-School Multiplication
 * Multiplies digits at indices (i, j) and accumulates into indices (i + j, i + j + 1).
 *
 * Time Complexity: O(M * N)
 * Space Complexity: O(M + N)
 */

public class Solution {

    public String multiply(String num1, String num2) {
        if ("0".equals(num1) || "0".equals(num2)) return "0";

        int m = num1.length();
        int n = num2.length();
        int[] res = new int[m + n];

        for (int i = m - 1; i >= 0; i--) {
            int d1 = num1.charAt(i) - '0';
            for (int j = n - 1; j >= 0; j--) {
                int d2 = num2.charAt(j) - '0';
                int mul = d1 * d2;

                int p1 = i + j;
                int p2 = i + j + 1;
                int total = mul + res[p2];

                res[p2] = total % 10;
                res[p1] += total / 10;
            }
        }

        StringBuilder sb = new StringBuilder();
        int start = 0;
        while (start < res.length && res[start] == 0) {
            start++;
        }

        for (int i = start; i < res.length; i++) {
            sb.append(res[i]);
        }

        return (sb.length() == 0) ? "0" : sb.toString();
    }

    public static void main(String[] args) {
        Solution solver = new Solution();

        System.out.println("Test 1: " + solver.multiply("2", "3"));     // Expected: "6"
        System.out.println("Test 2: " + solver.multiply("123", "456")); // Expected: "56088"
        System.out.println("Test 3: " + solver.multiply("0", "9999"));  // Expected: "0"
    }
}
