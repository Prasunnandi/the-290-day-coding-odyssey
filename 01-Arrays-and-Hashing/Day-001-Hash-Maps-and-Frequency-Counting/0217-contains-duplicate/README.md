# 0217. Contains Duplicate

- **Difficulty:** Easy
- **Topic:** Arrays & Hashing
- **Pattern:** Hash Set (Membership Testing with Early Exit)
- **LeetCode Link:** [Contains Duplicate](https://leetcode.com/problems/contains-duplicate/)

---

## Problem Statement

Given an integer array `nums`, return `true` if any value appears at least twice in the array, and return `false` if every element is distinct.

### Examples

**Example 1:**
```text
Input: nums = [1,2,3,1]
Output: true
```

**Example 2:**
```text
Input: nums = [1,2,3,4]
Output: false
```

**Example 3:**
```text
Input: nums = [1,1,1,3,3,4,3,2,4,2]
Output: true
```

---

## 💡 Intuition

If an element has already been seen, we can immediately return `true` without scanning the rest of the array. A hash set provides $O(1)$ average time complexity for both membership checking and insertions.

---

## 🚀 Approach 1: Sorting

Sort the array in ascending order. If there are duplicates, they will end up adjacent to each other.

### Python 3
```python
class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
        nums.sort()
        for i in range(1, len(nums)):
            if nums[i] == nums[i - 1]:
                return True
        return False
```

### Java
```java
import java.util.Arrays;

class Solution {
    public boolean containsDuplicate(int[] nums) {
        Arrays.sort(nums);
        for (int i = 1; i < nums.length; i++) {
            if (nums[i] == nums[i - 1]) return true;
        }
        return false;
    }
}
```

### Complexity
- **Time Complexity:** $O(N \log N)$ due to sorting.
- **Space Complexity:** $O(1)$ or $O(\log N)$ depending on sorting algorithm implementation.

---

## 🌟 Approach 2: Hash Set with Early Exit (Optimal)

Maintain a set `seen`. As you iterate through each number:
- If `num` is already in `seen`, return `True`.
- Otherwise, add `num` to `seen`.

In Java, `Set.add()` returns `false` if the element is already present, making the check even cleaner.

### Python 3
```python
class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
        seen = set()
        for num in nums:
            if num in seen:
                return True
            seen.add(num)
        return False
```

### Java
```java
import java.util.HashSet;
import java.util.Set;

class Solution {
    public boolean containsDuplicate(int[] nums) {
        Set<Integer> seen = new HashSet<>();
        for (int num : nums) {
            if (!seen.add(num)) return true;
        }
        return false;
    }
}
```

### Complexity
- **Time Complexity:** $O(N)$ worst-case, with best-case $O(1)$ early exit.
- **Space Complexity:** $O(N)$ to store up to $N$ unique elements.
