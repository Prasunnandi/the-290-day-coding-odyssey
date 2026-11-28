"""
LeetCode 8: String to Integer (atoi)
Difficulty: Medium
Topic: Strings & State Machine / Parsing

Pattern: Deterministic String Parsing & 32-Bit Overflow Clamping
Steps:
1. Discard all leading whitespace.
2. Check for optional '+' or '-' sign indicator.
3. Read contiguous ASCII digits '0'-'9'.
4. Overflow Handling:
   - 32-bit signed integer range: [-2^31, 2^31 - 1] = [-2147483648, 2147483647]
   - Check threshold before multiplying:
     if res > INT_MAX // 10 or (res == INT_MAX // 10 and digit > 7):
         return INT_MAX if sign == 1 else INT_MIN

Time Complexity: O(N) — single pass.
Space Complexity: O(1) — constant auxiliary variables.
"""

class Solution:
    def myAtoi(self, s: str) -> int:
        """
        Converts a string to a 32-bit signed integer with clamping.
        
        Args:
            s: str, input string
            
        Returns:
            int, parsed integer within [-2^31, 2^31 - 1]
        """
        INT_MAX = 2147483647
        INT_MIN = -2147483648
        
        n = len(s)
        i = 0
        
        # 1. Skip leading whitespace
        while i < n and s[i] == " ":
            i += 1
            
        if i == n:
            return 0
            
        # 2. Check sign
        sign = 1
        if s[i] == "-":
            sign = -1
            i += 1
        elif s[i] == "+":
            i += 1
            
        # 3. Read digits and clamp on overflow
        res = 0
        max_div_10 = INT_MAX // 10
        
        while i < n and s[i].isdigit():
            digit = ord(s[i]) - ord("0")
            
            # Check for 32-bit signed integer overflow
            if res > max_div_10 or (res == max_div_10 and digit > 7):
                return INT_MAX if sign == 1 else INT_MIN
                
            res = res * 10 + digit
            i += 1
            
        return sign * res


if __name__ == "__main__":
    solver = Solution()
    
    # Test Case 1: Simple positive
    print("Test 1 Result:", solver.myAtoi("42"))  # Expected: 42
    
    # Test Case 2: Leading whitespace and negative sign
    print("Test 2 Result:", solver.myAtoi("   -042"))  # Expected: -42
    
    # Test Case 3: Trailing words
    print("Test 3 Result:", solver.myAtoi("1337c0d3"))  # Expected: 1337
    
    # Test Case 4: Words before number
    print("Test 4 Result:", solver.myAtoi("words and 987"))  # Expected: 0
    
    # Test Case 5: Negative overflow clamping
    print("Test 5 Result:", solver.myAtoi("-91283472332"))  # Expected: -2147483648
