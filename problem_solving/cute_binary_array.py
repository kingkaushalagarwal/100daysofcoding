class Solution:
    # @param A : list of integers
    # @param B : list of integers
    # @return an integer
    def solve(self, A, B):
        i = 0;
        j = 0
        n = len(A);
        m = len(B)
        stack = []
        end = max(max(A), max(B))
        # print(A,B)
        A.sort()
        B.sort()
        while i < n and j < m:
            # print(stack,i,j)
            if A[i] < B[j]:
                if len(stack) == 0:
                    stack.append([i, 0])
                else:
                    t = stack[-1][1]
                    if t == 1:
                        stack.pop()
                    else:
                        stack.append([i, 0])
                i += 1
            elif A[i] > B[j]:
                if len(stack) == 0:
                    stack.append([j, 1])
                else:

                    t = stack[-1][1]
                    if t == 0:
                        stack.pop()
                    else:
                        stack.append([j, 1])
                j+=1
        while i<n:
            if len(stack) == 0:
                stack.append([i, 0])
            else:
                t = stack[-1][1]
                if t == 1:
                    stack.pop()
                else:
                    stack.append([i, 0])
            i += 1
        while  j<m:
            if len(stack) == 0:
                stack.append([j, 0])
            else:
                t= stack[-1][1]
                if t == 0:
                    stack.pop()
                else:
                    stack.append([j, 1])
            j+=1
        # print(stack)
        # print(A[stack[-1][0]]-min(min(A), min(B)))
        # print(A[stack[-1][0]])
        if len(stack)==0:
            ans = max(max(A),max(B)) - min(min(A),min(B))
        else:
            if stack[-1][1]==1:
                length =0
                while len(stack)!=0:
                    length = max(length, end -  B[stack[-1][0]]-1)
                    end = B[stack[-1][0]]
                    stack.pop()
                length = max(length,end -  min(min(A),min(B)))
                ans = length
            else:
                if len(stack)%2==0:
                    ans = max(max(A), max(B)) - min(min(A), min(B))
                else:
                    length =0
                    while len(stack)>2:
                        length = max(length,end-A[stack[-2][0]]-1)
                        end = A[stack[-1][0]]
                        stack.pop()
                    # print(end)
                    length = max(length,end - min(min(A),min(B))-1)
                    # ans = max(A[stack[-1][0]]-min(min(A), min(B)),end - A[stack[0][0]]-1)
                    ans = length
        return ans
A = [1, 5, 10]
B = [2]
ans  = Solution().solve(A,B)
print(ans)
print(max(max([1,2,3,4]),max([3,5,6,7])))
n=9
print('{:0>{}}'.format(10,n))
print(bin(10))
print(1<<2)