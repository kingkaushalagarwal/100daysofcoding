class Solution:
    def bruteForce(self,A,B,C,D):
        n = len(A) + 1
        # creating adjacency matrix
        dp = [[float('inf')] * n for i in range(n)]
        for i in range(n):
            dp[i][i] = 0
        for i in range(len(B)):
            u, v, w = B[i], C[i], D[i]
            dp[u][v] = min(dp[u][v], w)
            dp[v][u] = dp[u][v]
        # flyod warshell
        for k in range(1, n):
            for i in range(1, n):
                for j in range(1, n):
                    dp[i][j] = min(dp[i][j], dp[i][k] + dp[k][j])
        for i in range(1, n):
            for j in range(1, n):
                dp[i][j] += A[j - 1]
        ans = []
        for i in range(1, n):
            ans.append(min(dp[i]))
        return ans

    def solve(self, A, B, C, D):
        #time complexity exceeded in case of floyd warshall
        #using floyd_warshall algo
        # value  = self.bruteForce(A,B,C,D)
        ans = []
        ans = self.optimize(A,B,C,D)
        return ans
    #Driver Cod
A = [ 1, 2, 3, 1, 5 ]
B = [ 1, 2, 3, 4 ]
C = [ 2, 3, 4, 5 ]
D = [ 1, 1, 1, 1 ]
ans = Solution().solve(A,B,C,D)
print(ans)