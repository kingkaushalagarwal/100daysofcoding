A="abba"
n = len(A)
dp = [[0] * (n + 1) for j in range(n + 1)]
for i in range(1, n + 1):
    for j in range(1,n + 1):
        if A[i - 1] == A[j - 1] and i != j:
            dp[i][j] = dp[i - 1][j - 1] + 1
        else:
            dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
for  i in range(len(dp)):
    print(*dp[i])

