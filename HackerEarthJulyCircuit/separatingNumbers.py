# from collections import defaultdict
from testInput import input
from collections import defaultdict, deque


# from testInput import input

class Tree:
    def __init__(self, N):
        self.tree = defaultdict(list)
        self.N = N

    def add(self, u, v):
        self.tree[u].append(v)
        self.tree[v].append(u)

    def remove(self, u, v):
        self.tree[u].remove(v)
        self.tree[v].remove(u)

    def count(self, u, v, arr):
        visited = [False] * (N + 1)
        C1 = defaultdict(int)
        C2 = defaultdict(int)
        visited[u] = True
        queue = deque()
        queue.append(u)
        while len(queue) != 0:
            node = queue.popleft()
            visited[node] = True
            C1[arr[node]] += 1
            for x in self.tree[node]:
                if visited[x] == False:
                    queue.append(x)
        queue = deque()
        queue.append(v)
        while len(queue) != 0:
            node = queue.popleft()
            visited[node] = True
            C2[arr[node]] += 1
            for x in self.tree[node]:
                if visited[x] == False:
                    queue.append(x)
        num = 0
        for k in C1.keys():
            if k in C2.keys():
                num += C1[k] * C2[k]
        return num


N = int(input())
t = Tree(N)
edge = [None]
for _ in range(N - 1):
    u, v = map(int, input().split())
    edge.append([u, v])
    t.add(u, v)
# color array
color = [0] + list(map(int, input().split()))
arr = tuple(map(int, input().split()))
# print(arr)
for x in arr:
    t.remove(edge[x][0], edge[x][1])
    u, v = edge[x]
    ans = t.count(u, v, color)
    print(ans)
