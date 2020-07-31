#interviewBit
#slightly different approach using DSU
class Solution:
    # @param A : list of list of integers
    # @return an integer
    def find(self, u, parent):
        if parent[u] == u:
            return u
        par = self.find(parent[u], parent)
        parent[u] = par
        return par

    def union(self, u, v, parent, height):
        C = self.find(u, parent)
        D = self.find(v, parent)
        if C == D:
            return
        if height[C] > height[D]:
            parent[D] = C
        elif height[D] > height[C]:
            parent[C] = D
        else:
            height[C] = +1
            parent[D] = C

    def check(self, r, c, n, m):
        return r >= 0 and r < n and c >= 0 and c < m

    def change(self, source, n, m, parent, height, A):
        row = [1, -1, 0, 0, 1, 1, -1, -1]
        col = [0, 0, 1, -1, 1, -1, 1, -1]
        stack = [source]
        while len(stack) != 0:
            s = stack.pop()
            r = s // m;
            c = s % m
            for i in range(8):
                nr = r + row[i]
                nc = c + col[i]
                ns = nr * m + nc
                if self.check(nr, nc, n, m) and parent[ns] == (ns) and A[nr][nc] == 1:
                    self.union(s, ns, parent, height)
                    stack.append(ns)

    def solve(self, A):
        n = len(A)
        m = len(A[0])
        height = [1] * (n * m)
        parent = list(range(n * m))
        count = 0
        for i in range(n):
            for j in range(m):
                s = i * m + j
                if A[i][j] == 1 and parent[s] == s:
                    count += 1
                    self.change(s, n, m, parent, height, A)
        return count



