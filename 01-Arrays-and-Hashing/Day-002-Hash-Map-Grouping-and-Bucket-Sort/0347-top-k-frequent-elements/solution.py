"""
LeetCode #347: Top K Frequent Elements
Difficulty: Medium
Topic: Arrays & Hashing
Pattern: Frequency Bucket Sort & Min-Heap
Link: https://leetcode.com/problems/top-k-frequent-elements/

Problem Statement:
Given an integer array nums and an integer k, return the k most frequent elements.
You may return the answer in any order.
"""

from collections import Counter
import heapq
from typing import List


class Solution:

    # ==========================================
    # Approach 1: Min-Heap / Priority Queue
    # Time Complexity: O(N log K)
    # Space Complexity: O(N + K)
    # ==========================================
    def topKFrequentHeap(self, nums: List[int], k: int) -> List[int]:
        count = Counter(nums)
        # Maintain a min-heap of size k: (frequency, num)
        min_heap = []
        for num, freq in count.items():
            heapq.heappush(min_heap, (freq, num))
            if len(min_heap) > k:
                heapq.heappop(min_heap)

        return [num for freq, num in min_heap]

    # ==========================================
    # Approach 2: Bucket Sort (Optimal Linear Time)
    # Time Complexity: O(N)
    # Space Complexity: O(N)
    # ==========================================
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = Counter(nums)
        n = len(nums)

        # buckets[f] contains all numbers that appear with frequency f
        # Max possible frequency of any element is n
        buckets = [[] for _ in range(n + 1)]

        for num, freq in count.items():
            buckets[freq].append(num)

        result = []
        # Traverse buckets from highest frequency (n) down to 1
        for freq in range(n, 0, -1):
            for num in buckets[freq]:
                result.append(num)
                if len(result) == k:
                    return result

        return result


# Local Test Verification
if __name__ == "__main__":
    solver = Solution()

    # Test 1
    nums1 = [1, 1, 1, 2, 2, 3]
    k1 = 2
    res1 = sorted(solver.topKFrequent(nums1, k1))
    assert res1 == [1, 2], f"Test 1 failed: {res1}"

    # Test 2
    nums2 = [1]
    k2 = 1
    assert solver.topKFrequent(nums2, k2) == [1], "Test 2 failed"

    print("All tests passed for LeetCode #347: Top K Frequent Elements!")
