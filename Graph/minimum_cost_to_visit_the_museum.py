import heapq
class Solution:
    def bruteForce(self,A,B,C,D):
        n = len(A) + 1
        # creating adjacency matrix
        dp = [[float('inf')] * n for i in range(n)]
        for i in range(n):
            dp[i][i] = 0
        for i in range(len(B)):
            u, v, w = B[i], C[i], D[i]
            dp[u][v] = min(dp[u][v], w)
            dp[v][u] = dp[u][v]
        # flyod warshell
        for k in range(1, n):
            for i in range(1, n):
                for j in range(1, n):
                    dp[i][j] = min(dp[i][j], dp[i][k] + dp[k][j])
        for i in range(1, n):
            for j in range(1, n):
                dp[i][j] += A[j - 1]
        ans = []
        for i in range(1, n):
            ans.append(min(dp[i]))
        return ans

    def modifiedDijkastra(self, A, B, C, D):
        cost =[[] for i in range(len(A))]
        adj = [ [] for i in range(len(A))]
        #creating adjacency matrix and cost matrix
        for  i in range(len(B)):
            u,v,w = B[i]-1,C[i]-1,D[i]
            adj[u].append(v)
            adj[v].append(u)
            cost[u].append(w)
            cost[v].append(w)

        #initialization of priority queue i.e. min-heap
        #different from normal dijkastra having single source vertex we are taken all vertex as source vertex
        g =[]
        heapq.heapify(g)
        for i in range(len(A)):
            heapq.heappush(g,[A[i],i])

        while len(g)!=0:
            node = heapq.heappop(g)
            u = node[1]
            for i in range(len(adj[u])):
                v = adj[u][i]
                if cost[u][i]+A[u]<A[v]:
                    A[v]=cost[u][i]+A[u]
                    heapq.heappush(g,[A[v],v])
        return A


    def solve(self, A, B, C, D):
        #time complexity exceeded in case of floyd warshall
        #using floyd_warshall algo
        # value  = self.bruteForce(A,B,C,D)
        ans = []
        ans = self.modifiedDijkastra(A,B,C,D)
        return ans
    #Driver Cod
A = [ 1, 2, 3, 1, 5 ]
B = [ 1, 2, 3, 4 ]
C = [ 2, 3, 4, 5 ]
D = [ 1, 1, 1, 1 ]
ans = Solution().solve(A,B,C,D)
print(ans)