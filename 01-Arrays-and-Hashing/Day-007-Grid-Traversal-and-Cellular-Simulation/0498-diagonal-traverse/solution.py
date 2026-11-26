"""
LeetCode #498: Diagonal Traverse
Difficulty: Medium
Topic: Arrays & Hashing
Pattern: Diagonal Index Invariance (r + c = d) & Zigzag Parity
Link: https://leetcode.com/problems/diagonal-traverse/

Problem Statement:
Given an m x n matrix mat, return an array of all the elements of the array in a diagonal order.
"""

from collections import defaultdict
from typing import List


class Solution:

    # ==========================================
    # Approach 1: Hash Map / Grouping by (r + c)
    # Cells on the same anti-diagonal share the identical sum: r + c = d
    # If d % 2 == 0: reverse order (traversing upwards)
    # If d % 2 == 1: keep natural order (traversing downwards)
    # Time Complexity: O(M * N)
    # Space Complexity: O(M * N)
    # ==========================================
    def findDiagonalOrderGrouping(self, mat: List[List[int]]) -> List[int]:
        if not mat or not mat[0]:
            return []

        m, n = len(mat), len(mat[0])
        diagonals = defaultdict(list)

        for r in range(m):
            for c in range(n):
                diagonals[r + c].append(mat[r][c])

        result = []
        for d in range(m + n - 1):
            if d % 2 == 0:
                result.extend(reversed(diagonals[d]))
            else:
                result.extend(diagonals[d])

        return result

    # ==========================================
    # Approach 2: Direct In-Place Simulation (O(1) Auxiliary Space)
    # Advance pointers (r, c) directly along diagonals with edge reflections
    # Time Complexity: O(M * N)
    # Space Complexity: O(1) auxiliary (excluding return array)
    # ==========================================
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        if not mat or not mat[0]:
            return []

        m, n = len(mat), len(mat[0])
        result = []
        r, c = 0, 0
        up = True

        for _ in range(m * n):
            result.append(mat[r][c])

            if up:
                if c == n - 1:
                    r += 1
                    up = False
                elif r == 0:
                    c += 1
                    up = False
                else:
                    r -= 1
                    c += 1
            else:
                if r == m - 1:
                    c += 1
                    up = True
                elif c == 0:
                    r += 1
                    up = True
                else:
                    r += 1
                    c -= 1

        return result


# Local Test Verification
if __name__ == "__main__":
    solver = Solution()

    mat1 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    assert solver.findDiagonalOrder(mat1) == [1, 2, 4, 7, 5, 3, 6, 8, 9], "Test 1 failed"

    mat2 = [[1, 2], [3, 4]]
    assert solver.findDiagonalOrder(mat2) == [1, 2, 3, 4], "Test 2 failed"

    print("All tests passed for LeetCode #498: Diagonal Traverse!")
