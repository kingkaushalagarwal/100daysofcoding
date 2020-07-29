import heapq
class Solution:
##using heap and hashing time complexity O(k*logk) where k=D
    def solve1(self, A, B, C, D):
        count = D
        pq = set([A, B, C])
        pq = list(pq)
        ans = []
        heapq.heapify(pq)
        d = dict().fromkeys(set([A, B, C]), 1)
        while len(ans) != count:
            ele = heapq.heappop(pq)
            ans.append(ele)
            if ele * A not in d:
                d[ele * A] = 1
                heapq.heappush(pq, ele * A)
            if ele * B not in d:
                d[ele * B] = 1
                heapq.heappush(pq, ele * B)
            if ele * C not in d:
                d[ele * C] = 1
                heapq.heappush(pq, ele * C)
        return ans

##this is bfs way of solving problem time complexity = O(K)
    def solve2(self, p1, p2, p3, k):
        x = 0
        y = 0
        z = 0
        ans = [0] * (k + 1)
        ans[0] = 1
        for i in range(1, k + 1):
            print(ans,x,y,z)
            temp = min(min(p1 * ans[x], p2 * ans[y]), p3 * ans[z])
            ans[i] = temp
            if (temp == p1 * ans[x]):
                x += 1
            if (temp == p2 * ans[y]):
                y += 1
            if (temp == p3 * ans[z]):
                z += 1
        ans = ans[1:]
        return ans
A=19
B=31
C=31
D= 9
ans = Solution().solve2(A,B,C,D)
print(ans)