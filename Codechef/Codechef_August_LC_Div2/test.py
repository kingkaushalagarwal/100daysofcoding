from testInput import input
def findMin(W,weight,freq):
    initial_count = 0
    for v in freq:
        initial_count += (v * (v - 1) * (v - 2)) // 6

    dp =[[0]*(W+1) for i in range(len(freq)+1)]
    for i in range(1,len(freq)+1):
        for j in range(1,W+1):
            if (j-weight[i-1]) >= 0:
                n = freq[i-1]
                c = (j//weight[i-1])-1
                n = n - c
                a = dp[i][j-weight[i-1]] + ((n-1)*(n-2))//2
                b = dp[i - 1][j]
                dp[i][j] = max(a,b)
            else:
                dp[i][j] = dp[i-1][j]
    return initial_count - dp[-1][-1]

for _ in range(int(input())):
    N,C,W = map(int,input().split())
    line=[]
    freq =[0]*(C)
    for i in range(N):
        l = list(map(int, input().split()))
        line.append(l)
        ind = l[2]-1
        freq[ind]+=1
    weight = list(map(int,input().split()))
    ans = findMin(W,weight,freq)
    print(ans)