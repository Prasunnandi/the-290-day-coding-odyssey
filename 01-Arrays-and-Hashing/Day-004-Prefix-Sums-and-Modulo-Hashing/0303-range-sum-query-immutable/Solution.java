/**
 * LeetCode #303: Range Sum Query - Immutable
 * Difficulty: Easy
 * Topic: Arrays & Hashing
 * Pattern: 1D Prefix Sum Array
 * Link: https://leetcode.com/problems/range-sum-query-immutable/
 */

public class NumArray {

    private final int[] prefix;

    // ==========================================
    // Constructor: Build prefix sums in O(N)
    // prefix[k] stores sum of elements up to index k-1
    // ==========================================
    public NumArray(int[] nums) {
        prefix = new int[nums.length + 1];
        for (int i = 0; i < nums.length; i++) {
            prefix[i + 1] = prefix[i] + nums[i];
        }
    }

    // ==========================================
    // Query: Constant O(1) Time
    // ==========================================
    public int sumRange(int left, int right) {
        return prefix[right + 1] - prefix[left];
    }

    // Local Test Runner
    public static void main(String[] args) {
        int[] nums = {-2, 0, 3, -5, 2, -1};
        NumArray obj = new NumArray(nums);

        assert obj.sumRange(0, 2) == 1 : "Test 1 failed";
        System.out.println("Query (0, 2): " + obj.sumRange(0, 2)); // Expected: 1

        assert obj.sumRange(2, 5) == -1 : "Test 2 failed";
        System.out.println("Query (2, 5): " + obj.sumRange(2, 5)); // Expected: -1

        assert obj.sumRange(0, 5) == -3 : "Test 3 failed";
        System.out.println("Query (0, 5): " + obj.sumRange(0, 5)); // Expected: -3

        System.out.println("All Java tests passed for LeetCode #303: Range Sum Query - Immutable!");
    }
}
