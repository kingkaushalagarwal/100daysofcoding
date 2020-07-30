import sys
class Solution:
    def solve(self, A, B, C, D, E, F, G, H):
        fw = [[sys.maxsize] * (A+1) for i in range(A+1)]

        for i in range(B):
            u = D[i]
            v = E[i]
            w = F[i]
            fw[u][v] = min(w,fw[u][v])
            fw[v][u] = min(w,fw[v][u])
        for i in range(A+1):
            fw[i][i] = 0
        for k in range(1,A+1):
            for i in range(1,A+1):
                for j in range(1,A+1):
                     value =fw[i][k] + fw[k][j]
                     fw[i][j] = min(fw[i][j],value)

        ans = []
        for i in range(C):
            u, v = G[i] , H[i]
            value = fw[u][v]
            if value == sys.maxsize:
                ans.append(-1)
            else:
                ans.append(value)
        return ans
A = 15
B = 18
C = 29
D = [ 11, 2, 2, 6, 2, 8, 9, 3, 14, 15, 4, 14, 8, 7, 8, 6, 2, 12 ]
E = [ 2, 1, 1, 2, 1, 1, 7, 3, 2, 13, 2, 1, 6, 1, 7, 1, 2, 10 ]
F = [ 8337, 6651, 29, 7765, 3428, 5213, 6431, 2864, 3137, 4024, 8169, 5013, 7375, 3786, 4326, 6415, 8982, 6864 ]
G = [ 6, 2, 1, 15, 12, 2, 14, 10, 13, 15, 15, 4, 8, 7, 9, 4, 15, 13, 12, 5, 2, 10, 1, 11, 14, 7, 3, 13, 12 ]
H = [ 5, 2, 15, 13, 6, 2, 8, 6, 3, 13, 15, 3, 1, 1, 4, 4, 5, 8, 1, 3, 1, 10, 15, 9, 2, 1, 1, 10, 2 ]
ans  =Solution().solve(A, B, C, D, E, F, G, H)
print(ans)
