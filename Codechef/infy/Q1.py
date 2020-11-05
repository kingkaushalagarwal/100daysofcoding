from testInput import input
for _ in range(int(input())):
    x,y = map(int,input().split())
    d = abs(x-y)
    if d==0:
        print(0)
    elif y>x:
        if d%2==1:
            print(1)
        else:
            print(2)
    else:
        if d%2==1:
            print(2)
        else:
            print(1)