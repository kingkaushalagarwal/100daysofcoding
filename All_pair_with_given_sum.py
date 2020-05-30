#geeksforgeeks
#https://practice.geeksforgeeks.org/problems/find-all-pairs-whose-sum-is-x/0
#Find all pair with a given sum
from collections import Counter
for t in range(int(input())):
    n,m,x = map(int,input().split())
    arr1 = list(map(int,input().split()))
    arr2 = list(map(int,input().split()))
    arr1.sort()
    arr2.sort()
    i=0;j=m-1
    count = 0
    flag = True
    while i!=n and j!=-1:
        if arr1[i]+arr2[j]==x:
            if flag==False:
                print(end=", ")
            flag = False
            print(arr1[i],arr2[j],end="")
            i+=1;
            j-=1
        elif arr1[i]+arr2[j]<x:
            i+=1
        else:
            j-=1
    if flag:
        print(-1,end="")
    print()        