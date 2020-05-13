#Interview Bit
#Regular expression matching

class Solution:
	# @param A : string
	# @param B : string
	# @return an integer
	def bruteForce(self,string,new_pattern,i,j):
	    if i==-1 and j==-1:
	        return True
	    elif i==-1 and j==0 and new_pattern[j]=='*':
	        return  True
	    elif i!=-1 and j==-1:
	        return False
	    if string[i]==new_pattern[j] or new_pattern[j]=='?':
	        return self.bruteForce(string,new_pattern,i-1,j-1)
	    elif new_pattern[j]=='*':
	        return self.bruteForce(string,new_pattern,i-1,j-1) or self.bruteForce(string,new_pattern,i-1,j)
	    else:return False     
    def optimise(self,string,pattern):
        m = len(string)
        n = len(pattern)
        dp= [ [False]*(m+1) for i in range(n+1) ]
        dp[0][0]=True
        for i in range(1,n+1):
            if dp[i-1][0] and pattern[i-1]=='*':
                dp[i][0] = True
            else:
                dp[i][0] = False
        for i in range(1,n+1):
            for j in range(1,m+1):
                v1 = dp[i-1][j]
                v2 = dp[i][j-1]
                v3 = dp[i-1][j-1]
                if pattern[i-1]==string[j-1] and v3:
                    dp[i][j]=True
                elif pattern[i-1]=='?' and v3:
                    dp[i][j]=True
                elif pattern[i-1]=='*' and (v1 or v2 or v3):
                    dp[i][j]=True
        # for i in range(len(dp)):
        #     print(dp[i])
        return dp[-1][-1]        
	                
	    
	def isMatch(self, string, pattern):
	    new_pattern =[]
	    prev =None
	    for i in range(len(pattern)):
	        if pattern[i]!='*':
	            new_pattern.append(pattern[i])
	        else:
	            if prev=='*':
	                continue
	            else:
	                new_pattern.append(pattern[i])
            prev = pattern[i]
	    ans = self.optimise(string,new_pattern)
        if ans:
            return 1
        else: return 0    