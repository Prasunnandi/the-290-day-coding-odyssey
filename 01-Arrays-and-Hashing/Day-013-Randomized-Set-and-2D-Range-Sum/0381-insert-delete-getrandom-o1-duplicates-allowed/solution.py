"""
LeetCode 381: Insert Delete GetRandom O(1) - Duplicates allowed
Difficulty: Hard
Topic: Arrays & Hash Table

Pattern: Dynamic Array + Hash Map of Index Sets
Supporting duplicates with uniform weighted probability requires:
1. Dynamic Array (vals):
   - Stores all inserted values, including duplicates.
   - Preserves probability weighting: element appearing k times has probability k / N.
2. Hash Map of Sets (val_to_indices):
   - Maps each val -> set of indices in vals where it appears.

Deletion Algorithm (Swap-and-Pop with Duplicate Sets):
1. Extract any index `idx_to_remove` from val_to_indices[val].
2. Identify the last index `last_idx = len(vals) - 1` and `last_val = vals[-1]`.
3. If idx_to_remove != last_idx:
   - Overwrite vals[idx_to_remove] = last_val.
   - Update val_to_indices[last_val]: remove last_idx, insert idx_to_remove.
4. Pop vals[-1] in O(1).

Time Complexity: O(1) average for all operations.
Space Complexity: O(N) to store values and index sets.
"""

import collections
import random


class RandomizedCollection:
    def __init__(self):
        """Initializes empty RandomizedCollection."""
        self.vals = []
        self.val_to_indices = collections.defaultdict(set)

    def insert(self, val: int) -> bool:
        """
        Inserts a value into the collection.
        Returns true if the collection did not already contain the specified element.
        """
        not_present = len(self.val_to_indices[val]) == 0
        self.val_to_indices[val].add(len(self.vals))
        self.vals.append(val)
        return not_present

    def remove(self, val: int) -> bool:
        """
        Removes a value from the collection if present.
        Returns true if the collection contained the specified element.
        """
        if not self.val_to_indices[val]:
            return False
            
        # Get an arbitrary index of val
        idx_to_remove = self.val_to_indices[val].pop()
        last_idx = len(self.vals) - 1
        last_val = self.vals[-1]
        
        # If removing element is not the last element, swap
        if idx_to_remove != last_idx:
            self.vals[idx_to_remove] = last_val
            # Update index set of last_val
            self.val_to_indices[last_val].remove(last_idx)
            self.val_to_indices[last_val].add(idx_to_remove)
            
        self.vals.pop()
        return True

    def getRandom(self) -> int:
        """
        Get a random element from the collection.
        Probability is proportional to frequency of occurrence.
        """
        return random.choice(self.vals)


if __name__ == "__main__":
    rCol = RandomizedCollection()
    print("Insert 1:", rCol.insert(1))  # True
    print("Insert 1 again:", rCol.insert(1))  # False
    print("Insert 2:", rCol.insert(2))  # True
    print("GetRandom:", rCol.getRandom())  # 1 (2/3 chance) or 2 (1/3 chance)
    print("Remove 1:", rCol.remove(1))  # True
    print("GetRandom:", rCol.getRandom())  # 1 (1/2 chance) or 2 (1/2 chance)
