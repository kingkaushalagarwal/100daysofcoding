#InterviewBit Coin Sum Infinite
class Solution:
	# @param A : list of integers
	# @param B : integer
	# @return an integer
	def coinchange2(self, A, B):
        def find2(arr,N):
            dp =[[0]*(N+1) for i in range(2)]
            dp[0][0] = 1
            dp[1][0] = 1
            m = 10**6+7
            for i in range(1,len(arr)+1):
                ind = i&1
                for j in range(1,N+1):
                    if j<arr[i-1]:
                        dp[ind][j] = dp[ind^1][j]
                    else:
                        dp[ind][j] = dp[ind^1][j] + dp[ind][j-arr[i-1]]
            return dp[len(arr)&1][-1]%m
        return find2(A,B)    v