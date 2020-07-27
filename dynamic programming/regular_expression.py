def removingMultipleAstrik(B):
    prev = ""
    l=[]
    for i in range(len(B)):
        if B[i] == '*':
            if prev != B[i]:
                l.append(B[i])
        else:
            l.append(B[i])
        prev = B[i]
    return  ''.join(l)


A = "bacb"
B = "b**c*?*"
B = removingMultipleAstrik(B)
n = len(A)
m = len(B)
dp=[[0]*(m+1) for i in range(n+1)]
dp[0][0]=1
p=1
for i in range(1,m+1):
    if B[i-1]!='*':
        p=0
    dp[0][i]=p
for i in range(1,n+1):
    for j in range(1,m+1):
        if A[i-1]==B[j-1] or B[j-1]=='?' or B[j-1]=='*':
            dp[i][j]=dp[i-1][j-1]
        if B[j-1]=='*':
            dp[i][j] =dp[i][j]| dp[i-1][j]|dp[i][j-1]

for i in range(n+1):
    print(*dp[i])
# print(B)
# print(A,n)
