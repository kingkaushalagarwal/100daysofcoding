from collections import deque
class Solution:
    # @param A : list of integers
    # @param B : integer
    # @param C : integer
    # @return an integer
    def solve(self, A, B, C):
        count =0
        queue =deque()
        n=  len(A)
        ans =0
        for i in range(len(A)):
            if A[i]%C==0:
                count+=1
            queue.append(i)
            while count==B:
                ans+= n-queue[-1]
                ind = queue.popleft()
                if A[ind]%C==0:
                    count-=1
        return ans