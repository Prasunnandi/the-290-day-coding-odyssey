"""
LeetCode 380: Insert Delete GetRandom O(1)
Difficulty: Medium
Topic: Arrays & Hash Table

Pattern: Dynamic Array + Hash Map (Swap-and-Pop)
Requirements:
  - insert(val): O(1) average
  - remove(val): O(1) average
  - getRandom(): O(1) average with uniform probability

Data Structures:
1. Dynamic Array (vals):
   - Enables O(1) uniform random access via random index selection.
2. Hash Map (val_to_idx):
   - Maps val -> index in vals for O(1) lookups and location tracking.

The Swap-and-Pop Deletion Technique:
Standard deletion in an array at arbitrary index i takes O(N) due to shifting.
By copying the LAST element of the array into index i and decrementing array length (pop),
we achieve O(1) deletion without shifting elements!

Time Complexity: O(1) average for all methods.
Space Complexity: O(N) to store up to N elements.
"""

import random


class RandomizedSet:
    def __init__(self):
        """Initializes empty RandomizedSet."""
        self.vals = []
        self.val_to_idx = {}

    def insert(self, val: int) -> bool:
        """
        Inserts a value to the set. Returns true if the set did not already contain the specified element.
        """
        if val in self.val_to_idx:
            return False
            
        self.val_to_idx[val] = len(self.vals)
        self.vals.append(val)
        return True

    def remove(self, val: int) -> bool:
        """
        Removes a value from the set. Returns true if the set contained the specified element.
        """
        if val not in self.val_to_idx:
            return False
            
        idx_to_remove = self.val_to_idx[val]
        last_val = self.vals[-1]
        
        # Overwrite the target index with the last element
        self.vals[idx_to_remove] = last_val
        self.val_to_idx[last_val] = idx_to_remove
        
        # Pop the last element in O(1)
        self.vals.pop()
        del self.val_to_idx[val]
        
        return True

    def getRandom(self) -> int:
        """
        Get a random element from the set with uniform probability.
        """
        return random.choice(self.vals)


if __name__ == "__main__":
    rSet = RandomizedSet()
    print("Insert 1:", rSet.insert(1))  # True
    print("Remove 2:", rSet.remove(2))  # False
    print("Insert 2:", rSet.insert(2))  # True
    print("GetRandom:", rSet.getRandom())  # 1 or 2
    print("Remove 1:", rSet.remove(1))  # True
    print("Insert 2 again:", rSet.insert(2))  # False
    print("GetRandom:", rSet.getRandom())  # 2
