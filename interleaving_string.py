import sys
#using i+j-1 as k which reduce 3 parameter and problem solved in 2-D array
def Tabulation(A, B, C):
    n = len(A)
    m = len(B)
    dp = [[0] * (m + 1) for i in range(n + 1)]
    for i in range(n + 1):
        for j in range(m + 1):
            if i == 0 and j == 0:
                dp[i][j] = 1
            elif i == 0:
                if B[j - 1] == C[j - 1]:
                    dp[i][j] = dp[i][j - 1]
            elif j == 0:
                if A[i - 1] == C[i - 1]:
                    dp[i][j] = dp[i - 1][j]
            elif A[i - 1] != C[i + j - 1] and B[j - 1] == C[i + j - 1]:
                dp[i][j] = dp[i][j - 1]
            elif A[i - 1] == C[i + j - 1] and B[j - 1] != C[i + j - 1]:
                dp[i][j] = dp[i - 1][j]
            elif A[i - 1] == C[i + j - 1] and B[j - 1] == C[i + j - 1]:
                dp[i][j] = dp[i - 1][j] or dp[i][j - 1]
    return dp[n][m]


def find(A,B,C,i,j,k):
    # print(i,j,k)
    if k<0 :
        if (i>=0 or j>=0):
            return 0
        else:
            return 1
    if i<0:
        if B[j]==C[k]:
            return find(A,B,C,i,j-1,k-1)
        else:
            return 0
    elif j<0:
        if A[i]==C[k]:
            return find(A,B,C,i-1,j,k-1)
        else:
            return 0
    elif A[i]!=C[k] and B[j]!=C[k]:
        return 0
    elif A[i]!=C[k] and B[j]==C[k]:
        return find(A,B,C,i,j-1,k-1)
    elif A[i]==C[k] and B[j]!=C[k]:
        return find(A, B, C, i-1, j , k - 1)
    elif A[i] == C[k] and B[j] == C[k]:
        return find(A, B, C, i - 1, j, k - 1) or find(A,B,C,i,j-1,k-1)


#Driver Code
A = "LgR8D8k7t8KIprKDTQ7aoo7ed6mhKQwWlFxXpyjPkh"
B = "Q7wQk8rqjaH971SqSQJAMgqYyETo4KmlF4ybf"
C = "Q7wLgR8D8Qkk7t88KIrpqjarHKD971SqSQJTQ7aoAMgoq7eYd6yETmhoK4KmlQwWFlF4xybXfpyjPkh"
if (len(A)+len(B))!=len(C):
    print(0)
    sys.exit(0)
l = len(A)-1
m = len(B)-1
n = len(C)-1
ans = find(A,B,C,l,m,n)


print(ans)