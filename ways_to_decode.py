'''
InterviewBit
Ways to Decode
Problem Description
A message containing letters from A-Z is being encoded to numbers using the following mapping:
'A' -> 1
'B' -> 2
...
'Z' -> 26
Given an encoded message denoted by string A containing digits, determine the total number of ways to decode it. 


Problem Constraints
1 <= length(A) <= 105
'''
class Solution:
	# @param A : string
	# @return an integer
	def numDecodings(self, A):
	    if A.count('00')!=0 or len(A)==0:
	        return 0
	    arr =[int(x) for x in A]
	    stack=[]
	    for x in arr:
	        if x==0:
	            if len(stack)==0 or (stack[-1]!=1 and stack[-1]!=2):
	                return 0
	            else:
	                stack.pop()
	        else:
	            stack.append(x)
        if len(stack)==0:
            return 1
        prev = None;count =0;p1=0;p2=0;
        for x in stack:
            if prev==None:
                count =1
                prev =x;p1=1
            else:
                num = prev*10+x
                if num>10 and num<27:
                    count = p1+p2
                    p2=p1
                    p1=count
                else:
                    count =p1
                    p2=p1
                    p1=count
                prev = x    
        return p1            
            
            
            
            
            
            