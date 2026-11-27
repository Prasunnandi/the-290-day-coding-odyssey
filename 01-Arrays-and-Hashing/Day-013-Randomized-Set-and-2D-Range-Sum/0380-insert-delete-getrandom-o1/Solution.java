/**
 * LeetCode 380: Insert Delete GetRandom O(1)
 * Difficulty: Medium
 * Topic: Arrays & Hash Table
 *
 * Pattern: Dynamic Array + Hash Map (Swap-and-Pop)
 * Combines ArrayList (O(1) getRandom) and HashMap (O(1) search and index tracking).
 *
 * Time Complexity: O(1) average for insert, remove, getRandom.
 * Space Complexity: O(N)
 */

import java.util.*;

class RandomizedSet {

    private final List<Integer> vals;
    private final Map<Integer, Integer> valToIdx;
    private final Random rand;

    public RandomizedSet() {
        vals = new ArrayList<>();
        valToIdx = new HashMap<>();
        rand = new Random();
    }

    public boolean insert(int val) {
        if (valToIdx.containsKey(val)) {
            return false;
        }
        valToIdx.put(val, vals.size());
        vals.add(val);
        return true;
    }

    public boolean remove(int val) {
        if (!valToIdx.containsKey(val)) {
            return false;
        }

        int idxToRemove = valToIdx.get(val);
        int lastVal = vals.get(vals.size() - 1);

        // Move last element to idxToRemove
        vals.set(idxToRemove, lastVal);
        valToIdx.put(lastVal, idxToRemove);

        // Remove last element
        vals.remove(vals.size() - 1);
        valToIdx.remove(val);

        return true;
    }

    public int getRandom() {
        int randomIndex = rand.nextInt(vals.size());
        return vals.get(randomIndex);
    }

    public static void main(String[] args) {
        RandomizedSet rSet = new RandomizedSet();
        System.out.println("Insert 1: " + rSet.insert(1)); // true
        System.out.println("Remove 2: " + rSet.remove(2)); // false
        System.out.println("Insert 2: " + rSet.insert(2)); // true
        System.out.println("GetRandom: " + rSet.getRandom()); // 1 or 2
        System.out.println("Remove 1: " + rSet.remove(1)); // true
        System.out.println("GetRandom: " + rSet.getRandom()); // 2
    }
}
