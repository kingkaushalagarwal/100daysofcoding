class Solution:
    # @param A : list of integers
    # @return an integer
    def solve(self, arr):
        stack = []
        count = 0
        for i in  range(len(arr)):
            if len(stack)==0:
                stack.append(i)
                if i!=0:
                    count+=1
            else:
                ind =  stack[-1]
                if arr[ind]>arr[i]:
                    stack.append(i)
                    count+=1
                # elif arr[ind]==arr[i]:
                #     continue
                else:
                    prev = i
                    flag = False
                    while stack and arr[stack[-1]] <= arr[i]:
                        ind = stack.pop()
                        if (ind+1)!=prev:
                            count+=1
                        prev = ind
                        flag = True
                    if flag:
                        count+=1
                    stack.append(i)

        if stack:
            prev= stack[-1]
            stack.pop()
        while stack:
            if stack[-1]+1==prev:
                prev = stack.pop()
            else:
                prev = stack.pop()
                count+=1
        return count




A = [ 120, 131, 101, 30, 17, 127, 55, 35, 45, 50, 64, 62, 96, 92, 63, 76, 25, 52, 85, 75 ]
ans  = Solution().solve(A)
print(ans)