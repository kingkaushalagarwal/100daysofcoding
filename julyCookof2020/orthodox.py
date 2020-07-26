"""
Simple observation is that each number must have atleast unique set bit which others does not have
So, total different number possible is log(10**18,2)==62
"""
# from testInput import input
from math import log
# print(log(10**18,2))
for _ in range(int(input())):
    n = int(input())
    arr = list(map(int,input().split()))
    if n>62:
        print("NO")
    else:
        d={}
        flag = False
        for i in range(len(arr)):
            num=0
            for j in range(i,len(arr)):
                num = num|arr[j]
                if num not in d:
                    d[num]=None
                else:
                    flag = True
                    break
            if flag:
                break
        if flag:
            print("NO")
        else:
            print("YES")

