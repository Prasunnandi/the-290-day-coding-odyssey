"""
LeetCode 542: 01 Matrix
Difficulty: Medium
Topic: Matrix & Breadth-First Search (BFS)

Pattern: Multi-Source BFS
Rather than running BFS from each cell containing 1 (which would take O((M * N)^2)),
we reverse the search perspective:
  - Seed the BFS queue with ALL cells containing 0 simultaneously at distance 0.
  - Traverse outward level-by-level in 4 cardinal directions.
  - The first time a cell containing 1 is reached from any 0, the shortest Manhattan distance
    to the nearest 0 is guaranteed by the BFS shortest-path property.

Time Complexity: O(M * N) — every cell is enqueued and dequeued at most once.
Space Complexity: O(M * N) — queue and distance matrix.
"""

from collections import deque
from typing import List


class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        """
        Finds the distance of the nearest 0 for each cell in an m x n binary matrix.
        
        Args:
            mat: List[List[int]], binary matrix
            
        Returns:
            List[List[int]], distance matrix
        """
        m, n = len(mat), len(mat[0])
        dist = [[-1] * n for _ in range(m)]
        queue = deque()
        
        # Initialize queue with all 0-cells at distance 0
        for r in range(m):
            for c in range(n):
                if mat[r][c] == 0:
                    dist[r][c] = 0
                    queue.append((r, c))
                    
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        
        # Multi-source BFS expansion
        while queue:
            r, c = queue.popleft()
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if 0 <= nr < m and 0 <= nc < n and dist[nr][nc] == -1:
                    dist[nr][nc] = dist[r][c] + 1
                    queue.append((nr, nc))
                    
        return dist


if __name__ == "__main__":
    solver = Solution()
    
    # Test Case 1: Simple 3x3 with central 0
    mat1 = [
        [0, 0, 0],
        [0, 1, 0],
        [0, 0, 0]
    ]
    print("Test 1 Result:", solver.updateMatrix(mat1))
    # Expected: [[0, 0, 0], [0, 1, 0], [0, 0, 0]]
    
    # Test Case 2: Expanding distance
    mat2 = [
        [0, 0, 0],
        [0, 1, 0],
        [1, 1, 1]
    ]
    print("Test 2 Result:", solver.updateMatrix(mat2))
    # Expected: [[0, 0, 0], [0, 1, 0], [1, 2, 1]]
