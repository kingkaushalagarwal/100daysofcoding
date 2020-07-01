#InterviewBit
#Shortest distance in maze 

from collections import deque
class Solution:
	def solve(self,A,B,C):
		srci,srcj = B[0],B[1]
		desi,desj = C[0],C[1]
		q = deque()
		q.append((srci,srcj))
		r,c = len(A),len(A[0])
		res = arr = [ [0]*c for i in range(r)]
		map = {}
		while q:
			node = q.popleft()
			i,j = node[0],node[1]
			if not (node in map):
				map[node] = 1
				d = res[i][j]
				
				k = j
				cd = 0
				
				while k!=c and A[i][k]==0:
					k+=1
					cd+=1
					
				if res[i][k-1]==0 and not(i==srci and k-1==srcj):
					res[i][k-1]=d+cd-1
					q.append((i,k-1))
				k=j 
				cd =0
				while k!=-1 and A[i][k]==0:
					k-=1
					cd+=1
					
				if res[i][k+1]==0 and not(i==srci and k+1==srcj):
					res[i][k+1]=d+cd-1
					q.append((i,k+1))
					
				k = i
				cd = 0
				
				while k!=r and A[k][j]==0:
					k+=1
					cd+=1
					
				if res[k-1][j]==0 and not(k-1==srci and j==srcj):
					res[k-1][j]=d+cd-1
					q.append((k-1,j))
				k=i
				cd =0
				while k!=-1 and A[k][j]==0:
					k-=1
					cd+=1
					
				if res[k+1][j]==0 and not(k+1==srci and j==srcj):
					res[k+1][j]=d+cd-1
					q.append((k+1,j))
					
		if res[desi][desj]==0 : return -1
		return res[desi][desj]
		
					
					
					

				