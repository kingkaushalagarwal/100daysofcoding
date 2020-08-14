class Solution:
	# @param A : tuple of integers
	# @return an integer
	def trap(self, A):
            n =len(A)
            prefix=[0]*n
            suffix=[0]*n
            prefix[0]=A[0]
            suffix[-1]=A[-1]
            for i in range(1,n):
                prefix[i] = max(A[i],prefix[i-1])
            for i in range(n-2,-1,-1):
                suffix[i] = max(A[i],suffix[i+1])
            area =0
            for i in range(n):
                area +=min(prefix[i],suffix[i])-A[i]
            return area