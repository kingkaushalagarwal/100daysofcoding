from testInput import input
for _ in range(int(input())):
    n = int(input())
    arr = list(map(int,input().split()))
    # print(arr)
    dp=[0]*(n+1)
    for i in range(8,-1,-1):
        for j in range(arr[i],n+1):
            dp[j]= max(dp[j],dp[j-arr[i]]*10 + (i+1) )
    if dp[-1]==0:
        print(-1)
    else:
        print(dp[-1])

