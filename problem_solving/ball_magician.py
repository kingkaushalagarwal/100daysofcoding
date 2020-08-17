class Solution:
    # @param A : list of integers
    # @return a list of integers
    def solve(self, A):
        A.sort()
        i, n, low = 0, len(A), len(A)
        high = max(A[-1] - n + 2 - A[1], A[-2] - A[0] - n + 2)
        for j in range(n):
            while A[j] - A[i] >= n: i += 1
            if j - i + 1 == n - 1 and A[j] - A[i] == n - 2:
                low = min(low, 2)
            else:
                low = min(low, n - (j - i + 1))
        return [low, high]

arr= [ 8, 7, 6, 5, 11 ]
# ans = largestWindow(arr)
ans = Solution().solve(arr)
print(ans)