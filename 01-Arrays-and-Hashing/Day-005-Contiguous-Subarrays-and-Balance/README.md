# 📅 Day 005: Arrays & Hashing — Subarray Balancing & Pivot Sums

- **Phase:** Phase 1: Arrays & Hashing
- **Focus Pattern:** Subarray Balancing, First-Occurrence Hash Maps & Running Pivot Sums
- **Target Difficulty:** 1 Easy, 2 Medium Problems

---

## 🎯 Day 5 Overview & Algorithmic Patterns

1. **First-Occurrence Hash Maps for Length Constraints:** When checking for subarrays of length $\ge 2$ or finding the maximum possible length, **only the earliest occurrence** of each remainder/sum should be retained in the map. Overwriting would shrink subsequent window lengths!
2. **Value Transformation for Symmetry ($0 \rightarrow -1$):** Transforming binary inputs by mapping $0$ to $-1$ reduces the problem of finding equal frequencies of two items into finding a subarray with net sum $0$.
3. **Total Sum vs. Running Left Sum:** Eliminating prefix array memory by computing total sum in $O(N)$ and maintaining a rolling left sum, checking `left_sum == total_sum - left_sum - nums[i]` in $O(1)$ space.

---

## 📚 Problems Solved Today

| # | LeetCode ID | Problem Title | Difficulty | Pattern | Python Solution | Java Solution | Time | Space | Status |
| :---: | :---: | :--- | :---: | :--- | :---: | :---: | :---: | :---: | :---: |
| 1 | 0523 | [Continuous Subarray Sum](https://leetcode.com/problems/continuous-subarray-sum/) | Medium | Prefix Remainder Earliest Index | [Python](./0523-continuous-subarray-sum/solution.py) | [Java](./0523-continuous-subarray-sum/Solution.java) | $O(N)$ | $O(\min(N, K))$ | ✅ Solved |
| 2 | 0525 | [Contiguous Array](https://leetcode.com/problems/contiguous-array/) | Medium | 0 to -1 Balance Prefix Transform | [Python](./0525-contiguous-array/solution.py) | [Java](./0525-contiguous-array/Solution.java) | $O(N)$ | $O(N)$ | ✅ Solved |
| 3 | 0724 | [Find Pivot Index](https://leetcode.com/problems/find-pivot-index/) | Easy | Total Sum Balance | [Python](./0724-find-pivot-index/solution.py) | [Java](./0724-find-pivot-index/Solution.java) | $O(N)$ | $O(1)$ | ✅ Solved |

---

## 💡 Key Takeaways & Cheat Sheet

```text
Pattern: Subarray sum divisible by K with length >= 2
-> map[remainder] = first_seen_index
-> Seed with map[0] = -1

Pattern: Equal count of 0s and 1s
-> Replace 0 with -1
-> Find longest subarray where prefix_sum_j == prefix_sum_i
-> Seed with map[0] = -1

Pattern: Find equilibrium / pivot index
-> right_sum = total_sum - left_sum - nums[i]
-> Check: left_sum == right_sum
```
