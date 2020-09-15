# from testInput import input
for _ in range(int(input())):
    n=int(input())
    if n&1: #odd
        if (n+1)%4==0:
            print((n+1)//4+1)
        else:
            print(0)
    else:
        if n%4==0:
            print(n//4+1)
        else:
            print(0)