from heapq import heapify, heappush, heappop


class Solution:
    def nthUglyNumber(self, n: int) -> int:
        if n <= 1:
            return 1
        pq = [2, 3, 5]
        count = 1
        store = set([2,3,5])
        while len(pq) != 0:
            node = heappop(pq)
            count += 1
            print(count,node)
            if count == n:
                return node
            else:
                if node*2 not in store:
                    heappush(pq, node * 2)
                    store.add(node*2)
                if node * 3 not in store:
                    store.add(node * 3)
                    heappush(pq, node * 3)
                if node * 5 not in store:
                    store.add(node * 5)
                    heappush(pq, node * 5)

n = int(input())
ans = Solution().nthUglyNumber(n)
print(ans)