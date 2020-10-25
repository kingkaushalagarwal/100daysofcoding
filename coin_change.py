from typing import List
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        if amount == 0:
            return 0

        n = len(coins)
        coins.sort()
        dp = [-1] * (amount + 1)
        for i in range(n):
            dp[0] = 0

        for i in range(n):
            for j in range(amount + 1):
                if j - coins[i] >= 0 and dp[j-coins[i]]!=-1:
                    if dp[j] == -1 :
                        dp[j] = dp[j - coins[i]] + 1
                    else:
                        dp[j] = min(dp[j], dp[j - coins[i]] + 1)
                else:
                    dp[j] = dp[j]
        print(dp)
        return dp[-1]
coins = [2]
amount =3
ans  = Solution().coinChange(coins,amount)

