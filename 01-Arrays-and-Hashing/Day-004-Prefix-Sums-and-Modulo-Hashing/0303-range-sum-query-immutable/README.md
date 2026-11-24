# 0303. Range Sum Query - Immutable

- **Difficulty:** Easy
- **Topic:** Arrays & Hashing
- **Pattern:** 1D Prefix Sum Array
- **LeetCode Link:** [Range Sum Query - Immutable](https://leetcode.com/problems/range-sum-query-immutable/)

---

## Problem Statement

Given an integer array `nums`, handle multiple queries of the following type:
* Calculate the sum of the elements of `nums` between indices `left` and `right` inclusive where `left <= right`.

Implement the `NumArray` class:
* `NumArray(int[] nums)`: Initializes the object with the integer array `nums`.
* `int sumRange(int left, int right)`: Returns the sum of the elements of `nums` between indices `left` and `right` inclusive.

---

## 💡 Intuition: Why Prefix Sums?

If we sum up elements in a loop for every query, each query takes $O(N)$ time. For $Q$ queries, total time is $O(Q \cdot N)$, which leads to TLE.

By precomputing cumulative sums in $O(N)$ once, every range query can be answered in **$O(1)$ constant time**:

$$\text{sumRange}(\text{left}, \text{right}) = \sum_{k=\text{left}}^{\text{right}} \text{nums}[k] = \text{prefix}[\text{right} + 1] - \text{prefix}[\text{left}]$$

### 1-Based Prefix Array Alignment

```text
nums:              [ -2,    0,    3,   -5,    2,   -1 ]
indices:              0     1     2     3     4     5

prefix:       [  0,  -2,   -2,    1,   -4,   -2,   -3 ]
prefix idx:      0    1     2     3     4     5     6

Query(2, 5): prefix[5 + 1] - prefix[2] = prefix[6] - prefix[2]
            = (-3) - (-2) = -1
```

---

## 🚀 Implementations

### Python 3
```python
class NumArray:
    def __init__(self, nums: list[int]):
        self.prefix = [0] * (len(nums) + 1)
        for i, num in enumerate(nums):
            self.prefix[i + 1] = self.prefix[i] + num

    def sumRange(self, left: int, right: int) -> int:
        return self.prefix[right + 1] - self.prefix[left]
```

### Java
```java
public class NumArray {
    private final int[] prefix;

    public NumArray(int[] nums) {
        prefix = new int[nums.length + 1];
        for (int i = 0; i < nums.length; i++) {
            prefix[i + 1] = prefix[i] + nums[i];
        }
    }

    public int sumRange(int left, int right) {
        return prefix[right + 1] - prefix[left];
    }
}
```

---

## 📊 Complexity Analysis

- **Time Complexity:**
  * Constructor (`__init__`): $O(N)$ to compute cumulative sums.
  * Query (`sumRange`): $O(1)$ constant time lookup.
- **Space Complexity:** $O(N)$ to store the $(N+1)$-element prefix table.
