#Stepping number interview Bit

from testInput import input
from collections import deque
N,M = map(int,input().split())
ans =[0]
queue =deque([1,2,3,4,5,6,7,8,9])
# print("start")
while len(queue)!=0:
    # print(queue)
    u = queue.popleft()
    ans.append(u)
    last_digit = u%10
    if last_digit==0:
        v= u*10+1
        if v<=M:
            queue.append(v)
    elif last_digit==9:
        v = u*10+8
        if v<=M:
            queue.append(v)
    else:
        v1 = u*10 +last_digit - 1
        v2 = u*10+ last_digit + 1
        if v1<=M:
            queue.append(v1)
        if v2<=M:
            queue.append(v2)

l=0;r=len(ans)-1
start =-1
while l<=r:
    mid = (l+r)//2
    if ans[mid]==N:
        start = mid
        break
    elif ans[mid]>N:
        r=mid-1
    else:
        l=mid+1
if start!=-1:
    print(*ans[start : ])
else:
    print(*ans[l:])
