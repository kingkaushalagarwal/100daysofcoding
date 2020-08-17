class Solution:
    # @param A : list of integers
    # @param B : list of integers
    # @return an integer
    def solve(self, A, B):
        k = 0
        l = 0
        n = len(A)
        m = len(B)
        c = 0
        while k < 2 * len(A) + 1:
            i = k % n
            j = l % m
            if A[i] == B[j]:
                k += 1
                l += 1
                c += 1
            else:
                k += 1
                c = 0
            if c == m:
                break
        return 1 if c == m else 0

