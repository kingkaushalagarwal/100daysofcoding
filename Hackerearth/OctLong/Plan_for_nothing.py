from testInput import input
n = int(input())
array =[]
maxx = 0
for i in range(n):
    l = list(map(int,input().split()))
    maxx = max(maxx,max(l))
    array.append(l)
dp =[0]*(maxx + 2)
for i in range(n):
    m = array[i][0]
    c = 0
    for j in range(m):
        ind = 2*c+1
        l = array[i][ind]
        r = array[i][ind+1]
        dp[l]+=1
        dp[r+1]-=1
        print(i,l,r,dp)
        c+=1
for i in range(1,len(dp)):
    dp[i]+=dp[i-1]
ans =-1
for i in range(1,len(dp)-1):
    if dp[i]==0:
        ans = i
        break
print(ans)
# 4
# 2 1 2 3 5
# 2 1 3 5 7
# 2 1 3 4 5
# 2 3 6 11 12