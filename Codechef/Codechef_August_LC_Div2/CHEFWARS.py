from testInput import input
for _ in range(int(input())):
    H,P = map(int,input().split())
    while H>0 and P>0:
        H = H-P
        P= P//2
    if H==0 and P==0:
        print(1)
    elif P>0:
        print(1)
    else:
        print(0)