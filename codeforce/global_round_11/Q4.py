# from testInput import input
from collections import defaultdict
class Graph:
    def __init__(self,V):
        self.graph =defaultdict(list)
        self.V = V
    def add(self,u,v):
        self.graph[u].append(v)
    def dfs(self,s,visited,c,maxx):
        visited[s]=True
        c+=1
        maxx[0] = max(maxx[0],c)
        for x in self.graph[s]:
            if visited[x]==False:
                self.dfs(x,visited,c,maxx)
        visited[s]=False
    def dfs1(self,s,visited,dp):
        if dp[s]!=-1:
            return dp[s]
        visited[s]=True
        ans = 0
        for x in self.graph[s]:
            if visited[x]==False:
                c= self.dfs1(x,visited,dp)
                ans = max(ans,c)
        visited[s]=False
        ans +=1
        dp[s]=ans
        return ans

    def find(self):
        visited =[False]*self.V
        dp = [-1]*self.V
        ans = 0
        for x in self.graph[0]:
            if visited[x]==False:
                maxx = [0]
                self.dfs1(x,visited,dp)

        return max(dp)

r,n = map(int,input().split())
array =[[0,1,1]]
for i in range(n):
    array.append(list(map(int,input().split())))
array.sort()
G = Graph(n+1)
for i in range(len(array)):
    for j in range(i+1,len(array)):
        t1,x1,y1=array[i]
        t2,x2,y2=array[j]
        #possible move
        if (t1+abs(x1-x2)+abs(y1-y2))<=t2:
                G.add(i,j)
if 0 not in G.graph:
    print(0)
else:
    ans = G.find()
    print(ans)
