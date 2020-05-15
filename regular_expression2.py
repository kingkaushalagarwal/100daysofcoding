'''
InterviewBit
Regular Expression II
Problem Description
Implement wildcard pattern matching with support for ' ? ' and ' * ' for strings A and B.
' . ' : Matches any single character.
' * ' : Matches zero or more of the preceding element.
 The matching should cover the entire input string (not partial).  
Example Input
Input 1:
 A = "aab"
 B = "c*a*b"
Input 2:
 A = "acz"
 B = "a.a" 
'''
class Solution:
	# @param A : string
	# @param B : string
	# @return an integer
	def isMatch(self, A, B):
        d = {}
        arr =[]
        k=0
        for i in range(len(B)):
            if B[i]=='*':
               d[k-1]=None
            else:
                k+=1
                arr.append(B[i])
        B= arr
        n = len(A)
        m = len(B)
        
        dp =[[0]*(m+1) for i in range(n+1)]
        dp[0][0]=1
        
        for j in range(1,m+1):
            if j-1 not in d:
                dp[0][j]=0
            else:
                dp[0][j]=dp[0][j-1]
        for i in range(1,n+1):
            for j in range(1,m+1):        
                if j-1 not in d:
                    if A[i-1]==B[j-1] or B[j-1]=='.':
                        dp[i][j]=dp[i-1][j-1]
                    else:
                        dp[i][j]=0
                else:
                    if A[i-1]!=B[j-1] and B[j-1]!='.':
                        dp[i][j]=dp[i][j-1]
                    else:
                        dp[i][j]=dp[i-1][j] | dp[i][j-1]
        return dp[-1][-1]                
                        
                        