class Solution:
    668
    def findNumberOfLIS(self, nums) -> int:
        n = len(nums)
        if n==0:
            return 0
        if n==1:
            return 1
        length =1
        ans = n
        dp = [1]*n
        for i in range(n):
            for j in range(i):
                if nums[i]>nums[j] and dp[i]<(dp[j]+1):
                        dp[i]=dp[j]+1
        print(dp)
        return ans
arr=[1,2,3,1,2,3]
ans = Solution().findNumberOfLIS(arr)
print()

