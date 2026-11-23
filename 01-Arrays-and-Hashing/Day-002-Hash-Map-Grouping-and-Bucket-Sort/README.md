# 📅 Day 002: Arrays & Hashing — Grouping, Bucket Sort & Protocol Encoding

- **Phase:** Phase 1: Arrays & Hashing
- **Focus Pattern:** Hash Map Grouping (Signatures), Frequency Bucket Sort, Length-Prefixed Serialization
- **Target Difficulty:** 3 Medium Problems

---

## 🎯 Day 2 Overview & Algorithmic Patterns

On Day 2, we expand beyond basic hash maps into three advanced techniques:
1. **Canonical Signatures for Grouping:** Using sorted strings or fixed 26-char frequency tuples as hash map keys to group related items (Group Anagrams).
2. **Frequency Bucket Sort ($O(N)$ vs $O(N \log K)$):** Utilizing the constraint that an element's frequency cannot exceed array length $N$ to achieve linear-time selection without sorting or heaps (Top K Frequent Elements).
3. **Length-Prefixed Chunking Protocol:** Designing lossless string serialization robust against any character delimiters by prefixing each chunk with its length (`length#content`).

---

## 📚 Problems Solved Today

| # | LeetCode ID | Problem Title | Difficulty | Pattern | Python Solution | Java Solution | Time | Space | Status |
| :---: | :---: | :--- | :---: | :--- | :---: | :---: | :---: | :---: | :---: |
| 1 | 0049 | [Group Anagrams](https://leetcode.com/problems/group-anagrams/) | Medium | Hash Map Signature Grouping | [Python](./0049-group-anagrams/solution.py) | [Java](./0049-group-anagrams/Solution.java) | $O(N \cdot K)$ | $O(N \cdot K)$ | ✅ Solved |
| 2 | 0347 | [Top K Frequent Elements](https://leetcode.com/problems/top-k-frequent-elements/) | Medium | Bucket Sort / Min-Heap | [Python](./0347-top-k-frequent-elements/solution.py) | [Java](./0347-top-k-frequent-elements/Solution.java) | $O(N)$ | $O(N)$ | ✅ Solved |
| 3 | 0271 | [Encode and Decode Strings](https://leetcode.com/problems/encode-and-decode-strings/) | Medium | Length-Prefixed Chunking | [Python](./0271-encode-and-decode-strings/solution.py) | [Java](./0271-encode-and-decode-strings/Solution.java) | $O(N)$ | $O(1)$ | ✅ Solved |

---

## 💡 Key Takeaways & Cheat Sheet

```text
Pattern: Group items with equivalent properties
-> Build canonical key: sorted(s) or tuple of 26-char counts

Pattern: Find Top-K frequent in O(N)
-> Frequency array: buckets[frequency] = [elements with this frequency]
-> Iterate buckets backwards from max_freq (N) to 1

Pattern: Robust delimiter-proof serialization
-> Format: [length]#[content]
-> Jump pointer forward by length characters
```
