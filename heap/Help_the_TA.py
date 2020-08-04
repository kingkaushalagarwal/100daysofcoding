import heapq
class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return a list of integers
    def solve(self, A, B):
        pq = []
        for i in range(len(A)):
            if A[i]!=0:
                pq.append([-A[i],i])
        heapq.heapify(pq)
        ans =[]
        while B>0 and len(pq)>0:
            node,i = heapq.heappop(pq)
            ans.append(i)
            if (node+1)!=0:
                heapq.heappush(pq,[node+1,i])
            B-=1
        return ans