# 📅 Day 004: Arrays & Hashing — Prefix Sums, Complements & Modulo Congruence

- **Phase:** Phase 1: Arrays & Hashing
- **Focus Pattern:** 1D Range Queries, Subarray Sums Equals K & Remainder Modulo Congruence
- **Target Difficulty:** 1 Easy, 2 Medium Problems

---

## 🎯 Day 4 Overview & Core Invariants

1. **Range Query in $O(1)$ Time:** Precomputing cumulative sums into a 1-based prefix table allows answering arbitrary range queries `sum(L..R)` in $O(1)$ without re-scanning.
2. **Subarray Sum Equals K ($O(N)$ with Negative Numbers):** When elements can be negative, sliding windows fail. Instead, we use the prefix difference identity:
   $$\text{prefix}[j] - \text{prefix}[i-1] = k \iff \text{prefix}[i-1] = \text{prefix}[j] - k$$
   We count occurrences of `(current_sum - k)` using a frequency hash map.
3. **Modular Congruence Principle:** Two prefix sums sharing the identical remainder modulo $k$ guarantee that the elements between them sum to a multiple of $k$. Storing remainder frequencies in an `int[k]` array yields optimal $O(N)$ time and $O(K)$ space.

---

## 📚 Problems Solved Today

| # | LeetCode ID | Problem Title | Difficulty | Pattern | Python Solution | Java Solution | Time | Space | Status |
| :---: | :---: | :--- | :---: | :--- | :---: | :---: | :---: | :---: | :---: |
| 1 | 0303 | [Range Sum Query - Immutable](https://leetcode.com/problems/range-sum-query-immutable/) | Easy | 1D Prefix Array | [Python](./0303-range-sum-query-immutable/solution.py) | [Java](./0303-range-sum-query-immutable/Solution.java) | $O(1)$ query | $O(N)$ | ✅ Solved |
| 2 | 0560 | [Subarray Sum Equals K](https://leetcode.com/problems/subarray-sum-equals-k/) | Medium | Prefix Sum + Hash Map | [Python](./0560-subarray-sum-equals-k/solution.py) | [Java](./0560-subarray-sum-equals-k/Solution.java) | $O(N)$ | $O(N)$ | ✅ Solved |
| 3 | 0974 | [Subarray Sums Divisible by K](https://leetcode.com/problems/subarray-sums-divisible-by-k/) | Medium | Prefix Sum + Modulo Congruence | [Python](./0974-subarray-sums-divisible-by-k/solution.py) | [Java](./0974-subarray-sums-divisible-by-k/Solution.java) | $O(N)$ | $O(K)$ | ✅ Solved |

---

## 💡 Key Takeaways & Cheat Sheet

```text
Pattern: Range sum query on static array
-> prefix[right + 1] - prefix[left]

Pattern: Subarray sum equals K (with negatives)
-> complement = current_sum - k
-> count += prefix_map[complement]
-> Base case: prefix_map[0] = 1

Pattern: Subarray sum divisible by K
-> rem = ((current_sum % k) + k) % k
-> count += remainder_counts[rem]
-> Base case: remainder_counts[0] = 1
```
