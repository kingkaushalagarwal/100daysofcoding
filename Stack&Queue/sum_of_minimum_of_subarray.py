def sumSubarrayMins( A):
    res = 0
    s = []
    A = [0] + A + [0]
    for i, x in enumerate(A):
        print(s,res,end=" ")
        while s and A[s[-1]] > x:
            j = s.pop()
            k = s[-1]
            res += A[j] * (i - j) * (j - k)
        s.append(i)
    return res % (10 ** 9 + 7)

A=[3,1,2,4]
ans  = sumSubarrayMins(A)
print(ans)