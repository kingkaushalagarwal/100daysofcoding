def memoization(k,A,B,summ,d):
    m = 10**9 + 7
    if summ+k*9<B:
        return 0
    #Base condition
    if k==0:
        if summ==B:
            return 1
        else:
            return 0
    if (k,summ) in d:
        return d[(k,summ)]
    #first digit does not equal to zero
    if k==A:
        s =1
    else:
        s=0
    ans =0
    for i in range(s,10):
        if summ+i<=B:
            ans += memoization(k-1,A,B,summ+i,d)%m
    d[(k,summ)]= ans%m
    return ans%m
def tabulation(A,B):
    flag = True
    dp=[ [0]*(B+1) for i in range(A+1) ]
    dp[0][0]=1
    for i in range(1,A+1):
        for j in range(1,B+1):
            for k in range(10):
                if flag:
                    flag = False
                    continue

                if j-k>=0:
                    dp[i][j]+=dp[i-1][j-k]
    return dp[-1][-1]%(10**9+7)
A = 75
B = 22
d = {}
ans1 = memoization(A,A,B,0,d)
ans2 = tabulation(A,B)
print(ans1,ans2)