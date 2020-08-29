class Solution:
    # @param A : integer
    # @param B : list of list of integers
    # @return an integer
    def find(self, ind, mask, A, dp, n):
        if mask == (2 ** n -2):
            return A[ind][0]
        if dp[ind][mask] != float('inf'):
            return dp[ind][mask]

        ans = float('inf')
        for i in range(1,n):
            if (mask & (1 << i)) or A[ind][i]==0:
                continue
            value = A[ind][i] + self.find(i, (mask | (1 << i)), A, dp, n)
            ans = min(ans,value)

        dp[ind][mask] = ans

        return ans

    def solve(self, n, A):
        dp = [[float('inf')] * (2 ** n) for i in range(n)]
        mask = 0
        ans = float('inf')
        for i in range(1, n):
            if A[0][i]!=0:
                ans = min(ans, A[0][i] + self.find(i, (mask | (1 << i)), A, dp, n) )

        return ans

A = 4
B =[ [0, 1, 2, 3],
     [3, 0, 2, 1],
     [5, 6, 0, 7],
     [8, 9, 0, 0]
]
ans = Solution().solve(A,B)
print(ans)
