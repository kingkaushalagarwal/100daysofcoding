from math import ceil
# from testInput import input

def find(n):
    if n==0 or n==1:
        return 0
    elif n==2:
        return 1
    minn = n - 1
    k=2
    # for k in range(2,min(n,100005)):
    value = (k - 1) + (n // k - 1)
    while minn>value:
        if minn>value:
            minn = value
            if n%k!=0:
                minn+=1
        k+=1
        value = (k - 1) + (n // k - 1)
    return minn



for _ in range(int(input())):
    n = int(input())
    print(find(n))
# 0
# 3
# 11
# 72
# 63244