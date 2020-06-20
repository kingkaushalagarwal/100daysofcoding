#InterviewBit Dungeon Princess
class Solution:
	# @param A : list of list of integers
	# @return an integer
	def calculateMinimumHP(self, dp):
        if dp[-1][-1]>0:
            dp[-1][-1]=1
        else:
            dp[-1][-1] = 1 - dp[-1][-1]
        n = len(dp)
        m = len(dp[0])
        for i in range(n-1,-1,-1):
            for j in range(m-1,-1,-1):
                if i==n-1 and j==m-1:
                    continue           
                if i+1==n:
                    val = dp[i][j+1] - dp[i][j]
                    if val<=0:
                        val = 1
                    dp[i][j] = val    
                    continue
                if j+1==m:
                    val = dp[i+1][j] - dp[i][j]
                    if val<=0:
                        val =1
                    dp[i][j] = val
                    continue
                val1  = dp[i][j+1] - dp[i][j]
                if val1<=0:
                    val1 = 1
                val2 = dp[i+1][j] - dp[i][j]
                if val2<=0:
                    val2 =1
                dp[i][j] = min(val1,val2)    
        return dp[0][0]            
        
        
        
        
        