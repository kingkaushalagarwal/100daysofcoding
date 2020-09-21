# from testInput import input
from math import log,floor
def f(n):
    if n==0 or n==1:
        return 1
    if n==2 or n==3:
        return 1
    return min(f(n//2)+1,f(n//2-1)+1)
for i in range(2,100):
    # n = int(input())
    n =i
    print(i, floor(log(n,2)),f(n))
