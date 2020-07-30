# from testInput import input
for _ in range(int(input())):
    a,b = map(int,input().split())
    if b%2==1:
        b=b-1
    if b//2>=a:
        print(b//2,b)
    else:
        print(-1,-1)
