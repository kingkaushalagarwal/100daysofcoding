#interviewBit
#longest balance substring
#meomory limit exceed
string = input()
n = len(string)
dp=[[-1]*n for i in range(n)]
maxx =[0]
for l in range(n):
    for m in range(n-l):
        i=m;j=l+m				
        cond = string[i]=='(' and string[j]==')' or  string[i]=='{' and string[j]=='}' or string[i]=='[' and string[j]==']'
        
        if (j-i+1)&1:
            dp[i][j]= False
        elif i+1==j and cond:
            maxx[0]= max(maxx[0],j-i+1)
            dp[i][j]=True
        elif cond and dp[i+1][j-1]:
            maxx[0]= max(maxx[0],j-i+1)
            dp[i][j]=True
        else:
            for k in range(i+1,j-1):
                if dp[i][k] and dp[k+1][j]:
                    maxx[0]= max(maxx[0],j-i+1)
                    dp[i][j]=True
            if dp[i][j]==-1:
                    dp[i][j]=False