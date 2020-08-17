#partition array such that product of both parts is maximum
#recursion knapsack
def knapsack(A,W,i):
    if i<0:
        return 0
    if W==0:
        return 0
    a = knapsack(A,W,i-1)
    b = 0
    if A[i]<=W:
        b= knapsack(A, W - A[i], i - 1)+A[i]
    return max(a,b)

#dp knapsack
def knapsackdp(A,W):
    n = len(A)
    dp = [[0]*(W+1) for i in range(n+1)]
    for i in range(1,n+1):
        for j in range(1,W+1):
            a = 0; b=0
            if j>=A[i-1]:
                a = dp[i-1][j-A[i-1]] + A[i-1]
            b = dp[i-1][j]
            dp[i][j] = max(a,b)
    return dp[-1][-1]
def solve(A):
    summ = sum(A)
    W = summ//2
    n =  len(A)
    # part1 = knapsack(A,W,n-1)
    part1 = knapsackdp(A,W)
    part2 = summ - part1
    return part1*part2

#finding all possible numbers which is constructed given array numbers and then finding maximum using condition
class Solution:
    # @param A : list of integers
    # @return an integer
    def solve(self, A):
        summ = sum(A)
        n =  len(A)
        dp =[False]*(summ+1)
        dp[0]= True
        for x in A:
            for i in range(summ,x-1,-1):
                if i>=x and dp[i-x]==True:
                    dp[i] = True
            dp[x]=True
        maxx = float('-inf')
        for i in range(summ+1):
            maxx = max(maxx,i*(summ- i))
        return maxx

A = [1, 3,7,1]
solve(A)