from collections import deque
class Solution:
    def solve(self,A,B,C,D,E):
        n = len(E)
        m= len(E[0])
        vis = list([0]*(m+1) for i in range(n+1))
        q = deque()
        q.append([0,A-1,B-1])
        vis[A-1][B-1]=1
        while len(q)!=0:
            t = q.popleft()
            d = t[0]
            x = d[1]
            y = d[2]
            if C==x+1 and D==y+1:
                return d
            #move down
            for i in range(x+1,n):
                if E[i][y]=='0' and vis[i][y]==0:
                    vis[i][y]=1
                    q.append([d+1,i,y])
                elif E[i][y]=='1':
                    break
            #move up
            for i in range(x-1,-1,-1):
                if E[i][y]=='0' and vis[i][y]==0:
                    vis[i][y]=1
                    q.append([d+1,i,y])
                elif E[i][y]=='1':
                    break

            # move right
            for i in range(y + 1, m):
                if E[x][i] == '0' and vis[x][i] == 0:
                    vis[x][i] = 1
                    q.append([d + 1, x, i])
                elif E[x][i] == '1':
                    break

            # move left
            for i in range(y - 1, -1, -1):
                if E[x][i] == '0' and vis[x][i] == 0:
                    vis[x][i] = 1;
                    q.append([d + 1, x, i]);
                elif E[x][i] == '1':
                    break

        return -1;