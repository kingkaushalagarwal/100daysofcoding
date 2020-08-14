class Solution:
	# @param A : string
	# @return an integer
	def longestValidParentheses(self, A):
            stack= []
            for i in range(len(A)):
                # print(stack)
                if A[i]=='(':
                    stack.append(i)
                elif A[i]==')':
                    if len(stack)!=0 and A[stack[-1]]=='(':
                        stack.pop()
                    else:
                        stack.append(i)
            print(stack)
            if len(stack)==0:
                return len(A)
            else:
                n = len(stack)
                prev = n
                maxx = float('-inf')
                while len(stack)!=0:
                    x = stack.pop()
                    count = prev - x-1
                    prev = x
                    maxx = max(maxx,count)
                maxx = max(maxx,prev)
                return maxx
A = "(()))((((((())(()))()()(()()())(()(()))(())))((()(((((()()))())(())()()()))((())()())())()"
ans = Solution().longestValidParentheses(A)
print(ans)