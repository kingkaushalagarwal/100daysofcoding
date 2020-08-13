# from testInput import input
for _ in range(int(input())):
    a,b = map(int,input().split())
    c1 = a//9 + (1 if a%9>0 else 0)
    c2 = b//9 + (1 if b%9>0 else 0)
    # print(a,b,c1,c2)
    if c1<c2:
        print(0,c1)
    else:
        print(1,c2)



#1 1
# 1 2
# 0 2