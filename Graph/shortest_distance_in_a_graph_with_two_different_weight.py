#InterviewBit question
#for finding shortest distance between two nodes in unweighted graph we are using bfs
#for finding shortest distance between two nodes in weighted graph we are using dijkastra
#for finding shortest distance between tow nodes in weighted graph having atmost k-weigh at particular edge we are using k*V queues approach
from collections import defaultdict, deque
class Graph:
    def __init__(self, V):
        self.V = V
        self.graph = defaultdict(list)

    def add(self, u, v, d):
        self.graph[u].append([v, d])
        self.graph[v].append([u, d])


class Solution:
    # @param A : integer
    # @param B : list of list of integers
    # @param C : integer
    # @param D : integer
    # @return an integer
    def solve(self, A, B, C, D):
        G = Graph(A)
        for x in B:
            u, v, d = x
            G.add(u, v, d)
        queue = deque()
        arr = [deque() for i in range(2 * A + 1)]
        arr[0].append([C, 0])
        i = 0
        visited = [0] * A
        ans = -1
        while True:
            while i < len(arr) and len(arr[i]) == 0:
                i += 1
            if i == len(arr):
                break
            u, distance = arr[i].popleft()
            if u == D:
                ans = distance
                break
            visited[u] = 1
            for x in G.graph[u]:
                v, d = x
                if visited[v] == 0:
                    new_distance = distance + d
                    arr[new_distance].append([v, new_distance])
        return ans

