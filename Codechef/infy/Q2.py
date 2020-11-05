from testInput import input
# from heapq import heapify,heappush,heappop
from copy import deepcopy
for _ in range(int(input())):
    n = int(input())
    ans = list(map(int,input().split()))
    pq =[[ans[i],i] for i in range(len(ans))]
    # heapify(pq)
    visited =[False]*n
    # ans = deepcopy(ans)
    for i in range(len(ans)):
        val,ind = ans[i],i
        if visited[ind]==False:
            i = ind+1
            while i<len(ans):
                if (val + i-ind)<ans[i]:
                    ans[i] = val+ i - ind
                    visited[i] = True
                else:
                    break
                i+=1
            i = ind-1
            while i>-1:
                if (val+ind-i)<ans[i]:
                    ans[i] = val + ind - i
                    visited[i] = True
                else:
                    break
                i-=1
            visited[ind]=True
    print(*ans)