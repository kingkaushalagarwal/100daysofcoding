#Interview Bit
from sys import maxsize
import heapq
class Solution:
	# @param A : list of integers
	# @param B : integer
	# @return an integer
    def solve(self, A, B):
        pq =[]
        for i in range(len(A)):
            pq.append([A[i]*2,i])
        heapq.heapify(pq)
        maxx =max(A)
        while B>0:
            node,i = heapq.heappop(pq)
            maxx = max(maxx,node)
            heapq.heappush(pq,[node+A[i],i])
            B-=1
        return maxx