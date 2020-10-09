from typing import List
from copy import deepcopy


class Solution:
    def check(self, r, c, n, m):
        return r >= 0 and r < n and c >= 0 and c < m

    def cherryPickup(self, grid: List[List[int]]) -> int:
        if len(grid) == 0 or grid[0][0] == -1 or grid[-1][-1] == -1:
            return 0
        n = len(grid)
        m = len(grid[0])
        array = deepcopy(grid)
        prev = 0
        for i in range(n):
            if array[i][0] == -1:
                prev = -1
            elif prev == -1:
                array[i][0] = -1
            else:
                array[i][0] += prev
                prev = array[i][0]
        prev = 0
        for j in range(m):
            if array[0][j] == -1:
                prev = -1
            elif prev == -1:
                array[0][j] = -1
            else:
                array[0][j] += prev
                prev = array[0][j]
        for i in range(len(array)):
            print(*array[i])
        print()
        # calculating the maximum cherries in top to bottom path
        for i in range(1, n):
            for j in range(1, m):
                if array[i][j] == -1:
                    continue
                a = -1;
                b = -1
                if array[i - 1][j] != -1:
                    a = array[i - 1][j]
                if array[i][j - 1] != -1:
                    b = array[i][j - 1]
                if (a == -1) and (b == -1):
                    array[i][j] = -1
                else:
                    array[i][j] += max(a, b)

        # either no cherries in the path or their is some blockage in the path
        for i in range(len(array)):
            print(*array[i])
        print(array[-1][-1])
        if array[-1][-1] == 0 or array[-1][-1] == -1:
            return 0
        cherries = array[-1][-1]

        i = n - 1;
        j = m - 1
        while self.check(i, j, n, m):
            r1, c1 = i - 1, j
            r2, c2 = i, j - 1
            a = -1;
            b = -1
            if self.check(r1, c1, n, m) and array[r1][c1] >= 0:
                a = array[r1][c1]
            if self.check(r2, c2, n, m) and array[r2][c2] >= 0:
                b = array[r2][c2]
            if grid[i][j] == 1:
                grid[i][j] = 0
            if a != 1 or b != -1:
                if a > b:

                    i = r1;
                    j = c1
                else:
                    i = r2;
                    j = c2
            else:
                break
        array = deepcopy(grid)
        for i in range(1, n):
            for j in range(1, m):
                if array[i][j] == -1:
                    continue
                a = 0;
                b = 0
                if array[i - 1][j] != -1:
                    a = array[i - 1][j]
                if array[i][j - 1] != -1:
                    b = array[i][j - 1]
                array[i][j] += max(a, b)
        cherries += array[-1][-1]
        return cherries



grid = [[1,1,-1],[1,-1,1],[-1,1,1]]
ans  = Solution().cherryPickup(grid)
print(ans)