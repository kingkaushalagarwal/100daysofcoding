#find total number of distinct subsequence of given array
def bruteForceFind(A,i,l,d):
    if i==len(A):
        value=''.join(l)
        if  len(value)!=0  and value not in d:
            d[value] =1
            return 1
        else:
            return 0
    l.append(A[i])
    a = bruteForceFind(A,i+1,l,d)
    l.pop()
    b = bruteForceFind(A,i+1,l,d)
    return a+b

#my solution
def tabulation(A):
    m = 10 ** 9 + 7
    n = len(A)
    last = [-1] * 26
    dp = [0] * (n + 1)
    dp[0] = 0
    dp[1] = 1
    last[ord(A[0]) - 97] = 0
    for i in range(2, n + 1):
        dp[i] = (2 * dp[i - 1] + 1) % m
        index = ord(A[i - 1]) - 97
        if last[index] != -1:
            ind = last[index]
            dp[i] = (dp[i] - dp[ind] - 1) % m
        last[index] = i - 1
    return dp[-1]


#gfg solution
# Python3 program to count number of
# distinct subseqences of a given string

MAX_CHAR = 256
def countSub(ss):
    last = [-1 for i in range(MAX_CHAR + 1)]
    n = len(ss)
    dp = [-2 for i in range(n + 1)]
    dp[0] = 1
    for i in range(1, n + 1):
        dp[i] = 2 * dp[i - 1]
        if last[ord(ss[i - 1])] != -1:
            dp[i] = dp[i] - dp[last[ord(ss[i - 1])]]
        last[ord(ss[i - 1])] = i - 1

    return dp[n]-1
