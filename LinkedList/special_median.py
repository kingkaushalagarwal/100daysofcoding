from heapq import heappop, heappush
class MinHeap:
    def __init__(self):
        self.heap = []
        self.size = 0

    def push(self, val):
        self.size += 1
        heappush(self.heap, val)

    def pop(self):
        val = None
        if self.size > 0:
            val = heappop(self.heap)
            self.size -= 1
        return val

    def top(self):
        if self.size > 0:
            return self.heap[0]
        return None


class MaxHeap:
    def __init__(self):
        self.heap = []
        self.size = 0

    def push(self, val):
        self.size += 1
        heappush(self.heap, -val)

    def pop(self):
        val = None
        if self.size > 0:
            val = -heappop(self.heap)
            self.size -= 1
        return val

    def top(self):
        if self.size > 0:
            return -self.heap[0]
        return None


class Solution:
    # @param A : list of integers
    # @return an integer
    def solve(self, arr):
        lh = MaxHeap()
        rh = MinHeap()
        lh.push(arr[0])
        median = arr[0]
        for i in range(1, len(arr)):
            if median == arr[i]:
                return 1
            # insert new value in right heap
            if arr[i] > median:
                if rh.size <= lh.size:
                    rh.push(arr[i])
                else:
                    value = rh.pop()
                    lh.push(value)
                    rh.push(arr[i])
            else:
                if lh.size <= rh.size:
                    lh.push(arr[i])
                else:
                    value = lh.pop()
                    rh.push(value)
                    lh.push(arr[i])
            if lh.size == rh.size:
                median = (lh.top() + rh.top()) / 2
            elif lh.size > rh.size:
                median = lh.top()
            elif rh.size > lh.size:
                median = rh.top()

        lh = MaxHeap()
        rh = MinHeap()
        rh.push(arr[-1])
        median = arr[-1]
        for i in range(len(arr) - 2, -1, -1):
            if median == arr[i]:
                return 1
            # insert new value in right heap
            if arr[i] > median:
                if rh.size <= lh.size:
                    rh.push(arr[i])
                else:
                    value = rh.pop()
                    lh.push(value)
                    rh.push(arr[i])
            else:
                if lh.size <= rh.size:
                    lh.push(arr[i])
                else:
                    value = lh.pop()
                    rh.push(value)
                    lh.push(arr[i])
            if lh.size == rh.size:
                median = (lh.top() + rh.top()) / 2
            elif lh.size > rh.size:
                median = lh.top()
            elif rh.size > lh.size:
                median = rh.top()

        return 0

