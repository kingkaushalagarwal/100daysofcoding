#maximum product subarray
#https://leetcode.com/explore/challenge/card/september-leetcoding-challenge/555/week-2-september-8th-september-14th/3456/
class Solution:
    def maxProduct(self, nums) -> int:
        maxx = max(nums)
        prev = nums[0]
        for i in range(1, len(nums)):
            if prev != 0:
                maxx = max(maxx, prev * nums[i])
                prev = prev * nums[i]
            else:
                maxx = max(maxx, nums[i])
                prev = nums[i]
        prev = nums[-1]
        for i in range(len(nums) - 2, -1, -1):
            if prev != 0:
                maxx = max(maxx, prev * nums[i])
                prev = prev * nums[i]
            else:
                maxx = max(maxx, nums[i])
                prev = nums[i]
        return maxx

