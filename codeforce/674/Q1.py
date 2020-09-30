# from testInput import input
from math import ceil
for _ in range(int(input())):
    n,x = map(int,input().split())
    if n<=2:
        print(1)
    else:
        value = ceil(n//x)
        n-=2
        print(ceil(n/x)+1)
