from testInput import input
from math import log,floor
for _ in range(int(input())):
    n,q = map(int,input().split())
    arr = list(map(int,input().split()))
    maxx =max(arr)
    length = int(log(maxx,2))+1
    print(maxx,length)
    msb= [[0]*length for i in range(n)]
    parent = [[0]*length for i in range(n)]

    for i in range(n):
        val = arr[i]
        # m = floor(log(arr[i],2)) +1
        count =0
        while val!=0 and val>>1!=0:
            if val&1==1:
                parent[i][count]+=1
            val = val>>1
            count+=1
        msb[i][count]+=1
    # print(*list(range(length)))
    # print(*arr)
    for i in range(n):
        print(arr[i])
        print(*msb[i],end="   ")
        print(*parent[i])
    for i in range(1,n):
        for j in range(length):
            msb[i][j] += msb[i-1][j]
            parent[i][j]+=parent[i-1][j]
    # for i in range(n):
    #     print(*msb[i])
    print("last line")
    print(msb[-1],parent[-1])
    for i in range(q):
        l,r = map(int,input().split())
        l=l-1;r=r-1
        ans = 0
        if l==0:
            ax = msb[r]
            ay=  parent[r]
        else:
            ax= [];ay=[]
            for j in range(length):
                ax.append(msb[r][j]-msb[l-1][j])
                ay.append(parent[r][j]-parent[l-1][j])
        for j in range(length):
            ans+= ax[j]*ay[j]
        print(ans)
        