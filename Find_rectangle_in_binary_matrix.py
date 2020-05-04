#Interview Bit question
#Find rectangle in binary matrix
from collections import defaultdict
class Solution:
    # @param A : tuple of list of integers
    # @return an integer
    def solve(self, A):
        row = defaultdict(set)
        col = defaultdict(set)
        for i in range(len(A)):
            x = A[i]
            for j in  range(len(x)):
                if A[i][j]==1:
                    row[i].add(j)
                    col[j].add(i)
        for k1,v1 in col.items():
            if len(v1)>=2:
                for k2,v2 in col.items():
                    if k1!=k2 and len(v2)>=2 and len(v1.intersection(v2))>=2:
                        return 1
        return  0 