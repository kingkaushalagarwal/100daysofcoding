from testInput import input
from collections import defaultdict,deque
class Tree:
    def __init__(self):
        self.tree=defaultdict(list)
    def add(self,u,v):
        self.tree[u].append(v)
        self.tree[v].append(u)

for _ in range(int(input())):
    n,k = map(int,input().split())
    arr = list(map(int,input().split()))
    t= Tree()
    for i in range(n-1):
        u,v= map(int,input().split())
        t.add(u,v)
    # source =1
    visited =[False]*(n+1)
    queue= deque()
    queue.append([1,0])
    maxdis=-1;maxnode=None
    while len(queue)!=0:
        node = queue.popleft()
        val=node[0]
        dis = node[1]
        if maxdis<dis:
            maxdis=dis
            maxnode=val
        visited[val]=True
        for x in t.tree[val]:
            if visited[x]==False:
                queue.append([x,dis+1])
    #important
    maxnode1= maxnode

    visited = [False] * (n + 1)
    maxnode=None
    maxdis=-1
    queue=deque()
    queue.append([maxnode1,0])
    while len(queue)!=0:
        node = queue.popleft()
        val = node[0]
        dis = node[1]
        if maxdis < dis:
            maxdis = dis
            maxnode = val
        visited[val] = True
        for x in t.tree[val]:
            if visited[x] == False:
                queue.append([x, dis + 1])
    distance = maxdis+1
    # print(distance)
    arr.sort()
    arr = arr[::-1]
    summ = 0
    if k==2:
        summ=arr[-1]+arr[-2]
    elif k<=2*distance:
        num=k//2
        for i in range(num):
            summ+=arr[i]*2
        if k&1:
            summ+=arr[num]
    else:
        ps =0
        for i in range(distance):
            ps+=arr[i]
        while k>=distance:
            summ+=ps
            k-=distance
        for q in range(k):
            summ+=arr[q]

    print(str(summ))


    # print(maxnode1,maxnode)