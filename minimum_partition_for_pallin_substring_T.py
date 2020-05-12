#InterviewBit
#find minimum number of partition required to make every substring as pallindrome
#Tabulation 

def ispallin(string,i,j):
    while i<j:
        if string[i]!=string[j]:
            return False
        i+=1;j-=1
    return True
    
string = "abaxyyxyzy"
n = len(string)
p = [ [False]*n for j in range(n)]
for i in range(n):
    p[i][i]=True
for L in  range(2,n+1):
    for i in range(n-L+1):
        j = i+ L-1
        if L==2:
            if string[i]==string[j]:
                p[i][j]=True
        else:
           
            if string[i]==string[j] and p[i+1][j-1]:
                p[i][j]=True

dp =[-1]*n 
for i in range(n):
    if p[0][i]:
        dp[i]=0
    if dp[i]!=-1:
        for j in range(i+1,n):
            if p[i+1][j]:
                if dp[j]>dp[i]+1 or dp[j]==-1: 
                    dp[j]=dp[i]+1 
print(dp[-1])                    
        