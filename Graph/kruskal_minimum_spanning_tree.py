#Interview Bit
"""
Input Format
The first argument contains an integer, A, representing the number of islands.

The second argument contains an 2-d integer matrix, B, of size M x 3 where Island B[i][0] and B[i][1] are connected using a bridge of cost B[i][2].

Output Format
Return an integer representing the minimal cost required.
"""

#implemented using Disjoint Set union
class Solution:
    # @param A : integer
    # @param B : list of list of integers
    # @return an integer
    def find(self, u, parent):
        if parent[u] == u:
            return u
        par = self.find(parent[u], parent)
        parent[u] = par
        return par

    def union(self, u, v, height, parent):
        C = self.find(u, parent)

        D = self.find(v, parent)
        if (C == D):
            return False


        if height[C] > height[D]:
            parent[D] = C
        elif height[D] > height[C]:
            parent[C] = D
        else:
            height[C] += 1
            parent[D] = C
        return True


    def solve(self, A, B):
        parent = list(range(A + 1))
        height = [1] * (A + 1)
        B = sorted(B, key=lambda a: a[2])
        cost = 0
        for i in range(len(B)):
            u = B[i][0]
            v = B[i][1]
            if self.union(u, v, height, parent):
                cost += B[i][2]
        return cost

