#number of recent calls
from collections import deque
class RecentCounter:

    def __init__(self):
        self.queue = deque()
        self.num = 0

    def ping(self, t: int) -> int:
        count = 0
        while self.queue and self.queue[0] < (t - 3000):
            count += 1
            self.queue.popleft()
        self.queue.append(t)
        self.num += 1 - count
        return self.num

# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)