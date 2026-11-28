"""
LeetCode 43: Multiply Strings
Difficulty: Medium
Topic: Strings & Math / Simulation

Pattern: Column-wise Elementary Grade-School Multiplication
Constraints:
- Cannot convert inputs directly to integers.
- Cannot use BigInteger libraries.

Mathematical Principle:
Multiplying two numbers of lengths M and N produces a product of at most M + N digits.
When multiplying digit num1[i] and digit num2[j]:
  - Their product contributes to positions (i + j) and (i + j + 1) in the result array:
    p1 = i + j      (carries tens place)
    p2 = i + j + 1  (stores units place)

Algorithm:
1. Initialize array res of size M + N with zeroes.
2. Iterate backwards through num1 (index i) and num2 (index j):
   - mul = digit1 * digit2
   - total = mul + res[p2]
   - res[p2] = total % 10
   - res[p1] += total // 10
3. Skip any leading zeroes and format output string.

Time Complexity: O(M * N) — nested loops over string lengths.
Space Complexity: O(M + N) — result digit array.
"""

class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        """
        Multiplies two arbitrary-precision integers represented as strings.
        
        Args:
            num1: str, non-negative integer string
            num2: str, non-negative integer string
            
        Returns:
            str, product string
        """
        if num1 == "0" or num2 == "0":
            return "0"
            
        m, n = len(num1), len(num2)
        res = [0] * (m + n)
        
        for i in range(m - 1, -1, -1):
            d1 = ord(num1[i]) - ord("0")
            for j in range(n - 1, -1, -1):
                d2 = ord(num2[j]) - ord("0")
                mul = d1 * d2
                
                p1, p2 = i + j, i + j + 1
                total = mul + res[p2]
                
                res[p2] = total % 10
                res[p1] += total // 10
                
        # Find index of first non-zero digit
        start = 0
        while start < len(res) and res[start] == 0:
            start += 1
            
        return "".join(map(str, res[start:])) if start < len(res) else "0"


if __name__ == "__main__":
    solver = Solution()
    
    # Test Case 1: Standard multiplication
    print("Test 1 Result:", solver.multiply("2", "3"))  # Expected: "6"
    
    # Test Case 2: Multi-digit multiplication
    print("Test 2 Result:", solver.multiply("123", "456"))  # Expected: "56088"
    
    # Test Case 3: Zero multiplication
    print("Test 3 Result:", solver.multiply("0", "9999"))  # Expected: "0"
    
    # Test Case 4: Large digits with cascading carries
    print("Test 4 Result:", solver.multiply("999", "999"))  # Expected: "998001"
