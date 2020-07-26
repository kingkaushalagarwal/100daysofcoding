#interview Bit
class Solution:
    # @param A : tuple of integers
    # @return an integer
    def maxProfit(self, A):
        if len(A) == 0:
            return 0

        maxxTillnow = A[-1]
        maxx = 0
        for i in range(len(A) - 1, -1, -1):
            maxx = max(maxx, maxxTillnow - A[i])
            maxxTillnow = max(maxxTillnow, A[i])
        return maxx
