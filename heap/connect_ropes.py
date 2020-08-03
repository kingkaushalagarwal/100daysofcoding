#InterviewBit
import heapq
class Solution:
    # @param A : list of integers
    # @return an integer
    def solve(self, A):
        heapq.heapify(A)
        cost =0
        while len(A)>1:
            r1 = heapq.heappop(A)
            r2 = heapq.heappop(A)
            heapq.heappush(A,r1+r2)
            cost+=r1+r2
        return cost