#interveiwBit
class Solution:
    # @param A : list of integers
    # @return an integer
    def solve(self, A):
        ans = [1]*(len(A))
        for i in range(1,len(A)):
            if A[i]>A[i-1]:
                ans[i]=ans[i-1]+1
        for i in range(len(A)-2,-1,-1):
            if A[i]>A[i+1]:
                ans[i]=ans[i+1]+1
        return sum(ans)