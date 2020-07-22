from testInput import input
def find(arr,summ,k,m,i):
    if k==0:
        return summ
    if i<0:
        return -1
    a = find(arr,summ+arr[i]*(k%m),k-1,m,i-1)
    b =find(arr,summ,k,m,i-1)
    return max(a,b)
n,k,m = map(int,input().split())
arr = list(map(int,input().split()))
dp =[[0]*(n+1) for i in range(2)]
for i in range(1,k+1):
    for j in range(i,n+1):
        if i==j:
            dp[i&1][j]=dp[(i-1)&1][j-1] + (arr[j-1]* (i%m))
        else:
            dp[i&1][j] = max(dp[i&1][j-1],dp[(i-1)&1][j-1] + (arr[j-1]* (i%m)))

print(dp[k&1][-1])