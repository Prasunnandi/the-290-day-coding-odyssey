/**
 * LeetCode 381: Insert Delete GetRandom O(1) - Duplicates allowed
 * Difficulty: Hard
 * Topic: Arrays & Hash Table
 *
 * Pattern: Dynamic Array + Hash Map of LinkedHashSet
 * Handles duplicates with weighted probability proportional to frequency.
 *
 * Time Complexity: O(1) average for insert, remove, getRandom.
 * Space Complexity: O(N)
 */

import java.util.*;

class RandomizedCollection {

    private final List<Integer> vals;
    private final Map<Integer, Set<Integer>> valToIndices;
    private final Random rand;

    public RandomizedCollection() {
        vals = new ArrayList<>();
        valToIndices = new HashMap<>();
        rand = new Random();
    }

    public boolean insert(int val) {
        boolean notPresent = !valToIndices.containsKey(val) || valToIndices.get(val).isEmpty();
        valToIndices.computeIfAbsent(val, k -> new LinkedHashSet<>()).add(vals.size());
        vals.add(val);
        return notPresent;
    }

    public boolean remove(int val) {
        if (!valToIndices.containsKey(val) || valToIndices.get(val).isEmpty()) {
            return false;
        }

        Set<Integer> indices = valToIndices.get(val);
        int idxToRemove = indices.iterator().next();
        indices.remove(idxToRemove);

        int lastIdx = vals.size() - 1;
        int lastVal = vals.get(lastIdx);

        if (idxToRemove != lastIdx) {
            vals.set(idxToRemove, lastVal);
            Set<Integer> lastValIndices = valToIndices.get(lastVal);
            lastValIndices.remove(lastIdx);
            lastValIndices.add(idxToRemove);
        }

        vals.remove(lastIdx);
        return true;
    }

    public int getRandom() {
        int randomIndex = rand.nextInt(vals.size());
        return vals.get(randomIndex);
    }

    public static void main(String[] args) {
        RandomizedCollection rCol = new RandomizedCollection();
        System.out.println("Insert 1: " + rCol.insert(1)); // true
        System.out.println("Insert 1: " + rCol.insert(1)); // false
        System.out.println("Insert 2: " + rCol.insert(2)); // true
        System.out.println("GetRandom: " + rCol.getRandom());
        System.out.println("Remove 1: " + rCol.remove(1)); // true
        System.out.println("GetRandom: " + rCol.getRandom());
    }
}
