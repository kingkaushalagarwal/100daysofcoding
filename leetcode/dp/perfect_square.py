from math import sqrt, floor
class Solution:
    def numSquares(self, n: int) -> int:
        if n <= 1:
            return n
        l = floor(sqrt(n))
        dp = list(range(n + 1))
        for i in range(2, l + 1):
            for j in range(i * i, n + 1):
                dp[j] = min(dp[j], dp[j - i * i] + 1)
        print(dp)
        return dp[-1]
n  = int(input())
ans = Solution().numSquares(n)
print(ans)