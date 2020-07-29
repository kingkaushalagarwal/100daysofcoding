from collections import defaultdict
import heapq
from sys import maxsize


class Graph(object):
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
    # @return a list of integers

    def solve(self, A, B, C):
        dist = [maxsize] * A
        dist[C] = 0
        visited = [0] * A
        pq = [[0, C]]
        heapq.heapify(pq)

        G = Graph(A)
        for i in range(len(B)):
            u, v, d = B[i]
            G.add(u, v, d)
        while (len(pq) != 0):
            node = heapq.heappop(pq)
            d = node[0]
            u = node[1]
            visited[u] = 1
            for x in G.graph[u]:
                distance = x[1]
                v = x[0]
                if visited[v] == 0:
                    if dist[u] + distance < dist[v]:
                        dist[v] = dist[u] + distance
                        heapq.heappush(pq, [dist[v], v])
        for i in range(len(dist)):
            if dist[i] == maxsize:
                dist[i] = -1
        return dist



