from typing import List
class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        if len(grid)==0:
            return 0
        n = len(grid)
        m = len(grid[0])
        prev = 0
        for i in range(n):
            grid[i][0] += prev
            prev = grid[i][0]
        prev =0
        for j in range(m):
            grid[0][j] += prev
            prev = grid[0][j]
        for i in range(1,n):
            for j in range(1,m):
                grid[i][j] += min(grid[i-1][j],grid[i][j-1])
        return grid[-1][-1]