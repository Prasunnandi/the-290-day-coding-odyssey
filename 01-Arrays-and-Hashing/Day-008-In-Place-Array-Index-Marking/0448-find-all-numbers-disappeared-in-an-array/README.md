# 0448. Find All Numbers Disappeared in an Array

## Problem Description
Given an array `nums` of $n$ integers where `nums[i]` is in the range $[1, n]$, return an array of all the integers in the range $[1, n]$ that do not appear in `nums`.

**Follow up:** Could you do it without extra space and in $O(n)$ runtime? You may assume the returned list does not count as extra space.

[LeetCode Problem Link](https://leetcode.com/problems/find-all-numbers-disappeared-in-an-array/)

---

## 1. Algorithmic Pattern: Sign Inversion as Boolean Flag

Because all numbers satisfy $1 \le \text{nums}[i] \le n$, there is a 1-to-1 correspondence between values and array indices:
$$\text{value } x \longleftrightarrow \text{index } (x - 1)$$

Rather than using an auxiliary hash set or boolean array of size $n$, we encode the boolean flag **"visited"** into the sign bit of the element residing at index $(|x| - 1)$:
1. Read $|x| = |\text{nums}[i]|$.
2. Target index: $\text{target\_idx} = |x| - 1$.
3. If $\text{nums}[\text{target\_idx}] > 0$, negate it: $\text{nums}[\text{target\_idx}] = -\text{nums}[\text{target\_idx}]$.
4. In the second pass, if $\text{nums}[i] > 0$, index $i$ was never targeted by any value in the array. Therefore, the number $i + 1$ is missing.

---

## 2. Visual State Trace

```
Initial Array: [4,  3,  2,  7,  8,  2,  3,  1] (n = 8)

Value 4 -> target index 3 -> negate nums[3] (7 -> -7)
Value 3 -> target index 2 -> negate nums[2] (2 -> -2)
Value 2 -> target index 1 -> negate nums[1] (3 -> -3)
Value 7 -> target index 6 -> negate nums[6] (3 -> -3)
Value 8 -> target index 7 -> negate nums[7] (1 -> -1)
Value 2 -> target index 1 -> already negative (skip)
Value 3 -> target index 2 -> already negative (skip)
Value 1 -> target index 0 -> negate nums[0] (4 -> -4)

State after Pass 1:
Index:     0    1    2    3    4    5    6    7
Value:   [-4,  -3,  -2,  -7,   8,   2,  -3,  -1]
                               ^    ^
Indices 4 and 5 remain POSITIVE!
Missing Numbers: 4 + 1 = 5, 5 + 1 = 6.
```

---

## 3. Complexity Analysis

| Metric | Complexity | Notes |
| :--- | :--- | :--- |
| **Time Complexity** | $O(N)$ | Two sequential linear scans over the array of size $N$. |
| **Space Complexity** | $O(1)$ | Operates purely in-place via sign flipping; output list does not count toward auxiliary space. |
