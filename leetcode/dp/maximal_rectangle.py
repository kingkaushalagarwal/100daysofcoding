# 1 2 3 3 4 5
# 2  2  3  4  2
# -1 -1  2  2 -1
class Solution:
    def rightSmallest(self, arr):
        n = len(arr)
        smallest = [-1] * n
        stack = []
        for i in range(n):
            if len(stack) == 0 or arr[stack[-1]] > arr[i]:
                while stack and arr[stack[-1]] > arr[i]:
                    ind = stack.pop()
                    smallest[ind] = i
                stack.append(i)
            else:
                stack.append(i)
        return smallest

    def leftSmallest(self, arr):
        n = len(arr)
        smallest = [-1] * n
        stack = []
        for i in range(n - 1, -1, -1):
            if len(stack) == 0 or arr[stack[-1]] > arr[i]:
                while stack and arr[stack[-1]] > arr[i]:
                    ind = stack.pop()
                    smallest[ind] = i
                stack.append(i)
            else:
                stack.append(i)
        return smallest

    def findmax(self, arr):
        n = len(arr)

        left = self.leftSmallest(arr)
        right = self.rightSmallest(arr)
        print("array: ",arr)
        print("left :",left)
        print("right :",right)
        maxx = max(arr)
        for i in range(n):
            area = 0
            if left[i] == -1 and right[i] == -1:
                area = arr[i] * n
            elif left[i] == -1:
                area = arr[i] * right[i]
            elif right[i] == -1:
                area = arr[i] * (n - left[i] - 1)
            else:
                area = arr[i] * (right[i] - left[i] - 1)
            maxx = max(maxx, area)
        return maxx

    def maximalRectangle(self, arr):
        n = len(arr)
        m = len(arr[0])
        for i in range(m):
            prev = 0
            for j in range(n):
                arr[j][i] = int(arr[j][i])
                if arr[j][i] != 0:
                    arr[j][i] += prev
                prev = arr[j][i]
        for i in range(len(arr)):
            print(arr[i])
        maxx = float('-inf')
        for i in range(n):
            val = self.findmax(arr[i])
            # print(val)
            maxx = max(maxx, val)
        return maxx


arr = [["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]]
ans = Solution().maximalRectangle(arr)
print(ans)