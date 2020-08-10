#giving wrong answer
from copy import deepcopy
from testInput import input;
for _ in range(int(input())):
    n, x = map(int,input().split())
    arr = list(map(int,input().split()))
    arr.sort();
    i=0;days=0

    while x<max(arr):
        if arr[i]<=x:
            while  i<len(arr) and arr[i]<=x:
                if arr[i]*2>x:
                    x = arr[i]*2
                    arr[i]=-1
                    days+=1
                i+=1
        else:
            x = 2*x
            days+=1
    for i in range(len(arr)):
        if arr[i]!=-1:
            days+=1
    print(days)