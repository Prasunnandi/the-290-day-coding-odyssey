"""
LeetCode 229: Majority Element II
Difficulty: Medium
Topic: Arrays & Hashing

Pattern: Extended Boyer-Moore Voting Algorithm (n / 3 threshold)
By Pigeonhole Principle:
  At most 2 distinct elements can appear strictly more than floor(n / 3) times.

Algorithm:
1. Pass 1 (Candidate Elimination):
   Maintain two candidate slots (cand1, cand2) and two vote counters (count1, count2).
   - If num matches cand1 -> increment count1
   - Else if num matches cand2 -> increment count2
   - Else if count1 == 0 -> cand1 = num, count1 = 1
   - Else if count2 == 0 -> cand2 = num, count2 = 1
   - Else (3 distinct elements encountered) -> decrement both count1 and count2
2. Pass 2 (Verification):
   Count exact frequencies of cand1 and cand2 in nums.
   Append to result if frequency > floor(n / 3).

Time Complexity: O(N) — two sequential passes.
Space Complexity: O(1) auxiliary space — constant scalar variables.
"""

from typing import List


class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        """
        Finds all elements appearing strictly more than floor(n / 3) times.
        
        Args:
            nums: List[int], input array
            
        Returns:
            List[int], list of up to 2 majority elements
        """
        if not nums:
            return []
            
        cand1, cand2 = None, None
        count1, count2 = 0, 0
        
        # Step 1: Boyer-Moore Candidate Selection
        for num in nums:
            if num == cand1:
                count1 += 1
            elif num == cand2:
                count2 += 1
            elif count1 == 0:
                cand1, count1 = num, 1
            elif count2 == 0:
                cand2, count2 = num, 1
            else:
                count1 -= 1
                count2 -= 1
                
        # Step 2: Verification Pass
        threshold = len(nums) // 3
        result = []
        
        freq1 = sum(1 for x in nums if x == cand1)
        freq2 = sum(1 for x in nums if x == cand2)
        
        if freq1 > threshold:
            result.append(cand1)
        if cand2 != cand1 and freq2 > threshold:
            result.append(cand2)
            
        return result


if __name__ == "__main__":
    solver = Solution()
    
    # Test Case 1: Single element exceeding n / 3
    test1 = [3, 2, 3]
    print("Test 1 Result:", solver.majorityElement(test1))  # Expected: [3]
    
    # Test Case 2: Single element array
    test2 = [1]
    print("Test 2 Result:", solver.majorityElement(test2))  # Expected: [1]
    
    # Test Case 3: Two elements exceeding n / 3
    test3 = [1, 2]
    print("Test 3 Result:", solver.majorityElement(test3))  # Expected: [1, 2]
    
    # Test Case 4: No element exceeding threshold
    test4 = [1, 2, 3, 4]
    print("Test 4 Result:", solver.majorityElement(test4))  # Expected: []
