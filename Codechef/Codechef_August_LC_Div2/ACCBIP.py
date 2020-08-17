from heapq import heappush, heappop,heapify
from testInput import input


def unboundedKnapsack(W, freq, wt):
    n = len(freq)
    dp = [0 for i in range(W + 1)]
    ans = 0
    for i in range(W + 1):
        for j in range(n):
            if (wt[j] <= i):
                c = freq[j]
                dp[i] = max(dp[i], dp[i - wt[j]] + val[j])
    return dp[W]
def findMinTriangelUtil(W,i):
    global weight;
    global freq;
    global d;
    if i < 0:
        return 0
    if (W,i,freq[i]) in d:
        return d[(W,i,freq[i])]


    n = freq[i]
    freq[i]-=1
    a =0;b= 0
    if W>=weight[i]:
        a = findMinTriangelUtil(W-weight[i],i) + ((n-1)*(n-2))//2
    freq[i]+=1

    b = findMinTriangelUtil(W,i-1)
    value =  max(a,b)
    d[(W,i,freq[i])] = value
    return value

def findMin(W,weight,freq):
    initial_count = 0
    for v in freq:
        initial_count += (v * (v - 1) * (v - 2)) // 6
    dp =[[0]*(W+1) for i in range(len(freq)+1)]
    # print(W,cost)
    for i in range(1,len(freq)+1):
        for j in range(1,W+1):
            n = freq[i - 1]
            c = j // weight[i - 1] - 1
            n = n - c
            if (j-weight[i-1]*(c+1))>=0 and n>=3 and c>=0:
                a = dp[i][j-weight[i-1]*1] + ((n-1)*(n-2))//2
                b = dp[i - 1][j]
                dp[i][j] = max(a,b)
            else:
                dp[i][j] = dp[i-1][j]
    # for i in range(len(dp)):
    #     print(dp[i])
    # print("dp :",dp[-1][-1])
    # print("initial_count: ",initial_count)

    return initial_count - dp[-1][-1]

def findMinTriangle(W,weight,freq):
    initial_count =0
    for v in freq:
        initial_count += (v*(v-1)*(v-2))//6
    temp  = findMinTriangelUtil(W,len(freq)-1)
    return initial_count - temp

for _ in range(int(input())):
    N,C,K = map(int,input().split())
    line=[]
    freq =[0]*(C)
    for i in range(N):
        l = list(map(int, input().split()))
        line.append(l)
        ind = l[2]-1
        freq[ind]+=1
    d ={}
    weight = list(map(int,input().split()))
    # ans = findMinTriangle(K , weight,freq)
    ans= findMin(K,weight,freq)
    print(ans)