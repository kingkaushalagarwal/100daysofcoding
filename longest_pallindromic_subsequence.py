#Interview bit
#longest pallindromic subsequence
class Solution:
    # @param A : string
    # @return an integer
    def solve(self, A):
        n = len(A)
        if n == 0: return 0
        dp = [ [0]*(n+1) for i in range(n+1) ]
        for i in range(1,n+1):
            dp[i][i]=1
        for l in range(1,n+1):
            for m in range(1,n+1-l):
                i=m;j=l+m
                if A[i-1]==A[j-1]:
                    dp[i][j]=2+dp[i+1][j-1]
                else:
                    dp[i][j]=max(dp[i+1][j],dp[i][j-1])
        return dp[1][-1]            
                
                