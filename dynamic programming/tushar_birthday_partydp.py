#InterviewBit Tushar's Birthday party
def solve(A,B,C):
    dp = [-1]*(max(A)+1)
    dp[0] = 0
    total_cost = 0
    for x in  A:
        total_cost += calculate(x,B,C,dp)
    print(dp)    
    return total_cost     
def calculate(W,B,C,dp):
    if W==0:
        return 0
    if dp[W]!=-1:
        return dp[W]
    n = len(B)
    min_cost = 0
    for i in range(n):
        if W-B[i]>=0:
            value = C[i] + calculate(W-B[i],B,C,dp)
            if min_cost==0 or min_cost>value:
                min_cost = value
    dp[W] = min_cost
    return min_cost 
def sort(B,C):
    n = len(B)
    for i in range(n-1):
        for j  in range(n-i-1):
            if B[j]>B[j+1]:
                B[j],B[j+1]= B[j+1],B[j]
                C[j],C[j+1] = C[j+1],C[j]
                
def solve2(A,B,C):
    max_of_A = max(A)
    n = len(B)
    dp= [ [0]*(max_of_A + 1) for i in range(n)]
    sort(B,C)
    for j in range(1,max_of_A + 1):
        dp[0][j]= dp[0][j-B[0]] + C[0]
        
    for i in range(1,len(B)):
        for j in range(1,max_of_A + 1):
            if B[i]>j:
                dp[i][j]=dp[i-1][j]
            else:
                dp[i][j] = min(dp[i][j-B[i]]+C[i], dp[i-1][j])
    cost  = 0            
    for x in A:
        cost += dp[-1][x]
    for i in range(n):
        print(*dp[i])
    return cost    
#Driver Code 
A = list(map(int,input().split()))
B = list(map(int,input().split()))
C = list(map(int,input().split()))
ans1 = solve(A,B,C)
ans2 = solve2(A,B,C)
print(ans1,ans2)