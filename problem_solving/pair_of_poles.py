#Interview Bit
#Good question
class Solution:
    # @param A : list of integers
    # @return an integer
    def solve(self, A):
        n = len(A)
        stack =[]
        count =0
        for  i in range(len(A)):
            if len(stack)==0 or A[stack[-1]]>A[i]:
                stack.append(i)
            else:
                if stack[-1]+1==i:
                    stack.pop()
                while stack and A[stack[-1]]==A[i]:
                    stack.pop()
                while stack and A[stack[-1]]<=A[i]:
                    stack.pop()
                    count+=1
                stack.append(i)
        stack =[]
        for i in range(len(A)-1,-1,-1):
            if len(stack)==0 or A[stack[-1]]>A[i]:
                stack.append(i)
            else:
                if stack[-1]-1==i:
                    stack.pop()
                while stack and A[stack[-1]]==A[i]:
                    stack.pop()
                while stack and A[stack[-1]]<=A[i]:
                    stack.pop()
                    count+=1
                stack.append(i)
        prev = A[0]
        for i in range(1,len(A)):
            if prev!=A[i]:
                count+=1
            prev = A[i]
        return count