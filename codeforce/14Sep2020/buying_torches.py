from math import ceil
# from testInput import input
for _ in range(int(input())):
    x,y,k = map(int,input().split())
    print(ceil((k*(y+1))/(x-1))+k)
# 14
# 33
# 25
# 2000000003
# 1000000001999999999
