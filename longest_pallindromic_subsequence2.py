# -*- coding: utf-8 -*-
"""
Created on Tue Jun  2 00:52:21 2020

@author: hp
"""

def input():
    global f;
    return f.readline().strip()
#Driver Code
f=open("D:/interview_bits/100daysofcoding/testcase/sample_input.txt",'r')
for t in range(int(input())):
    string = input()
    n = len(string)
    dp = [[0]*(n) for i in range(n)]
    for i in range(n):
        for j in range(n-i):
            if j==j+i:
                dp[j][j+i]=1
            else:
                val =0
#                print(j,j+i,end=" ")
#        print()
                if string[j]==string[j+i]:
#                    print(string[j],string[j+i])
                    val = dp[j+1][j+i-1] + 2

                dp[j][j+i] = max(dp[j][j+i-1],dp[j+1][j+i],val)
    print(dp[0][-1])
    for i in range(len(dp)):
        print(dp[i])
#bbabcbcab
#abbaab
