from testInput import input
from collections import Counter
import gc

def expo(x,n,p):
    if n==0:
        return 1
    elif n==1:
        return x%p
    elif n&1:
        return ((x%p)*expo((x*x)%p,n//2,p)%p)
    else:
        return expo((x*x)%p,n//2,p)%p

def createCombination(combination,n,p):
    combination[n]= [0]*(n+1)
    combination[n][0]=1
    for r in range(n):
        combination[n][r+1] = (combination[n][r]*(n-r)*expo(r+1,p-2,p))%p
    for i in range(1,n+1):
        combination[n][i]+=combination[n][i-1]


#Driver Code
m  = 10**9+ 7
combination = {0:[1]}
for t in range(int(input())):
    n = int(input())
    arr = list(map(int,input().split()))

    answer = [0] * (n + 1)
    keys = sorted(list(set(arr)))
    if len(keys)==n:
        for i in range(1, n + 1):
            answer[i] = expo(2,n-i,m)
        print(*answer[1:])
        continue

    counter = Counter(arr)
    keys = sorted(list(set(arr)))
    freq =[]
    for key in keys:
        value = counter[key]
        freq.append(value)
        if value not in combination:
            createCombination(combination,value,m)

    counter = None
    gc.collect()


    max_freq = max(freq)
    dp =[[0]*len(freq) for i in range(max_freq+1)]
    for i in range(len(freq)):
        dp[0][i]=1

    for i in range(1,max_freq+1):
        for j in range(len(freq)):
            n1 = freq[j]
            r1 = i
            cl = len(combination[n1])
            if r1<cl:
                dp[r1][j] = combination[n1][r1]
            else:
                dp[r1][j] = combination[n1][-1]

    prefix = [[0] * len(freq) for i in range(max_freq + 1)]

    for i in range(len(dp)):
        mul=1
        for j in range(len(dp[0])):
            prefix [i][j] = (mul * dp[i][j])%m
            mul = prefix[i][j]

    suffix = dp
    for i in range(len(dp)):
        mul = 1
        for j in range(len(dp[0])-1,-1,-1):
            suffix[i][j] = (mul*dp[i][j])%m
            mul = suffix[i][j]

    for i in range(len(freq)):
        n1 = freq[i]
        summ =0
        for j in range(1,n1+1):
            if i==0:
                summ+= ( (combination[n1][j] - combination[n1][j - 1]) * suffix[j][i + 1])%m
            elif i==(len(freq)-1):
                summ+= (prefix[j-1][i - 1] * (combination[n1][j] - combination[n1][j - 1]))%m
            else:
                summ+=(prefix[j-1][i-1]*(combination[n1][j]-combination[n1][j-1])*suffix[j][i+1] )%m
        answer[keys[i]]=summ%m

    print(*answer[1:])
    del freq
    del answer
    del suffix
    del prefix
    del keys
    gc.collect()