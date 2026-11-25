# 0525. Contiguous Array

- **Difficulty:** Medium
- **Topic:** Arrays & Hashing
- **Pattern:** Prefix Sum with Value Transformation (0 $\rightarrow$ -1 Balance Counter)
- **LeetCode Link:** [Contiguous Array](https://leetcode.com/problems/contiguous-array/)

---

## Problem Statement

Given a binary array `nums`, return the maximum length of a contiguous subarray with an equal number of `0` and `1`.

### Examples

**Example 1:**
```text
Input: nums = [0,1]
Output: 2
Explanation: [0, 1] is the longest contiguous subarray with an equal number of 0 and 1.
```

**Example 2:**
```text
Input: nums = [0,1,0]
Output: 2
Explanation: [0, 1] (or [1, 0]) is a longest contiguous subarray with equal number of 0 and 1.
```

---

## 💡 Intuition: Transforming 0s into -1s

Counting zeros and ones separately is clumsy. Instead, use a mathematical transformation:
$$\text{Treat } 0 \rightarrow -1, \quad \text{Treat } 1 \rightarrow +1$$

Now the condition *"equal number of 0s and 1s"* simplifies to:
$$\sum (\text{transformed elements in subarray}) = 0$$

### The Matching Prefix Invariant
If the cumulative prefix sum at index $j$ equals the cumulative prefix sum at index $i$:
$$\text{prefix}[j] = \text{prefix}[i] \implies \sum_{k=i+1}^j \text{nums}[k] = 0$$

The subarray `nums[i + 1 ... j]` contains an equal number of zeros and ones!
* **Length:** $j - i$.
* **To maximize $j - i$:** Store only the **earliest (first)** index where each prefix sum appears.
* **Base Case:** `prefix_map[0] = -1` accounts for balanced subarrays starting from index $0$.

### Visual Balance Trace

```text
nums:             [   0,    1,    1,    0,    1,    1,    1,    0  ]
transformed:      [  -1,   +1,   +1,   -1,   +1,   +1,   +1,   -1  ]
indices:              0     1     2     3     4     5     6     7

prefix_sum:          -1     0     1     0     1     2     3     2
earliest map:
  sum 0  -> idx -1
  sum -1 -> idx 0
  sum 1  -> idx 2

At index 3: prefix_sum is 0. Seen at -1 -> length = 3 - (-1) = 4! (subarray [0, 1, 1, 0])
```

---

## 🚀 Implementations

### Python 3
```python
class Solution:
    def findMaxLength(self, nums: list[int]) -> int:
        prefix_map = {0: -1}
        max_length = 0
        current_sum = 0

        for i, num in enumerate(nums):
            current_sum += 1 if num == 1 else -1

            if current_sum in prefix_map:
                max_length = max(max_length, i - prefix_map[current_sum])
            else:
                prefix_map[current_sum] = i

        return max_length
```

### Java
```java
import java.util.HashMap;
import java.util.Map;

class Solution {
    public int findMaxLength(int[] nums) {
        Map<Integer, Integer> prefixMap = new HashMap<>();
        prefixMap.put(0, -1);

        int maxLength = 0;
        int currentSum = 0;

        for (int i = 0; i < nums.length; i++) {
            currentSum += (nums[i] == 1) ? 1 : -1;

            if (prefixMap.containsKey(currentSum)) {
                maxLength = Math.max(maxLength, i - prefixMap.get(currentSum));
            } else {
                prefixMap.put(currentSum, i);
            }
        }

        return maxLength;
    }
}
```

---

## 📊 Complexity Analysis

- **Time Complexity:** $O(N)$ — Single linear pass over the binary array.
- **Space Complexity:** $O(N)$ — The prefix map stores at most $2N + 1$ distinct prefix values in the worst case.
