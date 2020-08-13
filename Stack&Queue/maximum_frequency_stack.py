from heapq import heapify, heappop, heappush
from collections import defaultdict
class Solution:
    # @param A : list of list of integers
    # @return a list of integers
    def solve(self, A):
        count = defaultdict(int)
        pq = []
        heapify(pq)
        ans = []
        for i in range(len(A)):
            typeq, val = A[i]
            if typeq == 1:
                count[val] += 1
                heappush(pq, [- count[val], -i,val])
                ans.append(-1)
            elif len(pq) != 0:
                c, ind,val = heappop(pq)
                count[val]-=1
                ans.append(val)
        return ans
A = [ [1, 2],
  [2, 0],
  [1, 2],
  [1, 7],
  [2, 0],
  [2, 0],
  [1, 4],
  [1, 1],
  [1, 7]
]
ans = Solution().solve(A)
print(ans)
print("ABC".lower())