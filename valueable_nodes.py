#interview Bit question on tree-dp
from collections import defaultdict, deque
class Tree:
    def __init__(self):
        self.tree = defaultdict(list)

    def add(self, u, v):
        self.tree[u].append(v)

class Node:
    def __init__(self):
        self.x1 = 0
        self.x2 = 0
        self.x3 = 0

class Solution:
    # @param A : list of integers
    # @param B : list of integers
    # @return an integer
    def find(self, root, T, B):
        # in case of leave node
        m = 10 ** 9 + 7
        if len(T.tree[root]) == 0:
            node = Node()
            node.x1 = B[root - 1]
            return node
        arr = []
        for x in T.tree[root]:
            arr.append(self.find(x, T, B))
        node = Node()
        node.x1 = B[root - 1]
        for y in arr:
            node.x1 += y.x3 % m
            node.x2 += max(y.x1, y.x2) % m
            node.x3 += max(y.x2, y.x3) % m
        return node

    def solve(self, A, B):
        T = Tree()
        for i in range(1, len(A)):
            u = A[i]
            v = i + 1
            T.add(u, v)
        ans = self.find(1, T, B)
        m = 10 ** 9 + 7
        return max(ans.x1, ans.x2, ans.x3) % m









