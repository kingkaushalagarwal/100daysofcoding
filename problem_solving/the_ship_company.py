from heapq import heapify, heappush, heappop


class Solution:
    # @param A : integer
    # @param B : integer
    # @param C : list of integers
    # @return a list of integers
    def solve(self, A, B, C):
        maximum = 0
        minimum = 0
        n = A;
        count = 0
        pq = [x for x in C]
        heapify(pq)
        while n > 0:
            val = heappop(pq)
            count += val
            if val - 1 > 0:
                heappush(pq, val - 1)
            n -= 1
        minimum = count

        n = A;
        count = 0
        pq = [-x for x in C]
        heapify(pq)
        count = 0
        while n > 0:
            val = - heappop(pq)
            count += val
            if val - 1 > 0:
                heappush(pq, -(val - 1))
            n -= 1
        maximum = count
        return [maximum, minimum]

