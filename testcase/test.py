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
def find(root,T,B):
    #in case of leave node
    if len(T.tree[root])==0:
        node = Node()
        node.x1 = B[root-1]
        return node
    arr =[]
    for x in T.tree[root]:
        arr.append(find(x,T,B))
    node = Node()
    node.x1 = B[root-1]
    for y in arr:
        node.x1 += y.x3
        node.x2 += max(y.x1,y.x2)
        node.x3 += max(y.x2,y.x3)
    return node
def solve(A,B):
    T = Tree()
    for i in range(1, len(A)):
        u = A[i]
        v = i + 1
        T.add(u, v)
    ans = find(1, T, B)
    return max(ans.x1,ans.x2,ans.x3)

    # def find(A,B):

# A = [0, 1, 1,2,2,3,3]
# B = [2,5,8,9,11,13,2]
A = [ 0, 1, 1, 1, 3, 3, 6, 6 ]
B = [ 100, 2, 3, 4, 5, 6, 7, 8 ]
# A : [ 0, 1, 1, 1, 3, 3, 6, 6 ]
# B : [ 100, 2, 3, 4, 5, 6, 7, 8 ]
# A = [ 0, 1, 1, 1, 3, 3, 6, 6 ]
# B = [ 1, 2, 3, 4, 5, 100, 7, 8 ]
ans  = solve(A,B)
print(ans)