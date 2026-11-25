# 0523. Continuous Subarray Sum

- **Difficulty:** Medium
- **Topic:** Arrays & Hashing
- **Pattern:** Prefix Sum Modulo Hash Map (First Occurrence Index Tracking)
- **LeetCode Link:** [Continuous Subarray Sum](https://leetcode.com/problems/continuous-subarray-sum/)

---

## Problem Statement

Given an integer array `nums` and an integer `k`, return `true` if `nums` has a **good subarray** or `false` otherwise.

A **good subarray** is defined as:
* its length is **at least two**, and
* the sum of the elements of the subarray is a multiple of `k` (i.e. $\text{sum} = n \times k$ where $n \in \mathbb{Z}$).

---

## 💡 Intuition & Modulo Congruence

From modular arithmetic:
$$(\text{prefix}[j] - \text{prefix}[i]) \pmod k = 0 \iff \text{prefix}[j] \pmod k = \text{prefix}[i] \pmod k$$

If the cumulative remainder at index $j$ equals the cumulative remainder at an earlier index $i$, then the sum of elements from index $i + 1$ to $j$ is divisible by $k$.

### The Length $\ge 2$ Constraint
The problem specifies the subarray must contain at least 2 elements:
$$\text{length} = j - i \ge 2$$

To maximize the chance of satisfying this length condition, **we store only the earliest (first) index where each remainder was observed**. We never overwrite existing entries in our map!

### Base Case Setup: `remainder_map[0] = -1`
If a valid subarray starts from index `0` up to index `j`, its sum is directly divisible by `k` (`remainder == 0`).
For its length to be $j - (-1) = j + 1 \ge 2$, we seed the map with `remainder_map[0] = -1`.

```text
nums:          [  23,    2,    4,    6,    7  ],  k = 6
indices:           0     1     2     3     4
current_sum:      23    25    29    35    42
remainder % 6:     5     1     5     5     0

At index 2: remainder 5 was previously seen at index 0.
Length = 2 - 0 = 2 >= 2  -->  Valid subarray found: [2, 4]! (sum = 6)
```

---

## 🚀 Implementations

### Python 3
```python
class Solution:
    def checkSubarraySum(self, nums: list[int], k: int) -> bool:
        remainder_map = {0: -1}
        current_sum = 0

        for i, num in enumerate(nums):
            current_sum += num
            remainder = current_sum % k

            if remainder in remainder_map:
                if i - remainder_map[remainder] >= 2:
                    return True
            else:
                remainder_map[remainder] = i

        return False
```

### Java
```java
import java.util.HashMap;
import java.util.Map;

class Solution {
    public boolean checkSubarraySum(int[] nums, int k) {
        Map<Integer, Integer> remainderMap = new HashMap<>();
        remainderMap.put(0, -1);
        int currentSum = 0;

        for (int i = 0; i < nums.length; i++) {
            currentSum += nums[i];
            int remainder = currentSum % k;

            if (remainderMap.containsKey(remainder)) {
                if (i - remainderMap.get(remainder) >= 2) {
                    return true;
                }
            } else {
                remainderMap.put(remainder, i);
            }
        }
        return false;
    }
}
```

---

## 📊 Complexity Analysis

- **Time Complexity:** $O(N)$ — Single pass over `nums` of length $N$ with $O(1)$ average hash map operations.
- **Space Complexity:** $O(\min(N, K))$ — The hash map stores at most $\min(N, K)$ distinct remainders.
