#Interviewbit
#minimum number of squares
from math import sqrt,ceil
class Solution:
	# @param A : integer
	# @return an integer
	def countMinSquares(self, n):
        if n<=3:return n
        dp=[0,1,2,3]
        for i in range(4,n+1):
            dp.append(i)
            x = 1
            s =i*i
            while x<s:  
                temp = x*x 
                if temp>i:
                    break
                else:
                    dp[i]= min(dp[i],1+dp[i-temp])
                x+=1    
        return dp[-1]      
