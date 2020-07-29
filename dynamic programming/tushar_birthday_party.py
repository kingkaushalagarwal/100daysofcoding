from sys import maxsize


class Solution:
    # @param A : tuple of integers
    # @param B : tuple of integers
    # @param C : tuple of integers
    def sorting(self, A, B):
        n = len(A)
        for i in range(n - 1):
            for j in range(n - i - 1):
                if A[j] > A[j + 1]:
                    A[j], A[j + 1] = A[j + 1], A[j]
                    B[j], B[j + 1] = B[j + 1], B[j]

    def solve(self, capacity, weight, cost):
        weight = list(weight)
        cost = list(cost)

        self.sorting(weight, cost)
        W = max(capacity)
        n = len(weight)
        dp = [[0] * (W + 1) for i in range(n + 1)]
        dp[0][0] = 0
        for i in range(1, W + 1):
            dp[0][i] = maxsize
        for i in range(1, n + 1):
            for j in range(1, W + 1):
                if (j - weight[i - 1]) >= 0:
                    dp[i][j] = min(cost[i - 1] + dp[i][j - weight[i - 1]], dp[i - 1][j])
                else:
                    dp[i][j] = dp[i - 1][j]

        summ = 0
        for x in capacity:
            summ += dp[n][x]
        return summ

