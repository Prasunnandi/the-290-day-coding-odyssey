/**
 * LeetCode 179: Largest Number
 * Difficulty: Medium
 * Topic: Strings & Custom Sorting
 *
 * Pattern: Concatenation Comparator
 * Compare strings (b + a).compareTo(a + b) for descending concatenation order.
 *
 * Time Complexity: O(N log N * K)
 * Space Complexity: O(N * K)
 */

import java.util.Arrays;

public class Solution {

    public String largestNumber(int[] nums) {
        if (nums == null || nums.length == 0) return "";

        String[] strNums = new String[nums.length];
        for (int i = 0; i < nums.length; i++) {
            strNums[i] = String.valueOf(nums[i]);
        }

        // Sort descending based on concatenation
        Arrays.sort(strNums, (a, b) -> (b + a).compareTo(a + b));

        // Edge case: if highest element is "0", result is "0"
        if ("0".equals(strNums[0])) {
            return "0";
        }

        StringBuilder sb = new StringBuilder();
        for (String s : strNums) {
            sb.append(s);
        }

        return sb.toString();
    }

    public static void main(String[] args) {
        Solution solver = new Solution();

        int[] test1 = {10, 2};
        System.out.println("Test 1: " + solver.largestNumber(test1)); // Expected: "210"

        int[] test2 = {3, 30, 34, 5, 9};
        System.out.println("Test 2: " + solver.largestNumber(test2)); // Expected: "9534330"

        int[] test3 = {0, 0};
        System.out.println("Test 3: " + solver.largestNumber(test3)); // Expected: "0"
    }
}
