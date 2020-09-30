# from testInput import input
from math import factorial
from heapq import heappush,heappop
def expo(x,n,p):
    if n==0:
        return 1
    elif n==1:
        return x%p
    elif n&1:
        return ((x%p)*expo((x*x)%p,n//2,p)%p)
    else:
        return expo((x*x)%p,n//2,p)%p

def combination(n,r,p):
    if n<r:
        return 0
    num=den=1
    for i in range(r):
        num = (num*(n-i))%p
        den = (den*(i+1))%p
    return (num*expo(den,p-2,p))%p


m = 998244353
n,k = map(int,input().split())
arr =[]
for _ in range(n):
    arr.append(list(map(int,input().split())))
if k==1:
    print(n)
else:
    count = 0
    ans = 0
    arr.sort()
    pq= []
    for i in range(n):
        s,e = arr[i]
        while pq and pq[0]<s:
            heappop(pq)
            count-=1
        value=combination(count,k-1,m)
        ans+=value
        count+=1
        heappush(pq,e)
    print(ans)
    # print(pq)