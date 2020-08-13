# from collections import deque
class Solution:
    # @param A : list of integers
    # @return a list of integers
    def solve(self, A):
        if len(A)==0:
            return A
        val = A.pop()
        stack =  self.solve(A)
        stack  = [val] + stack
        return stack
A =[1,2,3,4,5]
ans = Solution().solve(A)
print(ans)