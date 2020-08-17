from collections import defaultdict


class Tree:
    def __init__(self):
        self.t = defaultdict(list)

    def add(self, u, v):
        self.t[u].append(v)
        self.t[v].append(u)


class Solution:
    # @param A : integer
    # @param B : list of integers
    # @param C : list of integers
    # @return an integer
    def dfs(self, T, parent, source, summ, count, maxx, visited, C):
        if count == 0:
            return
        visited[source] == True
        value = abs(C[parent - 1] - C[source - 1])
        print("parent: ",parent," source: ",source," value: ",value," count: ",count," summ: ",summ)
        maxx[0] = max(maxx[0], value * count+summ)
        summ += value
        count -= 1
        for x in T.t[source]:
            if visited[x] == False:
                self.dfs(T, source, x, summ, count, maxx, visited, C)

    def solve(self, A, B, C):
        T = Tree()
        for i in range(1, len(B)):
            T.add(i + 1, B[i])
        visited = [False] * (len(B) + 1)
        start = 1
        count = A
        maxx = [0]
        visited[start]=True
        for x in T.t[start]:
            if visited[x] == False:
                self.dfs(T, start, x, 0, count, maxx, visited, C)
        return maxx[0]



A = 3
B = [0, 1, 1, 2, 2, 3]
C = [1, 6, 7, 21, 5, 18]
ans = Solution().solve(A,B,C)
print(ans)