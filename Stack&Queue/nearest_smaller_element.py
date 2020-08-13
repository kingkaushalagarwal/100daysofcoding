class Solution:
	# @param A : list of integers
	# @return a list of integers
	def prevSmaller(self, A):
            stack =[]
            ans =[0]*len(A)
            for  i in range(len(A)-1,-1,-1):
                if len(stack)==0 or A[stack[-1]]<=A[i]:
                    stack.append(i);
                else:
                    print(stack)
                    while len(stack)!=0 and A[stack[-1]]>A[i]:
                        ind = stack.pop()
                        ans[ind] = A[i];
                    stack.append(i)
            while len(stack)!=0:
                ind = stack.pop()
                ans[ind]=-1
            return ans
A = [ 34, 35, 27, 42, 5, 28, 39, 20, 28 ]
ans = Solution().prevSmaller(A)
print(ans)