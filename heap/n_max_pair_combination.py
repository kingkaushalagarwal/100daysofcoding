#InterviewBit
import heapq
class Solution:
    # @param A : list of integers
    # @param B : list of integers
    # @return a list of integers
    def solve(self, A, B):
        n = len(A)
        A.sort()
        B.sort()
        A = A[::-1]
        B = B[::-1]
        summ = A[0] + B[0]
        pq = [[-summ, 0, 0]]
        heapq.heapify(pq)
        ans = []
        d = {}
        d[(0, 0)] = 1
        while n > 0:
            val, i, j = heapq.heappop(pq)
            ans.append(-val)
            if i + 1 < len(A) and ((i + 1, j) not in d):
                heapq.heappush(pq, [-(A[i + 1] + B[j]), i + 1, j])
                d[(i + 1, j)] = 1
            if j + 1 < len(B) and ((i, j + 1) not in d):
                heapq.heappush(pq, [-(A[i] + B[j + 1]), i, j + 1])
                d[(i, j + 1)] = 1
            n -= 1
        return ans
