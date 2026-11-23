/**
 * LeetCode #347: Top K Frequent Elements
 * Difficulty: Medium
 * Topic: Arrays & Hashing
 * Pattern: Frequency Bucket Sort & Min-Heap
 * Link: https://leetcode.com/problems/top-k-frequent-elements/
 *
 * Problem Statement:
 * Given an integer array nums and an integer k, return the k most frequent elements.
 */

import java.util.*;

public class Solution {

    // ==========================================
    // Approach 1: Min-Heap / PriorityQueue
    // Time Complexity: O(N log K)
    // Space Complexity: O(N + K)
    // ==========================================
    public int[] topKFrequentHeap(int[] nums, int k) {
        Map<Integer, Integer> countMap = new HashMap<>();
        for (int num : nums) {
            countMap.put(num, countMap.getOrDefault(num, 0) + 1);
        }

        // Min-heap ordered by frequency ascending
        PriorityQueue<Integer> minHeap = new PriorityQueue<>(Comparator.comparingInt(countMap::get));

        for (int num : countMap.keySet()) {
            minHeap.offer(num);
            if (minHeap.size() > k) {
                minHeap.poll(); // Evict lowest frequency
            }
        }

        int[] result = new int[k];
        for (int i = 0; i < k; i++) {
            result[i] = minHeap.poll();
        }
        return result;
    }

    // ==========================================
    // Approach 2: Bucket Sort (Optimal Linear Time)
    // Time Complexity: O(N)
    // Space Complexity: O(N)
    // ==========================================
    @SuppressWarnings("unchecked")
    public int[] topKFrequent(int[] nums, int k) {
        Map<Integer, Integer> countMap = new HashMap<>();
        for (int num : nums) {
            countMap.put(num, countMap.getOrDefault(num, 0) + 1);
        }

        // Buckets where index represents frequency (0 to n)
        int n = nums.length;
        List<Integer>[] buckets = new List[n + 1];

        for (Map.Entry<Integer, Integer> entry : countMap.entrySet()) {
            int num = entry.getKey();
            int freq = entry.getValue();
            if (buckets[freq] == null) {
                buckets[freq] = new ArrayList<>();
            }
            buckets[freq].add(num);
        }

        int[] result = new int[k];
        int index = 0;

        // Traverse backwards from highest possible frequency
        for (int freq = n; freq >= 1 && index < k; freq--) {
            if (buckets[freq] != null) {
                for (int num : buckets[freq]) {
                    result[index++] = num;
                    if (index == k) {
                        return result;
                    }
                }
            }
        }

        return result;
    }

    // Local Test Runner
    public static void main(String[] args) {
        Solution solver = new Solution();

        int[] nums1 = {1, 1, 1, 2, 2, 3};
        int k1 = 2;
        int[] res1 = solver.topKFrequent(nums1, k1);
        System.out.println("Test 1 Result: " + Arrays.toString(res1)); // Expected: [1, 2]

        int[] nums2 = {1};
        int k2 = 1;
        int[] res2 = solver.topKFrequent(nums2, k2);
        System.out.println("Test 2 Result: " + Arrays.toString(res2)); // Expected: [1]

        System.out.println("All Java tests passed for LeetCode #347: Top K Frequent Elements!");
    }
}
