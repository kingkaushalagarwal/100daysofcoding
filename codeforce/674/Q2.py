# from testInput import input
for _ in range(int(input())):
    n,m = map(int,input().split())
    flag = False
    for i in range(n):
        a,b = map(int,input().split())
        c, d = map(int, input().split())
        if b==c: flag = True
    if m&1==1 or flag==False:
        print("NO")
    else:
        print("YES")
