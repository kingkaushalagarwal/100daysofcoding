#Interview Bit
"""
All the approachs are similar but by observation reducing memory and time
coinChangeTabulation, memoryOptimizeTabulation and spaceAndTimeOptimize solution.
"""

#Brute Force Solution
def coinChange(A,B,i):
    if B==0:
        return 1
    if i<0:
        return 0
    ans =0
    if B-A[i]>=0:
        ans+= coinChange(A,B-A[i],i)
    ans+= coinChange(A,B,i-1)
    return ans

#Solution 1
def coinChangeTabulation(A,B):
    n = len(A)
    dp = [[0] * (B + 1) for i in range(n + 1)]
    for i in range(n+1):
        dp[i][0]=1
    for i in range(1,n+1):
        for j in range(1,B+1):
            if j<A[i-1]:
                dp[i][j]=dp[i-1][j]
            else:
                dp[i][j] = dp[i][j-A[i-1]] + dp[i-1][j]
    for i in range(n+1):
        print(*dp[i])
    print(dp[-1][-1])

#Solution 2
def MemoryOptimizeTabulation(A, B):
    n = len(A)
    dp = [[0] * (B + 1) for i in range(2)]
    dp[0][0] = 1
    dp[1][0] = 1

    for i in range(1, n + 1):
        for j in range(1, B + 1):
            if j < A[i - 1]:
                dp[i % 2][j] = dp[(i - 1) % 2][j]
            else:
                dp[i % 2][j] = dp[i % 2][j - A[i - 1]] + dp[(i - 1) % 2][j]

    return dp[(B + 1) % 2][-1]

#Solution 3
def spaceAndTimeOptimize(A,B):
    n = len(A)
    dp = [0] * (B + 1)
    dp[0] = 1
    for i in range(n):
        for j in range(A[i], B + 1):
            dp[j] += dp[j - A[i]]

    return dp[-1]
#Driver Code
A = [1,2,3]
B = 4
n = len(A)
# ans = coinChange(A,B,n-1)
# coinChangeTabulation(A,B)
ans = spaceAndTimeOptimize(A,B)
print("ans: ",ans)