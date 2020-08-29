class Solution:
    def lengthOfLIS(self, nums) -> int:
        if len(nums)==0:
            return 0
        n = len(nums)
        dp = [0]*n
        length =0
        for i in  range(1,n):
            if nums[i]>nums[dp[length]]:
                dp[length+1]=i
                length+=1
            elif nums[i]<=nums[dp[0]]:
                dp[0]=i
            else:
                l=1;h=length-1
                while l<=h:
                    mid = (l+h)//2
                    ind = dp[mid]
                    if nums[i]>nums[ind]:
                        l = mid+1
                    elif nums[i]<=nums[ind]:
                        h = mid-1
                dp[l]=i
        return length+1

nums= [5,4,10,4,3,8,9]
ans = Solution().lengthOfLIS(nums)
print(ans)
A =(1,3)
print(A)
A = A+(1,)
print(A)
