# -*- coding: utf-8 -*-
"""
Created on Mon Jun  1 23:54:28 2020
@author: hp
"""
def input():
    global f;
    return f.readline().strip()
#Driver Code
f=open("D:/interview_bits/100daysofcoding/testcase/sample_input.txt",'r')

def subsetSum_Memoization(arr):
    n = len(arr)
    dp = [ [None for i in range(sum(arr)//2 +1)] for j in range(n+1)]
    return subsetSum(arr,dp,n,sum(arr)//2)
def subsetSum(arr, dp ,n, total):
        if dp[n][total] is None:
            if total==0:
                dp[n][total]=True
            elif n==0 and total!=0:
                dp[n][total]=False
            elif total<arr[n-1]:
                dp[n][total]=subsetSum(arr,dp,n-1,total)
            elif total>=arr[n-1]:
                dp[n][total]= subsetSum(arr,dp,n-1,total) or subsetSum(arr,dp,n-1,total - arr[n-1])
        return dp[n][total]

def subsetSum_tabulation(arr):
    n = len(arr)
    dp = [ [False]*(n+1) for i in range(sum(arr)//2 + 1)]
    for i in range(n+1):
        dp[0][i] = True
    for i in range(1,sum(arr)//2+1):
        for j in range(1,n+1):
            dp[i][j]=dp[i][j-1]
            if i>=arr[j-1]:
                dp[i][j]=dp[i][j] or dp[i-arr[j-1]][j]
    return dp[sum(arr)//2][n]



t = int(input())
for _ in range(t):
    n = int(input())
    arr = list(map(int,input().split()))
    if sum(arr)%2==1:
        print('NO')
        continue
    if subsetSum_tabulation(arr):
        print("YES")
    else:
        print("NO")

    if subsetSum_Memoization(arr):
        print("YES")
    else:
        print("NO")


