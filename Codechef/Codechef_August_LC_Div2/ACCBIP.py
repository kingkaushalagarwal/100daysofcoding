from heapq import heappush, heappop,heapify
from testInput import input
for _ in range(int(input())):
    n,color,earser = map(int,input().split())
    freq ={}
    line=[]
    for i in range(n):
        l = list(map(int, input().split()))
        line.append(l)
        if l[2] not in freq:
            freq[l[2]]=1
        else:
            freq[l[2]]+=1
    pq = [-x for x in freq.values()]
    heapify(pq)
    cost =list(map(int,input().split()))
    while earser>cost[0]:
        val = -heappop(pq)
        if val==0:
            break
        else:
            val = val-1
        heappush(pq,-val)
        earser -=cost[0]
    count =0
    for x in pq:
        val = -x
        count += (val*(val-1)*(val-2))//6
    print(count)

    