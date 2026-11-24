# 0974. Subarray Sums Divisible by K

- **Difficulty:** Medium
- **Topic:** Arrays & Hashing
- **Pattern:** Prefix Sum + Modulo Arithmetic Congruence
- **LeetCode Link:** [Subarray Sums Divisible by K](https://leetcode.com/problems/subarray-sums-divisible-by-k/)

---

## Problem Statement

Given an integer array `nums` and an integer `k`, return the number of non-empty **subarrays** that have a sum divisible by `k`.

A **subarray** is a contiguous part of an array.

### Examples

**Example 1:**
```text
Input: nums = [4,5,0,-2,-3,1], k = 5
Output: 7
Explanation: There are 7 subarrays with a sum divisible by k = 5:
[4, 5, 0, -2, -3, 1], [5], [5, 0], [5, 0, -2, -3], [0], [0, -2, -3], [-2, -3]
```

---

## 💡 Intuition & Modular Congruence

Recall from modular arithmetic:
$$(\text{prefix}[j] - \text{prefix}[i]) \pmod k = 0 \iff \text{prefix}[j] \pmod k = \text{prefix}[i] \pmod k$$

Whenever two different prefix sums yield the **exact same remainder** when divided by $k$, the elements sandwiched between them **must sum to a multiple of $k$**!

### Example Trace ($k = 5$)
```text
nums:          [  4,   5,   0,  -2,  -3,   1 ]
current_sum:       4   9   9    7    4    5
remainder % 5:     4   4   4    2    4    0

Notice remainder '4' appears 4 times:
Each pair of matching remainders (4, 4) forms a valid subarray divisible by 5!
```

### ⚠️ Handling Negative Modulo
In Java, C, and C++, the `%` operator can return negative values (e.g. `-2 % 5 == -2`).
To normalize the remainder to the positive range $[0, k-1]$:
$$\text{rem} = ((\text{sum} \pmod k) + k) \pmod k$$
*(Python's `%` operator automatically normalizes to positive remainders).*

---

## 🚀 Implementations

### Python 3
```python
from collections import defaultdict

class Solution:
    def subarraysDivByK(self, nums: list[int], k: int) -> int:
        count = 0
        current_sum = 0
        remainder_counts = defaultdict(int)
        remainder_counts[0] = 1  # Base case for prefix sum directly divisible by k

        for num in nums:
            current_sum += num
            remainder = current_sum % k

            if remainder in remainder_counts:
                count += remainder_counts[remainder]

            remainder_counts[remainder] += 1

        return count
```

### Java (Using Fixed Array `int[k]` — Faster than HashMap)
```java
class Solution {
    public int subarraysDivByK(int[] nums, int k) {
        int count = 0;
        int currentSum = 0;
        int[] remainderCounts = new int[k];
        remainderCounts[0] = 1;

        for (int num : nums) {
            currentSum += num;
            // Normalizing negative remainder in Java
            int rem = ((currentSum % k) + k) % k;

            count += remainderCounts[rem];
            remainderCounts[rem]++;
        }

        return count;
    }
}
```

---

## 📊 Complexity Analysis

- **Time Complexity:** $O(N)$ — Single pass over `nums` of size $N$.
- **Space Complexity:** $O(K)$ — We only need an array of size $K$ to store frequencies of remainders $0 \dots k-1$.
