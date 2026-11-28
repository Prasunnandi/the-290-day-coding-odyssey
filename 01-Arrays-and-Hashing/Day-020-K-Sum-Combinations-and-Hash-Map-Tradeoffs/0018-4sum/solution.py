"""
LeetCode 18: 4Sum
Difficulty: Medium
Topic: Arrays & Two Pointers / Sorting

Pattern: General K-Sum Reduction Framework
Rather than nesting 4 rigid loops, we implement the generalized K-Sum pattern:
1. Sort nums to enable two-pointer convergence and duplicate pruning.
2. Recursive kSum(start, target, k):
   - Base Case (k == 2):
     Run standard Two-Pointer search on sorted nums[start:]:
       - If nums[left] + nums[right] == target: record pair, advance both, skip duplicates.
       - If sum < target: left += 1
       - If sum > target: right -= 1
   - Recursive Case (k > 2):
     For each index i from start to len(nums) - k:
       - Skip duplicate values (if i > start and nums[i] == nums[i - 1]).
       - Pruning optimization:
           if nums[i] * k > target: break (all subsequent k-sums exceed target)
           if nums[-1] * k < target: continue (even the largest k elements cannot reach target)
       - Recurse on kSum(i + 1, target - nums[i], k - 1).

Time Complexity: O(N^(k - 1)) = O(N^3) for 4Sum.
Space Complexity: O(N) auxiliary space for recursion stack and sorting.
"""

from typing import List


class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        """
        Finds all unique quadruplets summing to target.
        
        Args:
            nums: List[int], array of integers
            target: int, target sum
            
        Returns:
            List[List[int]], unique quadruplets
        """
        nums.sort()
        n = len(nums)
        
        def kSum(start: int, target: int, k: int) -> List[List[int]]:
            res = []
            
            # Boundary check
            if start >= n:
                return res
                
            # Early pruning: minimum possible sum > target or maximum possible sum < target
            avg = target // k
            if nums[start] > avg or nums[-1] < avg:
                return res
                
            # Base Case: Two Pointers
            if k == 2:
                left = start
                right = n - 1
                while left < right:
                    curr_sum = nums[left] + nums[right]
                    if curr_sum == target:
                        res.append([nums[left], nums[right]])
                        left += 1
                        right -= 1
                        while left < right and nums[left] == nums[left - 1]:
                            left += 1
                        while left < right and nums[right] == nums[right + 1]:
                            right -= 1
                    elif curr_sum < target:
                        left += 1
                    else:
                        right -= 1
                return res
                
            # Recursive Case: Reduce k to k - 1
            for i in range(start, n - k + 1):
                if i > start and nums[i] == nums[i - 1]:
                    continue
                for sub in kSum(i + 1, target - nums[i], k - 1):
                    res.append([nums[i]] + sub)
                    
            return res
            
        return kSum(0, target, 4)


if __name__ == "__main__":
    solver = Solution()
    
    # Test Case 1: Standard case
    test1 = [1, 0, -1, 0, -2, 2]
    print("Test 1 Result:", solver.fourSum(test1, 0))
    # Expected: [[-2, -1, 1, 2], [-2, 0, 0, 2], [-1, 0, 0, 1]]
    
    # Test Case 2: Identical elements
    test2 = [2, 2, 2, 2, 2]
    print("Test 2 Result:", solver.fourSum(test2, 8))
    # Expected: [[2, 2, 2, 2]]
    
    # Test Case 3: Negative target
    test3 = [-3, -1, 0, 2, 4, 5]
    print("Test 3 Result:", solver.fourSum(test3, 0))
    # Expected: [[-3, -1, 0, 4]]
