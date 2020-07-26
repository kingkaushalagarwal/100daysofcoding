
# def find(arr,i,mul1,mul2):
#     if i<0:
#          n=2 * 10 ** 18
#          if mul1<=n and mul2<=n:
#              return [mul1,mul2]
#          return None
#
#     a = find(arr,i-1,mul1*arr[i],mul2)
#     if a!=None:
#         return a
#     b = find(arr,i-1,mul1,mul2*arr[i])
#     if b!=None:
#         return b
#
# arr= [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97 ]
# mul=1
# mul1=1;mul2=1
# for i in range(len(arr)):
#     if mul1*arr[i]<2*10**18:
#         mul1 = mul1*arr[i]
#     else:
#         mul2 = mul2*arr[i]
#
# print(mul1,len(str(mul1)))
# print(mul2,len(str(mul2)))
# print(find(arr,len(arr)-1,1,1))
# from testInput import input
from collections import defaultdict,deque
class Tree:
    def __init__(self):
        self.tree = defaultdict(list)
    def add(self,u,v):
        self.tree[u].append(v)
        self.tree[v].append(u)
    def bfs(self,p1,p2,n):
        visited = [False] * (n + 1)
        source = 1
        ans = [0] * n
        count = 0
        queue = deque()
        queue.append([source,0])
        # print(n)
        # return ans

        while len(queue)!=0:
            ind,val = queue.popleft()
            visited[ind]=True
            if val==1:
                ans[ind-1]=p1
            else:
                ans[ind-1]=p2
            for x in self.tree[ind]:
                if visited[x]==False:
                    if val==1:
                        queue.append([x,0])
                    else:
                        queue.append([x,1])
        return ans

p1 = 1627168839228008057
p2 =  1416919933790871510
for _ in range(int(input())):
    T = Tree()
    n = int(input())
    for i in range(1,n):
        u,v = map(int,input().split())
        T.add(u,v)
    ans = T.bfs(p1,p2,n)
    print(*ans)