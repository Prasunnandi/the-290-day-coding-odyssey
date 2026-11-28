# Day 17: String Parsing & Big-Number Simulation

## Overview
Day 17 dives into precision string parsing and arithmetic simulation:
1. **Vertical Column Scanning (Longest Common Prefix):** Inspecting characters column by column to stop at the earliest possible character mismatch.
2. **Deterministic State Parsing (String to Integer - atoi):** Handling leading whitespace, optional signs, digit streams, and 32-bit overflow boundary clamping.
3. **Place-Value Positional Multiplication (Multiply Strings):** Simulating grade-school multiplication in $O(M \cdot N)$ time and $O(M + N)$ space without converting directly to big numbers.

---

## Problems Solved

| Problem | Difficulty | Key Pattern | Time Complexity | Space Complexity | Code Links |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **0014. Longest Common Prefix** | Easy | Vertical Column Scanning | $O(S)$ | $O(1)$ aux | [Python](0014-longest-common-prefix/solution.py) / [Java](0014-longest-common-prefix/Solution.java) |
| **0008. String to Integer (atoi)** | Medium | Deterministic State Parsing & Clamping | $O(N)$ | $O(1)$ aux | [Python](0008-string-to-integer-atoi/solution.py) / [Java](0008-string-to-integer-atoi/Solution.java) |
| **0043. Multiply Strings** | Medium | Positional Place-Value Simulation | $O(M \cdot N)$ | $O(M + N)$ aux | [Python](0043-multiply-strings/solution.py) / [Java](0043-multiply-strings/Solution.java) |

---

## Positional Place Mapping Formula
For multiplying strings of lengths $M$ and $N$:
$$\text{digit}_1[i] \times \text{digit}_2[j] \implies \begin{cases} \text{Carry position (tens):} & p_1 = i + j \\ \text{Base position (units):} & p_2 = i + j + 1 \end{cases}$$
Directly accumulating into $p_1$ and $p_2$ eliminates the need for intermediate multi-line string buffers.
