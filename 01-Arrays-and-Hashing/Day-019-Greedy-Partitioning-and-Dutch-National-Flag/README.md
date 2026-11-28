# Day 19: Greedy Partitioning & Dutch National Flag

## Overview
Day 19 covers in-place pointer partitioning and greedy string segmentations:
1. **Furthest Right Occurrence Tracking (Partition Labels):** Greedily expanding partition boundaries until the current index meets the furthest occurrence of all enclosed characters.
2. **Two-Pointer Write Head Compaction (Move Zeroes):** Preserving relative non-zero ordering while in-place shifting zeroes to the tail.
3. **Dijkstra's 3-Way Partitioning (Sort Colors):** Maintaining the Dutch National Flag 4-zone state invariant in single-pass $O(1)$ memory.

---

## Problems Solved

| Problem | Difficulty | Key Pattern | Time Complexity | Space Complexity | Code Links |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **0763. Partition Labels** | Medium | Furthest Right Occurrence Tracking | $O(N)$ | $O(1)$ aux | [Python](0763-partition-labels/solution.py) / [Java](0763-partition-labels/Solution.java) |
| **0283. Move Zeroes** | Easy | Two-Pointer Write Head Compaction | $O(N)$ | $O(1)$ aux | [Python](0283-move-zeroes/solution.py) / [Java](0283-move-zeroes/Solution.java) |
| **0075. Sort Colors** | Medium | Dijkstra's Dutch National Flag (3-Way) | $O(N)$ | $O(1)$ aux | [Python](0075-sort-colors/solution.py) / [Java](0075-sort-colors/Solution.java) |

---

## Pointer Invariant Mechanics
```
Dutch National Flag:
[ 0s zone | 1s zone | Unexamined (?) | 2s zone ]
 0    low-1 low  mid-1 mid        high high+1 n-1

Two-Pointer Compaction:
[ Non-zeroes in relative order | Zeroes displaced ]
 0                       slow-1 slow          fast
```
