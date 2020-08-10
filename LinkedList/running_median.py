from heapq import heapify, heappop, heappush
class MinHeap:
    def __init__(self):
        self.heap = []
        self.size = 0
        heapify(self.heap)

    def push(self, val):
        heappush(self.heap, val)
        self.size += 1

    def pop(self):
        val = None
        if self.size > 0:
            self.size -= 1
            val = heappop(self.heap)
        return val

    def top(self):
        if self.size > 0:
            return self.heap[0]
        return -1


class MaxHeap:
    def __init__(self):
        self.heap = []
        self.size = 0
        heapify(self.heap)

    def push(self, val):
        self.size+=1
        heappush(self.heap, -val)

    def pop(self):
        val = None
        if self.size > 0:
            self.size -= 1
            val = heappop(self.heap)
        return -val

    def top(self):
        if self.size > 0:
            return -self.heap[0]
        return -1


class Solution:
    # @param A : list of integers
    # @return a list of integers
    def solve(self, A):
        lh = MaxHeap()
        rh = MinHeap()
        median = None
        ans = []
        for i in range(len(A)):
            if i == 0:
                lh.push(A[i])
                ans.append(A[i])
                median = A[i]
                continue
            # insert the new value into right heap
            l1 = lh.size
            l2 = rh.size

            if A[i] > median:
                if l2 <= l1:
                    rh.push(A[i])
                else:
                    value = rh.pop()
                    lh.push(value)
                    rh.push(A[i])
            else:
                if l1 <= l2:
                    lh.push(A[i])
                else:
                    value = lh.pop()
                    rh.push(value)
                    lh.push(A[i])
            if lh.size == rh.size:
                ans.append(lh.top())
                median = lh.top()
            elif lh.size > rh.size:
                ans.append(lh.top())
                median = lh.top()
            else:
                ans.append(rh.top())
                median = rh.top()
        return ans


A = [ 32, 91, 86, 8, 4, 100, 98, 15, 79, 32, 4, 99 ]
ans  = Solution().solve(A)
print(*ans)