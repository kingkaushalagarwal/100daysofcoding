import heapq
from heapq import heapify, heappush,heappop
def solve(dest,gas,miles,capacity):
    ans =0
    pq =[]
    for i in range(len(miles)):
        if gas>=dest:
            return ans
        if gas<miles[i]:
            while len(pq)!=0 and gas<miles[i]:
                gas += -heappop(pq)
                ans+=1
            if len(pq)==0 and gas<miles[i]:
                return -1
        heappush(pq, -capacity[i])

    while len(pq)!=0 and gas<dest:
        gas += -heappop(pq)
        ans+=1
        if len(pq)==0 and gas<miles[i]:
            return -1
    return ans
dest = 100
gas = 2
mile = [10]
capacity = [100]
# A = 100
# B = 2
# C = [10]
# D = [100]
ans = solve(dest,gas,mile,capacity)
print(ans)