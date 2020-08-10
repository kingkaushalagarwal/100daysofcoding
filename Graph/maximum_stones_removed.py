# Interview Bit leetcode solution
from collections import defaultdict
class DSU:
    def __init__(self,N):
        self.p = list(range(N))
    def find(self,x):
        if self.p[x]!=x:
            self.p[x] = self.find(self.p[x])
        return self.p[x]
    def union(self,x,y):
        xr = self.find(x)
        yr = self.find(y)
        self.p[xr]= yr
class Solution(object):
    #DFS Approachs
    def removeStones(self, stones):
        graph = defaultdict(list)
        for i, x in enumerate(stones):
            for j in range(i):
                y = stones[j]
                if x[0]==y[0] or x[1]==y[1]:
                    graph[i].append(j)
                    graph[j].append(i)

        N = len(stones)
        ans = 0

        seen = [False] * N
        for i in range(N):
            if not seen[i]:
                stack = [i]
                seen[i] = True
                while stack:
                    ans += 1
                    node = stack.pop()
                    for nei in graph[node]:
                        if not seen[nei]:
                            stack.append(nei)
                            seen[nei] = True
                ans -= 1
        return ans
    def solve(self,stones):
        N = len(stones)
        dsu = DSU(200000)
        for x,y in stones:
            dsu.union(x,y+100000)
        return N - len({dsu.find(x) for x,y in stones})
A =[[6, 2],
  [9, 6],
  [7, 6],
  [5, 9],
  [8, 6],
  [9, 1],
]
ans = Solution().removeStones(A)
ans1 = Solution().solve(A)
print (ans,ans1)