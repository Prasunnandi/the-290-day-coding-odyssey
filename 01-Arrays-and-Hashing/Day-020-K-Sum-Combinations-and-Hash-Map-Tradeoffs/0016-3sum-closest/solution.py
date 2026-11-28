"""
LeetCode 16: 3Sum Closest
Difficulty: Medium
Topic: Arrays & Two Pointers / Sorting

Pattern: Two-Pointer Convergent Gap Minimization
Given array nums and target, find 3 integers whose sum minimizes abs(sum - target).

Algorithm:
1. Sort nums in ascending order: O(N log N).
2. Initialize closest_sum = nums[0] + nums[1] + nums[2].
3. For each fixed index i from 0 to n - 3:
   - Skip adjacent duplicate values to avoid redundant checks.
   - Set left = i + 1 and right = n - 1.
   - While left < right:
       curr_sum = nums[i] + nums[left] + nums[right]
       
       # Update closest sum if closer to target
       if abs(curr_sum - target) < abs(closest_sum - target):
           closest_sum = curr_sum
           
       if curr_sum < target:
           left += 1    # Need a larger sum
       elif curr_sum > target:
           right -= 1   # Need a smaller sum
       else:
           return target  # Distance is 0 (optimal)

Time Complexity: O(N^2) — outer loop with linear two-pointer inner scan.
Space Complexity: O(1) auxiliary space (ignoring sorting memory).
"""

from typing import List


class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        """
        Finds the sum of three integers closest to target.
        
        Args:
            nums: List[int], array of integers
            target: int, target value
            
        Returns:
            int, closest sum
        """
        nums.sort()
        n = len(nums)
        closest_sum = nums[0] + nums[1] + nums[2]
        
        for i in range(n - 2):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
                
            left = i + 1
            right = n - 1
            
            while left < right:
                curr_sum = nums[i] + nums[left] + nums[right]
                
                if abs(curr_sum - target) < abs(closest_sum - target):
                    closest_sum = curr_sum
                    
                if curr_sum < target:
                    left += 1
                elif curr_sum > target:
                    right -= 1
                else:
                    return target
                    
        return closest_sum


if __name__ == "__main__":
    solver = Solution()
    
    # Test Case 1: Standard case
    print("Test 1 Result:", solver.threeSumClosest([-1, 2, 1, -4], 1))  # Expected: 2 (-1 + 2 + 1)
    
    # Test Case 2: Exact match with zeroes
    print("Test 2 Result:", solver.threeSumClosest([0, 0, 0], 1))  # Expected: 0
    
    # Test Case 3: Negative numbers
    print("Test 3 Result:", solver.threeSumClosest([-5, -4, -3, -2, -1], -10))  # Expected: -10 (-5 + -3 + -2)
