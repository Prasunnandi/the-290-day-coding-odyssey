# 0724. Find Pivot Index

- **Difficulty:** Easy
- **Topic:** Arrays & Hashing
- **Pattern:** Total Sum vs. Rolling Left Sum Balance
- **LeetCode Link:** [Find Pivot Index](https://leetcode.com/problems/find-pivot-index/) *(Also LeetCode #1991)*

---

## Problem Statement

Given an array of integers `nums`, calculate the **pivot index** of this array.

The **pivot index** is the index where the sum of all the numbers strictly to the left of the index is equal to the sum of all the numbers strictly to the index's right.

If the index is on the left edge of the array, the left sum is `0` because there are no elements to the left. This also applies to the right edge.

Return the **leftmost pivot index**. If no such index exists, return `-1`.

---

## 💡 Intuition & Algebraic Simplification

We don't need two prefix arrays!
1. Calculate `total_sum = sum(nums)` in a preliminary pass.
2. Maintain a running `left_sum` (initially 0).
3. At any index $i$:
   $$\text{right\_sum} = \text{total\_sum} - \text{left\_sum} - \text{nums}[i]$$
4. The pivot condition simplifies to:
   $$\text{left\_sum} == \text{right\_sum}$$
5. If matched, immediately return the index $i$ (guarantees leftmost). Otherwise, add `nums[i]` to `left_sum`.

### Visual Balance Trace

```text
nums:          [  1,   7,   3,   6,   5,   6  ]
total_sum = 28

i = 0: left = 0,   right = 28 - 0 - 1 = 27  --> No
i = 1: left = 1,   right = 28 - 1 - 7 = 20  --> No
i = 2: left = 8,   right = 28 - 8 - 3 = 17  --> No
i = 3: left = 11,  right = 28 - 11 - 6 = 11 --> MATCH! Return index 3
```

---

## 🚀 Implementations

### Python 3
```python
class Solution:
    def pivotIndex(self, nums: list[int]) -> int:
        total_sum = sum(nums)
        left_sum = 0

        for i, num in enumerate(nums):
            if left_sum == total_sum - left_sum - num:
                return i
            left_sum += num

        return -1
```

### Java
```java
class Solution {
    public int pivotIndex(int[] nums) {
        int totalSum = 0;
        for (int num : nums) totalSum += num;

        int leftSum = 0;
        for (int i = 0; i < nums.length; i++) {
            if (leftSum == totalSum - leftSum - nums[i]) {
                return i;
            }
            leftSum += nums[i];
        }
        return -1;
    }
}
```

---

## 📊 Complexity Analysis

- **Time Complexity:** $O(N)$ — One pass to compute total sum, and a second pass to identify the pivot index.
- **Space Complexity:** $O(1)$ — Only scalar integers are used.
