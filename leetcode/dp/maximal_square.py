class Solution:
    def maximalSquare(self, arr) :
        if len(arr) == 0:
            return 0
        n = len(arr)
        m = len(arr[0])

        maxx = 0
        for i in range(n):
            for j in range(m):
                arr[i][j] = int(arr[i][j])
                if i == 0 or j == 0:
                    maxx = max(maxx, arr[i][j])
                    continue
                if arr[i][j] == 1:
                    arr[i][j] = min(arr[i - 1][j], arr[i][j - 1],arr[i-1][j-1]) + 1
                maxx = max(arr[i][j], maxx)
        for i in range(n):
            print(arr[i])
        return maxx ** 2
arr =[["1","0","1","0"],["1","0","1","1"],["1","0","1","1"],["1","1","1","1"]]
ans = Solution().maximalSquare(arr)
print(ans)