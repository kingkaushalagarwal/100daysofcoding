#interviewBit
from math import floor, ceil
import heapq
class Solution:
    def nchoc(self, A, B):
        pq = []
        for i in range(len(B)):
            pq.append(-B[i])
        heapq.heapify(pq)

        chocolates = 0
        while A > 0:
            c = heapq.heappop(pq)
            chocolates += -c
            heapq.heappush(pq, ceil(c / 2))
            A -= 1
        return chocolates % (10 ** 9 + 7)


