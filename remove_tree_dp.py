#interview Bit important question
from testInput import input
from sys import maxsize
class Solution:
    # @param A : list of integers
    # @return an integer
    def solve(self, A):
        def find(start, end, arr):
            if start > end:
                return 0
            minn = maxsize

            for i in range(start, end + 1):
                temp = find(start, i - 1, arr) + find(i + 1, end, arr) + arr[start - 1] * arr[i] * arr[end + 1]
                minn = min(minn, temp)
            return minn

    def findMemoization(arr):
        dp = [[0] * len(arr) for i in range(len(arr))]
        for l in range(len(arr) - 1):
            for m in range(1, len(arr) - l - 1):
                i = m;
                j = m + l
                if i == j:
                    dp[i][j] = arr[i - 1] * arr[i] * arr[i + 1]
                else:
                    minn = maxsize
                    for k in range(i, j + 1):
                        temp = dp[i][k - 1] + dp[k + 1][j] + arr[i - 1] * arr[k] * arr[j + 1]
                        minn = min(minn, temp)
                    dp[i][j] = minn

        return dp[1][len(A) - 2]

    return findMemoization(A)
