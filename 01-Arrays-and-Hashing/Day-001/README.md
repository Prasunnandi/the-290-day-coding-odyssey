# 📅 Day 001: Arrays & Hashing — Hash Map & Hash Set Foundations

- **Phase:** Phase 1: Arrays & Hashing
- **Focus Pattern:** Frequency Counting, Complement Lookup & Hash Set Early Exit
- **Target Difficulty:** 3 Easy Foundations

---

## 🎯 Day 1 Overview & Key Concepts

On Day 1, we establish the core primitives of **Hash Tables** (`dict` / `HashMap`) and **Hash Sets** (`set` / `HashSet`):
1. **Complement Lookup:** Using `complement = target - current` to solve pair-matching problems in a single pass ($O(N)$ instead of $O(N^2)$).
2. **Frequency Array vs. Hash Map:** When alphabet or keys are bounded (e.g. 26 lowercase letters), an integer array `int[26]` is faster and uses $O(1)$ constant memory compared to dynamic hash maps.
3. **Early Exit with Sets:** Immediate detection of membership in $O(1)$ amortized time.

---

## 📚 Problems Solved Today

| # | LeetCode ID | Problem Title | Difficulty | Pattern | Python Solution | Java Solution | Time | Space | Status |
| :---: | :---: | :--- | :---: | :--- | :---: | :---: | :---: | :---: | :---: |
| 1 | 0001 | [Two Sum](https://leetcode.com/problems/two-sum/) | Easy | One-Pass Hash Map | [Python](./0001-two-sum/solution.py) | [Java](./0001-two-sum/Solution.java) | $O(N)$ | $O(N)$ | ✅ Accepted (0ms) |
| 2 | 0242 | [Valid Anagram](https://leetcode.com/problems/valid-anagram/) | Easy | 26-char Array Counter | [Python](./0242-valid-anagram/solution.py) | [Java](./0242-valid-anagram/Solution.java) | $O(N)$ | $O(1)$ | ✅ Solved |
| 3 | 0217 | [Contains Duplicate](https://leetcode.com/problems/contains-duplicate/) | Easy | Hash Set Early Exit | [Python](./0217-contains-duplicate/solution.py) | [Java](./0217-contains-duplicate/Solution.java) | $O(N)$ | $O(N)$ | ✅ Solved |

---

## 💡 Key Takeaways & Cheat Sheet

```text
Problem: "Find two elements that add to X"
-> Hash Map: seen[complement] -> index

Problem: "Are two strings re-orderings of each other?"
-> Array of size 26: counts[c - 'a']++ and counts[c - 'a']--

Problem: "Does any element repeat?"
-> Hash Set: seen.add(x) with early return on seen.contains(x)
```
