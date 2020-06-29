#InterviewBit
#Capture Regions on Board
from collections import deque
class Solution:
    # @param A : list of list of chars
    def check(self,nr,nc,n,m):
        return nr<n and nr>=0 and nc<m and nc>=0
    def solve(self, A):
        n = len(A)
        m = len(A[0])
        queue = deque()
        for i in range(n):
            #first column
            if A[i][0]=='O':
                A[i][0]=2
                queue.append([i,0])
            #last column
            if A[i][-1]=='O':
                A[i][m-1]=2
                queue.append([i,m-1])
        
        for j in range(1,m-1):
            #first row
            if A[0][j]=='O':
                A[0][j]=2
                queue.append([0,j])
            #last row
            if A[n-1][j]=='O':
                A[n-1][j]=2
                queue.append([n-1,j])
        row = [1,-1,0,0]
        col = [0,0,1,-1]
        while len(queue)!=0:
            node = queue.popleft()
            r = node[0]
            c = node[1]
            for k in range(4):
                nr = r + row[k]
                nc = c + col[k]
                if self.check(nr,nc,n,m) and A[nr][nc]=='O':
                    A[nr][nc]=2
                    queue.append([nr,nc])
        for i in range(n):
            for j in range(m):
                if A[i][j]=='O':
                    A[i][j]='X'
        for i in range(n):
            for j in range(m):
                if A[i][j]==2:
                    A[i][j]='O'
                
            
                
        
