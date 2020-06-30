#InterviewBit
#Distance of nearest cell
from collections import deque
class Solution:
    # @param A : list of list of integers
    # @return a list of list of integers
    def check(self,nr,nc,n,m):
        return nr<n and nc<m and nr>=0 and nc>=0
    def solve(self, A):
        n = len(A)
        m = len(A[0])
        queue = deque()
        for i in range(n):
            for j in range(m):
                if A[i][j]==1:
                    A[i][j]='X'
                    queue.append([i,j])
        row = [1,-1,0,0]
        col = [0,0,1,-1]
        while len(queue)!=0:
            node = queue.popleft()
            r = node[0]
            c = node[1]
            for k in range(4):
                nr = r + row[k]
                nc = c + col[k]
                if self.check(nr,nc,n,m) and A[nr][nc]==0:
                    if A[r][c]=='X':
                        A[nr][nc]=1
                    else:
                        A[nr][nc] = A[r][c] + 1
                    queue.append([nr,nc])    
        for i in range(n):
            for j in range(m):
                if A[i][j]=='X':
                    A[i][j]=0
        return A            
                        
            
            
            
            
            