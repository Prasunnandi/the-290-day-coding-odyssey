# Day 11: Subarray Constraint Optimization (Sliding Window)

## Overview
Day 11 establishes the sliding window paradigm over arrays with positive elements or bounded state budgets:
1. **Subarray Counting by Product Boundary (Subarray Product Less Than K):** Summing window lengths `(right - left + 1)` to count all valid ending subarrays.
2. **Dynamic Shrink Window (Minimum Size Subarray Sum):** Minimizing window length under monotonic accumulation.
3. **Budget Window (Max Consecutive Ones III):** Mapping a "flip at most $k$ zeroes" problem to a maximum window with at most $k$ zero elements.

---

## Problems Solved

| Problem | Difficulty | Key Pattern | Time Complexity | Space Complexity | Code Links |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **0713. Subarray Product Less Than K** | Medium | Monotonic Product Window & Combinatorics | $O(N)$ | $O(1)$ aux | [Python](0713-subarray-product-less-than-k/solution.py) / [Java](0713-subarray-product-less-than-k/Solution.java) |
| **0209. Minimum Size Subarray Sum** | Medium | Shrinking Variable Window | $O(N)$ | $O(1)$ aux | [Python](0209-minimum-size-subarray-sum/solution.py) / [Java](0209-minimum-size-subarray-sum/Solution.java) |
| **1004. Max Consecutive Ones III** | Medium | Resource Budget Sliding Window | $O(N)$ | $O(1)$ aux | [Python](1004-max-consecutive-ones-iii/solution.py) / [Java](1004-max-consecutive-ones-iii/Solution.java) |

---

## Core Template
```python
left = 0
for right in range(len(nums)):
    # 1. Expand right and update state
    add_to_state(nums[right])
    
    # 2. Contract left while invalid
    while condition_violated():
        remove_from_state(nums[left])
        left += 1
        
    # 3. Update answer (either count, min_len, or max_len)
    update_result(right - left + 1)
```
