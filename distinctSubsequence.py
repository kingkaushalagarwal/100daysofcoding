#InterviewBit
'''
Distinct Subsequences
Problem Description
Given two sequences A and B, count number of unique ways in sequence A, to form a subsequence that is identical to the sequence B. Subsequence : A subsequence of a string is a new string which is formed from the original string by deleting some (can be none) of the characters without disturbing the relative positions of the remaining characters. (ie, "ACE" is a subsequence of "ABCDE" while "AEC" is not). 
'''
class Solution:
	# @param A : string
	# @param B : string
	# @return an integer
	def numDistinct(self, A, B):
        def bf(A,B,i,j):
            if j==0:
                return 1
            elif i==0 and j!=0:
                return 0
            if A[i-1]==B[j-1]:
                return bf(A,B,i-1,j-1)+bf(A,B,i-1,j)
            else:
                return bf(A,B,i-1,j)
        # ans = bf(A,B,len(A),len(B))
        if len(A)<len(B):return 0
        n = len(A)
        m = len(B)
        dp =[1]*(n+1) 
        for i in range(1,m+1):
            prev_up=None;prev =0    
            for j in range(i,n+1):
                if prev_up==None:
                    prev_up=dp[j-1]
                if B[i-1]==A[j-1]:
                    temp  =  dp[j]
                    dp[j] =  prev + prev_up
                    prev_up = temp 
                    prev = dp[j]
                else:
                    temp = dp[j]
                    dp[j] = prev
                    prev  = dp[j]
                    prev_up = temp
        return dp[-1]   
                
                
                