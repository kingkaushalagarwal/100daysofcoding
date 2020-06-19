#Number of coins from geeksforgeeks
for t in range(int(input())): 
    n,c = map(int,input().split())
    coin = list(map(int,input().split()))
    # coin.sort()
    MAX=10**9
    dp=[MAX]*(n+1)
    dp[0]=0
    # for i in range(n+1):
    #     for j in range(c):
    #         if i<coin[j]:
    #             break
    #         if i>=coin[j] and dp[i-coin[j]]!=-1:
    #             if dp[i]==-1:
    #                 dp[i] = dp[i-coin[j]] + 1
    #             else:
    #                 dp[i] = min(dp[i],dp[i-coin[j]] + 1)
    
    for i in range(c):
        for j in range(coin[i],n+1):
            if dp[j-coin[i]]!=MAX:
                dp[j]= min(dp[j],dp[j-coin[i]]+1)
                
    if dp[n]!=MAX:                    
        print(dp[n])
    else:
        print('-1')