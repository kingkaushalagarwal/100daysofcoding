# from testInput import input
def find(arr,k):
    d= {}
    c =k
    for x in arr:
        if x in d:
            c+=k
            d= {}
        d[x]=1
    return c
def findMin(arr,k):
    n = len(arr)
    freq =[0]*101
    cost =[0]*n
    c = k
    for i in range(n-1,-1,-1):
        x = arr[i]
        freq[x] +=1
        if freq[x]==2:
            c+=2
        elif freq[x]>2:
            c+=1
        cost[i]=c
    d ={}
    final_cost =0
    c=k;
    prev=0;
    for i in range(n):
        x = arr[i]
        if x not in d:
            d[x] =1
        else:
            if cost[prev]>=(c+cost[i]):
                prev = i
                final_cost += c
                c = k
                d = {}
                d[x]=1
            else:
                d[x]+=1
                if d[x]==2:
                    c+=2
                elif d[x]>2:
                    c+=1
    final_cost+=c
    return final_cost

def findCost(arr,k,s,e):
    freq =[0]*101
    for i in range(s,e+1):
        x= arr[i]
        freq[x]+=1
    cost = k
    for x in freq:
        if x>1:
            cost +=x
    return cost


def findMin3(arr,k):
    n = len(arr)
    dp =[ [0]*n  for i in range(n)]
    for i in range(n):
        for j in range(i,n):
            if i==j:
                dp[i][j] = k
            else:
                dp[i][j]= findCost(arr,k,i,j)
    for l in range(2, n + 1):
        for i in range(n - l + 1):
            j = i + l - 1
            cost = dp[i][j]
            for k in range(i,j):
                cost = min(cost,dp[i][k]+dp[k+1][j])
            dp[i][j] = cost
    return dp[0][n-1]

for _ in range(int(input())):
    n, k = map(int, input().split())
    arr = list(map(int, input().split()))
    if n<101:
        ans  = findMin3(arr,k)
    else:
        ans = min(find(arr,k),findMin(arr,k))
    print(ans)