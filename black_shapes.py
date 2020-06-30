#InterviewBit 
#Black Shapes 
#DFS Graph question
class Solution:
	# @param A : list of strings
	# @return an integer
	def check(self,r,c,n,m):
	    return r<n and c<m and r>=0 and c>=0
	def DFS(self,A,i,j,n,m):
	    A[i][j]='M'
	    row = [1,-1,0,0]
	    col = [0,0,1,-1]
	    for k in range(4):
	        r = i + row[k]
	        c = j + col[k]
	        if self.check(r,c,n,m) and A[r][c]=='X':
	            self.DFS(A,r,c,n,m)
	            
	def black(self,arr ):
	    A =[]
	    for x in arr:
	        A.append(list(x))
        n = len(A)
        m = len(A[0])
        count = 0
        for i in range(n):
            for j in range(m):
                if A[i][j]=='X':
                    count += 1
                    self.DFS(A,i,j,n,m)
        return count            
                    