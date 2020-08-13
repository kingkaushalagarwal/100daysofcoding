# from testInput import input
for _ in range(int(input())):
    n,k = map(int,input().split())
    arr = list(map(int,input().split()))
    mincount = float('inf')
    num = None

    for i in range(n):
        if arr[i]>0 and arr[i]<=k:
            # print(k,arr[i])
            if k%arr[i]==0:
                c = k//arr[i]
                if mincount>c:
                    mincount = c
                    num = arr[i]

    if mincount==float('inf'):
        print(-1)
    else:
        print(num)

