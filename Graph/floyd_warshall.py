from sys import maxsize
class Solution:
    # @param A : list of list of integers
    # @return a list of list of integers
    def solve(self, A):
        n = len(A)
        for k in range(n):
            for i in range(n):
                for j in range(n):
                    if A[i][k] == -1 or A[k][j] == -1:
                        continue
                    if A[i][j] == -1:
                        A[i][j] = A[i][k] + A[k][j]
                    else:
                        A[i][j] = min(A[i][j], A[i][k] + A[k][j])

        return A
