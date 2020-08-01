#InterviewBit
from collections import defaultdict

class Graph:
    def __init__(self, N):
        self.graph = defaultdict(list)
        self.size = N

    def add(self, u, v):
        self.graph[u].append(v)
        self.graph[v].append(u)

    def findUtil(self, s, B, maxx, visited, count):
        visited[s] = True
        c = 0
        for x in self.graph[s]:
            if visited[x] == False:
                value = self.findUtil(x, B, maxx, visited, count)
                if maxx[0] == value:
                    count[0] += 1
                elif maxx[0] < value:
                    maxx[0] = value
                    count[0] = 1
                c = c ^ value

        return B[s] ^ c

    def find(self, s, B):
        visited = [False] * self.size
        maxx = [float('-inf')]
        count = [0]
        value = self.findUtil(0, B, maxx, visited, count)
        if maxx[0] == value:
            count[0] += 1
        elif maxx[0] < value:
            maxx[0] = value
            count[0] = 1
        return [maxx[0], count[0]]


class Solution:
    # @param A : integer
    # @param B : list of integers
    # @param C : list of list of integers
    # @return a list of integers
    def solve(self, A, B, C):
        G = Graph(A)
        for i in range(len(C)):
            u, v = C[i]
            G.add(u, v)
        return G.find(0, B)


