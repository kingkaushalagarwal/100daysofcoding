# from testInput import input
for _ in range(int(input())):
    n = int(input())
    s = input()
    one=0
    zero=0
    mone=0
    mzero=0
    prev = None
    for i in range(n):
        if s[i]=='1':
            one+=1
            mzero += max(zero-1,0)
            zero= 0
        else:
            zero+=1
            mone += max(one-1,0)
            one=0
    mzero += max(zero - 1, 0)
    mone += max(one - 1, 0)
    minn = min(mone,mzero)
    maxx = max(mone,mzero)
    # print(minn,maxx)
    if minn!=0:
        print(minn)
    else:
        print(maxx)
    # print(min(mone,mzero)-1)