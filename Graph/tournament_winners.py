#time complexity is exceeded in case of python but same solution perfectly run in C++
#my solution is same as editorial solution
from collections import defaultdict, deque
class Solution:
    # @param A : integer
    # @param B : list of list of integers
    # @return an integer
    def dfs(self, graph, s, visited, count):
        visited[s] = True
        count += 1
        for x in graph[s]:
            if visited[x] == False:
                count = max(count, self.dfs(graph, x, visited, count))
        return count

    def solve(self, A, B):
        graph = defaultdict(list)
        for i in range(A):
            for j in range(A):
                if B[i][j] == 1:
                    graph[i].append(j)
        ans = 0
        for i in range(A):
            visited = [False] * A
            count = 0
            count = self.dfs(graph, i, visited, count)
            if count == A:
                ans += 1
        return ans
