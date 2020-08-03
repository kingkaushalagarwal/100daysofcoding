import heapq
class Solution:
    # @param A : integer
    # @param B : list of integers
    # @return a list of integers
    def solve(self, A, B):
        if A > len(B):
            return [-1] * len(B)
        ans = []
        for i in range(A - 1):
            ans.append(-1)
        pq = B[:A]
        heapq.heapify(pq)
        for i in range(A, len(B)):
            node = pq[0]
            ans.append(node)
            if B[i]>pq[0]:
                heapq.heappop(pq)
                heapq.heappush(pq, B[i])
        ans.append(heapq.heappop(pq))
        return ans
