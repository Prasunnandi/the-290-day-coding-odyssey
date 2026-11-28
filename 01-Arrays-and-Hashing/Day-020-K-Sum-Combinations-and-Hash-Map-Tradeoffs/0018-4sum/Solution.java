/**
 * LeetCode 18: 4Sum
 * Difficulty: Medium
 * Topic: Arrays & Two Pointers / Sorting
 *
 * Pattern: General K-Sum Reduction Framework
 * Uses long to prevent integer overflow on large target values.
 *
 * Time Complexity: O(N^3)
 * Space Complexity: O(N)
 */

import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

public class Solution {

    public List<List<Integer>> fourSum(int[] nums, int target) {
        Arrays.sort(nums);
        return kSum(nums, 0, (long) target, 4);
    }

    private List<List<Integer>> kSum(int[] nums, int start, long target, int k) {
        List<List<Integer>> res = new ArrayList<>();
        int n = nums.length;

        if (start >= n) return res;

        long avg = target / k;
        if (nums[start] > avg || nums[n - 1] < avg) return res;

        if (k == 2) {
            int left = start;
            int right = n - 1;

            while (left < right) {
                long sum = (long) nums[left] + nums[right];
                if (sum == target) {
                    res.add(Arrays.asList(nums[left], nums[right]));
                    left++;
                    right--;
                    while (left < right && nums[left] == nums[left - 1]) left++;
                    while (left < right && nums[right] == nums[right + 1]) right--;
                } else if (sum < target) {
                    left++;
                } else {
                    right--;
                }
            }
            return res;
        }

        for (int i = start; i <= n - k; i++) {
            if (i > start && nums[i] == nums[i - 1]) continue;

            List<List<Integer>> subRes = kSum(nums, i + 1, target - nums[i], k - 1);
            for (List<Integer> sub : subRes) {
                List<Integer> quad = new ArrayList<>();
                quad.add(nums[i]);
                quad.addAll(sub);
                res.add(quad);
            }
        }

        return res;
    }

    public static void main(String[] args) {
        Solution solver = new Solution();

        int[] test1 = {1, 0, -1, 0, -2, 2};
        System.out.println("Test 1: " + solver.fourSum(test1, 0));

        int[] test2 = {2, 2, 2, 2, 2};
        System.out.println("Test 2: " + solver.fourSum(test2, 8));
    }
}
