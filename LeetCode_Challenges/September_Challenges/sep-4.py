#partition problem
#https://leetcode.com/explore/featured/card/september-leetcoding-challenge/554/week-1-september-1st-september-7th/3448/
class Solution:
    def partitionLabels(self, string: str):
        dp = [0] * 26
        for ch in string:
            ind = ord(ch) - 97
            dp[ind] += 1
        count = 0
        ans = []
        d = {}
        for ch in string:
            count += 1
            ind = ord(ch) - 97
            if ch not in d:
                d[ch] = dp[ind]
            d[ch] -= 1
            if d[ch] == 0:
                del d[ch]
            if len(d) == 0:
                ans.append(count)
                count = 0

        return ans