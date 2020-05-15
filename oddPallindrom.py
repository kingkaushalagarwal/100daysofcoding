#InterviewBit
class Solution:
    # @param A : string
    # @return a list of integers
    def solve(self, A):
        def oddPallindrom(A):
            if len(A)==0:
                return []
            n = len(A)
            dp= [ [0]*n for i in range(n) ]
            mod = 10**9+7
            for length  in range(n-1,-1,-1):
                for i in range(n-length):
                    j = i+ length
                    if i==0 and j==n-1:
                        if A[i]==A[j]:
                            dp[i][j]=2
                        else:
                            dp[i][j]=1
                        continue
                    if A[i]==A[j]:
                        if i-1>=0:
                            dp[i][j]=dp[i-1][j]%mod
                        if j+1<n:
                            dp[i][j]+=dp[i][j+1]%mod
                        if i-1<0 or j+1>=n:
                            dp[i][j]+=1
                    else:
                        if i-1>=0:
                            dp[i][j]=dp[i-1][j]%mod
                        if j+1<n:
                            dp[i][j]+=dp[i][j+1]%mod
                        if i-1>=0 and j+1<n:
                            dp[i][j]-=dp[i-1][j+1]%mod
            ans =[]
            for i in range(n):
                if i==0 or i==n-1:
                    ans.append(1)
                else:
                    ans.append(dp[i-1][i+1]%mod)
            return ans
        
        ans = oddPallindrom(A)
        return ans
            
                            