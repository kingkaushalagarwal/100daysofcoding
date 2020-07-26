#based on question find maximum area under histogram stack based solution.
class Solution:
    # @param A : list of list of integers
    # @return an integer
    def findMaxArea(self, arr):
        stack = [];
        maxarea = 0;
        n = len(arr)

        for i in range(len(arr)):
            x = arr[i]
            if len(stack) == 0 or arr[stack[-1]] <= arr[i]:
                stack.append(i)
            else:
                while len(stack) != 0 and arr[stack[-1]] > arr[i]:
                    height = arr[stack.pop()]  # top element of array
                    if len(stack) == 0:
                        length = i
                    else:
                        length = (i - stack[-1] - 1)
                    area = height * length
                    maxarea = max(maxarea, area)
                stack.append(i)

        while len(stack) != 0:
            height = arr[stack.pop()]
            if len(stack) == 0:
                length = n
            else:
                length = (n - stack[-1] - 1)
            area = height * length
            maxarea = max(maxarea, area)
        return maxarea

    def maximalRectangle(self, A):
        arr = A[0];
        maxarea = self.findMaxArea(A[0])

        for i in range(1, len(A)):
            for j in range(len(A[0])):
                if A[i][j] == 0:
                    arr[j] = 0
                else:
                    arr[j] += 1
            maxarea = max(maxarea, self.findMaxArea(arr))
        return maxarea
