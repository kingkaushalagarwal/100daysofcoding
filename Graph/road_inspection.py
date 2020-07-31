class Solution:
    # @param A : integer
    # @param B : list of list of integers
    # @return a list of integers
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
            height[C] += 1
            parent[D] = C

    def solve(self, A, B):
        height = [1] * (A + 1)
        parent = list(range(A + 1))
        ans = []
        for i in range(len(B)):
            type, u, v = B[i]
            if type == 0:
                self.union(u, v, parent, height)
            else:
                C = self.find(u, parent)
                D = self.find(v, parent)
                if C == D:
                    ans.append(1)
                else:
                    ans.append(0)
        return ans

