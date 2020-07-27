#very very important problem
#minimum partition required for making every substring of partition palindrom
class Solution:
	# @param A : string
	# @return an integer
	def minCut(self, string):
	    n = len(string)
	    p=[ [False]*n for i in range(n)]
	    for i in range(n):
	        p[i][i]=True
	    for l in range(2,n+1):
	        for i in range(n-l+1):
	            j = i+l-1
	            if l==2:
	                if string[i]==string[j]:
	                    p[i][j]=True
	            else:
	                if string[i]==string[j] and p[i+1][j-1]==True:
	                    p[i][j]= True
	    dp=[-1]*n
	    for i in range(n):
	        if p[0][i]==True:
	            dp[i]=0
	        if dp[i]!=-1:
	            for j in range(i+1,n):
	                if p[i+1][j]==True:
	                    if dp[j]>dp[i]+1 or dp[j]==-1:
	                        dp[j]=dp[i]+1
	    return dp[-1]