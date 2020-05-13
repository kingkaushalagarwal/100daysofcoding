#interview Bit
#Longest common subsequence 

class Solution:
    # @param A : string
    # @param B : string
    # @return an integer
    def solve(self, A, B):
        n = len(A)
        m = len(B)
        if n==0 or m==0:
            return 0
        dp= [0]*(m+1)
        prev = 0
        for i in range(1,n+1):
            prev_up= 0;prev=0
            for j in range(1,m+1):
                temp = dp[j]
                if A[i-1]==B[j-1]:
                    dp[j]= 1+prev_up
                else:
                    dp[j]= max(dp[j],dp[j-1])
                prev_up = temp    
        return dp[-1]        
                
