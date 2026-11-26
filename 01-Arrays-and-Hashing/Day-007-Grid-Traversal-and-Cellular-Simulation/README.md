# Day 7: Grid Traversal and Cellular Simulation

## Overview
Day 7 explores advanced 2D matrix manipulation patterns:
1. **Diagonal Traversal:** Grouping cells by diagonal invariant sum `(r + c)` and alternating traversal directions.
2. **Cellular Automaton (Game of Life):** In-place state transitions using bitwise encoding or dual-state representation without requiring $O(M \times N)$ auxiliary storage.
3. **Matrix Reshaping:** Bijective 1D-to-2D indexing arithmetic (`row = i // cols`, `col = i % cols`).

---

## Problems Solved

| Problem | Difficulty | Key Pattern | Time Complexity | Space Complexity | Code Links |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **0498. Diagonal Traverse** | Medium | Diagonal Invariant `(r + c)` | $O(M \cdot N)$ | $O(1)$ aux | [Python](0498-diagonal-traverse/solution.py) / [Java](0498-diagonal-traverse/Solution.java) |
| **0289. Game of Life** | Medium | Bit-encoding In-Place State Simulation | $O(M \cdot N)$ | $O(1)$ aux | [Python](0289-game-of-life/solution.py) / [Java](0289-game-of-life/Solution.java) |
| **0566. Reshape the Matrix** | Easy | 1D-to-2D Linear Index Mapping | $O(M \cdot N)$ | $O(1)$ aux | [Python](0566-reshape-the-matrix/solution.py) / [Java](0566-reshape-the-matrix/Solution.java) |

---

## Core Algorithmic Insights

### 1. Diagonal Invariant Property
In any 2D grid, all cells on the same anti-diagonal share the property:
$$\text{diagonal\_index} = r + c$$
- When traversing upwards-right, we increment column and decrement row.
- When traversing downwards-left, we increment row and decrement column.
- Reversing odd-indexed diagonal groups achieves alternating snake-like traversal.

### 2. State Encoding for In-Place Grid Mutations
When cell updates depend on initial neighboring states:
- State `0 -> 0`: `0`
- State `1 -> 1`: `1`
- State `1 -> 0` (Live dies): `-1` (or 2-bit representation `01`)
- State `0 -> 1` (Dead becomes live): `2` (or 2-bit representation `10`)

Using the 2-bit pattern:
- Bit 0: Initial state (`cell & 1`)
- Bit 1: Next state (`cell >> 1`)
At the end, a single pass `cell >>= 1` updates the entire board simultaneously in $O(1)$ extra space.
