#interviewBit
#Distinct Subsequence
from typing import List
def numDistinct( A, B):
    dp = [0]*(len(B)+1)
    dp[0]=1
    for i in range(1,len(A)+1):
        prev = 1
        for j in range(1,len(B)+1):
            temp = dp[j]
            if A[i-1]==B[j-1]:
                dp[j] = dp[j]+prev
            else:
                dp[j] = dp[j]
            prev = temp
    return dp[-1]
A = "rabbbit"
B = "rabbit"
ans = numDistinct(A,B)
print(ans)