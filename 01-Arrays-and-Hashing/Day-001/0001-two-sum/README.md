# 0001. Two Sum

- **Difficulty:** Easy
- **Topic:** Arrays & Hashing
- **Pattern:** Hash Map (Complement Lookup)
- **LeetCode Link:** [Two Sum](https://leetcode.com/problems/two-sum/)
- **Submission Status:** Accepted (0 ms · Beats 100.00% · 20.5 MB)

---

## Problem Statement

Given an array of integers `nums` and an integer `target`, return indices of the two numbers such that they add up to `target`.

You may assume that each input would have **exactly one solution**, and you may not use the same element twice. You can return the answer in any order.

### Examples

**Example 1:**
```text
Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].
```

**Example 2:**
```text
Input: nums = [3,2,4], target = 6
Output: [1,2]
```

**Example 3:**
```text
Input: nums = [3,3], target = 6
Output: [0,1]
```

---

## 💡 Intuition

For any given number $x$, we are essentially looking for its complement:
$$\text{complement} = \text{target} - x$$

Instead of repeatedly scanning the array to find this complement in $O(N)$, we can use a hash map to trade extra memory for instant $O(1)$ amortized lookups.

---

## 🚀 Approach 1: Brute Force

Check every pair $(i, j)$ where $i < j$. If `nums[i] + nums[j] == target`, return `[i, j]`.

### Python 3
```python
class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        n = len(nums)
        for i in range(n):
            for j in range(i + 1, n):
                if nums[i] + nums[j] == target:
                    return [i, j]
        return []
```

### Java
```java
class Solution {
    public int[] twoSum(int[] nums, int target) {
        int n = nums.length;
        for (int i = 0; i < n; i++) {
            for (int j = i + 1; j < n; j++) {
                if (nums[i] + nums[j] == target) {
                    return new int[]{i, j};
                }
            }
        }
        return new int[]{};
    }
}
```

### Complexity
- **Time Complexity:** $O(N^2)$ due to nested iterations.
- **Space Complexity:** $O(1)$ extra space.

---

## ⚡ Approach 2: Two-Pass Hash Table

1. **Pass 1:** Insert all elements into a hash map mapping `value -> index`.
2. **Pass 2:** For each element, check if `target - nums[i]` exists in the map and is not the current element itself.

### Python 3
```python
class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        val_to_index = {num: i for i, num in enumerate(nums)}
        for i, num in enumerate(nums):
            complement = target - num
            if complement in val_to_index and val_to_index[complement] != i:
                return [i, val_to_index[complement]]
        return []
```

### Java
```java
import java.util.HashMap;
import java.util.Map;

class Solution {
    public int[] twoSum(int[] nums, int target) {
        Map<Integer, Integer> map = new HashMap<>();
        for (int i = 0; i < nums.length; i++) {
            map.put(nums[i], i);
        }
        for (int i = 0; i < nums.length; i++) {
            int complement = target - nums[i];
            if (map.containsKey(complement) && map.get(complement) != i) {
                return new int[]{i, map.get(complement)};
            }
        }
        return new int[]{};
    }
}
```

### Complexity
- **Time Complexity:** $O(N)$ — two linear scans with $O(1)$ map lookups.
- **Space Complexity:** $O(N)$ — stores at most $N$ entries.

---

## 🌟 Approach 3: One-Pass Hash Table (Optimal — 0ms)

Combine building the hash map and searching for the complement into a single pass. As we traverse, check if `target - num` is already in `seen`. If yes, return immediately; if not, store `seen[num] = i`.

### Python 3
```python
class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        seen = {}
        for i, num in enumerate(nums):
            complement = target - num
            if complement in seen:
                return [seen[complement], i]
            seen[num] = i
        return []
```

### Java
```java
import java.util.HashMap;
import java.util.Map;

class Solution {
    public int[] twoSum(int[] nums, int target) {
        Map<Integer, Integer> seen = new HashMap<>();
        for (int i = 0; i < nums.length; i++) {
            int complement = target - nums[i];
            if (seen.containsKey(complement)) {
                return new int[]{seen.get(complement), i};
            }
            seen.put(nums[i], i);
        }
        return new int[]{};
    }
}
```

### Complexity
- **Time Complexity:** $O(N)$ — single pass over the array with $O(1)$ amortized lookups and insertions.
- **Space Complexity:** $O(N)$ — stores at most $N - 1$ entries.

---

## 📊 Summary Comparison

| Approach | Time Complexity | Space Complexity | Practical Speed | Notes |
| :--- | :--- | :--- | :--- | :--- |
| **1. Brute Force** | $O(N^2)$ | $O(1)$ | Slow ($>50$ ms) | Simple, but inefficient |
| **2. Two-Pass Hash Map** | $O(N)$ | $O(N)$ | Fast (~3 ms) | Extra pass over the array |
| **3. One-Pass Hash Map** | $O(N)$ | $O(N)$ | **0 ms (Beats 100%)** | Optimal single traversal |
