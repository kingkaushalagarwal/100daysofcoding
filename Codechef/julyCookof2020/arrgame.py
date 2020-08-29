# from testInput import input
from collections import defaultdict
for _ in range(int(input())):
    n = int(input())
    arr = list(map(int,input().split()))
    even=0
    odd=0
    prev=1
    count=0
    d =defaultdict(int)
    prev=None
    for x in arr:
        if x==0:
            count+=1
        else:
            if prev==0:
                if count&1:
                    odd = max(odd,count)
                else:
                    even = max(even,count)
                d[count]+=1
            count=0
        prev = x
    if prev==0:
        if count & 1:
            odd = max(odd, count)
        else:
            even = max(even, count)
        d[count]+=1
    # print(d)
    if even>=odd or d[odd]>1:
        print("No")
    else:
        print("Yes")
