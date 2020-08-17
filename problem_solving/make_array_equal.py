from collections import defaultdict
class Solution:
    # @param A : list of integers
    # @param B : list of integers
    # @return an integer
    def solve(self, A, B):
        n = len(B)
        d = defaultdict(int)
        rotation = defaultdict(int)
        for i in range(n):
            d[B[i]] = i
        for i in range(n):
            if A[i] in d:
                val  = (d[A[i]]-i+n)%n
                rotation[val] +=1
        minn= float('inf')
        for k,v in rotation.items():
            minn = min(minn,n-v+k)
        return minn