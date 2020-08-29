from collections import defaultdict
from testInput import input
for _ in range(int(input())):
    n = int(input())
    arr = list(map(int,input().split()))
    prefix = [[0]*(n+1) for i in range(n+1)]
    for i in range(1,n+1):
        for j in range(1,n+1):
            if arr[j-1]==i:
                prefix[i][j] = prefix[i][j-1]+1
            else:
                prefix[i][j] = prefix[i][j-1]
    for i in range(len(prefix)):
        print(prefix[i])
    d =defaultdict(list)
    for i in range(n):
        d[arr[i]].append(i+1)
    count = 0
    for key,value in d.items():
        if len(value)<=1:
            continue
        else:
            for s in range(len(value)):
                for t in range(s+1,len(value)):
                    v1 = value[s]
                    v2 = value[t]
                    if (v1+1)!=v2:
                        for i in range(1,n+1):
                            a = prefix[i][v2]-prefix[i][v1]-1
                            b = prefix[i][-1] =prefix[i][v2]
                            print(i,key,a,b,v1,v2)
                            count += a*b
    print(count)