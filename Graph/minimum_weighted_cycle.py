#Minimum weighted cycle in an undirected graph

import sys
import heapq
from collections import defaultdict


class Graph:
    def __init__(self, N):
        self.graph = defaultdict(list)
        self.size = N

    def add(self, u, v, w):
        self.graph[u].append([v, w])
        self.graph[v].append([u, w])

    def dfs(self, source, s, visited, distance, flag, minn, parent):
        if flag == False and s == source:
            minn[0] = min(minn[0], distance)

        visited[s] = True
        if flag:
            visited[s] = False
            flag = False
        for x in self.graph[s]:
            v, d = x[0], x[1]
            # print(v,s)
            if v == parent:
                continue
            if visited[v] == False:
                self.dfs(source, v, visited, distance + d, flag, minn, s)
        visited[s] = False

    def findMinWeightCycle(self):
        minn = [sys.maxsize]
        for source in range(1, self.size + 1):
            visited = [False] * (self.size + 1)
            self.dfs(source, source, visited, 0, True, minn, None)

        if minn[0] == sys.maxsize:
            return -1
        else:
            return minn[0]


class Solution:
    # @param A : integer
    # @param B : list of list of integers
    # @return an integer
    def solve(self, A, B):
        G = Graph(A)
        for i in range(len(B)):
            u, v, w = B[i]
            G.add(u, v, w)
        return G.findMinWeightCycle()

