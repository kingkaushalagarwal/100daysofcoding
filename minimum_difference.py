#InterviewBit
#Minimum Difference 
from sys import maxsize
# from math import abs
class Solution:
    # @param A : integer
    # @param B : integer
    # @param C : list of list of integers
    # @return an integer
    def solve(self, A, B, C):
        for i in range(A):
            C[i].sort()
        flag = False;
        # ans = float('inf')
        ans = maxsize
        for k in range(A-1):
            i=0;j=0
            while i<B and j<B:
                x = C[k][i]
                y = C[k+1][j]
                ans = min(abs(x-y),ans)
                if (x-y)>0:
                    j+=1
                elif (x-y)<0:
                    i+=1
                else:
                    flag = True
                    break
        if flag:
            return 0
        return ans    
            