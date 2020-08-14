class Solution:
    # @param A : list of list of integers
    # @return an integer
    def solve(self, A):
        def justSmallLeft(arr):
            n = len(arr)
            ans = [0] * n
            stack = []
            for i in range(n):
                x = arr[i]
                if len(stack) == 0 or arr[stack[-1]] <= arr[i]:
                    stack.append(i)
                else:
                    while len(stack) != 0 and arr[stack[-1]] > arr[i]:
                        ind = stack.pop()
                        ans[ind] = i
                    stack.append(i)
            while len(stack) != 0:
                ind = stack.pop()
                ans[ind] = -1
            return ans

        def justSmallRight(arr):
            n = len(arr)
            ans = [0] * n
            stack = []
            for i in range(len(arr) - 1, -1, -1):
                if len(stack) == 0 or arr[stack[-1]] <= arr[i]:
                    stack.append(i)
                else:
                    while len(stack) != 0 and arr[stack[-1]] > arr[i]:
                        ind = stack.pop()
                        ans[ind] = i
                    stack.append(i)
            while len(stack) != 0:
                ind = stack.pop()
                ans[ind] = -1
            return ans

        def solve(A):
            n = len(A)
            left = justSmallLeft(A)
            right = justSmallRight(A)
            maxx = float('-inf')
            for i in range(len(A)):
                if left[i] == right[i] == -1:
                    area = n * A[i]
                elif left[i] == -1:
                    area = (n - right[i] - 1) * A[i]
                elif right[i] == -1:
                    area = left[i] * A[i]
                else:
                    area = (left[i] - right[i] - 1) * A[i]
                maxx = max(maxx, area)
            return maxx

        n = len(A)
        m = len(A[0])
        for j in range(m):
            prev = 0
            for i in range(n):
                if prev == 0 or A[i][j] == 0:
                    prev = A[i][j]
                else:
                    A[i][j] += prev
                    prev = A[i][j]
        maxx = float('-inf')
        for i in range(n):
            maxx = max(maxx, solve(A[i]))
        return maxx


A =[[0, 1, 1],
  [1, 0, 0],
  [1, 0, 0],
  [1, 0, 0],
  [1, 0, 0],
  [1, 1, 1],
  [0, 1, 0]]
ans = Solution().solve(A)
print(ans)