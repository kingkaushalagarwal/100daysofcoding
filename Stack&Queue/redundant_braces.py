class Solution:
	# @param A : string
	# @return an integer
	def braces(self, A):
            stack =[]
            for x in A:
                print(stack)
                if x!=')':
                    stack.append(x)
                else:
                    flag = False
                    while len(stack)!=0 and stack[-1]!='(':
                        flag = True
                        stack.pop()
                    print(stack)
                    if flag==False:
                        return 1
                    elif len(stack)!=0:
                        stack.pop()
            return  0

A = "(a+(a+b))"
ans  = Solution().braces(A)
print(ans)