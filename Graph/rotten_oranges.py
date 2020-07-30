#InterviewBit
#Rotten Oranges

from collections import deque
class Solution:
    # @param A : list of list of integers
    # @return an integer
    def check(self,r,c,n,m):
        return r<n and r>=0 and c<m and c>=0
    def solve(self, A):
        queue = deque()
        n = len(A)
        m = len(A[0])
        for i in range(n):
            for j in range(m):
                if A[i][j]==2:
                    queue.append([i,j])
        
        row = [1,-1,0,0]
        col = [0,0,-1,1]
        while len(queue)!=0:
            node =  queue.popleft()
            r = node[0]
            c = node[1]
            for k in range(4):
                nr = r+row[k]
                nc = c+col[k]
                if self.check(nr,nc,n,m) and A[nr][nc]==1:
                    A[nr][nc]=A[r][c]+1
                    queue.append([nr,nc])
        maxx =-1;flag = False
        for i in range(n):
            for j in range(m):
                if A[i][j]==1:
                    flag = True
                    break
                maxx = max(maxx,A[i][j])
        if flag:
            return -1
        else:
            return maxx-2
                    
                    
        