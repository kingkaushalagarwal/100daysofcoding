#interviewBit 
#memoization solution
class Solution:
    # @param A : string
    # @return an integer
    def LBSlength(self, string):
        def lbs(string ,i ,j,maxx,dp):
            if i==j or i>j: return False
            if dp[i][j]!=-1:
                return dp[i][j]
            if (j-i+1)%2==0:
                cond1 = string[i]=='(' and string[j]==')'
                cond2 = string[i]=='{' and string[j]=='}'
                cond3 = string[i]=='[' and string[j]==']'
                if i+1==j and (cond1 or cond2 or cond3):
                    maxx[0]= max(maxx[0],j-i+1)
                    dp[i][j]=True
                    return dp[i][j]
                elif(cond1 or cond2 or cond3) and lbs(string,i+1,j-1,maxx,dp):
                    maxx[0]= max(maxx[0],j-i+1)
                    dp[i][j]=True
                    return dp[i][j]
                else:
                    for k in range(i+1,j-1):
                        if lbs(string,i,k,maxx,dp) and lbs(string,k+1,j,maxx,dp):
                            maxx[0]= max(maxx[0],j-i+1)
                            dp[i][j]=True
                            return dp[i][j]
            dp[i][j]=False
            lbs(string,i,j-1,maxx,dp) 
            lbs(string,i+1,j,maxx,dp)
    
                    
                
        
        n = len(string)
        dp=[[-1]*n for i in range(n)]
        maxx =[0]
        
        lbs(string,0,len(string)-1,maxx,dp)
        return maxx[0]    
        
            
            