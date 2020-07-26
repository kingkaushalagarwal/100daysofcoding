import sys
A = [-2, 1, -3, 4, -1, 2, 1, -5, 4]

#Simple implementation gfg's
def maxSubArray( A):
    maxx = A[0]
    curr_summ = A[0]
    for i in range(1, len(A)):
        curr_summ = max(curr_summ + A[i], A[i])
        maxx = max(maxx, curr_summ)

    return maxx

#my implementation
def maxSubArray(A):
    maxx=-sys.maxsize
    curr_summ= None
    for i in range(len(A)):
        if curr_summ==None:
            curr_summ = A[i]
        else:
            if curr_summ<0 and A[i]>0:
                curr_summ = A[i]
            else:
                if curr_summ+A[i]>curr_summ or curr_summ+A[i]>0:
                    curr_summ += A[i]
                else:
                    curr_summ = A[i]
        # print(i,curr_summ)
        maxx = max(maxx,curr_summ)
    return maxx

